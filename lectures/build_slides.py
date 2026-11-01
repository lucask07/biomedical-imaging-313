"""Compile Markdown decks with Pandoc and XeLaTeX; keep intermediates in build/."""
from pathlib import Path
import re
import shutil
import subprocess
import sys

HERE=Path(__file__).resolve().parent
BUILD=HERE.parent/"build"/"lectures"


def run(command, log_path):
    result=subprocess.run(command,cwd=HERE,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    log_path.write_text(result.stdout)
    if result.returncode:
        print(result.stdout[-7000:])
        raise SystemExit(result.returncode)


def main():
    for program in ["pandoc","xelatex"]:
        if not shutil.which(program):
            raise SystemExit(f"Missing {program}; see lectures/README.md")
    BUILD.mkdir(parents=True,exist_ok=True)
    run([sys.executable,str(HERE/"generate_figures.py")],BUILD/"figures.log")
    paths=[HERE/p for p in sys.argv[1:]] if len(sys.argv)>1 else sorted(HERE.glob("[0-9][0-9]_*.md"))
    for path in paths:
        stem=path.stem
        tex=BUILD/(stem+".tex")
        run(["pandoc",str(path),"--standalone","--to=beamer","--slide-level=2",
             "--include-in-header=theme.tex","--variable=fontsize:20pt",
             "--variable=aspectratio:169","--output="+str(tex)],BUILD/(stem+"-pandoc.log"))
        for iteration in range(2):
            run(["xelatex","-interaction=nonstopmode","-halt-on-error",
                 "-output-directory="+str(BUILD),str(tex)],BUILD/(stem+f"-pass{iteration+1}.log"))
        warnings=re.findall(r"(?:Overfull \\[hv]box)[^\n]*",(BUILD/(stem+".log")).read_text())
        if warnings:
            print(stem+": layout warnings\n"+"\n".join(warnings))
            raise SystemExit("Resolve layout warnings before publishing this PDF")
        output=HERE/(stem+".pdf")
        shutil.copyfile(BUILD/(stem+".pdf"),output)
        print("Compiled",output.name,flush=True)


if __name__=="__main__":
    main()
