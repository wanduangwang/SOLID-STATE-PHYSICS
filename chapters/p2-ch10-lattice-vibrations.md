---
title: "10 Optical Study of Lattice Vibrations"
abstract: "This chapter reviews the optical study of lattice vibrations in solids, including infrared absorption, Raman and Brillouin scattering, dielectric response to phonons, polariton dispersion relations, Feynman diagram techniques, and applications to quantum wells and superlattices."
---

# 10 Optical Study of Lattice Vibrations

## 10.0 Overview

The lattice vibrations in solids can be sensitively investigated by optical methods. Infrared spectroscopy probes infrared-active phonons (odd parity modes with a dipole moment), while Raman spectroscopy probes Raman-active modes (even parity modes). Because the wave vector of light is very small compared to the Brillouin zone dimensions, these optical techniques probe phonon modes near $\vec{q} = 0$. Thermal neutrons provide complementary information over the full Brillouin zone. This chapter introduces the dielectric response to phonons, the polariton dispersion relation, light scattering, Feynman diagrams for Raman scattering, and Raman studies of quantum wells and superlattices.

## 10.1 Lattice Vibrations in Semiconductors

### 10.1.1 General Considerations

The lattice vibrations in semiconductors are described in terms of $3N$ branches for the phonon dispersion relations where $N$ is the number of atoms per primitive unit cell. Three of these branches are the acoustic branches, and the remaining $3N-3$ are the optical branches. The optical lattice modes at $\vec{q} = 0$ are sensitively studied by infrared spectroscopy (optical reflectivity or transmission) for odd parity modes, including those for which the normal mode vibrations involve a dipole moment. Raman spectroscopy provides a complementary tool to infrared spectroscopy, insofar as Raman spectroscopy is sensitive to even parity modes. Since the group IV semiconductors have inversion symmetry, the optical phonon branch is Raman active but is not seen in infrared spectroscopy. The III-V compound semiconductors, however, do not have inversion symmetry, so that the optical modes for semiconductors such as GaAs are both infrared-active and Raman-active. A schematic optical absorption curve to a semiconductor is shown in Fig. {numref}`fig-p2-ch10-1`.

:::{figure} images/fig-p2-ch10-1.png
:name: fig-p2-ch10-1
:width: 80%
:align: center
Fig. 10.1: Hypothetical absorption spectrum for a typical III-V semiconductor as a function of photon energy.
:::

Since the wavevector for light is very much smaller than the Brillouin zone dimensions, conservation of momentum requires the wave vector for the phonon $\vec{q}_{\rm phonon}$ that is created or absorbed to be much smaller than Brillouin zone dimensions, so that the wave vectors for phonons that are observed in first order infrared or Raman processes are close to $\vec{q} = 0$. Since thermal neutrons can have a wide range of momentum values, neutron spectroscopy using thermal neutrons as a probe allows exploration of the phonon branches over a wide range of $\vec{q}_{\rm phonon}$. Since heat in a semiconductor is dominantly carried by the acoustic phonons, information about the acoustic phonons is also provided by thermal conductivity studies.

We now review the interaction of the electromagnetic field with an oscillating dipole due to a lattice vibration. Crystals composed of two different atomic species (like NaCl) can have vibrating ions at finite temperatures. When these ions are vibrating in an optic mode, a vibrating dipole is created and this dipole can interact with the electromagnetic field. In discussing this interaction, we wish to focus attention on the following points:

1. The existence of two characteristic frequencies for the vibrations in a solid in the presence of light:
   - $\omega_t =$ transverse optical phonon frequency (TO)
   - $\omega_\ell =$ longitudinal optical phonon frequency (LO)

   The transverse optical phonon frequency $\omega_t$ corresponds to a resonance in the dielectric function

   ```{math}
   :label: eq-p2-ch10-1
   \varepsilon(\omega) = \varepsilon_\infty + \frac{\rm const}{\omega_t^2 - \omega^2}
   ```

   where $\varepsilon_\infty$ is the high frequency dielectric function (appropriate to electronic excitation processes) and a resonance in $\varepsilon(\omega)$ occurs at the TO phonon frequency $\omega = \omega_t$. The strong frequency dependence of the dielectric function (large dispersion) near $\omega_t$ is exploited in designing prisms for monochromators. The frequency $\omega_t$ is also called the *reststrahl* frequency.

2. The frequency $\omega_\ell$ is the frequency at which the real part of the dielectric function vanishes $\varepsilon_1(\omega_\ell) = 0$. It will be shown below that $\omega_\ell$ is the longitudinal optical phonon frequency corresponding to $\vec{q} = 0$ (zero wave vector). By group theory, it can be shown that the lattice modes at $\vec{q} = 0$ for a cubic crystal are three-fold degenerate. This degeneracy is lifted by the electromagnetic interaction in polar materials to give a splitting between the LO and TO modes. An example of the reflectivity of a normally transparent material in the region where phonon excitation processes dominate is shown in Fig. {numref}`fig-p2-ch10-2`.

:::{figure} images/fig-p2-ch10-2.png
:name: fig-p2-ch10-2
:width: 70%
:align: center
Fig. 10.2: Reflectivity of a thick crystal of NaCl vs. wave length at several temperatures. The nominal values of $\omega_\ell$ and $\omega_t$ at room temperature correspond to wavelengths of 38 and 61 microns, respectively. The additional structure seen in the reflectivity spectrum near $\omega_\ell$ is associated with defects.
:::

From the diagram, we see that for $\omega_t < \omega < \omega_\ell$, the dielectric is both highly reflective and lossy. This range between $\omega_t$ and $\omega_\ell$ is also observed as an absorption band in infrared absorption studies.

3. The dielectric function $\varepsilon(\omega)$ approaches the static dielectric constant $\varepsilon_0$ as $\omega \to 0$. Also, $\varepsilon(\omega)$ approaches the high frequency dielectric function $\varepsilon_\infty$ as $\omega$ approaches frequencies that are large compared with $\omega_t$ and $\omega_\ell$. Even when we consider $\omega$ to be large, we are still thinking of $\omega$ as being very much smaller than typical interband electronic frequencies. Lattice modes typically are important in the wavelength range $10 \leq \lambda \leq 100\,\mu$m or $0.01 \leq \hbar\omega \leq 0.1\,$eV or $50 \leq \omega \leq 1000\,$cm$^{-1}$.

4. The quantities $\varepsilon_0$, $\varepsilon_\infty$, $\omega_t$ and $\omega_\ell$ are not independent, but are related by a very general relation called the Lyddane-Sachs-Teller relation:

   ```{math}
   :label: eq-p2-ch10-2
   \frac{\omega_\ell^2}{\omega_t^2} = \frac{\varepsilon_0}{\varepsilon_\infty}
   ```

   which is written here for a crystal with two atoms/unit cell.

## 10.2 Dielectric Constant and Polarizability

The polarizability $\alpha$ of an atom is defined in terms of the local electric field at the atom,

```{math}
:label: eq-p2-ch10-3
p = \alpha E_{\rm local}.
```

The polarizability is an atomic property, the dielectric constant will depend on the manner in which the atoms are assembled to form a crystal. For a non-spherical atom $\alpha$ will be a tensor. The polarization of a crystal may be approximated as the product of the polarizabilities of the atoms times the local electric fields,

```{math}
:label: eq-p2-ch10-4
P = \sum_j N_j p_j = \sum_j N_j \alpha_j E_{\rm local}(j),
```

where $N_j$ is the concentration and $\alpha_j$ the polarizability of atoms or ions $j$, and $E_{\rm local}(j)$ is the local field at atomic sites $j$. If the local field is given by the Lorentz relation, then

```{math}
:label: eq-p2-ch10-5
P = \left(\sum_j N_j \alpha_j\right)\left(E + \frac{4\pi}{3}P\right).
```

Solving for the susceptibility

```{math}
:label: eq-p2-ch10-6
\chi = \frac{P}{E} = \frac{\sum_j N_j \alpha_j}{1 - \frac{4\pi}{3}\sum_j N_j \alpha_j}.
```

Using the definition $\epsilon = 1 + 4\pi\chi$ one obtains the Clausius-Mossotti relation

```{math}
:label: eq-p2-ch10-7
\frac{\epsilon - 1}{\epsilon + 2} = \frac{4\pi}{3}\sum_j N_j \alpha_j.
```

This relates the dielectric constant to the electronic polarizability, but only for crystal structures for which the Lorentz local field relation applies.

## 10.3 Polariton Dispersion Relations

The statements 1-5 in §10.1 provide an overview on optical studies of lattice modes. In this section we discuss the polariton dispersion relations which describe the interaction of light with the electric dipole moment associated with infrared absorption, and the LO-TO splitting of the normal mode vibration of the atoms in the solid arising from these dispersion relations.

Consider the equation of motion of an ion in a solid using the normal mode coordinate $\vec{r}$, so that harmonic motion yields

```{math}
:label: eq-p2-ch10-8
m\ddot{\vec{r}} = -\kappa \vec{r} + e\vec{E} = -m\omega^2\vec{r}
```

where

```{math}
:label: eq-p2-ch10-9
\vec{E} = \vec{E}_0 e^{-i\omega t}
```

and $-\kappa\vec{r}$ represents a lattice restoring force while $e\vec{E}$ is the force due to the actual electric field $\vec{E}$ at an ion site. Maxwell's equations give us

```{math}
:label: eq-p2-ch10-10
\nabla \times \vec{H} = \frac{1}{c}\dot{\vec{D}} = \frac{1}{c}(\dot{\vec{E}} + 4\pi\dot{\vec{P}}) = -\frac{i\omega}{c}(\vec{E} + 4\pi\vec{P})
```

```{math}
:label: eq-p2-ch10-11
\nabla \times \vec{E} = -\frac{1}{c}\dot{\vec{H}} = \frac{i\omega}{c}\vec{H}
```

We also have a constitutive equation which tells us that the total polarization arises from an ionic contribution $N'e\vec{r}$ where $N'$ is the number of optical modes per unit volume and from an electronic contribution $n\alpha\vec{E}$, where $n$ is the electron concentration and $\alpha$ is the electronic polarizability:

```{math}
:label: eq-p2-ch10-12
\vec{P} = N'e\vec{r} + n\alpha\vec{E}.
```

Equations {eq}`eq-p2-ch10-8`, {eq}`eq-p2-ch10-10`, {eq}`eq-p2-ch10-11` and {eq}`eq-p2-ch10-12` represent 4 equations in the 4 variables $\vec{E}$, $\vec{H}$, $\vec{r}$, and $\vec{P}$.

We now seek plane wave solutions for transverse wave propagation: $(\vec{E},\vec{H})$ in the $xy$ plane and perpendicular to the Poynting vector, $\vec{S} = [c/(8\pi)]\mathrm{Re}(\vec{E}^* \times \vec{H})$, and the Poynting vector is taken along the $z$ direction

```{math}
:label: eq-p2-ch10-13
E_x = E_x^0 e^{-i(\omega t - Kz)}
```

```{math}
:label: eq-p2-ch10-14
H_y = H_y^0 e^{-i(\omega t - Kz)}
```

```{math}
:label: eq-p2-ch10-15
P_x = P_x^0 e^{-i(\omega t - Kz)}
```

```{math}
:label: eq-p2-ch10-16
r_x = r_x^0 e^{-i(\omega t - Kz)}.
```

Here $K$ is the wave vector for the light, $K = 2\pi/\lambda$. Using values for $\lambda$ typical for lattice modes in NaCl, we have $\lambda \sim 60\,\mu$m and $K \sim 10^3\,$cm$^{-1}$. Substitution of the harmonic solutions in Eqs. {eq}`eq-p2-ch10-13`-{eq}`eq-p2-ch10-16` into the 4 equations (Eqs. {eq}`eq-p2-ch10-8`, {eq}`eq-p2-ch10-10`, {eq}`eq-p2-ch10-11` and {eq}`eq-p2-ch10-12`) for the four variables $\vec{E}$, $\vec{H}$, $\vec{r}$, and $\vec{P}$ yields:

```{math}
:label: eq-p2-ch10-17
iK H_y - \frac{i\omega}{c}E_x - \frac{4\pi i\omega}{c}P_x = 0
```

```{math}
:label: eq-p2-ch10-18
-iK E_x + \frac{i\omega}{c}H_y = 0
```

```{math}
:label: eq-p2-ch10-19
-\omega^2 r_x + \frac{\kappa}{m}r_x - \frac{e}{m}E_x = 0
```

```{math}
:label: eq-p2-ch10-20
P_x - N' e r_x - n\alpha E_x = 0.
```

Equations {eq}`eq-p2-ch10-17`-{eq}`eq-p2-ch10-20` form 4 equations in 4 unknowns. To have a non-trivial solution to Eqs. {eq}`eq-p2-ch10-17`-{eq}`eq-p2-ch10-20`, the coefficient determinant must vanish. We arrange the coefficient determinant following the order of the variables in Eqs. {eq}`eq-p2-ch10-13`-{eq}`eq-p2-ch10-16`: $(E_x \quad H_y \quad P_x \quad r_x)$:

```{math}
:label: eq-p2-ch10-21
\begin{vmatrix}
\omega/c & -K & 4\pi\omega/c & 0 \\
K & -\omega/c & 0 & 0 \\
e/m & 0 & 0 & \omega^2 - \kappa/m \\
-n\alpha & 0 & 1 & -N'e
\end{vmatrix} = 0.
```

Multiplying out the determinant in Eq. {eq}`eq-p2-ch10-21`, we get a quadratic equation in $\omega^2$

```{math}
:label: eq-p2-ch10-22
\omega^4[1 + 4\pi n\alpha] - \omega^2\left[c^2K^2 + \frac{\kappa}{m} + \frac{4\pi N'e^2}{m} + \frac{4\pi n\alpha\kappa}{m}\right] + K^2c^2\frac{\kappa}{m} = 0.
```

Equation {eq}`eq-p2-ch10-22` is more conveniently written in terms of the parameters $\varepsilon_\infty$, $\varepsilon_0$, and $\omega_T$ where these parameters are defined in Eqs. {eq}`eq-p2-ch10-23`, {eq}`eq-p2-ch10-25` and {eq}`eq-p2-ch10-27` given below:

1. The high frequency dielectric constant $\varepsilon_\infty$ is written as $\varepsilon_\infty = 1 + 4\pi P_\infty/E$, and is the parameter normally used to express the optical core dielectric constant when discussing electronic processes studied by optical techniques. From the equation of motion (Eq. {eq}`eq-p2-ch10-8`), we conclude that at high frequencies ($\omega \gg \omega_T$ and we show below that $\omega_T$ is the transverse optical frequency), the ionic displacement is small, for otherwise the acceleration would tend to $\infty$. Thus as the frequency increases, the ions contribute less and less to the polarization vector. We thus have the result $P_\infty = n\alpha E$, so that the electronic contribution dominates and

   ```{math}
   :label: eq-p2-ch10-23
   \varepsilon_\infty = 1 + 4\pi n\alpha.
   ```

2. The low frequency ($\omega \ll \omega_T$) dielectric constant is written as $\varepsilon_0$. At $\omega = 0$ the equation of motion Eq. {eq}`eq-p2-ch10-8` yields $\vec{r} = e\vec{E}/\kappa$ so that the polarization vector at zero frequency is

   ```{math}
   :label: eq-p2-ch10-24
   \vec{P}_0 = \left[\frac{N'e^2}{\kappa} + n\alpha\right]\vec{E};
   ```

   and

   ```{math}
   :label: eq-p2-ch10-25
   \varepsilon_0 = 1 + 4\pi\left[\frac{N'e^2}{\kappa} + n\alpha\right].
   ```

   At a general frequency $\omega$, we must from Eqs. {eq}`eq-p2-ch10-8` and {eq}`eq-p2-ch10-12` write

   ```{math}
   :label: eq-p2-ch10-26
   \varepsilon(\omega) = 1 + 4\pi\left[\frac{N'e^2}{\kappa - m\omega^2} + n\alpha\right].
   ```

3. Finally, we introduce a frequency $\omega_T$ defined as

   ```{math}
   :label: eq-p2-ch10-27
   \omega_T^2 \equiv \frac{\kappa}{m}
   ```

   which depends only on the restoring forces and not on the externally applied field. Of course, these restoring forces will depend on internal fields, since electromagnetic interactions are responsible for producing these lattice vibrations in the first place. We will later identify $\omega_T$ with $\omega_t$, the transverse optical phonon frequency. Substitution of $\varepsilon_\infty$, $\varepsilon_0$, and $\omega_T$ into Eq. {eq}`eq-p2-ch10-22` yields the polarization dispersion relation

   ```{math}
   :label: eq-p2-ch10-28
   \omega^4\varepsilon_\infty - \omega^2[c^2K^2 + \omega_T^2\varepsilon_0] + \omega_T^2c^2K^2 = 0.
   ```

   Equation {eq}`eq-p2-ch10-28` has two solutions

   ```{math}
   :label: eq-p2-ch10-29
   \omega^2 = \frac{1}{2\varepsilon_\infty}(\omega_T^2\varepsilon_0 + c^2K^2) \pm \left[\frac{1}{4\varepsilon_\infty^2}(\omega_T^2\varepsilon_0 + c^2K^2)^2 - \omega_T^2K^2\frac{c^2}{\varepsilon_\infty}\right]^{1/2}
   ```

   which are shown graphically in Fig. {numref}`fig-p2-ch10-3`. Each solution in Eq. {eq}`eq-p2-ch10-29` is twofold degenerate, since $\vec{E}$ can be chosen in any arbitrary direction perpendicular to the propagation vector. The coupled excitation of the transverse optical phonon to the electromagnetic radiation is called the **polariton** and the picture in Fig. {numref}`fig-p2-ch10-3` is called the **polariton** dispersion relation. There is also a longitudinal direction for both the light and the lattice vibrations; for this case there is no coupling between the light and the phonons and the frequency is the same as in the absence of light. We therefore obtain a total of 6 modes for the 3 coupled optical lattice modes and the three electromagnetic modes (two transverse modes representing photons and one longitudinal mode). It is of interest to examine the solutions of Eq. {eq}`eq-p2-ch10-29` for small and large $K$ vectors where we must remember that the scale of the $K$-vectors for light is a scale of $10^3 - 10^4\,$cm$^{-1}$ rather than $10^8\,$cm$^{-1}$ which describes the Brillouin zone dimension, corresponding to Brillouin zone dimensions. Thus the whole picture shown in Fig. {numref}`fig-p2-ch10-3` occurs essentially at $\vec{q} = 0$ when plotting phonon dispersion relations $\omega_q(\vec{q})$ for wave vectors $\vec{q}$ in the Brillouin zone.

:::{figure} images/fig-p2-ch10-3.png
:name: fig-p2-ch10-3
:width: 80%
:align: center
Fig. 10.3: Polariton dispersion relations showing the coupling between the transverse lattice vibrations and the electromagnetic radiation. In this figure, we clearly see the splitting of the LO and TO modes ($\omega_L - \omega_T$) induced by the ionicity of the solid.
:::

At small $K$ vectors ($|K| \ll 10^4\,$cm$^{-1}$), we have two solutions to Eq. {eq}`eq-p2-ch10-29`. The positive solution is given by

```{math}
:label: eq-p2-ch10-30
\omega^2 = \frac{1}{\varepsilon_\infty}(\omega_T^2\varepsilon_0 + c^2K^2)
```

which gives

```{math}
:label: eq-p2-ch10-31
\omega_T^2\frac{\varepsilon_0}{\varepsilon_\infty} \equiv \omega_L^2,
```

thus defining the frequency $\omega_L$. In writing this solution we neglected the term $c^2K^2$ as $K \to 0$. This solution corresponds to the phonon branch with finite frequency at $K = 0$ and hence is an optical phonon mode. We will call this frequency $\omega_L$ and later we will identify $\omega_L$ with the longitudinal optical phonon mode frequency, $\omega_\ell$. We shall see that the above definition is equivalent to taking frequency $\omega_\ell$ as the frequency where the real part of the dielectric function vanishes $\varepsilon_1(\omega_\ell) \equiv 0$. We also remember, that the longitudinal optical (LO) phonon does not interact with the electromagnetic field. For a phonon-electromagnetic interaction, we require that the electric field be transverse to the direction of propagation.

With regard to the *negative solution* of Eq. {eq}`eq-p2-ch10-29`, we expand the square root term in Eq. {eq}`eq-p2-ch10-29` to obtain:

```{math}
:label: eq-p2-ch10-32
\omega^2 = \frac{\omega_T^2K^2c^2}{\omega_T^2\varepsilon_0 + c^2K^2}
```

or

```{math}
:label: eq-p2-ch10-33
\omega^2 \simeq \frac{c^2K^2}{\varepsilon_0}
```

yielding the photon-like mode with a linear $K$ dependence

```{math}
:label: eq-p2-ch10-34
\omega = \frac{cK}{\sqrt{\varepsilon_0}} \quad \text{for } \omega \ll \omega_T.
```

At large $K$ values ($|K| \sim 10^5\,$cm$^{-1}$), we solve the quadratic equation given by Eq. {eq}`eq-p2-ch10-29` in the large $K$ limit and obtain positive and negative solutions. Using a binomial expansion for Eq. {eq}`eq-p2-ch10-29`, we obtain the following positive and negative solutions. For the positive solution, i.e., $K$ large, we obtain

```{math}
:label: eq-p2-ch10-35
\omega^2 \simeq \frac{1}{\varepsilon_\infty}(\omega_T^2\varepsilon_0 + c^2K^2) = \frac{c^2K^2}{\varepsilon_\infty}.
```

This is clearly the photon-like mode, since

```{math}
:label: eq-p2-ch10-36
\omega = \frac{cK}{\sqrt{\varepsilon_\infty}} \quad \text{for } \omega \gg \omega_T.
```

This result is almost identical to Eq. {eq}`eq-p2-ch10-34` obtained in the low $K$ limit, except that now we have $\varepsilon_\infty$ instead of $\varepsilon_0$. Correspondingly, the phonon-like mode for large $K$ arises from the negative solution:

```{math}
:label: eq-p2-ch10-37
\omega^2 \simeq \frac{\omega_T^2K^2c^2}{\omega_T^2\varepsilon_0 + c^2K^2} \simeq \omega_T^2.
```

We have thus introduced two frequencies: $\omega_T$ and $\omega_L$ and from the definition of $\omega_L$ we obtain the Lyddane-Sachs-Teller relation

```{math}
:label: eq-p2-ch10-38
\frac{\omega_L^2}{\omega_T^2} = \frac{\varepsilon_0}{\varepsilon_\infty}.
```

Now, $\omega_T$ and $\omega_L$ have well-defined meanings with regard to the dielectric function as can be seen in Fig. {numref}`fig-p2-ch10-3`. From Eq. {eq}`eq-p2-ch10-12`, we have for the polarization due to ions and electrons:

```{math}
:label: eq-p2-ch10-39
\vec{P} = N'e\vec{r} + n\alpha\vec{E}
```

while the equation of motion, Eq. {eq}`eq-p2-ch10-8`, ($F = ma$) gives

```{math}
:label: eq-p2-ch10-40
-m\omega^2\vec{r} = -\kappa\vec{r} + e\vec{E}
```

yielding

```{math}
:label: eq-p2-ch10-41
\vec{r} = \frac{e\vec{E}}{\kappa - m\omega^2} = \frac{e\vec{E}/m}{\omega_T^2 - \omega^2}
```

so that

```{math}
:label: eq-p2-ch10-42
\frac{P}{E} = \frac{\varepsilon(\omega) - 1}{4\pi} = \frac{N'e^2/m}{\omega_T^2 - \omega^2} + \frac{\varepsilon_\infty - 1}{4\pi},
```

since the electronic polarizability term is $n\alpha = (\varepsilon_\infty - 1)/4\pi$. We therefore obtain:

```{math}
:label: eq-p2-ch10-43
\varepsilon(\omega) = \varepsilon_\infty + \frac{4\pi N'e^2/m}{\omega_T^2 - \omega^2}
```

where $\varepsilon_\infty$ represents the contribution from the electronic polarizability and the resonant term represents the lattice contribution. Neglecting damping, we have the result $|\varepsilon(\omega)| \to \infty$ as $\omega \to \omega_T$, where the transverse optical phonon frequency $\omega = \omega_T$ is interpreted as the frequency at which the dielectric function $\varepsilon(\omega)$ is resonant. The name *reststrahl* frequency denotes that frequency $\omega_T$ where light is maximally absorbed by the medium.

We would now like to get a more physical idea about $\omega_\ell$. So far $\omega_\ell$ has been introduced as the phonon mode of the polariton curve in Fig. {numref}`fig-p2-ch10-3` near $k = 0$. From Eq. {eq}`eq-p2-ch10-43` we have the relation

```{math}
:label: eq-p2-ch10-44
\varepsilon_0 = \varepsilon_\infty + \frac{4\pi N'e^2}{m\omega_T^2}
```

where $\varepsilon_0$ is defined by $\varepsilon_0 \equiv \varepsilon(\omega = 0)$, so that

```{math}
:label: eq-p2-ch10-45
\frac{4\pi N'e^2}{m} = \omega_T^2(\varepsilon_0 - \varepsilon_\infty)
```

and $\omega_t = \omega_T$ is the frequency where $\varepsilon(\omega)$ is resonant. Thus from Eqs. {eq}`eq-p2-ch10-1` and {eq}`eq-p2-ch10-43`, we can write

```{math}
:label: eq-p2-ch10-46
\varepsilon(\omega) = \varepsilon_\infty + \frac{(\varepsilon_0 - \varepsilon_\infty)}{(1 - \omega^2/\omega_t^2)} = \varepsilon_\infty + \frac{(\varepsilon_0 - \varepsilon_\infty)}{(1 - \omega^2/\omega_T^2)}
```

so that $\omega_T = \omega_t$. We define $\omega_\ell$ as the frequency at which the dielectric function vanishes $\varepsilon(\omega_\ell) \equiv 0$ so that setting $\varepsilon(\omega) = 0$ in Eq. {eq}`eq-p2-ch10-46` yields

```{math}
:label: eq-p2-ch10-47
\varepsilon_\infty = \frac{(\varepsilon_\infty - \varepsilon_0)}{(1 - \omega_\ell^2/\omega_t^2)}
```

or

```{math}
:label: eq-p2-ch10-48
\frac{\omega_\ell^2}{\omega_t^2} = \frac{\varepsilon_0}{\varepsilon_\infty}.
```

Thus, the frequency $\omega_\ell$, which yields a zero in the dielectric function, also satisfies the Lyddane-Sachs-Teller relation (Eq. {eq}`eq-p2-ch10-48`).

We illustrate the properties of $\omega_\ell$ and $\omega_t$ in Fig. {numref}`fig-p2-ch10-4` where we see that the frequency dependence of the dielectric function $\varepsilon(\omega)$ has two special features:

- a zero of $\varepsilon(\omega)$ occurring at $\omega_\ell$
- an infinity or pole of $\varepsilon(\omega)$ occurring at $\omega_t$.

:::{figure} images/fig-p2-ch10-4.png
:name: fig-p2-ch10-4
:width: 60%
:align: center
Fig. 10.4: The dielectric function $\varepsilon(\omega)$ plotted as a function of normalized frequency $\omega/\omega_T$. When damping is included, the real part of the dielectric function remains finite at $\omega_T$.
:::

For $\omega_t < \omega < \omega_\ell$, the dielectric function $\varepsilon(\omega)$ is negative, so that losses must occur and transmission is consequently poor. The frequency difference between the two characteristic frequencies $\omega_t$ and $\omega_\ell$ depends on the ionicity of the crystal. Thus, predominantly covalent materials like InSb which have weak ionicity have a smaller $\omega_\ell - \omega_t$ splitting than alkali halide crystals which are highly ionic. For weakly polar materials like InSb, the treatment of the electric field given here is adequate. For highly polar materials, one must also consider the local fields, as distinct from the applied field. These local fields tend to increase the separation between $\omega_t$ and $\omega_\ell$, pulling $\omega_t$ to low frequencies. Since mechanically hard materials tend to have high Debye temperatures and high phonon frequencies, the passage of $\omega_t$ toward zero for ferroelectric materials (extremely high dielectric function and capable of spontaneous polarization) is referred to as the appearance of a "soft mode".

The Lyddane-Sachs-Teller relation is more general than the derivation given here would imply. This relation can be extended to cover anisotropic materials with any number of optical modes. In this context we can write the frequency dependence of the symmetrized dielectric tensor function associated with symmetry $\mu$ as

```{math}
:label: eq-p2-ch10-49
\varepsilon_\mu(\omega) = \varepsilon_\mu(\infty) + \sum_{j=1}^{p} \frac{f_{\mu,j}\omega_{T,j}^2}{\omega_{T,j}^2 - \omega^2 - i\gamma_j\omega}
```

where $f_{\mu,j}$ is the oscillator strength, $\gamma_j$ is the damping of mode $j$, and $p$ is the number of modes with symmetry $\mu$. An example where this would apply is the case of tetragonal symmetry where $\mu$ could refer to the in-plane modes ($E_u$ symmetry) or to the out-of-plane modes ($A_{2u}$ symmetry). Figure {numref}`fig-p2-ch10-5` shows the measured reflectivity for the lattice modes of TeO$_2$ which has 4 formula units per unit cell (12 atoms/unit cell) can be described by a model based on Eq. {eq}`eq-p2-ch10-49` for polarization of the electromagnetic field parallel and perpendicular to the tetragonal axis.

:::{figure} images/fig-p2-ch10-5.png
:name: fig-p2-ch10-5
:width: 70%
:align: center
Fig. 10.5: Reflectivity in paratelluride, TeO$_2$, for (a) $\vec{E}$ parallel and (b,c) perpendicular to the tetragonal axis at 295 K (b). The polarization $\vec{E} \parallel$ the tetragonal axis has only the $A_{2u}$ modes allowed whereas for $\vec{E} \perp$ the tetragonal axis has only the $E_{2u}$ modes allowed. The points are experimental and the solid line is a model based on Eq. {eq}`eq-p2-ch10-49`. (After Korn, et al., Phys. Rev. B8, 768 (1973).)
:::

Setting the damping terms in Eq. {eq}`eq-p2-ch10-49` to zero, $\gamma_j = 0$, we obtain the result

```{math}
:label: eq-p2-ch10-50
\frac{\varepsilon(\omega)}{\varepsilon(\infty)} = \prod_{j=1}^{p} \left(\frac{\omega_{L,j}^2 - \omega^2}{\omega_{T,j}^2 - \omega^2}\right)
```

which leads to the generalized Lyddane-Sachs-Teller relation

```{math}
:label: eq-p2-ch10-51
\frac{\varepsilon_0}{\varepsilon_\infty} = \frac{\varepsilon(0)}{\varepsilon(\infty)} = \prod_{j=1}^{p} \left(\frac{\omega_{L,j}^2}{\omega_{T,j}^2}\right).
```

Equation {eq}`eq-p2-ch10-51` can be generalized for anisotropic crystals by writing Eq. {eq}`eq-p2-ch10-50` for each component, keeping in mind that the optical selection rules differ for each component. The dependence of the reflectivity on polarization and on temperature is illustrated for the tetragonal crystal TeO$_2$ in Fig. {numref}`fig-p2-ch10-5`.

To find the LO and TO modes associated with Eq. {eq}`eq-p2-ch10-49`, we would look for zeros and poles of the dielectric function for a general direction of light propagation. For example, in a tetragonal crystal we can write

```{math}
:label: eq-p2-ch10-52
\varepsilon(\theta,\omega) = \frac{\varepsilon_\parallel(\omega)\varepsilon_\perp(\omega)}{\varepsilon_\parallel(\omega)\cos^2\theta + \varepsilon_\perp(\omega)\sin^2\theta}.
```

The observation of LO and TO phonon frequencies by optical measurements is made using two basically different techniques. In one approach, we make absorption, reflection or transmission measurements, while in the other approach, light scattering measurements are made. These are often complementary methods for the following reason. Many important crystals have inversion symmetry (e.g., the NaCl structure). In this case, the phonon modes are purely odd or purely even. If the odd parity modes have dipole moments and couple directly to the electromagnetic fields, then they are infrared active. On the other hand, the even parity modes are not infrared active but instead may be Raman active and can be observed in a light scattering experiment. Thus, by doing both infrared absorption and Raman scattering measurements we can find both even and odd parity optical phonon modes, except for the silent modes which because of other symmetry requirements are neither infrared nor Raman active. These concepts are discussed in detail in the group theory course.

In modeling the phonon and free carrier contributions to the dielectric function it can happen that these phenomena occur over a common frequency range. In this case, we write the complex dielectric function for an isotropic semiconductor as follows in analyzing optical data

```{math}
:label: eq-p2-ch10-53
\frac{\varepsilon_\mu(\omega)}{\varepsilon_\mu(\infty)} = \left(1 - \frac{\omega_p^2}{\omega(\omega + i\gamma_p)}\right) + \sum_{j=1}^{p} \frac{\omega_{L,j}^2 - \omega_{T,j}^2}{\omega_{T,j}^2 - \omega^2 - i\omega\gamma_j}
```

where the first and second terms are, respectively, the free carrier and the infrared-active phonon contributions to the dielectric function. In Eq. {eq}`eq-p2-ch10-53`, $\omega_p$ is the screened electronic plasma frequency ($\omega_p^2 = 4\pi n e^2/m^*\varepsilon(\infty)$, and $\varepsilon(\infty)$ is the core dielectric constant used to approximate the higher frequency electronic polarizability). The phonon contribution to Eq. {eq}`eq-p2-ch10-53` depends on $\omega_{L,j}$ and $\omega_{T,j}$ which are the $j$-th longitudinal and transverse optic mode frequencies, while $\gamma_j$ and $\gamma_p$ are the phonon and plasma damping factors, respectively.

The model given by Eq. {eq}`eq-p2-ch10-53` can, for example, be used to model the optical properties of the anisotropic compound La$_2$CuO$_4$ which becomes a high $T_c$ superconductor, upon addition of a small concentration of Sr. In this case it is important to obtain polarized reflectivity measurements on oriented single crystals, and to carry out the Kramers-Kronig analysis of reflectivity data for each of the polarization components separately.

## 10.4 Light Scattering

Light scattering techniques provide an exceedingly useful tool to study fundamental excitations in solids, such as phonons, because light can be scattered from solids inelastically, whereby the incident and scattered photons have different frequencies. Inelastic light scattering became an important tool for the study of excitations in solids in the mid-1960's with the advent of laser light sources, because the inelastically scattered light is typically only $\sim 10^{-7}$ of the intensity of the incident light.

In the light scattering experiments shown schematically in Fig. {numref}`fig-p2-ch10-6`, conservation of energy gives:

```{math}
:label: eq-p2-ch10-54
\omega = \omega_0 \pm \omega_q
```

and conservation of momentum gives:

```{math}
:label: eq-p2-ch10-55
\vec{K} = \vec{K}_0 \pm \vec{q}
```

where the "0" subscript refers to the incident light, $\vec{K}$ refers to the wave vector of the light and "$\vec{q}$" refers to the wave vector for the excitation in the solid. Since $K_0 = 2\pi/\lambda$ is very small compared with the Brillouin zone dimensions, measurement of the angular dependence of $\omega_q(\vec{q})$ can then be used to provide dispersion relations for the excitations near $\vec{q} = 0$. If $\omega_q \ll \omega_0$, then $|\vec{K}| \simeq |\vec{K}_0|$, and we have $|q| \simeq 2|\vec{K}_0|\sin(\theta/2)$ so that $|q_{max}| = 2K_0$.

:::{figure} images/fig-p2-ch10-6.png
:name: fig-p2-ch10-6
:width: 80%
:align: center
Fig. 10.6: Raman scattering of a photon showing both phonon emission (Stokes) and absorption (anti-Stokes) processes. The scattering process is called Brillouin scattering when an acoustic phonon is involved and polariton (Raman) scattering when an optical phonon is involved. Similar processes occur with magnons, plasmons or any other excitation of the solid with the correct symmetry.
:::

If the excitation is an **acoustic** phonon, the inelastic light scattering process is called **Brillouin scattering**, while light scattering by **optical** phonons is called **Raman scattering**. Raman and Brillouin scattering also denote light scattering processes due to other elementary excitations in solids.

The light scattering can be understood on the basis of classical electromagnetic theory. When an electric field $\vec{E}$ is applied to a solid, a polarization $\vec{P}$ results

```{math}
:label: eq-p2-ch10-56
\vec{P} = \overset{\leftrightarrow}{\alpha} \cdot \vec{E}
```

where $\overset{\leftrightarrow}{\alpha}$ is the polarizability tensor of the atom in the solid, indicating that the positive charge moves in one direction and the negative charge in the opposite direction under the influence of the applied field. In the light scattering experiments, the electric field is oscillating at an optical frequency $\omega_0$

```{math}
:label: eq-p2-ch10-57
\vec{E} = \vec{E}_0 \sin\omega_0 t.
```

The lattice vibrations in the solid modulate the polarizability of the atoms themselves

```{math}
:label: eq-p2-ch10-58
\alpha = \alpha_0 + \alpha_1 \sin\omega_q t.
```

so that the polarization which is induced by the applied electric field is:

```{math}
:label: eq-p2-ch10-59
\begin{aligned}
\vec{P} &= \vec{E}_0(\alpha_0 + \alpha_1 \sin\omega_q t)\sin\omega_0 t \\
&= \vec{E}_0\left[\alpha_0\sin(\omega_0 t) + \tfrac{1}{2}\alpha_1\cos(\omega_0 - \omega_q)t - \tfrac{1}{2}\alpha_1\cos(\omega_0 + \omega_q)t\right].
\end{aligned}
```

Thus we see in Fig. {numref}`fig-p2-ch10-7` that light will be scattered elastically at frequency $\omega_0$ (Raleigh scattering) and also inelastically, being modulated downward by the natural vibration frequency $\omega_q$ of the atom (Stokes process) or upward by the same frequency $\omega_q$ (anti-Stokes process).

:::{figure} images/fig-p2-ch10-7.png
:name: fig-p2-ch10-7
:width: 70%
:align: center
Fig. 10.7: Schematic diagram of light scattering spectrum showing the central unshifted Rayleigh line, the up-shifted anti-Stokes line (emission process), and the downshifted Stokes line (absorption process). The ratio of the Stokes to anti-Stokes can be used to estimate the temperature of the phonon system.
:::

The light scattering process can also be viewed from a quantum mechanical perspective. If the "system" is initially in a state $E''$, then light scattering can excite the "system" to a higher energy state $E'$ shown in Fig. {numref}`fig-p2-ch10-8`a by absorption of an excitation energy $(E' - E'')$. Similarly, the "system" can initially be in a state $E'$ and light scattering can serve to bring the system to a final state of lower energy $E''$ by emission of an excitation of energy $(E' - E'')$ as shown in Fig. {numref}`fig-p2-ch10-8`b. The matrix element of the polarization vector between initial and final states is written (when expressed in terms of quantum mechanics) as

```{math}
:label: eq-p2-ch10-60
\vec{P}_{nm} = \int \Psi_n^* \vec{P} \Psi_m d^3r = \vec{E} \cdot \int \Psi_n^* \overset{\leftrightarrow}{\alpha} \Psi_m d^3r
```

where the polarizability $\overset{\leftrightarrow}{\alpha}$ is a second rank symmetrical tensor. The Stokes and anti-Stokes processes arise from consideration of the phase factors in this matrix element: $\Psi_m$ has a phase factor $e^{-iE_m t/\hbar}$ while $\Psi_n^*$ has a phase factor $e^{+iE_n t/\hbar}$. The polarizability tensor has a phase factor $e^{\pm i\omega_q t}$ so that the integration implied by Eq. {eq}`eq-p2-ch10-60` yields

```{math}
:label: eq-p2-ch10-61
E_m - E_n \pm \hbar\omega_q = 0.
```

:::{figure} images/fig-p2-ch10-8.png
:name: fig-p2-ch10-8
:width: 70%
:align: center
Fig. 10.8: Schematic energy level diagram for the (a) Stokes and (b) anti-Stokes processes. In this figure the solid lines denote real processes and the dashed lines virtual processes.
:::

We should remember that the optical absorption process is governed by the **momentum** matrix element which is a radial vector. Of particular significance is the case of a crystal with inversion symmetry whereby the momentum operator is an odd function, but the polarizability tensor is an even function. This characteristic feature has an important consequence; namely electronic absorption processes are sensitive to transitions between states of opposite parity (parity meaning even or odd), while light scattering is sensitive to transitions between states of similar parity. For this reason, light scattering and optical absorption are considered to be complementary spectroscopies, and together form basic tools for the study of the optical properties of elementary excitations in solids.

It is important to draw a clear distinction between Raman scattering and fluorescence. In Raman scattering, the intermediate states shown in Fig. {numref}`fig-p2-ch10-8`a,b are "virtual" states and don't have to correspond to eigenstates of the physical "system" -- any optical excitation frequency will in principle suffice. In fluorescence, on the other hand, the optical excitation state must be a real state of the system and in this case a real absorption of light occurs, followed by a real emission at a different frequency.

The major reason why these two processes are sometimes confused is that Raman scattering in solids often has a much higher intensity when $\hbar\omega_0$ is equal to an energy band gap and this effect is called resonant Raman scattering. In such cases, the fluorescent emission differs from the Raman process because fluorescent phenomena take a finite time to occur.

Typical Raman traces are shown in Fig. {numref}`fig-p2-ch10-9` for several III-V compound semiconductors. The laser wavelength is $1.06\,\mu$m (Nd:YAG laser) which is a photon energy below the band gap for each material. The scattered light is collected at 90° with respect to the incident light and both the LO and TO phonon modes at $\vec{q} = 0$ are observed. For the case of the group IV semiconductors there is no LO-TO splitting and only a single optical Raman-allowed mode is observed (at 519 cm$^{-1}$ for Si). What is measured in Fig. {numref}`fig-p2-ch10-9` is the frequency shift between the incident and scattered light beams. For the range of phonon wave vectors where Raman scattering can be carried out, this technique is the most accurate method available for the measurement of the dispersion relations near the Brillouin zone center.

:::{figure} images/fig-p2-ch10-9.png
:name: fig-p2-ch10-9
:width: 80%
:align: center
Fig. 10.9: Raman spectra of three zinc-blende-type semiconductors showing the TO and LO phonons in both Stokes and anti-Stokes scattering.
:::

By doing the Raman scattering experiment with polarized light, it is possible to get information on the symmetry of the lattice vibrations by monitoring the polarization of both the incident and scattered radiation. This approach is important in the identification of phonon frequencies with specific lattice normal modes.

The inelastic neutron scattering technique, though less accurate than Raman scattering, has the advantage of providing information about phonons throughout the Brillouin zone. By using neutrons of low energy (thermal neutrons), it is possible to make the neutron wavelengths comparable to the lattice dimensions, in which case the inelastic scattering by a lattice vibration can cause a large momentum transfer to the neutron.

## 10.5 Feynman Diagrams for Light Scattering

Feynman diagrams are useful for keeping track of various processes that may occur in an inelastic scattering process that absorbs or creates an excitation. The basic notation used in drawing Feynman diagrams consists of propagators such as electrons, phonons or photons and vertices where interactions occur, as shown in Fig. {numref}`fig-p2-ch10-10`g.

The rules in drawing Feynman diagrams are:

- Excitations such as photon, phonons and electron-hole pairs in Raman scattering are represented by lines (or propagators) as shown in Fig. {numref}`fig-p2-ch10-10`g. These propagators can be labeled with properties of the excitations, such as their wavevectors, frequencies and polarizations.
- The interaction between two excitations is represented by an intersection of their propagators. This intersection is known as a *vertex* and is sometimes highlighted by a symbol such as a filled circle or empty rectangle.
- Propagators are drawn with an arrow to indicate whether they are created or annihilated in an interaction. Arrows pointing towards a vertex represent excitations which are annihilated. Those pointing away from the vertex are created.
- When several interactions are involved they are always assumed to proceed sequentially from the left to the right as a function of time.
- Once a diagram has been drawn for a certain process, other possible processes are derived by permuting the time order in which the vertices occur in this diagram.

The basic diagram for the Raman process is given in Fig. {numref}`fig-p2-ch10-10`a taken from the Yu and Cardona book on "Fundamentals of Semiconductors." The other permutations of (a) obtained by different orders of the vertices are given in Figs. {numref}`fig-p2-ch10-10`b-f. We then use the Fermi Golden rule for each diagram, multiplying the contributions from each vertex. For example, the first vertex in Fig. {numref}`fig-p2-ch10-10`a contributes a term to the scattering probability per unit time of the form

$$
\frac{\langle n|\mathcal{H}_{eR}(\omega_i)|i\rangle}{[\hbar\omega_i - (E_n - E_i)]}
$$

where the sign $(+)$ corresponds to absorption and $(-)$ to emission and $\mathcal{H}_{eR}(\omega_i)$ denotes the interaction between the electron and the electromagnetic radiation field. The interaction for the second vertex $\mathcal{H}_{e-\mathrm{ion}}(\omega_i)$ between the electron and the lattice vibrations of the ion (or the electron-phonon interaction) and the corresponding energy denominator is

$$
\hbar\omega_i - (E_n - E_i) - \hbar\omega_q - (E_{n'} - E_n) = [\hbar\omega_i - \hbar\omega_q - (E_{n'} - E_i)]
$$

and for the third vertex the denominator becomes $[\hbar\omega_i - \hbar\omega_q - \hbar\omega_s - (E_{n'} - E_i)]$ but since the initial and final electron energies are the same, energy conservation requires $\delta(\hbar\omega_i - \hbar\omega_q - \hbar\omega_s)$ to yield the probability per unit time for Raman scattering for diagram (a):

```{math}
:label: eq-p2-ch10-62
\begin{aligned}
P_{\rm ph}(\omega_s) = \biggl(\frac{2\pi}{\hbar}\biggr) \biggl|\sum_{n,n'} \frac{\langle i|\mathcal{H}_{eR}(\omega_s)|n'\rangle\langle n'|\mathcal{H}_{e-\mathrm{ion}}|n\rangle\langle n|\mathcal{H}_{eR}(\omega_i)|i\rangle}{[\hbar\omega_i - (E_n - E_i)][\hbar\omega_i - \hbar\omega_q - (E_{n'} - E_i)]}\biggr|^2 \\
\times \delta(\hbar\omega_i - \hbar\omega_q - \hbar\omega_s).
\end{aligned}
```

Then summing over the other 5 diagrams yields the result

```{math}
:label: eq-p2-ch10-63
\begin{aligned}
P_{\rm ph}(\omega_s) = \biggl(\frac{2\pi}{\hbar}\biggr) \biggl| & \sum_{n,n'} \frac{\langle i|\mathcal{H}_{eR}(\omega_i)|n\rangle\langle n|\mathcal{H}_{e-\mathrm{ion}}|n'\rangle\langle n'|\mathcal{H}_{eR}(\omega_s)|i\rangle}{[\hbar\omega_i - (E_n - E_i)][\hbar\omega_i - \hbar\omega_q - (E_{n'} - E_i)]} \\
& + \frac{\langle i|\mathcal{H}_{eR}(\omega_i)|n\rangle\langle n|\mathcal{H}_{eR}(\omega_s)|n'\rangle\langle n'|\mathcal{H}_{e-\mathrm{ion}}|i\rangle}{[\hbar\omega_i - (E_n - E_i)][\hbar\omega_i - \hbar\omega_q - (E_{n'} - E_i)]} \\
& + \frac{\langle i|\mathcal{H}_{eR}(\omega_s)|n\rangle\langle n|\mathcal{H}_{e-\mathrm{ion}}|n'\rangle\langle n'|\mathcal{H}_{eR}(\omega_i)|i\rangle}{[-\hbar\omega_s - (E_n - E_i)][-\hbar\omega_s - \hbar\omega_q - (E_{n'} - E_i)]} \\
& + \frac{\langle i|\mathcal{H}_{eR}(\omega_s)|n\rangle\langle n|\mathcal{H}_{eR}(\omega_i)|n'\rangle\langle n'|\mathcal{H}_{e-\mathrm{ion}}|i\rangle}{[-\hbar\omega_s - (E_n - E_i)][-\hbar\omega_s + \hbar\omega_i - (E_{n'} - E_i)]} \\
& + \frac{\langle i|\mathcal{H}_{e-\mathrm{ion}}|n\rangle\langle n|\mathcal{H}_{eR}(\omega_i)|n'\rangle\langle n'|\mathcal{H}_{eR}(\omega_s)|i\rangle}{[-\hbar\omega_q - (E_n - E_i)][-\hbar\omega_q + \hbar\omega_i - (E_{n'} - E_i)]} \\
& + \frac{\langle i|\mathcal{H}_{e-\mathrm{ion}}|n\rangle\langle n|\mathcal{H}_{eR}(\omega_s)|n'\rangle\langle n'|\mathcal{H}_{eR}(\omega_i)|i\rangle}{[-\hbar\omega_q - (E_n - E_i)][-\hbar\omega_q - \hbar\omega_s - (E_{n'} - E_i)]}\biggr|^2 \\
& \times \delta(\hbar\omega_i - \hbar\omega_s - \hbar\omega_q).
\end{aligned}
```

:::{figure} images/fig-p2-ch10-10.png
:name: fig-p2-ch10-10
:width: 70%
:align: center
Fig. 10.10: Feynman diagrams for the six scattering processes that contribute to one-phonon (Stokes) Raman scattering. (Taken from Yu and Cardona.) (g) Symbols used in drawing Feynman diagrams to represent Raman scattering.
:::

Although Eq. {eq}`eq-p2-ch10-63` is not generally used to calculate scattering intensities directly, Feynman diagrams similar to those in Fig. {numref}`fig-p2-ch10-10` are widely used in physics.

## 10.6 Raman Spectra in Quantum Wells and Superlattices

Raman spectroscopy has also been used to study quantum well and superlattice phenomena. One important example is the use of Raman spectroscopy to elucidate zone folding phenomena in the phonon branches of a superlattice of quantum wells. Since the Raman effect is highly sensitive to phonon frequencies, this technique can be used to characterize quantum wells and superlattices with regard to the composition of an alloy constituent (e.g., the composition $x$ of an alloy such as Si$_x$Ge$_{1-x}$). The Raman effect can then be used to determine the amount of strain in each constituent from measurement of the phonon frequencies.

Zone folding effects in the phonon dispersion relations are demonstrated in a superlattice of [GaAs (13.6 Å)/AlAs (11.4 Å)] $\times$ 1720 periods. The observed Raman spectra are shown in Figs. {numref}`fig-p2-ch10-11`a and (b), demonstrating the zone folding of the LA branch. The difference in the force constants between the GaAs and AlAs constituents causes splittings of the zone-folded phonon branch, as shown in Fig. {numref}`fig-p2-ch10-11`c. The peaks in the Raman spectrum at $\sim$64 cm$^{-1}$ and $\sim$ 66 cm$^{-1}$ are identified and labeled with the zone folded modes of the LA branch with symmetries $A_1^{(1)}$ and $B_2^{(1)}$, consistent with the polarization of the incident and scattered photons. At higher frequencies the Raman spectrum of Fig. {numref}`fig-p2-ch10-11`a shows additional structure related to the zone folded LO phonon branch. Here we note that the normally three-fold levels of $T$ symmetry of the cubic crystal are split into $E$ and $B_2$ symmetries in the superlattice because of its lower tetragonal symmetry. The two-fold level of $E$ symmetry can be further split by the LO-TO splitting which occurs in ionic solids.

:::{figure} images/fig-p2-ch10-11.png
:name: fig-p2-ch10-11
:width: 80%
:align: center
Fig. 10.11: (a) Raman spectra of a superlattice consisting of 1720 periods of a 13.6 Å GaAs quantum well and a 11.4 Å AlAs barrier. The polarizations for the incident and scattered light are arranged so that only longitudinal phonons are observed. (b) Dispersion of the LA phonons in the superlattice. (c) An expanded view of the 65 cm$^{-1}$ region of the zone folded LA branch near $\vec{k} \approx 0$. (C. Colvard, T.A. Grant, M.V. Klein, R. Merlin, R. Fischer, H. Morkoc and A.C. Gossard, *Phys. Rev.* B31, 2080 (1985).)
:::

As another example, Raman spectroscopy can be used as a compositional characterization technique to confirm the chemical composition of a semiconductor alloy. This characterization is based on the identification of the Raman-active modes and the measurement of their frequency shifts and their relative intensities. The strain induced by the lattice mismatch at the interface between Si$_{0.5}$Ge$_{0.5}$ and a GaAs (110) surface is responsible for the dependence of the frequency shifts of the Ge-Ge, Si-Si and Si-Ge phonon lines on the thickness of the quantum wells in the spectra shown in Fig. {numref}`fig-p2-ch10-12` for Si$_{0.5}$Ge$_{0.5}$ layers of various thicknesses on a GaAs (110) surface. Since phonon frequencies depend on $(K/M)^{1/2}$ (where $K$ is the force constant and $M$ is the ion mass) the mode frequencies of the Ge-Ge, Ge-Si and Si-Si optical mode vibrations are very different as seen in Fig. {numref}`fig-p2-ch10-12`. Therefore the amount of interface strain can be sensitively monitored by Raman scattering. Note the disappearance of the GaAs Raman lines (associated with the substrate) as the thickness of the Si$_{0.5}$Ge$_{0.5}$ overlayer increases.

:::{figure} images/fig-p2-ch10-12.png
:name: fig-p2-ch10-12
:width: 70%
:align: center
Fig. 10.12: Raman spectra for various thicknesses of Si$_{0.5}$Ge$_{0.5}$ on an GaAs (110) substrate. Here the dependence of the Si-Si, Ge-Ge, and Si-Ge bond lengths on the thickness of the Si$_{0.5}$Ge$_{0.5}$ layer can readily be seen. The samples were grown at 720 K and the measurements were made at 80 K using a laser with a wavelength of 457.9 nm. (G. Abstreiter, H. Brugger, T. Wolf, H. Jorke and H.J. Herzog, *Phys. Rev. Lett.* 54, 2441 (1985).)
:::
