---
title: "4 Transport Phenomena"
abstract: "This chapter develops the semiclassical transport theory of metals and semiconductors, starting from the Boltzmann equation and the relaxation-time approximation. It derives the electrical conductivity tensor (the Drude formula) for both metals and intrinsic semiconductors, generalizes the result to ellipsoidal carrier pockets, treats electrons and holes in intrinsic and doped semiconductors via the grand canonical ensemble, and concludes with the characterization of semiconductors through carrier density and mobility."
---

# 4 Transport Phenomena

## 4.0 Overview

The transport properties of solids are central to solid state physics because they can be measured on nearly all materials and therefore provide a valuable tool for characterizing materials. In this chapter we study some of the electrical and thermal transport properties for metals and semiconductors, beginning with the Boltzmann transport equation and its solution in the relaxation-time approximation, and applying the results to metals, intrinsic semiconductors, and doped (extrinsic) semiconductors.

**References:**

* Ziman, *Principles of the Theory of Solids*, Cambridge Univ. Press, 1972, Chapters 7 and 9.
* Ashcroft and Mermin, *Solid State Physics*, Holt, Rinehart and Winston, 1976, Chapter 13.
* Smith, Janak and Adler, *Electronic Conduction in Solids*, McGraw-Hill, 1967, Chapters 7, 8, and 9.

## 4.1 Introduction

In this section we study some of the transport properties for metals and semiconductors. An intrinsic semiconductor at $T = 0$ has no carriers and therefore there is no transport of carriers under the influence of external fields. However at finite temperatures there are thermally generated carriers. Impurities also can serve to generate carriers and transport properties. For insulators, there is very little charge transport and in this case, the defects and the ions themselves can participate in charge transport under the influence of external applied fields. Metals make use of the Fermi-Dirac distribution function but are otherwise similar to semiconductors, for which the Maxwell-Boltzmann distribution function is usually applicable.

At finite fields, the electrical conductivity will depend on the product of the carrier density and the carrier mobility. For a one carrier system, the Hall effect gives the carrier density and the magnetoresistance gives the mobility, the key parameters governing the transport properties of a semiconductor. From the standpoint of device applications, the carrier density and the carrier mobility are the parameters of greatest importance.

To the extent that electrons can be considered as particles, the electrical conductivity, the electronic contribution to the thermal conductivity and the magnetoresistance are all found by solving the Boltzmann equation. For the case of nano-scale systems, where the wave aspects of the electron must be considered (called mesoscopic physics), more sophisticated approaches to the transport properties must be considered. To review the standard procedures for classical electrons, we briefly review the Boltzmann equation and its solution in the next section.

## 4.2 The Boltzmann Equation

The Boltzmann transport equation is a statement that in the steady state, there is no net change in the distribution function $f(\vec{r},\vec{k},t)$ which determines the probability of finding an electron at position $\vec{r}$, crystal momentum $\vec{k}$ and time $t$. Therefore we get a zero sum for the changes in $f(\vec{r},\vec{k},t)$ due to the 3 processes of diffusion, the effect of forces and fields, and collisions:

```{math}
:label: eq-p1-ch04-1
\frac{\partial f(\vec{r},\vec{k},t)}{\partial t}\Big|_{\text{diffusion}}
+ \frac{\partial f(\vec{r},\vec{k},t)}{\partial t}\Big|_{\text{fields}}
+ \frac{\partial f(\vec{r},\vec{k},t)}{\partial t}\Big|_{\text{collisions}}
= 0 .
```

It is customary to substitute the following differential form for the diffusion process

```{math}
:label: eq-p1-ch04-2
\frac{\partial f(\vec{r},\vec{k},t)}{\partial t}\Big|_{\text{diffusion}}
= -\vec{v}(\vec{k})\cdot \frac{\partial f(\vec{r},\vec{k},t)}{\partial \vec{r}}
```

which expresses the continuity equation in real space in the absence of forces, fields and collisions. For the forces and fields, we write correspondingly

```{math}
:label: eq-p1-ch04-3
\frac{\partial f(\vec{r},\vec{k},t)}{\partial t}\Big|_{\text{fields}}
= -\dot{\vec{k}}\cdot \frac{\partial f(\vec{r},\vec{k},t)}{\partial \vec{k}}
```

and by combining {eq}`eq-p1-ch04-1`, {eq}`eq-p1-ch04-2`, and {eq}`eq-p1-ch04-3`, we obtain the Boltzmann equation:

```{math}
:label: eq-p1-ch04-4
\frac{\partial f(\vec{r},\vec{k},t)}{\partial t}
+ \vec{v}(\vec{k})\cdot\frac{\partial f(\vec{r},\vec{k},t)}{\partial \vec{r}}
+ \dot{\vec{k}}\cdot\frac{\partial f(\vec{r},\vec{k},t)}{\partial \vec{k}}
= \frac{\partial f(\vec{r},\vec{k},t)}{\partial t}\Big|_{\text{collisions}}
```

which includes derivatives for all the variables of the distribution function on the left hand side of the equation and the collision terms appear on the right hand side of {eq}`eq-p1-ch04-4`. The first term in {eq}`eq-p1-ch04-4` gives the explicit time dependence of the distribution function and is needed for the solution of ac driving forces or for impulse perturbations. Boltzmann's equation is usually solved using two approximations:

1. The perturbation due to external fields and forces is assumed to be small so that the distribution function can be linearized and written as:

```{math}
:label: eq-p1-ch04-5
f(\vec{r},\vec{k}) = f_0(E) + f_1(\vec{r},\vec{k})
```

where $f_0(E)$ is the equilibrium distribution function (the Fermi function) which depends only on the energy $E$, while $f_1(\vec{r},\vec{k})$ is the perturbation term giving the departure from equilibrium.

2. The collision term in the Boltzmann equation is written in the relaxation time approximation so that the system returns to equilibrium uniformly:

```{math}
:label: eq-p1-ch04-6
\frac{\partial f}{\partial t}\Big|_{\text{collisions}}
= -\frac{f - f_0}{\tau}
= -\frac{f_1}{\tau}
```

where $\tau$ denotes the relaxation time and in general is a function of crystal momentum, i.e., $\tau = \tau(\vec{k})$. The physical interpretation of the relaxation time is the time associated with the rate of return to the equilibrium distribution when the external fields or thermal gradients are switched off. Solution to {eq}`eq-p1-ch04-6` when the fields are switched off at $t = 0$ leads to

```{math}
:label: eq-p1-ch04-7
\frac{\partial f}{\partial t} = -\frac{f - f_0}{\tau}
```

which has solutions

```{math}
:label: eq-p1-ch04-8
f(t) = f_0 + \big[ f(0) - f_0 \big]\, e^{-t/\tau}
```

where $f_0$ is the equilibrium distribution and $f(0)$ is the distribution function at time $t = 0$. The relaxation previously described by {eq}`eq-p1-ch04-8` follows a Poisson distribution, indicating that collisions relax the distribution function exponentially to $f_0$ with a time constant $\tau$.

With these approximations, the Boltzmann equation is solved to find the distribution function which in turn determines the number density and current density. The current density $\vec{j}(\vec{r},t)$ is given by

```{math}
:label: eq-p1-ch04-9
\vec{j}(\vec{r},t) = \frac{e}{4\pi^3}\int \vec{v}(\vec{k})\, f(\vec{r},\vec{k},t)\, d^3k
```

in which the crystal momentum $\hbar\vec{k}$ plays the role of the momentum $\vec{p}$ in specifying a volume in phase space. Every element of size $h$ (Planck's constant) in phase space can accommodate one spin $\uparrow$ and one spin $\downarrow$ electron. The carrier density $n(\vec{r},t)$ is thus simply given by integration of the distribution function over k-space

```{math}
:label: eq-p1-ch04-10
n(\vec{r},t) = \frac{1}{4\pi^3}\int f(\vec{r},\vec{k},t)\, d^3k
```

where $d^3k$ is an element of 3D wavevector space. The velocity of a carrier with crystal momentum $\hbar\vec{k}$ is related to the $E(\vec{k})$ dispersion expression by

```{math}
:label: eq-p1-ch04-11
\vec{v}(\vec{k}) = \frac{1}{\hbar}\frac{\partial E(\vec{k})}{\partial \vec{k}}
```

and $f_0(E)$ is the Fermi distribution function

```{math}
:label: eq-p1-ch04-12
f_0(E) = \frac{1}{1 + e^{(E - E_F)/k_B T}}
```

which defines the equilibrium state in which $E_F$ is the Fermi energy and $k_B$ is the Boltzmann constant.

## 4.3 Electrical Conductivity

To calculate the static electrical conductivity, we consider an applied electric field $\vec{E}$ which for convenience we will take to be along the x-direction. We will assume for the present that there is no magnetic field and that there are no thermal gradients present. The electrical conductivity is expressed in terms of the conductivity tensor $\overleftrightarrow{\sigma}$ which is evaluated explicitly from the relation

```{math}
:label: eq-p1-ch04-13
\vec{j} = \overleftrightarrow{\sigma}\cdot \vec{E} ,
```

from solution of {eq}`eq-p1-ch04-9`, using $\vec{v}(\vec{k})$ from {eq}`eq-p1-ch04-11` and the distribution function $f(\vec{r},\vec{k},t)$ from solution of the Boltzmann equation represented by {eq}`eq-p1-ch04-4`. The first term in {eq}`eq-p1-ch04-4` vanishes since the dc applied field $\vec{E}$ has no time dependence.

For the second term in the Boltzmann equation {eq}`eq-p1-ch04-4`, $\vec{v}(\vec{k})\cdot \partial f(\vec{r},\vec{k},t)/\partial\vec{r}$, we note that

```{math}
:label: eq-p1-ch04-14
\frac{\partial f}{\partial \vec{r}} \simeq \frac{\partial f_0}{\partial \vec{r}}
= \frac{\partial f_0}{\partial T}\frac{\partial T}{\partial \vec{r}} .
```

Since there are no thermal gradients present in the simplest calculation of the electrical conductivity given in this section, this term does not contribute to {eq}`eq-p1-ch04-4`. For the third term in {eq}`eq-p1-ch04-4`, which we write as

```{math}
:label: eq-p1-ch04-15
\dot{\vec{k}}\cdot\frac{\partial f(\vec{r},\vec{k},t)}{\partial \vec{k}}
= \sum_\alpha \dot{k}_\alpha \frac{\partial f(\vec{r},\vec{k},t)}{\partial k_\alpha}
```

where the right hand side shows the summation over the vector components, we do get a contribution, since the equations of motion ($F = ma$) give

```{math}
:label: eq-p1-ch04-16
\hbar\dot{\vec{k}} = e\vec{E}
```

and

```{math}
:label: eq-p1-ch04-17
\frac{\partial f(\vec{r},\vec{k},t)}{\partial \vec{k}}
= \frac{\partial (f_0 + f_1)}{\partial \vec{k}}
= \frac{\partial f_0}{\partial E}\frac{\partial E}{\partial \vec{k}} + \frac{\partial f_1}{\partial \vec{k}} .
```

In considering the linearized Boltzmann equation, we retain only the leading terms in the perturbing electric field, so that $(\partial f_1/\partial\vec{k})$ can be neglected and only the term $(\partial f_0/\partial E)\hbar\vec{v}(\vec{k})$ need be retained. We thus obtain the linearized Boltzmann equation for the case of an applied static electric field and no thermal gradients:

```{math}
:label: eq-p1-ch04-18
\dot{\vec{k}}\cdot\frac{\partial f(\vec{r},\vec{k},t)}{\partial \vec{k}}
= \frac{\varphi}{\tau}\frac{\partial f_0}{\partial E}
= -\frac{f_1}{\tau}
```

where it is convenient to write:

```{math}
:label: eq-p1-ch04-19
f_1 = -\varphi\,\frac{\partial f_0}{\partial E}
```

in order to show the $(\partial f_0/\partial E)$ dependence explicitly. Substitution of {eq}`eq-p1-ch04-16` and {eq}`eq-p1-ch04-17` into {eq}`eq-p1-ch04-18` yields

```{math}
:label: eq-p1-ch04-20
\left[ \frac{e\vec{E}}{\hbar}\left(\frac{\partial f_0}{\partial E}\right) \right]\cdot [\hbar\vec{v}(\vec{k})]
= \frac{\varphi(\vec{k})}{\tau}\left(\frac{\partial f_0}{\partial E}\right)
```

so that

```{math}
:label: eq-p1-ch04-21
\varphi(\vec{k}) = e\tau\,\vec{E}\cdot\vec{v}(\vec{k}) .
```

Thus we can relate $\varphi(\vec{k})$ to $f_1(\vec{k})$ by

```{math}
:label: eq-p1-ch04-22
f_1(\vec{k}) = -\varphi(\vec{k})\frac{\partial f_0(E)}{\partial E}
= -e\tau\,\vec{E}\cdot\vec{v}(\vec{k})\,\frac{\partial f_0(E)}{\partial E} .
```

The current density is then found from the distribution function $f(\vec{k})$ by calculation of the average value of $\langle n e\vec{v}\rangle$ over all k-space

```{math}
:label: eq-p1-ch04-23
\vec{j} = \frac{1}{4\pi^3}\int e\vec{v}(\vec{k})\, f(\vec{k})\, d^3k
= \frac{1}{4\pi^3}\int e\vec{v}(\vec{k})\, f_1(\vec{k})\, d^3k
```

since

```{math}
:label: eq-p1-ch04-24
\int e\vec{v}(\vec{k})\, f_0(\vec{k})\, d^3k = 0 .
```

Equation {eq}`eq-p1-ch04-24` states that no net current flows in the absence of an applied electric field, another statement of the equilibrium condition. Substitution for $f_1(\vec{k})$ given by {eq}`eq-p1-ch04-22` into {eq}`eq-p1-ch04-23` for $\vec{j}$ yields

```{math}
:label: eq-p1-ch04-25
\vec{j} = -\frac{e^2 \vec{E}}{4\pi^3}\cdot \int \tau\,\vec{v}\,\vec{v}\,\frac{\partial f_0}{\partial E}\, d^3k
```

where in general $\tau = \tau(\vec{k})$ and $\vec{v}$ is given by {eq}`eq-p1-ch04-11`. A comparison of {eq}`eq-p1-ch04-25` and {eq}`eq-p1-ch04-13` thus yields the desired result for the conductivity tensor $\overleftrightarrow{\sigma}$

```{math}
:label: eq-p1-ch04-26
\overleftrightarrow{\sigma} = -\frac{e^2}{4\pi^3}\int \tau\,\vec{v}\,\vec{v}\,\frac{\partial f_0}{\partial E}\, d^3k
```

where $\overleftrightarrow{\sigma}$ is a symmetric second rank tensor ($\sigma_{ij} = \sigma_{ji}$). The evaluation of the integral in {eq}`eq-p1-ch04-26` over all k-space depends on the $E(\vec{k})$ relations through the $\vec{v}\,\vec{v}$ terms and the temperature dependence comes through the $\partial f_0/\partial E$ term. We will in §4.4 evaluate {eq}`eq-p1-ch04-26` for a simple example of a metal, and in §4.5 do the same for an intrinsic semiconductor.

## 4.4 Electrical Conductivity of Metals

To exploit the energy dependence of $(\partial f_0/\partial E)$ in applying {eq}`eq-p1-ch04-26` to metals, it is more convenient to evaluate $\overleftrightarrow{\sigma}$ if we replace $\int d^3k$ with an integral over the constant energy surfaces

```{math}
:label: eq-p1-ch04-27
\int d^3k = \int d^2S\, dk_\perp \equiv \int \frac{d^2S\, dE}{|\partial E/\partial \vec{k}|} .
```

Thus {eq}`eq-p1-ch04-26` is written as

```{math}
:label: eq-p1-ch04-28
\overleftrightarrow{\sigma} = -\frac{e^2}{4\pi^3}\int \tau\,\frac{\vec{v}\,\vec{v}}{|\partial E/\partial \vec{k}|}\,\frac{\partial f_0}{\partial E}\, d^2S\, dE .
```

From the Fermi-Dirac distribution function $f_0(E)$ shown in {numref}`fig-p1-ch04-1`, we see that the derivative $(-\partial f_0/\partial E)$ can approximately be replaced by a $\delta$-function for the case of a metal, so that {eq}`eq-p1-ch04-28` can be written as

```{math}
:label: eq-p1-ch04-29
\overleftrightarrow{\sigma} = \frac{e^2}{4\pi^3\hbar}\int_{\text{Fermi surface}} \tau\,\vec{v}\,\vec{v}\,\frac{d^2S}{v} .
```

For a cubic crystal, $[v_x v_x] = v^2/3$ and thus $\overleftrightarrow{\sigma}$ has only diagonal components $\sigma$ that are all equal to each other:

```{math}
:label: eq-p1-ch04-30
\sigma = \frac{e^2}{4\pi^3\hbar}\int_{\text{Fermi surface}} \frac{\tau v\, d^2S}{3}
= \frac{n e^2\tau}{m^*}
```

since

```{math}
:label: eq-p1-ch04-31
n = (1/4\pi^3)(4\pi/3)k_F^3
```

and

```{math}
:label: eq-p1-ch04-32
v_F = \hbar k_F/m .
```

The result

```{math}
:label: eq-p1-ch04-33
\sigma = n e^2\tau/m^*
```

is called the Drude formula for the dc electrical conductivity. Generalization of this methodology to metals with anisotropic Fermi surfaces or with more than one type of carrier can be done directly and requires numerical calculations in most cases.

:::{figure} images/fig-p1-ch04-1.png
:name: fig-p1-ch04-1
:align: center
:width: 70%

Schematic plot of $f_0(E)$ and $-\partial f_0(E)/\partial E$ for a metal showing the $\delta$-function-like behavior near the Fermi level $E_F$ for the derivative.
:::

## 4.5 Electrical Conductivity of Semiconductors

We show in this section that the simple Drude model $\sigma = ne^2\tau/m^*$ can also be recovered for a semiconductor from the general relation given by {eq}`eq-p1-ch04-26`, using a simple parabolic band model and a constant relaxation time approximation. When a more complete theory is used, departures from the simple Drude model will result.

In deriving the Drude model for a semiconductor we make three approximations:

* **Approximation #1**

In the case of electron states in intrinsic semiconductors having no donor or acceptor impurities, we have the condition $(E - E_F) \gg k_B T$ since $E_F$ is in the band gap and $E$ is the energy of an electron in the conduction band, as shown in {numref}`fig-p1-ch04-2`.

:::{figure} images/fig-p1-ch04-2.png
:name: fig-p1-ch04-2
:align: center
:width: 80%

Electron and hole states in the conduction and valence bands of an intrinsic semiconductor. (a) Location of $E_F$ in an intrinsic semiconductor. (b) The corresponding density of states for electrons and holes. (c) The Fermi functions for electrons (solid curve) and holes (dashed curve). (d) The occupation of electron and hole states in an intrinsic semiconductor.
:::

Thus, the first approximation is equivalent to writing

```{math}
:label: eq-p1-ch04-34
f_0(E) = \frac{1}{1 + \exp[(E - E_F)/k_B T]} \simeq \exp[-(E - E_F)/k_B T]
```

which is equivalent to using the Maxwell-Boltzmann distribution in place of the full Fermi-Dirac distribution. Since $E$ is usually measured with respect to the bottom of the conduction band, $E_F$ is a negative energy and it is therefore convenient to write $f_0(E)$ as

```{math}
:label: eq-p1-ch04-35
f_0(E) \simeq e^{-|E_F|/k_B T}\, e^{-E/k_B T}
```

so that the derivative of the Fermi function becomes

```{math}
:label: eq-p1-ch04-36
\frac{\partial f_0(E)}{\partial E}
= -e^{-|E_F|/k_B T}\,\frac{1}{k_B T}\, e^{-E/k_B T} .
```

* **Approximation #2**

For simplicity we assume a constant relaxation time $\tau$ that is independent of $\vec{k}$ and $E$. This approximation is made for simplicity and may not be valid for specific cases. Some common scattering mechanisms yield an energy-dependent relaxation time, such as acoustic deformation potential scattering or ionized impurity scattering, where $r = -1/2$ and $r = +3/2$, respectively, in the relation $\tau = \tau_0(E/k_B T)^r$.

* **Approximation #3**

To illustrate the explicit evaluation of the integral in {eq}`eq-p1-ch04-26`, we consider the simplest case, assuming an isotropic, parabolic band $E = \hbar^2 k^2/2m^*$ for the evaluation of $\vec{v} = \partial E/\hbar\partial\vec{k}$ about the conduction band extremum.

```{math}
:label: eq-p1-ch04-37
\vec{v}\,\vec{v} = \frac{1}{3}v^2\,\overleftrightarrow{1},\qquad
k^2 = 2m^*E/\hbar^2,\qquad
2k\,dk = 2m^*\,dE/\hbar^2,\qquad
v^2 = 2E/m^*,\qquad
v = \hbar k/m^*
```

where $\overleftrightarrow{1}$ is the unit second rank tensor. We next convert {eq}`eq-p1-ch04-26` to an integration over energy and write

```{math}
:label: eq-p1-ch04-38
d^3k = 4\pi k^2\,dk = 4\pi\sqrt{2}\,(m^*/\hbar^2)^{3/2}\sqrt{E}\,dE
```

so that {eq}`eq-p1-ch04-26` becomes

```{math}
:label: eq-p1-ch04-39
\sigma = \frac{e^2\tau}{4\pi^3}\left[\frac{8\sqrt{2\pi}\,\sqrt{m^*}}{3\hbar^3 k_B T}\right]
e^{-|E_F|/k_B T}\int_0^\infty E^{3/2}\,dE\,e^{-E/k_B T}
```

in which the integral over energy $E$ is extended to $\infty$ because there is negligible contribution for large $E$ and because the definite integral

```{math}
:label: eq-p1-ch04-40
\int_0^\infty x^p\,dx\,e^{-x} = \Gamma(p + 1)
```

can be evaluated exactly, $\Gamma(p)$ being the $\Gamma$ function which has the property

```{math}
:label: eq-p1-ch04-41
\Gamma(p + 1) = p\,\Gamma(p),\qquad \Gamma(1/2) = \sqrt{\pi} .
```

Substitution into {eq}`eq-p1-ch04-39` thus yields

```{math}
:label: eq-p1-ch04-42
\sigma = \frac{2e^2\tau}{m^*}\left(\frac{m^* k_B T}{2\pi\hbar^2}\right)^{3/2} e^{-|E_F|/k_B T}
```

which gives the temperature dependence of $\sigma$. Now the carrier density calculated using the same approximations becomes

```{math}
:label: eq-p1-ch04-43
n = (4\pi^3)^{-1} e^{-|E_F|/k_B T}\int e^{-E/k_B T} 4\pi k^2\,dk
= (\sqrt{2}/\pi^2)\left(\frac{m^*}{\hbar^2}\right)^{3/2} e^{-|E_F|/k_B T}
\int_0^\infty \sqrt{E}\,dE\,e^{-E/k_B T}
```

where

```{math}
:label: eq-p1-ch04-44
\int_0^\infty \sqrt{E}\,dE\,e^{-E/k_B T} = \frac{\sqrt{\pi}}{2}(k_B T)^{3/2}
```

which gives the final result for the temperature dependence of the carrier density

```{math}
:label: eq-p1-ch04-45
n = 2\left(\frac{m^* k_B T}{2\pi\hbar^2}\right)^{3/2} e^{-|E_F|/k_B T}
```

so that by substitution into {eq}`eq-p1-ch04-42`, the Drude formula is recovered

```{math}
:label: eq-p1-ch04-46
\sigma = \frac{n e^2\tau}{m^*}
```

for a semiconductor with constant $\tau$ and isotropic, parabolic dispersion relations.

To find $\sigma$ for a semiconductor with more than one spherical carrier pocket, the conductivities per carrier pocket are added

```{math}
:label: eq-p1-ch04-47
\sigma = \sum_i \sigma_i
```

where $i$ is the carrier pocket index. We use these simple formulae to make rough estimates for the carrier density and conductivity of semiconductors. For more quantitative analysis, the details of the $E(\vec{k})$ relation must be considered, as well as an energy dependent $\tau$ and use of the complete Fermi function.

The electrical conductivity and carrier density of a semiconductor with one carrier type exhibits an exponential temperature dependence so that the slope of $\ln\sigma$ vs $1/T$ yields an activation energy (see {numref}`fig-p1-ch04-3`). The plot of $\ln\sigma$ vs $1/T$ is called an "Arrhenius plot". If a plot of $\ln\sigma$ vs $1/T$ exhibits one temperature range with activation energy $E_{A1}$ and a second temperature range with activation energy $E_{A2}$, then two carrier behavior is suggested. Also in such cases, the activation energies can be extracted from an Arrhenius plot as shown in the schematic of {numref}`fig-p1-ch04-3`.

:::{figure} images/fig-p1-ch04-3.png
:name: fig-p1-ch04-3
:align: center
:width: 70%

Schematic diagram of an Arrhenius plot of $\ln\sigma$ vs $1/T$ showing two carrier types with different activation energies.
:::

### 4.5.1 Ellipsoidal Carrier Pockets

The conductivity results given above for a spherical Fermi surface can easily be generalized to an ellipsoidal Fermi surface which is commonly found in degenerate semiconductors. Semiconductors are degenerate at $T = 0$ when the Fermi level is in the valence or conduction band rather than in the energy band gap.

For an ellipsoidal Fermi surface, we write

```{math}
:label: eq-p1-ch04-48
E(\vec{k}) = \frac{\hbar^2 k_x^2}{2m_{xx}} + \frac{\hbar^2 k_y^2}{2m_{yy}} + \frac{\hbar^2 k_z^2}{2m_{zz}}
```

where the effective mass components $m_{xx}$, $m_{yy}$ and $m_{zz}$ are appropriate to the band curvatures in the $x$, $y$, $z$ directions, respectively. Substitution of

```{math}
:label: eq-p1-ch04-49
k'_\alpha = k_\alpha\sqrt{m_0/m_\alpha}
```

for $\alpha = x, y, z$ brings {eq}`eq-p1-ch04-48` into spherical form

```{math}
:label: eq-p1-ch04-50
E(\vec{k}') = \frac{\hbar^2 k'^2}{2m_0}
```

where $k'^2 = k'^2_x + k'^2_y + k'^2_z$. For the volume element $d^3k$ in {eq}`eq-p1-ch04-26` we have

```{math}
:label: eq-p1-ch04-51
d^3k = \sqrt{\frac{m_{xx}m_{yy}m_{zz}}{m_0^3}}\, d^3k'
```

and the carrier density associated with a single carrier pocket becomes

```{math}
:label: eq-p1-ch04-52
n_i = 2\sqrt{m_{xx}m_{yy}m_{zz}} \left(\frac{k_B T}{2\pi\hbar^2}\right)^{3/2} e^{-|E_F|/k_B T} .
```

For an ellipsoidal constant energy surface (see {numref}`fig-p1-ch04-4`), the directions of the electric field, electron velocity and electron acceleration will in general be different. Let $(x, y, z)$ be the coordinate system for the major axes of the constant energy ellipsoid and $(X, Y, Z)$ be the laboratory coordinate system. Then in the laboratory system the current density $\vec{j}$ and electric field $\vec{E}$ are related by

```{math}
:label: eq-p1-ch04-53
\begin{pmatrix} j_X \\ j_Y \\ j_Z \end{pmatrix}
=
\begin{pmatrix}
\sigma_{XX} & \sigma_{XY} & \sigma_{XZ} \\
\sigma_{YX} & \sigma_{YY} & \sigma_{YZ} \\
\sigma_{ZX} & \sigma_{ZY} & \sigma_{ZZ}
\end{pmatrix}
\begin{pmatrix} E_X \\ E_Y \\ E_Z \end{pmatrix}
```

As an example, suppose that the electric field is applied in the $XY$ plane along the $X$ axis at an angle $\theta$ with respect to the $x$ axis of the constant energy ellipsoid (see {numref}`fig-p1-ch04-4`). The conductivity tensor is easily written in the $xyz$ crystal coordinate system where the $xyz$ axes are along the principal axes of the ellipsoid:

```{math}
:label: eq-p1-ch04-54
\begin{pmatrix} j_x \\ j_y \\ j_z \end{pmatrix}
= n e^2 \tau
\begin{pmatrix}
1/m_{xx} & 0 & 0 \\
0 & 1/m_{yy} & 0 \\
0 & 0 & 1/m_{zz}
\end{pmatrix}
\begin{pmatrix} E\cos\theta \\ E\sin\theta \\ 0 \end{pmatrix}
```

:::{figure} images/fig-p1-ch04-4.png
:name: fig-p1-ch04-4
:align: center
:width: 50%

Schematic diagram of an ellipsoidal constant energy surface.
:::

A coordinate transformation from the crystal axes to the laboratory frame allows us to relate $\overleftrightarrow{\sigma}_{\text{crystal}}$ which we have written easily by {eq}`eq-p1-ch04-54` to $\overleftrightarrow{\sigma}_{\text{Lab}}$ which we measure by {eq}`eq-p1-ch04-53`. In general

```{math}
:label: eq-p1-ch04-55
\overleftrightarrow{\sigma}_{\text{Lab}} = R\,\overleftrightarrow{\sigma}_{\text{crystal}}\,R^{-1}
```

where

```{math}
:label: eq-p1-ch04-56
R =
\begin{pmatrix}
\cos\theta & \sin\theta & 0 \\
-\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{pmatrix}
```

and

```{math}
:label: eq-p1-ch04-57
R^{-1} =
\begin{pmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{pmatrix}
```

so that the conductivity tensor $\overleftrightarrow{\sigma}_{\text{Lab}}$ in the lab frame becomes:

```{math}
:label: eq-p1-ch04-58
\overleftrightarrow{\sigma}_{\text{Lab}} = n e^2 \tau
\begin{pmatrix}
\cos^2\theta/m_{xx} + \sin^2\theta/m_{yy} & \cos\theta\sin\theta(1/m_{yy} - 1/m_{xx}) & 0 \\
\cos\theta\sin\theta(1/m_{yy} - 1/m_{xx}) & \sin^2\theta/m_{xx} + \cos^2\theta/m_{yy} & 0 \\
0 & 0 & 1/m_{zz}
\end{pmatrix}
```

Semiconductors with ellipsoidal Fermi surfaces usually have several such surfaces located in crystallographically equivalent locations. In the case of cubic symmetry, the sum of the conductivity components results in an isotropic conductivity even though the contribution from each ellipsoid is anisotropic. Thus measurement of the electrical conductivity provides no information on the anisotropy of the Fermi surfaces of cubic materials. However, measurement of the magnetoresistance does provide such information, since the application of a magnetic field gives special importance to the magnetic field direction, thereby lowering the effective crystal symmetry.

## 4.6 Electrons and Holes in Intrinsic Semiconductors

Intrinsic semiconductors refer to semiconductors with no doping and no departures from perfect stoichiometry. In this section we consider the symmetry between electron and holes and we show how the Fermi energy is found for such semiconductors. In §4.7, we consider the corresponding issues for doped semiconductors containing impurities or departures from ideal stoichiometry.

In the absence of doping, carriers are generated by thermal or optical excitations. Thus at $T = 0$, all valence band states are occupied and all conduction band states are empty. Thus, for each electron that is excited into the conduction band, a hole is left behind. For intrinsic semiconductors, conduction is by both holes and electrons. The Fermi level is thus determined by the condition that the number of electrons is equal to the number of holes. Writing $g_v(E_h)$ and $g_c(E_e)$ as the density of hole states in the valence band and electron states in the conduction band, respectively, we obtain

```{math}
:label: eq-p1-ch04-59
n_h = \int_0^\infty g_v(E_h)\,\hat{f}_0(E_h + E_{F,h})\,dE_h
= \int_0^\infty g_c(E_e)\,\hat{f}_0(E_e + E_{F,e})\,dE_e = n_e
```

where the notation we have used is shown in {numref}`fig-p1-ch04-5`. Here the energy gap $E_g$ is written as the sum of the Fermi energies for electrons and holes, both taken as positive numbers

```{math}
:label: eq-p1-ch04-60
E_{F,e} + E_{F,h} = E_g ,
```

and the Fermi functions $\hat{f}_0$ are written so as to include explicitly the Fermi energy. The condition $n_e = n_h$ for intrinsic semiconductors is used to determine the position of the Fermi levels for electrons and holes within the band gap. If the band curvatures of the valence and conduction bands are the same, then their effective masses are the same magnitude and $E_F$ lies at midgap. We also derive in this section the general result for the placement of $E_F$ when $m^*_e \neq m^*_h$.

On the basis of this interpretation, the holes obey Fermi statistics as do the electrons, only we must measure the hole energies downward, while electron energies are measured upwards, as indicated in {numref}`fig-p1-ch04-5`. This approach clearly builds on the symmetry relation between electrons and holes. It is convenient to measure electron energies $E_e$ with respect to the bottom of the conduction band $E_c$ so that $E_e = E - E_c$ and to measure hole energies $E_h$ with respect to the top of the valence band $E_v$ so that $E_h = -(E - E_v)$. The Fermi level for the electrons is $-E_{F,e}$ (measured from the bottom of the conduction band which is taken as $E = 0$) and for holes it is $-E_{F,h}$ (measured from the top of the valence band which is taken as $E = 0$ for holes), so that $E_{F,e}$ and $E_{F,h}$ have positive values. Referring to {eq}`eq-p1-ch04-59`, $\hat{f}_0(E_e + E_{F,e})$ denotes the Fermi function for electrons where $E - E_F$ is written explicitly

```{math}
:label: eq-p1-ch04-61
\hat{f}_0(E_e + E_{F,e}) = \frac{1}{1 + \exp[(E_e + E_{F,e})/k_B T]}
```

and is consistent with the definitions given above. A similar expression to {eq}`eq-p1-ch04-61` follows for $\hat{f}_0(E_h + E_{F,h})$.

In an intrinsic semiconductor, the magnitudes of the energies $E_{F,e}$ and $E_{F,h}$ are both much greater than thermal energies, i.e., $|E_{F,e}| \gg k_B T$ and $|E_{F,h}| \gg k_B T$, where $k_B T$ at room temperature is $\sim 25$ meV. Thus the distribution functions can be approximated by the Boltzmann form

```{math}
:label: eq-p1-ch04-62
\hat{f}_0(E_e + E_{F,e}) \simeq e^{-(E_e + E_{F,e})/k_B T},\qquad
\hat{f}_0(E_h + E_{F,h}) \simeq e^{-(E_h + E_{F,h})/k_B T} .
```

If $m_e$ and $m_h$ are, respectively, the electron and hole effective masses and if we write the dispersion relations around the valence and conduction band extrema as

```{math}
:label: eq-p1-ch04-63
E_e = \hbar^2 k^2/(2m_e),\qquad E_h = \hbar^2 k^2/(2m_h)
```

then the density of states for electrons at the bottom of the conduction band and for holes at the top of the valence band can be written in their respective nearly free electron forms (see {eq}`eq-p1-ch04-68`)

```{math}
:label: eq-p1-ch04-64
g_c(E_e) = \frac{1}{2\pi^2}\left(\frac{2m_e}{\hbar^2}\right)^{3/2} E_e^{1/2},\qquad
g_v(E_h) = \frac{1}{2\pi^2}\left(\frac{2m_h}{\hbar^2}\right)^{3/2} E_h^{1/2} .
```

These expressions follow from

```{math}
:label: eq-p1-ch04-65
n = \frac{1}{4\pi^3}\frac{4\pi}{3}k^3
```

and substitution of $k$ via the simple parabolic relation

```{math}
:label: eq-p1-ch04-66
E = \frac{\hbar^2 k^2}{2m^*}
```

so that

```{math}
:label: eq-p1-ch04-67
n = \frac{1}{3\pi^2}\left(\frac{2m^*E}{\hbar^2}\right)^{3/2}
```

and

```{math}
:label: eq-p1-ch04-68
g(E) = \frac{dn}{dE} = \frac{1}{2\pi^2}\left(\frac{2m^*}{\hbar^2}\right)^{3/2} E^{1/2} .
```

Substitution of this density of states expression into {eq}`eq-p1-ch04-45` results in a carrier density

```{math}
:label: eq-p1-ch04-69
n_e = 2\left(\frac{m_e k_B T}{2\pi\hbar^2}\right)^{3/2} e^{-E_{F,e}/k_B T} .
```

Likewise for holes we obtain

```{math}
:label: eq-p1-ch04-70
n_h = 2\left(\frac{m_h k_B T}{2\pi\hbar^2}\right)^{3/2} e^{-E_{F,h}/k_B T} .
```

Thus the famous product rule is obtained

```{math}
:label: eq-p1-ch04-71
n_e n_h = 4\left(\frac{k_B T}{2\pi\hbar^2}\right)^3 (m_e m_h)^{3/2} e^{-E_g/k_B T}
```

where $E_g = E_{F,e} + E_{F,h}$. But for an intrinsic semiconductor $n_e = n_h$. Thus by taking the square root of the above expression, we obtain both $n_e$ and $n_h$

```{math}
:label: eq-p1-ch04-72
n_e = n_h = 2\left(\frac{k_B T}{2\pi\hbar^2}\right)^{3/2}(m_e m_h)^{3/4} e^{-E_g/2k_B T} .
```

Comparison with the expressions given in {eq}`eq-p1-ch04-69` and {eq}`eq-p1-ch04-70` for $n_e$ and $n_h$ allows us to solve for the Fermi levels $E_{F,e}$ and $E_{F,h}$

```{math}
:label: eq-p1-ch04-73
n_e = 2\left(\frac{m_e k_B T}{2\pi\hbar^2}\right)^{3/2}e^{-E_{F,e}/k_B T}
= 2\left(\frac{k_B T}{2\pi\hbar^2}\right)^{3/2}(m_e m_h)^{3/4}e^{-E_g/2k_B T}
```

so that

```{math}
:label: eq-p1-ch04-74
\exp(-E_{F,e}/k_B T) = (m_h/m_e)^{3/4}\exp(-E_g/2k_B T)
```

and

```{math}
:label: eq-p1-ch04-75
E_{F,e} = \frac{E_g}{2} - \frac{3}{4}k_B T \ln(m_h/m_e) .
```

If $m_e = m_h$, we obtain the simple result that $E_{F,e} = E_g/2$ which says that the Fermi level lies in the middle of the energy gap. However, if the masses are not equal, $E_F$ will lie closer to the band edge with higher curvature, thereby enhancing the Boltzmann factor term in the thermal excitation process, to compensate for the lower density of states for the higher curvature band.

If however $m_e \ll m_h$, the Fermi level approaches the conduction band edge and the full Fermi functions have to be considered. In this case

```{math}
:label: eq-p1-ch04-76
n_e = \frac{1}{2\pi^2}\left(\frac{2m_e}{\hbar^2}\right)^{3/2}
\int_{E_c}^\infty (E - E_c)^{1/2}\,dE\,\frac{1}{\exp[(E - E_{F,e})/k_B T] + 1}
\equiv N_e\,F_{1/2}\!\left(\frac{E_{F,e} - E_c}{k_B T}\right)
```

where $E_c$ is the bottom of the conduction band, $E_{F,e}$ is the Fermi energy for electrons which here is allowed the possibility of moving up into the conduction band (and therefore its sign cannot be predetermined), and $N_e$ is the "effective electron density" which, in accordance with {eq}`eq-p1-ch04-69`, is given by

```{math}
:label: eq-p1-ch04-77
N_e = 2\left(\frac{m_e k_B T}{2\pi\hbar^2}\right)^{3/2} .
```

The Fermi integral in {eq}`eq-p1-ch04-76` is written in standard form as

```{math}
:label: eq-p1-ch04-78
F_j(\eta) = \frac{1}{j!}\int_0^\infty \frac{x^j\,dx}{\exp(x - \eta) + 1} .
```

We can take $F_j(\eta)$ from the tables in Blakemore, "Semiconductor Physics" (Appendix B). For the semiconductor limit ($\eta < -4$), then $F_j(\eta) \to \exp(\eta)$. Clearly, when the full version of $F_j(\eta)$ is required to describe the carrier density, then $F_j(\eta)$ is also needed to describe the conductivity. These refinements are important for a detailed solution of the transport properties of semiconductors over the entire temperature range of interest, and eventually in the presence of doping.

:::{figure} images/fig-p1-ch04-5.png
:name: fig-p1-ch04-5
:align: center
:width: 70%

Schematic diagram of the band gap in a semiconductor showing the symmetry of electrons and holes.
:::

## 4.7 Donor and Acceptor Doping of Semiconductors

In general a semiconductor has electron and hole carriers due to the presence of impurities as well as from thermal excitation processes. For many applications, impurities are intentionally introduced to generate carriers: donor impurities to generate electrons in n-type semiconductors and acceptor impurities to generate holes in p-type semiconductors. Assuming for the moment that each donor contributes one electron to the conduction band, then the donors can contribute an excess carrier concentration up to $N_d$, where $N_d$ is the donor impurity concentration. Similarly, if every acceptor contributes one hole to the valence band, then the excess hole concentration will be $N_a$, where $N_a$ is the acceptor impurity concentration. In general, the semiconductor is partly compensated, which means that both donor and acceptor impurities are present, thereby giving a partial cancellation to the net carrier concentration. Furthermore, at finite temperatures, the donor and acceptor levels will be partially occupied, so that somewhat less than the maximum charge will be released as mobile charge into the conduction and valence bands. The density of electrons bound to a donor site $n_d$ is found from the grand canonical ensemble in statistical mechanics as

```{math}
:label: eq-p1-ch04-79
\frac{n_d}{N_d} = \frac{\sum_j N_j e^{-(E_j - \mu N_j)/k_B T}}{\sum_j e^{-(E_j - \mu N_j)/k_B T}}
```

where $E_j$ and $N_j$ are, respectively, the energy and number of electrons that can be placed in state $j$, and $\mu$ is the chemical potential (Fermi energy). Referring to {numref}`tab-p1-ch04-1`, the system can be found in one of three states: one where no electrons are present in state $j$ (hence no contribution is made to the energy), and two states where one electron is present (one with spin $\uparrow$, the other with spin $\downarrow$) corresponding to the donor energy $E_d$, where the sign is included directly so that $E_d$ has a positive energy value. Placing two electrons in the same energy state would result in a very high energy because of the Coulomb repulsion between the two electrons; therefore this possibility is neglected in practical calculations. Writing either $N_j = 0, 1$ for the 3 states of importance, we obtain for the relative ion concentration of occupied donor sites

```{math}
:label: eq-p1-ch04-80
\frac{n_d}{N_d} = \frac{2 e^{-(\varepsilon_d - \mu)/k_B T}}{1 + 2 e^{-(\varepsilon_d - \mu)/k_B T}}
= \frac{1}{1 + \frac{1}{2}e^{(\varepsilon_d - \mu)/k_B T}}
= \frac{1}{1 + \frac{1}{2}e^{-(E_d - E_{F,e})/k_B T}}
```

in which $E_d$ and $E_{F,e}$ are positive numbers, but lie below the zero of energy which is taken to be at the bottom of the conduction band. The energy $\varepsilon_d$ denotes the energy for the donor level and is a negative number relative to the zero of energy.

Consequently, the concentration of electrons thermally ionized into the conduction band will be

```{math}
:label: eq-p1-ch04-81
N_d - n_d = \frac{N_d}{1 + 2e^{(E_d - E_{F,e})/k_B T}} = n_e - n_h
```

where $n_e$ and $n_h$ are the mobile electron and hole concentrations. At low temperatures, where $E_d \sim k_B T$, almost all of the carriers in the conduction band will be generated by the ionized donors, so that $n_h \ll n_e$ and $(N_d - n_d) \simeq n_e$. The Fermi level will then adjust itself so that $N_d - n_d \simeq n_e$. From {eq}`eq-p1-ch04-45` and {eq}`eq-p1-ch04-81` the following equation determines $E_{F,e}$:

```{math}
:label: eq-p1-ch04-82
n_e = 2\left(\frac{m_e k_B T}{2\pi\hbar^2}\right)^{3/2}e^{-E_{F,e}/k_B T}
\simeq \frac{N_d}{1 + 2e^{(E_d - E_{F,e})/k_B T}} .
```

Solution of {eq}`eq-p1-ch04-82` shows that the presence of the ionized donor carriers moves the Fermi level up above the middle of the band gap and close to the bottom of the conduction band. For the donor impurity problem, the Fermi level will be close to the position of the donor level $E_d$, as shown in {numref}`fig-p1-ch04-6`. The position of the Fermi level also varies with temperature. {numref}`fig-p1-ch04-7`(a) shows the dependence of the Fermi level on temperature. Here $T_1$ denotes the temperature at which the thermal excitation of intrinsic electrons and holes become important, and $T_1$ is normally a high temperature. In contrast, $T_2$ is normally a very low temperature and denotes the temperature below which donor-generated electrons begin to freeze out in impurity level bound states and no longer contribute to conduction. This carrier freeze-out is illustrated in {numref}`fig-p1-ch04-7`(b). In the temperature range $T_2 < T < T_1$, the Fermi level in {numref}`fig-p1-ch04-7`(a) falls as $T$ increases according to

```{math}
:label: eq-p1-ch04-83
E_F = E_c - k_B T \ln(N_c/N_d)
```

:::{figure} images/fig-p1-ch04-6.png
:name: fig-p1-ch04-6
:align: center
:width: 60%

Variation of the Fermi energy ($E_F \equiv E_f$) with donor and acceptor concentrations. For a heavily doped n-type semiconductor $E_F$ is close to the donor level $E_d$, while for a heavily doped p-type semiconductor $E_F$ is close to $E_a$. This plot is made assuming almost all the donor and acceptor states are ionized.
:::

:::{figure} images/fig-p1-ch04-7.png
:name: fig-p1-ch04-7
:align: center
:width: 90%

(a) Temperature dependence of the Fermi energy for an n-type doped semiconductor. See the text for definitions of $T_1$ and $T_2$. Here $E_{Fi}$ denotes the position of the Fermi level in the high temperature limit where the thermal excitation of carriers far exceeds the electron density contributed by the donor impurities. (b) Temperature dependence of the electron density for Si doped with $10^{15}\,\mathrm{cm}^{-3}$ donors.
:::

where $N_c = 2m_e k_B T/(2\pi\hbar^2)$. In {numref}`fig-p1-ch04-7`(b) we see the temperature dependence of the carrier concentration in the intrinsic range ($T > T_1$), the saturation range ($T_2 < T < T_1$), and finally the low temperature range ($T < T_2$) where carriers freeze out into bound states in the impurity band at $E_d$. The plot of the electron density $n$ in {numref}`fig-p1-ch04-7`(b) is presented as a function of $(1000/T)$ and the corresponding temperature values are shown on the upper scale of the figure.

For the case of acceptor impurities, an ionized acceptor level releases a hole into the valence band, or alternatively, an electron from the valence band gets excited into an acceptor level, leaving a hole behind. At very low temperature, the acceptor levels are filled with holes under freeze-out conditions. Because of hole-hole Coulomb repulsion, we can place no more than one hole in each acceptor level. A singly occupied hole can have either spin up or spin down. Thus for the acceptor levels, a formula analogous to {eq}`eq-p1-ch04-80` for donors is obtained for the occupation of an acceptor level

```{math}
:label: eq-p1-ch04-84
\frac{n_a}{N_a} = \frac{1}{1 + \frac{1}{2}e^{-(E_a - E_{F,h})/k_B T}}
```

so that the essential symmetry between holes and electrons is maintained. To obtain the hole concentration in the valence band, we use a formula analogous to {eq}`eq-p1-ch04-81`.

A situation which commonly arises for the acceptor levels relates to the degeneracy of the valence bands for group IV and III-V compound semiconductors. We will illustrate the degenerate valence band in the case where spin-orbit interaction is considered (which is usually the situation that is relevant for opto-electronic applications). Under strong spin-orbit interaction we have a degenerate heavy and light hole band and a lower lying split-off band. The two degenerate bands are only weakly coupled, so that we can approximate the impurity acceptor levels by hydrogenic acceptor levels for the heavy hole $\varepsilon_{a,h}$ and light hole $\varepsilon_{a,l}$ bands. In this case the split-off band does not contribute significantly because it lies much lower in energy. The density of holes bound to both types of acceptor sites is given by

```{math}
:label: eq-p1-ch04-85
\frac{n_a}{N_a} = \frac{\sum_j N_j e^{-(E_j - \mu N_j)/k_B T}}{\sum_j e^{-(E_j - \mu N_j)/k_B T}} ,
```

following {eq}`eq-p1-ch04-79`, where we note that the heavy hole and light hole bands can each accommodate one spin up and one spin down electron for each wavevector $\vec{k}$. Using the same arguments as above, we obtain:

```{math}
:label: eq-p1-ch04-86
\frac{n_a}{N_a} = \frac{2 e^{-(\varepsilon_{a,l} - \mu)/k_B T} + 2 e^{-(\varepsilon_{a,h} - \mu)/k_B T}}
{1 + 2 e^{-(\varepsilon_{a,l} - \mu)/k_B T} + 2 e^{-(\varepsilon_{a,h} - \mu)/k_B T}}
```

so that

```{math}
:label: eq-p1-ch04-87
\frac{n_a}{N_a} = \frac{1 + e^{-(\varepsilon_{a,h} - \varepsilon_{a,l})/k_B T}}
{1 + \frac{1}{2}e^{(\varepsilon_{a,l} - \mu)/k_B T} + e^{-(\varepsilon_{a,h} - \varepsilon_{a,l})/k_B T}} .
```

If the thermal energy is large in comparison to the difference between the acceptor levels for the heavy and light hole bands, then

```{math}
:label: eq-p1-ch04-88
(\varepsilon_{a,h} - \varepsilon_{a,l})/k_B T \ll 1
```

and

```{math}
:label: eq-p1-ch04-89
\exp[-(\varepsilon_{a,h} - \varepsilon_{a,l})/k_B T] \simeq 1
```

so that the density of holes bound to acceptor sites becomes

```{math}
:label: eq-p1-ch04-90
\frac{n_a}{N_a} \simeq \frac{1}{1 + \frac{1}{4}e^{-(\varepsilon_{a,l} - \mu)/k_B T}}
= \frac{1}{1 + \frac{1}{4}e^{(E_a - E_{F,h})/k_B T}}
```

where $E_a$ and $E_{F,h}$ are positive values corresponding to $\varepsilon_{a,l}$ and $\mu$, respectively. From {eq}`eq-p1-ch04-81` and {eq}`eq-p1-ch04-90`, the temperature dependence of $E_F$ can be calculated for the case of doped semiconductors considering doping by donor and acceptor impurities, either separately or at the same time. {numref}`fig-p1-ch04-6` shows the doping dependence of $E_F$ for p-doped semiconductors as well as n-doped semiconductors.

:::{table} tab-p1-ch04-1
:name: tab-p1-ch04-1
:align: center

**Table 4.1:** Occupation of impurity states in the grand canonical ensemble.

| state | $N_j$ | spin | $E_j$ |
|-------|--------|------|--------|
| 1 | 0 | – | 0 |
| 2 | 1 | $\uparrow$ | $-E_d$ |
| 3 | 1 | $\downarrow$ | $-E_d$ |
| 4 | 2 | $\uparrow\downarrow$ | $-E_d + E_{\text{Coulomb}}$ |
:::

## 4.8 Characterization of Semiconductors

In describing the electrical conductivity of semiconductors, it is customary to write the conductivity as

```{math}
:label: eq-p1-ch04-91
\sigma = n_e |e|\mu_e + n_h |e|\mu_h
```

in which $n_e$ and $n_h$ are the carrier densities for the carriers, and $\mu_e$ and $\mu_h$ are their mobilities. We have shown in {eq}`eq-p1-ch04-46` that for cubic materials the static conductivity can under certain approximations be written as

```{math}
:label: eq-p1-ch04-92
\sigma = \frac{n e^2\tau}{m^*}
```

for each carrier type, so that the mobilities and effective masses are related by

```{math}
:label: eq-p1-ch04-93
\mu_e = \frac{|e|\langle\tau_e\rangle}{m_e}
```

and

```{math}
:label: eq-p1-ch04-94
\mu_h = \frac{|e|\langle\tau_h\rangle}{m_h}
```

which show that materials with small effective masses have high mobilities. By writing the electrical conductivity as a product of the carrier density with the mobility, it is easy to contrast the temperature dependence of $\sigma$ for metals and semiconductors. For metals, the carrier density $n$ is essentially independent of $T$, while $\mu$ is temperature dependent. In contrast, $n$ for semiconductors is highly temperature dependent in the intrinsic regime [see {numref}`fig-p1-ch04-7`(b)] and $\mu$ is relatively less temperature dependent. {numref}`fig-p1-ch04-8` shows the carrier concentration for intrinsic Si and Ge in the neighborhood of room temperature ($250 < T < 500$ K), demonstrating the rapid increase of the carrier concentration. These values of $n$ indicate the doping levels necessary to exceed the intrinsic carrier level at a given temperature. {numref}`fig-p1-ch04-9` shows the mobility for n-type Si samples with various impurity levels. The observed temperature dependence can be explained by the different temperature dependences of the impurity scattering and phonon scattering mechanisms (see {numref}`fig-p1-ch04-10`). This is further discussed in Chapter 6.

A table of typical mobilities for semiconductors is given in {numref}`tab-p1-ch04-2`. By way of comparison, $\mu$ for copper at room temperature is $35\,\mathrm{cm}^2/\mathrm{volt}\text{-}\mathrm{sec}$. When using conductivity formulae in esu units, remember that the mobility is expressed in $\mathrm{cm}^2/\mathrm{statvolt}\text{-}\mathrm{sec}$ and that all the numbers in {numref}`tab-p1-ch04-2` have to be multiplied by 300 to match the units given in the notes.

:::{table} tab-p1-ch04-2
:name: tab-p1-ch04-2
:align: center

**Table 4.2:** Mobilities for some typical semiconductors at room temperature in units of $\mathrm{cm}^2/\mathrm{V}\text{-}\mathrm{sec}$.

| Crystal | Electrons | Holes | Crystal | Electrons | Holes |
|---------|-----------|-------|---------|-----------|-------|
| Diamond | 1800 | 1200 | GaAs | 8000 | 300 |
| Si | 1350 | 480 | GaSb | 5000 | 1000 |
| Ge | 3600 | 1800 | PbS | 550 | 600 |
| InSb | 77000 | 750 | PbSe | 1020 | 930 |
| InAs | 30000 | 460 | PbTe | 2500 | 1000 |
| InP | 4600 | 100 | AgCl | 50 | – |
| AlAs | 280 | – | AlSb | 900 | 400 |
| KBr (100 K) | 100 | – | SiC | 100 | 10–20 |
:::

:::{figure} images/fig-p1-ch04-8.png
:name: fig-p1-ch04-8
:align: center
:width: 80%

Temperature dependence of the electron concentration for intrinsic Si and Ge in the range $250 < T < 500$ K. Circles indicate the doping levels that must be exceeded to have extrinsic carriers dominate over thermally excited carriers at 300 K.
:::

:::{figure} images/fig-p1-ch04-9.png
:name: fig-p1-ch04-9
:align: center
:width: 80%

Temperature dependence of the mobility for n-type Si for a series of samples with different impurity concentrations. Note that the mobility is not as strong a function of temperature as is the carrier density shown in {numref}`fig-p1-ch04-8`. At low temperature impurity scattering by the donor impurity ions becomes important as shown in the inset. The different temperature dependences of impurity and electron-phonon scattering allows one to identify the important scattering mechanisms experimentally.
:::

:::{figure} images/fig-p1-ch04-10.png
:name: fig-p1-ch04-10
:align: center
:width: 80%

Temperature dependence of the mobility for n-type GaAs showing the separate and combined scattering processes.
:::

In the characterization of a semiconductor for device applications, researchers are expected to provide information on the carrier density and mobility, preferably as a function of temperature. Such plots are shown in {numref}`fig-p1-ch04-8` and {numref}`fig-p1-ch04-9`. When presenting characterization data in condensed form, the carrier density and mobility of semiconductors are traditionally given at 300 K and 77 K. Other information of values in semiconductor physics are values of the effective masses ({numref}`tab-p1-ch04-3`) and of the energy gaps ({numref}`tab-p1-ch04-4`).

:::{table} tab-p1-ch04-3
:name: tab-p1-ch04-3
:align: center

**Table 4.3:** Semiconductor effective masses of electrons and holes in direct gap semiconductors.

| Crystal | $m_e/m_0$ | $m_{hh}/m_0$ | $m_{lh}/m_0$ | $m_{soh}/m_0$ | $\Delta$ (eV) |
|---------|-----------|-------------|-------------|--------------|------------|
| InSb | 0.015 | 0.39 | 0.021 | (0.11) | 0.82 |
| InAs | 0.026 | 0.41 | 0.025 | 0.08 | 0.43 |
| InP | 0.073 | 0.4 | (0.078) | (0.15) | 0.11 |
| GaSb | 0.047 | 0.3 | 0.06 | (0.14) | 0.80 |
| GaAs | 0.066 | 0.5 | 0.082 | 0.17 | 0.34 |
:::

:::{table} tab-p1-ch04-4
:name: tab-p1-ch04-4
:align: center

**Table 4.4:** Semiconductor energy gaps between the valence and conduction bands.

| Crystal | Gap$^a$ | 0 K | 300 K | Crystal | Gap$^a$ | 0 K | 300 K |
|---------|---------|-----|--------|---------|---------|-----|--------|
| Diamond | i | 5.4 | – | HgTe$^b$ | d | – | – |
| Si | i | 1.17 | 1.11 | PbS | d | 0.286 | 0.34–0.37 |
| Ge | i | 0.744 | 0.66 | PbSe | i | 0.165 | 0.27 |
| $\alpha$Sn | d | 0.00 | 0.00 | PbTe | i | 0.190 | 0.29 |
| InSb | d | 0.23 | 0.17 | CdS | d | 2.582 | 2.42 |
| InAs | d | 0.43 | 0.36 | CdSe | d | 1.840 | 1.74 |
| InP | d | 1.42 | 1.27 | CdTe | d | 1.607 | 1.44 |
| GaP | i | 2.32 | 2.25 | ZnO | – | 3.436 | 3.2 |
| GaAs | d | 1.52 | 1.43 | ZnS | – | 3.91 | 3.6 |
| GaSb | d | 0.81 | 0.68 | SnTe | d | 0.3 | 0.18 |
| AlSb | i | 1.65 | 1.6 | AgCl | – | – | 3.2 |
| SiC(hex) | i | 3.0 | – | AgI | – | – | 2.8 |
| Te | d | 0.33 | – | Cu$_2$O | d | 2.172 | – |
| ZnSb | – | 0.56 | 0.56 | TiO$_2$ | – | 3.03 | – |

$^a$The indirect gap is labeled by i, and the direct gap is labeled by d.
$^b$HgTe is a zero gap semiconductor, and because of non-ideal stoichiometry, the Fermi level may be in the valence or conduction band.
:::
