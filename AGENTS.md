# Project instructions

## Project purpose

Develop and maintain materials for the Fall 2026 Medical Imaging course. 
## Course overview

- 2 credit, half semester for students seeking a biomedical minor. 
- Students have some programming experience but should not assume much.
- Focus is on the engineering and physics of imaging systems not image processing. 
- Primary text is "Medical Imaging: Signals and Systems"  by Jerry L. Prince and Jonathan M. Links

## General expectations

- Preserve existing source files unless explicitly asked to replace them.
- Keep generated files beside their source or in the established output directory.
- Use clear, consistent filenames.
- Do not commit temporary, cache, or intermediate build files.
- Inspect existing materials before introducing a new structure or convention.

## Technical conventions

- Use SI units unless the problem explicitly specifies otherwise.
- Include units in numerical answers.
- Distinguish vectors from scalar magnitudes clearly.
- Use the course's existing notation for fields, coordinates, phasors, and complex quantities.
- State the assumed time convention, such as `e^{jωt}`, when it affects signs.
- Check dimensional consistency and important limiting cases.

## Slides

- Create a consistent format that generates slide source for each day in markdown. 
- Slides should be compiled to a PDF. 

## Exercises 

- Primary exercises will be through iPython notebook using Google CoLab. 
- Students will interpret and complete code, not generate code by themselves. 

## LaTeX and documents

- Follow the formatting conventions in nearby source files.
- Keep reusable commands in the existing preamble or style file.
- Escape LaTeX-sensitive characters in generated text.
- Compile changed LaTeX documents and inspect the resulting PDF.
- Do not leave compilation artifacts unless the project already tracks them.

## Verification

- Recalculate numerical results rather than copying displayed answers blindly.
- Verify signs, coordinate directions, boundary conditions, and unit conversions.
- Report any ambiguous problem statement instead of silently choosing an interpretation.
