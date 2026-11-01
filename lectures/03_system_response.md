---
title: "System response"
date: ""
---

## A point becomes a spot

![](figures/03_psf_images.pdf){width=91%}

The **point-spread function (PSF)** describes the image of an ideal point input.

::: notes
Original Gaussian intensity-PSF simulations, peak-normalized for display. The ideal point is not assigned a finite drawn area. Ask students to describe what a wider spot would do to a pair of nearby points. The normalization in the image is for display only; the analytic PSF integrates to one. Define PSF before using the abbreviation repeatedly.
:::

## Linear, shift-invariant imaging

For a **linear** system, weighted input signals produce the same weighted combination of output signals.

For a **shift-invariant** system, moving an input point shifts its response without changing its shape.

These assumptions allow one PSF to describe the system over the region of interest.

::: notes
This is LSI terminology in Prince and Links. Link explicitly to students' linear systems background. A real imaging system may only approximately satisfy these assumptions over a limited region. MRI magnitude operations, nonlinear processing, and position-dependent resolution need more care. Here we model a continuous intensity-blur stage, not every step of every modality as globally LSI.
:::

## Convolution and image formation

$$I_{\rm blur}(x,y)=(I_0*h)(x,y).$$

The system spreads each object point according to the PSF and adds the contributions.

$$I_{\rm blur}(x,y)=\iint I_0(\xi,\eta)\,h(x-\xi,y-\eta)\,d\xi\,d\eta.$$

For an intensity-preserving blur model, $\iint h(x,y)\,dx\,dy=1$.

::: notes
Convolution is review. Explain the normalization through a uniform input: its intensity is unchanged by this ideal blur. With dimensionless normalized input intensity and coordinates in mm, h has units mm^-2. The PSF represents intensity response for incoherent optical imaging in this notebook. It is not a coherent field-amplitude PSF.
:::

## Object and image in the frequency domain

Use $f(x,y)$ for the object, $h(x,y)$ for the impulse response, and $g(x,y)$ for the output image.

$$g=f*h
\quad\Longleftrightarrow\quad
G(u,v)=F(u,v)H(u,v).$$

The **transfer function** $H$ is the Fourier transform of $h$. Each object's frequency component is multiplied by the system's response at that frequency.

A constant input probes the zero-frequency response:

$$H(0,0)=\iint h(x,y)\,dx\,dy.$$

::: notes
This notation is equivalent to I_blur=I_0*h on the preceding slide. Uppercase F,G,H denote the cycles-per-length Fourier transforms of lowercase f,g,h. Spatial convolution and frequency multiplication describe the same LSI model. H(0,0) is the DC gain, which need not equal one for an arbitrary impulse response. A uniform object of value f_0 produces a uniform output f_0 H(0,0), ignoring boundaries.
:::

## Two nearby point inputs

![](figures/03_two_points.pdf){width=93%}

A wider PSF makes the two responses overlap more strongly.

::: notes
Original simulation of equal point inputs at x=-0.3 and +0.3 mm, using Gaussian line-spread responses sigma=0.08 and 0.25 mm. Both responses use the same vertical scale and integrated signal. Do not announce a universal criterion for resolving two points. Resolution depends on the task, contrast, and measurement conditions. The point pair is a one-dimensional illustration.
:::

## Gaussian PSF width

$$h(x,y)=\frac{1}{2\pi\sigma^2}\exp\left[-\frac{x^2+y^2}{2\sigma^2}\right].$$

$\sigma$ sets the width of the spot and has units of mm.

The **full width at half maximum (FWHM)** is the width across the central profile at half its peak value:

$$\mathrm{FWHM}=2\sqrt{2\ln2}\,\sigma\approx2.355\sigma.$$

**Example:** $\sigma=0.10$ mm gives FWHM $\approx0.236$ mm.

::: notes
A Gaussian is the model, not an exact universal camera PSF. At sigma=0 the notebook uses the delta-function limit analytically. The FWHM is measured along a line through the Gaussian center, not an area or radius. Have students check that the equation has units of length.
:::

## Separable Gaussian responses

If $h(x,y)=h_x(x)h_y(y)$, its transform factors:

$$H(u,v)=H_x(u)H_y(v).$$

For $a,b>0$,

$$h(x,y)=A e^{-\pi[(x/a)^2+(y/b)^2]}
\quad\Longrightarrow\quad
H(u,v)=Aab\,e^{-\pi[(au)^2+(bv)^2]}.$$

**Method:** transform each one-dimensional Gaussian, include its scale factor, and multiply. Check $H(0,0)$ against the integral of $h$.

::: notes
Use normalized coordinates, or let a,b carry the same length units as x,y and let u,v have reciprocal length units. This is a general family, not a worked copy of the assessment response. The scaling rule is f(x/a) transforms to a F(au) for a>0. For an intensity-preserving PSF choose A=1/(ab), giving H(0,0)=1. A unit-peak h with A=1 instead has DC gain ab. This distinction prepares students to normalize MTF without assuming that every given h already has unit area.
:::

## Resolution can differ by direction

![](figures/03_directional_response.pdf){width=85%}

In this example, the PSF is wider along $x$. The response falls more rapidly with $u$, so the system preserves finer detail along $y$.

::: notes
Original normalized separable Gaussian with a=0.60 mm, b=0.30 mm, and A=1/(ab). The aspect ratio and direction differ from the assessment example. Compare H(u,0) with H(0,v), not rows or columns chosen arbitrarily from a displayed spectrum. At the same numerical frequency the narrower spatial PSF direction has higher MTF. Ask students to predict the direction before revealing the final sentence verbally. The PSF-width comparison is independent of its overall gain.
:::

## Sinusoidal contrast

$$C=\frac{I_{\max}-I_{\min}}{I_{\max}+I_{\min}}.$$

For $I(x)=\overline I[1+C\cos(2\pi f x+\phi)]$, contrast is the amplitude divided by the mean.

The notebook target has $\overline I=0.5$ and $C_0=0.9$, giving $I_{\max}=0.95$ and $I_{\min}=0.05$.

Blur can reduce contrast without changing the stripe frequency.

::: notes
This contrast definition is for a sinusoidal target with a positive mean. It is not the only contrast definition used in imaging. Use extrema from the continuous sinusoid; sampled extrema may miss its peaks and troughs.
:::

## Modulation transfer function

The **MTF** describes how much sinusoidal contrast the system preserves at each spatial frequency:

$$\mathrm{MTF}(f)=\frac{C_{\rm out}(f)}{C_{\rm in}(f)}.$$

For our normalized LSI blur model, it is the magnitude of the Fourier transform of the PSF.

An MTF of 0.5 at a particular frequency means the output sinusoid has half the input contrast at that frequency.

::: notes
General normalized definition is |H(f)|/|H(0)|; H(0)=1 for our intensity-preserving PSF. In two dimensions, MTF depends on the frequency vector. Here we examine a sinusoid varying only in x. Explain that modulation refers to the sinusoidal variation about the mean, not a programming operation. Source context: Michigan Medical Imaging Systems and the course textbook. The formula follows directly from the convolution theorem.
:::

## MTF normalization and DC gain

For an LSI system with positive DC gain,

$$\mathrm{MTF}(u,v)=\frac{|H(u,v)|}{|H(0,0)|}.$$

Dividing by the zero-frequency gain compares sinusoidal amplitude transfer with mean-intensity transfer. This gives contrast transfer and makes $\mathrm{MTF}(0,0)=1$.

**Example:** if $H(0,0)=4$ and $|H(u_1,v_1)|=2$, the MTF there is 0.5. An input contrast of 0.8 becomes 0.4.

::: notes
For a constant mean plus a sinusoid, the mean scales by H(0,0) while the modulation amplitude scales by |H|. Their ratio gives C_out/C_in=|H|/H(0,0). Positive, nonzero DC gain applies to the intensity-blur systems discussed here. A zero-DC system needs a different interpretation. The normalized notebook PSF happens to have H(0,0)=1, so its MTF is simply |H|. The general expression is needed for impulse responses supplied with other normalizations.
:::

## PSF width and contrast transfer

![](figures/03_psf_mtf.pdf){width=93%}

For a Gaussian, $H_{\rm opt}(f)=\exp(-2\pi^2\sigma^2f^2)$.

::: notes
Original exact Gaussian profiles and transfer curves at sigma=.04 and .25 mm. The PSF profiles are peak-normalized for a width comparison; the analytic PSFs themselves have unit integral. A larger sigma gives faster attenuation of high frequencies. Gaussian optical MTF50 equals sqrt(ln 2)/(sqrt(2) pi sigma), but students do not need to derive it today.
:::

## Finite pixel size

A pixel reports an average over its collecting area, followed by one value at its center.

For vertical stripes and pixels of width and spacing $p$,

$$d_n=\frac{1}{p}\int_{x_n-p/2}^{x_n+p/2}I_{\rm blur}(x)\,dx,
\qquad x_n=(n+\tfrac12)p.$$

Larger pixels average over more of the spatial variation.

::: notes
The collecting area is also called an aperture. Define it in plain language before using that term in the notebook. Square light-sensitive areas fill the detector without gaps. Because the object is constant in y, its two-dimensional area average reduces to this one-dimensional integral. This is an average intensity, so there is no factor of p left after averaging a uniform field.
:::

## Averaging and sampling

![](figures/03_pixel_average.pdf){width=93%}

The step display assigns each recorded average to its pixel area.

::: notes
Original exact sinusoidal integration, f=1 cycle/mm, sigma=0, p=0.4 mm, and C=.9. Blue curve is continuous object intensity, orange steps are recorded averages, and markers show pixel centers. This frequency is below Nyquist (1.25 cycles/mm), yet finite-area averaging reduces contrast. No interpolating smoothing is applied to the step display.
:::

## Combined response before sampling

For a sinusoid at frequency $f$, pixel averaging contributes

$$H_{\rm pixel}(f)=\mathrm{sinc}(pf),\qquad \mathrm{sinc}(u)=\frac{\sin(\pi u)}{\pi u}.$$

The combined **presampling MTF** is

$$\mathrm{MTF}_{\rm pre}(f)=|H_{\rm opt}(f)H_{\rm pixel}(f)|.$$

Sampling adds a separate limit: $f_N=1/(2p)$.

::: notes
sinc(0)=1 by the limit. A negative sinc changes sinusoidal phase by pi; MTF retains magnitude. Stay on the first lobe for the introductory explanation. Calling Nyquist a separate limit must not imply that the Gaussian strictly band-limits the input. It suppresses high frequencies without making them exactly zero.
:::

## Contrast loss below Nyquist

Take a sinusoid at $f=1$ cycle/mm and pixels of width and spacing $p=0.40$ mm.

$$f_N=\frac{1}{2p}=1.25\ \text{cycles/mm},\qquad
|H_{\rm pixel}(f)|=|\operatorname{sinc}(0.40)|\approx0.757.$$

The frequency is below Nyquist, yet pixel averaging preserves only about 76% of the continuous sinusoidal contrast.

- **Averaging:** nearby bright and dark intensities contribute to one pixel value.
- **Aliasing:** different continuous frequencies produce the same samples.

::: notes
This is the quantitative reading of the earlier averaging plot. The mean intensity is preserved by the normalized pixel average. Larger pixels can average away modulation without producing an incorrect frequency when the target remains below Nyquist. The contrast here is that of the continuous aperture-averaged sinusoid; extrema of a finite set of samples need not coincide with its peaks and troughs. The notebook's input contrast .9 would become about .681 with pixel averaging alone at these settings.
:::

## An MTF curve and a sampling limit

![](figures/03_combined_mtf.pdf){width=93%}

**MTF50** is the first frequency where the combined MTF falls to 0.5.

::: notes
Original exact optical, pixel, and combined curves at sigma=.04 mm and p=.10 mm. The shaded region is above Nyquist, not a frequency range in which the presampling response disappears. MTF50 is a bandwidth descriptor, not a hard cutoff or universal smallest resolvable feature. Point at f=1 cycle/mm and ask for an estimated contrast-transfer fraction.
:::

## Guided notebook investigation

Open **01_sampling_resolution.ipynb** and run all cells.

1. Select **Fine sampling**. Identify the object, optical image, and detector image.
2. Predict what will change when the PSF gets wider.
3. Select **Blur limited**. Keep frequency and pixel spacing fixed.
4. Compare the images, intensity profile, and MTF curve.

Explain the observed change to a partner before recording your answer.

::: notes
Start the notebook block by minute 40. Allow five minutes for opening and identifying the panels, followed by eight minutes for predictions and comparison. Both presets have f=1 cycle/mm and p=.10 mm, so only sigma changes from .04 to .25 mm. Keep phase at its default zero. Do not require the aliasing or optional phase investigation today.
:::

## Measurements for the comparison

| Quantity | Fine sampling | Blur limited |
|:---|:---|:---|
| PSF width $\sigma$ (mm) | 0.04 | 0.25 |
| FWHM $\approx2.355\sigma$ (mm) | Calculate | Calculate |
| MTF at 1 cycle/mm | Read | Read |
| MTF50 (cycles/mm) | Read | Read |

Why does stripe contrast decrease even though there are still ten pixels per stripe period?

::: notes
Use the next seven minutes to calculate, compare, and debrief. Approximate FWHMs are .0942 and .5887 mm. Combined MTF at f=1 is .9531 and .2864, with predicted contrasts .8577 and .2578 respectively. Exact values are checked by the figure-generation script. The model's MTF50 values should be read from the notebook, not inferred from FWHM. Students may complete notebook question 1 after class if needed.
:::

## Exit questions

1. What does the PSF describe, and what does the MTF describe?
2. If $C_{\rm in}=0.8$ and MTF $=0.5$, what is $C_{\rm out}$?
3. What can limit spatial detail even when the pixel spacing is small?

Next meeting: image quality, detector sampling, and aliasing in the notebook.

::: notes
Five-minute close. Expected responses: PSF is point response, MTF is sinusoidal contrast transfer versus frequency; output contrast .4, unitless; physical blur can attenuate fine detail before detector sampling. Finish with a student explanation rather than an additional derivation.
:::

## Reading and resources

Prince and Links, *Medical Imaging: Signals and Systems*: LSI imaging, point-spread functions, and image quality.

- [Michigan EECS 516: Medical Imaging Systems](https://web.eecs.umich.edu/~fessler/course/516/index.html)
- [MIT RES.6-007: convolution and Fourier-transform review](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/pages/lecture-notes/)
- Course notebook: **01_sampling_resolution.ipynb**, investigation 1.

::: notes
Reference slide, outside the timed class plan. All simulations and numerical examples are original and use the same Gaussian blur and full-width pixel integration model as the notebook. No external lecture figures have been copied. Details of negative sinc lobes and exact-Nyquist phase dependence remain optional.
:::
