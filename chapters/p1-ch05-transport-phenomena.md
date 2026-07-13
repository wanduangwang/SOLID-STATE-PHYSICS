---
title: "5 Thermal Transport"
abstract: "This chapter treats thermal transport in solids and the thermoelectric coupling between electrical and thermal currents. It derives the electronic contribution to the thermal conductivity for metals, semiconductors, and insulators from the Boltzmann equation, establishes the Wiedemann-Franz law, and analyzes the thermoelectric effects (Seebeck, Peltier, Thomson), the Kelvin relations, the figure of merit, and the phonon-drag effect."
---

# 5 Thermal Transport

## 5.0 Overview

The electrons in solids not only conduct electricity but also conduct heat, as they transfer energy from a hot junction to a cold junction. Just as the electrical conductivity characterizes the response of a material to an applied voltage, the thermal conductivity likewise characterizes the material with regard to heat flow in the presence of a temperature gradient. In fact the electrical conductivity and thermal conductivity are coupled, since thermal conduction also transports charge and electrical conduction also transports energy. This coupling between electrical and thermal transport gives rise to thermo-electricity. In this chapter, we discuss first the thermal conductivity for metals, semiconductors and insulators and then consider the coupling between electrical and thermal transport which gives rise to thermoelectric phenomena. In Chapter 6, we discuss scattering mechanisms for electrons and phonons.

**References:**

* Ziman, *Principles of the Theory of Solids*, Cambridge Univ. Press, 1972, Chapter 7.
* Reif, *Fundamentals of Statistical and Thermal Physics*, McGraw-Hill, 1965, pp. 393-397.
* Wolfe, Holonyak and Stillman, *Physical Properties of Semiconductors*, Prentice Hall, 1989, chapter 5.

## 5.1 Thermal Transport

The electrons in solids not only conduct electricity but also conduct heat, as they transfer energy from a hot junction to a cold junction. Just as the electrical conductivity characterizes the response of a material to an applied voltage, the thermal conductivity likewise characterizes the material with regard to heat flow in the presence of a temperature gradient. In fact the electrical conductivity and thermal conductivity are coupled, since thermal conduction also transports charge and electrical conduction also transports energy. This coupling between electrical and thermal transport gives rise to thermo-electricity. In this chapter, we discuss first the thermal conductivity for metals, semiconductors and insulators and then consider the coupling between electrical and thermal transport which gives rise to thermoelectric phenomena. In Chapter 6, we discuss scattering mechanisms for electrons and phonons.

## 5.2 Thermal Conductivity

### 5.2.1 General Considerations

Thermal transport, like electrical transport follows from the Boltzmann equation. We will first derive a general expression for the electronic contribution to the thermal conductivity using Boltzmann's equation. We will then apply this general expression to find the thermal conductivity for metals and then for semiconductors. The total thermal conductivity $\overleftrightarrow{\kappa}$ of any material is, of course, the superposition of the electronic part $\overleftrightarrow{\kappa}_e$ with the lattice part $\overleftrightarrow{\kappa}_L$:

```{math}
:label: eq-p1-ch05-1
\overleftrightarrow{\kappa} = \overleftrightarrow{\kappa}_e + \overleftrightarrow{\kappa}_L .
```

We now consider the calculation of the electronic contribution to the thermal conductivity. The contribution of the phonons to the thermal conductivity is considered in §5.2.4. The application of a temperature gradient to a solid gives rise to a flow of heat. We define $\vec{U}$ as the thermal current that is driven by the heat energy $E - E_F$, which in turn is the excess energy of an electron above the equilibrium energy $E_F$. Neglecting time dependent effects, we define $\vec{U}$ as

```{math}
:label: eq-p1-ch05-2
\vec{U} = \frac{1}{4\pi^3}\int \vec{v}\,(E - E_F)\, f(\vec{r},\vec{k})\, d^3k
```

where the distribution function $f(\vec{r},\vec{k})$ is related to the Fermi function $f_0$ by $f = f_0 + f_1$. Under equilibrium conditions there is no thermal current density

```{math}
:label: eq-p1-ch05-3
\int \vec{v}\,(E - E_F)\, f_0\, d^3k = 0
```

so that the thermal current is driven by the thermal gradient which causes a departure from the equilibrium distribution:

```{math}
:label: eq-p1-ch05-4
\vec{U} = \frac{1}{4\pi^3}\int \vec{v}\,(E - E_F)\, f_1\, d^3k
```

where the electronic contribution to the thermal conductivity tensor $\overleftrightarrow{\kappa}_e$ is defined by the relation

```{math}
:label: eq-p1-ch05-5
\vec{U} = -\overleftrightarrow{\kappa}_e \cdot \frac{\partial T}{\partial \vec{r}} .
```

Assuming no explicit time dependence for the distribution function, the function $f_1$ representing the departure of the distribution from equilibrium is found from solution of Boltzmann's equation

```{math}
:label: eq-p1-ch05-6
\vec{v}\cdot\frac{\partial f}{\partial \vec{r}} + \dot{\vec{k}}\cdot\frac{\partial f}{\partial \vec{k}} = -\frac{f_1}{\tau}
```

for a time independent temperature gradient. In the absence of an electric field, $\dot{\vec{k}} = 0$ and the drift velocity $\vec{v}$ is found from the equation

```{math}
:label: eq-p1-ch05-7
\vec{v}\cdot\frac{\partial f}{\partial \vec{r}} = -\frac{f_1}{\tau} .
```

Using the linear approximation for the term $\partial f/\partial\vec{r}$ in the Boltzmann equation, we obtain

```{math}
:label: eq-p1-ch05-8
\frac{\partial f}{\partial \vec{r}} \simeq \frac{\partial f_0}{\partial \vec{r}}
= \frac{\partial}{\partial \vec{r}}\left[ \frac{1}{1 + e^{(E-E_F)/k_B T}} \right]
= \left\{ -\frac{e^{(E-E_F)/k_B T}}{[1 + e^{(E-E_F)/k_B T}]^2} \right\}
\left\{ -\frac{1}{k_B T}\frac{\partial E_F}{\partial \vec{r}}
- \frac{(E-E_F)}{k_B T^2}\frac{\partial T}{\partial \vec{r}} \right\}
= \left\{ k_B T\,\frac{\partial f_0}{\partial E} \right\}
\left\{ -\frac{1}{k_B T}\frac{\partial T}{\partial \vec{r}} \right\}
\left\{ \frac{\partial E_F}{\partial T} + \frac{(E-E_F)}{T} \right\}
= -\frac{\partial f_0}{\partial E}
\left\{ \frac{\partial E_F}{\partial T} + \frac{(E-E_F)}{T} \right\}
\frac{\partial T}{\partial \vec{r}} .
```

We will now give some typical values for these two terms for semiconductors and metals. For semiconductors, we evaluate the expression in {eq}`eq-p1-ch05-8` by referring to {eq}`eq-p1-ch04-75`

```{math}
:label: eq-p1-ch05-9
E_F = \frac{1}{2}E_g - \frac{3}{4}k_B T \ln(m_h/m_e)
```

from which

```{math}
:label: eq-p1-ch05-10
\frac{\partial E_F}{\partial T} \simeq \frac{3}{4}k_B \ln(m_h/m_e)
```

showing that the temperature dependence of $E_F$ arises from the inequality of the valence and conduction band effective masses. If $m_h = m_e$, which would be the case of strongly coupled "mirror" bands, then $\partial E_F/\partial T$ would vanish. For a significant mass difference such as $m_h/m_e = 2$, we obtain $\partial E_F/\partial T \sim 0.5\,k_B$ from {eq}`eq-p1-ch05-10`. For a band gap of $0.5$ eV and the Fermi level in the middle of the gap, we obtain for the other term in {eq}`eq-p1-ch05-8`

```{math}
:label: eq-p1-ch05-11
\frac{(E-E_F)}{T} \approx \left[\frac{0.5}{1/40}\right]k_B = 20\,k_B
```

where $k_B T \approx 1/40$ eV at room temperature. Thus for a semiconductor, the term $(E-E_F)/T$ is much larger than the term $(\partial E_F/\partial T)$.

For a metal with a spherical Fermi surface, the following relation

```{math}
:label: eq-p1-ch05-12
E_F = E_F^0 - \frac{\pi^2}{12}\frac{(k_B T)^2}{E_F^0}
```

is derived in standard textbooks on statistical mechanics, so that at room temperature and assuming that for a typical metal $E_F^0 = 5$ eV, we obtain from {eq}`eq-p1-ch05-12`

```{math}
:label: eq-p1-ch05-13
\frac{\partial E_F}{\partial T}
= \frac{\pi^2}{6}\frac{k_B T}{E_F^0}\,k_B
\approx \frac{10}{6}\left(\frac{1}{40}\right)^5 k_B
\approx 8\times 10^{-3} k_B .
```

Thus, for both semiconductors and metals, the term $(E - E_F)/T$ tends to dominate over $(\partial E_F/\partial T)$, though there can be situations where the term $(\partial E_F/\partial T)$ cannot be neglected. In this presentation, we will temporarily neglect the term $\vec{\nabla}E_F$ in {eq}`eq-p1-ch05-8` in calculation of the electronic contribution to the thermal conductivity, but we will include this term formally in our derivation of thermoelectric effects in §5.3.

Typically, the electron energies of importance in any transport problem are those within $k_B T$ of the Fermi energy so that for many applications for metals, we can make the rough approximation,

```{math}
:label: eq-p1-ch05-14
\frac{E - E_F}{T} \approx k_B
```

though the results given in this section are derived without the above approximation for $(E - E_F)/T$. Rather, all integrations are carried out in terms of the variable $(E - E_F)/T$.

We return now to the solution of the Boltzmann equation in the relaxation time approximation

```{math}
:label: eq-p1-ch05-15
\frac{\partial f}{\partial \vec{r}} =
\left[ -\frac{\partial f_0}{\partial E} \right]
\left[ \frac{E-E_F}{T} \right]
\left[ \frac{\partial T}{\partial \vec{r}} \right] .
```

Solution of the Boltzmann equation yields

```{math}
:label: eq-p1-ch05-16
f_1 = -\tau\vec{v}\cdot\left[\frac{\partial f}{\partial \vec{r}}\right]
= \tau\vec{v}\left[\frac{\partial f_0}{\partial E}\right]
\left[\frac{E-E_F}{T}\right]\frac{\partial T}{\partial \vec{r}} .
```

Substitution of $f_1$ in the equation for the thermal current $\vec{U}$

```{math}
:label: eq-p1-ch05-17
\vec{U} = \frac{1}{4\pi^3}\int \vec{v}\,(E-E_F)\,f_1\,d^3k
```

then results in

```{math}
:label: eq-p1-ch05-18
\vec{U} = \frac{1}{4\pi^3 T}\left[\frac{\partial T}{\partial \vec{r}}\right]\cdot
\int \tau\,\vec{v}\,\vec{v}\,(E-E_F)^2
\left[\frac{\partial f_0}{\partial E}\right] d^3k .
```

Using the definition of the thermal conductivity tensor $\overleftrightarrow{\kappa}_e$ given by {eq}`eq-p1-ch05-5` we write the electronic contribution to the thermal conductivity $\overleftrightarrow{\kappa}_e$ as

```{math}
:label: eq-p1-ch05-19
\overleftrightarrow{\kappa}_e = -\frac{1}{4\pi^3 T}
\int \tau\,\vec{v}\,\vec{v}\,(E-E_F)^2
\left[\frac{\partial f_0}{\partial E}\right] d^3k
```

where $d^3k = d^2S\,dk_\perp = d^2S\,dE/|\partial E/\partial\vec{k}| = d^2S\,dE/(\hbar v)$ is used to exploit our knowledge of the dependence of the distribution function on the energy as discussed below.

### 5.2.2 Thermal Conductivity for Metals

In the case of a metal, the integral for $\overleftrightarrow{\kappa}_e$ given by {eq}`eq-p1-ch05-19` can be evaluated easily by converting the integral over phase space $\int d^3k$ to an integral over $\int dE\,d^2S_F$ in order to exploit the $\delta$-function property of $(-\partial f_0/\partial E)$. We then make use of the following result that you will show for homework and can be found in any standard statistical mechanics text (see for example, Reif)

```{math}
:label: eq-p1-ch05-20
\int G(E)\left[-\frac{\partial f_0}{\partial E}\right]dE
= G(E_F) + \frac{\pi^2}{6}(k_B T)^2 G''(E_F) + \cdots
```

It is necessary to consider the expansion given in {eq}`eq-p1-ch05-20` in solving {eq}`eq-p1-ch05-19` since $G(E_F)$ vanishes at $E = E_F$ for the integral defined in {eq}`eq-p1-ch05-19` for $\overleftrightarrow{\kappa}_e$. To solve the integral equation of {eq}`eq-p1-ch05-19` we make the identification of

```{math}
:label: eq-p1-ch05-21
G(E) = g(E)(E-E_F)^2
```

where

```{math}
:label: eq-p1-ch05-22
g(E) = \frac{1}{4\pi^3}\int \tau\,\vec{v}\,\vec{v}\,\frac{d^2S}{\hbar v}
```

so that $G(E_F) = 0$ and $({\partial G}/{\partial E})|_{E_F} = 0$ while

```{math}
:label: eq-p1-ch05-23
G''(E_F) = 2g(E_F) .
```

These relations will be used again in connection with the calculation of the thermopower in §5.3.1. For the case of the thermal conductivity for a metal we then obtain

```{math}
:label: eq-p1-ch05-24
\overleftrightarrow{\kappa}_e = \frac{\pi^2}{3}(k_B T)^2 g(E_F)
= \frac{(k_B T)^2}{12\pi\hbar}\int_{\text{Fermi surface}} \frac{\tau\,\vec{v}\,\vec{v}\,d^2S}{v}
```

where the integration is over the Fermi surface. We immediately recognize that the integral appearing in {eq}`eq-p1-ch05-24` is the same as that for the electrical conductivity (see {eq}`eq-p1-ch04-26` and {eq}`eq-p1-ch04-29`)

```{math}
:label: eq-p1-ch05-25
\overleftrightarrow{\sigma} = \frac{e^2}{4\pi^3\hbar}\int_{\text{Fermi surface}} \frac{\tau\,\vec{v}\,\vec{v}\,d^2S}{v}
```

so that the electronic contribution to the thermal conductivity and the electrical conductivity tensors are proportional to each other

```{math}
:label: eq-p1-ch05-26
\overleftrightarrow{\kappa}_e = \overleftrightarrow{\sigma}\,T\,\frac{\pi^2 k_B^2}{3 e^2}
```

and {eq}`eq-p1-ch05-26` is known as the Wiedemann-Franz Law. The physical basis for this relation is that in electrical conduction each electron carries a charge $e$ and experiences an electrical force $e\vec{E}$ so that the electrical current per unit field is $e^2$. In thermal conduction, each electron carries a unit of thermal energy $k_B T$ and experiences a thermal force $k_B\partial T/\partial\vec{r}$ so that the heat current per unit thermal gradient is proportional to $k_B^2 T$. Therefore the ratio of $|\kappa_e|/|\sigma|$ must be on the order of $(k_B^2 T^2/e^2)$. The Wiedemann-Franz law suggests that the ratio $\kappa_e/(\sigma T)$ should be a constant (called the Lorenz number), independent of materials properties

```{math}
:label: eq-p1-ch05-27
\frac{\overleftrightarrow{\kappa}_e}{\overleftrightarrow{\sigma}T}
= \frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2
= 2.45\times 10^{-8}\ \mathrm{W}/(\Omega\cdot\mathrm{deg}^2) .
```

The ratio $(\kappa_e/\sigma T)$ is approximately constant for all metals at high temperatures $T > \Theta_D$ and at very low temperatures $T \ll \Theta_D$, where $\Theta_D$ is the Debye temperature. The derivation of the Wiedemann-Franz Law depends on the relaxation time approximation, which is valid at high temperatures $T > \Theta_D$ where the electron scattering is dominated by the quasi-elastic phonon scattering process and is valid also at very low temperatures $T \ll \Theta_D$ where phonon scattering is unimportant and the dominant scattering mechanism is impurity and lattice defect scattering, both of which tend to be elastic scattering processes. These scattering processes are discussed in Chapter 6 where we discuss in more detail the temperature dependence for $\kappa$. When specific scattering processes are considered in detail, the value of the Lorenz number may change.

The temperature dependence of the thermal conductivity of a metal is given in {numref}`fig-p1-ch05-1`. From {eq}`eq-p1-ch05-27` we can write the following relation for the electronic contribution to the thermal conductivity $\kappa_e$ when the Wiedemann-Franz law is satisfied

```{math}
:label: eq-p1-ch05-28
\kappa_e = \left[\frac{n e^2\tau}{m^*}\right] T\,\frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2 .
```

At very low temperatures where scattering by impurities, defects, crystal boundaries is dominant, $\sigma$ is independent of $T$ and therefore from the Wiedemann-Franz law, $\kappa_e \sim T$. At somewhat higher temperatures, but still in the regime $T \ll \Theta_D$, electron-phonon scattering starts to dominate and $\kappa_e$ starts to decrease. In this regime, the electrical conductivity exhibits a $T^{-5}$ dependence. However only small $q$ phonons participate in this regime. Thus it is only the phonon density which increases as $T^3$ that is relevant to the phonon-electron scattering, thereby yielding an electrical resistivity with a $T^3$ dependence and a conductivity with a $T^{-3}$ dependence. Using {eq}`eq-p1-ch05-28`, we thus find that in the low $T$ range, where only low $q$ phonons participate in thermal transport, $\kappa_e$ should show a $T^{-2}$ dependence, in agreement with {numref}`fig-p1-ch05-1`. At high $T$ where all the phonons contribute to thermal transport, we have $\sigma \sim 1/T$ so that $\kappa_e$ becomes independent of $T$. Since $\Theta_D \sim 300$ K for Cu, this temperature range far exceeds the upper limit of {numref}`fig-p1-ch05-1`.

:::{figure} images/fig-p1-ch05-1.png
:name: fig-p1-ch05-1
:align: center
:width: 80%

The temperature dependence of the thermal conductivity of copper. Note that both $\kappa$ and $T$ are plotted on linear scales. At low temperatures where the phonon density is low, the thermal transport is by electrons predominantly, while at high temperatures, thermal transport by phonons becomes more important.
:::

### 5.2.3 Thermal Conductivity for Semiconductors

For the case of non-degenerate semiconductors, the integral for $\overleftrightarrow{\kappa}_e$ in {eq}`eq-p1-ch05-19` is evaluated by replacing $(E - E_F) \to E$, since in a semiconductor the electrons that can conduct heat must be in the conduction band, and the lowest energy an electron can have in the thermal conduction process is at the conduction band minimum which is taken as the zero of energy in these calculations. Then the thermal conductivity for a non-degenerate semiconductor can be written as

```{math}
:label: eq-p1-ch05-29
\overleftrightarrow{\kappa}_e = \frac{1}{4\pi^3 T}
\int \tau\,\vec{v}\,\vec{v}\,E^2
\left[-\frac{\partial f_0}{\partial E}\right] d^3k .
```

For intrinsic semiconductors, the Fermi distribution function can normally be approximated by the Maxwell-Boltzmann distribution so that

```{math}
:label: eq-p1-ch05-30
\frac{\partial f_0}{\partial E} \to -\frac{1}{k_B T}
e^{-|E_{F,e}|/k_B T}\, e^{-E/k_B T} ,
```

assuming that the doping level is not high enough to push $E_F$ close to the band edge (band extremum) or into the conduction band to produce a degenerate semiconductor. For a parabolic band we have $E = \hbar^2 k^2/2m^*$, so that the volume element in reciprocal space can be written as

```{math}
:label: eq-p1-ch05-31
\int d^3k = \int 4\pi k^2\,dk
= \int_0^\infty 2\pi(2m^*/\hbar^2)^{3/2} E^{1/2}\,dE ,
```

and $\vec{v} = (1/\hbar)(\partial E/\partial\vec{k}) = \hbar\vec{k}/m^*$. Assuming a constant relaxation time, we then substitute all these terms into {eq}`eq-p1-ch05-29` for $\overleftrightarrow{\kappa}_e$ and integrate to obtain

```{math}
:label: eq-p1-ch05-32
\kappa_{e,xx} = \frac{1}{4\pi^3 T}\int \tau v_x^2 E^2
(k_B T)^{-1} e^{-|E_{F,e}|/k_B T} e^{-E/k_B T}
\,2\pi(2m^*/\hbar^2)^{3/2} E^{1/2}\,dE
= \left[\frac{k_B(k_B T)\tau}{3\pi^2 m^*}\right]
\left(\frac{2m^* k_B T}{\hbar^2}\right)^{3/2}
e^{-|E_{F,e}|/k_B T}\int_0^\infty x^{7/2} e^{-x}\,dx
```

where $\int_0^\infty x^{7/2}e^{-x}dx = 105\sqrt{\pi}/8$, from which it follows that $\kappa_{e,xx}$ has a temperature dependence of the form

```{math}
:label: eq-p1-ch05-33
T^{5/2}\, e^{-|E_{F,e}|/k_B T}
```

in which the exponential term is dominant for temperatures of physical interest, where $k_B T \ll |E_{F,e}|$. We note from {eq}`eq-p1-ch04-42` that for a semiconductor, the temperature dependence of the electrical conductivity is given by

```{math}
:label: eq-p1-ch05-34
\sigma_{xx} = \frac{2e^2\tau}{m^*}
\left(\frac{m^* k_B T}{2\pi\hbar^2}\right)^{3/2} e^{-|E_{F,e}|/k_B T} .
```

Assuming cubic symmetry, we can write the conductivity tensor as

```{math}
:label: eq-p1-ch05-35
\overleftrightarrow{\sigma} =
\begin{pmatrix}
\sigma_{xx} & 0 & 0 \\
0 & \sigma_{xx} & 0 \\
0 & 0 & \sigma_{xx}
\end{pmatrix}
```

so that the electronic contribution to the thermal conductivity of a semiconductor can be written as

```{math}
:label: eq-p1-ch05-36
\kappa_{e,xx} = \frac{35}{2}\frac{k_B^2}{e^2}\,\sigma_{xx} T
```

where

```{math}
:label: eq-p1-ch05-37
\sigma_{xx} = \frac{n e^2\tau}{m_{xx}} = n e\,\mu_{xx}
```

and we note that the coefficient $(35/2)$ for this calculation for semiconductors is different from the corresponding coefficient $(\pi^2/3)$ for metals (see {eq}`eq-p1-ch05-27`). Except for numerical constants, the formal results relating the electronic contribution to the thermal conductivity $\kappa_{e,xx}$ and $\sigma_{xx}$ are similar for metals and semiconductors, with the electronic thermal conductivity and electrical conductivity being proportional.

A major difference between semiconductors and metals is the magnitude of the electrical conductivity and hence of the electronic contribution to the thermal conductivity. Since $\sigma_{xx}$ is much smaller for semiconductors than for metals, $\kappa_e$ for semiconductors is relatively unimportant and the thermal conductivity tends to be dominated by the lattice contribution $\kappa_L$.

### 5.2.4 Thermal Conductivity for Insulators

In the case of insulators, heat is only carried by phonons (lattice vibrations). The thermal conductivity in insulators therefore depends on phonon scattering mechanisms (see Chapter 6). The lattice thermal conductivity is calculated from kinetic theory and is given by

```{math}
:label: eq-p1-ch05-38
\kappa_L = \frac{C_p\, v_q\,\Lambda_{ph}}{3}
```

where $C_p$ is the heat capacity, $v_q$ is the average phonon velocity and $\Lambda_{ph}$ is the phonon mean free path.

As discussed above, the total thermal conductivity of a solid is given as the sum of the lattice contribution $\kappa_L$ and the electronic contribution $\kappa_e$. For metals the electronic contribution dominates, while for insulators and semiconductors the phonon contribution dominates.

Let us now consider the temperature dependence of $\kappa_{e,xx}$ (see {numref}`fig-p1-ch05-2`) for heat conduction by phonons. At very low $T$ in the defect scattering range, the heat capacity has a dependence $C_p \propto T^3$ while $v_q$ and $\Lambda_{ph}$ are almost independent of $T$. As $T$ increases and we enter the phonon-phonon scattering regime due to normal scattering processes and involving only low $q$ phonons, $C_p$ is still increasing with $T$ but the increase is slower than $T^3$, while $v_q$ remains independent of $T$ and $\Lambda_{ph}$. As $T$ increases further, the thermal conductivity increases more and more gradually and eventually starts to decrease because of phonon-phonon scattering events, for which the density of phonons available for scattering depends on the Bose-Einstein factor $[\exp(\hbar\omega/k_B T) - 1]$. This causes a peak in $\kappa_L(T)$. The decrease in $\kappa_L(T)$ becomes more pronounced as $C_p$ becomes independent of $T$ and $\Lambda_{ph}$ continues to be proportional to $[\exp(\hbar\bar{\omega}/k_B T) - 1]$ where $\bar{\omega}$ is a typical phonon frequency (see §6.4.1). As $T$ increases further, we eventually enter the $T \gg \Theta_D$ regime, where $\Theta_D$ is the Debye temperature. In this regime, the temperature dependence of $\Lambda_{ph}$ simply becomes $\Lambda_{ph} \sim (1/T)$. Referring to {numref}`fig-p1-ch05-2` for $\kappa(T)$ for NaF we see that the peak in $\kappa$ occurs at about 18 K where the complete Bose-Einstein factor $[\exp(\hbar\bar{\omega}/k_B T) - 1]$ must be used to describe the $T$ dependence of $\kappa_L$. For much of the temperature range in {numref}`fig-p1-ch05-2`, only low $q$ phonons participate in the thermal conduction process. At higher temperatures where larger $q$ phonons contribute to thermal conduction, umklapp processes become important in the phonon scattering process, as discussed in §6.3.1. The discussion in this section also applies to the lattice contribution to the thermal conductivity for metals, semimetals and semiconductors.

:::{figure} images/fig-p1-ch05-2.png
:name: fig-p1-ch05-2
:align: center
:width: 80%

Temperature dependence of the thermal conductivity of a highly purified insulating crystal of NaF. Note that both $\kappa$ and $T$ are plotted on a log scale, and that the peak in $\kappa$ occurs at quite a low temperature ($\sim 17$ K). The temperature dependence of $\kappa$ is further discussed in §6.4.
:::

## 5.3 Thermoelectric Phenomena

In many metals and semiconductors there exists a coupling between the electrical current and the thermal current. This coupling can be appreciated by observing that when electrons carry thermal current, they are also transporting charge and therefore generating electric fields. This coupling between the charge transport and heat transport gives rise to thermoelectric phenomena. In our discussion of thermoelectric phenomena we start with a general derivation of the coupled equations for the electrical current density $\vec{j}$ and the thermal current density $\vec{U}$:

```{math}
:label: eq-p1-ch05-39
\vec{j} = \frac{e}{4\pi^3}\int \vec{v}\,f_1\,d^3k
```

```{math}
:label: eq-p1-ch05-40
\vec{U} = \frac{1}{4\pi^3}\int \vec{v}\,(E-E_F)\,f_1\,d^3k
```

and the perturbation to the distribution function $f_1$ is found from solution of Boltzmann's equation in the relaxation time approximation:

```{math}
:label: eq-p1-ch05-41
\vec{v}\cdot\frac{\partial f}{\partial \vec{r}} + \dot{\vec{k}}\cdot\frac{\partial f}{\partial \vec{k}}
= -\frac{(f-f_0)}{\tau} ,
```

which is written here for the case of time independent forces and fields. Substituting for $(\partial f/\partial\vec{r})$ from {eq}`eq-p1-ch05-8` and {eq}`eq-p1-ch05-15`, for $\partial f/\partial\vec{k}$ from {eq}`eq-p1-ch04-17`, and for $\partial f/\partial\vec{k} = (\partial f_0/\partial E)(\partial E/\partial\vec{k})$ yields

```{math}
:label: eq-p1-ch05-42
\vec{v}\cdot\left(\frac{\partial f_0}{\partial E}\right)
\cdot\left( e\vec{E} - \vec{\nabla}E_F \right)
- \frac{(E-E_F)}{T}\left(\vec{\nabla}T\right)
= -\frac{f_1}{\tau} ,
```

so that the solution to the Boltzmann equation in the presence of an electric field and a temperature gradient is

```{math}
:label: eq-p1-ch05-43
f_1 = \vec{v}\tau\cdot\left(\frac{\partial f_0}{\partial E}\right)
\left[ \frac{(E-E_F)}{T}\vec{\nabla}T - e\vec{E} + \vec{\nabla}E_F \right] ,
```

in which $e$ is negative for electrons and positive for holes. The electrical and thermal currents in the presence of both an applied electric field and a temperature gradient can thus be obtained by substituting $f_1$ into $\vec{j}$ and $\vec{U}$ in {eq}`eq-p1-ch05-39` and {eq}`eq-p1-ch05-40` to yield expressions of the form:

```{math}
:label: eq-p1-ch05-44
\vec{j} = e^2 \overleftrightarrow{\kappa}_0\cdot
\left(\vec{E} - \frac{1}{e}\vec{\nabla}E_F\right)
- \frac{e}{T}\overleftrightarrow{\kappa}_1\cdot\vec{\nabla}T
```

and

```{math}
:label: eq-p1-ch05-45
\vec{U} = e\,\overleftrightarrow{\kappa}_1\cdot
\left(\vec{E} - \frac{1}{e}\vec{\nabla}E_F\right)
- \frac{1}{T}\overleftrightarrow{\kappa}_2\cdot\vec{\nabla}T
```

where $\overleftrightarrow{\kappa}_0$ is related to the conductivity tensor $\overleftrightarrow{\sigma}$ by

```{math}
:label: eq-p1-ch05-46
\overleftrightarrow{\kappa}_0 = \frac{1}{4\pi^3}\int \tau\,\vec{v}\,\vec{v}
\left(-\frac{\partial f_0}{\partial E}\right)d^3k = \frac{\overleftrightarrow{\sigma}}{e^2} ,
```

and

```{math}
:label: eq-p1-ch05-47
\overleftrightarrow{\kappa}_1 = \frac{1}{4\pi^3}\int \tau\,\vec{v}\,\vec{v}\,(E-E_F)
\left(-\frac{\partial f_0}{\partial E}\right)d^3k ,
```

and $\overleftrightarrow{\kappa}_2$ is related to the thermal conductivity tensor $\overleftrightarrow{\kappa}_e$ by

```{math}
:label: eq-p1-ch05-48
\overleftrightarrow{\kappa}_2 = \frac{1}{4\pi^3}\int \tau\,\vec{v}\,\vec{v}\,(E-E_F)^2
\left(-\frac{\partial f_0}{\partial E}\right)d^3k = T\,\overleftrightarrow{\kappa}_e .
```

Note that the integrands for $\overleftrightarrow{\kappa}_1$ and $\overleftrightarrow{\kappa}_2$ are both related to that for $\overleftrightarrow{\kappa}_0$ by introducing factors of $(E-E_F)$ and $(E-E_F)^2$, respectively. Note also that the same integral $\overleftrightarrow{\kappa}_1$ occurs in the expression for the electric current $\vec{j}$ induced by a thermal gradient $\vec{\nabla}T$ and in the expression for the thermal current $\vec{U}$ induced by an electric field $\vec{E}$. The motion of charged carriers across a temperature gradient results in a flow of electric current expressed by the term $-(e/T)(\overleftrightarrow{\kappa}_1)\cdot\vec{\nabla}T$. This term is the origin of thermoelectric effects.

The discussion up to this point has been general. If specific boundary conditions are imposed, we obtain a variety of thermoelectric effects such as the Seebeck effect, the Peltier effect and the Thomson effect. We now define the conditions under which each of these thermoelectric effects occur.

### 5.3.1 Thermoelectric Phenomena in Metals

All thermoelectric effects in metals depend on the tensor $\overleftrightarrow{\kappa}_1$ which we evaluate below for the case of a metal.

```{math}
:label: eq-p1-ch05-49
\vec{j} = 0 = e^2 \overleftrightarrow{\kappa}_0\cdot
\left(\vec{E} - \frac{1}{e}\vec{\nabla}E_F\right)
- \frac{e}{T}\overleftrightarrow{\kappa}_1\cdot\vec{\nabla}T
```

so that the Seebeck coefficient $\overleftrightarrow{S}$ is defined by

```{math}
:label: eq-p1-ch05-50
\vec{E} - \frac{1}{e}\vec{\nabla}E_F
= \frac{1}{eT}\overleftrightarrow{\kappa}_0^{-1}\cdot
\overleftrightarrow{\kappa}_1\cdot\vec{\nabla}T
\equiv \overleftrightarrow{S}\cdot\vec{\nabla}T ,
```

and $S$ is sometimes called the thermopower. Using the relation $\vec{\nabla}E_F = (\partial E_F/\partial T)\vec{\nabla}T$ we obtain the definition for the Thomson coefficient $T_b$

```{math}
:label: eq-p1-ch05-51
\vec{E} = \left[ \frac{1}{e}\frac{\partial E_F}{\partial T} + \overleftrightarrow{S} \right]\vec{\nabla}T
\equiv \overleftrightarrow{T}_b\cdot\vec{\nabla}T
```

where

```{math}
:label: eq-p1-ch05-52
\overleftrightarrow{T}_b = T\frac{\partial \overleftrightarrow{S}}{\partial T} .
```

For many thermoelectric systems of interest, $\overleftrightarrow{S}$ has a linear temperature dependence, and in this case it follows from {eq}`eq-p1-ch05-52` that $\overleftrightarrow{T}_b$ and $\overleftrightarrow{S}$ for such systems are almost equivalent for practical purposes. Therefore the Seebeck and Thomson coefficients are used almost interchangeably in the literature.

From {eq}`eq-p1-ch05-50` and neglecting the term in $\vec{\nabla}E_F$, as is usually done, we have

```{math}
:label: eq-p1-ch05-53
\overleftrightarrow{S} = \frac{1}{eT}\overleftrightarrow{\kappa}_0^{-1}\cdot\overleftrightarrow{\kappa}_1
```

which is simplified by assuming an isotropic medium, yielding the scalar quantities

```{math}
:label: eq-p1-ch05-54
S = \frac{1}{eT}\frac{\kappa_1}{\kappa_0} .
```

However in an anisotropic medium, the tensor components of $\overleftrightarrow{S}$ are found from

```{math}
:label: eq-p1-ch05-55
S_{ij} = \frac{1}{eT}(\kappa_0^{-1})_{i\alpha}(\kappa_1)_{\alpha j} ,
```

where the Einstein summation convention is assumed. {numref}`fig-p1-ch05-3` shows a schematic diagram for measuring the thermopower or Seebeck effect in an n-type semiconductor. At the hot junction the Fermi level is higher than at the cold junction. Electrons will move from the hot junction to the cold junction in an attempt to equalize the Fermi level, thereby creating an electric field which can be measured in terms of the open circuit voltage $V$ shown in {numref}`fig-p1-ch05-3`.

Another important thermoelectric coefficient is the Peltier coefficient $\overleftrightarrow{\Pi}$, defined as the proportionality between $\vec{U}$ and $\vec{j}$

```{math}
:label: eq-p1-ch05-56
\vec{U} \equiv \overleftrightarrow{\Pi}\cdot\vec{j}
```

in the absence of a thermal gradient. For $\vec{\nabla}T = 0$, {eq}`eq-p1-ch05-44` and {eq}`eq-p1-ch05-45` become

```{math}
:label: eq-p1-ch05-57
\vec{j} = e^2 \overleftrightarrow{\kappa}_0\cdot
\left(\vec{E} - \frac{1}{e}\vec{\nabla}E_F\right)
```

:::{figure} images/fig-p1-ch05-3.png
:name: fig-p1-ch05-3
:align: center
:width: 70%

Determination of the Seebeck effect for an n-type semiconductor. In the presence of a temperature gradient, electrons will move from the hot junction to the cold junction, thereby creating an electric field and a voltage $V$ across the semiconductor.
:::

```{math}
:label: eq-p1-ch05-58
\vec{U} = e\,\overleftrightarrow{\kappa}_1\cdot
\left(\vec{E} - \frac{1}{e}\vec{\nabla}E_F\right)
```

so that

```{math}
:label: eq-p1-ch05-59
\vec{U} = \frac{1}{e}\overleftrightarrow{\kappa}_1\cdot
(\overleftrightarrow{\kappa}_0)^{-1}\cdot\vec{j}
= \overleftrightarrow{\Pi}\cdot\vec{j}
```

where

```{math}
:label: eq-p1-ch05-60
\overleftrightarrow{\Pi} = \frac{1}{e}\overleftrightarrow{\kappa}_1\cdot
(\overleftrightarrow{\kappa}_0)^{-1} .
```

Comparing {eq}`eq-p1-ch05-53` and {eq}`eq-p1-ch05-60` we see that $\overleftrightarrow{\Pi}$ and $\overleftrightarrow{S}$ are related by

```{math}
:label: eq-p1-ch05-61
\overleftrightarrow{\Pi} = T\,\overleftrightarrow{S} ,
```

where $T$ is the temperature. For isotropic materials the Peltier coefficient thus becomes a scalar, and is proportional to the thermopower $S$:

```{math}
:label: eq-p1-ch05-62
\Pi = \frac{1}{e}\frac{\kappa_1}{\kappa_0} = T S ,
```

while for anisotropic materials the tensor components of $\overleftrightarrow{\Pi}$ can be found in analogy with {eq}`eq-p1-ch05-55`. We note that both $\overleftrightarrow{S}$ and $\overleftrightarrow{\Pi}$ exhibit a linear dependence on $e$ and therefore depend explicitly on the sign of the carrier, and measurements of $\overleftrightarrow{S}$ or $\overleftrightarrow{\Pi}$ can be used to determine whether transport is dominated by electrons or holes.

We have already considered the evaluation of $\overleftrightarrow{\kappa}_0$ in treating the electrical conductivity and $\overleftrightarrow{\kappa}_2$ in treating the thermal conductivity. To treat thermoelectric phenomena we need now to evaluate $\overleftrightarrow{\kappa}_1$

```{math}
:label: eq-p1-ch05-63
\overleftrightarrow{\kappa}_1 = \frac{1}{4\pi^3}\int \tau\,\vec{v}\,\vec{v}\,(E-E_F)
\left(-\frac{\partial f_0}{\partial E}\right)d^3k .
```

In §5.3.1 we evaluate $\overleftrightarrow{\kappa}_1$ for the case of a metal and in §5.3.2 we evaluate $\overleftrightarrow{\kappa}_1$ for the case of the electrons in an intrinsic semiconductor. In practice, the thermopower is of interest for heavily doped semiconductors, which are either degenerate with the Fermi level in the conduction or valence band or very close to these band edges. A thermoelectric device has both n-type and p-type legs or constituents.

We can then obtain the thermopower

```{math}
:label: eq-p1-ch05-64
\overleftrightarrow{S} = \frac{1}{eT}\left(\overleftrightarrow{\kappa}_1\cdot\overleftrightarrow{\kappa}_0^{-1}\right)
```

or the Peltier coefficient

```{math}
:label: eq-p1-ch05-65
\overleftrightarrow{\Pi} = \frac{1}{e}\left(\overleftrightarrow{\kappa}_1\cdot\overleftrightarrow{\kappa}_0^{-1}\right)
```

or the Thomson coefficient

```{math}
:label: eq-p1-ch05-66
\overleftrightarrow{T}_b = T\,\frac{\partial \overleftrightarrow{S}}{\partial T} .
```


To evaluate $\overleftrightarrow{\kappa}_1$ for metals we wish to exploit the $\delta$-function behavior of $(-\partial f_0/\partial E)$. This is accomplished by converting the integration $d^3k$ to an integration over $dE$ and over a constant energy surface, $d^3k = d^2S\,dE/\hbar v$. From Fermi statistics we have the general relation (see {eq}`eq-p1-ch05-20`)

```{math}
:label: eq-p1-ch05-67
\int G(E)\left[-\frac{\partial f_0}{\partial E}\right]dE
= G(E_F) + \frac{\pi^2}{6}(k_B T)^2 G''(E_F) + \cdots
```

For the integral in {eq}`eq-p1-ch05-63` which defines $\overleftrightarrow{\kappa}_1$, we can write

```{math}
:label: eq-p1-ch05-68
G(E) = g(E)(E-E_F)
```

where

```{math}
:label: eq-p1-ch05-69
g(E) = \frac{1}{4\pi^3}\int \tau\,\vec{v}\,\vec{v}\,\frac{d^2S}{v}
```

and the integration in {eq}`eq-p1-ch05-69` is carried out over a constant energy surface at energy $E$. Differentiation of $G(E)$ then yields

```{math}
:label: eq-p1-ch05-70
G'(E) = g'(E)(E-E_F) + g(E),\qquad
G''(E) = g''(E)(E-E_F) + 2g'(E) .
```

Evaluation at $E = E_F$ yields

```{math}
:label: eq-p1-ch05-71
G(E_F) = 0,\qquad G''(E_F) = 2g'(E_F) .
```

We therefore obtain

```{math}
:label: eq-p1-ch05-72
\overleftrightarrow{\kappa}_1 = \frac{\pi^2}{3}(k_B T)^2 g'(E_F) .
```

We interpret $g'(E_F)$ in {eq}`eq-p1-ch05-72` to mean that the same integral $\overleftrightarrow{\kappa}_0$ which determines the conductivity tensor is evaluated on a constant energy surface $E$, and $g'(E_F)$ is the energy derivative of that integral evaluated at the Fermi energy $E_F$. The temperature dependence of $g'(E_F)$ is related to the temperature dependence of $\tau$, since $v$ is essentially temperature independent. For example, we will see in Chapter 6 that acoustic phonon scattering in the high temperature limit $T \gg \Theta_D$ yields a temperature dependence $\tau \sim T^{-1}$ so that $\overleftrightarrow{\kappa}_1$ in this important case for metals will be proportional to $T$.

For a spherical constant energy surface $E = \hbar^2 k^2/2m^*$ and assuming a relaxation time $\tau$ that is independent of energy, we can readily evaluate {eq}`eq-p1-ch05-72` to obtain

```{math}
:label: eq-p1-ch05-73
g(E) = \frac{\tau}{3\pi^2 m^*}
\left(\frac{2m^*}{\hbar^2}\right)^{3/2} E^{3/2}
```

```{math}
:label: eq-p1-ch05-74
g'(E_F) = \frac{\tau}{2\pi^2 m^*}
\left(\frac{2m^*}{\hbar^2}\right)^{3/2} E_F^{1/2}
```

and

```{math}
:label: eq-p1-ch05-75
\kappa_1 = \frac{\tau}{6m^*}
\left(\frac{2m^*}{\hbar^2}\right)^{3/2} E_F^{1/2}(k_B T)^2 .
```

Using the same approximations, we can write for $\kappa_0$:

```{math}
:label: eq-p1-ch05-76
\kappa_0 = \frac{\tau}{3\pi^2 m^*}
\left(\frac{2m^*}{\hbar^2}\right)^{3/2} E_F^{3/2}
```

so that from {eq}`eq-p1-ch05-67` we have for the Seebeck coefficient

```{math}
:label: eq-p1-ch05-77
S = \frac{\kappa_1}{\kappa_0 e T}
= \frac{\pi^2 k_B}{2e}\frac{k_B T}{E_F} .
```

From {eq}`eq-p1-ch05-77` we see that $S$ exhibits a linear dependence on $T$ and a sensitivity to the sign of the carriers. We note from {eq}`eq-p1-ch05-67` that a low carrier density implies a large $S$ value. Thus degenerate (heavily doped with $n \sim 10^{18}-10^{19}/\mathrm{cm}^3$) semiconductors tend to have higher thermopowers than metals. The derivation given here works as a good approximation for these very heavily doped semiconductors.

### 5.3.2 Thermopower for Intrinsic Semiconductors

In this section we evaluate $\overleftrightarrow{\kappa}_1$ for electrons in an intrinsic or lightly doped semiconductor for illustrative purposes. Intrinsic semiconductors are not important for practical thermoelectric devices since the contributions of electrons and holes to $\overleftrightarrow{\kappa}_1$ are of opposite signs and tend to cancel. Thus it is only heavily doped semiconductors with a single carrier type that are important for thermoelectric applications.

The evaluation of the general expression for the integral $\overleftrightarrow{\kappa}_1$

```{math}
:label: eq-p1-ch05-78
\overleftrightarrow{\kappa}_1 = \frac{1}{4\pi^3}\int \tau\,\vec{v}\,\vec{v}\,(E-E_F)
\left(-\frac{\partial f_0}{\partial E}\right)d^3k
```

is different for semiconductors and metals. Referring to {numref}`fig-p1-ch05-4` for an intrinsic semiconductor we need to make the substitution $(E - E_F) \to E$ in {eq}`eq-p1-ch05-78`, since only conduction electrons can carry heat. The equilibrium distribution function for an intrinsic semiconductor can be written as

```{math}
:label: eq-p1-ch05-79
f_0 = e^{-E/k_B T}\,e^{-|E_{F,e}|/k_B T}
```

so that

```{math}
:label: eq-p1-ch05-80
\frac{\partial f_0}{\partial E} = -\frac{1}{k_B T}\,e^{-E/k_B T}\,e^{-|E_{F,e}|/k_B T} .
```

:::{figure} images/fig-p1-ch05-4.png
:name: fig-p1-ch05-4
:align: center
:width: 60%

Schematic $E$ vs $k$ diagram, showing that $E = 0$ is the lowest electronic energy for heat conduction.
:::

To evaluate $d^3k$ we need to assume a model for $E(\vec{k})$. For simplicity, assume a simple parabolic band

```{math}
:label: eq-p1-ch05-81
E = \frac{\hbar^2 k^2}{2m^*}
```

```{math}
:label: eq-p1-ch05-82
d^3k = 4\pi k^2\,dk
```

so that

```{math}
:label: eq-p1-ch05-83
d^3k = 2\pi\left(\frac{2m^*}{\hbar^2}\right)^{3/2} E^{1/2}\,dE
```

and also

```{math}
:label: eq-p1-ch05-84
\vec{v} = \frac{1}{\hbar}\frac{\partial E}{\partial \vec{k}}
= \frac{\hbar\vec{k}}{m^*} .
```

Substitution into the equation for $\overleftrightarrow{\kappa}_1$ for a semiconductor with the simple $E = \hbar^2 k^2/2m^*$ dispersion relation then yields upon integration

```{math}
:label: eq-p1-ch05-85
\kappa_{1,xx} = \frac{5\tau k_B T}{m^*}
\left(\frac{m^* k_B T}{2\pi\hbar^2}\right)^{3/2}
e^{-|E_{F,e}|/k_B T} .
```

This expression is valid for a semiconductor for which the Fermi level is far from the band edge $(E - E_F) \gg k_B T$. The thermopower is then found by substitution

```{math}
:label: eq-p1-ch05-86
S = \frac{1}{eT}\frac{\kappa_{1,xx}}{\kappa_{0,xx}}
```

where the expression for $\kappa_{0,xx} = \sigma_{xx}/e^2$ is given by {eq}`eq-p1-ch05-46`. We thus obtain the result

```{math}
:label: eq-p1-ch05-87
S = \frac{5}{2}\frac{k_B}{e}
```

which is a constant independent of temperature, independent of the band structure, but sensitive to the sign of the carriers. The calculation in this section was for the contribution of electrons. In an actual intrinsic semiconductor, the contribution of both electrons and holes to $\kappa_1$ must be found. Likewise the calculation for $\kappa_{0,xx}$ would also include contributions from both electrons and holes. Since the contribution to $(1/e)\kappa_{1,xx}$ for holes and electrons are of opposite sign, we can from {eq}`eq-p1-ch05-87` expect that $S$ for holes will cancel $S$ for electrons for an intrinsic semiconductor, while the $\kappa_0$ for holes and electrons will add.

Materials with a high thermopower or Seebeck coefficient are heavily doped degenerate semiconductors for which the Fermi level is close to the band edge and the complete Fermi function must be used. Since $S$ depends on the sign of the charge carriers, thermoelectric materials are doped either heavily doped n-type or heavily doped p-type semiconductors to prevent cancellation of the contribution from electrons and holes, as occurs in intrinsic semiconductors which because of thermal excitations of carriers have equal concentrations of electrons and holes.

### 5.3.3 Effect of Thermoelectricity on the Thermal Conductivity

From the coupled equations given by {eq}`eq-p1-ch05-44` and {eq}`eq-p1-ch05-45` it is seen that the proportionality between the thermal current $\vec{U}$ and the temperature gradient $\vec{\nabla}T$ in the absence of electrical current ($\vec{j} = 0$) contains terms related to $\overleftrightarrow{\kappa}_1$. We now solve {eq}`eq-p1-ch05-44` and {eq}`eq-p1-ch05-45` to find the contribution of the thermoelectric terms to the electronic thermal conductivity. When $\vec{j} = 0$, {eq}`eq-p1-ch05-44` becomes

```{math}
:label: eq-p1-ch05-88
\left(\vec{E} - \frac{1}{e}\vec{\nabla}E_F\right)
= \frac{1}{eT}\overleftrightarrow{\kappa}_0^{-1}\cdot
\overleftrightarrow{\kappa}_1\cdot\vec{\nabla}T
```

so that

```{math}
:label: eq-p1-ch05-89
\vec{U} = -\frac{1}{T}\cdot
\left[ \overleftrightarrow{\kappa}_2
- \overleftrightarrow{\kappa}_1\cdot\overleftrightarrow{\kappa}_0^{-1}\cdot\overleftrightarrow{\kappa}_1 \right]
\cdot\vec{\nabla}T
```

where $\overleftrightarrow{\kappa}_0$, $\overleftrightarrow{\kappa}_1$, and $\overleftrightarrow{\kappa}_2$ are given by {eq}`eq-p1-ch05-46`, {eq}`eq-p1-ch05-47`, and {eq}`eq-p1-ch05-48`, respectively, or

```{math}
:label: eq-p1-ch05-90
\overleftrightarrow{\kappa}_0 = \frac{1}{4\pi^3\hbar}
\int_{\text{Fermi surface}} \frac{\tau\,\vec{v}\,\vec{v}\,d^2S}{v} ,
```

```{math}
:label: eq-p1-ch05-91
\overleftrightarrow{\kappa}_1 = \frac{\pi^2}{3}(k_B T)^2
\left.\frac{\partial \overleftrightarrow{\kappa}_0}{\partial E}\right|_{E_F} ,
```

and

```{math}
:label: eq-p1-ch05-92
\overleftrightarrow{\kappa}_2 = \frac{(k_B T)^2}{12\pi\hbar}
\int_{\text{Fermi surface}} \frac{\tau\,\vec{v}\,\vec{v}\,d^2S}{v} .
```

We now evaluate the contribution to the thermal conductivity from the thermoelectric coupling effects for the case of a metal having a simple dispersion relation

```{math}
:label: eq-p1-ch05-93
E = \frac{\hbar^2 k^2}{2m^*} .
```

In this case where $\tau$ is considered to be independent of $E$, {eq}`eq-p1-ch05-91` and {eq}`eq-p1-ch05-90`, respectively, provide expressions for $\kappa_1$ and $\kappa_0$ from which

```{math}
:label: eq-p1-ch05-94
\frac{1}{T}\overleftrightarrow{\kappa}_1\overleftrightarrow{\kappa}_0^{-1}\overleftrightarrow{\kappa}_1
= \frac{\pi^4 n\tau}{4 m^* k_B^2 T}\left(\frac{k_B T}{E_F}\right)^2
```

so that from {eq}`eq-p1-ch05-28` and {eq}`eq-p1-ch05-94` the total electronic thermal conductivity for the metal becomes

```{math}
:label: eq-p1-ch05-95
\kappa_e = \frac{\pi^2 n\tau}{3 m^* k_B^2 T}
\cdot\left[ 1 - \frac{3\pi^2}{4}\left(\frac{k_B T}{E_F}\right)^2 \right] .
```

For typical metals $(T/T_F) \sim (1/30)$ at room temperature so that the thermoelectric correction term is less than 1%. For highly degenerate semiconductors as are of interest for thermoelectric applications, the complete Fermi function must be considered.

:::{figure} images/fig-p1-ch05-5.png
:name: fig-p1-ch05-5
:align: center
:width: 70%

Thermopower between two different metals showing the principle of operation of a thermocouple under open circuit conditions (i.e., $j = 0$).
:::

## 5.4 Thermoelectric Measurements

### 5.4.1 Seebeck Effect (Thermopower)

The thermopower $S$ as defined in {eq}`eq-p1-ch05-50` and is the characteristic coefficient in the Seebeck effect, where a metal subjected to a thermal gradient $\vec{\nabla}T$ exhibits an electric field $\vec{E} = S\vec{\nabla}T$. The measurements are made under an open-circuit voltage $V$ and under conditions of no current flow.

In the application of the Seebeck effect to thermocouple operation, we usually measure the difference in thermopower $S_A - S_B$ between two different metals $A$ and $B$ by measuring the open circuit voltage $V_{AB}$ as shown in {numref}`fig-p1-ch05-5`. This voltage can be calculated from

```{math}
:label: eq-p1-ch05-96
V_{AB} = -\int_H \vec{E}\cdot d\vec{r}
= -\int_H S\frac{\partial T}{\partial\vec{r}}\,d\vec{r}
= \int_{T_1}^{T_0} S_B\,dT + \int_{T_2}^{T_1} S_A\,dT + \int_{T_0}^{T_2} S_B\,dT
= \int_{T_2}^{T_1} (S_A - S_B)\,dT .
```

With $T_1 \neq T_2$, an open-circuit potential difference $V_{AB}$ can be measured and {eq}`eq-p1-ch05-96` shows that $V_{AB}$ is independent of the temperature $T_0$. Thus if $T_1$ is known and $V_{AB}$ is measured, then temperature $T_2$ can be found from the calibration table of the thermocouple. From the simple expression of {eq}`eq-p1-ch05-77`

```{math}
:label: eq-p1-ch05-97
S = \frac{\pi^2 k_B}{2e}\frac{k_B T}{E_F}
```

a linear dependence of $S$ on $T$ is predicted for simple metals. For actual thermocouples used for temperature measurements, the $S(T)$ dependence is approximately linear, but is given by an accurate calibration table to account for small deviations from this linear relation. Thermocouples are calibrated at several fixed temperatures and the calibration table comes from a fit of these thermal data to a polynomial function that is approximately linear in $T$.

### 5.4.2 Peltier Effect

The Peltier effect is the observation of a thermal current $\vec{U} = \overleftrightarrow{\Pi}\cdot\vec{j}$ in the presence of an electric current $\vec{j}$ with no thermal gradient ($\vec{\nabla}T = 0$) so that

```{math}
:label: eq-p1-ch05-98
\overleftrightarrow{\Pi} = T\,\overleftrightarrow{S} .
```

The Peltier effect measures the heat generated (or absorbed) at the junction of two dissimilar metals held at constant temperature, when an electric current passes through the junction. Sending electric current around a circuit of two dissimilar metals cools one junction and heats another and is the basis of the operation of thermoelectric coolers. This thermoelectric effect is represented schematically in {numref}`fig-p1-ch05-6`. Because of the similarities between the Peltier coefficient and the Seebeck coefficient, materials exhibiting a large Seebeck effect also show a large Peltier effect. Since both $\overleftrightarrow{S}$ and $\overleftrightarrow{\Pi}$ are proportional to $(1/e)$, the sign of $\overleftrightarrow{S}$ and $\overleftrightarrow{\Pi}$ is negative for electrons and positive for holes in the case of degenerate semiconductors. Reversing the direction of $\vec{j}$, will interchange the junctions where heat is generated (absorbed).

:::{figure} images/fig-p1-ch05-6.png
:name: fig-p1-ch05-6
:align: center
:width: 60%

A heat engine based on the Peltier effect with heat $(\Pi_A - \Pi_B)\vec{j}$ introduced at one junction and extracted at another under the conditions of no temperature gradient ($\vec{\nabla}T = 0$).
:::

### 5.4.3 Thomson Effect

Assume that we have an electric circuit consisting of a single metal conductor. The power generated in a sample, such as an n-type semiconductor, as shown in {numref}`fig-p1-ch05-7`, is

```{math}
:label: eq-p1-ch05-99
P = \vec{j}\cdot\vec{E}
```

where the electric field can be obtained from {eq}`eq-p1-ch05-49` and {eq}`eq-p1-ch05-51` as

```{math}
:label: eq-p1-ch05-100
\vec{E} = (\overleftrightarrow{\sigma}^{-1})\cdot\vec{j}
- \overleftrightarrow{T}_b\cdot\vec{\nabla}T
```

where $\overleftrightarrow{T}_b$ is the Thomson coefficient defined in {eq}`eq-p1-ch05-51` and is related to the Seebeck coefficient $\overleftrightarrow{S}$ as discussed in §5.3 and §5.3.1. Substitution of {eq}`eq-p1-ch05-100` into {eq}`eq-p1-ch05-99` yields the total power dissipation

```{math}
:label: eq-p1-ch05-101
P = \vec{j}\cdot(\overleftrightarrow{\sigma}^{-1})\cdot\vec{j}
- \vec{j}\cdot\overleftrightarrow{T}_b\cdot\vec{\nabla}T .
```

The first term in {eq}`eq-p1-ch05-101` is the conventional joule heating term while the second term is the contribution from the Thomson effect. For an n-type semiconductor $\overleftrightarrow{T}_b$ is negative. Thus when $\vec{j}$ and $\vec{\nabla}T$ are parallel, heating will result, as in {numref}`fig-p1-ch05-7`(a). However if $\vec{j}$ and $\vec{\nabla}T$ are antiparallel, as in {numref}`fig-p1-ch05-7`(b), cooling will occur. Thus reversal of the direction of $\vec{j}$ without changing the direction of $\vec{\nabla}T$ will reverse the sign of the Thomson contribution. Likewise, a reversal in the direction of $\vec{\nabla}T$ keeping the direction of $\vec{j}$ unchanged will also reverse the sign of the Thomson contribution.

Thus, if either (but not both) the direction of the electric current or the direction of the thermal gradient is reversed, an absorption of heat from the surroundings will take place. The Thomson effect is utilized in thermoelectric refrigerators which are useful as practical low temperature laboratory coolers.

Referring to {numref}`fig-p1-ch05-8`, we see a schematic diagram explaining the operation of a thermoelectric cooler. We see that for a degenerate n-type semiconductor where $\overleftrightarrow{T}_b$, $\overleftrightarrow{S}$, and $\overleftrightarrow{\Pi}$ are all negative, when $\vec{j}$ and $\vec{\nabla}T$ are antiparallel then cooling occurs and heat is extracted from the cold junction and transferred to the heat sink at temperature $T_H$. For the p-type leg, all the thermoelectric coefficients are positive, so {eq}`eq-p1-ch05-101` shows that cooling occurs when $\vec{j}$ and $\vec{\nabla}T$ are parallel. Thus both the n-type and p-type legs in a thermoelectric element contribute to cooling in a thermoelectric cooler.

:::{figure} images/fig-p1-ch05-7.png
:name: fig-p1-ch05-7
:align: center
:width: 80%

The Thomson term in an n-type semiconductor produces (a) heating when $\vec{j}$ and $\vec{\nabla}T$ are in the same direction and (b) cooling when $\vec{j}$ and $\vec{\nabla}T$ are in opposite directions.
:::

:::{figure} images/fig-p1-ch05-8.png
:name: fig-p1-ch05-8
:align: center
:width: 80%

Schematic diagram of a thermoelectric cooler. The heat sinks and cold junctions are metals that form ohmic contacts to the active thermoelectric n-type and p-type semiconductors.
:::

### 5.4.4 The Kelvin Relations

The three thermoelectric effects are related and these relations were first derived by Lord Kelvin after he became a Lord and changed his name from Thomson to Kelvin. The Kelvin relations are based on arguments of irreversible thermodynamics and relate $\Pi$, $S$, and $T_b$. If we define the thermopower $S_{AB} = S_B - S_A$ and the Peltier coefficient similarly $\Pi_{AB} = \Pi_A - \Pi_B$ for material $A$ joined to material $B$, then we obtain the first Kelvin relation:

```{math}
:label: eq-p1-ch05-102
S_{AB} = \frac{\Pi_{AB}}{T} .
```

The Thomson coefficient $T_b$ is defined by

```{math}
:label: eq-p1-ch05-103
T_b = T\frac{\partial S}{\partial T}
```

which allows determination of the Seebeck coefficient at temperature $T_0$ by integration of the above equation

```{math}
:label: eq-p1-ch05-104
S(T_0) = \int_0^{T_0} \frac{T_b(T)}{T}\,dT .
```

Furthermore, from the above definitions, we deduce the second Kelvin relation

```{math}
:label: eq-p1-ch05-105
T_{b,A} - T_{b,B} = T\frac{\partial S_{AB}}{\partial T}
= T\frac{\partial S_A}{\partial T} - T\frac{\partial S_B}{\partial T}
```

from which we obtain an expression relating all three thermoelectric coefficients

```{math}
:label: eq-p1-ch05-106
T_{b,A} = T\frac{\partial S_A}{\partial T}
= T\frac{\partial (\Pi_A/T)}{\partial T}
= \frac{\partial \Pi_A}{\partial T} - \frac{\Pi_A}{T}
= \frac{\partial \Pi_A}{\partial T} - S_A .
```

### 5.4.5 Thermoelectric Figure of Merit

A good thermoelectric material for cooling applications must have a high thermoelectric figure of merit, $Z$, which is defined by

```{math}
:label: eq-p1-ch05-107
Z = \frac{S^2\sigma}{\kappa}
```

where $S$ is the thermoelectric power (Seebeck coefficient), $\sigma$ is the electrical conductivity, and $\kappa$ is the thermal conductivity. In order to achieve a high $Z$, one requires a high thermoelectric power $S$, a high electrical conductivity $\sigma$ to maintain high carrier mobility, and a low thermal conductivity $\kappa$ to retain the applied thermal gradient. In general, it is difficult in practical systems to increase $Z$ for the following reasons: increasing $S$ for simple materials also leads to a simultaneous decrease in $\sigma$, and an increase in $\sigma$ leads to a comparable increase in the electronic contribution to $\kappa$ because of the Wiedemann-Franz law. So with known conventional solids, a limit is rapidly obtained where a modification to any one of the three parameters $S$, $\sigma$, or $\kappa$ adversely affects the other transport coefficients, so that the resulting $Z$ does not vary significantly. Currently, the commercially available materials with the highest $Z$ are $\mathrm{Bi}_2\mathrm{Te}_3$ alloys such as $\mathrm{Bi}_{0.5}\mathrm{Sb}_{1.5}\mathrm{Te}_3$ with $ZT \sim 1$ at 300 K. Only small increases in $Z$ have been achieved in the last two to three decades. Research on thermoelectric materials has therefore been at a low level since about 1960. Since 1994, new interest has been revived in thermoelectricity with the discovery of new materials: skutterudites - $\mathrm{CeFe}_{4-x}\mathrm{Co}_x\mathrm{Sb}_{12}$ or $\mathrm{LaFe}_{4-x}\mathrm{Co}_x\mathrm{Sb}_{12}$ for $0 < x < 4$, which offer promise for higher $Z$ values in bulk materials, and low dimensional systems (quantum wells, quantum wires) which offer promise for enhanced $Z$ relative to bulk $Z$ values in the same material. Thus thermoelectricity has again become an active research field.

## 5.5 Phonon Drag Effect

For a simple metal such as an alkali metal one would expect the thermopower $S$ to be given by the simple expression in {eq}`eq-p1-ch05-77`, and to be negative since the carriers are electrons. This is true at room temperature for all of the alkali metals except Li. Furthermore, $S$ is positive for the noble metals Au, Ag and Cu. The anomalous sign of $S$ in these metals can be understood by recalling the complex Fermi surfaces for these metals (see {numref}`fig-p1-ch02-6`), where we note that copper in fact exhibits hole orbits in the extended zone. In general, with multiple carrier types as occur in semiconductors, the interpretation of thermopower data can become complicated.

Another complication which must also be considered, especially at low temperatures, is the phonon drag effect. In the presence of a thermal gradient, the phonons will diffuse and "drag" the electrons along with them because of the electron-phonon interaction. For a simple explanation of phonon drag, consider a gas of phonons with an average energy density $E_{ph}/V$ where $V$ is the volume. Using kinetic theory, we find that the phonon gas exerts a pressure

```{math}
:label: eq-p1-ch05-108
P = \frac{1}{3}\left(\frac{E_{ph}}{V}\right)
```

on the electron gas. In the presence of a thermal gradient, the electrons are subject to a force density

```{math}
:label: eq-p1-ch05-109
\frac{F_x}{V} = -\frac{dP}{dx}
= -\frac{1}{3V}\left(\frac{dE_{ph}}{dT}\right)\frac{dT}{dx} .
```

To prevent the flow of current, this force must be balanced by the electric force. Thus, for an electron density $n$, we obtain

```{math}
:label: eq-p1-ch05-110
-n e E_x + \frac{F_x}{V} = 0
```

giving a phonon-drag contribution to the thermopower. Using the definition of the Seebeck coefficient for an open circuit system, we can write

```{math}
:label: eq-p1-ch05-111
S_{ph} = \frac{E_x}{(dT/dx)}
\approx -\left(\frac{1}{3 e n V}\right)\frac{dE_{ph}}{dT}
= \frac{C_{ph}}{3 e n}
```

where $C_{ph}$ is the phonon heat capacity per unit volume. Although this is only a rough approximate derivation, it predicts the correct temperature dependence, in that the phonon-drag contribution is important at temperatures where the phonon specific heat is large.

The total thermopower is a sum of the diffusion contribution (considered in §5.4.1) and the phonon drag term $S_{ph}$. The phonon drag effect depends on the electron-phonon coupling; at higher temperatures where the phonon-phonon coupling (Umklapp processes) becomes more important than the electron-phonon coupling, phonon drag effects become less important (see §6.4.4).
