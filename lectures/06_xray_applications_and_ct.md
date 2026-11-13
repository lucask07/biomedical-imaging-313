---
title: "X-ray applications and CT"
date: ""
---

## When does a projection answer the question?

A projection is in single view of x-ray absorption.

- **Chest radiography:** one projection can show the overall lung pattern and the position of tubes and lines.
- **Mammography:** a projection can show fine calcifications when there is enough contrast and resolution.
- **Fluoroscopy:** repeated projections show motion during a procedure.

When the question is **where within the body** a feature lies, overlapping structures can make a single view ambiguous.

::: notes
0–12 min for applications, CT hardware, and detector rows. Ask what changes if the same two objects exchange depths without changing their ray paths.
:::

## A projection versus a slice

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

## One detector row samples a slice

![](figures/06_detector_geometry.pdf){width=99%}

::: notes
Allow about 3 minutes. In this ideal model the rays lie in the slice plane, which is perpendicular to the rotation axis. Each view uses the whole detector row. A single row can acquire successive slices if the table moves between scans. Multiple rows extend coverage along the rotation axis. Clinical multirow systems use diverging rays. The right panel illustrates coverage with parallel rays.
:::

## Each ray measures a sum of attenuation along its path

A **ray** is a unique direction of x-ray travel. 

Recall the two-layer result:

$$-\ln(I/I_0)=\mu_1x_1+\mu_2x_2.$$

For a ray through a slice with continuously varying attenuation,

$$p(s,\theta)=-\ln(I/I_0)=\int_{\text{ray}}\mu(x,y)\,d\ell.$$

This is a **line integral**: add the local attenuation coefficient times a short distance along the ray.

::: notes
12–25 min for projections, coordinates, and the sinogram. This assumes a single photon energy and primary transmission. Real systems account for scatter and energy-dependent effects. p denotes projection value in this deck. Use units: mu is inverse length, dℓ is distance along the ray, p is dimensionless.
:::

## Ray position on the detector

- $s$ is the signed position along the detector row, in mm. The central ray has $s=0$.
- $\theta$ is the angle of the detector coordinate measured from the $x$ axis. The rays run perpendicular to that coordinate.
- The ray through $(x,y)$ reaches detector position $s=x\cos\theta+y\sin\theta$.

At $0^\circ$, $s=x$ and the rays run parallel to $y$. At $90^\circ$, $s=y$ and the rays run parallel to $x$.

::: notes
Use the notebook's yellow rays to locate the insert centers. Those rays are examples. The profile uses the entire row. The object is a fixed 2D slice with a background disk and two higher-attenuation inserts. Tilting the plane through a 3D object would select a different slice.
:::

## One view (rotation) produces a profile across the detector

![](figures/06_views.pdf){width=92%}

Each point is a line integral of the linear absorption coefficient for a different ray through the same slice. One complete detector row gives one profile.

::: notes
Synthetic two-insert phantom. Left and right use perpendicular views. In one view the insert positions overlap along a ray. The other view separates them. The gray region represents a uniform background material.
:::

## Sinogram

![](figures/06_sinogram.pdf){width=77%}

Each column is one detector profile $p(s,\theta)$. Its values are dimensionless.

Follow the inserts. How does the position on the detector change as the view rotates?

::: notes
Finish the projection discussion here. Each column is one view. Follow the feature at zero, 45 and 90 degrees and connect to its projected position. An off-center point traces a sinusoidal path in this parallel-beam model. Colors represent dimensionless line integrals.
:::

## Backprojection spreads each value along its ray

For each detector measurement, add its value back along the ray that produced it. That's the best we can do! 

A single view gives stripes of possible locations. As views accumulate, rays from the same structure cross near that structure.

::: notes
25–42 min for backprojection and the ramp-filter walkthrough. Contributions from other rays accumulate into a broad haze. This is a visual introduction rather than a derivation.
:::

## More views better localize the signal

![](figures/06_backprojection.pdf){width=92%}

The inserts become easier to locate as views accumulate. Their edges still look broad.

::: notes
Three progressive snapshots using nested, uniformly spaced angle sets. Intensity is scaled for comparison to the same reference background region in the phantom. Point to radial contributions that persist around the inserts.
:::

## High-pass filtering sharpens the reconstruction

![](figures/06_reconstruction.pdf){width=92%}

**Filtered backprojection** filters each detector profile before spreading its values back along the rays.

Unfiltered brightness is scaled to match the reference background.

::: notes
The ramp filter weights higher spatial frequencies more strongly, compensating for the broad spread in unfiltered backprojection. It can also amplify high-frequency noise. This noiseless demonstration uses the same 180 views for both methods. Unfiltered backprojection is scaled to match a reference background region for visual comparison. FBP has attenuation units. No Fourier slice theorem derivation is needed.
:::

## Filter across detector position

For a fixed view $\theta$, Fourier transform the detector profile **along $s$**. The spatial frequency $u$ is in cycles/mm.

$$P(u,\theta)=\mathcal F_s\{p(s,\theta)\},\qquad
q(s,\theta)=\mathcal F_s^{-1}\{|u|P(u,\theta)\}.$$

![](figures/06_filter_steps.png){height=78mm}

The ramp $|u|$ gives higher spatial frequencies more weight. Apply it to each sinogram column independently.

::: notes
Use the notebook's 90-degree example. The ramp plot shows nonnegative frequencies. Negative values in the filtered profile help cancel the broad blur from ordinary backprojection. High-frequency noise can also be amplified. See Kak and Slaney, chapter 3.
:::

## One view's contribution to the slice

For each pixel $(x,y)$, sum the filtered values along the rays through it.

$$\hat\mu(x,y)\approx\Delta\theta\sum_{j=1}^{N}
q(x\cos\theta_j+y\sin\theta_j,\theta_j),\qquad\Delta\theta=\pi/N.$$

![](figures/06_view_sum.png){height=71mm}

At $90^\circ$, $s=y$ and the rays run horizontally. The left panel shows signed contributions in $\mathrm{mm}^{-1}$. Each panel spans $-63$ to $+63$ mm along $x$ and $y$.

::: notes
The image coordinates x and y are distances in mm from the rotation center. The panels show -63 to +63 mm in each direction. Only the left panel uses the signed color scale. The two grayscale panels share a display range. The notebook interpolates the profile between detector samples. Delta theta is in radians.
:::

## Too few views leave streaks

![](figures/06_few_views.pdf){width=92%}

Both images use filtered backprojection. 

::: notes
42–60 min for the guided CT notebook. Compare 0 and 90 degrees and reconstruct with 12 and 180 views. Use this slide to connect sparse views to streaks. Sparse views create angular undersampling artifacts. They are different from photon noise.
:::

## What does a CT pixel represent?

A reconstructed CT slice estimates the linear attenuation coefficient at locations within the slice.

Clinical images commonly express attenuation relative to water using **Hounsfield units (HU)**. The display maps a selected range of values to grayscale.

What is the difference between a detector reading in one view and a pixel in a reconstructed slice?

::: notes
60–65 min for HU and the exit question. A view measures transmission along a ray. A reconstructed pixel estimates local attenuation from many views. Water is near 0 HU and air near -1000 HU. Adjusting the display range changes image appearance without changing the reconstructed data.
:::

## Reading and image sources

[IAEA, *Diagnostic Radiology Physics*](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1564webNew-74666420.pdf), chapters 6 and 11.

The projection and reconstruction examples use a synthetic two-insert object and an ideal parallel-beam model.

```{=latex}
\vskip 0pt plus 1filll
{\footnotesize\color{CourseGray}
CT gantry photograph by \href{https://commons.wikimedia.org/wiki/File:Ct-internals.jpg}{ChumpusRex}\enspace\textperiodcentered\enspace \href{https://creativecommons.org/licenses/by-sa/3.0/}{CC BY-SA 3.0}.\par}
```

