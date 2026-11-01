# Imaging fundamentals: instructor guide

These drafts assume students have encountered sinusoids, phase, convolution, Fourier transforms, and the sampling theorem. The purpose is to apply those ideas to image formation. PSF, MTF, contrast, and pixel spacing need explicit introductions because students are encountering their imaging meanings for the first time.

Timing below excludes the final reference slide in each deck. Discussion times include student work and comparison of answers. Plans use topic names because slide builds add PDF pages without changing the frame number. Added material is intended to close prerequisite gaps, while retaining the original discussion and notebook activities.

## Physical signals and imaging modalities

| Time | Focus | Slides / activity |
|---|---|---|
| 0–5 min | Imaging and the consistent modality questions | Opening discussion |
| 5–11 min | Object, measurements, and the complete imaging chain | Camera as the running example |
| 11–24 min | Modality overview and projection | Radiography through PET |
| 24–34 min | Temporal versus spatial frequency; photon calculations | Work one example and check another |
| 34–41 min | Pixel values, repeated counts, and Poisson SNR | Predict the effect of four times the count |
| 41–49 min | Pixel spacing, blur, contrast, and resolution | Interpret the existing image examples |
| 49–60 min | Measurement discussion and modality comparison | Students explain the signal and measurement |
| 60–65 min | Exit questions | Short written or verbal responses |

The goal is to recognize what each modality measures, not to memorize all mechanisms. In the overview, define attenuation as reduction of the primary beam and a transducer as an energy-converting device. Define a radioactive tracer briefly and defer its biology and decay physics.

For the paired comparison:

1. A lower transmitted X-ray signal can indicate greater total attenuation along that path, with incident signal and detector settings fixed. A single projection does not assign the attenuation to a particular depth.
2. A later ultrasound echo corresponds to a longer round-trip propagation time. Converting time to depth requires a sound-speed assumption and knowledge of the beam path.
3. A PET coincidence constrains a line between detectors. A single pair does not determine where along the line the event occurred. Many events allow reconstruction; advanced time-of-flight information is outside today's scope.

If time is short, use the final modality table as a verbal recap. Preserve the imaging-chain distinction, the unit-conversion method, the Poisson model, and the measurement discussion. Keep clinical diagnosis outside this opening lesson.

## Signal theory for images

| Time | Focus | Slides / activity |
|---|---|---|
| 0–5 min | Spatial profiles and units | Opening review |
| 5–14 min | Sinusoids, period, phase, and angular frequency | State the frequency convention explicitly |
| 14–26 min | Components, Fourier coordinates, magnitude and phase | Check a quadrant-II complex number |
| 26–39 min | Rectangle/sinc and Gaussian transform pairs | Sketch both domains and track normalization |
| 39–48 min | Sampling limits in both frequency conventions | Interpret the alias figure |
| 48–60 min | Paired sampling calculation and debrief | Use the existing calculation table |
| 60–65 min | Exit questions and bridge to system response | Short responses |

The Fourier-transform convention uses exp(-j 2 pi f x), with f in cycles/mm. The two-dimensional frequency vector points perpendicular to the stripes. The plotted spectrum of the component example uses one-sided cosine amplitudes and is labeled accordingly; it is not a two-sided Fourier-transform plot.

The sampling calculation gives:

| Quantity | p = 0.20 mm | p = 0.40 mm |
|---|---|---|
| Sampling frequency | 5 samples/mm | 2.5 samples/mm |
| Nyquist frequency | 2.5 cycles/mm | 1.25 cycles/mm |
| Samples per 1.5 cycles/mm period | 3.333 | 1.667 |
| Target below Nyquist? | Yes | No |
| Apparent frequency | 1.5 cycles/mm | 1.0 cycle/mm |

The point-sampling example uses centers at np to keep the alias identity transparent. The notebook instead uses (n + 1/2)p and full pixel-area averaging. The origin changes phase relationships, not the sampling frequency. Explain this distinction if students compare the figures with the notebook.

The two-dimensional frequency image is a qualitative reference if time is short. Preserve the transform conventions, the signed sinc versus magnitude distinction, Gaussian width reciprocity, and the sampling calculation. Students should know which normalization they have chosen before using a transform pair.

## System response

| Time | Focus | Slides / activity |
|---|---|---|
| 0–5 min | PSF and LSI assumptions | Opening prediction |
| 5–13 min | Spatial convolution, G=FH, DC gain, and point responses | Relate the two descriptions of the same model |
| 13–23 min | Gaussian width, separability, and directional resolution | Predict which direction preserves finer detail |
| 23–32 min | Contrast, general MTF normalization, and transfer curves | Distinguish DC gain from contrast transfer |
| 32–40 min | Finite pixel averaging and contrast below Nyquist | Use the quantitative example |
| 40–60 min | Guided notebook comparison | Fine sampling versus Blur limited |
| 60–65 min | Exit questions | Short responses |

Before class, open the notebook and run all cells. Ask students to do the same at the start of class if setup takes time. The notebook block uses only Fine sampling and Blur limited. Frequency is 1 cycle/mm, pixel spacing is 0.10 mm, and phase is 0 degrees. Students predict a change before selecting the second preset.

Checked values for notebook question 1:

| Quantity | Fine sampling | Blur limited |
|---|---|---|
| Sigma (mm) | 0.04 | 0.25 |
| FWHM (mm) | 0.0942 | 0.5887 |
| Combined MTF at 1 cycle/mm | 0.9531 | 0.2864 |
| Predicted contrast at 1 cycle/mm | 0.8577 | 0.2578 |

The exact MTF50 values are calculated by `generate_figures.py` and recorded in `build/lectures/checked_metrics.json`. Students read them from the notebook. The separable Gaussian slide gives the analytic transfer-function method. In class, emphasize the scaling factors, DC-gain check, and directional interpretation rather than a lengthy Gaussian-integral derivation. The additional MTF-versus-Nyquist plot can serve as a reference during the notebook activity.

Students can finish the written response to question 1 after class. The image-quality class can use 20–25 minutes on pixel averaging and aliasing, with remaining required notebook questions completed afterward. Exact-Nyquist phase dependence stays optional.

## Strengthened preparation and teaching checks

- **Imaging chain:** distinguish the source and tissue interaction from collection, detection, reconstruction/processing, display, and perception. Camera examples transfer to other modalities.
- **Photon calculations:** state whether wavelength, temporal frequency, or energy per photon is given or assumed. Convert MHz to Hz and nm to m. A chosen X-ray photon energy approximates a spectrum, not a monochromatic clinical beam.
- **Count statistics:** expected count and one observed count differ. Poisson standard deviation is the square root of the expected count; linear mean-count SNR is dimensionless. Do not substitute a variance where a standard deviation is required.
- **Transform conventions:** positions x,y and frequencies u,v are conjugate coordinates. A spatial period is a repeating length. k_x=2 pi u and k_y=2 pi v express the same pattern in angular units.
- **Rectangle and Gaussian pairs:** track width, gain, and units. The sinc plot has negative lobes, while a centered Gaussian's transform is positive. Widening either spatial function narrows its transform.
- **Complex spectra:** magnitude is the Euclidean norm of the real and imaginary parts; atan2 selects the phase quadrant. Phase is undefined at zero magnitude.
- **System interpretation:** G=FH is the frequency-domain version of spatial convolution. H(0,0) is the integral of h. MTF divides modulation transfer by DC gain. A wider PSF direction corresponds to a narrower frequency response along that coordinate.
- **Sampling versus averaging:** angular and cycles-per-length Nyquist calculations must agree. Finite pixel averaging can reduce contrast below Nyquist; aliasing concerns different continuous patterns producing the same samples.

The added numerical examples are teaching examples, with inputs different from the assessment. Exact homework prompts and answer keys remain outside the public repository.

## Online resources and how to use them

### Michigan: Medical Imaging Systems

[Jeff Fessler's EECS 516 archive](https://web.eecs.umich.edu/~fessler/course/516/index.html) and [Douglas Noll's BME/EECS 516 archive](https://web.eecs.umich.edu/~dnoll/BME516/) organize modalities around physical principles and system models. This is the closest match to the course's emphasis. The material assumes more mathematical depth and a longer course, so use it to inform sequence and examples rather than assign whole lectures. These are archived offerings and some linked materials may move or become unavailable.

### MIT: Biomedical Signal and Image Processing

[HST.582J / 6.555J, Spring 2007](https://ocw.mit.edu/courses/hst-582j-biomedical-signal-and-image-processing-spring-2007/) includes lecture notes and laboratory assignments. Its practice of aligning lectures with hands-on lab activities is useful here. It is a graduate course, uses MATLAB, and places more emphasis on processing than this course. Use the lab structure as inspiration rather than its full workload or programming expectations.

### MIT: Signals and Systems

[RES.6-007 lecture notes](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/pages/lecture-notes/) provide optional prerequisite review. Especially relevant are lecture 4 (convolution), lecture 8 (continuous-time Fourier transform), lecture 16 (sampling), and lecture 17 (interpolation). Translate the time-domain examples into spatial coordinates for the imaging discussion.

### NIH NIBIB: Science Topics

[NIBIB fact sheets](https://www.nibib.nih.gov/science-education/science-topics) offer accessible introductions to X-rays, CT, ultrasound, MRI, and nuclear medicine. These are the best fit for short student previews of unfamiliar modalities. Use the explanations to establish what generates the signal, then develop the engineering model in class.

## Sources and reuse

The primary textbook remains Prince and Links, *Medical Imaging: Signals and Systems*. The drafts reference topics rather than unverified page or chapter numbers. All wording, numerical examples, and scientific plots in the decks are original. The linked courses supply pedagogical inspiration and optional reading, not copied slides. Check the original source's license and figure-specific credits before reusing any third-party visual. NIBIB pages can include externally credited images.
