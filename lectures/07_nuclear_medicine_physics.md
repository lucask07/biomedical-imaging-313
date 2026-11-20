---
title: "Physics of nuclear medicine"
date: ""
---

## Radiotracers

A **radiotracer** combines a radioactive label with a substance that follows a process in the body.

- The distribution of the tracer depends on the process being studied.
- The radioactive label supplies a signal that can be detected outside the body.
- The X-ray imaging modality is *transmission*. Nuclear imaging is *emission*. 


::: notes
0–8 min. Contrast an external transmission beam with emission from inside the body. Example: a tracer that concentrates in bone can reveal patterns of bone turnover. The tracer may also move or clear biologically.
:::

## What changes when a nucleus decays?

An **isotope** is a form of an element with a particular number of neutrons.

- $Z$ counts protons and identifies the element.
- $A$ counts protons plus neutrons.
- In $^{99\mathrm{m}}\mathrm{Tc}$, $99$ is the mass number and **m** indicates a long-lived excited state.

A **radionuclide** has an unstable nucleus. Its decay can change the element or leave the same nucleus at a lower energy.

::: notes
8–23 min for nuclear notation and both schematic decay diagrams. Distinguish mass number A in nuclide notation from activity A(t).
:::

## Common decay products

- **positron** the antiparticle of an electron but with positive charge (charge +1e, same mass and spin as electron)
- **alpha particle** Same as helium, 2 protons, 2 neutrons. Energy of 5 MeV, velocity of 4% the speed of light. Dangerous radioactive effects inside body. 
- **gamma ray** E&M radiation just like x-rays. The distinction is that $\gamma$ rays are from the nucleus, x-rays are from the electron cloud. Gamma rays are typically higher energy.  

::: notes

:::

## Gamma emission from nuclear excited state decay

Technetium-99m is one of the most common nuclear medical particles (m for metastable).
A simplified decay diagram for technetium-99m:

$$
\begin{array}{c}
{}^{99\mathrm{m}}\mathrm{Tc}\quad\text{excited state}\\
\downarrow\quad\text{de-excitation}\\
{}^{99}\mathrm{Tc}\quad\text{lower-energy state}
\end{array}
\qquad E_\gamma\approx 140~\mathrm{keV}.
$$

The photon can leave the body and be measured by a gamma camera.

Notice that the total number of protons or neutrons change did not change. The radiation dose is equivalent to about 500 chest x-rays. 

::: notes
No. Show the main imaging photon, not the full evaluated level scheme. Some transitions transfer energy to an electron through internal conversion.
:::

## PET: Positron emission produces a photon pair

A simplified decay diagram for fluorine-18:

$$^{18}\mathrm F \;\longrightarrow\;{}^{18}\mathrm O + e^+ + \nu_e.$$

A proton in the fluorine nucleus converts to a positron + neutron + neutrino. The positron loses kinetic energy in tissue. It typically annihilates with an electron and produces two photons traveling in nearly opposite directions.

$$E_\gamma \approx m_e c^2=511~\mathrm{keV}\quad\text{per photon}.$$

::: notes
The positron travels before annihilation. Explain that beta-plus decay changes a proton to a neutron in the nucleus, keeping the mass number fixed. The neutrino carries some energy. The equation shows the positron branch. Neglect residual kinetic energy for the annihilation calculation.
:::

## Activity and decay rate

Each radioactive nucleus has a constant probability per unit time of decaying. The expected remaining number $N(t)$ follows

$$N(t)=N_0 e^{-\lambda t},\qquad A(t)=\lambda N(t).$$

**Activity**: $A$ is the expected number of decays per second. One becquerel (Bq) is one decay per second.

**Half-life**: the time for the activity to reduce by $\frac{1}{2}$ 
$$T_{1/2}=\frac{\ln 2}{\lambda},\qquad A(t)=A_0\,2^{-t/T_{1/2}}.$$

::: notes
23–40 min for decay, example, and photon counts. Relate the exponential to a first-order system. Physical decay is set by the radionuclide. Changing tracer concentration in an organ can also reflect biological movement or clearance.
:::

## Activity versus time

Technetium-99m has a physical half-life of about $6$ h. A sample has activity $80$ MBq now.

1. What is its activity after $12$ h?
2. What is its activity after $3$ h?
3. In a closed sample, why does the same fraction decay in each successive $6$ h interval?

Note: 1 Ci = 3.7$\times$ $10^{10}$ Bq = 37 GBq

::: notes
20 MBq at 12 h. About 56.6 MBq at 3 h (80*2**(-1/2)). A fixed decay probability per parent nucleus gives the constant fractional change. Values are illustrative.
:::

## Decays, emitted photons, and counts

For a short interval $T$ compared with the half-life, a simple single-photon model gives the average number of counts as

$$\bar C\approx A\,T\,Y\,\varepsilon.$$

- $Y$ is the mean number of photons of interest emitted per decay.
- $\varepsilon$ is the probability that such a photon produces a detectable count count.

**Estimate.** If $A=1$ MBq, $T=10$ s, $Y=0.9$, and $\varepsilon=10^{-4}$, how many counts do we expect?

::: notes
900 counts. Efficiency here includes escape, geometry, detection, and acceptance. Distinguish decay rate from counts per second. Poisson approximation gives SD about 30 counts.
:::

## Gamma photon to an electrical pulse

A scintillation detector converts deposited energy into a flash of light. A photomultiplier tube (PMT) or silicon photomultiplier (SiPM) converts that light into an electrical pulse.

What can we learn from detector measurements? 

- **Pulse height** estimates the energy deposited.
- **Timestamp** estimates when the event arrived.
- **Relative pulse heights** The camera compares the pulse heights of nearby light sensors to estimate where the photon interacted in the crystal.

For what mechanisms does a photon deposit only part of its energy?

::: notes
40–55 min. A Compton interaction can leave recoil energy in the crystal while the outgoing photon escapes. A PMT uses a photocathode and electron multiplication. A SiPM uses avalanche microcells. Distinguish crystal light yield from conversion of light into charge.
:::

## Pulse height depends on deposited energy

Many events form a **pulse-height spectrum**.

- Full-energy deposits cluster near the emitted photon energy. This cluster is the **photopeak**.
- Partial deposits give smaller pulses.
- Statistical fluctuations and electronics give the peak a finite width.

A pulse processor can accept only heights within a chosen **energy window**.

::: notes
55–62 min. Ask why photon energy for a radionuclide can be well defined even though the measured peak has a width. Energy selection returns in planar imaging.
:::

## Example Problems: \#1, (Prince and Links)

Show that $1~\mathrm{u}\,c^2$ is about $931~\mathrm{MeV}$. 

1 u is $1/12$ the mass of carbon-12. 
A proton is 1.007276 u so that 1 u is (1.67262192 $\times 10^{-27}$ kg)/1.007276 = $1.6605 \times 10^{-27}$ kg.

$$
\begin{aligned}
E &= mc^2\\
  &\approx (1.6605\times10^{-27})(2.99792\times10^8)^2~\mathrm{J}\\
  &\approx 1.4924\times10^{-10}~\mathrm{J}\\
  &\approx 9.315\times10^8~\mathrm{eV}
   = 931.5~\mathrm{MeV}.
\end{aligned}
$$

using $1.6021767\times 10^{-19}$ J/eV

## Example Problems: \#2, (Prince and Links)

A deuteron has 1 proton (1.007276 u) and 1 neutron (1.008665 u) and a mass of 2.01355 u. Compute its mass defect and binding energy. 

The **mass defect** is the difference between the sum of the masses of the constituent particles and the actual mass. The binding energy is $E_b=\Delta m c^2$. 


Mass defect: $1.007276 + 1.008665 - 2.01355 = 0.002391 u$ 

Binding energy: $E_b\approx (0.002391)(931.5~\mathrm{MeV})=2.23~\mathrm{MeV}$.

## Example Problems: \#3, (Prince and Links)

Suppose there are $10^9$ radioactive atoms in a sample of iodine-123, which has a half-life of 13 hours.

(a) What is the initial activity?
(b) How many radioactive atoms are expected to remain after 24 hours?
(c) What is the probability that exactly $10^8$ radioactive atoms remain after 24 hours?

## Example Problems: \#3 part a, (Prince and Links)

What is the initial activity?

$$\lambda=\frac{\ln 2}{T_{1/2}}=\frac{\ln 2}{13~\mathrm{h}}
\approx 0.0533~\mathrm{h}^{-1}.$$

$$A_0=\lambda N_0\approx 5.33\times10^7~\mathrm{decays/h}
\approx 14.8~\mathrm{kBq}.$$

One becquerel is one decay per second.

## Example Problems: \#3 part b, (Prince and Links)

How many atoms are expected to remain after 24 hours?

The probability that one atom survives 24 hours is

$$p=2^{-24/13}\approx 0.2781.$$

The expected number remaining is

$$\overline N=N_0p\approx 2.78\times10^8~\mathrm{atoms}.$$

## Example Problems: \#3 part c, (Prince and Links)

If the atoms decay independently, the number remaining follows a **binomial distribution** with $N_0=10^9$ atoms and survival probability $p=0.2781$.

$$\sigma_N=\sqrt{N_0p(1-p)}\approx 14{,}200~\mathrm{atoms}.$$

The count $10^8$ is far below the mean of $2.78\times10^8$. The probability of **exactly** $10^8$ remaining is effectively zero.

**Discuss.** What if the question asked for **at least** $10^8$?

::: notes
The probability of at least 100 million is effectively one. The integral of the activity over 24 h gives the expected number of decays, 7.22e8. It provides a check on the mean but does not give the probability of an exact survivor count.
:::

## Exit question

A tracer has a half-life of $6$ h. The camera records far fewer counts per second than the sample has decays per second. Which quantities would you need to predict the camera count rate?



[IAEA, *Nuclear Medicine Physics*](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1617web-1294055.pdf)

::: notes
62–65 min. Expected activity at scan time, photon yield and overall acceptance. Suggested reading: Prince and Links, chapter 7.
:::

