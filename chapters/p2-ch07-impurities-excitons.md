---
title: "7 Impurities and Excitons"
abstract: "The optical spectra of impurities (donors, acceptors, deep levels, vacancies and color centers) are described within the effective-mass and central-cell-correction pictures. Excitons are then treated as hydrogenic electron–hole pairs; their classification (direct, indirect, free, bound, Wannier, Frenkel, molecular, and electron–hole drops) and their enhanced effects in quantum-well structures (including the quantum-confined Stark effect) are discussed."
---

# 7 Impurities and Excitons

## 7.0 Overview

The introduction of impurities or defects into a crystal perturbs the periodic potential and gives rise to bound states that often lie within the band gap. These impurity levels produce well-defined optical spectra and are classified as shallow (hydrogenic) or deep. Related localized defects include vacancies, interstitials, and Frenkel and Schottky point defects. When an electron and a hole are bound to one another by their Coulomb interaction, the resulting excitation is an exciton; excitons are treated in direct analogy with the hydrogenic impurity problem but using the reduced effective mass. The various kinds of excitons and excitonic complexes, and the particularly strong exciton effects that occur in low-dimensional quantum-well structures, are described.

## 7.1 Impurity Level Spectroscopy

References

- Yu and Cardona, *Fundamentals of Semiconductors*, Springer Verlag (1996). §6.3 and §6.6.
- Bassani and Pastori–Parravicini, *Electronic States and Optical Transitions in Solids*: chapter 6 and 7.

Selected impurities are frequently introduced into semiconductors to make them n-type or p-type. The introduction of impurities into a crystal lattice not only shifts the Fermi level, but also results in a perturbation to the periodic potential, giving rise to bound impurity levels which often occur in the band gap of the semiconductor.

Impurities and defects in semiconductors can be classified according to whether they result in a minor or major perturbation to the periodic potential. Any disturbance to the periodic potential results in energy levels differing from the energy levels of the perfect crystal. However, when these levels occur within the energy band gap of a semiconductor or of an insulator, they are most readily identified, and these are the levels which give rise to well-defined optical spectra. Impurity levels are classified into two categories:

1. shallow levels,
2. deep levels,

corresponding, respectively, to a minor or a major perturbation of the periodic potential. Impurities are also classified according to whether they give rise to electron carriers (donors) or hole carriers (acceptors). We will now discuss the optical spectra for impurities.

## 7.2 Shallow Impurity Levels

An example of a shallow impurity level in a semiconductor is a hydrogenic donor level in a semiconductor like Si, Ge or the III-V compounds. Let us briefly review the origin of shallow donor levels in n-type semiconductors, where conduction is predominantly by electron carriers.

Suppose we add donor impurities such as arsenic, which has 5 valence electrons, to germanium which has 4 valence electrons (see Part I, Fig. 4.1). Each germanium atom in the perfect crystal makes 4 bonds to its tetrahedrally placed neighbors. For the arsenic impurity in the germanium lattice, four of the valence electrons will participate in the tetrahedral bonding to the germanium neighbors, but the fifth electron will be attracted back to the arsenic impurity site because the arsenic ion on the site has a positive charge. Within the effective mass approximation, this interaction is described by the Coulomb perturbation Hamiltonian,

```{math}
:label: eq-p2-ch07-1
\mathcal{H}'(r) = -\frac{e^2}{\varepsilon_0 r} ,
```

where $\varepsilon_0$ is the static dielectric constant which is 16 for germanium and 12 for silicon. This Coulomb interaction is a screened Coulomb potential, screened by the static dielectric constant. The approximation of taking $\varepsilon_0$ to be independent of distance is however not valid for values of $r$ comparable to lattice dimensions, as discussed below.

In simple terms, $\mathcal{H}'$ given by Eq. {eq}`eq-p2-ch07-1` is the same as in the hydrogen atom except that the charge is now $e/\sqrt{\varepsilon_0}$ and the mass which enters the kinetic energy is the effective mass $m^*$ of the charge carriers. Since the levels in the hydrogen atom are given by the Bohr energy levels

```{math}
:label: eq-p2-ch07-2
E_n^{\text{hydrogen}} = -\frac{m_0 e^4}{2\hbar^2 n^2} ,
```

then the energy levels in the hydrogenic impurity problem are to a first approximation given by hydrogenic levels

```{math}
:label: eq-p2-ch07-3
E_n^{\text{impurity}} = -\frac{m^* e^4}{2\hbar^2\varepsilon_0^2 n^2} .
```

The impurity levels are shown schematically in Fig. {numref}`fig-p2-ch07-1`, where the donor levels are seen to lie in the gap below the conduction band minimum.

:::{figure} images/fig-p2-ch07-1.png
:name: fig-p2-ch07-1
:width: 55%
:align: center
Fig. 7.1: Hydrogenic impurity levels in a semiconductor.
:::

For the hydrogen atom $E_1^{\text{hydrogen}} = -13.6\ \text{eV}$, but for germanium $E_1^{\text{impurity}} \sim 6\times 10^{-3}\ \text{eV}$ where we have used a value of $m^* = 0.12\,m_0$ representing an average of the effective mass over the entire conduction band pocket. From measurements such as the optical absorption spectra we find that the thermal energy gap (which is the energy difference between the $L$ point lowest conduction band and the $\Gamma$ point highest valence band) is 0.66 eV at room temperature. But the donor level manifold is only $6\times 10^{-3}\ \text{eV}$ wide (ranging from the $E_1$ level to the ionization limit) so that these impurity levels are very close to the bottom of the conduction band.

Another quantity of interest in this connection is the "orbital radius" of the impurity. Unless the orbital radius is greater than a few lattice dimensions, it is not meaningful to use a dielectric constant independent of $\mathbf{r}$ in constructing the perturbation Hamiltonian, since the dielectric constant used there is conceptually meaningful only for a continuum. Therefore, it is of interest to calculate the hydrogen Bohr radius using the usual recipe for the hydrogen atom

```{math}
:label: eq-p2-ch07-4
r_n^{\text{hydrogen}} = \frac{n^2\hbar^2}{m_0 e^2} ,
```

where $\hbar = 1.054\times 10^{-27}\ \text{erg/sec}$, the mass of the free electron is $m_0 = 9.1\times 10^{-28}\ \text{g}$, and the charge on the electron is $e = 4.8\times 10^{-10}\ \text{esu}$. The value for the Bohr radius in the hydrogen atom is $r_1^{\text{hydrogen}} = 0.5\ \text{\AA}$ and for the screened hydrogenic states in the impurity problem, we have

```{math}
:label: eq-p2-ch07-5
r_n^{\text{impurity}} = \frac{n^2\hbar^2\varepsilon_0}{m^* e^2} ,
```

which is larger than the hydrogen Bohr radius by a factor $\varepsilon_0 m_0/m^*$. Using typical numbers for germanium we get the ground state radius $r_1^{\text{impurity}} \sim 70\ \text{\AA}$. Thus, the electron travels over many lattice sites in germanium and the dielectric constant approximation used in Eq. {eq}`eq-p2-ch07-1` is valid.

From this discussion we see that only a very small energy is needed to ionize a bound donor electron into the conduction band, and because this binding energy is small, these hydrogenic donor levels are called shallow impurity levels. Since $r_n^{\text{impurity}} \gg a$ where $a$ is the lattice constant, these electrons are well localized in momentum space according to the uncertainty principle. Shallow donor levels are associated with the $\mathbf{k}$-point where the conduction band minima occur.

Thus the simple hydrogenic view of impurity levels in a semiconductor predicts that the impurity spectrum should only depend on the host material and on the charge difference between the host and impurity. To see how well this model works, let us look at the experimental results summarized in Fig. {numref}`fig-p2-ch07-2`. This picture is for silicon where the Bohr radius is $\approx 20\ \text{\AA}$. Here the agreement with the hydrogenic type model is good except for the ground state, where the dielectric constant approximation is not as valid as for germanium. The actual calculation referred to in this picture is solved for the case where the effective mass tensor components are included in the calculation. Such a calculation cannot be done exactly for an ellipsoidal constant energy surface

```{math}
:label: eq-p2-ch07-6
\left[-\frac{\hbar^2}{2}\left(\frac{1}{m_l}\frac{\partial^2}{\partial x^2} + \frac{1}{m_t}\left(\frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}\right)\right) - \frac{e^2}{\varepsilon r}\right]\psi(\mathbf{r}) = E\,\psi(\mathbf{r})
```

for which $m_l \neq m_t$ but can be done exactly for the hydrogen atom for which $m_l = m_t$. In practice Eq. {eq}`eq-p2-ch07-6` is solved using a variational principle. To take into account that for small $r$, we have $\varepsilon(r) \to 1$ and for large $r$, we have $\varepsilon(r) \to \varepsilon_0$ where $\varepsilon_0$ is the static dielectric constant, a spatial dependence for $\varepsilon(r)$ thus needs to be assumed and this spatial dependence can be incorporated into the variational calculation. The inclusion of screening effects by the introduction of a spatial dependence to the dielectric function $\varepsilon(r)$, is called the "central cell correction" (see Part I §4.3).

:::{figure} images/fig-p2-ch07-2.png
:name: fig-p2-ch07-2
:width: 60%
:align: center
Fig. 7.2: Energy levels of donor states in silicon, experiment and theory. Very good agreement is achieved between theory and experiment in transitions between shallow impurity states at low temperature (4 K) and low carrier concentrations ($\sim 10^{14}/\text{cm}^3$), except for the ground state transition, for which central cell corrections become important.
:::

The impurity spectra are studied most directly by infrared absorption and transmission measurements. As an example of such spectra we see in Fig. {numref}`fig-p2-ch07-3` the absorption spectrum from phosphorus impurities in Si. Note that the photon energies used in these measurements are small so that far infrared frequencies must be employed. The ground state donor level is a 1s state and allowed transitions are made to a variety of p-states. Since the constant energy surface is ellipsoidal, the 2p levels break up into a $2p\,(m_l = 0)$ level and a $2p\,(m_l = \pm 1)$ level which is doubly degenerate (see Fig. {numref}`fig-p2-ch07-3`). Transitions from the 1s to both kinds of p levels occur, and account for the sharp features in the spectrum shown. The sensitivity of the spectra is somewhat improved using modulated spectroscopy techniques as shown in Fig. {numref}`fig-p2-ch07-4`, where transitions to higher quantum states ($n = 6$) and to higher angular momentum states (f levels where $\ell = 3$) can be resolved, noting that electric dipole transitions always occur between states of opposite parity. For both Figs. {numref}`fig-p2-ch07-3` and {numref}`fig-p2-ch07-4`, the initial state is the 1s impurity ground state. Analysis of such spectra gives the location in energy of the donor impurity levels, including the location of the ground state donor level, which is more difficult to calculate because of the central cell correction.

:::{figure} images/fig-p2-ch07-3.png
:name: fig-p2-ch07-3
:width: 60%
:align: center
Fig. 7.3: Absorption spectrum of phosphorus donors in Si for a sample at liquid helium temperature containing $\sim 1.2\times 10^{14}\ \text{cm}^{-3}$ phosphorus impurities. The inset shows the $2p_0$ line on an expanded horizontal scale.
:::

:::{figure} images/fig-p2-ch07-4.png
:name: fig-p2-ch07-4
:width: 60%
:align: center
Fig. 7.4: Photo-thermal ionization spectrum of phosphorus-doped Si measured by modulation spectroscopy, which is particularly useful for resolving the higher lying impurity levels. The inset shows schematically the photo-thermal ionization process for a donor atom.
:::

In absorption measurements, the impurity level transitions are observed as peaks. On the other hand, impurity spectra can also be taken using transmission techniques, where the impurity level transitions appear as minima in the transmission spectra.

## 7.3 Departures from the Hydrogenic Model

While the simple hydrogenic model works well for the donor states in silicon and germanium, it does not work so well for the degenerate valence bands. In this case the spectra are sensitive to the impurity species from column III in the periodic table, and the poorer agreement with the hydrogenic model is because the valence band masses are heavier and the effective Bohr radius is therefore more comparable to the lattice constant. Calculations for the acceptor impurity levels are now sufficiently accurate so that good agreement between theory and experiment is obtained in recent work using more accurate computational models.

It would be naive to assume that the simple hydrogenic model works for all kinds of impurity centers. If the effective Bohr radius is comparable with atomic separations, then clearly the Coulomb potential of the impurity center is not a small perturbation to the periodic potential seen by an electron. Specific cases where the impurity effective Bohr radius becomes small are materials with either (1) a large $m^*$ or (2) a small $\varepsilon_0$ which imply a small interband coupling. When these conditions are put into Eqs. {eq}`eq-p2-ch07-3` and {eq}`eq-p2-ch07-5`, we see that a small Bohr radius corresponds to a large $E_n$ value. Thus "deep" impurity levels are not well described by simple effective mass theory. In order to make any progress at all with deep impurity level problems, we must consider the energy band structure throughout the Brillouin zone. When an electron is localized in real space, a suitable description in momentum space must include a large range of $\mathbf{k}$ values.

When the impurity concentration becomes so large that the Bohr orbits for neighboring impurity sites start to overlap, the impurity levels start to broaden, and eventually impurity bands are formed. These impurity bands tend to be only half filled because of the Coulomb repulsion which inhibits placement of both a spin up and a spin down carrier in the same impurity level. When these impurity bands lie close to a conduction or valence band extremum, the coalescence of these impurity levels with band states produces band tailing. This band tailing results in a smearing out of the threshold of the fundamental absorption edge as observed in absorption measurements. When the impurity band broadening becomes sufficiently large that the electron wavefunction extends to adjacent sites, metallic conduction can occur. The onset of metallic conduction is called the Mott metal–insulator transition.

## 7.4 Vacancies, Color Centers and Interstitials

Closely related to the impurity problem is the vacancy problem. When a compound semiconductor crystallizes, the melt usually is slightly offstoichiometry with respect to the concentration of anions and cations. As an example, suppose that we prepare PbTe with Pb and Te concentrations in the melt that are stoichiometric to 0.01%. This means that there will be a slight excess of one of the atoms or slight deficiency of the other. This deficiency shows up in the crystal lattice as a vacancy or the absence of an atom. Such a vacancy represents a strong local perturbation of the crystal potential which again cannot be modeled in terms of hydrogenic impurity models. Such vacancy centers further tend to attract impurity atoms to form vacancy-impurity complexes. Furthermore, an excess of one stoichiometric type could also form interstitials. Both of these defects are difficult to model theoretically because their spatial localization requires participation of energy states throughout the Brillouin zone. Defect centers generally give rise to energy states within the band gap of semiconductors and insulators. Such defect centers are often studied by optical techniques.

One important defect in ionic insulating crystals is the F-center ("Farbe" or color center). We see in Fig. {numref}`fig-p2-ch07-5` that the negative ion vacancy acts like a +ve charge (absence of a −ve charge). This effective +ve charge tends to bind an electron. The binding of an electron to a −ve ion vacancy is called an F-center. These F-centers give rise to absorption bands in the visible. Without F-centers, these crystals are usually clear and transparent. The F-center absorption band causes crystals with defects to appear colored, having the color of the transmitted light. When the crystals are heated to high enough temperatures, these defects can be made to anneal and the colored absorption bands disappear. This process is called bleaching.

:::{figure} images/fig-p2-ch07-5.png
:name: fig-p2-ch07-5
:width: 40%
:align: center
Fig. 7.5: Diagram of a negative ion vacancy or F-center in an ionic crystal.
:::

Many other color centers are found in ionic crystals. For example, we can have a hole bound to a +ve ion vacancy. We can also have a defect formed by a vacancy that is bound to any impurity atom, forming a vacancy-impurity complex, which can bind a charged carrier. Or we can have two adjacent vacancies (one +ve and the other −ve) binding an electron and a hole. Further generalizations are also found. These defect centers are collectively called color centers and each color center has its characteristic absorption band. In Fig. {numref}`fig-p2-ch07-6` we see an example of absorption bands due to F-centers in several alkali halides. In all cases the absorption bands are very broad, in contrast with the sharp impurity lines which are observed in the far infrared for shallow impurity level transitions in semiconductors (see Figs. {numref}`fig-p2-ch07-3` and {numref}`fig-p2-ch07-4`). In the case of the vacancy defect there is a considerable lattice distortion around each vacancy site as the neighboring atoms rearrange their electronic bonding arrangements.

:::{figure} images/fig-p2-ch07-6.png
:name: fig-p2-ch07-6
:width: 70%
:align: center
Fig. 7.6: Examples of F-center absorption lines in various alkali halide ionic crystals.
:::

A few comments are in order about the classification of point defects. In Fig. {numref}`fig-p2-ch07-7` various types of point defects are shown. Figure {numref}`fig-p2-ch07-7`(a) illustrates a perfect ionic crystal. Figure {numref}`fig-p2-ch07-7`(b) shows an ionic crystal with vacancies. This particular collection of vacancies is of the Schottky type (equal numbers of positive and negative ion vacancies). Schottky point defects also include neutral vacancies. Finally Fig. {numref}`fig-p2-ch07-7`(c) shows both vacancies and interstitials. When a + (–) ion vacancy is near a + (–) ion interstitials, this defect configuration is called a Frenkel-type point defect.

:::{figure} images/fig-p2-ch07-7.png
:name: fig-p2-ch07-7
:width: 65%
:align: center
Fig. 7.7: Schematic of various possible arrangements of both vacancies and interstitials: (a) a perfect ionic crystal, (b) an ionic crystal with positive and negative ion vacancies, and (c) an ionic crystal with positive and negative ion vacancies and interstitials.
:::

We will now use simple statistical mechanical arguments to estimate the concentration of Schottky defects. Let $E_s$ be the energy required to take an atom from a lattice site inside the crystal to the surface. If $n$ is the number of vacancies, the change in internal energy resulting from vacancy generation is $U = nE_s$. Now the number of ways that $n$ vacancy sites can be picked from $N$ lattice sites is $N!/[(N-n)!n!]$, so that the formation of vacancies results in an increase in entropy of

```{math}
:label: eq-p2-ch07-7
S = k_B\ln\frac{N!}{(N-n)!\,n!}
```

and a change in free energy

```{math}
:label: eq-p2-ch07-8
F = U - TS = nE_s - k_B T\ln\frac{N!}{(N-n)!\,n!} .
```

Using Stirling's approximation for $\ln x!$ when $x$ is large, we write

```{math}
:label: eq-p2-ch07-9
\ln x! \simeq x\ln x - x .
```

Equilibrium is achieved when $(\partial F/\partial n) = 0$, so that at equilibrium we have

```{math}
:label: eq-p2-ch07-10
E_s = k_B T\,\frac{\partial}{\partial n}\ln\frac{N!}{(N-n)!\,n!} = k_B T\ln\frac{N-n}{n}
```

from which we write

```{math}
:label: eq-p2-ch07-11
\frac{n}{N-n} = \exp\left(-\frac{E_s}{k_B T}\right)
```

or

```{math}
:label: eq-p2-ch07-12
\frac{n}{N} \simeq \exp\left(-\frac{E_s}{k_B T}\right)
```

since $n \ll N$. The vacancy density is small because for $E_s \sim 1\ \text{eV}$, $T \sim 300\ \text{K}$, we get $(n/N) \sim e^{-40} \sim 10^{-17}$.

In the case of vacancy pair formation in an ionic crystal (Schottky defect), the number of ways to make $n$ separated pairs is $[N!/(N-n)!n!]^2$, so that for Schottky vacancy pair formation, we have

```{math}
:label: eq-p2-ch07-13
\frac{n_p}{N} \simeq \exp\left(-\frac{E_p}{2k_B T}\right)
```

where $n_p$ is the pair vacancy density and $E_p$ is the energy required for pair formation.

These arguments can readily be extended to the formation of Frenkel defects and it can be shown that if $N'$ is the density of possible interstitial sites, then the density of occupied interstitial sites is

```{math}
:label: eq-p2-ch07-14
n_i \simeq (N N')^{1/2}\exp\left(-\frac{E_i}{2k_B T}\right)
```

where $E_i$ is the energy to remove an atom from a lattice site to form an interstitial defect site.

## 7.5 Spectroscopy of Excitons

An exciton denotes a system of an electron and a hole bound together by their Coulomb interaction. When a photon excites an electron into the conduction band, a hole is left behind in the valence band; the electron, having a negative charge will be attracted to this hole and may (provided the energy is not too large) bind to the positively charged hole forming an exciton. Thus, the exciton binding energy is attractive and represents a lower energy state than the band states. Excitons are important in the optical spectra of bulk semiconductors especially at low temperature. Exciton levels are important for device applications since light emitting diodes and semiconductor lasers often involve excitons. However, because of the confinement of carriers in quantum wells, exciton effects become much more important in the case of quantum wells, superlattices and devices based on these deliberately structured materials (see Part I §8.3.1 of class notes). The topic of excitons in low dimensional semiconductor systems is discussed in §7.7.

We will now use the effective mass approximation to find the exciton spectrum near an interband threshold and we assume that the exciton was created by a photon with energy slightly less than the direct energy gap $E_g$. The Schrödinger equation for the two-body exciton packet wave function $\Phi$ is written in the effective mass approximation as:

```{math}
:label: eq-p2-ch07-15
\left[\frac{\mathbf{p}_e^2}{2m_e^*} + \frac{\mathbf{p}_h^2}{2m_h^*} - \frac{e^2}{\varepsilon_0|\mathbf{r}_e - \mathbf{r}_h|}\right]\Phi = E\Phi ,
```

thereby including the Coulomb binding energy of the electron–hole pair. For simplicity, we assume that the dielectric constant $\varepsilon_0$ is independent of $\mathbf{r}_e$ and $\mathbf{r}_h$ corresponding to a large spatial extension of the exciton in a semiconductor. We introduce new coordinates for the spatial separation $\mathbf{r}$ between the electron and hole

```{math}
:label: eq-p2-ch07-16
\mathbf{r} = \mathbf{r}_e - \mathbf{r}_h
```

and for the center of mass coordinate $\boldsymbol{\rho}$ given by

```{math}
:label: eq-p2-ch07-17
\boldsymbol{\rho} = \frac{m_e^*\,\mathbf{r}_e + m_h^*\,\mathbf{r}_h}{m_e^* + m_h^*} .
```

We now separate the Schrödinger equation (Eq. {eq}`eq-p2-ch07-15`) into an equation for the relative motion of the electron and hole in the exciton wave packet $F(\mathbf{r})$ and an equation of motion for the center of mass $G(\boldsymbol{\rho})$

```{math}
:label: eq-p2-ch07-18
\Phi(\mathbf{r}_e,\mathbf{r}_h) = F(\mathbf{r})\,G(\boldsymbol{\rho}) .
```

Thus Eq. {eq}`eq-p2-ch07-15` becomes

```{math}
:label: eq-p2-ch07-19
\left[\frac{\mathbf{p}_\rho^2}{2(m_e^*+m_h^*)} + \frac{\mathbf{p}_r^2}{2\mu^*} - \frac{e^2}{\varepsilon_0 r}\right] F(\mathbf{r})\,G(\boldsymbol{\rho}) = E\,F(\mathbf{r})\,G(\boldsymbol{\rho})
```

where the reduced effective mass $\mu^*$ is given by

```{math}
:label: eq-p2-ch07-20
\frac{1}{\mu^*} = \frac{1}{m_e^*} + \frac{1}{m_h^*} .
```

to obtain an eigenvalue equation for $G(\boldsymbol{\rho})$

```{math}
:label: eq-p2-ch07-21
\frac{\mathbf{p}_\rho^2}{2(m_e^*+m_h^*)}\,G(\boldsymbol{\rho}) = \Lambda\,G(\boldsymbol{\rho})
```

which is of the free particle form and has eigenvalues

```{math}
:label: eq-p2-ch07-22
\Lambda(\mathbf{K}) = \frac{\hbar^2 K^2}{2(m_e^* + m_h^*)}
```

where $\mathbf{K}$ is the wave vector of the exciton. The free particle solutions for the center of mass problem of Eq. {eq}`eq-p2-ch07-22` show that the exciton can move freely as a unit through the crystal. The momentum of the center of mass for a direct band gap exciton is small because of the small amount of momentum imparted to the excitation by the light.

We thus obtain the Schrödinger equation in the coordinate system of relative motion:

```{math}
:label: eq-p2-ch07-23
\left[\frac{\mathbf{p}_r^2}{2\mu^*} - \frac{e^2}{\varepsilon_0 r}\right] F(\mathbf{r}) = E_n F(\mathbf{r})
```

where Eq. {eq}`eq-p2-ch07-23` has the functional form of the Schrödinger equation for a hydrogen atom with eigenvalues $E_n$ for quantum numbers $n$ (where $n = 1, 2, \ldots$) given by

```{math}
:label: eq-p2-ch07-24
E_n = -\frac{\mu^* e^4}{2\hbar^2\varepsilon_0^2 n^2} ,
```

and the total energy for the exciton is then

```{math}
:label: eq-p2-ch07-25
E = \Lambda(\mathbf{K}) + E_n .
```

The energy levels of Eq. {eq}`eq-p2-ch07-24` look like the donor impurity spectrum, but instead of the effective mass of the conduction band $m_e^*$ we now have the reduced effective mass $\mu^*$ given by Eq. {eq}`eq-p2-ch07-20`. Since $\mu^*$ has a smaller magnitude than $m_e^*$ as seen in Eq. {eq}`eq-p2-ch07-20`, we conclude that the exciton binding energy is less than the impurity ionization energy for a particular solid. An example of a spectrum showing exciton effects is presented in Fig. {numref}`fig-p2-ch07-8`. The points are experimental and the solid curves are a fit of the data points to $\varepsilon_2(\omega)$ for excitons given by

```{math}
:label: eq-p2-ch07-26
\varepsilon_2(\omega) = \frac{8\pi\,|\langle v|\mathbf{p}|c\rangle|^2\,\mu^{*3}}{3\omega^2\varepsilon_0^3}\sum_{n=1}^{\infty}\frac{1}{n^3}\,\delta(\omega-\omega_n) ,
```

where the sum is over all the exciton bound states. From Table {numref}`tab-p2-ch07-1` we see that the binding energy for excitons for GaAs is 4.9 meV and the effective Bohr radius is 112 Å, which is many lattice spacings. The various exciton lines contributing to the exciton absorption profiles in Fig. {numref}`fig-p2-ch07-8` are unresolved even for the data shown for the lowest temperature of 21 K. A material for which the higher exciton energy levels ($n = 2, 3, \ldots$) of the Rydberg series are resolved is Cu$_2$O as can be seen in Fig. {numref}`fig-p2-ch07-9`. The observation of these higher states is attributed to the forbidden nature of the coupling of the valence and conduction bands, giving rise to a strict selection rule that only allows coupling to exciton states with $p$ symmetry. Since the observation of transitions for $n \geq 2$ requires $p$ exciton states, the $n = 1$ exciton is forbidden in the Cu$_2$O spectrum, and the exciton lines start at $n = 2$.

:::{figure} images/fig-p2-ch07-8.png
:name: fig-p2-ch07-8
:width: 70%
:align: center
Fig. 7.8: Excitonic absorption spectra in GaAs near its bandgap for several sample temperatures. The lines drawn through the 21, 90 and 294 K data points represent fits with theory.
:::

:::{figure} images/fig-p2-ch07-9.png
:name: fig-p2-ch07-9
:width: 45%
:align: center
Fig. 7.9: Low temperature absorption spectrum of Cu$_2$O (plotted as the log of the transmission) showing the excitonic $p$ series associated with its "dipole-forbidden" band edge in Cu$_2$O. The transitions are sharp, and well resolved exciton lines up to $n = 5$ can be identified in Fig. {numref}`fig-p2-ch07-9`.
:::

The exciton spectrum appears to be quite similar to the impurity spectrum of shallow impurity states. These two types of spectra are distinguished through their respective dependences on impurity concentration. Suppose that we start with a very pure sample ($10^{14}$ impurities/cm$^3$) and then dope the sample lightly (to $10^{16}$ impurities/cm$^3$). If the spectrum is due to donor impurity levels, the intensity of the lines would tend to increase and perhaps broaden somewhat. If, on the other hand, the spectrum is associated with an exciton, the spectrum would be attenuated because of screening effects associated with the charged impurities. Exciton states in 3D semiconductors are generally observed in very pure samples and at very low temperatures. The criterion is that the average Bohr orbit of the exciton is less than the distance between impurities. For the sake of this argument, consider an excitonic radius of $\sim 100\ \text{\AA}$. If an impurity ion is located within this effective Bohr radius, then the electron–hole Coulomb interaction is screened by the impurity ion and the sharp spectrum associated with the excitons will disappear. A carrier concentration of $10^{16}/\text{cm}^3$ corresponds to finding an impurity ion within every $100\ \text{\AA}$ from some lattice point. Thus the electron–hole coupling can be screened out by a charged impurity concentration as low as $10^{16}/\text{cm}^3$. Low temperatures are needed to yield an energy separation of the exciton levels that is larger than $k_B T$. Increasing the temperature shifts the absorption edge and broadens the exciton line in GaAs. At a temperature of 20 K we have $k_B T \simeq 1.7\ \text{meV}$ which is nearly as large as the exciton binding energy of 4.9 meV found in Table {numref}`tab-p2-ch07-1`, explaining why no well resolved exciton spectrum for higher quantum states is observed. For the case of Cu$_2$O, the exciton binding energy of the ground state (1s), were it to exist, would be 97 meV, neglecting central cell corrections. The large exciton binding energy in Cu$_2$O also helps with the resolution of the higher quantum exciton states.

:::{table} tab-p2-ch07-1
:name: tab-p2-ch07-1
Table {numref}`tab-p2-ch07-1`: Exciton binding energy ($E_1$) and Bohr radius ($r_1$) in some direct bandgap semiconductors with the zinc-blende structure (from Yu and Cardona).
| Semiconductor | $E_1$ (meV) | $E_1$ (theory) (meV) | $r_1$ (Å) |
|---|---|---|---|
| GaAs | 4.9 | 4.4 | 112 |
| InP | 5.1 | 5.14 | 113 |
| CdTe | 11 | 10.71 | 12.2 |
| ZnTe | 13 | 11.21 | 11.5 |
| ZnSe | 19.9 | 22.87 | 10.7 |
| ZnS | 29 | 38.02 | 10.22 |
:::

## 7.6 Classification of Excitons

The exciton model discussed above is appropriate for a free exciton and a direct exciton. For the direct exciton, the initial excitation is accomplished in a $\mathbf{k}$-conserving process without the intervention of phonons. In materials like silicon and germanium, the thermal band gap corresponds to an indirect energy gap. For these materials, the exciton is formed by an indirect phonon-assisted process and the exciton is consequently called an indirect exciton. Indirect excitons can be formed either with the emission or absorption of a phonon.

Since excitons are more important at low temperatures, the emission process is much more likely than the absorption process. Because of the large difference in crystal momentum $\hbar\mathbf{k}$ between the valence band extremum and the lowest conduction band minimum in these indirect gap semiconductors, the exciton may acquire a large center of mass momentum corresponding to the momentum of the absorbed or emitted phonon $\hbar\mathbf{q}$. For the indirect exciton, a large range of crystal momentum $\hbar\mathbf{k}$ values are possible and hence the exciton levels spread out into bands as shown in the lower dashed rectangle of Fig. {numref}`fig-p2-ch07-10`. This portion of the figure also appears in more detail in the upper left-hand corner. In Fig. {numref}`fig-p2-ch07-10` we also show in the upper right-hand corner the direct exciton associated with the $\Gamma$ point conduction band for various temperatures. The shift in the absorption edge is associated with the decrease in band gap with increasing temperature. In Fig. {numref}`fig-p2-ch07-10`, the individual exciton lines are not resolved – a lower temperature would be needed for that.

:::{figure} images/fig-p2-ch07-10.png
:name: fig-p2-ch07-10
:width: 75%
:align: center
Fig. 7.10: Plot of the square root of the absorption coefficient vs. $\hbar\omega$ for Ge (because Ge is an indirect band gap semiconductor) for various temperatures, showing the effect of excitons. Features associated with both indirect and direct excitons are found. The upper left shows the detailed behavior at the onset of the indirect bandgap absorption, where the absorption is low and the upper right show direct exciton phenomena where the absorption is high.
:::

Addition of impurities to suppress the exciton formation does not help with the identification of bandgaps in semiconductors since the presence of impurities broadens the band edges. It is for this reason that energy gaps are best found from optical data in the presence of a magnetic field, to be discussed in connection with magnetism (Part III of this course).

For small distances from the impurity site or for small electron-hole separations, the effective mass approximation must be modified to consider central cell corrections explicitly. For example, central cell corrections are very important in Cu$_2$O so that the binding energy attributed to the 1s state is 133 meV, whereas the binding energy deduced from the Rydberg series shown in Fig. {numref}`fig-p2-ch07-9` indicates a binding energy of 97 meV.

The kinds of excitons we have been considering above are called free excitons. In contrast to these, are excitations called bound excitons. It is often the case that an electron and hole may achieve a lower energy state by locating themselves near some impurity site, in which case the exciton is called a bound exciton and has a larger binding energy. Bound excitons are observed in typical semi-conducting materials, along with free excitons.

Another category of excitons that occurs in semiconductors is the molecular exciton. Just as the energy of two hydrogen atoms decreases in forming molecular hydrogen H$_2$, the energy of two free (or bound) excitons may decrease on binding to form a molecular state. More complicated exciton complexes can be contemplated and some of these have been observed experimentally.

As the exciton density increases, further interaction occurs and eventually a quantum fluid called the electron-hole drop is formed. Unlike other fluids, both the negatively and positively charged particles in the electron-hole fluid have light masses. A high electron-hole density can be achieved in indirect band gap semiconductors such as silicon and germanium because of the long lifetimes of the electron-hole excitations in these materials. In treating the electron-hole drops theoretically, the electrons and holes are regarded as free particles moving in an effective potential due to the other electrons and holes. Because of the Pauli exclusion principle, no two electrons (or holes) can have the same set of quantum numbers. For this reason, like particles tend to repel each other spatially, but unlike particles do not experience this repulsion. In this discussion, two electrons are like particles, but one electron and one hole are unlike particles. Thus electron-hole pairs are formed and these pairs can be bound to each other to form an electron-hole drop. These electron-hole drops have been studied in the emission or luminescence spectra (see Chapter 8). Results for the luminescence spectra of Ge and Si at very low temperatures ($T \leq 2$ K) are shown in Fig. {numref}`fig-p2-ch07-11`. Luminescence spectra for germanium provide experimental evidence for electron-hole drops for electron-hole concentrations exceeding $10^{17}/\text{cm}^3$.

:::{figure} images/fig-p2-ch07-11.png
:name: fig-p2-ch07-11
:width: 70%
:align: center
Fig. 7.11: Recombination radiation (or photoluminescence spectrum) of free electrons (FE) and of electron-hole drops (EHD) in Ge at low temperature 3.04 K. The Fermi energy in the electron-hole drop is $\epsilon_F$ and the cohesive energy of the electron-hole drop with respect to a free exciton is $\phi_s = 1.8\ \text{meV}$. The critical concentration and temperature for forming an electron-hole drop in Ge are respectively $2.6\times 10^{17}/\text{cm}^3$ and 6.7 K, and for this reason electron-hole drop experiments are done at low temperature.
:::

In insulators (as for example alkali halides), excitons are particularly important, but here they tend to be well localized in space because the effective masses of any carriers that are well localized tend to be large. These localized excitons, called Frenkel excitons, are much more strongly bound and must be considered on the basis of a much more complicated theory. It is only for the excitons which extend over many lattice sites, the Wannier excitons, that effective mass theory can be used. And even here many-body effects must be considered to solve the problem with any degree of accuracy – already an electron bound to a hole is a two-body problem so that one-electron effective mass theory is generally not completely valid.

In studying the optical absorption of the direct gap, the presence of excitons complicates the determination of the direct energy gap, particularly in alkali halides where the exciton binding energy is large. Referring to Fig. {numref}`fig-p2-ch07-12`(a), both $\Gamma$-point and $L$-point excitons are identified in the alkali halide ionic crystal KBr. The correspondence of the optical structure with the $E(\mathbf{k})$ diagram is shown by comparison of Figs. {numref}`fig-p2-ch07-12`(a) and (b). Here it is seen that the Frenkel exciton lines dominate the spectrum at the absorption edge and we also see huge shifts in energy between the exciton lines and the direct absorption edge. These figures show the dominance of strongly bound, localized Frenkel excitons in the spectra of alkali halides.

:::{figure} images/fig-p2-ch07-12.png
:name: fig-p2-ch07-12
:width: 75%
:align: center
Fig. 7.12: (a) A spectrum of the optical density of KBr showing Frenkel excitons. The optical density is defined as $\log(1/T)$ where $T$ is the optical transmission. (b) The energy bands of KBr, as inferred from tight-binding calculations of the valence bands and from the assignments of interband edges in optical experiments. The valence band in KBr is a Br 5p derived band. The conduction band would be dominated by the K 4s band with a higher lying band possibly a K 4p band. We note that the optical spectrum on the left is dominated by exciton effects and that direct band edge contributions are much less important. We further note that the exciton binding energy is on the order of an electron volt.
:::

Excitons involve the presence of an electron-hole pair. If instead, an electron is introduced into the conduction band of an ionic crystal, a charge rearrangement occurs. This charge rearrangement partially screens the electron, thereby reducing its effective charge. When an electric field is now applied and the charge starts to move through the crystal, it moves together with this lattice polarization. The electron together with its lattice polarization is called a polaron. While excitons are important in describing the optical properties of ionic or partly ionic materials, polarons are important in describing the transport properties of such materials. The presence of polaron effects leads to thermally activated mobilities, which says that a potential barrier must be overcome to move an electron together with its lattice polarization through the crystal.

The presence of polaron effects also results in an enhancement in the effective mass of the electron. Just as one categorizes excitons as weakly bound (Wannier) or strongly bound (Frenkel), a polaron may behave as a free particle with a relatively weak enhancement of the effective mass (a large polaron) or may be in a bound state with a finite excitation energy (a small polaron), depending on the strength of the electron-phonon coupling. Large polarons are typically seen in weakly ionic semiconductors, and small polarons in strongly ionic, large-gap materials. Direct evidence for large polarons in semiconductors has come from optical experiments in a magnetic field in the region where the cyclotron frequency $\omega_c$ is close to the optical phonon frequency $\omega_{\text{LO}}$.

## 7.7 Optical Transitions in Quantum Well Structures

Optical studies are extremely important in the study of quantum wells and superlattices. For example, the most direct evidence for bound states in quantum wells comes from optical absorption measurements. To illustrate such optical experiments consider a GaAs quantum well bounded on either side by the wider gap semiconductor Al$_x$Ga$_{1-x}$As. Because of the excellent lattice matching between GaAs and Al$_x$Ga$_{1-x}$As, these materials have provided the prototype semiconductor superlattice for study of the 2D electron gas. The threshold for absorption is now no longer the band gap of bulk GaAs but rather the energy separation between the highest lying bound state of the valence band and the lowest bound state of the conduction band. Since the valence band of GaAs is degenerate at $\mathbf{k} = 0$ and consists of light and heavy holes, there will be two $n = 1$ levels in the valence band. Since $E_n \propto 1/m^*$ for the quantum well $n = 1$ bound state level, the heavy hole subband extremum will be closer in energy to the band edge than that of the light hole as shown on the left side of Fig. {numref}`fig-p2-ch07-13`. Also the density of states for the heavy hole subband will be greater than that of the light hole subband by a factor of $2m_{hh}^*/m_{lh}^*$. The optical absorption will thus show two peaks near the optical threshold as illustrated in the diagram in Fig. {numref}`fig-p2-ch07-13`, with the lower energy peak associated with the heavy hole transition and the higher energy peak is for the light hole transition. These data are for a sample with a quantum well width of $50\ \text{\AA}$, which is small enough to contain a single bound state ($n = 1$), making use of the relation

$$
E_n = \frac{\hbar^2\pi^2 n^2}{2m^* L_z} ,
$$

where $L_z$ is the quantum well width. Since the optical absorption from a single quantum well is very weak, the experiment is usually performed in superlattice structures containing a periodic array of many equivalent quantum wells. In forming the superlattice structure, it is important that the barrier between the quantum wells is not too small in extent, because for small spatial separations between quantum wells and low band offsets at the interfaces, the eigenfunctions in adjacent wells become coupled and we no longer have a simple 2D electron gas in the quantum well.

:::{figure} images/fig-p2-ch07-13.png
:name: fig-p2-ch07-13
:width: 55%
:align: center
Fig. 7.13: Optical excitations in a quantum well (50 Å quantum well width) where the valence band has light holes (lh) and heavy holes (hh) (as in GaAs). The optical density, defined as $\log(1/T)$ where $T$ is the transmission, shows peaks associated with each of these transitions.
:::

For wider quantum wells containing several bound states (see Figs. {numref}`fig-p2-ch07-14` and {numref}`fig-p2-ch07-15`), a series of absorption peaks are found for the various bound states, and the interband transitions follow the selection rule $\Delta n = 0$. This selection rule follows because of the orthogonality of wave functions for different states $n$ and $n'$. Thus to get a large $n$ matrix element for coupling valence and conduction band states, $n'$ and $n$ must be equal. As the width of the quantum well increases, the spectral features associated with transitions to the bound states become smaller in intensity and more closely spaced and eventually cannot be resolved. For the thickest films, the quantum levels are too close to each other to be resolved and only the bulk exciton peak is seen. For the 210 Å quantum well (see Fig. {numref}`fig-p2-ch07-14`), transitions for all 4 bound states within the quantum well are observed. In addition, excitonic behavior is observed on the $n = 1$ peak. For the 140 Å well, the transitions are broader, and effects due to the light and heavy hole levels can be seen through the distorted lineshape (see Fig. {numref}`fig-p2-ch07-14`). To observe transitions to higher bound states, the spectra in Fig. {numref}`fig-p2-ch07-15` are taken for a quantum well width of 316 Å, for which transitions up to (6,6) are resolved. For such wide quantum wells, the contributions from the light holes are only seen clearly when a transition for a light hole state is not close to a heavy hole transition because of the lower density of states for the light holes (see Fig. {numref}`fig-p2-ch07-15`).

:::{figure} images/fig-p2-ch07-14.png
:name: fig-p2-ch07-14
:width: 55%
:align: center
Fig. 7.14: Frequency dependence of the absorption for GaAs/Al$_{0.2}$Ga$_{0.8}$As heterostructure superlattices of different thicknesses at optical frequencies. Exciton features can be seen most clearly for interband transitions to the lowest conduction subband ($n = 1$), and a thick film (4000 Å).
:::

Excitons effects are significantly more pronounced in quantum well structures than in bulk semiconductors, as can be understood from the following considerations. When the width $d_1$ of the quantum well is less than the diameter of the exciton Bohr orbit, the electron–hole separation will be limited by the quantum well width rather than by the larger Bohr radius, thereby significantly increasing the Coulomb binding energy and the intensity of the exciton peaks. Thus small quantum well widths enhance exciton effects. Normally sharp exciton peaks in bulk GaAs are observed only at low temperature ($T \ll 77$ K); but in quantum well structures, excitons can be observed at room temperature, as shown in Fig. {numref}`fig-p2-ch07-14`, which should be compared with Fig. {numref}`fig-p2-ch07-8` for 3D bulk GaAs.

:::{figure} images/fig-p2-ch07-15.png
:name: fig-p2-ch07-15
:width: 60%
:align: center
Fig. 7.15: Transmission spectrum of a GaAs/AlGaAs multi-quantum well (well width = 316 Å) measured as a function of photon energy at low temperature (right panel). The peaks labeled $(n, n)$ have been identified with optical transitions from the $n$th heavy hole (hh) and light hole (lh) subbands to the $n$th conduction subband as shown by arrows in the band diagram in the left panel, where we see the valence band levels confined to a 30 meV range and those for the conduction band to a 225 meV range. Conduction (valence) band levels at higher (lower) energies are considered to be in continuum states. The values of the band offsets used in the analysis are given in the diagram, but these are not the most recent values.
:::

The reason why the exciton line intensities are so much stronger in the quantum well structures is due to the reduction in the radius of the effective real space Bohr orbits, thereby allowing more $\mathbf{k}$ band-states to contribute to the optical transition. This argument is analogous to arguments made to explain why the exciton intensities for the alkali halides are huge [see Fig. {numref}`fig-p2-ch07-12`(a)]. In the alkali halides the excitons have very small real space Bohr orbits so that large regions of $\mathbf{k}$ space can contribute to the exciton excitation.

In the case of the quantum well structures, two exciton peaks are observed because the bound states for heavy and light holes have different energies, in contrast to the case of bulk GaAs where the $j = 3/2$ valence band states are degenerate at $k = 0$. This property was already noted in connection with Fig. {numref}`fig-p2-ch07-13` for the bound state energies. Because of the large phonon density available at room temperature, the ionization time for excitons is only $3\times 10^{-13}$ sec. Also the presence of the electron–hole plasma strongly modifies the optical constants, so that the optical constants are strongly dependent on the light intensity, thereby giving rise to non-linear effects that are not easily observed in 3D semiconductors. Because of the small binding energy of these exciton states in a semiconductor like GaAs, modest electric fields have a relatively large effect on the photon energy of the exciton peaks and on the optical constants. Application of an electric field perpendicular to the layers of the superlattice confines the electron and hole wave functions at opposite ends of the quantum well, as shown in Fig. {numref}`fig-p2-ch07-16`.

:::{figure} images/fig-p2-ch07-16.png
:name: fig-p2-ch07-16
:width: 40%
:align: center
Fig. 7.16: Excitonic wave functions in a GaAs quantum well without (left) and with (right) an applied electric field. Because of the triangular potentials that are created by the electric field in the $z$-direction, the quantum well retains the electron and hole in a bound state at electric fields much higher than would be possible in the bulk classical ionization field.
:::

Because of this spatial separation, the excitons become relatively long lived and now recombine on a time scale of $10^{-9}$ sec. Also because of the quantum confinement, it is possible to apply much higher (50 times) electric fields than is possible for an ionization field in a bulk semiconductor, thereby producing very large Stark red shifts of the exciton peaks, as shown in Fig. {numref}`fig-p2-ch07-17`. This perturbation by the electric field on the exciton levels in a quantum confined structure is called the quantum confined Stark effect. This effect is not observed in bulk semiconductors. The large electric field-induced change in the optical absorption that is seen in Fig. {numref}`fig-p2-ch07-17` has been exploited for device applications.

:::{figure} images/fig-p2-ch07-17.png
:name: fig-p2-ch07-17
:width: 55%
:align: center
Fig. 7.17: The absorption spectra in GaAs/Ga$_{1-x}$Al$_x$As heterostructures for various values of applied electric field illustrating the large changes in optical properties produced by the quantum confined Stark shift. The electric fields normal to the layer planes are: (a) $10^4$ V/cm, (b) $5\times 10^4$ V/cm, and (c) $7.5\times 10^4$ V/cm.
:::

The following mechanism is proposed to explain the quantum confined Stark effect when the electric field is applied perpendicular to the layers. This electric field pulls the electrons and holes toward opposite sides of the layers as shown in Fig. {numref}`fig-p2-ch07-16` resulting in an overall net reduction in the attractive energy of the electron–hole pair and a corresponding Stark (electric field induced) shift in the exciton absorption. Two separate reasons explain the strong exciton peaks in quantum well structures. Firstly the walls of the quantum wells impede the electron and hole from tunneling out of the wells. Secondly, because the quantum wells are narrow (e.g., $\sim 100\ \text{\AA}$) compared to the three-dimensional (3D) exciton size (e.g., $\sim 200\ \text{\AA}$), the electron–hole interaction, although slightly weakened by the separation of electron and hole, is still strong, and well defined excitonic states can still exist. Thus exciton resonances can remain to much higher fields than would be possible in the absence of this confinement, and large absorption shifts can be seen experimentally without excessive broadening.
