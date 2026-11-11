---
title: "X-ray applications and CT"
date: ""
---

## When does a projection answer the question?

- **Chest radiography:** one projection can show the overall lung pattern and the position of tubes and lines.
- **Mammography:** a projection can show fine calcifications when there is enough contrast and resolution.
- **Fluoroscopy:** repeated projections show motion during a procedure.

When the question is **where within the body** a feature lies, overlapping structures can make a single view ambiguous.

::: notes
0–10 min for application recap, depth ambiguity, and CT hardware. Ask what changes if the same two objects exchange depths without changing their ray paths.
:::

## A projection and a slice answer different questions

:::: {.columns}
::: {.column width="45%"}
**Chest radiograph**

![Normal chest radiograph](photos/chest.jpg){height=90mm}
:::

::: {.column width="51%"}
**Chest CT slice**

![Axial CT slice of the chest](photos/ct-chest.jpg){height=90mm}
:::
::::

The projection combines structures along each ray. The slice shows their positions within one cross-section.

```{=latex}
\vskip 0pt plus 1filll
{\footnotesize\color{CourseGray}
Mikael Häggström\enspace\textperiodcentered\enspace \href{https://commons.wikimedia.org/wiki/File:Normal_posteroanterior_\%28PA\%29_chest_radiograph_\%28X-ray\%29.jpg}{Radiograph} and \href{https://commons.wikimedia.org/wiki/File:High-resolution_computed_tomograph_of_a_normal_thorax,_axial_plane_\%2854\%29.jpg}{CT slice}\enspace\textperiodcentered\enspace \href{https://creativecommons.org/publicdomain/zero/1.0/}{CC0 1.0}\par}
```

::: notes
These images are from different individuals. Point to the ribs and lungs in each. The radiograph combines depth along the beam and the axial CT image estimates attenuation at locations within a thin slice.
:::

## A CT scanner acquires views around the body

:::: {.columns}
::: {.column width="46%"}
![CT gantry with housing removed and components labeled](photos/ct-gantry.jpg){height=105mm}
:::

::: {.column width="51%"}
The **gantry** supports the X-ray tube and detector array. In this scanner they rotate together around the patient.

- **T:** tube
- **D:** detector array
- **X:** fan-shaped beam
- **R:** direction of rotation

:::
::::

```{=latex}
\vskip 0pt plus 1filll
{\footnotesize\color{CourseGray}
\href{https://commons.wikimedia.org/wiki/File:Ct-internals.jpg}{ChumpusRex}\enspace\textperiodcentered\enspace \href{https://creativecommons.org/licenses/by-sa/3.0/}{CC BY-SA 3.0}\par}
```

::: notes
This is an annotated photograph of a scanner with its housing removed. Real CT geometries use divergent rays. The rest of this lecture uses parallel rays to isolate the reconstruction idea.
:::

## Each ray gives a sum of attenuation along its path

Recall the two-layer result:

$$-\ln(I/I_0)=\mu_1x_1+\mu_2x_2.$$

For a ray through a slice with continuously varying attenuation,

$$p=-\ln(I/I_0)=\int_{\text{ray}}\mu(x,y)\,ds.$$

This is a **line integral**: add the local attenuation coefficient times a short distance along the ray.

::: notes
10–25 min for the line integral, one view and multiple views. This assumes a single photon energy and primary transmission. Real systems account for scatter and energy-dependent effects. p denotes projection value in this deck. Use units: mu is inverse length, ds is length, p is dimensionless.
:::

## One view gives a profile across the detector

![](figures/06_views.pdf){width=92%}

Each point on a profile is the line integral for a different ray through the same slice.

::: notes
Synthetic two-insert phantom. Left and right use perpendicular views. In one view the insert positions overlap along a ray. The other view separates them. The gray region represents a uniform background material.
:::

## A sinogram stacks the profiles by angle

![](figures/06_sinogram.pdf){width=77%}

Pick an insert. How does its detector position change as the view rotates?

::: notes
25–35 min. Each column is one view. Follow the feature at zero, 45 and 90 degrees and connect to its projected position. An off-center point traces a sinusoidal path in this parallel-beam model. Colors represent dimensionless line integrals.
:::

## Backprojection spreads each value along its ray

For each detector measurement, add its value back along the ray that produced it.

A single view gives stripes of possible locations. As views accumulate, rays from the same structure cross near that structure.

**Predict:** What happens to the contributions that extend beyond the object?

::: notes
35–55 min for backprojection builds and filter comparison. Contributions from other rays accumulate into a broad haze. This is a visual introduction rather than a derivation.
:::

## More views concentrate the signal

![](figures/06_backprojection.pdf){width=92%}

The inserts become easier to locate as views accumulate. Their edges still look broad.

::: notes
Three progressive snapshots using nested, uniformly spaced angle sets. Intensity is scaled for comparison to the same reference background region in the phantom. Point to radial contributions that persist around the inserts.
:::

## Filtering sharpens the reconstructed features

![](figures/06_reconstruction.pdf){width=92%}

**Filtered backprojection** filters each detector profile before spreading its values back along the rays.

Unfiltered brightness is scaled to match the reference background.

::: notes
The ramp filter weights higher spatial frequencies more strongly, compensating for the broad spread in unfiltered backprojection. It can also amplify high-frequency noise. This noiseless demonstration uses the same 180 views for both methods. Unfiltered backprojection is scaled to match a reference background region for visual comparison. FBP has attenuation units. No Fourier slice theorem derivation is needed.
:::

## Too few views leave streaks

![](figures/06_few_views.pdf){width=92%}

Both images use filtered backprojection. Which features in the sparse-view image are absent from the known object?

::: notes
55–65 min for sparse views, meaning of a slice, and exit question. Sparse views create angular undersampling artifacts. They are different from photon noise.
:::

## What does a CT pixel represent?

A reconstructed CT slice estimates the linear attenuation coefficient at locations within the slice.

Clinical images commonly express attenuation relative to water using **Hounsfield units (HU)**. The display maps a selected range of values to grayscale.

**Exit question:** What is the difference between a detector reading in one view and a pixel in a reconstructed slice?

::: notes
A view measures transmission along a ray. A reconstructed pixel estimates local attenuation from many views. Water is near 0 HU and air near -1000 HU. Adjusting the display range changes image appearance without changing the reconstructed data.
:::

## Reading and image sources

[IAEA, *Diagnostic Radiology Physics*](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1564webNew-74666420.pdf), chapters 6 and 11.

The projection and reconstruction examples use a synthetic two-insert object and an ideal parallel-beam model.

```{=latex}
\vskip 0pt plus 1filll
{\footnotesize\color{CourseGray}
CT gantry photograph by \href{https://commons.wikimedia.org/wiki/File:Ct-internals.jpg}{ChumpusRex}\enspace\textperiodcentered\enspace \href{https://creativecommons.org/licenses/by-sa/3.0/}{CC BY-SA 3.0}.\par}
```

