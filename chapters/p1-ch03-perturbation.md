---
title: "3 Effective Mass Theory"
abstract: "This chapter develops the effective mass theorem for wavepackets in crystals, derives the group velocity and quasi-classical equations of motion, and applies the theorem to hydrogenic donor levels and the electrical conductivity tensor."
---

# 3 Effective Mass Theory

## 3.0 Overview

In a crystal lattice, the electronic motion induced by an applied field is conveniently described by a wavepacket composed of eigenstates of the unperturbed crystal. This chapter introduces the group velocity of such wavepackets, proves the effective mass theorem, applies it to donor impurity levels in semiconductors, and uses quasi-classical dynamics to obtain a general expression for the conductivity tensor and the Drude formula.

**Reference:**

- Smith, Janak and Adler, *Electron Conduction in Solids*, McGraw-Hill, 1967, Chapter 6.

## 3.1 Wavepackets in Crystals and Group Velocity of Electrons in Solids

In a crystal lattice, the electronic motion which is induced by an applied field is conveniently described by a wavepacket composed of eigenstates of the unperturbed crystal. These eigenstates are Bloch functions

```{math}
:label: eq-p1-ch03-1
\psi_{n\vec{k}}(\vec{r}) = e^{i\vec{k}\cdot\vec{r}} u_{n\vec{k}}(\vec{r})
```

and are associated with band $n$. These wavepackets are solutions of the time-dependent Schrödinger equation

```{math}
:label: eq-p1-ch03-2
\mathcal{H}_0 \psi_n(\vec{r}, t) = i\hbar \frac{\partial \psi_n(\vec{r}, t)}{\partial t}
```

where the time independent part of the Hamiltonian can be written as

```{math}
:label: eq-p1-ch03-3
\mathcal{H}_0 = \frac{p^2}{2m} + V(\vec{r}) ,
```

where $V(\vec{r}) = V(\vec{r}+\vec{R}_n)$ is the periodic potential. The wave packets $\psi_n(\vec{r}, t)$ can be written in terms of the Bloch states $\psi_{n\vec{k}}(\vec{r})$ as

```{math}
:label: eq-p1-ch03-4
\psi_n(\vec{r}, t) = \sum_{\vec{k}} A_{n,\vec{k}}(t) \psi_{n\vec{k}}(\vec{r}) = \int d^3k \, A_{n,\vec{k}}(t) \psi_{n\vec{k}}(\vec{r})
```

where we have replaced the sum by an integration over the Brillouin zone, since permissible $\vec{k}$ values for a macroscopic solid are very closely spaced. If the Hamiltonian $\mathcal{H}_0$ is time-independent as is often the case, we can write

```{math}
:label: eq-p1-ch03-5
A_{n,\vec{k}}(t) = A_{n,\vec{k}} e^{-i\omega_n(\vec{k})t}
```

where

```{math}
:label: eq-p1-ch03-6
\hbar \omega_n(\vec{k}) = E_n(\vec{k})
```

and thereby obtain

```{math}
:label: eq-p1-ch03-7
\psi_n(\vec{r}, t) = \int d^3k \, A_{n,\vec{k}} u_{n\vec{k}}(\vec{r}) e^{i[\vec{k}\cdot\vec{r}-\omega_n(\vec{k})t]} .
```

We can localize the wavepacket in $\vec{k}$-space by requiring that the coefficients $A_{n,\vec{k}}$ be large only in a confined region of $\vec{k}$-space centered at $\vec{k} = \vec{k}_0$. If we now expand the band energy in a Taylor series around $\vec{k} = \vec{k}_0$ we obtain:

```{math}
:label: eq-p1-ch03-8
E_n(\vec{k}) = E_n(\vec{k}_0) + (\vec{k}-\vec{k}_0) \cdot \left. \frac{\partial E_n(\vec{k})}{\partial \vec{k}} \right|_{\vec{k}=\vec{k}_0} + \ldots ,
```

where we have written $\vec{k}$ as

```{math}
:label: eq-p1-ch03-9
\vec{k} = \vec{k}_0 + (\vec{k}-\vec{k}_0) .
```

Since $|\vec{k}-\vec{k}_0|$ is assumed to be small compared with Brillouin zone dimensions, we are justified in retaining only the first two terms of the Taylor expansion in {eq}`eq-p1-ch03-8`. Substitution into {eq}`eq-p1-ch03-4` for the wave packet yields:

```{math}
:label: eq-p1-ch03-10
\psi_n(\vec{r}, t) \simeq e^{i(\vec{k}_0\cdot\vec{r}-\omega_n(\vec{k}_0)t)} \int d^3k \, A_{n,\vec{k}} u_{n\vec{k}}(\vec{r}) e^{i(\vec{k}-\vec{k}_0)\cdot\left[\vec{r}-\frac{\partial \omega_n(\vec{k})}{\partial \vec{k}} t\right]}
```

where

```{math}
:label: eq-p1-ch03-11
\hbar \omega_n(\vec{k}_0) = E_n(\vec{k}_0)
```

and

```{math}
:label: eq-p1-ch03-12
\hbar \frac{\partial \omega_n(\vec{k})}{\partial \vec{k}} = \frac{\partial E_n(\vec{k})}{\partial \vec{k}}
```

and the derivative $\partial \omega_n(\vec{k})/\partial \vec{k}$ which appears in the phase factor of {eq}`eq-p1-ch03-10` is evaluated at $\vec{k} = \vec{k}_0$. Except for the periodic function $u_{n\vec{k}}(\vec{r})$, {eq}`eq-p1-ch03-10` is in the standard form for a wavepacket moving with “group velocity” $\vec{v}_g$

```{math}
:label: eq-p1-ch03-13
\vec{v}_g \equiv \frac{\partial \omega_n(\vec{k})}{\partial \vec{k}}
```

so that

```{math}
:label: eq-p1-ch03-14
\vec{v}_g = \frac{1}{\hbar} \frac{\partial E_n(\vec{k})}{\partial \vec{k}} ,
```

while the phase velocity $\vec{v}_p$ is

```{math}
:label: eq-p1-ch03-15
\vec{v}_p = \frac{\omega_n(\vec{k})}{\vec{k}} = \frac{\partial E_n(\vec{k})}{\hbar \partial \vec{k}} .
```

In the limit of free electrons the group velocity becomes

```{math}
:label: eq-p1-ch03-16
\vec{v}_g = \frac{\vec{p}}{m} = \frac{\hbar \vec{k}}{m}
```

and $\vec{v}_g = \vec{v}_p$ in this limit. This result also follows from the above discussion using

```{math}
:label: eq-p1-ch03-17
E_n(\vec{k}) = \frac{\hbar^2 k^2}{2m}
```

and

```{math}
:label: eq-p1-ch03-18
\frac{\partial E_n(\vec{k})}{\hbar \partial \vec{k}} = \frac{\hbar \vec{k}}{m} .
```

We shall show later that the electron wavepacket moves through the crystal very much like a free electron provided that the wavepacket remains localized in $k$ space during the time interval of interest in the particular problem under consideration. Because of the uncertainty principle, the localization of a wavepacket in reciprocal space implies a delocalization of the wavepacket in real space.

We use wavepackets to describe electronic states in a solid when the crystal is perturbed in some way (e.g., by an applied electric or magnetic field). We make frequent applications of wavepackets to transport theory (e.g., electrical conductivity). In many practical applications of transport theory, use is made of the Effective-Mass Theorem, which is the most important result of transport theory.

We note that the above discussion for the wavepacket is given in terms of the perfect crystal. In our discussion of the Effective-Mass Theorem we will see that these wavepackets are also of use in describing situations where the Hamiltonian which enters Schrödinger’s equation contains both the unperturbed Hamiltonian of the perfect crystal $\mathcal{H}_0$ and the perturbation Hamiltonian $\mathcal{H}'$ arising from an external perturbation. Common perturbations are applied electric or magnetic fields, or a lattice defect or an impurity atom.

## 3.2 The Effective Mass Theorem

We shall now present the Effective Mass theorem, which is central to the consideration of the electrical and optical properties of solids. An elementary proof of the theorem will be given here for a simple but important case, namely the non-degenerate band which can be identified with the corresponding atomic state. The theorem will be discussed from a more advanced point of view which considers also the case of degenerate bands in the following courses in the physics of solids sequence.

For many practical situations we find a solid in the presence of some perturbing field (e.g., an externally applied electric field, or the perturbation created by an impurity atom or a crystal defect). The perturbation may be either time-dependent or time-independent. We will show here that under many common circumstances this perturbation can be treated in the effective mass approximation whereby the periodic potential is replaced by an effective Hamiltonian based on the $E(\vec{k})$ relations for the perfect crystal.

To derive the effective mass theorem, we start with the time-dependent Schrödinger equation

```{math}
:label: eq-p1-ch03-19
(\mathcal{H}_0 + \mathcal{H}') \psi_n(\vec{r}, t) = i\hbar \frac{\partial \psi_n(\vec{r}, t)}{\partial t} .
```

We then substitute the expansion for the wave packet

```{math}
:label: eq-p1-ch03-20
\psi_n(\vec{r}, t) = \int d^3k \, A_{n\vec{k}}(t) e^{i\vec{k}\cdot\vec{r}} u_{n\vec{k}}(\vec{r})
```

into Schrödinger’s equation and make use of the Bloch solution

```{math}
:label: eq-p1-ch03-21
\mathcal{H}_0 e^{i\vec{k}\cdot\vec{r}} u_{n\vec{k}}(\vec{r}) = E_n(\vec{k}) e^{i\vec{k}\cdot\vec{r}} u_{n\vec{k}}(\vec{r})
```

to obtain:

```{math}
:label: eq-p1-ch03-22
(\mathcal{H}_0 + \mathcal{H}') \psi_n(\vec{r}, t) = \int d^3k \, [E_n(\vec{k}) + \mathcal{H}'] A_{n\vec{k}}(t) e^{i\vec{k}\cdot\vec{r}} u_{n\vec{k}}(\vec{r}) = i\hbar \frac{\partial \psi_n(\vec{r}, t)}{\partial t} = i\hbar \int d^3k \, \dot{A}_{n\vec{k}}(t) e^{i\vec{k}\cdot\vec{r}} u_{n\vec{k}}(\vec{r}) .
```

It follows from Bloch’s theorem that $E_n(\vec{k})$ is a periodic function in the reciprocal lattice. We can therefore expand $E_n(\vec{k})$ in a Fourier series in the direct lattice

```{math}
:label: eq-p1-ch03-23
E_n(\vec{k}) = \sum_{\vec{R}_\ell} E_{n\ell} e^{i\vec{k}\cdot\vec{R}_\ell}
```

where the $\vec{R}_\ell$ are lattice vectors. Now consider the differential operator $E_n(-i\vec{\nabla})$ formed by replacing $\vec{k}$ by $-i\vec{\nabla}$

```{math}
:label: eq-p1-ch03-24
E_n(-i\vec{\nabla}) = \sum_{\vec{R}_\ell} E_{n\ell} e^{\vec{R}_\ell \cdot \vec{\nabla}} .
```

Consider the effect of $E_n(-i\vec{\nabla})$ on an arbitrary function $f(\vec{r})$. Since $e^{\vec{R}_\ell \cdot \vec{\nabla}}$ can be expanded in a Taylor series, we obtain

```{math}
:label: eq-p1-ch03-25
\begin{aligned}
e^{\vec{R}_\ell \cdot \vec{\nabla}} f(\vec{r}) &= \left[1 + \vec{R}_\ell \cdot \vec{\nabla} + \frac{1}{2}(\vec{R}_\ell \cdot \vec{\nabla})(\vec{R}_\ell \cdot \vec{\nabla}) + \ldots \right] f(\vec{r}) \\
&= f(\vec{r}) + \vec{R}_\ell \cdot \vec{\nabla} f(\vec{r}) + \frac{1}{2!} R_{\ell,\alpha} R_{\ell,\beta} \frac{\partial^2}{\partial r_\alpha \partial r_\beta} f(\vec{r}) + \ldots \\
&= f(\vec{r} + \vec{R}_\ell) .
\end{aligned}
```

Thus the effect of $E_n(-i\vec{\nabla})$ on a Bloch state is to produce $E_n(\vec{k})$ because

```{math}
:label: eq-p1-ch03-26
E_n(-i\vec{\nabla}) \psi_{n\vec{k}}(\vec{r}) = \sum_{\vec{R}_\ell} E_{n\ell} \psi_{n\vec{k}}(\vec{r}+\vec{R}_\ell) = \sum_{\vec{R}_\ell} E_{n\ell} e^{i\vec{k}\cdot\vec{R}_\ell} e^{i\vec{k}\cdot\vec{r}} u_{n\vec{k}}(\vec{r}) = E_n(\vec{k}) \psi_{n\vec{k}}(\vec{r}) ,
```

since from Bloch’s theorem

```{math}
:label: eq-p1-ch03-27
\psi_{n\vec{k}}(\vec{r}+\vec{R}_\ell) = e^{i\vec{k}\cdot\vec{R}_\ell} \cdot \left[ e^{i\vec{k}\cdot\vec{r}} u_{n\vec{k}}(\vec{r}) \right] .
```

Substitution of

```{math}
:label: eq-p1-ch03-28
E_n(-i\vec{\nabla}) \psi_{n\vec{k}}(\vec{r}) = E_n(\vec{k}) \psi_{n\vec{k}}(\vec{r})
```

from {eq}`eq-p1-ch03-26` into Schrödinger’s equation ({eq}`eq-p1-ch03-22`) yields:

```{math}
:label: eq-p1-ch03-29
\int d^3k \, \left[ E_n(-i\vec{\nabla}) + \mathcal{H}' \right] A_{n\vec{k}}(t) e^{i\vec{k}\cdot\vec{r}} u_{n\vec{k}}(\vec{r}) = \left[ E_n(-i\vec{\nabla}) + \mathcal{H}' \right] \int d^3k \, A_{n\vec{k}}(t) e^{i\vec{k}\cdot\vec{r}} u_{n\vec{k}}(\vec{r})
```

so that

```{math}
:label: eq-p1-ch03-30
\left[ E_n(-i\vec{\nabla}) + \mathcal{H}' \right] \psi_n(\vec{r}, t) = i\hbar \frac{\partial \psi_n(\vec{r}, t)}{\partial t} .
```

The result of {eq}`eq-p1-ch03-30` is called the effective mass theorem. We observe that the original crystal Hamiltonian $p^2/2m + V(\vec{r})$ does not appear in this equation. It has instead been replaced by an effective Hamiltonian which is an operator formed from the solution $E(\vec{k})$ for the perfect crystal in which we replace $\vec{k}$ by $-i\vec{\nabla}$. For example, for the free electron ($V(\vec{r}) \equiv 0$)

```{math}
:label: eq-p1-ch03-31
E_n(-i\vec{\nabla}) \to -\frac{\hbar^2 \nabla^2}{2m} .
```

In applying the effective mass theorem, we assume that $E(\vec{k})$ is known either from the results of a theoretical calculation or from the analysis of experimental results. What is important here is that once $E(\vec{k})$ is known, the effect of various perturbations on the ideal crystal can be treated in terms of the solution to the energy levels of the perfect crystal, without recourse to consideration of the full Hamiltonian. In practical cases, the solution to the effective mass equation is much easier to carry out than the solution to the original Schrödinger equation.

According to the above discussion, we have assumed that $E(\vec{k})$ is specified throughout the Brillouin zone. For many practical applications, the region of $\vec{k}$-space which is of importance is confined to a small portion of the Brillouin zone. In such cases it is only necessary to specify $E(\vec{k})$ in a local region (or regions) and to localize our wavepacket solutions to these local regions of $\vec{k}$-space. Suppose that we localize the wavepacket around $\vec{k} = \vec{k}_0$, and correspondingly expand our Bloch functions around $\vec{k}_0$,

```{math}
:label: eq-p1-ch03-32
\psi_{n\vec{k}}(\vec{r}) = e^{i\vec{k}\cdot\vec{r}} u_{n\vec{k}}(\vec{r}) \simeq e^{i\vec{k}\cdot\vec{r}} u_{n\vec{k}_0}(\vec{r}) = e^{i(\vec{k}-\vec{k}_0)\cdot\vec{r}} \psi_{n\vec{k}_0}(\vec{r})
```

where we have noted that $u_{n\vec{k}}(\vec{r}) \simeq u_{n\vec{k}_0}(\vec{r})$ has only a weak dependence on $\vec{k}$. Then our wavepacket can be written as

```{math}
:label: eq-p1-ch03-33
\psi_n(\vec{r}, t) = \int d^3k \, A_{n\vec{k}}(t) e^{i(\vec{k}-\vec{k}_0)\cdot\vec{r}} \psi_{n\vec{k}_0}(\vec{r}) = F(\vec{r}, t) \psi_{n\vec{k}_0}(\vec{r})
```

where $F(\vec{r}, t)$ is called the amplitude or envelope function and is defined by

```{math}
:label: eq-p1-ch03-34
F(\vec{r}, t) = \int d^3k \, A_{n\vec{k}}(t) e^{i(\vec{k}-\vec{k}_0)\cdot\vec{r}} .
```

Since the time dependent Fourier coefficients $A_{n\vec{k}}(t)$ are assumed here to be large only near $\vec{k} = \vec{k}_0$, then $F(\vec{r}, t)$ will be a slowly varying function of $\vec{r}$, because in this case

```{math}
:label: eq-p1-ch03-35
e^{i(\vec{k}-\vec{k}_0)\cdot\vec{r}} \simeq 1 + i(\vec{k}-\vec{k}_0)\cdot\vec{r} + \ldots .
```

It can be shown that the envelope function also satisfies the effective mass equation

```{math}
:label: eq-p1-ch03-36
\left[ E_n(-i\vec{\nabla}) + \mathcal{H}' \right] F(\vec{r}, t) = i\hbar \frac{\partial F(\vec{r}, t)}{\partial t}
```

where we now replace $\vec{k}-\vec{k}_0$ in $E_n(\vec{k})$ by $-i\vec{\nabla}$. This form of the effective mass equation is useful for treating the problem of donor and acceptor impurity states in semiconductors, and $\vec{k}_0$ is taken as the band extremum.

## 3.3 Application of the Effective Mass Theorem to Donor Impurity Levels in a Semiconductor

Suppose that we add an impurity from column V in the Periodic Table to a semiconductor such as silicon or germanium, which are both members of column IV of the periodic table. This impurity atom will have one more electron than is needed to satisfy the valency requirements for the tetrahedral bonds which the germanium or silicon atoms form with their 4 valence electrons (see {numref}`fig-p1-ch03-1`).

:::{figure} images/fig-p1-ch03-1.png
:name: fig-p1-ch03-1
:width: 60%
:align: center
Fig. 3.1: Crystal structure of diamond, showing the tetrahedral bond arrangement with an Sb$^+$ ion on one of the lattice sites and a free donor electron available for conduction.
:::

This extra electron from the impurity atom will be free to wander through the lattice, subject of course to the coulomb attraction of the ion core which will have one unit of positive charge. We will consider here the case where we add just a small number of these impurity atoms so that we may focus our attention on a single, isolated substitutional impurity atom in an otherwise perfect lattice. In the course of this discussion we will define more carefully what the limits on the impurity concentration must be so that the treatment given here is applicable.

Let us also assume that the conduction band of the host semiconductor in the vicinity of the band “minimum” at $\vec{k}_0$ has the simple analytic form

```{math}
:label: eq-p1-ch03-37
E_c(\vec{k}) \simeq E_c(\vec{k}_0) + \frac{\hbar^2 (\vec{k}-\vec{k}_0)^2}{2m^*} .
```

We can consider this expression for the conduction band level $E_c(\vec{k})$ as a special case of the Taylor expansion of $E(\vec{k})$ about an energy band minimum at $\vec{k} = \vec{k}_0$. For the present discussion, $E(\vec{k})$ is assumed to be isotropic in $\vec{k}$; this typically occurs in cubic semiconductors with band extrema at $\vec{k} = 0$. The quantity $m^*$ in this equation is the effective mass for the electrons. We will see that the energy levels corresponding to the donor electron will lie in the band gap below the conduction band minimum as indicated in the diagram in {numref}`fig-p1-ch03-2`.

:::{figure} images/fig-p1-ch03-2.png
:name: fig-p1-ch03-2
:width: 60%
:align: center
Fig. 3.2: Schematic band diagram showing donor levels in a semiconductor.
:::

To solve for the impurity levels explicitly, we may use the time-independent form of the effective mass theorem derived from {eq}`eq-p1-ch03-36`

```{math}
:label: eq-p1-ch03-38
\left[ E_n(-i\vec{\nabla}) + \mathcal{H}' \right] F(\vec{r}) = (E - E_c) F(\vec{r}) .
```

Equation {eq}`eq-p1-ch03-38` is applicable to the impurity problem in a semiconductor provided that the amplitude function $F(\vec{r})$ is sufficiently slowly varying over a unit cell. In the course of this discussion, we will see that the donor electron in a column IV (or III-V or II-VI compound semiconductor) will wander over many lattice sites and therefore this approximation on $F(\vec{r})$ will be justified.

For a singly ionized donor impurity (such as arsenic in germanium), the perturbing potential $\mathcal{H}'$ can be represented as a Coulomb potential

```{math}
:label: eq-p1-ch03-39
\mathcal{H}' = -\frac{e^2}{\varepsilon r}
```

where $\varepsilon$ is an average dielectric constant of the crystal medium which the donor electron sees as it wanders through the crystal. Experimental data on donor impurity states indicate that $\varepsilon$ is very closely equal to the low frequency limit of the electronic dielectric constant $\varepsilon_1(\omega)|_{\omega=0}$, which we will discuss extensively in treating the optical properties of solids (Part II of this course).

The above discussion involving an isotropic $E(\vec{k})$ is appropriate for semiconductors with conduction band minima at $\vec{k}_0 = 0$. The Effective Mass equation for the unperturbed crystal is

```{math}
:label: eq-p1-ch03-40
E_n(-i\vec{\nabla}) = -\frac{\hbar^2}{2m^*} \nabla^2
```

in which we have replaced $\vec{k}$ by $-i\vec{\nabla}$.

The donor impurity problem in the effective mass approximation thus becomes

```{math}
:label: eq-p1-ch03-41
\left[ -\frac{\hbar^2}{2m^*} \nabla^2 - \frac{e^2}{\varepsilon r} \right] F(\vec{r}) = (E - E_c) F(\vec{r})
```

where all energies are measured with respect to the bottom of the conduction band $E_c$. If we replace $m^*$ by $m$ and $e^2/\varepsilon$ by $e^2$, we immediately recognize this equation as Schrödinger’s equation for a hydrogen atom under the identification of the energy eigenvalues with

```{math}
:label: eq-p1-ch03-42
E_n = \frac{e^2}{2n^2 a_0} = \frac{m e^4}{2n^2 \hbar^2}
```

where $a_0$ is the Bohr radius $a_0 = \hbar^2/(me^2)$. This identification immediately allows us to write $E_\ell$ for the donor energy levels as

```{math}
:label: eq-p1-ch03-43
E_\ell = E_c - \frac{m^* e^4}{2 \varepsilon^2 \ell^2 \hbar^2}
```

where $\ell = 1, 2, 3, \ldots$ is an integer denoting the donor level quantum numbers and we identify the bottom of the conduction band $E_c$ as the ionization energy for this effective hydrogenic problem. Physically, this means that the donor levels correspond to bound (localized) states while the band states above $E_c$ correspond to delocalized nearly-free electron-like states. The lowest or “ground-state” donor energy level is then written as

```{math}
:label: eq-p1-ch03-44
E_d = E_{\ell=1} = E_c - \frac{m^* e^4}{2 \varepsilon^2 \hbar^2} .
```

It is convenient to identify the “effective” first Bohr radius for the donor level as

```{math}
:label: eq-p1-ch03-45
a_0^* = \frac{\varepsilon \hbar^2}{m^* e^2}
```

and to recognize that the wave function for the ground state donor level will be of the form

```{math}
:label: eq-p1-ch03-46
F(\vec{r}) = C e^{-r/a_0^*}
```

where $C$ is the normalization constant. Thus the solutions to {eq}`eq-p1-ch03-41` for a semiconductor are hydrogenic energy levels with the substitutions $m \to m^*$, $e^2 \to (e^2/\varepsilon)$ and the ionization energy, usually taken as the zero of energy for the hydrogen atom, now becomes $E_c$, the conduction band extremum.

For a semiconductor like germanium we have a very large dielectric constant, $\varepsilon \simeq 16$. The value for the effective mass is somewhat more difficult to specify in germanium since the constant energy surfaces for germanium are located about the $L$-points in the Brillouin zone (see §2.3.2) and are ellipsoids of revolution. Since the constant energy surfaces for such semiconductors are non-spherical, the effective mass tensor is anisotropic. However we will write down an average effective mass value $m^*/m \simeq 0.12$ (Kittel ISSP) so that we can estimate pertinent magnitudes for the donor levels in a typical semiconductor. With these values for $\varepsilon$ and $m^*$ we obtain:

```{math}
:label: eq-p1-ch03-47
E_c - E_d \simeq 0.007 \text{ eV}
```

and the effective Bohr radius

```{math}
:label: eq-p1-ch03-48
a_0^* \simeq 70 \text{ Å} .
```

These values are to be compared with the ionization energy of 13.6 eV for the hydrogen atom and with the hydrogenic Bohr orbit of $a_0 = \hbar^2/(me^2) = 0.5$ Å.

Thus we see that $a_0^*$ is indeed large enough to satisfy the requirement that $F(\vec{r})$ be slowly varying over a unit cell. On the other hand, if $a_0^*$ were to be comparable to a lattice unit cell dimension, then $F(\vec{r})$ could not be considered as a slowly varying function of $\vec{r}$ and generalizations of the above treatment would have to be made. Such generalizations involve: (1) treating $E(\vec{k})$ for a wider region of $\vec{k}$-space, and (2) relaxing the condition that impurity levels are to be associated with a single band. From the uncertainty principle, the localization in momentum space for the impurity state requires a delocalization in real space; and likewise, the converse is true, that a localized impurity in real space corresponds to a delocalized description in $\vec{k}$-space. Thus “shallow” hydrogenic donor levels (close in energy to the band extremum) can be attributed to a specific band at a specific energy extremum at $\vec{k}_0$ in the Brillouin zone. On the other hand, “deep” donor levels (far in energy from the band extremum) are not hydrogenic and have a more complicated energy level structure. Deep donor levels cannot be readily associated with a specific band or a specific $\vec{k}$ point in the Brillouin zone.

In dealing with this impurity problem, it is very tempting to discuss the donor levels in silicon and germanium. For example in silicon where the conduction band extrema are at the $\Delta$ point (see §2.3.3), the effective mass theorem requires us to replace $E(-i\vec{\nabla})$ by

```{math}
:label: eq-p1-ch03-49
E_n(-i\vec{\nabla}) \to -\frac{\hbar^2}{2m_\ell^*} \frac{\partial^2}{\partial x^2} - \frac{\hbar^2}{2m_t^*} \left( \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2} \right)
```

and the resulting Schrödinger equation can no longer be solved analytically. Although this is a very interesting problem from a practical point of view, numerical solutions are needed in this case.

## 3.4 Quasi-Classical Electron Dynamics

According to the “Correspondence Principle” of Quantum Mechanics, wavepacket solutions of Schrödinger’s equation (see §3.1) follow the trajectories of classical particles and satisfy Newton’s laws. One can give a Correspondence Principle argument for the form which is assumed by the velocity and acceleration of a wavepacket. According to the Correspondence Principle, the connection between the classical Hamiltonian and the quantum mechanical Hamiltonian is made by the identification of $\vec{p} \to (\hbar/i) \vec{\nabla}$. Thus

```{math}
:label: eq-p1-ch03-50
E_n(-i\vec{\nabla}) + \mathcal{H}'(\vec{r}) \; \longleftrightarrow \; E_n(\vec{p}/\hbar) + \mathcal{H}'(\vec{r}) = H_{\text{classical}}(\vec{p}, \vec{r}) .
```

In classical mechanics, Hamilton’s equations give the velocity according to

```{math}
:label: eq-p1-ch03-51
\dot{\vec{r}} = \frac{\partial H}{\partial \vec{p}} = \nabla_p H = \frac{1}{\hbar} \frac{\partial E(\vec{k})}{\partial \vec{k}}
```

in agreement with the group velocity for a wavepacket given by {eq}`eq-p1-ch03-13`. Hamilton’s equation for the acceleration is given by

```{math}
:label: eq-p1-ch03-52
\dot{\vec{p}} = -\frac{\partial H}{\partial \vec{r}} = -\frac{\partial \mathcal{H}'(\vec{r})}{\partial \vec{r}} .
```

For example, in the case of an applied electric field $\vec{\mathcal{E}}$ the perturbation Hamiltonian is

```{math}
:label: eq-p1-ch03-53
\mathcal{H}'(\vec{r}) = -e \vec{r} \cdot \vec{\mathcal{E}}
```

so that

```{math}
:label: eq-p1-ch03-54
\dot{\vec{p}} = \hbar \dot{\vec{k}} = e \vec{\mathcal{E}} .
```

In this equation $e\vec{\mathcal{E}}$ is the classical Coulomb force on an electric charge due to an applied field $\vec{\mathcal{E}}$. It can be shown (to be derived rigorously in the advanced course) that in the presence of a magnetic field $\vec{B}$, the acceleration theorem follows the Lorentz force equation

```{math}
:label: eq-p1-ch03-55
\dot{\vec{p}} = \hbar \dot{\vec{k}} = e\left[ \vec{\mathcal{E}} + \frac{1}{c} \vec{v} \times \vec{B} \right]
```

where

```{math}
:label: eq-p1-ch03-56
\vec{v} = \frac{1}{\hbar} \frac{\partial E(\vec{k})}{\partial \vec{k}} .
```

In the crystal, the crystal momentum $\hbar\vec{k}$ for the wavepacket plays the role of the momentum for a classical particle.

:::{figure} images/fig-p1-ch03-3.png
:name: fig-p1-ch03-3
:width: 60%
:align: center
Fig. 3.3: Displaced Fermi surface at $t = \delta t$ under the action of an electric field $\vec{\mathcal{E}}$.
:::

## 3.5 Quasi-Classical Theory of Electrical Conductivity – Ohm’s Law

We will now apply the idea of the quasi-classical electron dynamics in a solid to the problem of the electrical conductivity for a metal with an arbitrary Fermi surface and band structure. The electron is treated here as a wavepacket with momentum $\hbar\vec{k}$ moving in an external electric field $\vec{\mathcal{E}}$ in compliance with Newton’s laws. Because of the acceleration theorem, we can think of the electric field as creating a “displacement” of the electron distribution in $\vec{k}$-space. We remember that the Fermi surface encloses the region of occupied states within the Brillouin zone. The effect of the electric field is to change the wave vector $\vec{k}$ of an electron by

```{math}
:label: eq-p1-ch03-57
\delta \vec{k} = \frac{e}{\hbar} \vec{\mathcal{E}} \delta t
```

(where we note that the charge on the electron $e$ is a negative number). We picture the displacement $\delta \vec{k}$ of {eq}`eq-p1-ch03-57` by the displacement of the Fermi surface in time shown in {numref}`fig-p1-ch03-3`. From this diagram we see that the incremental volume of $\vec{k}$-space $\delta^3 V_{\vec{k}}$ which is “swept out” in the time $\delta t$ due to the presence of the field $\vec{\mathcal{E}}$ is

```{math}
:label: eq-p1-ch03-58
\delta^3 V_{\vec{k}} = \int d^2 S_F \, \hat{n} \cdot \delta \vec{k} = \int d^2 S_F \, \hat{n} \cdot \left( \frac{e}{\hbar} \vec{\mathcal{E}} \delta t \right)
```

and the electron density is found from

```{math}
:label: eq-p1-ch03-59
n = \frac{2}{(2\pi)^3} \int_{E \le E_F} d^3k
```

where $d^2 S_F$ is the element of area on the Fermi surface and $\hat{n}$ is a unit vector normal to this element of area and $\delta^3 V_{\vec{k}} \to d^3k$ both denote elements of volume in $\vec{k}$-space. The definition of the electrical current density is the current flowing through a unit area in real space and is given by the product of the [number of electrons per unit volume] with the [charge per electron] and with the [group velocity] so that the current density $\delta \vec{j}$ created by applying the electric field $\vec{\mathcal{E}}$ for a time interval $\delta t$ is given by

```{math}
:label: eq-p1-ch03-60
\delta \vec{j} = \int \left[ \frac{2}{(2\pi)^3} \right] \cdot \left[ \delta^3 V_{\vec{k}} \right] \cdot [e] \cdot [\vec{v}_g]
```

where $\vec{v}_g$ is the group velocity for electron wavepacket and $2/(2\pi)^3$ is the density of electronic states in $\vec{k}$-space (including the spin degeneracy of two) because we can put 2 electrons in each phase space state. Substitution for $\delta^3 V_{\vec{k}}$ in {eq}`eq-p1-ch03-60` by {eq}`eq-p1-ch03-58` yields the instantaneous rate of change of the current density averaged over the Fermi surface

```{math}
:label: eq-p1-ch03-61
\frac{\partial \vec{j}}{\partial t} = \frac{e^2}{4\pi^3 \hbar} \iint \vec{v}_g \, \hat{n} \cdot \vec{\mathcal{E}} \, d^2 S_F = \frac{e^2}{4\pi^3 \hbar} \iint \vec{v}_g \left( \frac{\vec{v}_g \cdot \vec{\mathcal{E}}}{|v_g|} \right) d^2 S_F
```

since the group velocity given by {eq}`eq-p1-ch03-13` is directed normal to the Fermi surface. In a real solid, the electrons will not be accelerated indefinitely, but will eventually collide with an impurity, or a lattice defect or a lattice vibration (phonon).

These collisions will serve to maintain the displacement of the Fermi surface at some steady state value, depending on $\tau$, the average time between collisions. We can introduce this relaxation time through the expression

```{math}
:label: eq-p1-ch03-62
n(t) = n(0) e^{-t/\tau}
```

where $n(t)$ is the number of electrons that have not made a collision at time $t$, assuming that the last collision had been made at time $t = 0$. The relaxation time is the average collision time

```{math}
:label: eq-p1-ch03-63
\langle t \rangle = \frac{1}{\tau} \int_0^\infty t e^{-t/\tau} dt = \tau .
```

If in {eq}`eq-p1-ch03-61`, we set $\langle \delta t \rangle = \tau$ and write the average current density as $\vec{j} = \langle \delta \vec{j} \rangle$, then we obtain

```{math}
:label: eq-p1-ch03-64
\vec{j} = \frac{e^2 \tau}{4\pi^3 \hbar} \iint \vec{v}_g \frac{\vec{v}_g \cdot \vec{\mathcal{E}}}{|v_g|} (d^2 S_F) .
```

We define the conductivity tensor as $\vec{j} = \overleftrightarrow{\sigma} \cdot \vec{\mathcal{E}}$, so that {eq}`eq-p1-ch03-64` provides an explicit expression for the tensor $\overleftrightarrow{\sigma}$:

```{math}
:label: eq-p1-ch03-65
\overleftrightarrow{\sigma} = \frac{e^2 \tau}{4\pi^3 \hbar} \iint \frac{\vec{v}_g \vec{v}_g}{|v_g|} (d^2 S_F) .
```

In the free electron limit $\overleftrightarrow{\sigma}$ becomes a scalar (isotropic conduction) and is given by the Drude formula which we derive below from {eq}`eq-p1-ch03-65`. Using the equations for the free electron limit

```{math}
:label: eq-p1-ch03-66
E = \frac{\hbar^2 k^2}{2m}, \qquad E_F = \frac{\hbar^2 k_F^2}{2m}, \qquad \vec{v}_g = \frac{\hbar \vec{k}_F}{m} .
```

We then obtain

```{math}
:label: eq-p1-ch03-67
\vec{v}_g \vec{v}_g \to v_x^2 = v_y^2 = v_z^2 = \frac{v^2}{3}
```

and

```{math}
:label: eq-p1-ch03-68
\int d^2 S_F = 4\pi k_F^2 ,
```

so that the number of electrons/unit volume can be written as

```{math}
:label: eq-p1-ch03-69
n = \frac{1}{4\pi^3} \frac{4\pi}{3} k_F^3 .
```

Therefore

```{math}
:label: eq-p1-ch03-70
\vec{j} = \frac{e^2 \tau}{4\pi^3 \hbar} \left( \frac{\hbar k_F}{m} \right) \frac{1}{3} \vec{\mathcal{E}} (4\pi k_F^2) = \frac{n e^2 \tau}{m} \vec{\mathcal{E}} .
```

Thus the free electron limit gives Ohm’s law in the familiar form

```{math}
:label: eq-p1-ch03-71
\sigma = \frac{n e^2 \tau}{m} = n e \mu ,
```

showing that the electrical conductivity in the diffusion regime where scattering is important depends on both the carrier density $n$ and the carrier mobility $\mu$. For low dimensional systems that are important on the nano-scale, in nanoscience and nanotechnology, ballistic transport is dominant, and in this regime the carriers can go from the anode to the cathode without scattering. This regime will be considered in a later lecture.

A slightly modified form of Ohm’s law is also applicable to conduction in a material for which the energy dispersion relations have a simple parabolic form and $m$ has been replaced by the effective mass $m^*$, $E(\vec{k}) = \hbar^2 k^2/2m^*$. In this case $\sigma$ is given by

```{math}
:label: eq-p1-ch03-72
\sigma = \frac{n e^2 \tau}{m^*}
```

where the effective mass is found from the band curvature $1/m^* = \partial^2 E/(\hbar^2 \partial k^2)$. The generalization of Ohm’s law can also be made to deal with solids for which the effective mass tensor is anisotropic and this will be discussed later in this course.

## 3.6 Summary

- A crystal wavepacket built from Bloch states moves with group velocity $\vec{v}_g = (1/\hbar) \partial E_n/\partial \vec{k}$ ({eq}`eq-p1-ch03-14`).
- The effective mass theorem replaces the periodic crystal Hamiltonian by an operator $E_n(-i\vec{\nabla})$ formed from the perfect-crystal band structure ({eq}`eq-p1-ch03-30`).
- For shallow donor impurities the theorem gives hydrogenic levels with scaled mass and dielectric constant ({eq}`eq-p1-ch03-43`–{eq}`eq-p1-ch03-46`).
- Quasi-classical dynamics yields the Lorentz force equation for crystal momentum ({eq}`eq-p1-ch03-55`).
- The conductivity tensor for an arbitrary Fermi surface reduces to the Drude formula in the free-electron limit ({eq}`eq-p1-ch03-65` and {eq}`eq-p1-ch03-71`).
