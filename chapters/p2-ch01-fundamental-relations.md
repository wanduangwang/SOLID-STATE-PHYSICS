---
title: "1 Review of Fundamental Relations for Optical Phenomena"
abstract: "This chapter reviews the macroscopic electromagnetic framework used to describe optical phenomena in solids. It introduces the complex dielectric function and complex optical conductivity from Maxwell's equations, derives the complex index of refraction, and connects these quantities to measurable observables such as the normal-incidence reflectivity. The distinction between intraband and interband optical processes is outlined."
---

# 1 Review of Fundamental Relations for Optical Phenomena

- G. Bekefi and A.H. Barrett, *Electromagnetic Vibrations Waves and Radiation*, MIT Press, Cambridge, MA
- J.D. Jackson, *Classical Electrodynamics*, Wiley, New York, 1975
- Bassani and Pastori-Parravicini, *Electronic States and Optical Transitions in Solids*, Pergamon Press, NY (1975)
- Yu and Cardona, *Fundamentals of Semiconductors*, Springer Verlag (1996)

## 1.0 Overview

The optical properties of solids provide an important tool for studying energy band structure, impurity levels, excitons, localized defects, lattice vibrations, and certain magnetic excitations. This chapter establishes the macroscopic electromagnetic framework that is used throughout Part II. It introduces the complex dielectric function $\varepsilon_{\text{complex}}$ and the complex optical conductivity $\sigma_{\text{complex}}$ through Maxwell's equations, derives the complex index of refraction $\tilde{N}_{\text{complex}}$, and obtains expressions for the normal-incidence reflectivity $\mathcal{R}$. It concludes by distinguishing intraband and interband optical processes.

## 1.1 Introductory Remarks on Optical Probes

The optical properties of solids provide an important tool for studying energy band structure, impurity levels, excitons, localized defects, lattice vibrations, and certain magnetic excitations. In such experiments, we measure some observable, such as reflectivity, transmission, absorption, ellipsometry or light scattering; from these measurements we deduce the dielectric function $\varepsilon(\omega)$, the optical conductivity $\sigma(\omega)$, or the fundamental excitation frequencies. It is the frequency-dependent complex dielectric function $\varepsilon(\omega)$ or the complex conductivity $\sigma(\omega)$, which is directly related to the energy band structure of solids.

The central question is the relationship between experimental observations and the electronic energy levels (energy bands) of the solid. In the infrared photon energy region, information on the phonon branches is obtained. These issues are the major concern of Part II of this course.

## 1.2 The Complex Dielectric Function and the Complex Optical Conductivity

The complex dielectric function and complex optical conductivity are introduced through Maxwell's equations (c.g.s. units):

:::{math}
:label: eq-p2-ch01-1
\nabla \times \vec{H} - \frac{1}{c}\frac{\partial \vec{D}}{\partial t} = \frac{4\pi}{c}\vec{j}
:::

:::{math}
:label: eq-p2-ch01-2
\nabla \times \vec{E} + \frac{1}{c}\frac{\partial \vec{B}}{\partial t} = 0
:::

:::{math}
:label: eq-p2-ch01-3
\nabla \cdot \vec{D} = 0
:::

:::{math}
:label: eq-p2-ch01-4
\nabla \cdot \vec{B} = 0
:::

where we have assumed that the charge density is zero. The constitutive equations are written as:

:::{math}
:label: eq-p2-ch01-5
\vec{D} = \varepsilon \vec{E}
:::

:::{math}
:label: eq-p2-ch01-6
\vec{B} = \mu \vec{H}
:::

:::{math}
:label: eq-p2-ch01-7
\vec{j} = \sigma \vec{E}
:::

Equation {eq}`eq-p2-ch01-5` defines the quantity $\varepsilon$ from which the concept of the complex dielectric function will be developed. When we discuss non-linear optics (see Chapter 11), these linear constitutive equations (Eqs. {eq}`eq-p2-ch01-5`–{eq}`eq-p2-ch01-7`) must be generalized to include higher order terms in $\vec{E}\vec{E}$ and $\vec{E}\vec{E}\vec{E}$. From Maxwell's equations and the constitutive equations, we obtain a wave equation for the field variables $\vec{E}$ and $\vec{H}$:

:::{math}
:label: eq-p2-ch01-8
\nabla^2 \vec{E} = \frac{\varepsilon\mu}{c^2}\frac{\partial^2 \vec{E}}{\partial t^2} + \frac{4\pi\sigma\mu}{c^2}\frac{\partial \vec{E}}{\partial t}
:::

and

:::{math}
:label: eq-p2-ch01-9
\nabla^2 \vec{H} = \frac{\varepsilon\mu}{c^2}\frac{\partial^2 \vec{H}}{\partial t^2} + \frac{4\pi\sigma\mu}{c^2}\frac{\partial \vec{H}}{\partial t}
:::

For optical fields, we must look for a sinusoidal solution to Eqs. {eq}`eq-p2-ch01-8` and {eq}`eq-p2-ch01-9`:

:::{math}
:label: eq-p2-ch01-10
\vec{E} = \vec{E}_0 e^{i(\vec{K}\cdot\vec{r} - \omega t)}
:::

where $\vec{K}$ is a complex propagation constant and $\omega$ is the frequency of the light. A solution similar to Eq. {eq}`eq-p2-ch01-10` is obtained for the $\vec{H}$ field. The real part of $\vec{K}$ can be identified as a wave vector, while the imaginary part of $\vec{K}$ accounts for attenuation of the wave inside the solid. Substitution of the plane wave solution Eq. {eq}`eq-p2-ch01-10` into the wave equation Eq. {eq}`eq-p2-ch01-8` yields the following relation for $K$:

:::{math}
:label: eq-p2-ch01-11
-K^2 = -\frac{\varepsilon\mu\omega^2}{c^2} - \frac{4\pi i \sigma \mu \omega}{c^2}
:::

If there were no losses (or attenuation), $K$ would be equal to

:::{math}
:label: eq-p2-ch01-12
K_0 = \frac{\omega}{c}\sqrt{\varepsilon\mu}
:::

and would be real, but since there are losses we write

:::{math}
:label: eq-p2-ch01-13
K = \frac{\omega}{c}\sqrt{\varepsilon_{\text{complex}}\mu}
:::

where we have defined the complex dielectric function as

:::{math}
:label: eq-p2-ch01-14
\varepsilon_{\text{complex}} = \varepsilon + \frac{4\pi i \sigma}{\omega} = \varepsilon_1 + i\varepsilon_2
:::

As shown in Eq. {eq}`eq-p2-ch01-14` it is customary to write $\varepsilon_1$ and $\varepsilon_2$ for the real and imaginary parts of $\varepsilon_{\text{complex}}$. From the definition in Eq. {eq}`eq-p2-ch01-14` it also follows that

:::{math}
:label: eq-p2-ch01-15
\varepsilon_{\text{complex}} = \frac{4\pi i}{\omega}\left[\sigma + \frac{\varepsilon\omega}{4\pi i}\right] = \frac{4\pi i}{\omega}\sigma_{\text{complex}}
:::

where we define the complex conductivity $\sigma_{\text{complex}}$ as:

:::{math}
:label: eq-p2-ch01-16
\sigma_{\text{complex}} = \sigma + \frac{\varepsilon\omega}{4\pi i}
:::

Now that we have defined the complex dielectric function $\varepsilon_{\text{complex}}$ and the complex conductivity $\sigma_{\text{complex}}$, we will relate these quantities in two ways:

1. to observables such as the reflectivity which we measure in the laboratory,
2. to properties of the solid such as the carrier density, relaxation time, effective masses, energy band gaps, etc.

After substitution for $K$ in Eq. {eq}`eq-p2-ch01-10`, the solution Eq. {eq}`eq-p2-ch01-11` to the wave equation (Eq. {eq}`eq-p2-ch01-8`) yields a plane wave

:::{math}
:label: eq-p2-ch01-17
\vec{E}(z,t) = \vec{E}_0 e^{-i\omega t} \exp\left(i\frac{\omega z}{c}\sqrt{\varepsilon\mu}\sqrt{1 + \frac{4\pi i \sigma}{\varepsilon\omega}}\right)
:::

For the wave propagating in vacuum ($\varepsilon=1$, $\mu=1$, $\sigma=0$), Eq. {eq}`eq-p2-ch01-17` reduces to a simple plane wave solution, while if the wave is propagating in a medium of finite electrical conductivity, the amplitude of the wave exponentially decays over a characteristic distance $\delta$ given by

:::{math}
:label: eq-p2-ch01-18
\delta = \frac{c}{\omega \tilde{N}_2(\omega)} = \frac{c}{\omega \tilde{k}(\omega)}
:::

where $\delta$ is called the optical skin depth, and $\tilde{k}$ is the imaginary part of the complex index of refraction (also called the extinction coefficient)

:::{math}
:label: eq-p2-ch01-19
\tilde{N}(\omega) = \sqrt{\mu\varepsilon_{\text{complex}}} = \sqrt{\varepsilon\mu\left(1 + \frac{4\pi i \sigma}{\varepsilon\omega}\right)} = \tilde{n}(\omega) + i\tilde{k}(\omega)
:::

This means that the *intensity* of the electric field, $|E|^2$, falls off to $1/e$ of its value at the surface in a distance

:::{math}
:label: eq-p2-ch01-20
\frac{1}{\alpha_{\text{abs}}} = \frac{c}{2\omega \tilde{k}(\omega)}
:::

where $\alpha_{\text{abs}}(\omega)$ is the absorption coefficient for the solid at frequency $\omega$.

Since light is described by a transverse wave, there are two possible orthogonal directions for the $\vec{E}$ vector in a plane normal to the propagation direction and these directions determine the *polarization* of the light. For cubic materials, the index of refraction is the same along the two transverse directions. However, for anisotropic media, the indices of refraction may be different for the two polarization directions, as is further discussed in §2.1.

## 1.3 Relation of Complex Dielectric Function to Observables

In relating $\varepsilon_{\text{complex}}$ and $\sigma_{\text{complex}}$ to the observables, it is convenient to introduce a complex index of refraction $\tilde{N}_{\text{complex}}$:

:::{math}
:label: eq-p2-ch01-21
\tilde{N}_{\text{complex}} = \sqrt{\mu\varepsilon_{\text{complex}}}
:::

where

:::{math}
:label: eq-p2-ch01-22
K = \frac{\omega}{c}\tilde{N}_{\text{complex}}
:::

and where $\tilde{N}_{\text{complex}}$ is usually written in terms of its real and imaginary parts (see Eq. {eq}`eq-p2-ch01-19`)

:::{math}
:label: eq-p2-ch01-23
\tilde{N}_{\text{complex}} = \tilde{n} + i\tilde{k} = \tilde{N}_1 + i\tilde{N}_2
:::

The quantities $\tilde{n}$ and $\tilde{k}$ are collectively called **the optical constants** of the solid, where $\tilde{n}$ is the index of refraction and $\tilde{k}$ is the extinction coefficient. (We use the tilde over the optical constants $\tilde{n}$ and $\tilde{k}$ to distinguish them from the carrier density and wave vector which are denoted by $n$ and $k$). The extinction coefficient $\tilde{k}$ vanishes for lossless materials. For non-magnetic materials, we can take $\mu=1$, and this will be done in writing the equations below.

With this definition for $\tilde{N}_{\text{complex}}$, we can relate

:::{math}
:label: eq-p2-ch01-24
\varepsilon_{\text{complex}} = \varepsilon_1 + i\varepsilon_2 = (\tilde{n} + i\tilde{k})^2
:::

yielding the important relations

:::{math}
:label: eq-p2-ch01-25
\varepsilon_1 = \tilde{n}^2 - \tilde{k}^2
:::

:::{math}
:label: eq-p2-ch01-26
\varepsilon_2 = 2\tilde{n}\tilde{k}
:::

where we note that $\varepsilon_1, \varepsilon_2, \tilde{n}$ and $\tilde{k}$ are all frequency dependent.

Many measurements of the optical properties of solids involve the normal incidence reflectivity which is illustrated in {numref}`fig-p2-ch01-1`. Inside the solid, the wave will be attenuated. We assume for the present discussion that the solid is thick enough so that reflections from the back surface can be neglected. We can then write the wave inside the solid for this one-dimensional propagation problem as

:::{math}
:label: eq-p2-ch01-27
E_x = E_0 e^{i(Kz - \omega t)}
:::

where the complex propagation constant for the light is given by $K = (\omega/c)\tilde{N}_{\text{complex}}$.

On the other hand, in free space we have both an incident and a reflected wave:

:::{math}
:label: eq-p2-ch01-28
E_x = E_1 e^{i\left(\frac{\omega z}{c} - \omega t\right)} + E_2 e^{i\left(\frac{-\omega z}{c} - \omega t\right)}
:::

:::{figure} images/fig-p2-ch01-1.png
:name: fig-p2-ch01-1
:width: 80%
:align: center
Figure 1.1: Schematic diagram for normal incidence reflectivity.
:::

From Eqs. {eq}`eq-p2-ch01-27` and {eq}`eq-p2-ch01-28`, the continuity of $E_x$ across the surface of the solid requires that

:::{math}
:label: eq-p2-ch01-29
E_0 = E_1 + E_2
:::

With $\vec{E}$ in the $x$ direction, the second relation between $E_0, E_1$, and $E_2$ follows from the continuity condition for tangential $H_y$ across the boundary of the solid. From Maxwell's equation (Eq. {eq}`eq-p2-ch01-2`) we have

:::{math}
:label: eq-p2-ch01-30
\nabla \times \vec{E} = \frac{-\mu}{c}\frac{\partial \vec{H}}{\partial t} = \frac{i\mu\omega}{c}\vec{H}
:::

which results in

:::{math}
:label: eq-p2-ch01-31
\frac{\partial E_x}{\partial z} = \frac{i\mu\omega}{c}H_y
:::

The continuity condition on $H_y$ thus yields a continuity relation for $\partial E_x/\partial z$ so that from Eq. {eq}`eq-p2-ch01-31`

:::{math}
:label: eq-p2-ch01-32
E_0 K = E_1 \frac{\omega}{c} - E_2 \frac{\omega}{c} = E_0 \frac{\omega}{c}\tilde{N}_{\text{complex}}
:::

or

:::{math}
:label: eq-p2-ch01-33
E_1 - E_2 = E_0 \tilde{N}_{\text{complex}}
:::

The normal incidence reflectivity $\mathcal{R}$ is then written as

:::{math}
:label: eq-p2-ch01-34
\mathcal{R} = \left|\frac{E_2}{E_1}\right|^2
:::

which is most conveniently related to the reflection coefficient $r$ given by

:::{math}
:label: eq-p2-ch01-35
r = \frac{E_2}{E_1}
:::

From Eqs. {eq}`eq-p2-ch01-29` and {eq}`eq-p2-ch01-33`, we have the results

:::{math}
:label: eq-p2-ch01-36
E_2 = \frac{1}{2}E_0(1 - \tilde{N}_{\text{complex}})
:::

:::{math}
:label: eq-p2-ch01-37
E_1 = \frac{1}{2}E_0(1 + \tilde{N}_{\text{complex}})
:::

so that the normal incidence reflectivity becomes

:::{math}
:label: eq-p2-ch01-38
\mathcal{R} = \left|\frac{1 - \tilde{N}_{\text{complex}}}{1 + \tilde{N}_{\text{complex}}}\right|^2 = \frac{(1 - \tilde{n})^2 + \tilde{k}^2}{(1 + \tilde{n})^2 + \tilde{k}^2}
:::

and the reflection coefficient for the wave itself is given by

:::{math}
:label: eq-p2-ch01-39
r = \frac{1 - \tilde{n} - i\tilde{k}}{1 + \tilde{n} + i\tilde{k}}
:::

where the reflectivity $\mathcal{R}$ is a number less than unity and $r$ has an amplitude of less than unity. We have now related one of the physical observables to the optical constants. To relate these results to the power absorbed and transmitted at normal incidence, we utilize the following relation which expresses the idea that all the incident power is either reflected, absorbed, or transmitted

:::{math}
:label: eq-p2-ch01-40
1 = \mathcal{R} + \mathcal{A} + \mathcal{T}
:::

where $\mathcal{R}$, $\mathcal{A}$, and $\mathcal{T}$ are, respectively, the fraction of the power that is reflected, absorbed, and transmitted as illustrated in {numref}`fig-p2-ch01-1`. At high temperatures, the most common observable is the emissivity, which is equal to the absorbed power for a black body or is equal to $1 - \mathcal{R}$ assuming $\mathcal{T}=0$. As a homework exercise, it is instructive to derive expressions for $\mathcal{R}$ and $\mathcal{T}$ when we have relaxed the restriction of no reflection from the back surface. Multiple reflections are encountered in thin films.

The discussion thus far has been directed toward relating the complex dielectric function or the complex conductivity to physical observables. If we know the optical constants, then we can find the reflectivity. We now want to ask the opposite question. Suppose we know the reflectivity, can we find the optical constants? Since there are two optical constants, $\tilde{n}$ and $\tilde{k}$, we need to make two independent measurements, such as the reflectivity at two different angles of incidence.

Nevertheless, even if we limit ourselves to normal incidence reflectivity measurements, we can still obtain both $\tilde{n}$ and $\tilde{k}$ provided that we make these reflectivity measurements for all frequencies. This is possible because the real and imaginary parts of a complex physical function are not independent. Because of causality, $\tilde{n}(\omega)$ and $\tilde{k}(\omega)$ are related through the Kramers–Kronig relation, which we will discuss in Chapter 6. Since normal incidence measurements are easier to carry out in practice, it is quite possible to study the optical properties of solids with just normal incidence measurements, and then do a Kramers–Kronig analysis of the reflectivity data to obtain the frequency-dependent dielectric functions $\varepsilon_1(\omega)$ and $\varepsilon_2(\omega)$ or the frequency-dependent optical constants $\tilde{n}(\omega)$ and $\tilde{k}(\omega)$.

In treating a solid, we will need to consider contributions to the optical properties from various electronic energy band processes. To begin with, there are **intraband processes** which correspond to the electronic conduction by free carriers, and hence are more important in conducting materials such as metals, semimetals and degenerate semiconductors. These intraband processes can be understood in their simplest terms by the classical Drude theory, or in more detail by the classical Boltzmann equation or the quantum mechanical density matrix technique. In addition to the intraband (free carrier) processes, there are **interband processes** which correspond to the absorption of electromagnetic radiation by an electron in an occupied state below the Fermi level, thereby inducing a transition to an unoccupied state in a higher band. This interband process is intrinsically a quantum mechanical process and must be discussed in terms of quantum mechanical concepts. In practice, we consider in detail the contribution of only a few energy bands to optical properties; in many cases we also restrict ourselves to detailed consideration of only a portion of the Brillouin zone where strong interband transitions occur. The intraband and interband contributions that are neglected are treated in an approximate way by introducing a core dielectric constant which is often taken to be independent of frequency and external parameters.

## 1.4 Units for Frequency Measurements

The frequency of light is measured in several different units in the literature. The relation between the various units are: $1\ \text{eV} = 8065.5\ \text{cm}^{-1} = 2.418 \times 10^{14}\ \text{Hz} = 11{,}600\ \text{K}$. Also $1\ \text{eV}$ corresponds to a wavelength of $1.2398\ \mu\text{m}$, and $1\ \text{cm}^{-1} = 0.12398\ \text{meV} = 3 \times 10^{10}\ \text{Hz}$.
