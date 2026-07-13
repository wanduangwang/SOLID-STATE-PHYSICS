---
title: "5 Magneto-Oscillatory and Other Effects Associated with Landau Levels"
abstract: "Cyclotron resonance and interband Landau-level transitions, the de Haas-van Alphen and related magneto-oscillatory effects, their periods in 1/B, selection rules for Landau-level transitions, and the Onsager quantization condition."
---

# 5 Magneto-Oscillatory and Other Effects Associated with Landau Levels

References

- Ashcroft and Mermin, *Solid State Physics*, Ch. 14.
- Kittel, *Introduction to Solid State Physics*, 6th Ed., pp. 239-249.

## 5.1 Overview of Landau Level Effects

Studies of the density of states in a magnetic field and intraband (cyclotron resonance) and interband transitions between magnetic energy levels provide three of the most informative techniques for study of the constant energy surfaces, Fermi surfaces, and effective mass parameters in solid state physics:

1. The de Haas-van Alphen effect and the other related magneto-oscillatory effects provide the main method for studying the shape of the constant energy surfaces of semiconductors and metals. This is the main focus of this chapter.
2. Cyclotron resonance (see Fig. {numref}`fig-p3-ch05-1`) gives values for the effective mass tensor components by measurement of the transition between adjacent magnetic energy levels in a single band (intraband transitions)

    ```{math}
    :label: eq-p3-ch05-1
    \hbar\omega_c^* = E_\ell - E_{\ell-1}
    ```

    where the cyclotron frequency for a carrier orbit normal to the magnetic field is given by $\omega_c^* = eB/(m_c^* c)$ and $E_\ell$ denotes a Landau level with Landau level index $\ell$. The magnetic energy level structure for two simple parabolic bands shown in Fig. {numref}`fig-p3-ch05-2` can be interpreted as the Landau level subbands for the valence and conduction bands for a model semiconductor. The dispersion of the energy levels along $k_z$ discussed in Chapter 4

    ```{math}
    :label: eq-p3-ch05-2
    E_{\ell,m_s}(k_z) = \frac{\hbar^2 k_z^2}{2m} + \hbar\omega_c\left(\ell + \frac{1}{2}\right) - g_s\mu_B m_s B
    ```

    is shown in Fig. {numref}`fig-p3-ch05-2` for each magnetic subband $\ell$ for a given spin state $m_s$. As shown in Fig. {numref}`fig-p3-ch05-1`, cyclotron resonance experiments can be carried out on both the electron and hole carrier pockets of semiconductors. Electrons and holes correspond to the two different circular polarizations of the microwave excitation radiation. Because of the different band curvatures and effective masses associated with the various carrier types in metals and semiconductors, $\hbar\omega_c^*$ will be in resonance with $\hbar\omega$ of the resonant microwave cavity at different magnetic field values. The optical selection for these intraband (cyclotron resonance) transitions is $\Delta\ell = \pm 1$. By varying the magnetic field direction relative to the crystal axes, the corresponding cyclotron effective masses can be determined, thereby giving the effective mass tensors for electrons and/or holes.
3. Interband Landau level transitions (see Fig. {numref}`fig-p3-ch05-2`) occur when the optical frequency is equal to the separation between the extrema ($k_z = 0$) of the Landau levels $\ell$ and $\ell'$

    ```{math}
    :label: eq-p3-ch05-3
    \hbar\omega = E_{\ell,c} - E_{\ell',v} = E_g + \hbar\omega_c^*,c\left(\ell + \frac{1}{2}\right) + \hbar\omega_c^*,v\left(\ell' + \frac{1}{2}\right) .
    ```

    These interband transitions provide information on effective masses for the valence and conduction bands and the bandgaps between them. The optical selection rule for these interband transitions is $\Delta\ell = 0$. In Eq. {eq}`eq-p3-ch05-3` the subscripts $v$ and $c$ refer to the valence and conduction bands, respectively. Table {numref}`tab-p3-ch05-1` gives values for the effective masses for the conduction band $m_e$, and valence bands for heavy holes $m_{hh}$ and light holes $m_{lh}$ and for the split-off bands for several direct gap semiconductors, and data are included for the split-off band shown in Fig. {numref}`fig-p3-ch04-3` (original).

:::{figure} images/fig-p3-ch05-1.png
:name: fig-p3-ch05-1
:width: 80%
:align: center
Fig. 5.1: Typical cyclotron resonance signals in (a) germanium and (b) silicon. The magnetic field lies in a (110) plane and makes an angle with the [001] axis of $60^\circ$ for the spectrum shown for Ge and $30^\circ$ for the spectrum shown for Si. (From G. Dresselhaus, et al., Phys. Rev. 98, 368 (1955).)
:::

In semiconductors it is relatively easy to observe quantum effects in a magnetic field because of the light mass, high mobility and long relaxation times of the carriers which make it easy to satisfy $\omega_c\tau \gg 1$, the requirement for observing quantum effects.

:::{figure} images/fig-p3-ch05-2.png
:name: fig-p3-ch05-2
:width: 70%
:align: center
Fig. 5.2: Magnetic energy levels for simple parabolic valence and conduction bands. Intraband cyclotron resonance and interband Landau level transitions occur between these magnetic energy levels. The dashed curves represent the energy dispersion relation in zero magnetic field. In this diagram the spin on the electron is neglected.
:::

:::{table} Table 5.1: Effective masses of electrons and holes in direct gap semiconductors.
:name: tab-p3-ch05-1

| Crystal | $m_e/m_0$ | $m_{hh}/m_0$ | $m_{lh}/m_0$ | $m_{soh}/m_0$ | $\Delta$ (eV) | $E_g$ (eV) |
|---|---:|---:|---:|---:|---:|---:|
| InSb | $0.015$ | $0.39$ | $0.021$ | $(0.11)$ | $0.82$ | $0.23$ |
| InAs | $0.026$ | $0.41$ | $0.025$ | $(0.08)$ | $0.43$ | $0.43$ |
| InP | $0.073$ | $0.40$ | $(0.078)$ | $(0.15)$ | $0.11$ | $1.42$ |
| GaSb | $0.047$ | $0.30$ | $0.06$ | $(0.14)$ | $0.80$ | $0.81$ |
| GaAs | $0.070$ | $0.68$ | $0.12$ | $(0.20)$ | $0.34$ | $1.52$ |
:::

## 5.2 Quantum Oscillatory Magnetic Phenomena

Consider the magnetic energy levels such as those shown in Fig. {numref}`fig-p3-ch05-2` for a band electron in a solid. Assume, for example, that we have carriers in the conduction band and hence a Fermi level as indicated in Fig. {numref}`fig-p3-ch05-3` where we plot the parabolic $E(\vec{k})$ relation in zero magnetic field and indicate the energy of each magnetic sub-band extremum by its Landau level index. For each magnetic subband, the density of states is singular at its subband extremum and the resonances in the magneto-oscillatory experiments occur when an energy extremum is at the Fermi energy. Now imagine that we increase the magnetic field. The Landau level spacing is $\hbar\omega_c^* = \hbar eB/(m_c^* c)$ and is proportional to $B$. Thus as we increase $B$, we eventually reach a value $B_\ell$ for which the highest occupied Landau level $\ell$ crosses the Fermi level and the electrons that formerly were in this level must redistribute themselves among the lower levels below the Fermi level.

:::{figure} images/fig-p3-ch05-3.png
:name: fig-p3-ch05-3
:width: 60%
:align: center
Fig. 5.3: Schematic diagram of the extrema of the energy of the Landau levels for the quantum limit $\ell = 0, 1, 2, \ldots$ showing occupation of the two lowest magnetic sub-bands for $k_z = 0$. The parabola indicates the $k_x$ (or $k_y$) dependence at $B = 0$.
:::

Assume for the moment that the Fermi level is independent of magnetic field, which is a good approximation when many Landau levels are occupied. We will now show that the passage of Landau levels through the Fermi level produces an oscillatory dependence of the electron density upon the reciprocal of the magnetic field.

Since many physical quantities depend on the density of states, these physical quantities will also exhibit an oscillatory dependence on $1/B$. Thus, this oscillatory dependence on $(1/B)$ is observed in a large class of observables such as the electrical resistivity (Shubnikov-de Haas effect), Hall effect, Seebeck coefficient, ultrasonic attenuation, velocity of sound, optical dielectric constant, relaxation time, temperature dependence (magnetothermal effect), magnetic susceptibility (the de Haas-van Alphen effect). We discuss below the oscillatory dependence of the carrier density on $1/B$ as representative of this whole class of magneto-oscillatory effects.

In order for the de Haas-van Alphen effect to be observable, we require that an electron complete an orbit before scattering. The time to complete an orbit is $2\pi/\omega_c^*$ and this time must be small compared with $\tau$ the average time between electron scattering events. Thus the condition for observing the de Haas-van Alphen effect is usually written as $\omega_c^*\tau \gg 1$. Thus the observation of magneto-oscillatory phenomena requires high magnetic fields (large $\omega_c$) and low temperatures (long $\tau$). Low temperatures are also necessary so that the Landau level separations can be large compared with thermal energies. Landau level separations generally are quite small in magnitude. For example, for $B = 10$ tesla or $100$ kilogauss, and $m$ equal to the free electron mass, the Landau level separation is $\sim 10^{-3}$ eV (or $\sim 12$ K) which is to be compared with $k_B T$ at room temperature with an energy of $0.025$ eV. Therefore it is desirable to carry out de Haas-van Alphen experiments in the vicinity of $1$ K. For simplicity, we will take $T = 0$ K in our simple discussion of magneto-oscillatory effects so that the Fermi function is $1$ for $E < E_F$ (occupied states) and is $0$ for $E > E_F$ (unoccupied states).

The oscillatory behavior of the electron density in a magnetic field can be understood from the following considerations. As we increase the magnetic field two things happen.

1. The density of states degeneracy associated with $k_x$ increases because this degeneracy is proportional to $B$ (see Eq. {numref}`eq-p3-ch04-29`).
2. With increasing field $B$, the number of electrons in a magnetic energy level $\ell$ decreases as its magnetic energy level extremum approaches the Fermi level. This emptying of electrons from higher lying magnetic sub-bands is not a linear function of $B$. In particular, when a level crosses the Fermi level, the emptying of electron states is very rapid due to the high density of states at $k_z = 0$ (see Fig. {numref}`fig-p3-ch04-2`(c)).

Consider, for example the emptying of the $\ell = 1$ Landau level as it passes through $E_F$, for increasing magnetic field. All electrons in this level must be emptied when the Landau level crosses $E_F$ (see Fig. {numref}`fig-p3-ch05-3`). We show below that the extrema in the Landau levels correspond to singularities in the density of states (see Fig. {numref}`fig-p3-ch04-2`(c)). The 3D density of states in a magnetic field has a monotonic magnetic field-dependent background due to the degeneracy factor of Eq. {numref}`eq-p3-ch04-29` as well as a resonance at

```{math}
:label: eq-p3-ch05-4
E_F = \hbar\omega_c^*\left(\ell + \frac{1}{2}\right) = \frac{\hbar eB}{m_c^* c}\left(\ell + \frac{1}{2}\right)
```

denoting the energy where a Landau level passes through the Fermi level. As $B$ increases further, the magnetic energy levels tend to empty their states slowly just after the Landau level has passed through the Fermi level, and the monotonic linearly increasing degeneracy term (Eq. {numref}`eq-p3-ch04-29`) dominates. The interplay of these two factors leads to oscillations in the density of states and consequently in all physical observables depending on the density of states. The resonance condition in the density of states in a magnetic field is given by Eq. {eq}`eq-p3-ch05-4` which defines the resonant magnetic field $B_\ell$ as the field where the $E_\ell$ Landau level passes through $E_F$. Making use of Eq. {eq}`eq-p3-ch05-4`, we see that the resonances in the density of states (Eq. {numref}`eq-p3-ch04-40`) are periodic in $1/B$ with a period defined by

```{math}
:label: eq-p3-ch05-5
P \equiv \frac{1}{B_\ell} - \frac{1}{B_{\ell-1}} = \frac{e\hbar}{m_c^* E_F c}\left[\left(\ell + \frac{1}{2}\right) - \left(\ell - \frac{1}{2}\right)\right] = \frac{e\hbar}{m_c^* E_F c} .
```

Equation {eq}`eq-p3-ch05-5` shows that the period $P$ is independent of the quantum number (Landau level index) $\ell$, but depends on the product $m_c^* E_F$. It turns out that the temperature dependence of the amplitude of the de Haas-van Alphen resonances depends on $m_c^*$ so that one can thus measure both $m_c^*$ and the product $m_c^* E_F$ through study of these magneto-oscillatory phenomena, thereby yielding $E_F$ and $m_c^*$ independently.

It is often convenient to discuss the de Haas-van Alphen effect in terms of cross-sectional areas of the Fermi surface. Since $E_F = \hbar^2 k_F^2/(2m^*)$ and $A = \pi k_F^2$, we have $E_F = \hbar^2 A/(2\pi m^*)$ and from Eq. {eq}`eq-p3-ch05-5` the de Haas-van Alphen period $P$ becomes

```{math}
:label: eq-p3-ch05-6
P = \frac{1}{B_\ell} - \frac{1}{B_{\ell-1}} = \frac{2\pi e}{c\hbar A} .
```

Equation {eq}`eq-p3-ch05-6` shows that the de Haas-van Alphen period $P$ depends only on the Fermi surface cross sectional area $A$ (see Fig. {numref}`fig-p3-ch05-4`) except for universal constants. A more rigorous derivation of the de Haas-van Alphen period $P$ shows that Eq. {eq}`eq-p3-ch05-6` is valid for an arbitrarily shaped Fermi surface and the area $A$ that is associated with the resonance is the extremal cross-sectional area -- either the maximum or minimum as illustrated in Fig. {numref}`fig-p3-ch05-4`. A physical explanation for the dominance of the extremal cross section of the Fermi surface is that all cross sectional areas normal to the magnetic field contribute to the magneto-oscillatory effect, but upon integration over $k_z$, the cross-sections which do not vary with $k_z$ (or vary very little with $k_z$) will contribute to the same de Haas-van Alphen period $P$, while the non-extremal cross sections will each contribute to different values of $P$ and therefore will not give a resonant oscillatory period. By varying the magnetic field orientation, different cross-sections will become extremal, and in this way the shape of the Fermi surface can be monitored. Ellipsoidal constant energy surfaces have only one extremal (maximum) cross-section and the cyclotron effective mass $m_c^*$ is independent of $k_z$.

:::{figure} images/fig-p3-ch05-4.png
:name: fig-p3-ch05-4
:width: 60%
:align: center
Fig. 5.4: Fermi surface showing extremal cross-sectional areas. The indicated maximum and minimum areas would each show distinct de Haas-van Alphen periods. The larger cross section would have a shorter period.
:::

As an example of the de Haas-van Alphen effect in a real material, we see in Fig. {numref}`fig-p3-ch05-5`(a) oscillations observed in silver with $\vec{B}\parallel(111)$ direction. In this figure we see oscillations with a long period as well as fast or short period oscillations. From the Fermi surface diagram in the extended Brillouin zone shown for silver in Fig. {numref}`fig-p3-ch05-5`(b), we identify the fast periods with the large Fermi surface cross sections associated with the belly orbits and the slow oscillations with the small cross sectional necks. From Fig. {numref}`fig-p3-ch05-5`(b), it is clear that the necks can be clearly observed only for the $\vec{B}\parallel(111)$ directions. However, the anisotropy of the belly orbit can be monitored by varying the orientation of $\vec{B}$.

Not only do the electrons execute orbits in reciprocal space, they also execute orbits in real space in the presence of a magnetic field. Because the length scales in real space and reciprocal space are inversely proportional to one another, large orbits in $k$-space (see Fig. {numref}`fig-p3-ch05-4`) correspond to small orbits in real space. Furthermore for ellipsoidal orbits (which commonly occur in semiconductor physics), a large $k_y/k_x$ ratio in the $k$-space orbit would correspond to a small $y/x$ ratio in real space orbit but a large value for $x/y$, so that the semi-major axis in the real space orbit is rotated by $90^\circ$, relative to the semi-major axis of the reciprocal space orbit.

Although we have neglected the electron spin in the above discussion, it is nevertheless important. De Haas-van Alphen oscillations occur whenever a spin-up or a spin-down level crosses $E_F$. In fact, magneto-oscillatory observations provide an excellent tool for studying both the Landau level spacing as well as the effective $g$--factor $g_{\text{eff}}$ as can be seen from Fig. {numref}`fig-p3-ch04-2`(d) (original). Values for $m_c^*$ and $g_{\text{eff}}$ can be obtained independently since the period between every second resonance yields the Landau level separation, while sequential resonances are separated by $g_{\text{eff}}\mu_B B$.

:::{figure} images/fig-p3-ch05-5.png
:name: fig-p3-ch05-5
:width: 80%
:align: center
Fig. 5.5: (a) De Haas-van Alphen effect for silver with $\vec{B}\parallel(111)$ direction, allowing observation of the belly (fast oscillation) orbit and neck (slow oscillation) orbit shown in (b). The Fermi surface for silver is inferred from measurement of the de Haas-van Alphen effect as a function of magnetic field orientation. The period for the neck orbits [see (b)] is given by the distance between the vertical arrows in (a).
:::

## 5.3 Selection Rules for Landau Level Transitions

Since the magnetic energy states are described by harmonic oscillator wave functions, the matrix elements coupling different Landau levels are described by the selection rules for harmonic oscillators. Utilizing the matrix element of the coordinate taken between harmonic oscillator states, we write

```{math}
:label: eq-p3-ch05-7
\langle \ell | x | \ell'\rangle = \sqrt{\frac{\hbar}{2m_c^*\omega_c^*}}\left[\sqrt{\ell+1}\,\delta_{\ell',\ell+1} + \sqrt{\ell}\,\delta_{\ell',\ell-1}\right] .
```

The corresponding matrix element for $p_x$ is

```{math}
:label: eq-p3-ch05-8
\langle \ell | p_x | \ell'\rangle = \sqrt{\frac{\hbar m_c^*\omega_c^*}{2}}\left[\sqrt{\ell+1}\,\delta_{\ell',\ell+1} + \sqrt{\ell}\,\delta_{\ell',\ell-1}\right] .
```

The matrix elements for $x$ and $p_x$ determine the matrix elements for intraband transitions, referred to in §5.1. It is also of interest to discuss the expectation value of $\langle\ell|x^2|\ell'\rangle$ and $\langle\ell|p_x^2|\ell'\rangle$ which are

```{math}
:label: eq-p3-ch05-9
\langle \ell | x^2 | \ell\rangle = \frac{\hbar}{2m_c^*\omega_c^*}(2\ell+1) = \frac{\hbar}{m_c^*\omega_c^*}\left(\ell + \frac{1}{2}\right)
```

```{math}
:label: eq-p3-ch05-10
\langle \ell | p_x^2 | \ell\rangle = \frac{\hbar m_c^*\omega_c^*}{2}(2\ell+1) = \hbar m_c^*\omega_c^*\left(\ell + \frac{1}{2}\right)
```

to yield the partition theorem that the kinetic and potential energies of the harmonic oscillator are each $(\hbar\omega_c^*/2)(\ell+1/2)$. The "classical mean radius" for a harmonic oscillator state is defined by

```{math}
:label: eq-p3-ch05-11
\sqrt{\langle \ell | x^2 | \ell\rangle} = \lambda\sqrt{\ell + \frac{1}{2}}
```

using Eq. {eq}`eq-p3-ch05-9`, thus giving physical meaning to the characteristic length $\lambda$ in a magnetic field which is $\lambda = (\hbar/m_c^*\omega_c^*)^{1/2} = (c\hbar/eB)^{1/2}$ as given in Eq. {numref}`eq-p3-ch04-30`. We see here that $\lambda$ is independent of $m_c^*$ and except for universal constants depends only on $B$. The classical mean radius thus has a value at $10$ tesla (or $100$ kG) of $\sim 10^{-6}$ cm which is about $30$ lattice constants in extent. Thus to get a classical orbit within a unit cell we would require fields of $\sim 3{,}000$ tesla or $30$ megagauss. With present technology it is not yet possible to generate an external magnetic field with magnetic effects comparable in magnitude to crystal fields, though the highest available fields ($300$ tesla in the form of pulsed fields) permit entry into this important and interesting regime.

## 5.4 Landau Level Quantization for Large Quantum Numbers

The most general quantization condition for electrons in conduction bands was given by Onsager. Suppose that a magnetic field is applied parallel to the $z$--axis. Then the wave vector components $k_x$, $k_y$ which are perpendicular to the magnetic field $B$ should satisfy the commutation relation

```{math}
:label: eq-p3-ch05-12
[k_x, k_y] = i s
```

where $s = 1/\lambda^2$ is proportional to the magnetic field $B$ and is defined as $s = eB/\hbar c$ and where

```{math}
:label: eq-p3-ch05-13
k_x \rightarrow \frac{1}{i}\frac{\partial}{\partial x} - \frac{eB}{c\hbar}y
```

and

```{math}
:label: eq-p3-ch05-14
k_y \rightarrow \frac{1}{i}\frac{\partial}{\partial y} .
```

The reason why $k_x$ and $k_y$ in a magnetic field do not commute, of course, relates to the fact that $y$ and $p_y$ do not commute. We define the raising and lowering operators $k_+$ and $k_-$ in terms of $k_x$ and $k_y$

```{math}
:label: eq-p3-ch05-15
k_{\pm} = \frac{1}{\sqrt{2}}(k_x \pm i k_y) ,
```

and the operation of $k_{\pm}$ on the harmonic oscillator wavefunction $\varphi_\ell$ is given by

```{math}
:label: eq-p3-ch05-16
k_+\varphi_\ell = [(\ell+1)s]^{1/2}\varphi_{\ell+1}, \qquad k_-\varphi_\ell = (\ell s)^{1/2}\varphi_{\ell-1}, \qquad \ell = 0, 1, 2, \ldots .
```

The general quantization condition gives $k^2 = k_+k_- + k_-k_+$ so that

```{math}
:label: eq-p3-ch05-17
(2\ell+1)s \leftrightarrow k^2
```

and corresponds to the Bohr-Sommerfeld-Onsager relation:

```{math}
:label: eq-p3-ch05-18
\oint_{E(k)=\text{const}} |k|\,dk = 2\pi s\left(\ell + \frac{1}{2}\right), \qquad (\ell\gg 1)
```

where the line integral is over an orbit on the constant energy surface. This semiclassical quantization gives the classical limit for large quantum numbers and can be applied to calculate orbits of carriers in a magnetic field on any constant energy surface.
