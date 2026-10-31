"""Run the complete lab in a fresh kernel and exercise actual widget callbacks."""
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
BUILD.mkdir(exist_ok=True)
for name, folder in [("MPLCONFIGDIR", "matplotlib"), ("IPYTHONDIR", "ipython"),
                     ("JUPYTER_RUNTIME_DIR", "runtime")]:
    os.environ[name] = str(BUILD / folder)

import nbformat
from nbclient import NotebookClient
from jupyter_client import AsyncKernelManager
from jupyter_client.kernelspec import KernelSpecManager

kernel_dir = BUILD / "kernels" / "imaging-validation"
kernel_dir.mkdir(parents=True, exist_ok=True)
(kernel_dir / "kernel.json").write_text(json.dumps({
    "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
    "display_name": "Imaging validation", "language": "python"}))
manager = AsyncKernelManager(kernel_name="imaging-validation",
    kernel_spec_manager=KernelSpecManager(kernel_dirs=[str(kernel_dir.parent)]))
path = ROOT / "notebooks/01_sampling_resolution.ipynb"
notebook = nbformat.read(path, as_version=4)
nbformat.validate(notebook)
count = len(notebook.cells)
probe = r'''
from pathlib import Path
build = Path("build")
build.mkdir(exist_ok=True)
for name, params in PRESETS.items():
    set_preset(name)
    assert all(controls[k].value == v for k, v in params.items())
    assert "NYQUIST" in metrics_box.value
    fig = make_dashboard(**params)
    fig.savefig(build / (name.lower().replace(" ", "_") + ".png"), dpi=130)
    plt.close(fig)
# Observe callbacks update metrics, rather than only testing rendering functions.
set_preset("Nyquist boundary")
assert measurements(**{k:w.value for k,w in controls.items()})["sample_range_contrast"] < 1e-12
controls["phase_deg"].value = 90
assert measurements(**{k:w.value for k,w in controls.items()})["sample_range_contrast"] > .5
assert "indeterminate" in metrics_box.value
controls["pitch"].value = .10
assert "BELOW NYQUIST" in metrics_box.value
for params in [dict(f=8, sigma=0, pitch=.5, phase_deg=360),
               dict(f=.25, sigma=.5, pitch=.05, phase_deg=0)]:
    fig = make_dashboard(**params)
    fig.canvas.draw()
    plt.close(fig)
set_preset("Fine sampling")
assert not plt.get_fignums()
print("PASS: all cells, four presets, observer updates, phase degeneracy and control extremes")
'''
notebook.cells.append(nbformat.v4.new_code_cell(probe))
def report_cell(cell, cell_index, **kwargs):
    print(f"Executing cell {cell_index + 1}/{len(notebook.cells)}: "
          f"{cell.source.splitlines()[0][:75]}", flush=True)


NotebookClient(notebook, km=manager, timeout=120, on_cell_start=report_cell,
               resources={"metadata": {"path": str(ROOT)}}).execute(cleanup_kc=True)
for output in notebook.cells[-1].outputs:
    if output.output_type == "stream":
        print(output.text.strip())
notebook.cells = notebook.cells[:count]
nbformat.write(notebook, BUILD / "01_sampling_resolution.executed.ipynb")
print("Execution artifacts:", BUILD)
