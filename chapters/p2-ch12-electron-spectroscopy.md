---
title: "12 Electron Spectroscopy and Surface Science"
abstract: "This chapter surveys electron spectroscopy and surface science techniques, including photoemission, angle-resolved photoemission, synchrotron radiation sources, LEED, EELS, Auger spectroscopy, EXAFS, scanning tunneling microscopy, and atomic force microscopy."
---

# 12 Electron Spectroscopy and Surface Science

## 12.0 Overview

In this chapter, we consider various electron spectroscopy techniques and their use for the characterization of solids. Some of the techniques discussed include photo-electron spectroscopy using both ultraviolet and x-ray photon sources, electron energy loss spectroscopy, Auger electron spectroscopy, electron diffraction and scanning tunneling probes. Optical measurements over a wide frequency range are usually carried out using synchrotron radiation light sources. Since electrons are very strongly interacting probes, they are strongly absorbed by matter and consequently have a very small penetration depth. For this reason, electron spectroscopy provides a powerful set of techniques for studying surfaces, and a brief review of surface science is also given.

## 12.1 Photoemission Electron Spectroscopy

### 12.1.1 Introduction

Photoemission is one of the most important of the electron spectroscopy techniques. In photoemission, the excitation particle is the photon and the excited particle is the electron. What we measure is the dielectric response function which gives us information about elementary excitations and the electronic structures of the solid. Depending on the excitation energies, photoemission measures the density of states and the energy distribution of the joint electronic density of states, and probes the valence bands (UV spectroscopy) and the core levels (x-ray spectroscopy). With the advent of the use of synchrotron radiation and angle-resolved spectroscopy, the mapping of the electron energy bands has become possible.

:::{figure} images/fig-p2-ch12-1.png
:name: fig-p2-ch12-1
:width: 75%
:align: center
Fig. 12.1: Absorption spectra of GaP, GaAs and Ge obtained with synchrotron radiation. The arrows labeled $D$ and $P$ indicate transitions from either $d$- or $p$-like core levels. The subscripts III, IV and V represent elements of group III, IV and V, respectively, and $\Delta_p$ stands for the spin-orbit splitting.
:::

:::{figure} images/fig-p2-ch12-2.png
:name: fig-p2-ch12-2
:width: 75%
:align: center
Fig. 12.2: The universal dependence of the electron escape depth on energy in various solids, showing that most of the existing experimental data for all materials follow a universal curve. The energies of several laboratory photon sources are shown for reference. Specific values for some of the most common semiconductors are also shown.
:::

Other electron spectroscopies or related surface techniques include:

1. ESCA (Electron Spectroscopy for Chemical Analysis) which measures the chemical shift and thereby probes the local environment and oxidation state of the compound -- also called x-ray photoelectron spectroscopy (XPS)
2. AES (Auger Electron Spectroscopy) is a two electron process mainly used for elemental analysis of surface constituents
3. X-ray Fluorescence again is mainly used for elemental (chemical) analysis
4. ELS (Electron Loss Spectroscopy) which like optical spectroscopy gives the dielectric function of the material -- also called electron energy loss spectroscopy (EELS)
5. LEED (Low Energy Electron Diffraction) mainly used for structural analysis.
6. RHEED (Reflection High Energy Electron Diffraction) mainly used for in situ characterization of superlattices during layer-by-layer growth process.
7. STM (Scanning Tunneling Microscopy) which is used to obtain atomic resolution of atoms and molecules on surfaces.

All of the above techniques, except LEED and RHEED, involve an inelastic scattering mechanism.

In photoemission the photoelectric current ($I$) can be written in the form

```{math}
:label: eq-p2-ch12-1
I = I(E, \theta_e, \phi_e, \vec{\sigma}; \hbar\omega, \vec{\rho}_p, \theta_p, \phi_p)
```

where $E, \theta_e, \phi_e, \vec{\sigma}$ are respectively the kinetic energy, polar angle, azimuthal angle, and spin of the electron, and $\omega, \vec{\rho}_p, \theta_p, \phi_p$ are, respectively, the frequency, polarization, polar angle, and azimuthal angle of the photon, as shown in Fig. {numref}`fig-p2-ch12-3` where $e$ denotes the electron and $L$ (laser) denotes the photon. For the various experimental measurements, different variables are held constant. The most common quantities that are measured in photoemission experiments include:

:::{figure} images/fig-p2-ch12-3.png
:name: fig-p2-ch12-3
:width: 70%
:align: center
Fig. 12.3: Diagram of a typical photoelectron spectroscopy measurement of the electron current $j(\hbar\omega_L, \hat{e}_L, \theta_L, \phi_L; E_e, \hat{e}_e, \theta_e, \phi_e)$ in which all of the variables can, in principle, be swept.
:::

1. EDC (Energy Distribution Curves) where the photoelectron current is observed as a function of electron energy $I = I(E)$ with all other parameters held constant
2. CIS (Constant Initial State Spectroscopy) where $\hbar\omega - E$ is kept constant, and the photoelectron current is measured as a function of electron energy and photon energy $I = I(E, \hbar\omega)|_{E-\hbar\omega = \text{const}}$
3. CFS (Constant Final State Spectroscopy) where $I = I(\hbar\omega)$ is measured
4. ARPS (Angular Resolved Photoemission Spectroscopy) where the angles are allowed to vary.

:::{figure} images/fig-p2-ch12-4.png
:name: fig-p2-ch12-4
:width: 70%
:align: center
Fig. 12.4: Band diagram of a semiconductor near the surface, showing the definitions of electron affinity $\Xi$ (denoted in the text by $E_a$), work function $\phi$, and photo-threshold energy $I$ (denoted in the text by $E_0$, the vacuum level).
:::

### 12.1.2 The Photoemission Process

Historically, photoemission was first used to study the work function of solids, and to study core levels in molecules. The explanation of the photoemission process was first given by Albert Einstein in 1905, for which he received the Nobel Prize in Physics in 1921. Both UPS (Ultraviolet Photoelectron Spectroscopy) and XPS (X-ray Photoelectron Spectroscopy) were used to probe core levels.

:::{figure} images/fig-p2-ch12-5.png
:name: fig-p2-ch12-5
:width: 70%
:align: center
Fig. 12.5: Schematic diagram of a typical angle-integrated photoelectron spectrum $j(V_S)$ in a semiconductor versus the potential $V_S$. Note the points which define the vacuum level ($V_{S0}$) and the top of the valence band ($V_{SV}$). The Fermi level, as determined from the spectrum of a metal, is also indicated.
:::

In the photoemission process light incident on a sample is absorbed in a length characterized by the optical skin depth. In this optical skin depth, electrons can be excited to ionization states and are eventually emitted. Because of the much stronger interaction of electrons with matter (in contrast to the case of photons), the characteristic absorption length for the photo-excited electrons is much smaller than that for the exciting photons and as a consequence, only electrons that are excited close to the surface will be emitted (see Fig. {numref}`fig-p2-ch12-2`). By applying an electric retarding potential to the sample, some of the electrons generated in the optical excitation process are collected and their kinetic energy is measured. The following two quantities are observed in standard photoemission studies:

1. the photoelectric yield (defined as the number of electrons that are produced per unit of incident photon flux) as a function of photon energy, and
2. the energy distribution of the emitted electrons, for various values of the incident photon energy $\hbar\omega_L$.

These measurements provide information on interband transitions through analysis of structure in the photoelectric yield curves, and on the density of valence states through the shape of the electron distribution curves. Because this technique provides one of the few methods for studying the electronic density of states (particularly for low lying valence states), this has become an important measurement technique. Furthermore, because of its surface sensitivity (see Fig. {numref}`fig-p2-ch12-2`), ultraviolet photoemission spectroscopy provides a useful tool for contrasting electronic states characteristic of the surface relative to states characteristic of the bulk.

In describing the photoemission process in a metal, we make use of the model for the potential barrier at a surface shown in Fig. {numref}`fig-p2-ch12-6`.

:::{figure} images/fig-p2-ch12-6.png
:name: fig-p2-ch12-6
:width: 70%
:align: center
Fig. 12.6: The potential barrier at a surface showing the work function $e\phi$, the vacuum level $E_0$ and the photon energy $\hbar\omega$.
:::

In so-doing, we illustrate one of the classical applications of the photoemission process in measuring the work function of a solid. The work function $e\phi$ represents the minimum kinetic energy that an electron must be given by the light in order to escape from the surface (see Fig. {numref}`fig-p2-ch12-6`). For the electron to retain any information about its initial state, the mean free path (see Fig. {numref}`fig-p2-ch12-7`) must be greater than the penetration depth of the exciting radiation.

:::{figure} images/fig-p2-ch12-7.png
:name: fig-p2-ch12-7
:width: 70%
:align: center
Fig. 12.7: Log plot of the mean free path for an electron in various materials as a function of electron energy.
:::

In the model for Fig. {numref}`fig-p2-ch12-6` we assume that our surface is in the $x-y$ plane, and that $p_z$ is the electron momentum (in the direction normal to this surface) which the electron acquires through the photo-excitation process. From the diagram, we see that it will be possible for this electron to escape from the surface (by photoemission) provided that

```{math}
:label: eq-p2-ch12-2
\frac{p_z^2}{2m} + \hbar\omega \geq E_0
```

where $E_0$ is called the vacuum level, located at an energy $\hbar\omega_0$ (denoted by $\hbar\omega_c$ in Fig. {numref}`fig-p2-ch12-6`) above the band extremum.

The photocurrent $I$ will then be proportional to the number of electrons escaping from the surface of the metal and related to the current density expression $j = nev$ by

```{math}
:label: eq-p2-ch12-3
I = e\int_0^{\infty} p_z n(p_z) D(p_z) dp_z
```

where $D(p_z)$ is the escape probability for an electron of momentum $p_z$ and $n(p_z)$ is the corresponding electron density, which can be expressed through the Fermi distribution function

```{math}
:label: eq-p2-ch12-4
n(p_z) = \frac{2}{h^3}\int_{-\infty}^{\infty} dp_x dp_y \frac{1}{e^{(p^2/2m - E_F)/k_B T} + 1}
```

where the kinetic energy of the carriers includes the term $(p_x^2 + p_y^2)/2m$ which participate in the integration.

:::{figure} images/fig-p2-ch12-8.png
:name: fig-p2-ch12-8
:width: 70%
:align: center
Fig. 12.8: Schematic diagram of the states near the Fermi energy of a semiconductor.
:::

The discussion given above is appropriate to photoemission from a metal. In the case of semiconductors there is an energy gap and the Fermi level lies in this energy gap, in contrast to the situation in metals where the Fermi level lies at the top of the occupied electron states within an energy band. For semiconductors, the work function $e\phi$ is still defined relative to the Fermi level, but the threshold energy is now increased to $e\phi + \delta$ where $\delta$ is the energy difference between the highest lying valence band maximum and the Fermi level as seen in Fig. {numref}`fig-p2-ch12-8`.

For semiconductors it is customary also to refer to the electron affinity, denoted by $E_a$ on the diagram in Fig. {numref}`fig-p2-ch12-8` and representing the energy difference between the vacuum level $E_0$ and the bottom of the conduction band. We can see how interband transitions are detected in the photoemission process by the following argument. Suppose that $E_a < E_g$. The threshold for photoemission requires the incident photons to have an energy of at least:

```{math}
:label: eq-p2-ch12-5
\hbar\omega > e\phi + \delta = E_a + E_g.
```

The photoemission process will dominate until the photo-emitted electrons are themselves energetic enough to make electron-hole pairs through collisions with other electrons. The threshold for this secondary interband transition process (whereby the photo-excited electron has enough energy to produce a second photoelectron) is

```{math}
:label: eq-p2-ch12-6
\hbar\omega > (E_a + E_g) + E_g = E_a + 2E_g.
```

:::{figure} images/fig-p2-ch12-9.png
:name: fig-p2-ch12-9
:width: 70%
:align: center
Fig. 12.9: Photocurrent (yield) near threshold measured for a Si(111) surface 1.5 min after cleavage (i.e., practically clean under the vacuum of $4 \times 10^{-10}$ torr used) and several times later. Note the effects of surface contamination.
:::

The threshold for this interband process gives rise to structure in the photoemission distribution curves identified with interband transitions.

We call this general field of study photoemission spectroscopy. The advent of the theoretical development of the electronic structure of solids in the 50's made the microscopic understanding of photoemission possible. Furthermore, instrumental advances in high vacuum technology in the late 60's extended the photon range of ultraviolet photoelectron spectroscopy (UPS) to greater than 6 eV. Simultaneously the use of synchrotron radiation as a light source gives tunability of the excitation frequency and high power densities from the visible to hard x-ray frequencies. Angle resolved techniques are now commonly used to gain an understanding of the electronic structure of solids.

In the photoemission process, three basic things must happen: (3-step model)

1. optical excitation of an electron from an occupied state
2. transport of the photo-excited electron to the surface
3. the electron must escape from the surface and into the vacuum region (see Fig. {numref}`fig-p2-ch12-2`)

In order for the electron to escape from the surface into the vacuum region where the electron is collected, it must have sufficient kinetic energy. Measurements of the photoelectric yield exhibit a threshold energy and thereby provide a measure of the work function. Photoelectric yield data are plotted in terms of the quantum yield (defined as the number of electrons emitted per incident photon) vs. photon energy as shown in Fig. {numref}`fig-p2-ch12-9`. The log scale in Fig. {numref}`fig-p2-ch12-9` gives greater sensitivity for determining the threshold energy for photoemission. The figure shows that the oxide and interface contamination on a Si surface reduces the threshold energy for this surface.

### 12.1.3 Energy Distribution Curves

Of greater interest however is the energy distribution of the photo-emitted electrons $N(E)$ which is defined as the number of electrons emitted with energy $E$ in the range $\Delta E$ relative to the total number of electrons produced per photon. We show that the probability that an electron of energy $E$ is produced is proportional to the initial density of states at energy $(E - \hbar\omega)$ written as $g(E - \hbar\omega)$. The intensity profile of the electrons emitted in a photoemission experiment will contain both the primary electrons which suffer no inelastic collisions, and the secondary electrons that suffer at least one inelastic collision. The photoelectric current can then be written as

```{math}
:label: eq-p2-ch12-7
I(E, \omega) = I_p(E, \omega) + I_s(E, \omega)
```

where $I_p, I_s$ are respectively identified with primary and secondary electrons. $I_p$ depends on three factors according to the three-step model:

```{math}
:label: eq-p2-ch12-8
I_p(E, \omega) = P(E, \omega) \cdot T(E) \cdot D(E)
```

where $P(E, \omega)$ is the probability that a photoelectron of energy $E$ is excited by a photon of energy $\hbar\omega$, $T(E)$ is the transmission function of the excited electrons and $D(E)$ is the escape function of the excited electron. We can write $T(E)$ as

```{math}
:label: eq-p2-ch12-9
T(E) = \frac{\lambda_e(E)/\lambda_{ph}(\omega)}{1 + \lambda_e(E)/\lambda_{ph}(\omega)}
```

where $\lambda_e$ is the mean free path of the electrons and $\lambda_{ph}$ is the attenuation length of photon. Likewise, we can write $D(E)$ as

```{math}
:label: eq-p2-ch12-10
D(E) = \begin{cases}
\frac{1}{2}\left[1 - \left(\frac{E_F + e\phi}{E}\right)^{1/2}\right] & \text{for } E > E_F + e\phi \\
0 & \text{otherwise}
\end{cases}
```

where $E_F$ denotes the Fermi level and $\phi$ is the work function. If we consider only bulk states, and direct transitions, the energy distribution takes the form

```{math}
:label: eq-p2-ch12-11
P(E, \omega) \sim \sum_{n,n'} \int d^3k\, \delta\bigl(E_{n'}(\vec{k}) - E_n(\vec{k}) - \hbar\omega\bigr) \delta\bigl(E_{n'}(\vec{k}) - E\bigr)
```

The first $\delta$ function represents the joint density of states for optical absorption and the second $\delta$ function selects out the energy that is set by the energy analyzer. Thus the structures of the EDCs (energy distribution curves) mimic those of the joint density of states and thus give information concerning the joint density of states. The experimental data for the photo-emitted electron energy distribution are taken for a variety of photon energies as shown in the curves in Fig. {numref}`fig-p2-ch12-10` and $N(E)$ is plotted as a function of $(E - \hbar\omega)$ in order to relate the electron energy distributions to the density of states at the same initial energy. Peaks in the density of initial states give rise to peaks in $N(E)$ at the same value of $E - \hbar\omega$, independent of the energy of the photons involved in the excitation process. Each curve in Fig. {numref}`fig-p2-ch12-10` for aluminum is labeled by the incident photon energy. The dashed curve is a density of states curve for the occupied electron states in aluminum obtained from the interpretation of these data. Note the threshold appearing at the Fermi level. Since the onset of interband transitions corresponds to discontinuities in the density of states spectrum, the EDC curves can also be used to identify interband transitions. To interpret valence band states we make use of the fact that $d$-bands have low dispersion and therefore a high density of states over a narrow energy region, while $s$- and $p$-bands have a low density of states over a wide energy region (see Fig. {numref}`fig-p2-ch12-10`).

:::{figure} images/fig-p2-ch12-10.png
:name: fig-p2-ch12-10
:width: 70%
:align: center
Fig. 12.10: Energy distribution curves for photoelectrons in aluminum for various photon energies. The dashed curve shows the density of states over a wide energy region.
:::

Since laboratory ultraviolet sources are weak and difficult to work with, it is common to use a monolayer of cesium on the surface to lower the work function and the threshold energy for the photoemission process. This allows the photoemission experiments to be carried out at somewhat lower photon energies where laboratory sources are more intense. More recently, intense synchrotron radiation ultraviolet sources have become available at a few of the national accelerator facilities and this has accelerated the development of photoemission spectroscopy research.

If we allow non-direct transitions to occur, then the energy distribution function $P(E, \omega)$ takes the form

```{math}
:label: eq-p2-ch12-12
P(E, \omega) \sim \sum_{nn'} \int d^3k\, d^3k'\, |\langle n'|\vec{p}|n\rangle|^2 \delta\bigl(E_{n'}(\vec{k}') - E_n(\vec{k}) - \hbar\omega\bigr) \delta\bigl(E_{n'}(\vec{k}') - E\bigr).
```

If we rewrite $P(E, \omega)$ as

```{math}
:label: eq-p2-ch12-13
P(E, \omega) \sim \sum_n \int d^3k\, \delta\bigl[E - \hbar\omega - E_n(\vec{k})\bigr] \sum_{n'} \int d^3k'\, \delta\bigl[E_{n'}(\vec{k}') - E\bigr] |\langle n'|\vec{p}|n\rangle|^2
```

then $P(E, \omega)$ is expressed as a weighted average of the initial and final density of states. Thus indirect transitions can be invoked to explain stationary structures in the EDCs as we scan the photon frequency.

Modifications to the three step model have been made to include the possibility of an energy dependent electron mean free path

```{math}
:label: eq-p2-ch12-14
\lambda_e(E) = v_g T_e(E) = \frac{1}{\hbar}|\nabla_k E(\vec{k})| T_e(E)
```

and the possibility that the transmission function $T_e(E)$ is described by more than one core state that couples to Bloch states. In Eq. {eq}`eq-p2-ch12-14` $v_g$ denotes the group velocity.

### 12.1.4 Angle Resolved Photoelectron Spectroscopy

Advances in angle-resolved photoemission have made photoemission an even more powerful experimental technique especially for the study of electronic band structure. If one measures the kinetic energy and the propagation direction of the electron by the conservation of wave vector parallel to the surface, we obtain

```{math}
:label: eq-p2-ch12-15
\vec{K}_{\parallel} = \vec{k}_{\parallel} + \vec{G}_{\parallel}
```

where $\vec{K}$ and $\vec{k}$ are respectively the wave vectors in vacuum and in the solid and $\vec{G}$ is a reciprocal lattice vector of the solid. Wave vector conservation together with the energy conservation

```{math}
:label: eq-p2-ch12-16
E = E_f(\vec{k})
```

where $E_f(\vec{k})$ denotes the energy of the electron and the zero of energy is taken at the vacuum level gives

```{math}
:label: eq-p2-ch12-17
E = \frac{\hbar^2}{2m}(K_{\perp}^2 + \vec{K}_{\parallel}^2)
```

```{math}
:label: eq-p2-ch12-18
\frac{\hbar^2 K_{\perp}^2}{2m} = E_f(\vec{k}) - \frac{\hbar^2(\vec{k}_{\parallel} + \vec{G}_{\parallel})^2}{2m}
```

allowing the determination of $E_f(\vec{k})$ as a function of $\vec{k}_{\parallel}$ from photoemission data. Thus with a good band structure calculation the energy for all the directions of the bulk photoemission are determined. The functional form of Eq. {eq}`eq-p2-ch12-18` is especially suitable for layered materials due to the fact that the $k_{\perp}$ dispersion is very small. Thus for layered materials the band structure is approximately 2-dimensional. Each peak in the EDC will give rise to a point on the $E$ vs. $\vec{k}_{\parallel}$ plot and thus $E$ vs. $k$ can then be mapped uniquely. For a three-dimensional system, a knowledge of the energy band structure is needed since $k_{\perp}$ is not determined if $E_f(\vec{k})$ is not known.

### 12.1.5 Synchrotron Radiation Sources

Before the availability of synchrotron radiation, photoemission was carried out using a few strong discrete line sources. Synchrotron radiation has provided us with a strong tunable source from the infrared to the x-ray region of the electromagnetic spectrum. Synchrotron radiation is emitted by electrons in circular accelerators, such as synchrotrons and storage rings. This radiation is a consequence of the centripetal acceleration of the particle moving in a circular path at relativistic velocities (close to the velocity of light). The energy to produce this radiation is supplied by particle accelerators.

:::{figure} images/fig-p2-ch12-11.png
:name: fig-p2-ch12-11
:width: 70%
:align: center
Fig. 12.11: Radiation emission pattern of electrons in circular motion: Case I, non-relativistic electrons. Case II, relativistic electrons. Synchrotron radiation sources operate under case II.
:::

Synchrotron radiation has a number of properties which make it extremely useful. First, this photon source can be extremely intense, several orders of magnitude more intense than other broad-band sources. Second, it can have a very broad frequency spectrum, including the ultraviolet and x-ray regions where there are no other intense, tunable sources. The center of the spectrum is near the energy

```{math}
:label: eq-p2-ch12-19
\hbar\omega = \frac{\gamma^3 \hbar c}{R}
```

where

```{math}
:label: eq-p2-ch12-20
\gamma = \frac{E}{mc^2}
```

is the ratio of the accelerator energy to the particle's rest energy, and

```{math}
:label: eq-p2-ch12-21
R = \frac{\gamma m c^2}{eB}
```

is the radius of the circular path. For example, a 1 GeV accelerator with a 1 tesla magnetic field and a radius of 3 meters gives $\hbar\omega$ of about 1 keV. The third important property of synchrotron radiation is that it is highly collimated, being confined to a narrow "searchlight" beam in the direction tangent to the orbit with angular spread $\sim \gamma^{-1}$ radians as shown in Fig. {numref}`fig-p2-ch12-11`.

A fourth useful property is the high degree of polarization of the radiation in the plane of the orbit. Fifth, devices called "wigglers" and "undulators" have recently been developed which enhance the intensity of the radiation in a particular part of the spectrum, adding one or two orders of magnitude to the already high intensity in the desired region.

The first experiments using synchrotron radiation were carried out in the so-called parasitic mode, at synchrotrons being used for particle physics research where the accelerators are optimized for the particular set of particle-physics experiments being carried out. Furthermore these synchrotrons operate in a pulsed mode, where the electrons are accelerated in bunches up to the maximum energy desired. The desired maximum energy may vary from experiment to experiment. An example of the spectral distribution available from the Stanford SLAC facility is shown in Fig. {numref}`fig-p2-ch12-12`.

:::{figure} images/fig-p2-ch12-12.png
:name: fig-p2-ch12-12
:width: 70%
:align: center
Fig. 12.12: Photon intensity vs. photon energy for various maximum accelerator energies $E_0$ showing the spectral distribution of a synchrotron radiation source. The photon energy at which the maximum photon intensity occurs is denoted by $\varepsilon_c$ on the figure.
:::

Dedicated sources of synchrotron radiation are becoming increasingly available, such as the National Light Source at Brookhaven National Laboratory, for both the UV and x-ray regions. These are operated as storage rings, where the electron beam is maintained at a constant energy for long periods of time. Some synchrotron radiation work is still being done in the parasitic mode at storage rings being used for colliding-beam high-energy physics experiments, but here the beam currents are lower and hence the radiation is weaker.

The new synchrotron radiation sources have made possible many new experiments, not only advances in photoemission such as angle-resolved experiments, but also advances in crystal structure determination, microlithography, x-ray fluorescence, and the determination of local environments on surfaces using x-ray absorption fine structure (EXAFS).

## 12.2 Surface Science

### 12.2.1 Introduction

Many electron devices depend on the electronic properties of surfaces. Because of the geometrical effect of a two-dimensional surface, atoms at a surface have fewer neighbors than similar atoms in the bulk. Therefore, the electronic energy levels at surfaces are different from what they are in the bulk. For example, a silicon atom in bulk silicon is surrounded by four tetrahedral bonds. On the surface, a silicon atom will have fewer bonds, and the surface valence electrons that do not participate in bonding are described as dangling bonds. These surface valence electrons give rise to new electronic states called surface states. When the surface states are located in the band gap of a semiconductor or insulator, they are more readily detected. A probe of electronic energy states with a skin depth $\delta$ that is large $\delta \gg a$ compared with a lattice constant $a$ is sensitive to the bulk electronic states because the surface atoms comprise a small fraction of the total number of atoms that are probed. On the other hand, a probe with a short skin depth (such as electrons in the ten and hundred eV range) is especially sensitive to the surface atoms.

In addition, impurity atoms are preferentially adsorbed on the surface. These impurity atoms also give rise to surface states. Since adsorbed impurity atoms are important in catalyzed chemical reactions, there is considerable interest in studying these surface states. At the present time there is a great deal of work being done on the study of surfaces and on their electronic surface states. One reason is the availability of new experimental probes, such as the photoemission experiments already discussed and the STM probes discussed in this chapter, using ultra-high vacuum equipment. A second reason is the recent improvement in the calculation of surface states and of the total energy of different surface structures. A third reason is related to the smaller dimensions of semiconductor electronic devices and the increasing importance of surfaces in these devices.

### 12.2.2 Electron Diffraction

:::{figure} images/fig-p2-ch12-13.png
:name: fig-p2-ch12-13
:width: 60%
:align: center
Fig. 12.13: Bragg condition for x-ray diffraction from rows of atoms.
:::

Another common technique is low energy electron diffraction (LEED). This technique is especially sensitive to atomic arrangements on the surface and is analogous to the x-ray diffraction techniques that are used to establish the crystal structure in the bulk solid. LEED experiments can be carried out to study the structure of clean surfaces or of adsorbed species on surfaces. The positions of the LEED spots on a photograph establish the periodicity of the intrinsic surface structure.

Because of the small penetration depth for low energy electrons ($E < 100$ eV), the LEED technique emphasizes the surface structure. The LEED spot pattern that is formed is due to the constructive interference of reflections of the electron beam through scattering of rows of atoms rather than planes of atoms as occur in three-dimensional x-ray diffraction illustrated in Fig. {numref}`fig-p2-ch12-13`. Since the Bragg law in this case corresponds to rows of atoms, the surface structure that is probed is indexed by a two-dimensional lattice. In many cases the surface structure forms a superlattice relative to the substrate. This rearrangement of the surface atoms takes place because of the dangling bonds, which would otherwise occur at the surface. The rearrangement partially satisfies the bonding requirements. Within the surface, rows of atoms may move closer together or farther apart, and the surface atoms may move in or out relative to the inner layers of atoms. Such a rearrangement of the surface atoms is called reconstruction.

:::{figure} images/fig-p2-ch12-14.png
:name: fig-p2-ch12-14
:width: 70%
:align: center
Fig. 12.14: A schematic diagram of the electronic and spatial configurations of the GaAs (110) surface. The As atoms have moved outward and the Ga atoms inward compared to the positions in the bulk of the crystal.
:::

Surface reconstruction is illustrated in Fig. {numref}`fig-p2-ch12-14` for the case of a (110) GaAs surface. The corresponding change in the surface density of states is shown in Fig. {numref}`fig-p2-ch12-15`. The surface is highly sensitive to the presence of adsorbed atoms. Figure {numref}`fig-p2-ch12-16` shows the modification to the surface density of states of a (110) surface of GaAs upon exposure to oxygen, as measured in this case by photoemission (see §12.1).

:::{figure} images/fig-p2-ch12-15.png
:name: fig-p2-ch12-15
:width: 70%
:align: center
Fig. 12.15: The local density of surface states (solid line) for the bond relaxation model of the GaAs (110) surface. Electronic states located on the first two layers of Ga and As atoms are shown.
:::

:::{figure} images/fig-p2-ch12-16.png
:name: fig-p2-ch12-16
:width: 80%
:align: center
Fig. 12.16: Energy distribution curves from the upper part of the valence band of two different GaAs (110) crystals. The effects of a small oxygen exposure on the Fermi level pinning and valence band structure are also shown.
:::

The notation used to describe the surface structure is in terms of (1) the length of the lattice vectors in the superlattice relative to those of the substrate and (2) the angle of rotation of the superlattice coordinate system relative to that of the substrate. Illustrated in Fig. {numref}`fig-p2-ch12-17` are examples of $(2 \times 2)R0^\circ$ and $(\sqrt{3} \times \sqrt{3})R30^\circ$ superlattices. Note in the case of the $(\sqrt{3} \times \sqrt{3})R30^\circ$ superlattice that the coordinate system of the superlattice makes an angle of $30^\circ$ with respect to that of the substrate.

:::{figure} images/fig-p2-ch12-17.png
:name: fig-p2-ch12-17
:width: 80%
:align: center
Fig. 12.17: This figure illustrates two possible commensurate structures for adsorbed atoms on a honeycomb triangular lattice substrate. (a) The $(2 \times 2)R0^\circ$ structure and (b) the $(\sqrt{3} \times \sqrt{3})R30^\circ$ structure.
:::

The LEED technique is used to study the structure of pristine surfaces. In many cases, the surface structure may be different from the bulk structure because the surface atoms have fewer nearest neighbors. In general, one would thus expect the bond lengths (normal to the surface) for the surface atoms to be slightly shorter than in the bulk.

In addition, the LEED techniques can be used to determine the structure of adsorbed species in the coverage range from below one monolayer to perhaps two monolayers. The analysis of LEED patterns in general is more complex than for x-ray diffraction because of multiple electron scattering phenomena. For many surface structures, other evidence in addition to LEED data is needed to determine the surface structure unambiguously.

The standard in situ characterization technique for MBE growth of semiconductor superlattices (see Fig. {numref}`fig-p2-ch12-18`) is RHEED (reflection high energy electron diffractometry). The RHEED measurements are carried out at almost glancing angles of incidence to accentuate the surface sensitivity. The RHEED measurements provide a diffraction pattern on a fluorescent screen which is used to monitor the growth, providing information on the:

:::{figure} images/fig-p2-ch12-18.png
:name: fig-p2-ch12-18
:width: 70%
:align: center
Fig. 12.18: Schematic diagram of an MBE system.
:::

- structure of the growing surface and smoothness of surface
- surface reconstruction
- growth dynamics through observation of intensity oscillations
- evolution of surface impurities.

Some examples of RHEED patterns from the growth of InSb on a CdTe (001) substrate, looking down a [110] direction (glancing angle) are seen in Fig. {numref}`fig-p2-ch12-19`. After 5 sec of InSb growth ($\sim 1\,$Å/sec growth rate), a spotty diffraction pattern is seen (Fig. {numref}`fig-p2-ch12-19`a), indicative of the formation of islands of InSb on the CdTe substrate. As the growth proceeds over a $\sim$75 sec time period, the islands get large enough to join up and form a smooth surface, yielding the more uniform streak pattern. This streak pattern develops further with increasing deposition time. The diffraction patterns for later times (75 sec and beyond) show a central diffraction line characteristic of the bulk material, and some weak sidebands characteristic of the surface reconstruction. The surface reconstruction sidebands indicate a surface structure that is also periodic but with a different structure than the bulk, due to the relaxation of the solid to tie up the dangling bonds at the surface.

:::{figure} images/fig-p2-ch12-19.png
:name: fig-p2-ch12-19
:width: 70%
:align: center
Fig. 12.19: Reflection high-energy electron diffraction patterns at 20 keV and at a glancing [110] angle characterizing the growth of InSb on CdTe (001): (a) after 5 sec; (b) after 75 sec; (c) after 115 sec; (d) after 160 sec, to yield an InSb quantum well of 160 Å. (After L. A. Kolodziejski, Gunshor, Otsuka, Datta, Becker, and Nurmikko, IEEE J. Quantum Electronics, vol. QE22, 1666 (1986).)
:::

### 12.2.3 Electron Energy Loss Spectroscopy, EELS

**Electron energy loss spectroscopy** (EELS or ELS) is another commonly used technique in surface science. In electron energy loss spectroscopy, a primary electron with an energy of perhaps 100 eV will excite an electron in a filled initial state to an empty excited state. The electronic structure of the valence band states is determined by examination of the energy spectrum of the emitted secondary electrons. In the interpretation of these energy loss studies, no correction need be made for the work function for the electron, since the same potential energy drop is experienced for both the primary and secondary electrons at the surface potential barrier.

The EELS technique is conceptually the same as Raman scattering (§10.4) or inelastic neutron scattering. An incident electron of energy $E_i$ is scattered by an electron in the solid, imparting (or absorbing) an energy $\hbar\omega$ to (from) the electron in the solid to achieve an energy $E_f$ for the scattered electron using conservation of energy:

```{math}
:label: eq-p2-ch12-22
E_i - E_f = \hbar\omega.
```

Likewise momentum is conserved to yield the relation

```{math}
:label: eq-p2-ch12-23
\vec{k}_i - \vec{k}_f = \vec{q}.
```

Unlike the case of Raman scattering, the incident electrons in the EELS experiment can have a large range of wave vectors $\vec{k}_i$ so that the change in momentum for the electron in the solid can be comparable to Brillouin zone dimensions. Since the incident electrons typically have energies up to $\sim 100\,$eV with wave vectors up to $\vec{k}_i \approx 5\,$Å$^{-1}$, the EELS technique can probe a wider wave vector range in the $E(\vec{k})$ diagram than is commonly probed in an optical reflectivity measurement.

EELS is different from optical absorption and Raman scattering in that it is sensitive to different aspects of the electronic structure of solids because the probe is a charged particle rather than a photon. An incident light wave is characterized by its electric field $\vec{E}$. The rate of absorption of the light or the power loss is proportional to

```{math}
:label: eq-p2-ch12-24
\Im(\vec{E} \cdot \vec{D}) \propto \Im(\varepsilon) |\vec{E}|^2 \propto \varepsilon_2(\omega) |\vec{E}|^2
```

where the imaginary $\Im(\varepsilon) = \varepsilon_2(\omega)$ and $\vec{D} = \varepsilon \vec{E}$ is the displacement vector while $\varepsilon = \varepsilon_1 + i\varepsilon_2$ is the complex dielectric constant. Optical absorption occurs preferentially at peaks in $\varepsilon_2(\omega)$. On the other hand, an incident electron sets up a free charge density $\rho(r)$ which determines the displacement vector $\vec{D}$ through the Maxwell equation

```{math}
:label: eq-p2-ch12-25
\nabla \cdot \vec{D} = 4\pi\rho
```

For an incident electron beam, the electron energy loss rate is proportional to

```{math}
:label: eq-p2-ch12-26
\Im(\vec{E} \cdot \vec{D}) = \Im\left(\frac{1}{\varepsilon}\right) |\vec{D}|^2 = \frac{\varepsilon_2}{\varepsilon_1^2 + \varepsilon_2^2} |\vec{D}|^2
```

Thus in the EELS experiment peaks in the energy loss rate occur both near peaks in $\varepsilon_2(\omega)$ (if $|\varepsilon_1(\omega)| \gg |\varepsilon_2(\omega)|$ in this frequency region), and also near zeros in $\varepsilon_1(\omega)$ (where $\varepsilon_2(\omega)$ often remains small), corresponding to longitudinal modes. The most important longitudinal mode is the plasma mode, which is usually a prominent feature in EELS data.

The standard EELS technique is limited by the small penetration depth of the electrons relative to that for photons. EELS is thus primarily a surface technique. By using electron beams of higher energy and near normal incidence, EELS can be applied to study the electronic structure of the bulk. To emphasize the electronic structure near the surface, low energy electrons are used at grazing angles of incidence.

### 12.2.4 Auger Electron Spectroscopy (AES)

To determine the chemical species present on a surface, Auger Electron Spectroscopy (AES) is commonly used. In this technique an electron beam of several keV is incident on the surface. An electron in this primary incident beam will excite an inner core electron, creating a hole in this inner core electron state, which we will label as state $\ell$. An electron in some higher-lying state $\ell'$ in the same atom will quickly fall into the hole state $\ell$. At the same time, a second electron in a state $\ell''$ also in the same atom will be ionized. This second electron will acquire kinetic energy $E$ such that energy is conserved in the total Auger process. Thus in the Auger process (see Fig. {numref}`fig-p2-ch12-20`) there are three quantum states involved: $\ell, \ell', \ell''$. What is measured is the energy spectrum of the emitted secondary electrons. In this spectrum, peaks in the intensity profile are identified with specific core states of the atom participating in the Auger process. Since each atomic species has its own characteristic core state spectrum, the Auger spectrum provides an excellent tool for the identification of atomic species.

:::{figure} images/fig-p2-ch12-20.png
:name: fig-p2-ch12-20
:width: 60%
:align: center
Fig. 12.20: Schematic diagram of the Auger process. $E = E_{\ell'} - E_\ell - E_{\ell''}$.
:::

Furthermore, the intensity of the Auger lines provides a measure of the concentration of each atomic species. Because of the strong interaction of electrons with matter, electrons will be emitted only from atoms near the surface and for this reason Auger electron spectroscopy preferentially studies the chemical species at or near (within $\sim 40\,$Å) the free surface. Typical Auger electron spectroscopy equipment contains an Argon ion sputtering gun, permitting the removal of surface atoms so that the Auger experiments can be carried out as a function of depth into the surface by a method called depth profiling. Use of the depth profiling technique is destructive to the sample, leaving a tiny hole behind.

X-ray fluorescence measurements are also used to identify the chemical species present in a given species. In the x-ray fluorescence technique, x-rays (energies $\sim 50\,$keV) are incident on a sample and eject an electron from a core state $\ell$ in the atom of the solid. An electron in a level $\ell'$ (see Fig. {numref}`fig-p2-ch12-21`) will fall into the state $\ell$, releasing a photon with energy $E_{\ell'} - E_\ell$ which is measured.

:::{figure} images/fig-p2-ch12-21.png
:name: fig-p2-ch12-21
:width: 60%
:align: center
Fig. 12.21: Schematic diagram for the x-ray fluorescence process.
:::

The emitted x-rays thus have characteristic energies corresponding to the core level for each atom, thereby allowing identification of the chemical species. The intensity of the characteristic emission lines are related to the concentration of each of the chemical species. X-ray fluorescence (see Fig. {numref}`fig-p2-ch12-21`) is a non-destructive method for chemical analysis and has a penetration depth of $\sim 1\mu$m. This technique is usually available when doing scanning electron microscopy (SEM) studies and is called EDX.

### 12.2.5 EXAFS

:::{figure} images/fig-p2-ch12-22.png
:name: fig-p2-ch12-22
:width: 60%
:align: center
Fig. 12.22: Schematic of x-ray absorption spectrum showing the threshold region (including pre-edge and edge region) and the EXAFS spectrum.
:::

Another powerful experimental method for studying solids is Extended X-ray Absorption Fine Structure (EXAFS), which has been applied to the study of surfaces. Figure {numref}`fig-p2-ch12-22` shows a typical x-ray absorption spectrum, in the region of an inner-shell ionization energy. The photon energy at the absorption edge is equal to the minimum of threshold energy required to excite an electron from an inner tightly-bound atomic level to an unbound or continuum state. The region of higher photon energies, which is about 1-2 keV above the absorption edge, is called the EXAFS region; small oscillations in the absorption strength are produced by interference between the wave function for the outgoing electron state and the wave-functions reflected from neighboring atoms in the solid or on the surface. (See EXAFS structure is shown in Fig. {numref}`fig-p2-ch12-22`).

To analyze the EXAFS region, the final state of the electron $\phi_f(r)$ is written as

```{math}
:label: eq-p2-ch12-27
\phi_f(r) = \phi_{f,\ell}(r) + \Sigma_{k_j} \phi_{SC}(r - R_j)
```

where $\phi_{f,\ell}(r)$ is the final state of the absorption process, centered at the particular atom with angular momentum quantum number $\ell$ and which corresponds to a particular energy $E$ above the threshold, and $\phi_{SC}$ is a reflected wave corresponding to the scattering of the electron in state $\phi_{f,\ell}(r)$ from a neighboring atom at position $R_j$. If one knows, from atomic physics experiments or theory, the phase shifts $\delta_j$ corresponding to scattering from each of the neighboring chemical species, then the position $R_j$ of these neighbors can in principle be determined, since the EXAFS amplitude is proportional to: (see a chapter on scattering theory in a quantum mechanics text such as Schiff, Chapter 5 or Sakurai, Chapter 7.)

```{math}
:label: eq-p2-ch12-28
\alpha(E) \propto |\langle \phi_i|\mathcal{H}'|\phi_f\rangle|^2 \propto \sum_j F(|\vec{R}_j|) \Im\left(f(\pi) e^{2ik|\vec{R}_j|} e^{2i\delta_j}\right)
```

where $\phi_i$ is the initial atomic state, $\mathcal{H}'$ is the optical perturbation Hamiltonian, $F$ is a smooth function of $|\vec{R}_j|$, and $k \propto (2mE/\hbar^2)^{1/2}$ is the wave vector of the ejected electrons, while $f(\pi)$ is the amplitude for scattering the ejected electron at 180°, back towards the emitting atom. Because of the factor $\exp(2ik|\vec{R}_j|)$, the EXAFS amplitude is essentially the Fourier transform of the probability distribution of nearest-neighbor separations $|\vec{R}_j|$. The Fourier transform of the probability distribution, is then compared to the function calculated for a given model of the structure to test the validity of that model. In Eq. {eq}`eq-p2-ch12-28`, $\phi_f$ is the wavefunction for the final state and $\delta_j$ is phase shift for an atom at position $j$.

:::{figure} images/fig-p2-ch12-23.png
:name: fig-p2-ch12-23
:width: 70%
:align: center
Fig. 12.23: Extended absorption edge fine structure (EXAFS) is shown in (a) for thinly dispersed pure ruthenium metal, (b) for ruthenium partially covered with O$_2$ at 25°, and (c) for ruthenium mostly converted to RuO$_2$ at 400°C. Curves $d$, $e$ and $f$ are the Fourier transforms of $a$, $b$ and $c$, from which the number and bond distances of nearest-neighbor atoms may be derived.
:::

Figure {numref}`fig-p2-ch12-23` gives an example of the power of the EXAFS technique. Here EXAFS spectra are shown for a clean ruthenium surface and for surfaces exposed to two different oxidation conditions. The analysis of each trace is shown on the right to extract the pertinent nearest neighbor distances.

Equipment to carry out the various surface science experiments mentioned above is very expensive and the techniques are generally useful in many areas of solid state research. Therefore we have a number of experimental systems available through the Central Facilities of the Center for Materials Science and Engineering (Building 13). The LEED, ESCA (Electron Spectroscopy for Chemical Analysis) and AES equipment is in the Surface Analytical Laboratory (4th floor), EELS measurements can be done with the transmission electron microscope (basement 13-1027) and x-ray fluorescence measurements can be made with the scanning electron microscope using the KEVEX attachments (2nd floor) or with an electron microprobe (basement level). A range of scanning electron microscopes (SEM), transmission electron microscopes (TEM), and scanning transmission microscopes (STEM) are also available in the Building 13 Central Facilities.

### 12.2.6 Scanning Tunneling Microscopy

The scanning tunneling microscope (STM) provides a unique and powerful new tool for the direct determination of real space surface structure at the atomic level, including nonperiodic structures. In this microscope, a small metal tip is brought close enough to the surface to permit electron tunneling between the tip and the surface. The tip scans the surface in two-dimensions (hence the name scanning tunneling microscope). By adjusting the height of the tip above the surface to maintain a constant tunneling current, it is possible to obtain a contour map of the surface. The announcement of the successful observation of surface structure on an atomic scale with the STM in 1982 created tremendous excitement in the solid state community.

:::{figure} images/fig-p2-ch12-24.png
:name: fig-p2-ch12-24
:width: 70%
:align: center
Fig. 12.24: Schematic of a scanning tunneling microscope and of its operation.
:::

Some useful references and reviews are listed below.

- *IBM Journal of Research and Development* **30**, #4 & #5 (1986)
- G. Binnig and H. Rohrer, *IBM Journal of Research and Development* **30**, 355 (1986); *Scientific American*, August 1985, p. 50.
- J.E. Demuth, R.J. Hamers, R.M. Tromp and M.E. Welland, *IBM Journal of Research and Development* **30**, 396 (1986)
- J.E. Demuth, *Physics in a Technological World*, French, Editor, AIP, NY 1988.
- *Inelastic Electron Tunneling Spectroscopy*, T. Wolfram, editor, Springer Series in Solid-State Sciences 4, Springer, Berlin (1977).
- *Tunneling in Solids*, C.B. Duke, ed. by H. Ehrenreich, F. Seitz, and D. Turnbull, *Solid State Physics, Supplement #10* Academic Press, New York (1969).
- M. Amrein, A. Stasiak, H. Gross, E. Stoll, and G. Travaglini, *Science* **240**, 514, (1988).

Referring to Fig. {numref}`fig-p2-ch12-24`, the piezo-drives $P_x$ and $P_y$ scan the metal tip over the surface. The control unit (CU) applies the appropriate voltage to the piezo-drive $P_z$ to maintain a constant tunneling current $J_T$ at constant tunnel voltage $V_T$. For a constant work function, the voltages applied to the piezo-drives $P_x$, $P_y$, and $P_z$ yield the topography of the surface directly, whereas modulation of the tunnel distance $z$ by $\Delta z$ gives a measure of the work function. The dotted line in Fig. {numref}`fig-p2-ch12-24` indicates the $z$ displacement in a $y$ scan at a surface step.

The very high resolution of the STM depends on the exponential dependence of the tunneling current on the distance $z$ between the tip and the scanned surface. If $\Phi$ is the average barrier height for tunneling (the average work function $\Phi = (\Phi_1 + \Phi_2)/2$ between the tip and the surface), then the tunneling current is given by

```{math}
:label: eq-p2-ch12-29
J_T = J_0 \exp(-2\kappa z)
```

where

```{math}
:label: eq-p2-ch12-30
\hbar^2\kappa^2 = 2m\Phi
```

and $m$ is the free electron mass, so that

```{math}
:label: eq-p2-ch12-31
J_T = J_0 \exp(-A\Phi^{1/2}z)
```

where

```{math}
:label: eq-p2-ch12-32
A = 2(2m/\hbar^2)^{1/2} = 1.025 \quad \text{Å}^{-1}\text{eV}^{-1/2}
```

and

```{math}
:label: eq-p2-ch12-33
J_0 = (e^2/\hbar)(\kappa/4\pi^2 z).
```

:::{figure} images/fig-p2-ch12-25.png
:name: fig-p2-ch12-25
:width: 80%
:align: center
Fig. 12.25: STM image of a clean Au (100) surface obtained at a constant tunneling current of 1 nA, showing the terraces and monolayer step lines. The wavy structure can be resolved into individual atomic rows. The divisions on the axes correspond to spacings of 5 Å (G. Binnig, H. Rohrer, Ch. Gerber and E. Stoll, *Surface Science* **114**, 321 (1984)).
:::

The tunneling probe tip in a typical instrument may be prepared to have a radius between a few thousand angstroms to 1 $\mu$m, but containing some sharp mini-tips close to the atomic limit as shown schematically in Fig. {numref}`fig-p2-ch12-24`. The extreme sensitivity of the tunneling current on the gap width selects the extremal mini-tip protuberance ($\simeq 10\,$Å) for operation of the STM.

The very fine tips of the STM can resolve monatomic steps within 10 Å lateral resolution, as indicated in Fig. {numref}`fig-p2-ch12-25` for the case of steps on a clean Au (100) surface (G. Binnig, H. Rohrer, Ch. Gerber and E. Stoll, *Surface Science* **114**, 321 (1984)). To give the order of magnitude of the sensitivity of the STM due to the exponential dependence of the current on distance $z$, an increase in distance of 1 Å results in an order of magnitude decrease in tunneling current.

From Eq. {eq}`eq-p2-ch12-31`, we see that scanning the tunneling tip at constant tunneling current implies that $\Phi^{1/2}z = \text{constant}$. Thus for constant work function of the substrate, the displacement in the $z$ direction is adjusted to yield $z = \text{constant}$ during the scan. The voltage applied to the piezo-drive $P_z$ to achieve $z = \text{constant}$ thus provides a record of the surface topography along the scan. Figure {numref}`fig-p2-ch12-25` shows scanning tunneling micrographs of a gold (100) surface, exhibiting atomically flat terraces with monolayer steps. The tunneling current is sensitive not only to the topographical features but also to the local electronic structure. A good deal of effort has been devoted to disentangling the contributions to the tunneling current from each of these two effects.

Electronic and chemical surface properties manifest themselves primarily in the voltage dependence of the tunneling current. They appear as specific features in the local $I-V$, $V-z$ or $I-z$ characteristics, where $z$ is the distance between the tip and the surface. In practice, electronic or chemical images are obtained by recording $dI/dV$ or $dI/dz$ while scanning and controlling the gap width, and while keeping the average current constant. Depicted in Fig. {numref}`fig-p2-ch12-26` is an example of such scanning tunneling spectroscopic (STS) imaging on a Ni (100) surface (R. Garcia, J.J. Saenz and N. Garcia, *Phys. Rev.* B33, 4439 (1986)). In trace (a) showing a plot of $dI/dV$ vs $V$, the strong peak at 0.8 V is attributed to surface nickel oxide. In (b), the surface is imaged with respect to that spectroscopic feature (top) by taking scans of $dI/dV$ at 0.8 V in the $y$ direction. On the bottom of (b), topographic $I = \text{constant}$ scans are taken at the indicated voltages. Whereas the STS images differ dramatically, the STM images remain essentially unchanged. Because of the usually close relation of the tip-to-sample spacing at $I = \text{constant}$ with the topography, of $dI/dV$ with the local density of states, and of $dI/dz$ with the local barrier height (or work function), it is possible to separate the various effects observed with STM. Associated images are often referred to as "topographical or STM" images, "spectroscopic or STS" images, and "work-function profiles", respectively.

:::{figure} images/fig-p2-ch12-26.png
:name: fig-p2-ch12-26
:width: 70%
:align: center
Fig. 12.26: Spectroscopic and structural imaging of NiO on a Ni (100) surface. Shown in (a) is $dI/dV$ vs. $V$ from an oxide-covered region. The strong peak at 0.8 V is characteristic of NiO. The STS and STM images shown in (b) were obtained at the indicated bias voltages of 0.8 and 1.3 V. An oxide island to the left is evident in the STS image obtained at 0.8 V. Spatial separations in units of the NiO lattice spacing are indicated at the left (bottom). The oxide island is hardly noticeable in the STM images. The divisions on the $y$ axis correspond to spacings of 5 Å (R. Garcia, J.J. Saenz and N. Garcia, *Phys. Rev.* B33, 4439 (1986)).
:::

An important aspect of the STM is its apparent nondestructive nature. In normal operation, no perceptible irreversible damage to the sample surface occurs as a result of its use. On the other hand, the STM can be used to intentionally induce permanent local structural or chemical modifications.

One of the most noteworthy achievements of the STM has been the direct observation of surface reconstruction in silicon (G. Binnig, H. Rohrer, Ch. Gerber and E. Weibel, *Phys. Rev. Lett.* **50**, 120 (1983); G. Binnig and H. Rohrer, *IBM Journal of Research and Development* **30**, 355 (1986); J.E. Demuth, R.J. Hamers, R.M. Tromp and M.E. Welland, *IBM Journal of Research and Development* **30**, 396 (1986)). Surface reconstruction pertains to a different surface structure relative to that of the bulk due to the broken bonds at the surface discontinuity. It has been known for some time that the surface structure of semiconductors differs from that of the bulk because of the different number of nearest neighbors available for bonding. It had been conjectured that the (111) surface of Si when heated above 900°C exhibits a $(7 \times 7)$ surface reconstruction, though many uncertainties remained about whether the $(7 \times 7)$ reconstruction was correct and where the atoms were located within the unit cell. With the STM, the $(7 \times 7)$ surface reconstruction has been vividly demonstrated, as shown in Fig. {numref}`fig-p2-ch12-27`.

:::{figure} images/fig-p2-ch12-27.png
:name: fig-p2-ch12-27
:width: 70%
:align: center
Fig. 12.27: STM relief of a (111) Si surface showing the $(7 \times 7)$ unit cells with a superposed model for the $(7 \times 7)$ structure. The diagram covers a scan area of 60 Å$\times$60 Å. Original work by G. Binnig, H. Rohrer, Ch. Gerber and E. Weibel, *Phys. Rev. Lett.* **50**, 120 (1983).
:::

This picture of the $(7 \times 7)$ reconstruction was obtained on a sample previously heated at 900°C in high vacuum to remove any surface oxide layer. The STM micrograph was taken at a 2.9 V positive tip potential. The $(7 \times 7)$ rhombohedral unit cell is clearly seen in the scan in Fig. {numref}`fig-p2-ch12-27`, bounded by lines on minima with deep corners. Each unit cell contains 12 maxima and the diagonals are determined to be $46 \pm 1$ Å and $29 \pm 4$ Å, in good agreement with the crystallographically determined values of 46.56 Å and 26.88 Å, respectively.

Following the successful development of the scanning tunneling microscope, several related instruments have emerged. One of the more important of these instruments is the atomic force microscope (AFM). The forces measured by this instrument are the interatomic forces between the surface atoms under investigation and the apex atoms of a very sharp diamond tip fixed on a conducting cantilever (see Fig. {numref}`fig-p2-ch12-28`). Bending of the cantilever by the interatomic forces is monitored by the tunneling current between the cantilever and an STM tip. Scanning the diamond tip across the conducting or insulating surface under investigation at constant interatomic force yields a topographical image of the surface. The AFM image is composed of contours of constant force between the imaged surface and a probe tip, and permits measurement of surface contours of both conductors and insulators; the present versions of the STM are not able to make topographical maps of insulators.

:::{figure} images/fig-p2-ch12-28.png
:name: fig-p2-ch12-28
:width: 70%
:align: center
Fig. 12.28: Schematic diagram of the Atomic Force Microscope (AFM). An STM is used to measure the displacements of the probe tip as it scans the surface of an insulating sample.
:::

Although atomic resolution has been achieved on graphite surfaces, this technique will be more widely exploited in the study of larger-scale features on real surfaces under normal laboratory conditions. Recent work at IBM (see Fig. {numref}`fig-p2-ch12-29`) shows an application of the AFM to examine the grooves in a reactive-ion-etched silicon wafer after oxidation in air. The different microstructures on top of and in the grooves are associated with the etching method and are clearly resolved by the AFM over a wide range of scales, even though the surface is insulating. At the highest resolution, features as small as 50 Å high are easily seen.

:::{figure} images/fig-p2-ch12-29.png
:name: fig-p2-ch12-29
:width: 80%
:align: center
Fig. 12.29: AFM images of grooves etched in Si for three increased magnifications. The highest magnification scans show the details of the groove substructure which is only 50 Å high. (Y. Martin, C.C. Williams, and H.K. Wickramasinghe, *J. Appl. Phys.* **61**, 4723 (1987).)
:::
