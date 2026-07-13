---
title: "5 Absorption of Light in Solids"
abstract: "The absorption coefficient is defined and evaluated for free carrier absorption in semiconductors and metals, direct interband transitions, and indirect interband transitions involving phonons, including discussions of the Burstein shift and the Franz–Keldysh effect."
---

# 5 Absorption of Light in Solids

## 5.0 References

- Ziman, *Principles of the Theory of Solids*: Chapter 8
- Bassani and Pastori–Parravicini, *Electronic States and Optical Transitions in Solids*: chapter 5
- Yu and Cardona, *Fundamentals of Semiconductors*, Chapter 6
- Wolfe, Holonyak and Stillman, *Physical Properties of Semiconductors*, Chapter 7

## 5.1 The Absorption Coefficient

Measurement of the absorption of light is one of the most important techniques for optical measurements in solids. In the absorption measurements, we are concerned with the light intensity $I(z)$ after traversal of a thickness $z$ of material as compared with the incident intensity $I_0$, thereby defining the absorption coefficient $\alpha_{\text{abs}}(\omega)$:

```{math}
:label: eq-p2-ch05-1
I(z) = I_0 e^{-\alpha_{\text{abs}}(\omega) z}
```

where the absorption constant is shown schematically in Fig. {numref}`fig-p2-ch05-1`. Since the intensity $I(z)$ depends on the square of the field variables, it immediately follows that

```{math}
:label: eq-p2-ch05-2
\alpha_{\text{abs}}(\omega) = 2\frac{\omega \tilde{k}(\omega)}{c}
```

where the factor of 2 results from the definition of $\alpha_{\text{abs}}(\omega)$ in terms of the light intensity, which is proportional to the square of the optical fields. This expression tells us that the absorption coefficient is proportional to $\tilde{k}(\omega)$, the imaginary part of the complex index of refraction (extinction coefficient), so that $\tilde{k}$ is usually associated with power loss. We note that Eq. {eq}`eq-p2-ch05-2` applies to free carrier absorption in semiconductors in the limit $\omega\tau \gg 1$, and $\omega \gg \omega_p$.

:::{figure} images/fig-p2-ch05-1.png
:name: fig-p2-ch05-1
:width: 45%
:align: center
Fig. 5.1: Frequency dependence of the absorption coefficient near a threshold for interband transitions.
:::

We will now show that the frequency dependence of the absorption coefficient is quite different for the various physical processes which occur in the optical properties of solids. We will consider here the frequency dependence of the absorption coefficient for:

1. Free carrier absorption
   - (a) typical semiconductor $\alpha_{\text{abs}}(\omega) \sim \omega^{-2}$
   - (b) metals at low frequencies $\alpha_{\text{abs}}(\omega) \sim \omega^{1/2}$
2. Direct interband transitions
   - (a) form of absorption coefficient $\alpha_{\text{abs}}(\omega) \sim \frac{(\hbar\omega - E_g)^{1/2}}{\hbar\omega}$
   - (b) conservation of crystal momentum
   - (c) relation between $m^*$ and momentum matrix element
   - (d) form of $\alpha_{\text{abs}}(\omega)$ for direct forbidden transition $\sim \frac{(\hbar\omega - E_g)^{3/2}}{\hbar\omega}$
3. Indirect interband transitions
   - (a) form of absorption coefficient $\alpha_{\text{abs}}(\omega) \sim (\hbar\omega - E_g \pm \hbar\omega_q)^2$
   - (b) phonon absorption and emission processes

The summary given above is for 3D systems. In the case of 2D and 1D systems, the functional dependence is sensitive to the dimensionality of the system for each process.

## 5.2 Free Carrier Absorption in Semiconductors

For free carrier absorption we use the relation for the complex dielectric function $\varepsilon(\omega) = \varepsilon_1(\omega) + i\varepsilon_2(\omega)$ given by

```{math}
:label: eq-p2-ch05-3
\varepsilon(\omega) = \varepsilon_0 + \frac{4\pi i\sigma}{\omega}
```

where $\varepsilon_0$ is the core dielectric constant in the optical frequency range above the lattice mode frequencies and $\varepsilon_0$ is here assumed to be independent of $\omega$. The electronic polarizability is related to the frequency dependent electrical conductivity by the frequency dependent Drude term

```{math}
:label: eq-p2-ch05-4
\sigma = \frac{ne^2\tau}{m^*(1 - i\omega\tau)}.
```

The plasma frequency $\omega_p$ is then given by the vanishing of $\varepsilon_1(\omega)$, that is $\varepsilon_1(\omega_p) = 0$ or

```{math}
:label: eq-p2-ch05-5
\omega_p^2 = \frac{4\pi ne^2}{m^*\varepsilon_0}.
```

For semiconductors, the core dielectric constant $\varepsilon_0$ is typically a large number and the contribution due to the free carriers is small at infrared and visible frequencies. For metals, the free carrier absorption is dominant over the entire optical frequency range.

For semiconductors, the typical frequency range of interest is that above the optical phonon frequencies, and for these frequencies it is generally true that $\omega\tau \gg 1$ (see §5.2). The generic expression for $\varepsilon(\omega)$ is:

```{math}
:label: eq-p2-ch05-6
\varepsilon(\omega) = \varepsilon_0 + \frac{4\pi i n e^2 \tau (1 + i\omega\tau)}{m^*\omega[1 + (\omega\tau)^2]} = \varepsilon_0 + \frac{i\varepsilon_0\omega_p^2\tau(1+i\omega\tau)}{\omega[1+(\omega\tau)^2]}
```

which for $\omega\tau \gg 1$ becomes

```{math}
:label: eq-p2-ch05-7
\varepsilon(\omega) \simeq \varepsilon_0 + \frac{i\varepsilon_0\omega_p^2\tau^2}{\omega^3\tau^3} - \frac{\varepsilon_0\omega_p^2}{\omega^2}.
```

In the range of interest for optical measurements in a semiconductor, the relation $\omega \gg \omega_p$ is generally satisfied. It is then convenient to express the complex dielectric function $\varepsilon(\omega)$ in terms of the optical constants $\tilde{n}(\omega)$ and $\tilde{k}(\omega)$ according to the definition $\varepsilon(\omega) = [\tilde{n}(\omega) + i\tilde{k}(\omega)]^2$ where $\tilde{n}(\omega)$ is the index of refraction and $\tilde{k}(\omega)$ is the extinction coefficient. We can then write for the real part of the dielectric function:

```{math}
:label: eq-p2-ch05-8
\varepsilon_1(\omega) \equiv \tilde{n}^2(\omega) - \tilde{k}^2(\omega) \approx \varepsilon_0
```

where the index of refraction $\tilde{n}(\omega)$ is large and the extinction coefficient $\tilde{k}(\omega)$ is small. For the imaginary part of the dielectric function, we have

```{math}
:label: eq-p2-ch05-9
\varepsilon_2(\omega) \equiv 2\tilde{n}(\omega)\tilde{k}(\omega) \approx 2\sqrt{\varepsilon_0}\,\tilde{k}(\omega) = \frac{\varepsilon_0\omega_p^2\tau^2}{\omega^3\tau^3}
```

which is small, since $\omega_p \ll \omega$. Thus the absorption coefficient can be written as:

```{math}
:label: eq-p2-ch05-10
\alpha_{\text{abs}}(\omega) = \frac{2\omega\tilde{k}(\omega)}{c} \simeq \frac{2\omega}{c}\frac{\varepsilon_0\omega_p^2}{2\sqrt{\varepsilon_0}\omega^3\tau} = \frac{\sqrt{\varepsilon_0}\omega_p^2}{c\omega^2\tau}
```

and thus $\alpha_{\text{abs}}(\omega)$ is proportional to $1/\omega^2$ or to $\lambda^2$ for free carrier absorption in semiconductors for the case where $\omega\tau \gg 1$ and $\omega \gg \omega_p$. Figure {numref}`fig-p2-ch05-2` shows a plot of the optical absorption coefficient for InAs vs wavelength on a log-log plot for various carrier densities, showing that $\alpha_{\text{abs}}(\omega) \sim \lambda^p$ where $p$ is between 2 and 3 for a wide range of donor concentrations. The dependence of the reflectivity spectra (vs wavelength) for various donor concentrations for heavily doped n-type InSb is shown in Fig. {numref}`fig-p2-ch05-3`. The dependence of the plasma frequency on the carrier concentration is readily visible from these data.

:::{figure} images/fig-p2-ch05-2.png
:name: fig-p2-ch05-2
:width: 50%
:align: center
Fig. 5.2: Free carrier absorption in n-type InAs at room temperature for six different carrier concentrations (in units of $10^{17}\,\text{cm}^{-3}$) A: 0.28; B: 0.85; C: 1.4; D: 2.5; E: 7.8; and F: 39.0.
:::

:::{figure} images/fig-p2-ch05-3.png
:name: fig-p2-ch05-3
:width: 50%
:align: center
Fig. 5.3: Plasma edges observed in the room temperature reflectivity spectra of n-type InSb with carrier concentration $n$ (labeled $N$ in the figure) varying between $3.5 \times 10^{17}\,\text{cm}^{-3}$ and $4.0 \times 10^{18}\,\text{cm}^{-3}$. Here we see the plasma frequency $\omega_p$ move to shorter wavelengths $\lambda$ as the carrier concentration $n$ increases. The solid curves are theoretical fits to the experimental points, including consideration of the energy dependence of $m^*$ due to the strong interband coupling (called non-parabolic effects).
:::

## 5.3 Free Carrier Absorption in Metals

The typical limits for metals are somewhat different than for semiconductors. In particular we consider here the case where $\omega\tau \ll 1$, $\omega \ll \omega_p$, $|\varepsilon_0| \ll 4\pi\sigma/\omega$, so that $\tilde{n} \simeq \tilde{k}$. Thus we obtain

```{math}
:label: eq-p2-ch05-11
\varepsilon(\omega) \simeq \frac{4\pi i\sigma}{\omega} \simeq \frac{4\pi i n e^2\tau}{\omega m^*} \simeq i\varepsilon_2(\omega) \equiv 2i\tilde{n}\tilde{k} \simeq 2i\tilde{k}^2
```

This gives us for the extinction coefficient $\tilde{k}(\omega)$

```{math}
:label: eq-p2-ch05-12
\tilde{k}(\omega) = \sqrt{\frac{2\pi n e^2\tau}{m^*\omega}}
```

and the absorption coefficient becomes:

```{math}
:label: eq-p2-ch05-13
\alpha_{\text{abs}}(\omega) = \frac{2\omega\tilde{k}(\omega)}{c} = \sqrt{\frac{8\pi\omega n e^2\tau}{m^*c^2}}
```

For this limit $\alpha_{\text{abs}}(\omega)$ is proportional to $\sqrt{\omega}$. Usually, the convenient observable for metals is the reflectivity. In the limit appropriate for metals, $\tilde{n} = \tilde{k}$, and both $\tilde{n}$ and $\tilde{k}$ are large. We thus have

```{math}
:label: eq-p2-ch05-14
\mathcal{R} = \frac{(\tilde{n}-1)^2 + \tilde{k}^2}{(\tilde{n}+1)^2 + \tilde{k}^2} = \frac{\tilde{n}^2 - 2\tilde{n} + 1 + \tilde{k}^2}{\tilde{n}^2 + 2\tilde{n} + 1 + \tilde{k}^2} = 1 - \frac{4\tilde{n}}{\tilde{n}^2 + \tilde{k}^2 + 2\tilde{n} + 1}
```

```{math}
:label: eq-p2-ch05-15
\mathcal{R} \approx 1 - \frac{4\tilde{n}}{\tilde{n}^2 + \tilde{k}^2} \approx 1 - \frac{2}{\tilde{n}}.
```

But from Eq. {eq}`eq-p2-ch05-12` and the condition $\tilde{n} \approx \tilde{k} \gg 1$, we obtain

```{math}
:label: eq-p2-ch05-16
\tilde{n}(\omega) \simeq \sqrt{\frac{2\pi n e^2\tau}{m^*\omega}}
```

so that the reflectivity goes as

```{math}
:label: eq-p2-ch05-17
\mathcal{R}(\omega) \simeq 1 - 2\sqrt{\frac{m^*\omega}{2\pi n e^2\tau}}.
```

Equation {eq}`eq-p2-ch05-17` is known as the Hagen-Rubens relation which holds well for most metals in the infrared region of the spectrum. This formula also applies to degenerate semiconductors below the plasma frequency.

## 5.4 Direct Interband Transitions

To calculate the absorption due to direct interband transitions we go back to the definition for the absorption coefficient $\alpha_{\text{abs}}(\omega)$ which is defined as the power removed from the incident beam per unit volume per unit incident flux of electromagnetic energy:

```{math}
:label: eq-p2-ch05-18
\alpha_{\text{abs}}(\omega) = \frac{(\hbar\omega) \times \text{number of transitions/unit volume/unit time}}{\text{incident electromagnetic flux}}.
```

The incident electromagnetic flux appearing in the denominator of Eq. {eq}`eq-p2-ch05-18` is calculated from the Poynting vector

```{math}
:label: eq-p2-ch05-19
\vec{S} = \frac{c}{8\pi} \text{Re}(\vec{E}^* \times \vec{H}).
```

It is convenient to relate the field variables to the vector potential:

```{math}
:label: eq-p2-ch05-20
\vec{E} = -\frac{1}{c}\frac{\partial \vec{A}}{\partial t} = \frac{i\omega}{c}\vec{A}
```

```{math}
:label: eq-p2-ch05-21
\mu\vec{H} = \vec{B} = \vec{\nabla}\times\vec{A}.
```

In non-magnetic materials we can take the permeability $\mu$ to be unity. In taking the curl of $\vec{A}$, we assume a plane wave form

```{math}
:label: eq-p2-ch05-22
\vec{A} = \vec{A}_0 e^{i(\vec{K}\cdot\vec{r} - \omega t)}
```

where the propagation constant for the light is denoted by the wave vector $\vec{K}$. We thus obtain for the Poynting vector

```{math}
:label: eq-p2-ch05-23
\vec{S} = \frac{c}{8\pi}\text{Re}\left[-\frac{i\omega}{c}\vec{A}^* \times (i\vec{K}\times\vec{A})\right]
```

or

```{math}
:label: eq-p2-ch05-24
\vec{S} = \frac{\omega}{8\pi}\text{Re}\left[(\vec{A}^*\cdot\vec{A})\vec{K} - (\vec{A}^*\cdot\vec{K})\vec{A}\right].
```

Utilizing the fact that for a transverse plane wave $\vec{A}^*\cdot\vec{K} = 0$, we obtain

```{math}
:label: eq-p2-ch05-25
\vec{S} = \frac{\omega}{8\pi}\frac{\tilde{n}\omega}{c}|A|^2\hat{K}
```

where $\tilde{n}$ denotes the real part of the complex index of refraction and $\hat{K}$ is a unit vector along the Poynting vector. This quantity $|\vec{S}|$ in Eq. {eq}`eq-p2-ch05-25` becomes the denominator in Eq. {eq}`eq-p2-ch05-18` which is the expression defining the absorption coefficient. The transition probability/unit time/unit volume is calculated from the "Fermi Golden Rule"

```{math}
:label: eq-p2-ch05-26
W = \frac{2\pi}{\hbar} |\mathcal{H}'_{vc}|^2 \rho_{cv}(\hbar\omega).
```

If we wish to consider the absorption process at finite temperature, we also need to include the Fermi functions to represent the occupation of the states at finite temperature

```{math}
:label: eq-p2-ch05-27
f(E_v)[1-f(E_c)] - f(E_c)[1-f(E_v)]
```

in which the first group of terms represents the absorption process which depends on the valence band ($v$) being nearly full and the conduction band ($c$) being nearly empty. The second group of terms represents the emission process which proceeds if there are occupied conduction states and unoccupied valence states. Clearly, the Fermi functions in Eq. {eq}`eq-p2-ch05-27` simply reduce to $[f(E_v) - f(E_c)]$. The matrix elements $|\mathcal{H}'_{vc}|^2$ in Eq. {eq}`eq-p2-ch05-26` can be written in terms of the electromagnetic interaction Hamiltonian

```{math}
:label: eq-p2-ch05-28
\mathcal{H}'_{vc} = \langle v|\mathcal{H}'_{em}|c\rangle = -\left(\frac{e}{mc}\right)\langle v|\vec{A}(\vec{r},t)\cdot\vec{p}|c\rangle.
```

We show in §5.5 that the matrix element $\langle v|\vec{A}(\vec{r},t)\cdot\vec{p}|c\rangle$ coupling the valence and conduction bands for the electromagnetic interaction is diagonal in wave vector $\vec{k}$ since the wave vector for light $\vec{K}$ is small relative to Brillouin zone dimensions. As a result the spatial dependence of the vector potential can be ignored. Thus the square of the matrix elements coupling the valence and conduction bands becomes

```{math}
:label: eq-p2-ch05-29
|\mathcal{H}'_{vc}|^2 = \left(\frac{e}{mc}\right)^2 |A|^2 |\langle v|p|c\rangle|^2,
```

where $|\langle v|p|c\rangle|^2$ couples states with the same electron wave vector in the valence and conduction bands. Since $|\langle v|p|c\rangle|^2$ is slowly varying with $k$ in comparison to $\rho_{cv}(\hbar\omega)$, it is convenient to neglect the $k$ dependence of $|\langle v|p|c\rangle|^2$ and to evaluate this quantity at the $M_i$ critical point. Thus for direct interband transitions, we obtain the following expression for the absorption coefficient

```{math}
:label: eq-p2-ch05-30
\alpha_{\text{abs}}(\omega) = \frac{(\hbar\omega)[\frac{2\pi}{\hbar}(\frac{e}{mc})^2|A|^2|\langle v|p|c\rangle|^2\rho_{cv}(\hbar\omega)][f(E_v)-f(E_c)]}{\frac{\omega}{8\pi}\frac{\tilde{n}\omega}{c}|A|^2}
```

or

```{math}
:label: eq-p2-ch05-31
\alpha_{\text{abs}}(\omega) = \frac{16\pi^2 e^2}{m^2 c \tilde{n}\omega} |\langle v|p|c\rangle|^2 \rho_{cv}(\hbar\omega)[f(E_v)-f(E_c)]
```

where $\tilde{n}$ in Eqs. {eq}`eq-p2-ch05-30` and {eq}`eq-p2-ch05-31` denotes the index of refraction.

To get an idea of the functional forms of the quantities in Eq. {eq}`eq-p2-ch05-31`, we will consider a rather simplified picture of two simple parabolic bands with an allowed optical transition, i.e., a non-vanishing momentum matrix element coupling them. Writing the joint density of states from Eq. {numref}`eq-p2-ch04-4` for the case of an $M_0$ critical point (as occurs near $k=0$ for many semiconductors)

```{math}
:label: eq-p2-ch05-32
\rho_{cv}(\hbar\omega) = \frac{1}{2\pi^2}\left(\frac{2m_r}{\hbar^2}\right)^{3/2}\sqrt{\hbar\omega - E_g}
```

where $m_r$ is the reduced mass for the valence and conduction bands, we can estimate the absorption coefficient $\alpha_{\text{abs}}(\omega)$. At very low temperature, a semiconductor has an essentially filled valence band and an empty conduction band; that is $f(E_v)=1$ and $f(E_c)=0$. We can estimate $|\langle v|p|c\rangle|^2$ from the effective mass sum-rule (Eq. {numref}`eq-p2-ch03-33`)

```{math}
:label: eq-p2-ch05-33
|\langle v|p|c\rangle|^2 \simeq \frac{m_0 E_g}{2}\frac{m_0}{m^*}
```

where $m_0$ is the free electron mass. After substitution of Eqs. {eq}`eq-p2-ch05-32` and {eq}`eq-p2-ch05-33` into Eq. {eq}`eq-p2-ch05-31`, we obtain the following frequency dependence for the absorption coefficient for direct allowed transitions:

```{math}
:label: eq-p2-ch05-34
\alpha_{\text{abs}}(\omega) \propto \frac{1}{\omega}\sqrt{\hbar\omega - E_g}
```

so that the direct optically-allowed interband transitions are characterized by a threshold at the energy gap $E_g$ as shown in Fig. {numref}`fig-p2-ch05-1`. We thus see a very different frequency dependence of $\alpha_{\text{abs}}(\omega)$ for the various physical processes.

It is sometimes convenient to relate the optical absorption coefficient to the imaginary part of the dielectric function

```{math}
:label: eq-p2-ch05-35
\varepsilon_2(\omega) = \frac{\tilde{n}c}{\omega}\alpha_{\text{abs}}(\omega)
```

which from Eq. {eq}`eq-p2-ch05-31` becomes

```{math}
:label: eq-p2-ch05-36
\varepsilon_2(\omega) = \left(\frac{4\pi e}{m\omega}\right)^2 |\langle v|p|c\rangle|^2 \rho_{cv}(\hbar\omega)[f(E_v)-f(E_c)].
```

If we introduce the dimensionless quantity $f_{vc}$, which is usually called the oscillator strength and is defined by

```{math}
:label: eq-p2-ch05-37
f_{vc} = \frac{2|\langle v|p|c\rangle|^2}{m[E_c(k)-E_v(k)]} = \frac{2|\langle v|p|c\rangle|^2}{m\hbar\omega},
```

we obtain the following result for $\varepsilon_2(\omega)$ at $T=0$

```{math}
:label: eq-p2-ch05-38
\varepsilon_2(\omega) = \left(\frac{8\pi^2 e^2\hbar}{m\omega}\right) f_{vc} \rho_{cv}(\hbar\omega).
```

We further discuss how $\varepsilon_1(\omega)$ for interband transitions is obtained from $\varepsilon_2(\omega)$ in §6.2 using the Kramers–Kronig relation.

To illustrate the fit between these simple models and the behavior of the absorption coefficient near the fundamental absorption edge, we show in Fig. {numref}`fig-p2-ch05-4` a plot of $[\alpha_{\text{abs}}]^2$ vs $\hbar\omega$ for PbS, with the intercept of $[\alpha_{\text{abs}}]^2$ on the photon energy axis giving the direct energy band gap. By plotting $\alpha_{\text{abs}}(\omega)$ on a log scale vs $\hbar\omega$, a more accurate value for the energy gap can also be obtained as shown in Fig. {numref}`fig-p2-ch05-5`. The derivation of the functional form for the absorption coefficient for direct forbidden transitions proceeds as in the derivation of Eq. {eq}`eq-p2-ch05-31`, except that $|\langle v|p|c\rangle|^2$ is now dependent on $k^2$ so that $\alpha_{\text{abs}}(\omega)$ shows a $(\hbar\omega - E_g)^{3/2}$ threshold dependence for direct forbidden interband transitions.

:::{figure} images/fig-p2-ch05-4.png
:name: fig-p2-ch05-4
:width: 50%
:align: center
Fig. 5.4: Plot of the square of the absorption coefficient of PbS as a function of photon energy showing the linear dependence of $[\alpha_{\text{abs}}(\omega)]^2$ on $\hbar\omega$. The intercept with the x-axis defines the direct energy gap.
:::

:::{figure} images/fig-p2-ch05-5.png
:name: fig-p2-ch05-5
:width: 50%
:align: center
Fig. 5.5: Semilogarithmic plot of the absorption coefficient of InSb at 5 K as a function of photon energy. The filled circles represent experimental results. The curves have been calculated using various models. Best results are obtained when the dependence of the matrix elements on $k$ are included. The intercept with the x-axis gives the direct bandgap of InSb, which can be found more accurately using a semilogarithmic plot than using a linear plot as in Fig. {numref}`fig-p2-ch05-4`. The logarithmic plot also shows the large increases in $\alpha_{\text{abs}}$ at the absorption edge of a direct gap semiconductor.
:::

### 5.4.1 Temperature Dependence of $E_g$

Because of the expansion and contraction of the lattice with temperature, the various band parameters, particularly the energy gap is temperature dependent. Although calculations are available to predict and account for the $T$ dependence of the band gap at the fundamental absorption edge (threshold), $E_g(T)$ is best found by empirical fits. We give below expressions for such fits which are useful for research purposes

$$E_g(T) = 1.165 - 2.84\times 10^{-4}T \qquad (\text{eV}) \quad \text{Si}$$
$$E_g(T) = 0.742 - 3.90\times 10^{-4}T \qquad (\text{eV}) \quad \text{Ge}$$
$$E_g(T) = 1.522 - \frac{5.8\times 10^{-4}T^2}{T+300} \qquad (\text{eV}) \quad \text{GaAs}$$
$$E_g(T) = 2.338 - \frac{6.2\times 10^{-4}T^2}{T+460} \qquad (\text{eV}) \quad \text{GaP}$$
$$E_g(T) = 263 + \sqrt{400 + (0.506T)^2} \qquad (\text{meV}) \quad \text{PbS}$$
$$E_g(T) = 125 + \sqrt{400 + (0.506T)^2} \qquad (\text{meV}) \quad \text{PbSe}$$
$$E_g(T) = 171.5 + \sqrt{164 + [0.44(T+20)]^2} \qquad (\text{meV}) \quad \text{PbTe}$$

For Group IV and III–V compound semiconductors, $E_g(T)$ decreases with increasing $T$, as shown above, but for IV–VI compounds, $E_g(T)$ increases with increasing $T$.

### 5.4.2 Dependence of the Absorption Edge on Fermi Energy

:::{figure} images/fig-p2-ch05-6.png
:name: fig-p2-ch05-6
:width: 70%
:align: center
Fig. 5.6: Diagram showing how the fundamental absorption edge of an n-type semiconductor is shifted to higher energy by heavy doping. The wave vector for the Burstein shift $k_{\text{BS}}$ is defined in Eq. {eq}`eq-p2-ch05-39`.
:::

For lightly doped semiconductors, $E_F$ lies in the bandgap and the absorption edge occurs at $E_g$, neglecting excitonic effects which are discussed in Chapter 7. However, for heavily doped semiconductors, $E_F$ lies in the valence or conduction bands and the threshold for optical absorption is shifted. This shift in the absorption edge is often referred to as the Burstein shift, and is illustrated in Fig. {numref}`fig-p2-ch05-6` where it is shown that the threshold for absorption occurs when

```{math}
:label: eq-p2-ch05-39
\hbar\omega = E_g + \frac{\hbar^2 k_{\text{BS}}^2}{2}\left(\frac{1}{m_e^*} + \frac{1}{m_h^*}\right) = E_g + \frac{\hbar^2 k_{\text{BS}}^2}{2m_r^*}
```

in which $m_r^*$ is the reduced mass, $(1/m_r^*) = (1/m_e^*) + (1/m_h^*)$, and $k_{\text{BS}}$ is the wave vector at the Fermi level corresponding to the Burstein shift defined in Eq. {eq}`eq-p2-ch05-39`.

Referring to Eq. {eq}`eq-p2-ch05-27` where we introduce the probability that the initial state is occupied and the final state is unoccupied, we find that since doping affects the position of the Fermi level, the Fermi functions will depend on carrier concentration for heavily doped semiconductors. In particular the quantity $(1-f_0)$ denoting the availability of final states will be affected by the Burstein shift. If we write

```{math}
:label: eq-p2-ch05-40
\frac{\hbar^2 k_{\text{BS}}^2}{2m_e^*} = E - E_c
```

where $E_c$ is the energy at the bottom of the conduction band, then the probability that the final state is empty is

```{math}
:label: eq-p2-ch05-41
1 - f_0 = \frac{1}{1 + \exp[(E_F - E)/k_BT]} = \frac{1}{1 + \exp\left[\frac{E_F-E}{k_BT} - \frac{(\hbar\omega - E_g)m_h^*}{(m_e^*+m_h^*)k_BT}\right]}
```

and Eq. {eq}`eq-p2-ch05-41` should be used for the probability of final states in evaluating $f(E_c)$ in Eq. {eq}`eq-p2-ch05-31`. Referring to Fig. {numref}`fig-p2-ch05-6`, we see that transitions to the conduction band can start at $E_F - 4k_BT$ given by Eq. {eq}`eq-p2-ch05-39`. The Fermi level is at $E_F$ and some states above $E_F$ are also occupied with electrons at finite temperature, which can be calculated from Eq. {eq}`eq-p2-ch05-31`.

### 5.4.3 Dependence of the Absorption Edge on Applied Electric Field

:::{figure} images/fig-p2-ch05-7.png
:name: fig-p2-ch05-7
:width: 70%
:align: center
Fig. 5.7: Energy band diagram in an electric field showing the wavefunction overlap (a) without and (b) with the absorption of a photon of energy $\hbar\omega$.
:::

The electron wave functions in the valence and conduction bands have an exponentially decaying amplitude in the energy gap. In the presence of an electric field $\vec{E}$, a valence band electron must tunnel through a triangular barrier to reach the conduction band. In the absence of photon absorption, the height of the barrier is $E_g$ and its thickness is $E_g/e|\vec{E}|$ where $|\vec{E}|$ is the magnitude of the electric field, as shown in Fig. {numref}`fig-p2-ch05-7`(a). The effect of the photon, as shown in Fig. {numref}`fig-p2-ch05-7`(b), is to lower the barrier thickness to

```{math}
:label: eq-p2-ch05-42
t(\hbar\omega) = \frac{E_g - \hbar\omega}{e|\vec{E}|}
```

so that the tunneling probability is enhanced by photon absorption. Figure {numref}`fig-p2-ch05-8` shows that the absorption edge being effectively lowered by the presence of the electric field, and the effect of the electric field on $\alpha_{\text{abs}}$ is particularly pronounced just below the zero field band gap. The effect of an electric field on the fundamental absorption edge is called the Franz–Keldysh effect.

:::{figure} images/fig-p2-ch05-8.png
:name: fig-p2-ch05-8
:width: 70%
:align: center
Fig. 5.8: Electric field and photon energy dependence of the band-to-band absorption for GaAs, which is a direct band gap semiconductor.
:::

## 5.5 Conservation of Crystal Momentum in Direct Optical Transitions

For clarity we now show why the momentum matrix elements coupling two Bloch states for a perfect crystal are diagonal in $\vec{k}$ and conserve crystal momentum. It is this property of the momentum matrix elements that is responsible for direct interband transitions. We write the momentum matrix elements coupling two bands (for example, the valence and conduction bands) as

```{math}
:label: eq-p2-ch05-43
\langle n'\vec{k}'|\vec{p}|n,\vec{k}\rangle = \int d^3r e^{-i\vec{k}'\cdot\vec{r}} u_{n'k'}^*(\vec{r}) \left(\frac{\hbar}{i}\vec{\nabla}\right) e^{i\vec{k}\cdot\vec{r}} u_{nk}(\vec{r}).
```

Operating with $\vec{\nabla}$ on the product function of the Bloch state yields

```{math}
:label: eq-p2-ch05-44
\langle n'\vec{k}'|\vec{p}|n,\vec{k}\rangle = \int d^3r e^{-i\vec{k}'\cdot\vec{r}} u_{n'k'}^*(\vec{r}) e^{i\vec{k}\cdot\vec{r}} (\hbar\vec{k} + \frac{\hbar}{i}\vec{\nabla}) u_{nk}(\vec{r}).
```

Now the term in $\hbar\vec{k}$ can be integrated immediately to give $\hbar\vec{k}\delta_{nn'}\delta(\vec{k}-\vec{k}')$ and is thus diagonal in both band index and crystal momentum. This term therefore does not give rise to interband transitions. The remaining term in Eq. {eq}`eq-p2-ch05-44` is

```{math}
:label: eq-p2-ch05-45
\int d^3r e^{i(\vec{k}-\vec{k}')\cdot\vec{r}} \frac{\hbar}{i} u_{n'k'}^*(\vec{r}) \vec{\nabla} u_{nk}(\vec{r}).
```

The function $u_{n'k'}^*(\vec{r})\vec{\nabla}u_{nk}(\vec{r})$ in Eq. {eq}`eq-p2-ch05-45` is periodic under the translation $\vec{r} \to \vec{r} + \vec{R}_n$ where $\vec{R}_n$ is any lattice vector. But any spatially periodic function can be Fourier expanded

```{math}
:label: eq-p2-ch05-46
\sum_m F_m e^{i\vec{G}_m\cdot\vec{r}} = \frac{\hbar}{i} u_{n'k'}^*(\vec{r}) \vec{\nabla} u_{nk}(\vec{r})
```

in terms of the reciprocal lattice vectors $\vec{G}_m$. We thus obtain for the integral in Eq. {eq}`eq-p2-ch05-45` factors of the form

```{math}
:label: eq-p2-ch05-47
\int d^3r e^{i(\vec{k}-\vec{k}')\cdot\vec{r}} F_m e^{i\vec{G}_m\cdot\vec{r}}
```

which vanishes unless

```{math}
:label: eq-p2-ch05-48
\vec{k} - \vec{k}' + \vec{G}_m = 0.
```

Since $\vec{k}-\vec{k}'$ must be within the first Brillouin zone, $\vec{k}$ and $\vec{k}'$ can only differ by the reciprocal lattice vector $\vec{G}_m \equiv 0$. Thus Eq. {eq}`eq-p2-ch05-47` vanishes unless $\vec{k} = \vec{k}'$ and we have demonstrated that because of the periodicity of the crystal lattice, the momentum matrix elements coupling two bands can only do so at the same value of crystal momentum $\vec{k}$. Since the probability for optical transitions involves the same momentum matrix elements as occur in the determination of the effective mass in the transport properties, study of the optical properties of a solid also bears an important relation to the transport properties of that material. If the finite wave vector of the light is included, then the spatial dependence of the vector potential must also be included, as a correction. In some cases the interband transition is not allowed at the high symmetry point for symmetry reasons. As we then move away from the high symmetry point the transitions can occur as the wave function is expanded in a Taylor expansion about the high symmetry point.

## 5.6 Indirect Interband Transitions

:::{figure} images/fig-p2-ch05-9.png
:name: fig-p2-ch05-9
:width: 70%
:align: center
Fig. 5.9: Indirect optically induced transitions of electrons (a) from the initial state 0 in the valence band to final states 1 and 2 in the conduction band, and (b) from initial states 1 and 2 in the valence band to the final state 0 in the conduction band. In both (a) and (b) a phonon labeled by $(\hbar\omega_s, q_s)$ is absorbed in the indirect transition process.
:::

In making indirect transitions, the semiconductor can either emit or absorb a phonon of energy $\hbar\omega_q$

```{math}
:label: eq-p2-ch05-49
\hbar\omega = E_f - E_i \pm \hbar\omega_q
```

in which $E_f$ and $E_i$ are, respectively, the energies of the final and initial electron states and the $\pm$ signs refer to phonon emission ($+$ sign) or absorption ($-$ sign).

To review indirect interband transitions in a semiconductor, we derive below an expression for the absorption coefficient for the situation where a phonon is absorbed in the indirect process, as shown schematically in Fig. {numref}`fig-p2-ch05-9`. Similar arguments can then be applied to the case where a phonon is emitted.

The conservation of energy principle is applied to the total process, consisting of the direct optical transition and the absorption of a phonon $\hbar\omega_q$, yielding

```{math}
:label: eq-p2-ch05-50
\hbar\omega = E_g - \hbar\omega_q + \frac{\hbar^2(\vec{k}_n - \vec{k}_c)^2}{2m_n} + \frac{\hbar^2 k_p^2}{2m_p}
```

in which the notation in Eq. {eq}`eq-p2-ch05-50` is defined in Fig. {numref}`fig-p2-ch05-10`, and $E_g$ is the thermal gap or energy difference between the conduction band minimum (e.g., at the $L$-point) and the valence band maximum at the $\Gamma$-point of the Brillouin zone. The negative sign in front of the phonon energy $\hbar\omega_q$ in Eq. {eq}`eq-p2-ch05-50` corresponds to the phonon absorption process. In Eq. {eq}`eq-p2-ch05-50`, the term $\hbar(\vec{k}_n - \vec{k}_c)$ denotes the difference between the crystal momentum $\hbar\vec{k}_n$ of an excited electron in the $L$-point conduction band and the crystal momentum $\hbar\vec{k}_c$ at the $L$-point conduction band minimum. Thus the kinetic energy of the excited electron with crystal momentum $\hbar\vec{k}_n$ is

```{math}
:label: eq-p2-ch05-51
E_n - E_c = \frac{\hbar^2(\vec{k}_n - \vec{k}_c)^2}{2m_n}
```

where $E_n$ is the energy above the conduction band minimum $E_c$, and $m_n$ in Eq. {eq}`eq-p2-ch05-51` is the effective mass of an electron near the conduction band minimum.

:::{figure} images/fig-p2-ch05-10.png
:name: fig-p2-ch05-10
:width: 50%
:align: center
Fig. 5.10: Schematic diagram of an indirect transition showing the notation used in the text. $E_c$ is the energy of the $L$-point conduction band at wave vector $k_c$, while $E_c$ is the thermal energy gap. The valence band maximum $E_v$ is taken at the zero of energy. $E_n$ and $(\vec{k}_n - \vec{k}_c)$, respectively, denote the energy and momentum of an excited electron, while $E_p$ and $\vec{k}_p$, respectively, denote the corresponding parameters for the holes near $\vec{k}=0$. It is customary to place the zero of energy at the valence band maximum.
:::

Since the valence band extremum is at $\vec{k}=0$, then $\hbar\vec{k}_p$ is the crystal momentum for the hole that is created when the electron is excited, corresponding to the kinetic energy of the hole

```{math}
:label: eq-p2-ch05-52
E_p = \frac{\hbar^2 k_p^2}{2m_p}.
```

The sign convention that is used in this discussion is to take $E_p$ as a positive number and the zero of energy is taken at the valence band maximum (see Fig. {numref}`fig-p2-ch05-10`). In terms of these sign conventions, conservation of energy yields

```{math}
:label: eq-p2-ch05-53
\hbar\omega = E_g - \hbar\omega_q + (E_n - E_c) + E_p
```

and conservation of momentum requires

```{math}
:label: eq-p2-ch05-54
\vec{q} = \vec{k}_n - \vec{k}_p
```

where $\vec{q}$ is the wave vector for the absorbed phonon. In Fig. {numref}`fig-p2-ch05-9`, the phonon energy and the wave vector are denoted by $\hbar\omega_{s_i}$ and $q_{s_i}$.

We now find the frequency dependence of the absorption edge for indirect transitions in order to make a distinction between direct and indirect transitions just from looking at the frequency dependence of the optical absorption data. Let us then consider the transition from some specific initial state $E_p$ to a specific final state $E_n$. The density of states $\rho_c(E_n)$ (number of states/unit volume/unit energy range) for the final state conduction band has an energy dependence given by

```{math}
:label: eq-p2-ch05-55
\rho_c(E_n) \propto (E_n - E_c)^{1/2}.
```

Using the conservation of energy relation in Eq. {eq}`eq-p2-ch05-53`, $\rho_c(E_n)$ can be expressed in terms of $E_p$ as

```{math}
:label: eq-p2-ch05-56
\rho_c(E_n) \propto (\hbar\omega - E_g - E_p + \hbar\omega_q)^{1/2}.
```

Thus we see that transitions to a state $E_n$ take place from a range of initial states, since $E_p$ can vary between $E_p = 0$ where all of the kinetic energy is given to the electron, and the opposite limit where $E_n - E_c = 0$ and all of the kinetic energy is given to the hole. Let the energy $\delta$ denote the range of possible valence band energies between these limits

```{math}
:label: eq-p2-ch05-57
\delta = \hbar\omega - E_g + \hbar\omega_q.
```

The density of initial states for the valence band has an energy dependence given by

```{math}
:label: eq-p2-ch05-58
\rho_v(E_p) \propto E_p^{1/2}
```

where we are using the convention $E_v \equiv 0$ for defining the zero of energy, so that $E_p$ vanishes at the top of the valence band. Thus the effective density of states for the phonon absorption process is found by summing over all $E_p$ values which conserve energy,

```{math}
:label: eq-p2-ch05-59
\rho(\hbar\omega) \propto \int_0^\delta \rho_c(E_n)\rho_v(E_p) dE_p \propto \int_0^\delta \sqrt{\delta - E_p}\sqrt{E_p}\,dE_p.
```

The integral in Eq. {eq}`eq-p2-ch05-59` can be carried out through integration by parts, utilizing the notation $u = E_p$, and $v = \delta - E_p$, and writing the limits of the integration in terms of the variable $E_p$

```{math}
:label: eq-p2-ch05-60
\int_0^\delta \sqrt{uv}\,du = \left.\frac{\delta - 2v}{4}\sqrt{uv}\right|_0^\delta + \left.\frac{\delta^2}{4}\tan^{-1}\sqrt{\frac{u}{\delta-u}}\right|_0^\delta = \frac{\delta^2\pi}{8}.
```

Substitution in Eq. {eq}`eq-p2-ch05-57` for $\delta$ in Eqs. {eq}`eq-p2-ch05-59` and {eq}`eq-p2-ch05-60` results in

```{math}
:label: eq-p2-ch05-61
\rho(\hbar\omega) \propto \frac{\pi}{8}(\hbar\omega - E_g + \hbar\omega_q)^2
```

which gives the frequency dependence for the indirect interband transitions involving phonon absorption. Also, the probability for the absorption of a phonon is proportional to the Bose-Einstein factor

```{math}
:label: eq-p2-ch05-62
n(\hbar\omega_q) = \frac{1}{\exp(\hbar\omega_q/k_BT) - 1}
```

so that the absorption coefficient for indirect transitions in which a phonon is absorbed becomes

```{math}
:label: eq-p2-ch05-63
\alpha_{\text{abs}}(\omega) = \mathcal{C}_a \frac{(\hbar\omega - E_g + \hbar\omega_q)^2}{\exp(\hbar\omega_q/k_BT) - 1}
```

where $\mathcal{C}_a$ is a constant for the phonon absorption process.

To find the absorption coefficient for the indirect absorption process that involves the emission of a phonon, we must find the effective density of states for the emission process. The derivation in this case is very similar to that given above for phonon absorption, except that the energy conservation condition now involves the phonon energy with the opposite sign. Furthermore, the probability of emission of a phonon is proportional to $[n(\hbar\omega_q)+1]$ which is given by

```{math}
:label: eq-p2-ch05-64
[n(\hbar\omega_q) + 1] = 1 + [e^{\hbar\omega_q/k_BT} - 1]^{-1} = \frac{1}{1 - e^{-\hbar\omega_q/k_BT}}
```

so that the absorption constant for phonon emission becomes

```{math}
:label: eq-p2-ch05-65
\alpha_{\text{ems}}(\omega) = \mathcal{C}_e \frac{(\hbar\omega - E_g - \hbar\omega_q)^2}{1 - \exp(-\hbar\omega_q/k_BT)}
```

where $\mathcal{C}_e$ is a constant for the phonon emission process.

At low temperatures, the phonon emission process dominates because there are so few phonons available for the absorption process. Furthermore, as a function of photon energy, different thresholds are obtained for the absorption and emission processes. In the absorption process, absorption starts when $\hbar\omega = E_g - \hbar\omega_q$ (see Fig. {numref}`fig-p2-ch05-11`), while for the emission process, the optical absorption starts when $\hbar\omega = E_g + \hbar\omega_q$. So if we plot $\sqrt{\alpha_{\text{abs}}(\omega)}$ vs $\hbar\omega$, as is shown in Fig. {numref}`fig-p2-ch05-11`, then $\sqrt{\alpha_{\text{abs}}(\omega)}$ in the low photon energy range will go as $\sqrt{\alpha_{\text{abs}}(\omega)} \propto (\hbar\omega - E_g + \hbar\omega_q)$ while $\sqrt{\alpha_{\text{ems}}(\omega)}$ will be proportional to $(\hbar\omega - E_g - \hbar\omega_q)$. Experimentally, a superposition of the absorption and emission processes will be observed.

:::{figure} images/fig-p2-ch05-11.png
:name: fig-p2-ch05-11
:width: 50%
:align: center
Fig. 5.11: Schematic diagram showing the frequency dependence of the square root of the absorption coefficient for indirect interband transitions near the thresholds for the phonon emission and absorption processes. The curves are for four different temperatures. At the lowest temperature (T4) the phonon emission process dominates, while at the highest temperature (T1) the phonon absorption process is most important at low photon energies. The magnitude of twice the phonon energy is indicated.
:::

:::{figure} images/fig-p2-ch05-12.png
:name: fig-p2-ch05-12
:width: 80%
:align: center
Fig. 5.12: Plots of the square root of the absorption coefficients of Si versus photon energy at several temperatures. The two segments of a straight line drawn through the experimental points represent the two contributions associated with phonon absorption and emission. (From Macfarlane, et al., Phys. Rev. 111, 1249 (1958)).
:::

Some experimental data illustrating indirect interband transitions are given in Fig. {numref}`fig-p2-ch05-12`. The shift of the curves in Fig. {numref}`fig-p2-ch05-12` as a function of photon energy is due to the temperature dependence of the indirect gap in silicon. In Fig. {numref}`fig-p2-ch05-12` it is easy to separate out the lower energy absorption contribution which is associated with the phonon absorption process (compare Figs. {numref}`fig-p2-ch05-11` and {numref}`fig-p2-ch05-12`). At higher energies it is also easy to separate out the phonon emission contribution. By carrying out measurements at several different temperatures it is possible to obtain a more accurate value for $\hbar\omega_q$. Figure {numref}`fig-p2-ch05-12` shows that the phonon absorption process becomes more favorable as the temperature is raised, while the emission process is less sensitive to temperature. The physical reason behind this is that for the absorption process to occur in the first place, phonons of the appropriate wave vector must be available. In Ge the phonon assisted process requires phonons of wave vector $\vec{q}$ extending from $\Gamma$ to $L$, while for Si we need a phonon $\vec{q}$-vector from $\Gamma$ to $\Delta_{\min}$ (where $\Delta_{\min}$ corresponds to the $\Delta$ point conduction band minimum). Since lattice vibrations are thermally excited, there are few available phonons at low temperatures, but more are available at high temperatures. On the other hand, phonon emission does not depend upon the availability of phonons since the emission process itself generates phonons; for this reason the phonon emission process is relatively insensitive to temperature.

Since silicon is a relatively hard material (with a Debye temperature of $\theta_D = 658\,\text{K}$), there will only be a few large wavevector phonons excited at room temperature. Therefore the phonon emission process will dominate in the optical absorption for photon energies where such emission is energetically possible. These arguments account for the different slopes observed for the phonon absorption and emission contributions to the absorption coefficient of Fig. {numref}`fig-p2-ch05-12`.

Another complication that arises in real materials is that there are several types of phonons present for a given $\vec{q}$-vector, i.e., there are acoustic and optical branches, and for each branch there are longitudinal and transverse modes. An example of the analysis of optical absorption data to obtain the frequencies of the various phonons at $q=0$ is given in Fig. {numref}`fig-p2-ch05-13` where $\alpha_{\text{abs}}^{1/2}$ vs $\hbar\omega$ is plotted for the indirect gap semiconductor GaP, from which it is possible to measure $\hbar\omega_q$ for various LO, LA, TO and TA phonons. Today such optical data are seldom taken, because it is now customary to use inelastic neutron diffraction data to plot out the entire dispersion curve for each of the phonon branches. When the phonon frequencies are high, electron energy loss spectroscopy can be helpful in obtaining $\omega_q(q)$ for the various phonon branches as is discussed in Chapter 12. In the case of graphite we have recently shown in our research group how resonance Raman spectroscopy can be used to obtain important information about the phonon dispersion relations for this system.

:::{figure} images/fig-p2-ch05-13.png
:name: fig-p2-ch05-13
:width: 50%
:align: center
Fig. 5.13: Plots of the square root of the absorption coefficients of GaP vs photon energy at two different temperatures. The labels denote the various absorption thresholds associated with the emission of various phonon modes. The observation of these phonon modes is made possible by the enhanced absorption associated with excitons at the absorption threshold (see Chapter 7). The apparent shift in the phonon frequencies is mostly due to the variation of the bandgap energy with temperature (see Figs. {numref}`fig-p2-ch05-11` and {numref}`fig-p2-ch05-12`).
:::
