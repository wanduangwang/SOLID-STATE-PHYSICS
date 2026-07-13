---
title: "11 Non-Linear Optics"
abstract: "This chapter introduces the basic phenomenology of non-linear optics, including the non-linear susceptibility, the non-linear wave equation, harmonic generation, parametric oscillation, and frequency conversion."
---

# 11 Non-Linear Optics

## 11.0 Overview

Non-linear optics became an important field of activity in the 1960's with the advent of high power laser sources. When electromagnetic fields become strong enough, the dielectric response itself depends on the electric field, giving rise to effects such as harmonic generation, parametric oscillation, and frequency conversion. This chapter reviews the non-linear wave equation, phase matching, and the elementary processes described by the lowest-order non-linear susceptibility.

## 11.1 Introductory Comments

Non-linear optics became an important field of activity in the 1960's with the advent of high power laser sources such as:

| Source | Wavelength |
|--------|------------|
| CO$_2$ | 10.6 $\mu$m |
| YAG:Nd$^{3+}$ | 1.06 $\mu$m |
| ruby | 6943 Å |
| argon | 5145 Å |

The topics we will consider under heading of non-linear optics are:

1. harmonic generation
2. paramagnetic oscillation
3. frequency conversion.

The significant point in non-linear optics is that, when the electromagnetic fields become strong enough, the dielectric function becomes dependent on the electric field $\vec{E}$. We write the total dielectric function as

```{math}
:label: eq-p2-ch11-1
\varepsilon_T = \varepsilon + \overset{\leftrightarrow}{\varepsilon}_{\rm NL} \cdot \vec{E}
```

where $\varepsilon$ is the linear response and $\overset{\leftrightarrow}{\varepsilon}_{\rm NL} \cdot \vec{E}$ represents the non-linear term. Thus, non-linear effects become more important as the magnitude of the electric field is increased. To observe non-linear effects, we require fields of magnitude $|\vec{E}| \sim 10^6$ volt/cm. Fields of this magnitude are readily available with high power laser sources. Non-linear effects are of great importance in quantum well structures.

It is sometimes more convenient to express these non-linear effects in terms of the polarization per unit volume $\vec{P}$

```{math}
:label: eq-p2-ch11-2
\vec{P} = \overset{\leftrightarrow}{\chi}_0 \vec{E} + \overset{\leftrightarrow}{\chi}_1 \vec{E}\vec{E} + \overset{\leftrightarrow}{\chi}_2 \vec{E}\vec{E}\vec{E} + \cdots
```

where $\overset{\leftrightarrow}{\chi}_0$ is the linear susceptibility tensor, $\overset{\leftrightarrow}{\chi}_1$ is the lowest order non-linear susceptibility important in non-linear materials with no center of inversion; and $\overset{\leftrightarrow}{\chi}_2$ is the second order non-linear susceptibility which comes into play for non-linear effects in cubic crystals with a center of inversion for which the first order term vanishes by symmetry.

For the present discussion we will only consider the lowest order non-linear term:

```{math}
:label: eq-p2-ch11-3
\vec{P}^{NL} = \overset{\leftrightarrow}{\chi}_1 \cdot \vec{E}\vec{E}
```

where $NL$ denotes non-linear and the non-linear susceptibility is in reality a 3rd rank tensor in the same sense that $\chi_0$ for the linear response is a second rank tensor in an actual solid state medium. Likewise $\overset{\leftrightarrow}{\chi}_2$ in Eq. {eq}`eq-p2-ch11-2` is a 4th rank tensor. We will not make any use of the tensorial properties of $\chi_1$ here, because we want to keep things simple.

Maxwell's equations in this case become

```{math}
:label: eq-p2-ch11-4
\nabla \times \vec{E} + \frac{\mu_0}{c}\left(\frac{\partial \vec{H}}{\partial t}\right) = 0 \qquad \nabla \times \vec{H} - \frac{\varepsilon_0}{c}\left(\frac{\partial \vec{E}}{\partial t}\right) = \frac{4\pi}{c}\left(\frac{\partial}{\partial t}\right)\overset{\leftrightarrow}{\chi}_1 \cdot \vec{E}\vec{E}
```

where the term in $\chi_1 \cdot \vec{E}\vec{E}$ is the non-linear term. We thus obtain the non-linear wave equation

```{math}
:label: eq-p2-ch11-5
\nabla^2 \vec{E} - \frac{\varepsilon_0\mu_0}{c^2}\left(\frac{\partial^2 \vec{E}}{\partial t^2}\right) = \frac{4\pi\mu_0}{c^2}\left(\frac{\partial^2}{\partial t^2}\right)\overset{\leftrightarrow}{\chi}_1 \cdot \vec{E}\vec{E}.
```

The wave equation *without the non-linear term* has plane wave eigen functions. That is, if we have an incident field with more than one frequency

```{math}
:label: eq-p2-ch11-6
\vec{E} = \left[\vec{E}_1 e^{i(K_1z - \omega_1t)} + \vec{E}_2 e^{i(K_2z - \omega_2t)}\right],
```

the wave equation

```{math}
:label: eq-p2-ch11-7
\nabla^2 \vec{E} - \frac{\varepsilon_0\mu_0}{c^2}\left(\frac{\partial^2 \vec{E}}{\partial t^2}\right) = 0
```

is valid for each of the waves in Eq. {eq}`eq-p2-ch11-6`. This insures that no mixing occurs and each frequency propagates independently through the linear medium.

Now what does the non-linear term do? Here we have to take a product $\vec{E}\vec{E}$. Clearly we will get terms at $2\omega_1$ and $2\omega_2$ (frequency doubling or second harmonic generation) and also at $|\omega_1 + \omega_2|$ (frequency mixing). This means that we now no longer have plane wave solutions

```{math}
:label: eq-p2-ch11-8
\vec{E}_i = \vec{\mathcal{E}}_i e^{i(K_i z - \omega_i t)}
```

for $\vec{E}_i$ polarized along $\hat{x}$, where $\vec{\mathcal{E}}_i$ is a constant amplitude. Instead we must look for a more generalized form. For example, we could seek a solution of the form of a modified plane wave

```{math}
:label: eq-p2-ch11-9
\vec{E}_i = \vec{\mathcal{E}}_i(z) e^{i(K_i z - \omega_i t)}
```

where $\vec{\mathcal{E}}_i(z)$ now has a weak $z$ dependence. This approach is in the spirit of perturbation theory. Now in taking spatial derivatives of $E_i$ we will get two terms

```{math}
:label: eq-p2-ch11-10
\frac{\partial E_i}{\partial z} = \left[\frac{\partial \mathcal{E}_i}{\partial z} + iK_i\mathcal{E}_i\right] e^{i(K_i z - \omega_i t)}
```

where the term in $iK_i\mathcal{E}_i$ is the large term and the term in $\partial\mathcal{E}_i/\partial z$ represents the small perturbation. Thus in taking two derivatives we will get

```{math}
:label: eq-p2-ch11-11
\frac{\partial^2 E_i}{\partial z^2} = iK_i\left[2\frac{\partial \mathcal{E}_i}{\partial z} + iK_i\mathcal{E}_i\right] e^{i(K_i z - \omega_i t)},
```

retaining only the lowest order term in the perturbation.

We will now show that coupling to frequency $\omega_3$ is possible for waves at frequencies $\omega_1$ and $\omega_2$ provided that $\omega_3 = \omega_1 + \omega_2$. From the wave equation Eq. {eq}`eq-p2-ch11-5`, we see that if the incident field has two frequencies $\omega_1$ and $\omega_2$, we will get a perturbation driving term on the right hand side of the non-linear wave equation and also a perturbation term on the left hand side of this equation due to the $z$ dependence of $\mathcal{E}_i(z)$. Assuming a solution at some frequency $\omega_3$ (to be determined from the wave equation, Eq. {eq}`eq-p2-ch11-7`) we can write an equation for the right and left hand perturbation terms

```{math}
:label: eq-p2-ch11-12
2iK_3\left(\frac{\partial \mathcal{E}_3}{\partial z}\right)e^{i(K_3z - \omega_3t)} = -(\omega_1 + \omega_2)^2\left(\frac{4\pi\mu_0}{c^2}\right)\chi_1 \cdot \mathcal{E}_1\mathcal{E}_2 e^{i(K_1z - \omega_1t)}e^{i(K_2z - \omega_2t)}
```

To satisfy the right hand side of Eq. {eq}`eq-p2-ch11-5` we need to match the time phase terms on the left hand side, yielding

```{math}
:label: eq-p2-ch11-13
\omega_3 = \omega_1 + \omega_2,
```

which indicates that mixing has occurred.

Because of the dispersion properties of crystals, the wave vector for light $K$ will be a function of $\omega$ and we cannot in general cancel the phases for all frequencies. Thus, some mismatch $\Delta K = K_3 - (K_1 + K_2)$ will generally occur. Phase matching is achieved when $\Delta K \equiv 0$ and in this case the three waves will be coherent. In free space, phase matching is automatically satisfied since there is no nonlinear response in free space. In a solid, $K = \tilde{n}\omega/c$ where $\tilde{n}$ is the index of refraction. Solids have the property that the optical constants are frequency-dependent so that in general $\tilde{n}_{\omega_1} + \tilde{n}_{\omega_2} \neq \tilde{n}_{\omega_3}$. If, however, $\Delta K$ is small, phase matching is approximately satisfied. In fact, provided that the phase changes by less than $\pi$, some coherence will be achieved. We thus introduce a phase coherence length $\ell_c$ defined as $\ell_c = \pi/\Delta K$ over which some degree of coherence is achieved.

## 11.2 Second Harmonic Generation

For the non-linear process corresponding to second harmonic generation we have $\omega_1 = \omega_2 = \omega$ and $\omega_3 = 2\omega$. The non-linear contribution to the polarization will be proportional to $(E_\omega)^2$ and the power generated at $2\omega$ will be proportional to $(E_\omega)^4$. If phase matching is achieved, the power produced at the second harmonic will be maximized. For phase matching we require

```{math}
:label: eq-p2-ch11-14
\omega_3\tilde{n}_3 = \omega_1\tilde{n}_1 + \omega_2\tilde{n}_2
```

or

```{math}
:label: eq-p2-ch11-15
2\omega\tilde{n}_3 = 2\omega\tilde{n}_1,
```

which can be written more conveniently as $\tilde{n}_{2\omega} = \tilde{n}_\omega$, which says that we require the index of refraction at $2\omega$ to be equal to the index at frequency $\omega$ for phase matching.

For solids, the index of refraction $\tilde{n}$ will generally be frequency dependent, so phase matching would seem difficult to achieve. By using anisotropic materials and selecting particular directions of propagation, it is sometimes possible to arrange matters so that $\tilde{n}_\omega$ for one polarization direction is equal to $\tilde{n}_{2\omega}$ for another polarization direction. Efficient harmonic generation has been achieved using the semiconductor Te, which crystallizes in a hexagonal structure and has a rather different index of refraction for the polarization $\vec{E} \parallel \vec{c}$ than for $\vec{E} \perp \vec{c}$. To achieve frequency doubling in Te, it is convenient to use a CO$_2$ laser source, since Te which has a band gap of 0.344 eV is quite transparent at both $\omega$ and $2\omega$ for the CO$_2$ laser line at 10.6 $\mu$m. With frequency doubling, it is possible to convert infrared light to visible radiation and thus to utilize the highly developed technology for the detection of visible light signals. The process of second harmonic generation need not be considered a small or weak effect. High conversion efficiencies ($>50\%$) can be achieved.

### 11.2.1 Parametric Oscillation

Here laser power is applied to a non-linear crystal at a pump frequency $\omega_3$. Oscillations are induced in the crystal at frequencies $\omega_1$ and $\omega_2$, the signal and idler frequencies respectively. The signal and idler frequencies are determined by the frequency condition

```{math}
:label: eq-p2-ch11-16
\omega_3 = \omega_1 + \omega_2
```

and the phase matching condition

```{math}
:label: eq-p2-ch11-17
\Delta K = 0, \qquad K_3 = (K_1 + K_2).
```

It is only when phase matching occurs that the two waves will interact sufficiently to produce any measurable non-linear effects. The phase matching condition can also be written as

```{math}
:label: eq-p2-ch11-18
\omega_3\tilde{n}_3 = \omega_1\tilde{n}_1 + \omega_2\tilde{n}_2
```

where $\tilde{n}_1$ and $\tilde{n}_2$ are refractive indices at frequencies $\omega_1$ and $\omega_2$ and are determined by the propagation direction and polarization of the modes at $\omega_1$ and $\omega_2$. In non-cubic materials, the index of refraction depends on the direction of the $\vec{E}$ field relative to the crystallographic directions. Thus, by changing the propagation direction of the pump frequency relative to the crystal optical axis (e.g., the "$c$" axis in a hexagonal crystal like Te), it is possible to "tune" the signal and idler frequencies $\omega_1$ and $\omega_2$. Furthermore, since the indices are temperature dependent, "tuning" can also be accomplished by varying the temperature of the non-linear crystal; tuning with application of uniaxial stress can also be accomplished. Parametric oscillation need not be a small effect. Using a Q-switched ruby laser as a pump at 6943 Å on a non-linear LiNbO$_3$ crystal, a signal at 1.04 $\mu$m and an idler at 2.08 $\mu$m have been achieved with 60 kW of signal power generated for 270 kW of input power or a conversion efficiency of $\sim 20\%$. Tuning with a parametric oscillator between 0.54 $\mu$m and 3.7 $\mu$m has also been achieved.

### 11.2.2 Frequency Conversion

For frequency conversion, two frequencies are applied to a non-linear crystal and the sum frequency (up converter) or difference frequency (down converter) is generated. In this experiment, we might impose a high power signal at a pump frequency $\omega_3$ and a lower power signal at $\omega_2$. These signals mix in the non-linear medium to produce a signal at

```{math}
:label: eq-p2-ch11-19
\omega_1 = \omega_3 - \omega_2 \qquad (\text{down converter})
```

or at

```{math}
:label: eq-p2-ch11-20
\omega_1 = \omega_3 + \omega_2 \qquad (\text{up-converter}).
```

Phase matching determines whether up-conversion or down-conversion actually occurs. The power from the signal at $\omega_3$ drives the system at frequencies $\omega_1$ and $\omega_2$, and as a function of length of the non-linear crystal, the amounts of power at $\omega_1$ and $\omega_2$ can be varied. Thus, by choosing the length properly the conversion of power to frequency $\omega_1$ can be maximized.

Frequency conversion is attractive for practical applications because up-conversion can be exploited to convert an infrared signal into the visible region where detectors are fast and sensitive. Down-converters can be exploited to create a different frequency in the far infrared where high power sources have been unavailable until about 1965, when some far infrared lasers were first built. For example, the two strong CO$_2$ laser lines at 10.6 $\mu$m and 9.6 $\mu$m can be mixed to get a far infrared signal.
