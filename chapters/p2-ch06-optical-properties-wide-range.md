---
title: "6 Optical Properties of Solids Over a Wide Frequency Range"
abstract: "The Kramers–Kronig relations that connect the real and imaginary parts of the dielectric function are derived from causality and linear response. Their use in extracting ε₁(ω) and ε₂(ω) from reflectivity data is illustrated for germanium, and the band-structure information contained in the optical constants is discussed. Modulated reflectivity spectroscopy, which emphasizes critical points, and ellipsometry, which measures the optical constants directly, are then described."
---

# 6 Optical Properties of Solids Over a Wide Frequency Range

## 6.0 Overview

This chapter deals with the optical response of a solid over a wide frequency range, where the absorption coefficient is too large for transmission techniques to be useful and reflectivity measurements are employed instead. The key theoretical tool is the set of Kramers–Kronig relations, which follow from causality and allow the real and imaginary parts of any linear, causal response function to be determined from one another. Applied to the dielectric function and to the optical constants, these relations permit a complete determination of $\varepsilon_1(\omega)$ and $\varepsilon_2(\omega)$ from reflectivity data. The connection between the observed optical structure and the band structure of the solid is then exploited in modulated-reflectivity experiments and in ellipsometry.

## 6.1 Kramers–Kronig Relations

References

- Yu and Cardona, *Fundamentals of Semiconductors*, Springer Verlag (1996). §6.1.3 and §6.6.
- Jones and March, *Theoretical Solid State Physics*: pp. 787–793.
- Jackson, *Classical Electrodynamics*: pp. 306–312.

Measurement of the absorption coefficient (Chapter 11) gives the imaginary part of the complex index of refraction, while the reflectivity is sensitive to a complicated combination of $\varepsilon_1(\omega)$ and $\varepsilon_2(\omega)$. Thus from measurements such as $\alpha_{\text{abs}}(\omega)$ we often have insufficient information to determine $\varepsilon_1(\omega)$ and $\varepsilon_2(\omega)$ independently. However, if we know either $\varepsilon_1(\omega)$ or $\varepsilon_2(\omega)$ over a wide frequency range, then $\varepsilon_2(\omega)$ or $\varepsilon_1(\omega)$ can be determined from the Kramers–Kronig relation given by

```{math}
:label: eq-p2-ch06-1
\varepsilon_1(\omega) - 1 = \frac{2}{\pi}\,\mathcal{P}\int_0^{\infty} \frac{\omega'\,\varepsilon_2(\omega')}{\omega'^2 - \omega^2}\,d\omega'
```

and

```{math}
:label: eq-p2-ch06-2
\varepsilon_2(\omega) = -\frac{2}{\pi}\,\mathcal{P}\int_0^{\infty} \frac{\omega'\,\varepsilon_1(\omega')}{\omega'^2 - \omega^2}\,d\omega' ,
```

in which $\mathcal{P}$ denotes the principal value. The Kramers–Kronig relations are based on causality, linear response theory and the boundedness of physical observables.

The Kramers–Kronig relations relate $\varepsilon_1(\omega)$ and $\varepsilon_2(\omega)$ so that if either of these functions is known as a function of $\omega$ the other is completely determined. Because of the form of these relations (Eqs. {eq}`eq-p2-ch06-1` and {eq}`eq-p2-ch06-2`), it is clear that the main contribution to $\varepsilon_1(\omega)$ comes from the behavior of $\varepsilon_2(\omega')$ near $\omega' \approx \omega$ due to the resonant denominator in these equations. What this means is that to obtain $\varepsilon_1(\omega)$, we really should know $\varepsilon_2(\omega')$ for all $\omega'$, but it is more important to know $\varepsilon_2(\omega')$ in the frequency range about $\omega$ than elsewhere. This property is greatly exploited in the analysis of reflectivity data, where measurements are available over a finite range of $\omega'$ values. Some kind of extrapolation procedure must be used for those frequencies $\omega'$ that are experimentally unavailable. We now give a derivation of the Kramers–Kronig relations after some introductory material.

This theorem is generally familiar to electrical engineers in another context. If a system is linear and obeys causality (i.e., there is no output before the input is applied), then the real and imaginary parts of the system function are related by a Hilbert transform. Let us now apply this causality concept to the polarization in a solid resulting from the application of an optical electric field. We have the constitutive equation which defines the polarization of the solid:

```{math}
:label: eq-p2-ch06-3
\varepsilon\,\mathbf{E} = \mathbf{D} = \mathbf{E} + 4\pi\,\mathbf{P}
```

so that

```{math}
:label: eq-p2-ch06-4
\mathbf{P} = \frac{\varepsilon - 1}{4\pi}\,\mathbf{E} \equiv \alpha(\omega)\,\mathbf{E}
```

where $\alpha(\omega)$ defines the polarizability, and $\mathbf{P}$ is the polarization per unit volume or the response of the solid to an applied field $\mathbf{E}$. The polarizability $\alpha(\omega)$ in electrical engineering language is the system function

```{math}
:label: eq-p2-ch06-5
\alpha(\omega) = \alpha_r(\omega) + i\,\alpha_i(\omega)
```

in which we have explicitly written the real and imaginary parts $\alpha_r(\omega)$ and $\alpha_i(\omega)$, respectively. Let $E(t) = E_0\,\delta(t)$ be an impulse field at $t = 0$. Then from the definition of a $\delta$-function, we have:

```{math}
:label: eq-p2-ch06-6
E(t) = E_0\,\delta(t) = \frac{E_0}{\pi}\int_0^{\infty} \cos \omega t\,d\omega .
```

The response to this impulse field yields an in-phase term proportional to $\alpha_r(\omega)$ and an out-of-phase term proportional to $\alpha_i(\omega)$, where the polarization vector is given by

```{math}
:label: eq-p2-ch06-7
\mathbf{P}(t) = \frac{E_0}{\pi}\int_0^{\infty} \bigl[\alpha_r(\omega)\cos\omega t + \alpha_i(\omega)\sin\omega t\bigr]\,d\omega ,
```

in which $\alpha(\omega)$ is written for the complex polarizability (see Eq. {eq}`eq-p2-ch06-5`). Since $\mathbf{P}(t)$ obeys causality and is bounded, we find that the integral of $\alpha(\omega)e^{-i\omega t}$ is well behaved along the contour $C'$ as $R\to\infty$ and no contribution to the integral is made along the contour $C'$ in the upper half plane (see Fig. {numref}`fig-p2-ch06-1`). Furthermore, the causality condition that $\mathbf{P}(t)$ vanishes for $t < 0$ requires that $\alpha(\omega)$ have no poles in the upper half plane shown in Fig. {numref}`fig-p2-ch06-1`.

:::{figure} images/fig-p2-ch06-1.png
:name: fig-p2-ch06-1
:width: 55%
:align: center
Fig. 6.1: Contours used in evaluating the complex polarizability integral of Eq. {eq}`eq-p2-ch06-7`.
:::

To find an explicit expression for $\alpha(\omega)$ we must generate a pole on the real axis. Then we can isolate the behavior of $\alpha(\omega)$ at some point $\omega_0$ by taking the principal value of the integral. We do this with the help of Cauchy's theorem. Since $\alpha(\omega)$ has no poles in the upper half-plane, the function $[\alpha(\omega)/(\omega - \omega_0)]$ will have a single pole at $\omega = \omega_0$ (see Fig. {numref}`fig-p2-ch06-2`). If we run our contour just above the real axis, there are no poles in the upper-half plane and the integral around the closed contour vanishes:

```{math}
:label: eq-p2-ch06-8
\oint \frac{\alpha(\omega)}{\omega - \omega_0}\,d\omega = 0 .
```

Let us now consider the integral taken over the various portions of this closed contour:

```{math}
:label: eq-p2-ch06-9
\int_{C'}\frac{\alpha(\omega)}{\omega-\omega_0}\,d\omega + \int_{-R}^{\omega_0-\epsilon}\frac{\alpha(\omega)}{\omega-\omega_0}\,d\omega + \int_{C}\frac{\alpha(\omega)}{\omega-\omega_0}\,d\omega + \int_{\omega_0+\epsilon}^{R}\frac{\alpha(\omega)}{\omega-\omega_0}\,d\omega = 0 .
```

:::{figure} images/fig-p2-ch06-2.png
:name: fig-p2-ch06-2
:width: 55%
:align: center
Fig. 6.2: Contour used to evaluate Eq. {eq}`eq-p2-ch06-9`.
:::

The contribution over the contour $C'$ vanishes since $\alpha(\omega)$ remains bounded, while $1/(\omega-\omega_0) \to 0$ as $R\to\infty$ (see Fig. {numref}`fig-p2-ch06-2`). Along the contour $C$, we use Cauchy's theorem to obtain

```{math}
:label: eq-p2-ch06-10
\lim_{\epsilon\to 0}\int_C \frac{\alpha(\omega)}{\omega-\omega_0}\,d\omega = -\pi i\,\alpha(\omega_0)
```

in which $\alpha(\omega_0)$ is the residue of $\alpha(\omega)$ at $\omega = \omega_0$ and the minus sign is written because the contour $C$ is taken clockwise. We further define the principal part $\mathcal{P}$ of the integral in the limit $R\to\infty$ and $\epsilon\to 0$ as

```{math}
:label: eq-p2-ch06-11
\lim_{\substack{R\to\infty \\ \epsilon\to 0}} \left[\int_{-R}^{\omega_0-\epsilon}\frac{\alpha(\omega)}{\omega-\omega_0}\,d\omega + \int_{\omega_0+\epsilon}^{R}\frac{\alpha(\omega)}{\omega-\omega_0}\,d\omega\right] \to \mathcal{P}\int_{-\infty}^{\infty}\frac{\alpha(\omega)}{\omega-\omega_0}\,d\omega .
```

The vanishing of the integral in Eq. {eq}`eq-p2-ch06-8` thus results in the relation

```{math}
:label: eq-p2-ch06-12
\alpha_r(\omega_0) + i\,\alpha_i(\omega_0) = \frac{1}{\pi i}\,\mathcal{P}\int_{-\infty}^{\infty}\frac{\alpha_r(\omega) + i\,\alpha_i(\omega)}{\omega - \omega_0}\,d\omega .
```

Equating real and imaginary parts of Eq. {eq}`eq-p2-ch06-12`, we get the following relations which hold for $-\infty < \omega < \infty$:

```{math}
:label: eq-p2-ch06-13
\alpha_r(\omega_0) = \frac{1}{\pi}\,\mathcal{P}\int_{-\infty}^{\infty}\frac{\alpha_i(\omega)}{\omega - \omega_0}\,d\omega
```

where $\alpha_r(\omega)$ is even, and

```{math}
:label: eq-p2-ch06-14
\alpha_i(\omega_0) = -\frac{1}{\pi}\,\mathcal{P}\int_{-\infty}^{\infty}\frac{\alpha_r(\omega)}{\omega - \omega_0}\,d\omega
```

where $\alpha_i(\omega)$ is odd.

We would like to write these relations in terms of integrals over positive frequencies. We can do this by utilizing the even- and oddness of $\alpha_r(\omega)$ and $\alpha_i(\omega)$. If we now multiply the integrand by $(\omega + \omega_0)/(\omega + \omega_0)$ and make use of the even- and oddness of the integrands, we get:

```{math}
:label: eq-p2-ch06-15
\alpha_r(\omega_0) = \frac{1}{\pi}\,\mathcal{P}\int_{-\infty}^{\infty}\frac{\alpha_i(\omega)(\omega + \omega_0)}{\omega^2 - \omega_0^2}\,d\omega = \frac{2}{\pi}\,\mathcal{P}\int_0^{\infty}\frac{\omega\,\alpha_i(\omega)}{\omega^2 - \omega_0^2}\,d\omega
```

and

```{math}
:label: eq-p2-ch06-16
\alpha_i(\omega_0) = -\frac{1}{\pi}\,\mathcal{P}\int_{-\infty}^{\infty}\frac{\alpha_r(\omega)(\omega + \omega_0)}{\omega^2 - \omega_0^2}\,d\omega = -\frac{2}{\pi}\,\mathcal{P}\int_0^{\infty}\frac{\omega_0\,\alpha_r(\omega)}{\omega^2 - \omega_0^2}\,d\omega .
```

We have now obtained the Kramers–Kronig relations. To avoid explicit use of the principal value of a function, we can subtract out the singularity at $\omega_0$, by writing

```{math}
:label: eq-p2-ch06-17
\alpha_r(\omega_0) + i\,\alpha_i(\omega_0) = \frac{1}{\pi i}\int_{-\infty}^{\infty}\left[\frac{\alpha(\omega) - \alpha(\omega_0)}{\omega - \omega_0}\right]\left[\frac{\omega + \omega_0}{\omega + \omega_0}\right]d\omega .
```

Using the evenness and oddness of $\alpha_r(\omega)$ and $\alpha_i(\omega)$ we then obtain

```{math}
:label: eq-p2-ch06-18
\alpha_r(\omega_0) = \frac{2}{\pi}\int_0^{\infty}\frac{\omega\,\alpha_i(\omega) - \omega_0\,\alpha_i(\omega_0)}{\omega^2 - \omega_0^2}\,d\omega
```

and

```{math}
:label: eq-p2-ch06-19
\alpha_i(\omega_0) = -\frac{2}{\pi}\int_0^{\infty}\frac{\omega_0\,\alpha_r(\omega) - \omega_0\,\alpha_r(\omega_0)}{\omega^2 - \omega_0^2}\,d\omega .
```

To obtain the Kramers–Kronig relations for the dielectric function itself, just substitute

```{math}
:label: eq-p2-ch06-20
\varepsilon(\omega) = 1 + 4\pi\,\alpha(\omega) = \varepsilon_1(\omega) + i\,\varepsilon_2(\omega)
```

to obtain

```{math}
:label: eq-p2-ch06-21
\varepsilon_1(\omega_0) - 1 = \frac{2}{\pi}\int_0^{\infty}\frac{\omega'\,\varepsilon_2(\omega') - \omega_0\,\varepsilon_2(\omega_0)}{\omega'^2 - \omega_0^2}\,d\omega'
```

and

```{math}
:label: eq-p2-ch06-22
\varepsilon_2(\omega_0) = -\frac{2}{\pi}\int_0^{\infty}\frac{\omega_0\,\varepsilon_1(\omega') - \omega_0\,\varepsilon_1(\omega_0)}{\omega'^2 - \omega_0^2}\,d\omega' .
```

The Kramers–Kronig relations are very general and depend, as we have seen, on the assumptions of causality, linearity and boundedness. From this point of view, the real and imaginary parts of a "physical" quantity $Q$ can be related by making the identification

```{math}
:label: eq-p2-ch06-23
Q_{\text{real}} \rightarrow \alpha_r
```

and

```{math}
:label: eq-p2-ch06-24
Q_{\text{imaginary}} \rightarrow \alpha_i .
```

Thus, we can identify $\varepsilon_1(\omega) - 1$ with $\alpha_r(\omega)$, and $\varepsilon_2(\omega)$ with $\alpha_i(\omega)$. The reason, of course, why the identification $\alpha_r(\omega)$ is made with $[\varepsilon_1(\omega) - 1]$ rather than with $\varepsilon_1(\omega)$ is that if $\varepsilon_2(\omega) \equiv 0$ for all $\omega$, we want $\varepsilon_1(\omega) \equiv 1$ for all $\omega$ (the dielectric constant for free space). Thus, if we are interested in constructing a Kramers–Kronig relation for the optical constants, then we again want to make the following identification for the optical constants:

```{math}
:label: eq-p2-ch06-25
[\tilde n(\omega) - 1] \rightarrow \alpha_r(\omega)
```

and

```{math}
:label: eq-p2-ch06-26
\tilde k(\omega) \rightarrow \alpha_i(\omega) .
```

From Eqs. {eq}`eq-p2-ch06-21` and {eq}`eq-p2-ch06-22`, we can obtain the Kramers–Kronig relations for the optical constants $\tilde n(\omega)$ and $\tilde k(\omega)$:

```{math}
:label: eq-p2-ch06-27
\tilde n(\omega) - 1 = \frac{2}{\pi}\int_0^{\infty}\frac{\omega'\,\tilde k(\omega') - \omega\,\tilde k(\omega)}{\omega'^2 - \omega^2}\,d\omega'
```

and

```{math}
:label: eq-p2-ch06-28
\tilde k(\omega) = -\frac{2}{\pi}\int_0^{\infty}\frac{\omega\,\tilde n(\omega') - \omega\,\tilde n(\omega)}{\omega'^2 - \omega^2}\,d\omega' ,
```

where we utilize the definition relating the complex dielectric function $\varepsilon(\omega)$ to the optical constants $\tilde n(\omega)$ and $\tilde k(\omega)$ where $\varepsilon(\omega) = [\tilde n(\omega) + i\,\tilde k(\omega)]^2$.

It is useful to relate the optical constants to the reflection coefficient $r(\omega)\exp[i\theta(\omega)]$ defined by

```{math}
:label: eq-p2-ch06-29
r(\omega)\,e^{i\theta(\omega)} = \frac{\tilde n(\omega) - 1 + i\,\tilde k(\omega)}{\tilde n(\omega) + 1 + i\,\tilde k(\omega)}
```

in which the conjugate variables are $\ln r(\omega)$ and $\theta(\omega)$ and the reflectivity is given as $R(\omega) = r^2(\omega)$. From Eq. {eq}`eq-p2-ch06-29`, we can then write

```{math}
:label: eq-p2-ch06-30
\tilde n(\omega) = \frac{1 - r^2(\omega)}{1 + r^2(\omega) - 2r(\omega)\cos\theta(\omega)}
```

and

```{math}
:label: eq-p2-ch06-31
\tilde k(\omega) = \frac{2r(\omega)\sin\theta(\omega)}{1 + r^2(\omega) - 2r(\omega)\cos\theta(\omega)}
```

so that once $r(\omega)$ and $\theta(\omega)$ are found, the optical constants $\tilde n(\omega)$ and $\tilde k(\omega)$ are determined. In practice $r(\omega)$ and $\theta(\omega)$ are found from the reflectivity $R$ which is measured over a wide frequency range and is modeled outside the measured range. A Kramers–Kronig relation can be written for the conjugate variables $\ln r(\omega)$ and $\theta(\omega)$, from which $\theta(\omega)$ is found:

```{math}
:label: eq-p2-ch06-32
\ln r(\omega) = \frac{2}{\pi}\int_0^{\infty}\frac{\omega'\,\theta(\omega') - \omega\,\theta(\omega)}{\omega'^2 - \omega^2}\,d\omega'
```

and

```{math}
:label: eq-p2-ch06-33
\theta(\omega) = -\frac{2\omega}{\pi}\int_0^{\infty}\frac{\ln r(\omega') - \ln r(\omega)}{\omega'^2 - \omega^2}\,d\omega' ,
```

where $\ln R(\omega) = 2\ln r(\omega)$.

From a knowledge of the frequency dependent reflectivity $R(\omega)$, the reflection coefficient $r(\omega)$ and the phase of the reflectivity coefficient $\theta(\omega)$ can be found. We can then find the frequency dependence of the optical constants $\tilde n(\omega)$ and $\tilde k(\omega)$, which in turn yields the frequency dependent dielectric functions $\varepsilon_1(\omega)$ and $\varepsilon_2(\omega)$. Starting with the experimental data for the reflectivity $R(\omega)$ for germanium in Fig. {numref}`fig-p2-ch06-3`(a), the Kramers–Kronig relations are used to obtain results for $\varepsilon_1(\omega)$ and $\varepsilon_2(\omega)$ for germanium as shown in Fig. {numref}`fig-p2-ch06-3`(b).

:::{figure} images/fig-p2-ch06-3.png
:name: fig-p2-ch06-3
:width: 80%
:align: center
Fig. 6.3: (a) Frequency dependence of the reflectivity of Ge over a wide frequency range. (b) Plot of the real $[\varepsilon_1(\omega)]$ and imaginary $[\varepsilon_2(\omega)]$ parts of the dielectric functions for Ge obtained by a Kramers–Kronig analysis of the reflectivity data in part (a).
:::

The Kramers–Kronig relations for the conjugate variables $\varepsilon_1(\omega)$ and $\varepsilon_2(\omega)$; $\tilde n(\omega)$ and $\tilde k(\omega)$; and $\ln r(\omega)$ and $\theta(\omega)$ are widely used in quantitative studies of the optical properties of specific materials, as for example germanium in Fig. {numref}`fig-p2-ch06-3`.

## 6.2 Optical Properties and Band Structure

If we are interested in studying the optical properties near the band edge such as the onset of indirect transitions or of the lowest direct interband transitions, then we should carry out absorption measurements (see Chapter 5) to determine the absorption coefficient $\alpha_{\text{abs}}(\omega)$ and thus identify the type of process that is dominant (indirect, direct, allowed, forbidden, etc.) at the band edge. However, if we are interested in the optical properties of a semiconductor over a wide energy range, then we want to treat all bands and transitions within a few eV from the Fermi level on an equal footing. Away from the band edge, the absorption coefficients become too high for the absorption technique to be useful, and reflectivity measurements are made instead. Experimentally, it is most convenient to carry out reflectivity measurements at normal incidence. From these measurements, the Kramers–Kronig analysis (see §6.1) is used to get the phase angle $\theta(\omega)$ for some frequency $\omega_0$, if the reflection coefficient $r(\omega)$ is known throughout the entire range of photon energies:

```{math}
:label: eq-p2-ch06-34
\theta(\omega_0) = -\frac{2\omega_0}{\pi}\int_0^{\infty}\frac{\ln r(\omega) - \ln r(\omega_0)}{\omega^2 - \omega_0^2}\,d\omega .
```

From a knowledge of $r(\omega)$ and $\theta(\omega)$, we can then find the frequency dependence of the optical constants $\tilde n(\omega)$ and $\tilde k(\omega)$ using Eqs. {eq}`eq-p2-ch06-30` and {eq}`eq-p2-ch06-31` and the frequency dependent dielectric function

```{math}
:label: eq-p2-ch06-35
\varepsilon_1(\omega) = \tilde n^2 - \tilde k^2
```

and

```{math}
:label: eq-p2-ch06-36
\varepsilon_2(\omega) = 2\,\tilde n\,\tilde k .
```

As an example of such an analysis, let us consider the case of the semiconductor germanium. The normal incidence reflectivity is given in Fig. {numref}`fig-p2-ch06-3`(a) and the results of the Kramers–Kronig analysis described above are given for $\varepsilon_1(\omega)$ and $\varepsilon_2(\omega)$ in Fig. {numref}`fig-p2-ch06-3`(b).

Corresponding to the structure in the reflectivity, there will be structure observed in the real and imaginary parts of the dielectric function. These structures in the reflectivity data are then identified with special features in the energy band structure. It is interesting to note that the indirect transition (0.66 eV) from the $\Gamma_{25}'$ valence band to the $L_1$ conduction band (see Part I of the notes) has almost no impact on the reflectivity data. Nor does the direct band gap, which is responsible for the fundamental absorption edge in germanium, have a significant effect on the reflectivity data. These effects are small on the scale of the reflectivity structures shown in Fig. {numref}`fig-p2-ch06-3`(a) and must be looked for with great care in a narrow frequency range where structure in the absorption data is found. The big contribution to the dielectric constant comes from interband transitions $L_3' \to L_1$ for which the joint density of states is large over large volumes of the Brillouin zone. The sharp rise in $\varepsilon_2(\omega)$ at 2.1 eV is associated with the $L_3' \to L_1$ transition. For higher photon energies, large volumes of the Brillouin zone contribute until a photon energy of about 5 eV is reached. Above this photon energy, we cannot find bands that track each other closely enough to give interband transitions with intensities of large magnitude.

## 6.3 Modulated Reflectivity Experiments

If we wish to study the critical point contributions to the optical reflectivity in more detail, it is useful to carry out modulated reflectivity measurements. If, for example, a small periodic perturbation is applied to a sample then there will be a change in reflectivity at the frequency of that perturbation. The frequency dependence of this change in reflectivity is small (parts in $10^3$ or $10^4$) but it is measurable. As an example, we show in Fig. {numref}`fig-p2-ch06-4`, results for the reflectivity $R(\omega)$ and for the wavelength modulated reflectivity $(1/R)(dR/dE)$ of GaAs. Structure at $E_0$ would be identified with the direct band gap, while the structure at $E_0 + \Delta_0$ corresponds to a transition from the split-off valence band at $\mathbf{k} = 0$ which arises through the spin-orbit interaction. The transitions at $E_1$ and $E_1 + \Delta_1$ correspond to $\Lambda$ point and $L$ point transitions, also showing spin-orbit splitting. Also identified in Fig. {numref}`fig-p2-ch06-5` are the $E_0'$ transition from the $\Delta_7$ valence band to the $\Delta_6$ conduction band, and the $E_2$ transition from $X_5 \to X_5$ at the $X$ point. Although the band structure and notation given in Fig. {numref}`fig-p2-ch06-5` applies to Ge in detail, the results for other group IV and III–V semiconductors is qualitatively similar, with values for the pertinent interband transitions given in Table {numref}`tab-p2-ch06-1` for Si, Ge, GaAs, InP and GaP.

:::{figure} images/fig-p2-ch06-4.png
:name: fig-p2-ch06-4
:width: 70%
:align: center
Fig. 6.4: Reflectance and frequency modulated reflectance spectra for GaAs. (a) Room temperature reflectance spectrum and (b) the wavelength modulated spectrum $(1/R)(dR/dE)$ at 4 K (the solid curve is experimental and the broken curve is calculated using a pseudopotential band structure model). Adapted from Yu and Cardona.
:::

In the vicinity of a critical point, the denominator in the joint density of states is small, so that a small change in photon energy can produce a significant change in the joint density of states. Hence, modulation spectroscopy techniques emphasize critical points. There are a number of parameters that can be varied in these modulation spectroscopy experiments:

| Quantity modulated | Technique |
|---|---|
| electric field | electro-reflectance |
| wavelength | wavelength modulation |
| stress | piezo-reflectance |
| light intensity | photo-reflectance |
| temperature | thermo-reflectance |

The various modulated reflectivity experiments are complementary rather than yielding identical information. For example, certain structures in the reflectance respond more sensitively to one type of modulation than to another. If we wish to look at structure associated with the $L$ point (111 direction) transitions, then a stress along the (100) direction will not produce as important a symmetry change as application of stress along a (111) direction; with a stress along a (111) direction, the ellipsoid having its longitudinal axis along (111) will be affected one way while the other three ellipsoids will be affected in another way. However, stress along the (100) direction treats all ellipsoids in the same way.

:::{figure} images/fig-p2-ch06-5.png
:name: fig-p2-ch06-5
:width: 75%
:align: center
Fig. 6.5: The band structure of Ge including spin-orbit interaction and showing the various direct transitions responsible for the structures that are observed in the imaginary part of the dielectric function $\varepsilon_2(\omega)$ and in the modulated reflectivity. Although the band structure in this figure is for Ge, a similar notation is used to identify the various interband transitions in other group IV or III–V compound semiconductors (see Table {numref}`tab-p2-ch06-1`).
:::

The reason why modulation spectroscopy emphasizes critical points can be seen by the following argument. For a direct interband transition, the optical absorption coefficient has a frequency dependence

```{math}
:label: eq-p2-ch06-37
\alpha_{\text{abs}}(\omega) = C\sqrt{\frac{\hbar\omega - E_g}{\hbar\omega}} .
```

Therefore, a plot of $\alpha_{\text{abs}}(\omega)$ vs. $\hbar\omega$ exhibits a threshold [Fig. {numref}`fig-p2-ch06-6`(a)], but no singularity in the frequency plot. However, when we take the derivative of Eq. {eq}`eq-p2-ch06-37`,

```{math}
:label: eq-p2-ch06-38
\frac{\partial \alpha_{\text{abs}}(\omega)}{\partial \omega} = \frac{C\,\hbar E_g}{2\,(\hbar\omega)^{3/2}\,\sqrt{\hbar\omega - E_g}} ,
```

a sharp structure is obtained in the modulated reflectivity due to the singularity in the first term of Eq. {eq}`eq-p2-ch06-37` at $\hbar\omega = E_g$ [see Figs. {numref}`fig-p2-ch06-4` and {numref}`fig-p2-ch06-6`(b)]. If we modulate the light with any arbitrary parameter $x$, then

```{math}
:label: eq-p2-ch06-39
\frac{\partial \alpha_{\text{abs}}}{\partial x} = \frac{\partial \alpha_{\text{abs}}}{\partial \omega}\,\frac{\partial \omega}{\partial x} ,
```

and structure in the reflectivity is expected as $x$ is varied. Thus all modulation parameters can be expected to produce singularities in the optical absorption. For some variables such as stress, the modulated signal is sensitive to both the magnitude and the direction of the stress relative to the crystal axes. For thermomodulation, the spectrum is sensitive to the magnitude of the thermal pulses, but the response is independent of crystalline direction. Thermomodulation is, however, especially sensitive to transitions from and to the Fermi level.

:::{figure} images/fig-p2-ch06-6.png
:name: fig-p2-ch06-6
:width: 65%
:align: center
Fig. 6.6: (a) The frequency dependence of the optical absorption coefficient showing a threshold for interband transitions at the band gap. (b) The derivative of (a) which is measured in the modulated reflectivity shows a sharp singularity associated with the threshold energy.
:::

Thus, the various modulation techniques can be used in optical studies to obtain additional information about symmetry, which can then be used for more reliable identification of structure in the optical properties. The modulation technique specifically emphasizes interband transitions associated with particular points in the Brillouin zone. The identification of where in the Brillouin zone a particular transition is occurring is one of the most important and difficult problems in optical studies of solids. It is often not the case that we have reliable band models available to us when we start to do optical studies. For this reason, symmetry is a very powerful tool for the study of optical properties.

The high sensitivity of modulation spectroscopy provides valuable information about the band structure that would be difficult to obtain otherwise, and some examples are cited below. One example of the use of modulation spectroscopy is to determine the temperature dependence of the bandgap of a semiconductor, as shown in Fig. {numref}`fig-p2-ch06-7` for the direct $\Gamma$ point gap in Ge. This measurement takes advantage of the high resolution of modulation spectroscopy and is especially useful for measurements at elevated temperatures. Another example is the dependence of the various band separations identified in Fig. {numref}`fig-p2-ch06-5` as a function of alloy concentration $x$ in Ge$_{1-x}$Si$_x$ alloys (Fig. {numref}`fig-p2-ch06-8`). Here again the high resolution of the modulation spectroscopy is utilized. A third example is the isotope dependence of the direct absorption edge of Ge as shown in Fig. {numref}`fig-p2-ch06-9`. Modulation spectroscopy has also been applied to studying interband transitions in metals. For example, Fig. {numref}`fig-p2-ch06-10` shows modulated spectroscopy results from a gold surface taken with both the thermal modulation and piezo-reflectance techniques. The results show that transitions involving states at the Fermi level (either initial or final states) are more sensitively seen using thermal modulation because small temperature variations affect the Fermi tail of the distribution function strongly. Thus, thermo-reflectance measurements on the noble metals give a great deal of well-resolved structure, compared with electro-reflectance and piezo-reflectance measurements as illustrated in Fig. {numref}`fig-p2-ch06-10`. In this figure, we see that in gold the piezo-reflectance is much more sensitive than ordinary reflectivity measurements near 4 eV, but the thermo-reflectance technique is most powerful for transitions made to states near the Fermi level.

:::{figure} images/fig-p2-ch06-7.png
:name: fig-p2-ch06-7
:width: 65%
:align: center
Fig. 6.7: Temperature dependence of the direct gap ($E_0$) of Ge.
:::

:::{figure} images/fig-p2-ch06-8.png
:name: fig-p2-ch06-8
:width: 65%
:align: center
Fig. 6.8: Dependence of the energies of the $E_0$, $E_0 + \Delta_0$, $E_1$, $E_1 + \Delta_1$, $E_0'$, and $E_2$ electro-reflectance peaks on $x$ in the Ge$_{1-x}$Si$_x$ alloy system at room temperature.
:::

:::{figure} images/fig-p2-ch06-9.png
:name: fig-p2-ch06-9
:width: 65%
:align: center
Fig. 6.9: Photo-modulated reflectivity of Ge showing the $E_0$ direct gap at $\mathbf{k}=0$ of single crystals of nearly isotopically pure $^{70}$Ge, $^{74}$Ge, and $^{76}$Ge, at $T = 6$ K. Note the remarkable dependence of $E_0$ on isotopic composition.
:::

:::{figure} images/fig-p2-ch06-10.png
:name: fig-p2-ch06-10
:width: 75%
:align: center
Fig. 6.10: Thermo-reflectance and normal incidence reflectivity spectra of gold near liquid nitrogen temperature (from W. J. Scouler, Phys. Rev. Letters 18, 445 (1967)) together with the room temperature piezo-reflectance spectrum (M. Garfunkel, J. J. Tiemann, and W. E. Engeler, Phys. Rev. 148, 698 (1966)).
:::

:::{table} tab-p2-ch06-1
:name: tab-p2-ch06-1
Table {numref}`tab-p2-ch06-1`: The measured energies (eV) of the prominent structures in the optical spectra of some semiconductors with the diamond and zinc-blende structures. All energies are low temperature values except that of the $E_0$ transition in Si, which was measured at room temperature. (see Fig. {numref}`fig-p2-ch06-5` for a definition of $E_0, E_1, E_2$, etc.)
| Transition | Si | Ge | GaAs | InP | GaP |
|---|---|---|---|---|---|
| $E_0$ | 3.73 | 0.898 | 1.5192 | 1.4236 | 2.869 |
| $E_0 + \Delta_0$ | 3.77 | 1.184 | 1.859 | 1.532 | 2.949 |
| $E_1$ | 3.45 | 2.222 | 3.017 | 3.15 | 3.785 |
| $E_1 + \Delta_1$ | – | 2.41 | 3.245 | 3.835 | – |
| $E_0'$ | 3.378 | 3.206 | 4.488 | 4.54 | 4.77 |
| $E_0' + \Delta_0'$ | – | 3.39 | 4.659 | – | – |
| $E_2$ | 4.33 | 4.49 | 5.11 | 5.05 | 5.21 |
| $E_1'$ | 5.5 | 5.65 | 6.63 | – | 6.8 |
:::

## 6.4 Ellipsometry and Measurement of Optical Constants

Ellipsometry is a standard method for measuring the complex dielectric function or the complex optical constants $\tilde N = \tilde n + i\,\tilde k$ of a material. Since two quantities are measured in an ellipsometry measurement, $\tilde n$ and $\tilde k$ can both be determined at a single frequency. The ellipsometry measurements are usually made over a range of frequencies, especially for frequencies well above the fundamental absorption edge where semiconductors become highly absorbing. At these higher frequencies very thin samples would be needed if the method of interference fringes were used to determine $\tilde n$, which is a very simple method for measuring the wavelength in a non-absorbing medium. One drawback of the ellipsometry technique is the high sensitivity of the technique to the quality and cleanliness of the surface. Ellipsometry is limited by precision considerations to measurements on samples with absorption coefficients $\alpha_{\text{abs}} \gtrsim 1$–$10\ \text{cm}^{-1}$. Ellipsometers can be made to operate in the near infrared, visible and near ultraviolet frequency regimes, and data acquisition can be made fast enough to do real time monitoring of $\varepsilon(\omega)$.

In the ellipsometry method the reflected light with polarizations "p" (parallel) and "s" (perpendicular) to the plane of incidence [see Fig. {numref}`fig-p2-ch06-11`(a)] is measured as a function of the angle of incidence $\phi$ and the light frequency $\omega$. The corresponding reflectances $R_s = |r_s|^2$ and $R_p = |r_p|^2$ are related to the complex dielectric function $\varepsilon(\omega) = \varepsilon_1(\omega) + i\,\varepsilon_2(\omega) = (\tilde n + i\,\tilde k)^2$ by the Fresnel equations which can be derived from the boundary conditions on the fields at the interface between two surfaces with complex dielectric functions $\varepsilon_a$ and $\varepsilon_s$ as shown in Fig. {numref}`fig-p2-ch06-11`(a). From the figure the complex reflection coefficients for polarizations $s$ and $p$ are

```{math}
:label: eq-p2-ch06-40
r_s = \frac{E_s^r}{E_s^i} = \frac{\tilde N_a\cos\phi - \tilde N_s\cos\phi_t}{\tilde N_a\cos\phi + \tilde N_s\cos\phi_t}
```

and

```{math}
:label: eq-p2-ch06-41
r_p = \frac{E_p^r}{E_p^i} = \frac{\varepsilon_s\,\tilde N_a\cos\phi - \varepsilon_a\,\tilde N_s\cos\phi_t}{\varepsilon_s\,\tilde N_a\cos\phi + \varepsilon_a\,\tilde N_s\cos\phi_t}
```

in which

```{math}
:label: eq-p2-ch06-42
\tilde N_s\cos\phi_t = (\varepsilon_s - \varepsilon_a\sin^2\phi)^{1/2}
```

and $r_s$ and $r_p$ are the respective reflection coefficients, $\varepsilon_s$ and $\tilde N_s$ denote the complex dielectric function and complex index of refraction within the medium, while $\varepsilon_a$ and $\tilde N_a$ are the corresponding quantities outside the medium (which is usually vacuum or air). When linearly polarized light, that is neither $s$- nor $p$-polarized, is incident on a medium at an oblique angle of incidence $\phi$, the reflected light will be elliptically polarized. The ratio ($\sigma_r$) of the complex reflectivity coefficients $r_p/r_s \equiv \sigma_r$ is then a complex variable which is measured experimentally in terms of its phase (or the phase shift relative to the linearly polarized incident light) and its magnitude, which is the ratio of the axes of the polarization ellipse of the reflected light [see Fig. {numref}`fig-p2-ch06-11`(a)]. These are the two measurements that are made in ellipsometry. The complex dielectric function of the medium $\varepsilon_s(\omega) = \varepsilon_1(\omega) + i\,\varepsilon_2(\omega)$ can then be determined from the angle $\phi$, the complex reflectivity coefficient ratio $\sigma_r$, and the dielectric function $\varepsilon_a$ of the ambient environment using the relation

```{math}
:label: eq-p2-ch06-43
\varepsilon_s = \varepsilon_a\sin^2\phi + \varepsilon_a\sin^2\phi\,\tan^2\phi\left(\frac{1 - \sigma_r}{1 + \sigma_r}\right)^2 ,
```

and in a vacuum environment $\varepsilon_a = 1$.

The experimental set-up for ellipsometry measurements is shown in Fig. {numref}`fig-p2-ch06-11`(b). Light from a tunable light source is passed through a monochromator to select a frequency $\omega$ and the light is then polarized linearly along the direction $\mathbf{E}$ to yield the $I_s$ and $I_p$ incident light intensities. After reflection, the light is elliptically polarized along $\mathbf{E}(t)$ as a result of the phase shifts that $E_p^r$ and $E_s^r$ have each experienced. The compensator introduces a phase shift $-\theta$ which cancels the $+\theta$ phase shift induced by the reflection at the sample surface, so that the light becomes linearly polarized again as it enters the analyzer. If the light is polarized at an angle of $\pi/2$ with respect to the analyzer setting, then no light reaches the detector. Thus at every angle of incidence and every frequency, $\varepsilon(\omega, \phi)$ is determined by Eq. {eq}`eq-p2-ch06-43` from measurement of the magnitude and phase of $\sigma_r$.

:::{figure} images/fig-p2-ch06-11.png
:name: fig-p2-ch06-11
:width: 90%
:align: center
Fig. 6.11: (a) Electric field vectors resolved into $p$ and $s$ components, for light incident (i), reflected (r), and transmitted (t) at an interface between media of complex indices of refraction $\tilde N_a$ and $\tilde N_s$. The propagation vectors are labeled by $\mathbf{k}_i$, $\mathbf{k}_r$, and $\mathbf{k}_t$. (b) Schematic diagram of an ellipsometer, where P and S denote polarizations parallel and perpendicular to the plane of incidence, respectively.
:::

Another common method to determine the optical constants is by measurement of the normal incidence reflectivity over a wide frequency range and using the Kramers–Kronig analysis as discussed in §6.2 to determine the optical constants $\tilde n(\omega)$ and $\tilde k(\omega)$.
