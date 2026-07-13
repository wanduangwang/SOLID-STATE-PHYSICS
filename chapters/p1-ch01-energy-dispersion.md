---
title: "1 Review of Energy Dispersion Relations in Solids"
abstract: 'This chapter reviews the single-electron energy dispersion relations $E(\vec{k})$ in solids, focusing on the weak binding (nearly free electron) and tight binding approximations, and introduces effective mass, group velocity, and the two-atom unit-cell extension for polyacetylene.'
---

# 1 Review of Energy Dispersion Relations in Solids

## 1.0 Overview

The transport properties of solids are closely related to the energy dispersion relations $E(\vec{k})$ in these materials, and in particular to the behavior of $E(\vec{k})$ near the Fermi level. Conversely, the analysis of transport measurements provides a great deal of information on $E(\vec{k})$. Although transport measurements do not generally provide the most sensitive tool for studying $E(\vec{k})$, such measurements are fundamental to solid state physics because they can be carried out on nearly all materials and therefore provide a valuable tool for characterizing materials. To provide the necessary background for the discussion of transport properties, we give here a brief review of the energy dispersion relations $E(\vec{k})$ in solids. In this connection, we consider in Chapter 1 the two limiting cases of weak and tight binding. In Chapter 2 we will discuss $E(\vec{k})$ for real solids including prototype metals, semiconductors, semimetals and insulators.

**References:**

- Ashcroft and Mermin, *Solid State Physics*, Holt, Rinehart and Winston, 1976, Chapters 8, 9, 10, 11.
- Bassani and Parravicini, *Electronic States and Optical Transitions in Solids*, Pergamon, 1975, Chapter 3.
- Kittel, *Introduction to Solid State Physics*, Wiley, 1986, pp. 228-239.
- Mott & Jones – *The Theory of the Properties of Metals and Alloys*, Dover, 1958 pp. 56–85.
- Omar, *Elementary Solid State Physics*, Addison–Wesley, 1975, pp. 189–210.
- Ziman, *Principles of the Theory of Solids*, Cambridge, 1972, Chapter 3.

## 1.1 Introduction

The transport properties of solids are closely related to the energy dispersion relations $E(\vec{k})$ in these materials and in particular to the behavior of $E(\vec{k})$ near the Fermi level. Conversely, the analysis of transport measurements provides a great deal of information on $E(\vec{k})$. Although transport measurements do not generally provide the most sensitive tool for studying $E(\vec{k})$, such measurements are fundamental to solid state physics because they can be carried out on nearly all materials and therefore provide a valuable tool for characterizing materials. To provide the necessary background for the discussion of transport properties, we give here a brief review of the energy dispersion relations $E(\vec{k})$ in solids. In this connection, we consider in Chapter 1 the two limiting cases of weak and tight binding. In Chapter 2 we will discuss $E(\vec{k})$ for real solids including prototype metals, semiconductors, semimetals and insulators.

## 1.2 One Electron $E(\vec{k})$ in Solids

### 1.2.1 Weak Binding or Nearly Free Electron Approximation

In the weak binding approximation, we assume that the periodic potential $V(\vec{r}) = V(\vec{r}+\vec{R}_n)$ is sufficiently weak so that the electrons behave almost as if they were free and the effect of the periodic potential can be handled in perturbation theory (see Appendix A). In this formulation $V(\vec{r})$ can be an *arbitrary* periodic potential. The weak binding approximation has achieved some success in describing the valence electrons in metals. For the core electrons, however, the potential energy is comparable with the kinetic energy so that core electrons are tightly bound and the weak binding approximation is not applicable. In the weak binding approximation we solve the Schrödinger equation in the limit of a very weak periodic potential

```{math}
:label: eq-p1-ch01-1
\mathcal{H}\psi = E\psi .
```

Using time-independent perturbation theory (see Appendix A) we write

```{math}
:label: eq-p1-ch01-2
E(\vec{k}) = E^{(0)}(\vec{k}) + E^{(1)}(\vec{k}) + E^{(2)}(\vec{k}) + \ldots
```

and take the unperturbed solution to correspond to $V(\vec{r}) = 0$ so that $E^{(0)}(\vec{k})$ is the plane wave solution

```{math}
:label: eq-p1-ch01-3
E^{(0)}(\vec{k}) = \frac{\hbar^2 k^2}{2m} .
```

The corresponding normalized eigenfunctions are the plane wave states

```{math}
:label: eq-p1-ch01-4
\psi^{(0)}_{\vec{k}}(\vec{r}) = \frac{e^{i\vec{k}\cdot\vec{r}}}{\Omega^{1/2}}
```

in which $\Omega$ is the volume of the crystal.

The first order correction to the energy $E^{(1)}(\vec{k})$ is the diagonal matrix element of the perturbation potential taken between the unperturbed states:

```{math}
:label: eq-p1-ch01-5
E^{(1)}(\vec{k}) = \langle \psi^{(0)}_{\vec{k}} \mid V(\vec{r}) \mid \psi^{(0)}_{\vec{k}} \rangle = \frac{1}{\Omega} \int_{\Omega} e^{-i\vec{k}\cdot\vec{r}} V(\vec{r}) e^{i\vec{k}\cdot\vec{r}} d^3r = \frac{1}{\Omega_0} \int_{\Omega_0} V(\vec{r}) d^3r = \overline{V(\vec{r})}
```

where $\overline{V(\vec{r})}$ is independent of $\vec{k}$, and $\Omega_0$ is the volume of the unit cell. Thus, in first order perturbation theory, we merely add a constant energy $\overline{V(\vec{r})}$ to the free particle energy, and that constant term is exactly the mean potential energy seen by the electron, averaged over the unit cell. The terms of interest arise in second order perturbation theory and are

```{math}
:label: eq-p1-ch01-6
E^{(2)}(\vec{k}) = \sum_{\vec{k}'}' \frac{|\langle \vec{k}' \mid V(\vec{r}) \mid \vec{k} \rangle|^2}{E^{(0)}(\vec{k}) - E^{(0)}(\vec{k}')}
```

where the prime on the summation indicates that $\vec{k}' \neq \vec{k}$. We next compute the matrix element $\langle \vec{k}' \mid V(\vec{r}) \mid \vec{k} \rangle$ as follows:

```{math}
:label: eq-p1-ch01-7
\langle \vec{k}' \mid V(\vec{r}) \mid \vec{k} \rangle = \frac{1}{\Omega} \int_{\Omega} e^{-i(\vec{k}'-\vec{k})\cdot\vec{r}} V(\vec{r}) d^3r = \frac{1}{\Omega} \int_{\Omega} e^{i\vec{q}\cdot\vec{r}} V(\vec{r}) d^3r ,
```

where $\vec{q} = \vec{k} - \vec{k}'$ is the difference wave vector and the integration is over the whole crystal. We now exploit the periodicity of $V(\vec{r})$. Let $\vec{r} = \vec{r}' + \vec{R}_n$ where $\vec{r}'$ is an arbitrary vector in a unit cell and $\vec{R}_n$ is a lattice vector. Then because of the periodicity $V(\vec{r}) = V(\vec{r}')$

```{math}
:label: eq-p1-ch01-8
\langle \vec{k}' \mid V(\vec{r}) \mid \vec{k} \rangle = \frac{1}{\Omega} \sum_n \int_{\Omega_0} e^{i\vec{q}\cdot(\vec{r}'+\vec{R}_n)} V(\vec{r}') d^3r'
```

where the sum is over unit cells and the integration is over the volume of one unit cell. Then

```{math}
:label: eq-p1-ch01-9
\langle \vec{k}' \mid V(\vec{r}) \mid \vec{k} \rangle = \frac{1}{\Omega} \sum_n e^{i\vec{q}\cdot\vec{R}_n} \int_{\Omega_0} e^{i\vec{q}\cdot\vec{r}'} V(\vec{r}') d^3r' .
```

Writing the following expressions for the lattice vectors $\vec{R}_n$ and for the wave vector $\vec{q}$

```{math}
:label: eq-p1-ch01-10
\vec{R}_n = \sum_{j=1}^3 n_j \vec{a}_j \,; \qquad \vec{q} = \sum_{j=1}^3 \alpha_j \vec{b}_j
```

where $n_j$ is an integer, then the lattice sum $\sum_n e^{i\vec{q}\cdot\vec{R}_n}$ can be carried out exactly to yield

```{math}
:label: eq-p1-ch01-11
\sum_n e^{i\vec{q}\cdot\vec{R}_n} = \left[ \prod_{j=1}^3 \frac{1 - e^{2\pi i N_j \alpha_j}}{1 - e^{2\pi i \alpha_j}} \right]
```

where $N = N_1 N_2 N_3$ is the total number of unit cells in the crystal and $\alpha_j$ is a real number. This sum fluctuates wildly as $\vec{q}$ varies and averages to zero. The sum is appreciable only if

```{math}
:label: eq-p1-ch01-12
\vec{q} = \sum_{j=1}^3 m_j \vec{b}_j
```

where $m_j$ is an integer and $\vec{b}_j$ is a primitive vector in reciprocal space, so that $\vec{q}$ must be a reciprocal lattice vector. Hence we have

```{math}
:label: eq-p1-ch01-13
\sum_n e^{i\vec{q}\cdot\vec{R}_n} = N \delta_{\vec{q},\vec{G}}
```

since $\vec{b}_j \cdot \vec{R}_n = 2\pi l_{jn}$ where $l_{jn}$ is an integer.

This discussion shows that the matrix element $\langle \vec{k}' \mid V(\vec{r}) \mid \vec{k} \rangle$ is only important when $\vec{q} = \vec{G}$ is a reciprocal lattice vector $= \vec{k} - \vec{k}'$ from which we conclude that the periodic potential $V(\vec{r})$ only connects wave vectors $\vec{k}$ and $\vec{k}'$ separated by a reciprocal lattice vector. We note that this is the same relation that determines the Brillouin zone boundary. The matrix element is then

```{math}
:label: eq-p1-ch01-14
\langle \vec{k}' \mid V(\vec{r}) \mid \vec{k} \rangle = \frac{N}{\Omega} \int_{\Omega_0} e^{i\vec{G}\cdot\vec{r}'} V(\vec{r}') d^3r' \, \delta_{\vec{k}'-\vec{k},\vec{G}}
```

where

```{math}
:label: eq-p1-ch01-15
\frac{N}{\Omega} = \frac{1}{\Omega_0}
```

and the integration is over the unit cell. We introduce $V_{\vec{G}} =$ Fourier coefficient of $V(\vec{r})$ where

```{math}
:label: eq-p1-ch01-16
V_{\vec{G}} = \frac{1}{\Omega_0} \int_{\Omega_0} e^{i\vec{G}\cdot\vec{r}'} V(\vec{r}') d^3r'
```

so that

```{math}
:label: eq-p1-ch01-17
\langle \vec{k}' \mid V(\vec{r}) \mid \vec{k} \rangle = \delta_{\vec{k}-\vec{k}',\vec{G}} \, V_{\vec{G}} .
```

We can now use this matrix element to calculate the $2^{nd}$ order change in the energy based on perturbation theory (see Appendix A)

```{math}
:label: eq-p1-ch01-18
E^{(2)}(\vec{k}) = \sum_{\vec{G}} \frac{|V_{\vec{G}}|^2}{k^2 - (\vec{G}+\vec{k})^2} \left( \frac{2m}{\hbar^2} \right) = \frac{2m}{\hbar^2} \sum_{\vec{G}} \frac{|V_{\vec{G}}|^2}{k^2 - (\vec{G}+\vec{k})^2} .
```

We observe that when $k^2 = (\vec{G}+\vec{k})^2$ the denominator in {eq}`eq-p1-ch01-18` vanishes and $E^{(2)}(\vec{k})$ can become very large. This condition is identical with the Laue diffraction condition. Thus, at a Brillouin zone boundary, the weak perturbing potential has a very large effect and therefore non-degenerate perturbation theory will not work in this case.

For $\vec{k}$ values near a Brillouin zone boundary, we must then use degenerate perturbation theory (see Appendix A). Since the matrix elements coupling the plane wave states $\vec{k}$ and $\vec{k}+\vec{G}$ do not vanish, *first-order degenerate* perturbation theory is sufficient and leads to the determinantal equation

```{math}
:label: eq-p1-ch01-19
\begin{vmatrix}
E^{(0)}(\vec{k}) + E^{(1)}(\vec{k}) - E & \langle \vec{k}+\vec{G} \mid V(\vec{r}) \mid \vec{k} \rangle \\
\langle \vec{k} \mid V(\vec{r}) \mid \vec{k}+\vec{G} \rangle & E^{(0)}(\vec{k}+\vec{G}) + E^{(1)}(\vec{k}+\vec{G}) - E
\end{vmatrix} = 0
```

in which

```{math}
:label: eq-p1-ch01-20
E^{(0)}(\vec{k}) = \frac{\hbar^2 k^2}{2m} \,; \qquad E^{(0)}(\vec{k}+\vec{G}) = \frac{\hbar^2 (\vec{k}+\vec{G})^2}{2m}
```

and

```{math}
:label: eq-p1-ch01-21
E^{(1)}(\vec{k}) = \langle \vec{k} \mid V(\vec{r}) \mid \vec{k} \rangle = \overline{V(\vec{r})} = V_0
```

```{math}
:label: eq-p1-ch01-22
E^{(1)}(\vec{k}+\vec{G}) = \langle \vec{k}+\vec{G} \mid V(\vec{r}) \mid \vec{k}+\vec{G} \rangle = V_0 .
```

Solution of this determinantal equation ({eq}`eq-p1-ch01-19`) yields

```{math}
:label: eq-p1-ch01-23
[E - V_0 - E^{(0)}(\vec{k})][E - V_0 - E^{(0)}(\vec{k}+\vec{G})] - |V_{\vec{G}}|^2 = 0 ,
```

or equivalently

```{math}
:label: eq-p1-ch01-24
E^2 - E[2V_0 + E^{(0)}(\vec{k}) + E^{(0)}(\vec{k}+\vec{G})] + [V_0 + E^{(0)}(\vec{k})][V_0 + E^{(0)}(\vec{k}+\vec{G})] - |V_{\vec{G}}|^2 = 0 .
```

Solution of the quadratic equation ({eq}`eq-p1-ch01-24`) yields

```{math}
:label: eq-p1-ch01-25
E^{\pm} = V_0 + \frac{1}{2}[E^{(0)}(\vec{k}) + E^{(0)}(\vec{k}+\vec{G})] \pm \frac{1}{2}\sqrt{[E^{(0)}(\vec{k}) - E^{(0)}(\vec{k}+\vec{G})]^2 + |V_{\vec{G}}|^2}
```

and we come out with two solutions for the two strongly coupled states. It is of interest to look at these two solutions in two limiting cases:

**Case (i)** $|V_{\vec{G}}| \ll \frac{1}{2}|[E^{(0)}(\vec{k}) - E^{(0)}(\vec{k}+\vec{G})]|$

In this case we can expand the square root expression in {eq}`eq-p1-ch01-25` for small $|V_{\vec{G}}|$ to obtain:

```{math}
:label: eq-p1-ch01-26
\begin{aligned}
E(\vec{k}) &= V_0 + \frac{1}{2}[E^{(0)}(\vec{k}) + E^{(0)}(\vec{k}+\vec{G})] \\
&\quad \pm \frac{1}{2}[E^{(0)}(\vec{k}) - E^{(0)}(\vec{k}+\vec{G})] \cdot \left[ 1 + \frac{2|V_{\vec{G}}|^2}{[E^{(0)}(\vec{k}) - E^{(0)}(\vec{k}+\vec{G})]^2} + \ldots \right]
\end{aligned}
```

which simplifies to the two solutions:

```{math}
:label: eq-p1-ch01-27
E^{-}(\vec{k}) = V_0 + E^{(0)}(\vec{k}) + \frac{|V_{\vec{G}}|^2}{E^{(0)}(\vec{k}) - E^{(0)}(\vec{k}+\vec{G})}
```

```{math}
:label: eq-p1-ch01-28
E^{+}(\vec{k}) = V_0 + E^{(0)}(\vec{k}+\vec{G}) + \frac{|V_{\vec{G}}|^2}{E^{(0)}(\vec{k}+\vec{G}) - E^{(0)}(\vec{k})}
```

and we recover the result obtained before using non-degenerate perturbation theory. This result in {eq}`eq-p1-ch01-18` is valid far from the Brillouin zone boundary, but near the zone boundary the more complete expression of {eq}`eq-p1-ch01-25` must be used.

**Case (ii)** $|V_{\vec{G}}| \gg \frac{1}{2}|[E^{(0)}(\vec{k}) - E^{(0)}(\vec{k}+\vec{G})]|$

Sufficiently close to the Brillouin zone boundary

```{math}
:label: eq-p1-ch01-29
|E^{(0)}(\vec{k}) - E^{(0)}(\vec{k}+\vec{G})| \ll |V_{\vec{G}}|
```

so that we can expand $E(\vec{k})$ as given by {eq}`eq-p1-ch01-25` to obtain

```{math}
:label: eq-p1-ch01-30
E^{\pm}(\vec{k}) = \frac{1}{2}[E^{(0)}(\vec{k}) + E^{(0)}(\vec{k}+\vec{G})] + V_0 \pm \left[ |V_{\vec{G}}| + \frac{1}{8} \frac{[E^{(0)}(\vec{k}) - E^{(0)}(\vec{k}+\vec{G})]^2}{|V_{\vec{G}}|} + \ldots \right]
```

```{math}
:label: eq-p1-ch01-31
\cong \frac{1}{2}[E^{(0)}(\vec{k}) + E^{(0)}(\vec{k}+\vec{G})] + V_0 \pm |V_{\vec{G}}| ,
```

so that at the Brillouin zone boundary $E^{+}(\vec{k})$ is elevated by $|V_{\vec{G}}|$, while $E^{-}(\vec{k})$ is depressed by $|V_{\vec{G}}|$ and the band gap that is formed is $2|V_{\vec{G}}|$, where $\vec{G}$ is the reciprocal lattice vector for which $E(\vec{k}_{B.Z.}) = E(\vec{k}_{B.Z.} + \vec{G})$ and

```{math}
:label: eq-p1-ch01-32
V_{\vec{G}} = \frac{1}{\Omega_0} \int_{\Omega_0} e^{i\vec{G}\cdot\vec{r}} V(\vec{r}) d^3r .
```

From this discussion it is clear that every Fourier component of the periodic potential gives rise to a specific band gap. We see further that the *band gap* represents a range of energy values for which there is no solution to the eigenvalue problem of {eq}`eq-p1-ch01-19` for real $k$ (see {numref}`fig-p1-ch01-1`). In the band gap we assign an imaginary value to the wave vector which can be interpreted as a highly damped and non-propagating wave.

:::{figure} images/fig-p1-ch01-1.png
:name: fig-p1-ch01-1
:width: 70%
:align: center
Fig. 1.1: One dimensional electron energy bands for the nearly free electron model shown in the extended Brillouin zone scheme. The dashed curve corresponds to the case of free electrons and the solid curves to the case where a weak periodic potential is present. The band gaps at the zone boundaries are $2|V_{\vec{G}}|$.
:::

We note that the larger the value of $\vec{G}$, the smaller the value of $V_{\vec{G}}$, so that higher Fourier components give rise to smaller band gaps. Near these energy discontinuities, the wave functions become linear combinations of the unperturbed states

```{math}
:label: eq-p1-ch01-33
\psi_{\vec{k}} = \alpha_1 \psi^{(0)}_{\vec{k}} + \beta_1 \psi^{(0)}_{\vec{k}+\vec{G}}
```

```{math}
:label: eq-p1-ch01-34
\psi_{\vec{k}+\vec{G}} = \alpha_2 \psi^{(0)}_{\vec{k}} + \beta_2 \psi^{(0)}_{\vec{k}+\vec{G}}
```

and at the zone boundary itself, instead of traveling waves $e^{i\vec{k}\cdot\vec{r}}$, the wave functions become standing waves $\cos\vec{k}\cdot\vec{r}$ and $\sin\vec{k}\cdot\vec{r}$. We note that the $\cos(\vec{k}\cdot\vec{r})$ solution corresponds to a maximum in the charge density at the lattice sites and therefore corresponds to an energy minimum (the lower level). Likewise, the $\sin(\vec{k}\cdot\vec{r})$ solution corresponds to a minimum in the charge density and therefore corresponds to a maximum in the energy, thus forming the upper level.

In constructing $E(\vec{k})$ for the reduced zone scheme we make use of the periodicity of $E(\vec{k})$ in reciprocal space

```{math}
:label: eq-p1-ch01-35
E(\vec{k}+\vec{G}) = E(\vec{k}) .
```

The reduced zone scheme more clearly illustrates the formation of energy bands (labeled (1) and (2) in {numref}`fig-p1-ch01-2`), band gaps $E_g$ and band widths (defined in {numref}`fig-p1-ch01-2` as the range of energy between $E_{min}$ and $E_{max}$ for a given energy band).

:::{figure} images/fig-p1-ch01-2.png
:name: fig-p1-ch01-2
:width: 90%
:align: center
Fig. 1.2: (a) One dimensional electron energy bands for the nearly free electron model shown in the extended Brillouin zone scheme for the three bands of lowest energy. (b) The same $E(\vec{k})$ as in (a) but now shown on the reduced zone scheme. The shaded areas denote the band gaps between bands $n$ and $n+1$ and the white areas the band states.
:::

We now discuss the connection between the $E(\vec{k})$ relations shown above and the transport properties of solids, which can be illustrated by considering the case of a semiconductor. An intrinsic semiconductor at temperature $T = 0$ has no carriers so that the Fermi level runs right through the band gap. On the diagram of {numref}`fig-p1-ch01-2`, this would mean that the Fermi level might run between bands (1) and (2), so that band (1) is completely occupied and band (2) is completely empty. One further property of the semiconductor is that the band gap $E_g$ be small enough so that at some temperature (e.g., room temperature) there will be reasonable numbers of thermally excited carriers, perhaps $10^{15}/\mathrm{cm}^3$. The doping with donor (electron donating) impurities will raise the Fermi level and doping with acceptor (electron extracting) impurities will lower the Fermi level. Neglecting for the moment the effect of impurities on the $E(\vec{k})$ relations for the perfectly periodic crystal, let us consider what happens when we raise the Fermi level into the bands. If we know the shape of the $E(\vec{k})$ curve, we are in a position to estimate the velocity of the electrons and also the so-called *effective mass* of the electrons. From the diagram in {numref}`fig-p1-ch01-2` we see that the conduction bands tend to fill up electron states starting at their energy extrema.

Since the energy bands have zero slope about their extrema, we can write $E(\vec{k})$ as a quadratic form in $\vec{k}$. It is convenient to write the proportionality in terms of the quantity called the effective mass $m^*$

```{math}
:label: eq-p1-ch01-36
E(\vec{k}) = E(0) + \frac{\hbar^2 k^2}{2m^*}
```

so that $m^*$ is defined by

```{math}
:label: eq-p1-ch01-37
\frac{1}{m^*} \equiv \frac{\partial^2 E(\vec{k})}{\hbar^2 \partial k^2}
```

and we can say in some approximate way that an electron in a solid moves as if it were a free electron but with an effective mass $m^*$ rather than a free electron mass. The larger the band curvature, the smaller the effective mass. The mean velocity of the electron is also found from $E(\vec{k})$, according to the relation

```{math}
:label: eq-p1-ch01-38
\vec{v}_k = \frac{1}{\hbar} \frac{\partial E(\vec{k})}{\partial \vec{k}} .
```

For this reason the energy dispersion relations $E(\vec{k})$ are very important in the determination of the transport properties for carriers in solids.

### 1.2.2 Tight Binding Approximation

In the tight binding approximation a number of assumptions are made and these are different from the assumptions that are made for the weak binding approximation. The assumptions for the tight binding approximation are:

1. The energy eigenvalues and eigenfunctions are known for an electron in an isolated atom.
2. When the atoms are brought together to form a solid they remain sufficiently far apart so that each electron can be assigned to a particular atomic site. This assumption is not valid for valence electrons in metals and for this reason, these valence electrons are best treated by the weak binding approximation.
3. The periodic potential is approximated by a superposition of atomic potentials.
4. Perturbation theory can be used to treat the difference between the actual potential and the atomic potential.

Thus both the weak and tight binding approximations are based on perturbation theory. For the weak binding approximation the unperturbed state is the free electron plane-wave state, while for the tight binding approximation, the unperturbed state is the atomic state. In the case of the weak binding approximation, the perturbation Hamiltonian is the weak periodic potential itself, while for the tight binding case, the perturbation is the *difference* between the periodic potential and the atomic potential around which the electron is localized.

We review here the major features of the tight binding approximation. Let $\phi(\vec{r}-\vec{R}_n)$ represent the atomic wave function for an atom at a lattice position denoted by $\vec{R}_n$, which is measured with respect to the origin. The Schrödinger equation for an electron in an isolated atom is then:

```{math}
:label: eq-p1-ch01-39
\left[ -\frac{\hbar^2}{2m} \nabla^2 + U(\vec{r}-\vec{R}_n) - E^{(0)} \right] \phi(\vec{r}-\vec{R}_n) = 0
```

where $U(\vec{r}-\vec{R}_n)$ is the atomic potential and $E^{(0)}$ is the atomic eigenvalue (see {numref}`fig-p1-ch01-3`). We now assume that the atoms are brought together to form the crystal for which $V(\vec{r})$ is the periodic potential, and $\psi(\vec{r})$ and $E(\vec{k})$ are, respectively, the wave function and energy eigenvalue for the electron in the crystal:

```{math}
:label: eq-p1-ch01-40
\left[ -\frac{\hbar^2}{2m} \nabla^2 + V(\vec{r}) - E \right] \psi(\vec{r}) = 0 .
```

:::{figure} images/fig-p1-ch01-3.png
:name: fig-p1-ch01-3
:width: 40%
:align: center
Fig. 1.3: Definition of the vectors used in the tight binding approximation.
:::

In the tight binding approximation we write $V(\vec{r})$ as a sum of atomic potentials:

```{math}
:label: eq-p1-ch01-41
V(\vec{r}) \simeq \sum_n U(\vec{r}-\vec{R}_n) .
```

If the interaction between neighboring atoms is ignored, then each state has a degeneracy of $N =$ number of atoms in the crystal. However, the interaction between the atoms lifts this degeneracy.

The energy eigenvalues $E(\vec{k})$ in the tight binding approximation for a non-degenerate $s$-state is simply given by

```{math}
:label: eq-p1-ch01-42
E(\vec{k}) = \frac{\langle \vec{k} \mid \mathcal{H} \mid \vec{k} \rangle}{\langle \vec{k} \mid \vec{k} \rangle} .
```

The normalization factor in the denominator $\langle \vec{k} \mid \vec{k} \rangle$ is inserted because the wave functions $\psi_{\vec{k}}(\vec{r})$ in the tight binding approximation are usually not normalized. The Hamiltonian in the tight binding approximation is written as

```{math}
:label: eq-p1-ch01-43
\mathcal{H} = -\frac{\hbar^2}{2m} \nabla^2 + V(\vec{r}) = \left\{ -\frac{\hbar^2}{2m} \nabla^2 + [V(\vec{r}) - U(\vec{r}-\vec{R}_n)] + U(\vec{r}-\vec{R}_n) \right\}
```

```{math}
:label: eq-p1-ch01-44
\mathcal{H} = \mathcal{H}_0 + \mathcal{H}'
```

in which $\mathcal{H}_0$ is the atomic Hamiltonian at site $n$

```{math}
:label: eq-p1-ch01-45
\mathcal{H}_0 = -\frac{\hbar^2}{2m} \nabla^2 + U(\vec{r}-\vec{R}_n)
```

and $\mathcal{H}'$ is the difference between the actual periodic potential and the atomic potential at lattice site $n$

```{math}
:label: eq-p1-ch01-46
\mathcal{H}' = V(\vec{r}) - U(\vec{r}-\vec{R}_n) .
```

We construct the wave functions for the unperturbed problem as a linear combination of atomic functions $\phi_j(\vec{r}-\vec{R}_n)$ labeled by quantum number $j$

```{math}
:label: eq-p1-ch01-47
\psi_j(\vec{r}) = \sum_{n=1}^{N} C_{j,n} \phi_j(\vec{r}-\vec{R}_n)
```

and so that $\psi_j(\vec{r})$ is an eigenstate of a Hamiltonian satisfying the periodic potential of the lattice. In this treatment we assume that the tight binding wave-functions $\psi_j$ can be identified with a *single* atomic state $\phi_j$; this approximation must be relaxed in dealing with degenerate levels. According to Bloch's theorem, $\psi_j(\vec{r})$ in the solid must satisfy the relation:

```{math}
:label: eq-p1-ch01-48
\psi_j(\vec{r}+\vec{R}_m) = e^{i\vec{k}\cdot\vec{R}_m} \psi_j(\vec{r})
```

where $\vec{R}_m$ is an arbitrary lattice vector. This restriction imposes a special form on the coefficients $C_{j,n}$.

Substitution of the expansion in atomic functions $\psi_j(\vec{r})$ from {eq}`eq-p1-ch01-47` into the left side of {eq}`eq-p1-ch01-48` yields:

```{math}
:label: eq-p1-ch01-49
\begin{aligned}
\psi_j(\vec{r}+\vec{R}_m) &= \sum_n C_{j,n} \, \phi_j(\vec{r}-\vec{R}_n+\vec{R}_m) \\
&= \sum_Q C_{j,Q+m} \, \phi_j(\vec{r}-\vec{R}_Q) \\
&= \sum_n C_{j,n+m} \, \phi_j(\vec{r}-\vec{R}_n)
\end{aligned}
```

where we have utilized the substitution $\vec{R}_Q = \vec{R}_n - \vec{R}_m$ and the fact that $Q$ is a dummy index. Now for the right side of the Bloch theorem ({eq}`eq-p1-ch01-48`) we have

```{math}
:label: eq-p1-ch01-50
e^{i\vec{k}\cdot\vec{R}_m} \psi_j(\vec{r}) = \sum_n C_{j,n} e^{i\vec{k}\cdot\vec{R}_m} \phi_j(\vec{r}-\vec{R}_n) .
```

The coefficients $C_{j,n}$ which relate the actual wave function $\psi_j(\vec{r})$ to the atomic functions $\phi_j(\vec{r}-\vec{R}_n)$ are therefore not arbitrary but must thus satisfy:

```{math}
:label: eq-p1-ch01-51
C_{j,n+m} = e^{i\vec{k}\cdot\vec{R}_m} C_{j,n}
```

which can be accomplished by setting:

```{math}
:label: eq-p1-ch01-52
C_{j,n} = \xi_j e^{i\vec{k}\cdot\vec{R}_n}
```

where the new coefficient $\xi_j$ is independent of $n$. We therefore obtain:

```{math}
:label: eq-p1-ch01-53
\psi_{j,\vec{k}}(\vec{r}) = \xi_j \sum_n e^{i\vec{k}\cdot\vec{R}_n} \phi_j(\vec{r}-\vec{R}_n)
```

where $j$ is an index labeling the particular atomic state of degeneracy $N$ and $\vec{k}$ is the quantum number for the translation operator and labels the Bloch state $\psi_{j,\vec{k}}(\vec{r})$.

:::{figure} images/fig-p1-ch01-4.png
:name: fig-p1-ch01-4
:width: 50%
:align: center
Fig. 1.4: The relation between atomic states and the broadening due to the presence of neighboring atoms. As the interatomic distance decreases (going to the right in the diagram), the level broadening increases so that a band of levels occurs at atomic separations characteristic of solids.
:::

For simplicity, we will limit the present discussion of the tight binding approximation to $s$-bands (non-degenerate atomic states) and therefore we can suppress the $j$ index on the wave functions. (The treatment for $p$-bands is similar to what we will do here, but more complicated because of the degeneracy of the atomic states.) To find matrix elements of the Hamiltonian we write

```{math}
:label: eq-p1-ch01-54
\langle \vec{k}' \mid \mathcal{H} \mid \vec{k} \rangle = |\xi|^2 \sum_{n,m} e^{i(\vec{k}\cdot\vec{R}_n - \vec{k}'\cdot\vec{R}_m)} \int_{\Omega} \phi^*(\vec{r}-\vec{R}_m) \mathcal{H} \phi(\vec{r}-\vec{R}_n) d^3r
```

in which the integration is carried out throughout the volume of the crystal. Since $\mathcal{H}$ is a function which is periodic in the lattice, the only significant distance (see {numref}`fig-p1-ch01-5`) is

```{math}
:label: eq-p1-ch01-55
(\vec{R}_n - \vec{R}_m) = \vec{\rho}_{nm} .
```

:::{figure} images/fig-p1-ch01-5.png
:name: fig-p1-ch01-5
:width: 40%
:align: center
Fig. 1.5: Definition of $\vec{\rho}_{nm}$ denoting the distance between atoms at $\vec{R}_m$ and $\vec{R}_n$.
:::

We then write the integral in {eq}`eq-p1-ch01-54` as:

```{math}
:label: eq-p1-ch01-56
\langle \vec{k}' \mid \mathcal{H} \mid \vec{k} \rangle = |\xi|^2 \sum_{\vec{R}_m} e^{i(\vec{k}-\vec{k}')\cdot\vec{R}_m} \sum_{\vec{\rho}_{nm}} e^{i\vec{k}\cdot\vec{\rho}_{nm}} \mathcal{H}_{mn}(\vec{\rho}_{nm})
```

where we have written the matrix element $\mathcal{H}_{mn}(\vec{\rho}_{nm})$ as

```{math}
:label: eq-p1-ch01-57
\mathcal{H}_{mn}(\vec{\rho}_{nm}) = \int_{\Omega} \phi^*(\vec{r}-\vec{R}_m) \mathcal{H} \phi(\vec{r}-\vec{R}_m-\vec{\rho}_{nm}) d^3r = \int_{\Omega} \phi^*(\vec{r}') \mathcal{H} \phi(\vec{r}'-\vec{\rho}_{nm}) d^3r' .
```

We note here that the integral in {eq}`eq-p1-ch01-57` depends only on $\vec{\rho}_{nm}$ and not on $\vec{R}_m$. According to {eq}`eq-p1-ch01-13`, the first sum in {eq}`eq-p1-ch01-56` is

```{math}
:label: eq-p1-ch01-58
\sum_{\vec{R}_m} e^{i(\vec{k}-\vec{k}')\cdot\vec{R}_m} = \delta_{\vec{k}',\vec{k}+\vec{G}} N
```

where $\vec{G}$ is a reciprocal lattice vector. It is convenient to restrict the $\vec{k}$ vectors to lie within the first Brillouin zone (i.e., we limit ourselves to reduced wave vectors). This is consistent with the manner of counting states for a crystal with periodic boundary conditions of length $d$ on a side

```{math}
:label: eq-p1-ch01-59
k_i d = 2\pi m_i \qquad \text{for each direction } i
```

where $m_i$ is an integer in the range $1 \le m_i < N_i$ where $N_i \approx N^{1/3}$ and $N$ is the total number of unit cells in the crystal. From {eq}`eq-p1-ch01-59` we have

```{math}
:label: eq-p1-ch01-60
k_i = \frac{2\pi m_i}{d} .
```

The maximum value that a particular $m_i$ can assume is $N_i$ and the maximum value for $k_i$ is $2\pi/a$ at the Brillouin zone boundary since $N_i/d = 1/a$. With this restriction, $\vec{k}$ and $\vec{k}'$ must both lie within the $1^{st}$ B.Z. and thus cannot differ by any reciprocal lattice vector other than $\vec{G} = 0$. We thus obtain the following form for the matrix element of $\mathcal{H}$ (and also the corresponding forms for the matrix elements of $\mathcal{H}_0$ and $\mathcal{H}'$):

```{math}
:label: eq-p1-ch01-61
\langle \vec{k}' \mid \mathcal{H} \mid \vec{k} \rangle = |\xi|^2 N \delta_{\vec{k},\vec{k}'} \sum_{\vec{\rho}_{nm}} e^{i\vec{k}\cdot\vec{\rho}_{nm}} \mathcal{H}_{mn}(\vec{\rho}_{nm})
```

yielding the result

```{math}
:label: eq-p1-ch01-62
E(\vec{k}) = \frac{\langle \vec{k} \mid \mathcal{H} \mid \vec{k} \rangle}{\langle \vec{k} \mid \vec{k} \rangle} = \frac{\sum_{\vec{\rho}_{nm}} e^{i\vec{k}\cdot\vec{\rho}_{nm}} \mathcal{H}_{mn}(\vec{\rho}_{nm})}{\sum_{\vec{\rho}_{nm}} e^{i\vec{k}\cdot\vec{\rho}_{nm}} \mathcal{S}_{mn}(\vec{\rho}_{nm})}
```

in which

```{math}
:label: eq-p1-ch01-63
\langle \vec{k}' \mid \vec{k} \rangle = |\xi|^2 \delta_{\vec{k},\vec{k}'} N \sum_{\vec{\rho}_{nm}} e^{i\vec{k}\cdot\vec{\rho}_{nm}} \mathcal{S}_{mn}(\vec{\rho}_{nm})
```

where the matrix element $\mathcal{S}_{mn}(\vec{\rho}_{nm})$ measures the overlap of atomic functions on different sites

```{math}
:label: eq-p1-ch01-64
\mathcal{S}_{mn}(\vec{\rho}_{nm}) = \int_{\Omega} \phi^*(\vec{r}) \phi(\vec{r}-\vec{\rho}_{nm}) d^3r .
```

The overlap integral $\mathcal{S}_{mn}(\vec{\rho}_{nm})$ will be nearly 1 when $\vec{\rho}_{nm} = 0$ and will fall off rapidly as $\vec{\rho}_{nm}$ increases, which exemplifies the spirit of the tight binding approximation. By selecting $\vec{k}$ vectors to lie within the first Brillouin zone, the orthogonality condition on the wave function $\psi_{\vec{k}}(\vec{r})$ is automatically satisfied. Writing $\mathcal{H} = \mathcal{H}_0 + \mathcal{H}'$ yields:

```{math}
:label: eq-p1-ch01-65
\begin{aligned}
\mathcal{H}_{mn} &= \int_{\Omega} \phi^*(\vec{r}-\vec{R}_m) \left[ -\frac{\hbar^2}{2m} \nabla^2 + U(\vec{r}-\vec{R}_n) \right] \phi(\vec{r}-\vec{R}_n) d^3r \\
&\quad + \int_{\Omega} \phi^*(\vec{r}-\vec{R}_m) [V(\vec{r}) - U(\vec{r}-\vec{R}_n)] \phi(\vec{r}-\vec{R}_n) d^3r
\end{aligned}
```

or

```{math}
:label: eq-p1-ch01-66
\mathcal{H}_{mn} = E^{(0)} \mathcal{S}_{mn}(\vec{\rho}_{nm}) + \mathcal{H}'_{mn}(\vec{\rho}_{nm})
```

which results in the general expression for the tight binding approximation:

```{math}
:label: eq-p1-ch01-67
E(\vec{k}) = E^{(0)} + \frac{\sum_{\vec{\rho}_{nm}} e^{i\vec{k}\cdot\vec{\rho}_{nm}} \mathcal{H}'_{mn}(\vec{\rho}_{nm})}{\sum_{\vec{\rho}_{nm}} e^{i\vec{k}\cdot\vec{\rho}_{nm}} \mathcal{S}_{mn}(\vec{\rho}_{nm})} .
```

In the spirit of the tight binding approximation, the second term in {eq}`eq-p1-ch01-67` is assumed to be small, which is a good approximation if the overlap of the atomic wave functions is small. We classify the sum over $\vec{\rho}_{nm}$ according to the distance between site $m$ and site $n$: (i) zero distance, (ii) the nearest neighbor distance, (iii) the next nearest neighbor distance, etc.

```{math}
:label: eq-p1-ch01-68
\sum_{\vec{\rho}_{nm}} e^{i\vec{k}\cdot\vec{\rho}_{nm}} \mathcal{H}'_{mn}(\vec{\rho}_{nm}) = \mathcal{H}'_{nn}(0) + \sum_{\vec{\rho}_1} e^{i\vec{k}\cdot\vec{\rho}_1} \mathcal{H}'_{mn}(\vec{\rho}_{nm}) + \ldots
```

The zero$^{th}$ neighbor term $\mathcal{H}'_{nn}(0)$ in {eq}`eq-p1-ch01-68` results in a constant additive energy, independent of $\vec{k}$. The sum over nearest neighbor distances $\vec{\rho}_1$ gives rise to a $\vec{k}$-dependent perturbation, and hence is of particular interest in calculating the band structure. The terms $\mathcal{H}'_{nn}(0)$ and the sum over the nearest neighbor terms in {eq}`eq-p1-ch01-68` are of comparable magnitude, as can be seen by the following argument. In the integral

```{math}
:label: eq-p1-ch01-69
\mathcal{H}'_{nn}(0) = \int \phi^*(\vec{r}-\vec{R}_n) [V - U(\vec{r}-\vec{R}_n)] \phi(\vec{r}-\vec{R}_n) d^3r
```

we note that $|\phi(\vec{r}-\vec{R}_n)|^2$ has an appreciable amplitude only in the vicinity of the site $\vec{R}_n$. But at site $\vec{R}_n$, the potential energy term $[V - U(\vec{r}-\vec{R}_n)] = \mathcal{H}'$ is a small term, so that $\mathcal{H}'_{nn}(0)$ represents the product of a small term times a large term. On the other hand, the integral $\mathcal{H}'_{mn}(\vec{\rho}_{nm})$ taken over nearest neighbor distances has a factor $[V - U(\vec{r}-\vec{R}_n)]$ which is large near the $m^{th}$ site; however, in this case the wave functions $\phi^*(\vec{r}-\vec{R}_m)$ and $\phi(\vec{r}-\vec{R}_n)$ are on different atomic sites and have only a small overlap on nearest neighbor sites. Therefore $\mathcal{H}'_{mn}(\vec{\rho}_{nm})$ over nearest neighbor sites also results in the product of a large quantity times a small quantity.

In treating the denominator in the perturbation term of {eq}`eq-p1-ch01-67`, we must sum

```{math}
:label: eq-p1-ch01-70
\sum_{\vec{\rho}_{nm}} e^{i\vec{k}\cdot\vec{\rho}_{nm}} \mathcal{S}_{mn}(\vec{\rho}_{nm}) = \mathcal{S}_{nn}(0) + \sum_{\vec{\rho}_1} e^{i\vec{k}\cdot\vec{\rho}_1} \mathcal{S}_{mn}(\vec{\rho}_{nm}) + \ldots
```

In this case the leading term $\mathcal{S}_{nn}(0)$ is approximately unity and the overlap integral $\mathcal{S}_{mn}(\vec{\rho}_{nm})$ over nearest neighbor sites is small, and can be neglected to lowest order in comparison with unity. The nearest neighbor term in {eq}`eq-p1-ch01-70` is of comparable relative magnitude to the next nearest neighbor terms arising from $\mathcal{H}_{mn}(\vec{\rho}_{nm})$ in {eq}`eq-p1-ch01-68`.

We will here make *several explicit evaluations* of $E(\vec{k})$ in the tight-binding limit to show how this method incorporates the crystal symmetry. For illustrative purposes we will give results for the simple cubic lattice (SC), the body centered cubic (BCC) and face centered cubic lattice (FCC). We shall assume here that the overlap of atomic potentials on neighboring sites is sufficiently weak so that only nearest neighbor terms need be considered in the sum on $\mathcal{H}'_{mn}$ and only the leading term need be considered in the sum of $\mathcal{S}_{mn}$.

For the simple cubic structure there are 6 terms in the nearest neighbor sum on $\mathcal{H}'_{mn}$ in {eq}`eq-p1-ch01-67` with $\vec{\rho}_1$ vectors given by:

```{math}
:label: eq-p1-ch01-71
\vec{\rho}_1 = a(\pm 1,0,0), \; a(0,\pm 1,0), \; a(0,0,\pm 1) .
```

By symmetry, $\mathcal{H}'_{mn}(\vec{\rho}_1)$ is the same for all of the $\vec{\rho}_1$ vectors so that

```{math}
:label: eq-p1-ch01-72
E(\vec{k}) = E^{(0)} + \mathcal{H}'_{nn}(0) + 2\mathcal{H}'_{mn}(\vec{\rho}_1)[\cos k_x a + \cos k_y a + \cos k_z a] + \ldots
```

where $\vec{\rho}_1 =$ the nearest neighbor separation and $k_x$, $k_y$, $k_z$ are components of the wave vector $\vec{k}$ in the first Brillouin zone.

:::{figure} images/fig-p1-ch01-6.png
:name: fig-p1-ch01-6
:width: 50%
:align: center
Fig. 1.6: The relation between the atomic levels and the broadened level in the tight binding approximation.
:::

This dispersion relation $E(\vec{k})$ clearly satisfies three properties which characterize the energy eigenvalues in typical periodic structures:

1. Periodicity in $\vec{k}$ space under translation by a reciprocal lattice vector $\vec{k} \to \vec{k} + \vec{G}$,
2. $E(\vec{k})$ is an even function of $\vec{k}$ (i.e., $E(k) = E(-k)$)
3. $\partial E / \partial k = 0$ at the Brillouin zone boundary

In the above expression ({eq}`eq-p1-ch01-72`) for $E(\vec{k})$, the maximum value for the term in brackets is $\pm 3$. Therefore for a simple cubic lattice in the tight binding approximation we obtain a bandwidth of $12 \, \mathcal{H}'_{mn}(\rho_1)$ from nearest neighbor interactions as shown in {numref}`fig-p1-ch01-6`.

Because of the different locations of the nearest neighbor atoms in the case of the BCC and FCC lattices, the expression for $E(\vec{k})$ will be different for the various cubic lattices. Thus the form of the tight binding approximation explicitly takes account of the crystal structure. The results for the simple cubic, body centered cubic and face centered cubic lattices are summarized below.

**simple cubic**

```{math}
:label: eq-p1-ch01-73
E(\vec{k}) = \text{const} + 2\mathcal{H}'_{mn}(\vec{\rho}_1)[\cos k_x a + \cos k_y a + \cos k_z a]
```

**body centered cubic**

The eight $\vec{\rho}_1$ vectors for the nearest neighbor distances in the BCC structure are $(\pm a/2, \pm a/2, \pm a/2)$ so that there are 8 exponential terms which combine in pairs such as:

```{math}
:label: eq-p1-ch01-74
\left[ \exp\frac{ik_x a}{2} \exp\frac{ik_y a}{2} \exp\frac{ik_z a}{2} + \exp\frac{-ik_x a}{2} \exp\frac{ik_y a}{2} \exp\frac{ik_z a}{2} \right]
```

to yield

```{math}
:label: eq-p1-ch01-75
2\cos\left(\frac{k_x a}{2}\right) \exp\frac{ik_y a}{2} \exp\frac{ik_z a}{2} .
```

We thus obtain for the BCC structure:

```{math}
:label: eq-p1-ch01-76
E(\vec{k}) = \text{const} + 8\mathcal{H}'_{mn}(\vec{\rho}_1) \cos\left(\frac{k_x a}{2}\right) \cos\left(\frac{k_y a}{2}\right) \cos\left(\frac{k_z a}{2}\right) + \ldots
```

where $\mathcal{H}'_{mn}(\vec{\rho}_1)$ is the matrix element of the perturbation Hamiltonian taken between nearest neighbor atomic orbitals.

**face centered cubic**

For the FCC structure there are 12 nearest neighbor distances $\vec{\rho}_1$: $(0, \pm a/2, \pm a/2)$, $(\pm a/2, \pm a/2, 0)$, $(\pm a/2, 0, \pm a/2)$, so that the twelve exponential terms combine in groups of 4 to yield:

```{math}
:label: eq-p1-ch01-77
\exp\frac{ik_x a}{2} \exp\frac{ik_y a}{2} + \exp\frac{ik_x a}{2} \exp\frac{-ik_y a}{2} + \exp\frac{-ik_x a}{2} \exp\frac{ik_y a}{2} + \exp\frac{-ik_x a}{2} \exp\frac{-ik_y a}{2} = 4\cos\left(\frac{k_x a}{2}\right) \cos\left(\frac{k_y a}{2}\right) ,
```

thus resulting in the energy dispersion relation

```{math}
:label: eq-p1-ch01-78
E(\vec{k}) = \text{const} + 4\mathcal{H}'_{mn}(\vec{\rho}_1) \left[ \cos\left(\frac{k_y a}{2}\right)\cos\left(\frac{k_z a}{2}\right) + \cos\left(\frac{k_x a}{2}\right)\cos\left(\frac{k_z a}{2}\right) + \cos\left(\frac{k_x a}{2}\right)\cos\left(\frac{k_y a}{2}\right) \right] + \ldots
```

We note that $E(\vec{k})$ for the FCC is different from that for the SC or BCC structures. The tight-binding approximation has symmetry considerations built into its formulation through the symmetrical arrangement of the atoms in the lattice. The situation is quite different in the weak binding approximation where symmetry enters into the form of $V(\vec{r})$ and determines which Fourier components $V_{\vec{G}}$ will be important in creating band gaps.

```{math}
:label: eq-p1-ch01-79
V_{\vec{G}} = \frac{1}{\Omega_0} \int_{\Omega_0} e^{-i\vec{G}\cdot\vec{r}} V(\vec{r}) d^3r .
```

From the point of view of the tight-binding approximation, the increasing bandwidth with increasing energy (see {numref}`fig-p1-ch01-7`) is also equivalent to a decrease in the forbidden band gap. At the same time, the atomic states at higher energies become more closely spaced, so that the increased bandwidth eventually results in band overlaps. When band overlaps occur, the tight-binding approximation as given above must be generalized to treat coupled or interacting bands using degenerate perturbation theory (see Appendix A).

:::{figure} images/fig-p1-ch01-7.png
:name: fig-p1-ch01-7
:width: 70%
:align: center
Fig. 1.7: Schematic diagram of (a) the quantized energy levels and (b) the increased bandwidth and decreased band gap in the tight binding approximation as the interatomic separation decreases.
:::

### 1.2.3 Weak and Tight Binding Approximations

We will now make some general statements about bandwidths and forbidden band gaps which follow from either the tight binding or weak binding (nearly free electron) approximations. With increasing energy, the bandwidth tends to increase. On the tight-binding picture, the higher energy atomic states are less closely bound to the nucleus, and the resulting increased overlap of the wave functions results in a larger value for $\mathcal{H}'_{mn}(\vec{\rho}_1)$ in the case of the higher atomic states: that is, for silicon, which has 4 valence electrons in the $n=3$ shell, the overlap integral $\mathcal{H}'_{mn}(\vec{\rho}_1)$ will be smaller than for germanium which is isoelectronic to silicon but has instead 4 valence electrons in the $n=4$ atomic shell. On the weak-binding picture, the same result follows, since for higher energies, the electrons are more nearly free; therefore, there are more allowed energy ranges available, or equivalently, the energy range of the forbidden states is smaller. Also in the weak-binding approximation the band gap of $2|V_{\vec{G}}|$ tends to decrease as $\vec{G}$ increases, because of the oscillatory character of $e^{-i\vec{G}\cdot\vec{r}}$ in {eq}`eq-p1-ch01-79`.

### 1.2.4 Tight Binding Approximation with 2 Atoms/Unit Cell

We present here a simple example of the tight binding approximation for a simplified version of polyacetylene which has two carbon atoms (with their appended hydrogens) per unit cell. In {numref}`fig-p1-ch01-8` we show, within the box defined by the dotted lines, the unit cell for *trans*-polyacetylene $(\mathrm{CH})_x$. This unit cell of an infinite one-dimensional chain contains two inequivalent carbon atoms, A and B. There is one $\pi$-electron per carbon atom, thus giving rise to two $\pi$-energy bands in the first Brillouin zone. These two bands are called bonding $\pi$-bands for the valence band, and anti-bonding $\pi$-bands for the conduction band.

:::{figure} images/fig-p1-ch01-8.png
:name: fig-p1-ch01-8
:width: 50%
:align: center
Fig. 1.8: The unit cell of *trans*-polyacetylene bounded by a box defined by the dotted lines, and showing two inequivalent carbon atoms, A and B, in the unit cell.
:::

The lattice unit vector and the reciprocal lattice unit vector of this one-dimensional polyacetylene chain are given by $\vec{a}_1 = (a,0,0)$ and $\vec{b}_1 = (2\pi/a,0,0)$, respectively. The Brillouin zone in 1D is the line segment $-\pi/a < k < \pi/a$ and the Brillouin zone boundary is at $k = \pm \pi/a$. The Bloch orbitals consisting of A and B atoms are given by

```{math}
:label: eq-p1-ch01-80
\psi_j(r) = \frac{1}{\sqrt{N}} \sum_{R_\alpha} e^{ikR_\alpha} \phi_j(r - R_\alpha), \quad (\alpha = \mathrm{A},\mathrm{B})
```

where the summation is taken over the atom site coordinate $R_\alpha$ for the A or B carbon atoms in the solid.

To solve for the energy eigenvalues and wavefunctions we need to solve the general equation:

```{math}
:label: eq-p1-ch01-81
\mathcal{H}\psi = E\mathcal{S}\psi
```

where $\mathcal{H}$ is the $n \times n$ tight binding matrix Hamiltonian for the $n$ coupled bands ($n=2$ in the case of polyacetylene) and $\mathcal{S}$ is the corresponding $n \times n$ overlap integral matrix. To obtain a solution to this matrix equation, we require that the determinant $|\mathcal{H} - E\mathcal{S}|$ vanish.

This approach is easily generalized to periodic structures with more than 2 atoms per unit cell.

The $(2 \times 2)$ matrix Hamiltonian, $\mathcal{H}_{\alpha\beta}$, $(\alpha,\beta = A,B)$ is obtained by substituting {eq}`eq-p1-ch01-80` into

```{math}
:label: eq-p1-ch01-82
\mathcal{H}_{jj'}(\vec{k}) = \langle \psi_j \mid \mathcal{H} \mid \psi_{j'} \rangle, \quad \mathcal{S}_{jj'}(\vec{k}) = \langle \psi_j \mid \psi_{j'} \rangle \qquad (j,j' = 1,2),
```

where the integrals over the Bloch orbitals, $\mathcal{H}_{jj'}(\vec{k})$ and $\mathcal{S}_{jj'}(\vec{k})$, are called transfer integral matrices and overlap integral matrices, respectively. When $\alpha = \beta =$ A, we obtain the diagonal matrix element

```{math}
:label: eq-p1-ch01-83
\begin{aligned}
\mathcal{H}_{AA}(r) &= \frac{1}{N} \sum_{R,R'} e^{ik(R-R')} \langle \phi_A(r-R') \mid \mathcal{H} \mid \phi_A(r-R) \rangle \\
&= \frac{1}{N} \sum_{R'=R} E_{2p} + \frac{1}{N} \sum_{R'=R\pm a} e^{\pm ika} \langle \phi_A(r-R') \mid \mathcal{H} \mid \phi_A(r-R) \rangle \\
&\quad + (\text{terms equal to or more distant than } R' = R \pm 2a) \\
&= E_{2p} + (\text{terms equal to or more distant than } R' = R \pm a) .
\end{aligned}
```

In {eq}`eq-p1-ch01-83` the main contribution to the matrix element $\mathcal{H}_{AA}$ comes from $R' = R$, and this gives the orbital energy of the $2p$ level, $E_{2p}$. We note that $E_{2p}$ is not simply the atomic energy value for the free atom, because the Hamiltonian $\mathcal{H}$ also includes a crystal potential contribution. The next order contribution to $\mathcal{H}_{AA}$ in {eq}`eq-p1-ch01-83` comes from terms in $R' = R \pm a$, which are here neglected for simplicity. Similarly, $\mathcal{H}_{BB}$ also gives $E_{2p}$ to the same order of approximation.

Next let us consider the off-diagonal matrix element $\mathcal{H}_{AB}(r)$ which explicitly couples the A unit to the B unit. The largest contribution to $\mathcal{H}_{AB}(r)$ arises when atoms A and B are nearest neighbors. Thus in the summation over $R'$, we only consider the terms with $R' = R \pm a/2$ as a first approximation and neglect more distant terms to obtain

```{math}
:label: eq-p1-ch01-84
\begin{aligned}
\mathcal{H}_{AB}(r) &= \frac{1}{N} \sum_R \left\{ e^{-ika/2} \langle \phi_A(r-R) \mid \mathcal{H} \mid \phi_B(r-R-a/2) \rangle \right. \\
&\quad \left. + e^{ika/2} \langle \phi_A(r-R) \mid \mathcal{H} \mid \phi_B(r-R+a/2) \rangle \right\} \\
&= 2t \cos(ka/2)
\end{aligned}
```

where $t$ is the transfer integral appearing in {eq}`eq-p1-ch01-84` and is denoted by

```{math}
:label: eq-p1-ch01-85
t = \langle \phi_A(r-R) \mid \mathcal{H} \mid \phi_B(r-R \pm a/2) \rangle .
```

Here we have assumed that all the $\pi$ bonding orbitals are of equal length (1.5 Å bonds). In the real $(\mathrm{CH})_x$ compound, bond alternation occurs, in which the bonding alternates between adjacent carbon atoms alternates between single bonds (1.7 Å) and double bonds (1.3 Å). With this bond alternation, the two matrix elements between atomic wavefunctions in {eq}`eq-p1-ch01-84` are not equal. Although the distortion of the lattice lowers the total energy, the electronic energy always decreases more than the lattice energy in a one-dimensional material. This distortion deforms the lattice by a process called the Peierls instability. This instability arises for example when a distortion is introduced into a system containing a previously degenerate system with 2 equivalent atoms per unit cell. The distortion making the atoms inequivalent increases the unit cell by a factor of 2 and decreases the reciprocal lattice by a factor of 2. If the energy band was formally half filled, a band gap is introduced by the Peierls instability at the Fermi level, which lowers the total energy of the system. It is stressed here that $t$ has a negative value which means that $t$ is an attractive potential that bonds atoms together to form a condensed state of matter. The matrix element $\mathcal{H}_{BA}(r)$ is obtained from $\mathcal{H}_{AB}(r)$ through the Hermitian conjugation relation $\mathcal{H}_{BA} = \mathcal{H}_{AB}^*$, but since $\mathcal{H}_{AB}$ is real in this case, we obtain $\mathcal{H}_{BA} = \mathcal{H}_{AB}$.

The overlap matrix $\mathcal{S}_{ij}$ can be calculated by a similar method as was used for $\mathcal{H}_{ij}$, except that the intra-atomic integral $\mathcal{S}_{ij}$ yields a unit matrix in the limit of large interatomic distances, if we assume that the atomic wavefunction is normalized so that $\mathcal{S}_{AA} = \mathcal{S}_{BB} = 1$. It is assumed that for polyacetylene, the $\mathcal{S}_{AA}$ and $\mathcal{S}_{BB}$ matrix elements are still approximately unity. For the off-diagonal matrix element for polyacetylene we have $\mathcal{S}_{AB} = \mathcal{S}_{BA} = 2s \cos(ka/2)$, where $s$ is an overlap integral between the nearest A and B atoms,

```{math}
:label: eq-p1-ch01-86
s = \langle \phi_A(r-R) \mid \phi_B(r-R \pm a/2) \rangle .
```

The secular equation for the $2p_z$ orbital of CH$_x$ is obtained by setting the determinant of $|\mathcal{H} - E\mathcal{S}|$ to zero to obtain

```{math}
:label: eq-p1-ch01-87
\begin{vmatrix}
E_{2p} - E & 2(t - sE)\cos(ka/2) \\
2(t - sE)\cos(ka/2) & E_{2p} - E
\end{vmatrix} = 0
```

or

```{math}
:label: eq-p1-ch01-88
(E_{2p} - E)^2 - 4(t - sE)^2 \cos^2(ka/2) = 0
```

yielding the eigenvalues of the energy dispersion relations of {eq}`eq-p1-ch01-87`

```{math}
:label: eq-p1-ch01-89
E_{\pm}(\vec{k}) = \frac{E_{2p} \pm 2t \cos(ka/2)}{1 \pm 2s \cos(ka/2)}, \quad \left(-\frac{\pi}{a} < k < \frac{\pi}{a}\right)
```

in which the $+$ sign is associated with the bonding $\pi$-band and the $-$ sign is associated with the antibonding $\pi^*$-band, as shown in {numref}`fig-p1-ch01-9`. Here it is noted that by setting $E_{2p}$ to zero (thereby defining the origin of the energy), the levels $E_{+}$ and $E_{-}$ are degenerate at $ka = \pm \pi$. {numref}`fig-p1-ch01-9` is constructed for $t < 0$ and $s > 0$. Since there are two $\pi$ electrons per unit cell, each with a different spin orientation, both electrons occupy the bonding $\pi$ energy band. The effect of the inter-atomic bonding is to lower the total energy below $E_{2p}$.

:::{figure} images/fig-p1-ch01-9.png
:name: fig-p1-ch01-9
:width: 70%
:align: center
Fig. 1.9: The energy dispersion relation $E_{\pm}(\vec{k})$ for polyacetylene $[(\mathrm{CH})_x]$, given by {eq}`eq-p1-ch01-89` with values for the parameters $t = -1$ and $s = 0.2$. Curves $E_{+}(\vec{k})$ and $E_{-}(\vec{k})$ are called bonding $\pi$ and antibonding $\pi^*$ energy bands, respectively, and the energy is plotted in units of $t$.
:::

## 1.3 Summary

- In the weak binding approximation a weak periodic potential is treated by perturbation theory. The nearly free electron bands develop energy gaps of magnitude $2|V_{\vec{G}}|$ at the Brillouin zone boundaries ({eq}`eq-p1-ch01-25`–{eq}`eq-p1-ch01-32`).
- In the tight binding approximation the electron states are built from atomic orbitals, and the resulting band structure explicitly reflects the crystal symmetry of the lattice ({eq}`eq-p1-ch01-72`–{eq}`eq-p1-ch01-78`).
- The effective mass $m^*$ and the group velocity $\vec{v}_k$ are obtained directly from the curvature and gradient of $E(\vec{k})$ ({eq}`eq-p1-ch01-37` and {eq}`eq-p1-ch01-38`).
- For a unit cell containing two inequivalent atoms the dispersion relation splits into two coupled bands; for polyacetylene the two bands are separated by a Peierls gap at the Fermi level ({eq}`eq-p1-ch01-89`).
