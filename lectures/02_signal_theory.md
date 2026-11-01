---
title: "Signal theory for images"
date: ""
---

## Spatial signals

An image can be represented by a function $I(x,y)$.

A line through the image gives a one-dimensional intensity profile, $I(x,y_0)$.

We can apply the same sinusoidal and Fourier descriptions used for time signals, with position replacing time.

::: notes
Five-minute opening: ask for the horizontal-axis units of a temporal signal and an image profile. Prerequisite review, not a new general signals-and-systems course. Source for review structure: MIT RES.6-007, Fourier analysis and sampling lectures.
:::

## A sinusoidal resolution target

![](figures/02_gratings.pdf){width=93%}

One bright-dark pair is one cycle. Increasing spatial frequency brings the stripes closer together.

::: notes
All panels have the same FOV, contrast, phase, and intensity scale. The object is a controlled test pattern rather than anatomy. Frequencies are 0.5, 1, and 2 cycles/mm. Ask students to count cycles before reading the labels.
:::

## Mean, amplitude, and phase

$$I(x)=\overline I+A\cos(2\pi f x+\phi).$$

| Symbol | Meaning | Units in this exercise |
|:---|:---|:---|
| $\overline I$ | Mean intensity | Normalized intensity |
| $A$ | Sinusoidal amplitude | Normalized intensity |
| $f$ | Spatial frequency | Cycles/mm |
| $\phi$ | Phase | Radians in the equation |

The notebook uses $\overline I=0.5$ and $A=0.5C_0$.

::: notes
Normalized intensity is dimensionless. Phase controls translation rather than stripe spacing. The notebook displays phase in degrees, converting to radians internally. Require dimensional consistency: fx must be dimensionless.
:::

## Stripe period

The period is the distance needed for one complete cycle:

$$T_x=\frac{1}{f}.$$

For $f=2$ cycles/mm, $T_x=0.50$ mm.

**Check:** a pattern has three bright-dark pairs across 2 mm. What are its spatial frequency and period?

::: notes
Answer: f=1.5 cycles/mm and period=2/3 mm, approximately 0.667 mm. Emphasize that T_x is a length despite the familiar T notation. It is not a temporal period. Allow two minutes before comparing results.
:::

## Spatial period and frequency conventions

The spatial period $T_x$ can also be written as $\Lambda_x$, uppercase lambda.

$$I(x)=\overline I+A\cos(2\pi u_0x+\phi)
      =\overline I+A\cos(k_{x0}x+\phi).$$

$$u_0=\frac{1}{\Lambda_x}\quad\text{(cycles/mm)},\qquad
k_{x0}=2\pi u_0=\frac{2\pi}{\Lambda_x}\quad\text{(rad/mm)}.$$

$x$ is a position; $\Lambda_x$ is a repeating distance. The notebook's frequency $f$ is a cycles-per-length frequency, like $u_0$.

::: notes
The period relations on this slide assume a positive frequency along x. For signed frequencies use Lambda_x=1/abs(u_0); zero frequency has no finite spatial period. The subscript zero identifies a particular sinusoidal component. Distinguish lowercase lambda for an electromagnetic wavelength from uppercase Lambda for a spatial intensity period. Do not equate spatial frequency to 1/x. Students should be able to convert between cycles/mm and radians/mm without changing the physical pattern.
:::

## Phase shifts the pattern

![](figures/02_phase.pdf){width=93%}

Both signals have the same frequency and amplitude.

::: notes
Original analytic sinusoids, f=1 cycle/mm, phases 0 and pi/2. A positive phase in cos(2 pi f x + phi) shifts the pattern left by phi/(2 pi f), here 0.25 mm. Do not require this sign calculation as a core outcome today.
:::

## A signal as a sum of spatial frequencies

![](figures/02_components.pdf){width=93%}

The mean, or zero-frequency component, sets the overall intensity level.

::: notes
Original periodic example I(x)=0.5+0.25 cos(2 pi x)+0.10 cos(2 pi 3x). The right panel lists cosine amplitudes, not a two-sided Fourier-transform magnitude. If writing the two-sided representation, each nonzero cosine contributes half its amplitude at each of plus and minus f. Fine variations come from the higher-frequency term.
:::

## Spatial Fourier transform

For a one-dimensional profile, we use

$$\widetilde I(f)=\int_{-\infty}^{\infty} I(x)e^{-j2\pi f x}\,dx.$$

- $x$ is position in mm and $f$ is spatial frequency in cycles/mm.
- Magnitude describes the strength of each frequency component.
- Phase describes its spatial alignment.

The inverse transform uses $e^{+j2\pi f x}$.

::: notes
State j squared equals -1. This is a Fourier-transform convention, not an assumed temporal phasor convention. A constant or infinite sinusoid has a transform involving delta functions. Avoid attempting to evaluate its ordinary improper integral on the board. For a finite profile of dimensionless intensity, the transform has units mm under this convention. Source: MIT RES.6-007 Fourier-transform notes.
:::

## Two-dimensional Fourier coordinates

Positions $(x,y)$ correspond to spatial frequencies $(u,v)$:

$$\widetilde I(u,v)=\iint I(x,y)e^{-j2\pi(ux+vy)}\,dx\,dy.$$

With angular spatial frequencies,

$$\widehat I(k_x,k_y)=\iint I(x,y)e^{-j(k_xx+k_yy)}\,dx\,dy.$$

$$k_x=2\pi u,\qquad k_y=2\pi v.$$

If $x,y$ are in mm, then $u,v$ are in cycles/mm and $k_x,k_y$ are in rad/mm.

::: notes
Both integrals extend over the whole spatial plane. The transform convention moves the 2 pi factor between the exponent and the frequency coordinates. The inverse angular-frequency transform would include 1/(2 pi)^2; the cycles convention would not. No inverse derivation is required today. Frequencies u,v can be positive or negative. This extends the preceding one-dimensional profile; it does not introduce a different imaging physics model.
:::

## Magnitude and phase of a complex spectrum

Write $F(u,v)=F_R(u,v)+jF_I(u,v)$, where $j^2=-1$.

$$|F|=\sqrt{F_R^2+F_I^2},\qquad
\angle F=\operatorname{atan2}(F_I,F_R).$$

The two-argument angle function identifies the correct quadrant. Phase is undefined where $|F|=0$.

**Example:** for $F=-1+j\sqrt3$, the magnitude is 2 and the phase is $2\pi/3$ radians, or $120^\circ$.

::: notes
On an Argand diagram the example lies in quadrant II. Using arctan(F_I/F_R) alone gives the wrong quadrant. Students need the formulas and their meaning rather than a programming implementation. The formulas apply to each frequency coordinate separately. A real, even spatial signal can have a real Fourier transform; negative real values still have magnitude greater than zero and phase pi.
:::

## A rectangular spatial signal and its transform

A unit-height rectangle $r(x)=\operatorname{rect}(x/a)$ equals 1 for $|x|<a/2$ and 0 outside. Its width is $a>0$.

$$R(u)=a\,\operatorname{sinc}(au),\qquad
\operatorname{sinc}(z)=\frac{\sin(\pi z)}{\pi z},\quad\operatorname{sinc}(0)=1.$$

![](figures/02_rect_transform.pdf){width=80%}

::: notes
The boundary value at plus or minus a/2 can be 1/2 without affecting the transform. The pair uses exp(-j 2 pi u x). The plotted example has a=2 mm: R(0)=2 mm, and the first zeros are at u=plus or minus 0.5 cycles/mm. The rectangle is dimensionless and R has units mm. Emphasize that this plot is the signed, real transform, not its magnitude. For a unit-area rectangle r(x)/a, the transform is sinc(au). A larger spatial width moves the transform zeros toward the origin. The transform follows by integrating the exponential over [-a/2,a/2].
:::

## A Gaussian spatial signal and its transform

For a centered Gaussian with unit area,

$$q(x)=\frac{1}{\sqrt{2\pi}\sigma}\,e^{-x^2/(2\sigma^2)},
\qquad Q(u)=e^{-2\pi^2\sigma^2u^2}.$$

![](figures/02_gaussian_transform.pdf){width=80%}

A wider spatial Gaussian has a narrower frequency response.

::: notes
Here sigma has units mm, q has units mm^-1, and Q is dimensionless. This choice of unit area keeps Q(0)=1 for both plotted widths. If students instead choose a unit-peak Gaussian, the transform gains the factor sqrt(2 pi)*sigma; either is valid when stated consistently. The transform is real and nonnegative because this example is centered and even. The useful base pair exp(-pi x^2) transforms to exp(-pi u^2); scaling changes widths reciprocally. The two-dimensional Gaussian example in the system-response lecture uses separability.
:::

## Frequency has a direction in two dimensions

![](figures/02_orientation.pdf){width=85%}

The frequency vector points in the direction of intensity variation, perpendicular to the stripes.

::: notes
Original periodic simulations and discrete Fourier transforms. Top row is I(x,y)=0.5+0.45 cos(2 pi (u x+v y)). Frequency pairs are (1,0), (0,1), and (0.75,0.75) cycles/mm. Bottom panels show DFT magnitudes relative to DC, not measured scanner k-space. A 4 mm periodic field puts all components exactly on DFT bins. Explain the symmetric peaks for real images. No need to derive the full two-dimensional transform today.
:::

## Spatial sampling

For ideal point samples with spacing $p$,

$$I_n=I(np),\qquad f_s=\frac{1}{p}.$$

The sampling frequency $f_s$ is the number of samples per mm.

For a sinusoid, the number of samples per period is

$$N_{\rm period}=\frac{1}{pf}.$$

::: notes
These are ideal point samples. A physical pixel averages over a finite area before sampling; the system-response lecture adds that effect. The origin here is np. The notebook places pixel centers at (n+1/2)p. The sampling rate and Nyquist frequency are unaffected by that origin choice.
:::

## Nyquist frequency

$$f_N=\frac{f_s}{2}=\frac{1}{2p}.$$

For an ideal band-limited signal, recovery from equally spaced samples requires its highest frequency to be strictly below $f_N$.

A sinusoid below this limit has more than two samples per period.

**Example:** $p=0.25$ mm gives $f_s=4$ samples/mm and $f_N=2$ cycles/mm.

::: notes
State the band-limited assumption. Exactly at Nyquist, arbitrary phase and amplitude are not recoverable; reserve the phase demonstration for the notebook extension. Do not equate two pixels per PSF FWHM with the sampling theorem. Source: MIT RES.6-007 Sampling, lecture 16.
:::

## A sampling limit in angular-frequency units

For pixel spacing $p$, the angular sampling frequency is $k_s=2\pi/p$ and the angular Nyquist frequency is $k_N=\pi/p$.

$$k_{\max}<\frac{\pi}{p},\qquad
p<\frac{\pi}{k_{\max}}.$$

**Example:** if $k_{\max}=10\pi$ rad/mm, then $u_{\max}=5$ cycles/mm and the limiting pitch is 0.10 mm.

Choose a smaller pitch for phase-independent sampling of the highest-frequency component. Exactly at the limit there are only two samples per period.

::: notes
Use a conversion-first strategy or the angular-frequency formula and check that they agree. The numerical input differs from the homework. "Nyquist-limit" names the boundary; a strict inequality is needed to preserve arbitrary phase at the highest frequency. Reserve a detailed phase-at-Nyquist demonstration for the optional notebook extension.
:::

## Aliasing

![](figures/02_alias.pdf){width=93%}

At these sample locations, the two continuous signals give identical values.

::: notes
Original exact point-sampling example. p=0.25 mm and x_n=np. A 3 cycles/mm cosine aliases to 1 cycle/mm because cos(2 pi 3n/4)=cos(2 pi n/4). The samples cannot identify the original high-frequency sinusoid without prior information. This plot intentionally omits pixel-area averaging.
:::

## A sampling calculation

A detector records a 1.5 cycles/mm stripe pattern.

| Quantity | $p=0.20$ mm | $p=0.40$ mm |
|:---|:---|:---|
| Sampling frequency $f_s$ | ? | ? |
| Nyquist frequency $f_N$ | ? | ? |
| Samples per stripe period | ? | ? |
| Target below Nyquist? | ? | ? |

Calculate the entries with a partner. Predict whether either detector can show a false stripe spacing.

::: notes
Allow eight minutes and four minutes of debrief. Answers: fs=5 and 2.5 samples/mm; fN=2.5 and 1.25 cycles/mm; samples per period=3.333 and 1.667. The second case aliases to 1 cycle/mm. Refer to the first as adequately sampled for this single sinusoid, not a guarantee about all possible objects.
:::

## Sampling and physical blur

An object can contain frequencies above a detector's Nyquist frequency.

Physical blur reduces high-frequency contrast before sampling. This can weaken aliases, while also reducing useful fine detail.

Increasing the displayed image size adds no new detector measurements.

Next meeting: the point-spread function and modulation transfer function quantify these effects.

::: notes
Use this as the bridge to system response, not as a derivation of MTF. A Gaussian does not strictly band-limit a signal. Later students will compare a blur curve with the detector Nyquist frequency.
:::

## Exit questions

1. What changes when spatial frequency doubles: stripe period, amplitude, or both?
2. What is the Nyquist frequency for $p=0.10$ mm?
3. Why can two different continuous patterns agree at every recorded sample?

::: notes
Answers: period halves, with amplitude otherwise independent; fN=5 cycles/mm; different frequencies can be aliases at the chosen sampling locations. Reserve five minutes and ask for a sentence of reasoning, not just the numerical answer.
:::

## Reading and resources

Prince and Links, *Medical Imaging: Signals and Systems*: spatial signals, Fourier representations, and sampling.

- [MIT RES.6-007: lecture notes](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/pages/lecture-notes/) on convolution, Fourier transforms, sampling, and interpolation.
- [MIT HST.582J: lecture notes](https://ocw.mit.edu/courses/hst-582j-biomedical-signal-and-image-processing-spring-2007/pages/lecture-notes/) for further biomedical signal examples.

::: notes
Reference slide, outside the timed class plan. These are optional review resources, not additional required full courses. Figures and numerical examples are original. The lecture focuses on image formation, not image-processing algorithms.
:::
