---
title: "Physical signals and imaging modalities"
date: ""
---

## Imaging

An imaging system records physical signals from the body and uses the measurements to form an image. Signals are typically emitted, transmitted, or reflected. 

An imaging modality uses a specific physical interaction. For example, cameras measure reflection of visible light. 

. . .

**Questions for each modality:**

- **Physical signal:** waves or particles that carry information from the body to the detector.
    - What signal does this modality use?
- **Detector measurement:** the quantity recorded from the received signal.
    - What does the detector record?
- **Contrast mechanism:** tissue properties or processes that make image regions differ.
    - Why do different tissues or regions give different image values?

::: notes
Use the opening five minutes for students' prior experiences with imaging. Ask for physical signals rather than diagnoses. A modality is a method of imaging based on a particular physical interaction. Reuse physical signal, detector measurement, and contrast mechanism throughout the examples. The physical signal can originate outside the body, as in X-ray transmission, or within it, as in nuclear imaging. Contrast mechanism describes a physical cause of image differences, while display settings also affect visible contrast. Source for modality-level framing: NIBIB Science Topics and Michigan EECS 516 course descriptions. Do not imply that every detector has a one-to-one correspondence with final image pixels.
:::

## Object, measurements, and image

An **image** is a map of measured or estimated values arranged by spatial position. 

| Stage | Example in X-ray Computed Tomography (CT) |
|:---|:---|
| Object property | How strongly tissue attenuates X-rays |
| Measurement | Transmitted X-ray signal along a path |
| Image | Estimated attenuation at locations in a slice |

The measurement and the reconstructed image describe different quantities. Image reconstruction may be simple or mathematically complex. 

::: notes
Attenuation means removal of photons from the primary beam through absorption or scattering. Reconstruction uses many measurements to estimate an internal distribution. Introduce the distinction here without deriving the CT forward model. Source: NIBIB CT and Medical X-rays fact sheets.
:::

## Imaging chain

| Stage | Visible-light camera example |
|:---|:---|
| Source | Light illuminating the scene |
| Interaction | Objects reflect or emit light |
| Propagation and collection | Light travels to the camera and passes through its lens |
| Detection | Sensor elements convert light into electrical signals |

The source, the object, and the detector each affect the recorded signal.

::: notes
Ask students to trace one ray from a scene through the lens to a detector pixel. Distinguish source from detector and distinguish propagation/collection from detection. Adapt the same stages to any modality. Keep the dental example for independent student application. This slide plus the next takes about four minutes.
:::

## Imaging chain part 2

| Stage | Visible-light camera example |
|:---|:---|
| Processing or reconstruction | Convert detector data into image values |
| Display | Map image values to brightness and color |
| Perception and interpretation | A viewer identifies structures or differences |

Data transfer and storage can occur between stages. Reconstruction may require many measurements, as in CT.

::: notes
Different imaging chains can group these stages differently. The important distinctions are the physical measurement, the operations that form an image, and the display/viewing process. A digital camera can include calibration, color processing and demosaicing. Do not imply that conventional photography uses the same inverse problem as CT.
:::

## Radiography and CT

**Physical signal:** X-ray photons transmitted through the body.

| Method | Detector measurement | Image formation |
|:---|:---|:---|
| Radiography | Transmitted X-ray intensity across a detector | A projection with overlapping structures |
| CT | Transmitted X-ray intensity from many directions | Reconstruction of cross-sectional slices |

**Contrast mechanism:** differences in X-ray attenuation, the reduction of the primary beam as it passes through material.

::: notes
Sources: NIBIB Medical X-rays and Computed Tomography. Keep clinical examples brief. No need to introduce Hounsfield units yet. CT and radiography share an interaction but use different measurement geometry and reconstruction.
:::

## Projection imaging

A **projection** records the combined effect of material along each measurement path. In radiography, the transmitted X-ray intensity depends on attenuation along the entire path through the body.

```{=latex}
\begin{center}
\includegraphics[width=0.65\linewidth]{figures/01_projection.pdf}
\end{center}
```

Can this measurement tell us where along the path the attenuation occurred?

::: notes
The purpose is to define projection imaging using radiography as the example, following the introduction to radiography and attenuation. Rays run parallel to the vertical coordinate in the left panel. The right panel is exp(-integral mu dy), a monoenergetic, scatter-free transmission model. The detector coordinate x alone cannot tell the depths of the two structures. The length and attenuation scales are illustrative, not clinical. For the question, a single projection combines attenuation along the ray and does not identify its depth. This ambiguity motivates CT's use of measurements from multiple directions.
:::

## Ultrasound

A transducer sends a sound pulse (acoustic energy) into tissue and detects returning echoes.

- **Physical signal:** reflected sound waves, or echoes.
- **Detector measurement:** echo intensity (via voltage) as a function of time.
- **Contrast mechanism:** differences in sound reflection and propagation between tissue regions.

Echo delay helps locate a reflecting boundary. The transducer converts the returning sound into an electrical signal.

::: notes
Source: NIBIB Ultrasound, How does it work? A transducer converts electrical and acoustic energy. Students may know the word from circuits but should hear this definition. Later lectures will develop round-trip travel time and acoustic impedance. Do not describe an ultrasound image as a direct map of density alone.
:::

## Magnetic resonance imaging (MRI)

MRI measures the response of nuclei in tissue to radiofrequency excitation in a magnetic field.

- **Physical signal:** radiofrequency electromagnetic signal from nuclei in tissue.
- **Detector measurement:** voltage in a receiver coil.
- **Contrast mechanism:** differences in the strength and decay of the tissue's magnetic response.

The scanner uses spatial variations (gradients) in an applied magnetic field to determine where the signal originates.

::: notes
Source: NIBIB MRI. Most clinical MRI measures hydrogen nuclei, primarily in water and fat. Define a receiver coil as the component that detects the changing magnetic response as a voltage. Introduce spatial encoding qualitatively and defer gradients and the spin model to the MRI lectures.
:::

## Positron emission tomography (PET)

A **radioactive tracer** is introduced into the body to follow a biological process.

- **Physical signal:** photon pair produced when a positron from the tracer annihilates with an electron.
- **Detector measurement:** pairs of photon detections close together in time.
- **Contrast mechanism:** differences in the distribution of the tracer.

Many detection pairs allow the scanner to estimate where the tracer is located.

::: notes
Source: NIBIB Nuclear Medicine. A positron is the positively charged counterpart of an electron. Define annihilation briefly as the interaction that converts their mass into photon energy. A detected photon pair constrains a line rather than identifying the exact annihilation location along it. Defer coincidence timing, radiotracer biology, and reconstruction details to the nuclear-imaging lectures. https://med.stanford.edu/miil/research/tofdetector.html
:::

## Physical frequency and spatial frequency

**Physical wave frequency:** oscillations per second, in hertz (Hz).

Examples include an ultrasound pressure wave and an MRI radiofrequency signal.

**Spatial frequency:** repetitions per unit distance, such as cycles/mm.

Example: closely spaced bright and dark stripes in an image have a high spatial frequency.

These frequencies describe different variables, time and position.

::: notes
Ask students which axis would appear on a plot of each signal. Next class will review spatial sinusoids using the same mathematics as temporal signals.
:::

## Wavelength, frequency, and photon energy

For electromagnetic radiation in free space,

$$c=\lambda\nu,\qquad E_\gamma=h\nu=\frac{hc}{\lambda}.$$

- $\lambda$: wavelength in m; $\nu$: temporal frequency in Hz.
- $E_\gamma$: energy of **one photon**, in J.
- $c\approx3.00\times10^8$ m/s; $h\approx6.626\times10^{-34}$ J s.
    - For a photon, Joules are extremely small. Instead the eV.

$$1\ \mathrm{eV}=1.602\times10^{-19}\ \mathrm{J},\qquad
E_\gamma[\mathrm{eV}]\approx\frac{1240}{\lambda[\mathrm{nm}]}.$$

::: notes
Sources: NIST SI definitions and constants, https://www.nist.gov/pml/special-publication-330/sp-330-section-2 and https://www.nist.gov/si-redefinition/meet-constants . In the last expression bracketed units mean the numerical values in those units. Photon energy differs from the total energy in an exposure or RF pulse. The relation c=lambda nu gives free-space wavelength; wavelength in tissue can differ. These photon equations apply to electromagnetic radiation, not to an ultrasound pressure wave.
:::

## Photon calculations and stated assumptions

| Assumed signal | Free-space wavelength | Energy per photon |
|:---|:---|:---|
| Visible light at 500 nm | 500 nm | 2.48 eV |
| RF at 100 MHz | 3.00 m | $4.14\times10^{-7}$ eV |
| X-ray photon at 50 keV | 0.0248 nm | 50 keV |

$$1\ \mathrm{eV}=1.602\times10^{-19}\ \mathrm{J},\qquad
E_\gamma[\mathrm{eV}]\approx\frac{1240}{\lambda[\mathrm{nm}]}.$$

Note: An X-ray beam contains a spectrum of photon energies centered around an average energy. 

::: notes
Examples use different inputs from the assessment. Derive one example at the board and have students check another. For 500 nm, lambda=5.00e-7 m and E=3.973e-19 J. For 100 MHz, nu=1.00e8 Hz. For 50 keV, E=5.00e4 eV before using 1240 eV nm. Rounded values use three significant figures. Source for the spectrum distinction: FDA Resource Manual for Compliance Test Parameters of Diagnostic X-Ray Systems, https://www.fda.gov/radiation-emitting-products/medical-x-ray-imaging/resource-manual-compliance-test-parameters-diagnostic-x-ray-systems . A tube voltage can specify a maximum photon energy, not a unique energy for the whole beam.
:::

## Pixel values

A **pixel** is one element of a digital image. Its value represents a measurement or an estimated quantity over a spatial region.

- A reconstructed image can have different units from the detector signal.
- Display settings map numerical values to gray levels or colors.

::: notes
Use the CT example: detector signal versus reconstructed attenuation. MRI image brightness depends on acquisition and display choices. Keep this qualitative. Define contrast on a later slide rather than assuming that students know the imaging use of the term.
:::

## Repeated photon counts: Noise

Repeated exposures under the same conditions can give different detected counts.

For independent arrivals with a constant expected count $\overline N$, a model with noise from Poisson statics is

$$N\sim\operatorname{Poisson}(\overline N),\qquad
\operatorname{E}[N]=\overline N,\qquad
\operatorname{Var}(N)=\overline N.$$

The standard deviation is $\sigma_N=\sqrt{\overline N}$.

An observed count $N$ is one outcome. The expected count $\overline N$ describes the mean over repeated exposures.

::: notes
Source: NIST/SEMATECH e-Handbook, Poisson distribution, https://itl.nist.gov/div898/handbook/eda/section3/eda366j.htm . The model assumes independent detection events; correlations, background, and electronic noise can change the variance. Counts are dimensionless event numbers; it is conventional to report the standard deviation in counts. Use N-bar rather than lambda for the mean to avoid confusing the Poisson parameter with wavelength. Introduce uncertainty as a physical measurement property.
:::

## SNR for Poisson counting

Here, **signal-to-noise ratio (SNR)** means the expected count divided by its standard deviation:

$$\mathrm{SNR}=\frac{\overline N}{\sigma_N}=\sqrt{\overline N}.$$

For $\overline N=100$, $\sigma_N=10$ counts and SNR $=10$.

**Predict:** if the expected count increases by a factor of four, what happens to the standard deviation and SNR?

::: notes
Both increase by a factor of two; the fractional noise sigma_N/N-bar decreases by a factor of two. SNR is unitless and is a linear ratio here, not dB. This is mean-count SNR, not contrast-to-noise ratio. Other detector noise sources are neglected. Discuss one minute, then return to image formation. More detected counts can improve precision without changing pixel spacing or PSF width.
:::

## Pixel spacing and field of view

The **field of view (FOV)** is the physical extent represented by the image.

The **pixel spacing**, also called pitch, is the distance between neighboring pixel centers.

For $N$ equally spaced pixels spanning width $L$,

$$p=\frac{L}{N}.$$

**Example:** $L=128$ mm and $N=256$ give $p=0.50$ mm.

::: notes
This convention treats L as the total width of N pixel cells. The distance between first and last pixel centers is (N-1)p. A larger displayed image on the projector does not change p or physical FOV. All values in this example are illustrative.
:::

## Spatial detail and blur

![](figures/01_blur.pdf){width=93%}

Each panel images the same physical object at the same intensity.

::: notes
Original simulation of a dimensionless intensity target. The object and display scale are fixed. No detector sampling change occurs here. The system-response lecture introduces the Gaussian model formally.
:::

## Contrast and resolution

**Contrast** describes differences in recorded or displayed values between regions.

**Spatial resolution** describes the ability to distinguish nearby structures or fine spatial detail.

A feature can become difficult to see because blur reduces its contrast. Small pixel spacing alone does not guarantee fine resolution.

::: notes
Return to the blur figure in discussion rather than duplicate it. Ask whether the number of stored pixels determines the width of a blurred spot. The answer is no. Resolution requires a stated task or criterion, which the PSF and MTF will help describe.
:::

## In-class discussion

For each example, let's identify the physical signal and detector measurement.

1. An X-ray detector records a weaker transmitted signal at one location.
2. An ultrasound probe receives an echo later than a previous echo. What causes echoes? 
3. A PET scanner records a pair of photon detections on opposite sides of the scanner.

Which measurements directly identify a depth? Which need additional measurements or assumptions to fully reconstruct the object?

::: notes
Allow eight minutes for discussion and five for comparison. Suggested responses are in instructor_guide.md. These cases test physical reasoning, not clinical diagnosis. Do not require knowledge of attenuation coefficients or detector electronics.
:::

## Image formation in each modality

```{=latex}
\begingroup
\fontsize{22}{28}\selectfont
```

| Modality | Physical signal | How position is determined |
|:---|:---|:---|
| Visible-light camera | Reflected or emitted visible light | Lens maps light directions to sensor positions |
| Radiography | Transmitted X-ray photons | Projection geometry |
| CT | Transmitted X-ray photons | Many projection directions |
| Ultrasound | Reflected sound waves | Echo timing and beam direction |
| MRI | Radiofrequency electromagnetic signal | Magnetic-field gradients |
| PET | Annihilation photons | Coincidence measurements |

```{=latex}
\endgroup
```

::: notes
Use this as the debrief rather than a memorization list. The visible-light camera row describes how a lens maps scene directions to sensor positions in a two-dimensional image; a single conventional photograph generally does not determine depth. Reflectivity and color contribute to contrast, rather than identifying position. Sources for the medical modalities: NIBIB fact sheets linked on the final slide. MRI gradients will be explained later. Avoid suggesting that a single PET coincidence supplies a complete location.
:::

## Questions to consider before next time

1. What is the difference between detector data and a reconstructed image?
2. At a fixed field of view, what happens to pixel spacing when the pixel count doubles in each direction?
3. Why can an image with many pixels still appear blurred?

Next meeting: spatial signals, Fourier representations, and sampling.

::: notes
Allow five minutes. Expected answers: data are measurements and reconstruction estimates spatial quantities from those measurements; spacing halves along each axis and total pixel count quadruples; physical blur can spread information over neighboring locations before digitization.
:::

## Reading and resources

Prince and Links, *Medical Imaging: Signals and Systems*: introductory material on imaging modalities and image representation.

- [NIBIB: Medical X-rays](https://www.nibib.nih.gov/science-education/science-topics/medical-x-rays)
- [NIBIB: Computed tomography](https://www.nibib.nih.gov/science-education/science-topics/computed-tomography-ct)
- [NIBIB: Ultrasound](https://www.nibib.nih.gov/science-education/science-topics/ultrasound)
- [NIBIB: MRI](https://www.nibib.nih.gov/science-education/science-topics/magnetic-resonance-imaging-mri)
- [NIBIB: Nuclear medicine](https://www.nibib.nih.gov/science-education/science-topics/nuclear-medicine)

::: notes
Reference slide, outside the timed class plan. Reading is identified by topic because the course's textbook edition has not been specified. All plots in this deck are original illustrative simulations. No third-party figures have been reproduced.
:::
