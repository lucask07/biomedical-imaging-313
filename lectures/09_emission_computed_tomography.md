---
title: "Emission computed tomography"
date: ""
---

## SPECT rotates a gamma camera

**Single-photon emission computed tomography (SPECT)** records collimated gamma-camera projections at several angles.

Reconstruction uses those projections to estimate a slice or volume of **tracer activity concentration**.

In X-ray CT, what property did the reconstructed pixels estimate?

::: notes
0–8 min. CT estimates attenuation. SPECT estimates activity distribution. Explain that the emission projections are weighted by photon escape and system response. Simple reconstruction connects to CT but clinical systems commonly use iterative models and corrections.
:::

## Emission and transmission give different data

| X-ray CT | Emission tomography |
|:---|:---|
| Tube sends photons toward detector. | Tracer emits photons in the patient. |
| Detector measures transmitted signal. | Detectors count accepted events. |
| Negative log of transmission estimates a line integral of attenuation. | Counts depend on tracer distribution and on whether photons reach the detectors. |

Both use many directions to recover spatial information.

::: notes
8–13 min. In the idealized unattenuated parallel-ray model the expected emission counts are proportional to activity integrated along each ray. Absorption and scatter change this simple model.
:::

## PET uses two photons to identify a line

A positron and an electron typically annihilate to produce two nearly opposite $511$ keV photons.

1. Two detector elements record hits within a short **coincidence window** (in time).
2. The line joining the detector elements is the **line of response (LOR)**.
3. Many LORs constrain the distribution of annihilations.

What can the detector positions tell us about one event along its line?

::: notes
13–22 min for coincidence geometry and the figure. Coincidence logic replaces the direction selection role of the gamma camera collimator. Distinguish positron range, photon noncollinearity and detector size as limits.
:::

## One pair gives a line through the object

![](figures/09_pet_coincidence.pdf){height=102mm}

Each accepted pair supplies one line. The red mark shows the simulated event position.

::: notes
Ask where other events could lie on that same line. The drawn probability band is schematic. It represents uncertainty along the line.
:::

## Timing refines the estimate along the line

Let $s$ be distance from the midpoint toward detector B and let $\Delta t=t_A-t_B$.

$$d_A-d_B=2s,\qquad s=\frac{c\,\Delta t}{2}.$$

**Example.** If B records the photon $200$ ps earlier than A, the best estimate lies about $30$ mm toward B.

A coincidence timing resolution of $400$ ps FWHM (full width at half maximum) corresponds to about $60$ mm FWHM along the line.

::: notes
22–34 min. c = 0.300 mm/ps. Derive the factor of two by moving the event toward B by s. FWHM means full width at half maximum. Differentiate a measured time difference for one pair, coincidence timing resolution, and the coincidence acceptance window. TOF localization width along one LOR differs from reconstructed image resolution.
:::

## Which events are counted? 

- **True:** both photons came from the same annihilation and reached the detectors without scattering.
- **Scatter:** a photon changed direction on the way to a detector, shifting the assigned line.
- **Random:** two unrelated hits fall within the coincidence window.

What could happen to the rate of true and random coincidences if the acceptance window is made wider?

::: notes
34–41 min. A wider window can recover true events near the cutoff but admits more random pairs. In PET/CT, a CT-derived attenuation map can help correct for photon loss. Real PET estimates random and scattered event contributions. Explain the coincidence requirement that both photons survive.
:::

## Radon transform

[Radon transform](https://www.mathworks.com/help/images/radon-transform.html)

## iPython Notebook

Open the **PET explorer** and use **Run all**.

1. Use a small event count. Find the lines from the two tracer deposits.
2. Increase the event count. Compare the spatial patterns in both panels.
3. Hold the event count fixed and improve timing resolution. Explain what happens to the along-line width and the image.

::: notes
41–60 min. Give pairs 15 minutes, then compare observations. Both panels use the same events. These are simple event backprojections for interpretation. Quantitative PET commonly uses iterative reconstruction with a model of acquisition and corrections.
:::

## Exit question

A single PET event has two detectors in coincidence. What does the pair tell you? What does the measured arrival-time difference add?

[IAEA, *Nuclear Medicine Physics*](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1617web-1294055.pdf)

[Stanford Molecular Imaging Instrumentation Laboratory, TOF PET](https://med.stanford.edu/miil/research/tofdetector.html)

::: notes
60–65 min. Position of the detector pair defines the line. Timing estimates position along it with uncertainty. Suggested reading: Prince and Links, chapter 9.
:::

