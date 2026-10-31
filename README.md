# Biomedical Imaging Interactive Notebooks

Interactive undergraduate labs about the physics and engineering of image formation. Students adjust controls, interpret images and measurements, and answer questions without writing Python.

## Start in Google Colab

1. Open [Google Colab](https://colab.research.google.com/), choose **File → Open notebook → GitHub**, and paste this repository's GitHub URL. Select `notebooks/01_sampling_resolution.ipynb`. Alternatively, upload the notebook through the **Upload** tab.
2. Choose **Runtime → Run all** and allow setup to finish. A CPU runtime is sufficient.
3. Scroll to **Resolution explorer**. Move a slider and release it to update the figures, or select a preset. The code cells are collapsed by default.
4. Record settings and measurements for the five questions at the end. Use **File → Save a copy in Drive** if you want to retain your work.

No repository owner or GitHub URL was supplied, so this README does not contain a fabricated launch link. After publishing, the direct Colab URL has the form `https://colab.research.google.com/github/OWNER/REPOSITORY/blob/main/notebooks/01_sampling_resolution.ipynb` (substitute the real owner, repository, and branch).

## Labs

| Lab | Status | Concepts |
| --- | --- | --- |
| [01 · Sampling and resolution](notebooks/01_sampling_resolution.ipynb) | Available | Gaussian PSF, finite pixel integration, presampling MTF, Nyquist limit, aliasing and phase |
| 02 · Photon noise | Planned | Photon statistics, quantum efficiency and SNR |
| 03 · CT reconstruction | Planned | X-ray projections and reconstruction |
| 04 · MRI k-space | Planned | Fourier encoding and spatial frequency |

Lab 01 takes about 30–45 minutes. It includes an adjustable sinusoidal resolution target, Gaussian blur, detector pixel pitch, target phase, fixed-scale image comparisons, profiles, a PSF cross-section and MTF curves. Presets isolate fine sampling, blur, aliasing, and the Nyquist boundary. Five student questions include a measurement table.

## Scientific model

All lengths refer to one image plane at unit magnification and are in millimeters. The target is an infinite sinusoidal intensity grating cropped to an 8 mm square field. A normalized, isotropic Gaussian PSF acts on intensity; square detector pixels then average over their full area with 100% fill factor. The displayed detector values are normalized intensity averages, not photon counts. There is no noise, clipping, sharpening, or automatic contrast scaling.

The optical response is `exp(-2 π² σ² f²)`; finite pixel width contributes the signed response `sinc(p f)`, where `sinc(u) = sin(πu)/(πu)`. Their product's absolute value is the **presampling** MTF. Sampling at pitch `p` has Nyquist frequency `1/(2p)`; it is a separate operation. A negative aperture response reverses phase. Above Nyquist a visible low-frequency pattern can be an alias, even when the measured contrast is substantial. MTF50 is a first-lobe bandwidth indicator, not a universal smallest resolvable feature size.

Analytic convolution and integration avoid a hidden fine-grid approximation and boundary artifacts. Rendering uses a fine grid only to display continuous images. The simulated target has no random component. Phase-dependent degeneracies at DC and Nyquist are explicitly flagged rather than assigned a misleading fitted contrast. A Gaussian has no finite frequency cutoff, so blur suppresses aliasing rather than guaranteeing its elimination.

## Repository layout

```text
notebooks/01_sampling_resolution.ipynb  Standalone Colab lab
data/README.md                        Data provenance policy
requirements.txt                      Lab dependencies
requirements-dev.txt                  Local verification dependencies
tests/test_sampling_resolution.py     Independent numerical model checks
tools/validate_notebook.py             Fresh-kernel execution and interface checks
```

## Local development and verification

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python tools/validate_notebook.py
```

The validator executes every cell in a fresh Python kernel, exercises presets and boundary settings, and writes an executed notebook and representative dashboard PNGs to ignored `build/`. For local interaction, open the source notebook in a widget-enabled Jupyter frontend. Dependency ranges allow Colab's installed packages; the setup cell prints the actual versions used. Record these versions alongside measurements when comparing runs.

## GitHub and Canvas workflow

Publish this directory as the GitHub repository `biomedical-imaging-labs` (or another chosen name). GitHub holds the authoritative notebooks; Colab copies are working copies. Review notebook changes before merging. Keep committed notebooks free of personal information and bulky execution outputs.

In Canvas, create a module item using **External URL** and paste the direct Colab URL above after substitution. Open in a new tab. Test the link with student-level access; a private repository requires GitHub access for every student. For a stable course offering, replace `main` in the URL with a release tag or commit SHA. Students should save their own copies, record their answers, and submit through your chosen Canvas assignment.

If controls are absent, wait for **Run all** to finish and rerun the last code cell. A static GitHub notebook preview cannot operate widgets. If the runtime disconnects, reconnect and run all cells again. Setup needs network access only when packages must be installed; the lab itself does not download data.

## References

- [J. G. Robertson, *Detector sampling of optical/IR spectra: how many pixels per FWHM?* (2017)](https://arxiv.org/abs/1707.06455): finite pixel size, sampling phase, and why pixels per PSF FWHM is not a universal Nyquist criterion.
- [Jupyter Widgets: Using Interact](https://ipywidgets.readthedocs.io/en/stable/examples/Using%20Interact.html): widget controls and updates on slider release.

The notebook states and derives the particular analytic model used here. No external sample images are included. Choose a repository license before public release; no license choice has been assumed.
