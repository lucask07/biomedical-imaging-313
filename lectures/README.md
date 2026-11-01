# Medical Imaging lectures

These draft decks assume 65-minute classes. Each has an editable Markdown source and a compiled PDF. The slides introduce imaging vocabulary while reviewing familiar signals-and-systems concepts. The system-response deck includes 20 minutes of guided work in the sampling notebook.

| Topic | Source | Slides |
|---|---|---|
| Physical signals and imaging modalities | [Markdown](01_physical_signals_and_modalities.md) | [PDF](01_physical_signals_and_modalities.pdf) |
| Signal theory for images | [Markdown](02_signal_theory.md) | [PDF](02_signal_theory.pdf) |
| System response | [Markdown](03_system_response.md) | [PDF](03_system_response.pdf) |

[Instructor guide](instructor_guide.md) contains timing, discussion responses, and teaching-resource suggestions. Instructor notes also appear in the Markdown inside `::: notes` blocks; the student PDFs omit them. References appear at the end of each deck. Exact textbook sections can be assigned once the edition is specified.

## Preparation covered

The modality deck includes the imaging chain, free-space wavelength and photon energy, and introductory Poisson count statistics and SNR. The signal-theory deck adds angular spatial frequency, two-dimensional Fourier conventions, complex magnitude and phase, and rectangle/sinc and Gaussian transform pairs. The system-response deck connects spatial convolution to frequency multiplication, develops separable Gaussian responses and directional resolution, and explains DC normalization of MTF and finite-pixel contrast loss below Nyquist.

The instructor guide retains 65-minute teaching plans, including a 20-minute guided notebook block in system response. Some existing figures act as reference material when more time is needed for calculation or discussion.

## Edit and rebuild

Edit slide text in the relevant `.md` file. A `##` heading starts a slide. Ordinary Markdown, tables, and `$...$` / `$$...$$` equations compile through Pandoc and Beamer. Keep instructor guidance inside `::: notes` blocks.

Nested bullets use four spaces for each level of indentation:

```markdown
- **Physical signal:** definition.
    - Guiding question or example.
        - Further detail, if needed.
```

Beamer supports three bullet levels. Prefer one or two levels on teaching slides so the hierarchy remains easy to follow.

### Progressive reveals (slide builds)

A line containing three spaced dots, `. . .`, pauses a slide before revealing the following content:

```markdown
## A two-stage slide

First half of the content.

. . .

Second half of the content.
```

The PDF contains two consecutive pages: the first shows the first part, and the second adds the remaining content. Both retain the same slide number. Advance one PDF page to reveal the next build. This works for paragraphs, lists, figures, and equations. Add another pause for another reveal. Builds are opt-in; the current decks do not reveal content in stages unless a pause is added.

See [Pandoc's pause documentation](https://pandoc.org/MANUAL.html#inserting-pauses).

### Compilation

From the repository root, with the scientific Python environment active:

```bash
python lectures/build_slides.py
```

To rebuild one deck:

```bash
python lectures/build_slides.py 03_system_response.md
```

Requirements: Python packages from the repository's `requirements.txt`, Pandoc, and a TeX distribution with XeLaTeX, Beamer, fontspec, and TeX Gyre Heros. On macOS, Pandoc and MacTeX provide the document tools. The script reports missing commands rather than installing software.

`theme.tex` supplies the common 16:9 layout and footer: Medical Imaging on the left, UST ECE, ENGR 313 centered, and slide number on the right. Title pages omit dates and meeting numbers. Keep `date: ""` in the Markdown metadata to prevent automatic date insertion. `generate_figures.py` creates scientific simulation figures in `figures/`; it uses no patient data, network downloads, or randomness. These PDF figures are included for portable rebuilding. Logs, numerical verification, TeX intermediates, and review images belong in ignored `build/lectures/`.

The slides are original drafts informed by the linked teaching resources. No external lecture figures or stock photographs have been copied. The scientific figures are simplified models, not clinical images. No repository license has been selected.
