---
title: "4 Paramagnetism and Diamagnetism of Nearly Free Electrons"
abstract: "Pauli paramagnetism of conduction electrons from Fermi statistics, and Landau diamagnetism associated with the quantized orbital (Landau level) spectrum of nearly free electrons in a magnetic field."
---

# 4 Paramagnetism and Diamagnetism of Nearly Free Electrons

References

- Ashcroft and Mermin, *Solid State Physics*, pp. 661-664, and Chapter 14.
- Kittel, *Introduction to Solid State Physics*, 6th Ed., pp. 239-249 and 413-416.

## 4.1 Introduction

In Chapter 3 we considered the diamagnetism and paramagnetism of bound electrons associated with the core electrons in crystalline materials. In the present chapter, we treat the paramagnetism of conduction electrons (Pauli paramagnetism) and also consider the diamagnetism (Landau diamagnetism) of the $s$ and $p$ nearly free electrons in metals and semiconductors. In addition we devote considerable attention to the discussion of the energy levels of conduction electrons in a magnetic field, also known as Landau levels.

## 4.2 Pauli Paramagnetism

We have previously discussed the response of bound electrons to a magnetic field. We first show in this section that the Curie law for bound electrons has the wrong temperature dependence for describing the paramagnetic response of conduction electrons in a magnetic field. We then indicate the new physics that must be introduced to handle the behavior of the conduction electrons, and show that by taking into account the Fermi statistics, the proper temperature dependence is obtained.

For the bound electrons, the paramagnetic susceptibility in a weak field is given by the Curie law:

```{math}
:label: eq-p3-ch04-1
\chi = \frac{n\hat{\mu} g^2\mu_B^2 j(j+1)}{3k_B T}
```

where $n$ is the carrier density and $\hat{\mu}$ is the permeability in the constitutive equation $B = \hat{\mu}H$. Free electrons have no orbital angular momentum, but only spin angular momentum so that $j = s = 1/2$ and $g = 2$. Therefore we obtain

```{math}
g^2 j(j+1) = 2^2\left(\frac{1}{2}\right)\left(\frac{3}{2}\right) = 3 ,
```

and we would expect the Curie law for free electrons having a concentration $n$ to be

```{math}
:label: eq-p3-ch04-3
\chi_{\text{free electrons}} = \frac{n\hat{\mu}\mu_B^2}{k_B T} .
```

Equation {eq}`eq-p3-ch04-3` suggests that the free electrons should contribute substantially to the susceptibility (for a simple metal like sodium) as the temperature is decreased. Instead, we find experimentally that $\chi_{\text{free electrons}}$ is small in magnitude and nearly independent of temperature. The reason for this discrepancy is simply that we need to use Fermi statistics to treat free electrons and not Maxwell-Boltzmann statistics which we used in the calculation of Curie's Law. In discussing the statistics for whole atomic systems, as was done in considering the paramagnetism of the bound electrons, Maxwell-Boltzmann statistics is the proper statistics to use since the quantum numbers of each atom are not correlated with those of other atoms.

We will now give two different derivations of the paramagnetic susceptibility of free electrons taking Fermi statistics into account. We will find this contribution to $\chi$ to be positive, and is called *Pauli paramagnetism*, in honor of the man who first explained this effect successfully.

The first "derivation" of the Pauli paramagnetic susceptibility is hand-waving. Although it can hardly qualify as a derivation, it nevertheless provides us with a very nice physical picture of Pauli paramagnetism. Suppose that the free electrons form an electron gas with all energy states occupied up to the Fermi level. Only those states near the Fermi surface can contribute to the susceptibility, for it is only those states which have unoccupied states nearby in energy. Thus, the fraction of electrons that can contribute to $\chi$ is on the order of $T/T_F$ where the Fermi temperature $T_F$ is related to the Fermi energy $E_F$ through the Boltzmann constant $k_B$ by $T_F = E_F/k_B$. This argument then indicates that the free electron density which is effective in contributing to $\chi$ is the fraction $n(T/T_F)$ so that

```{math}
:label: eq-p3-ch04-4
\chi_{\text{free electrons}} \simeq \frac{n\hat{\mu}\mu_B^2}{k_B T}\left(\frac{T}{T_F}\right) = \frac{n\hat{\mu}\mu_B^2}{k_B T_F} .
```

Because $T_F \gg T$ for metals at room temperature, the Pauli paramagnetism is expected to be small compared with the contribution from the bound electrons and $\chi$ is essentially independent of $T$ in agreement with experiment.

We will now give a second derivation of this result that is still quite physical, but somewhat more rigorous than the hand-waving approach. The second derivation given here is the basis for many arguments you will see in the literature in the field of magnetism, and is based on a density of states picture for spin-up and spin-down bands as shown in Fig. {numref}`fig-p3-ch04-1`. The arrows on this diagram refer to the directions of the magnetic moments. The spin angular momentum $\vec{S}$ has a direction opposite to $\vec{\mu}$. To see the familiar density of states curve for nearly free electrons in 3D space $\rho(E) \propto E^{1/2}$, hold Fig. {numref}`fig-p3-ch04-1` on its side. This figure shows that the total occupation for the spin-up and spin-down states is different, but the occupation in both cases is terminated at the same Fermi energy.

:::{figure} images/fig-p3-ch04-1.png
:name: fig-p3-ch04-1
:width: 55%
:align: center
Fig. 4.1: Pauli paramagnetism at $0$ K, the levels below $E_F$ are occupied. The number of electrons in the "up" and "down" bands will adjust to make the energies equal at the Fermi level. We use the notation $\hat{\mu}_B = |\mu_B|$ to take account of the fact that $\mu_B$ is a negative quantity due to the negative charge on the electron.
:::

If we were thinking of electrons in a solid, we would call the two sides of the picture spin-up and spin-down bands. In Fig. {numref}`fig-p3-ch04-1` the energy $E$ at the band edge is either $\pm\mu_B B$ relative to the energy in zero magnetic field. Thus, the electrons with spin along the magnetic field go into the $\downarrow$ band on the right hand side of the figure, while the electrons with $\vec{S}$ antiparallel to $\vec{B}$ go into the band on the left hand side of Fig. {numref}`fig-p3-ch04-1`.

Let us now calculate the average number of electrons in the spin up and spin down bands. This average number will be roughly half of the total carrier concentration $n$. In carrying out the calculation we note that because of the negative sign of the electron charge, $\mu_B$ is a negative quantity. We therefore use $\hat{\mu}_B$ to denote the absolute value $|\mu_B|$. Then we write

```{math}
:label: eq-p3-ch04-5
n_{+} = \frac{1}{2}\int_{-\hat{\mu}_B B}^{E_F} dE\, f(E)\,\rho(E + \hat{\mu}_B B)
```

where $n_{+}$ is the electron density with the magnetic moment directed along the field, $f(E)$ is the Fermi function, and $\rho(E + \hat{\mu}_B B)$ is the density of states for the ensemble for which the magnetic moment is directed along the magnetic field (see Fig. {numref}`fig-p3-ch04-1`). To carry out the integral in Eq. {eq}`eq-p3-ch04-5`, expand the density of states

```{math}
:label: eq-p3-ch04-6
\rho(E + \hat{\mu}_B B) = \rho(E) + \hat{\mu}_B B\,\frac{\partial\rho(E)}{\partial E} + \cdots .
```

Then upon substitution of Eq. {eq}`eq-p3-ch04-6` into Eq. {eq}`eq-p3-ch04-5` we obtain

```{math}
:label: eq-p3-ch04-7
n_{+} = \frac{1}{2}\int_0^\infty dE\,f(E)\rho(E) + \frac{1}{2}\int_{-\hat{\mu}_B B}^{0} dE\,f(E)\rho(E) + (\hat{\mu}_B B)^2\int_{-\hat{\mu}_B B}^{\infty} dE\,f(E)\rho'(E) .
```

The second term on the right hand side of Eq. {eq}`eq-p3-ch04-7` vanishes because $\rho(E) = 0$ for $E < 0$. The last term on the right hand side of Eq. {eq}`eq-p3-ch04-7` is handled through integration by parts:

```{math}
:label: eq-p3-ch04-8
\int_{-\hat{\mu}_B B}^{\infty} dE\,f(E)\,\rho'(E) = f(E)\rho(E)\Big|_{-\hat{\mu}_B B}^{\infty} - \int_{-\hat{\mu}_B B}^{\infty} dE\,f'(E)\rho(E) .
```

The first term in Eq. {eq}`eq-p3-ch04-8` vanishes at both limits, since $\rho(E)$ vanishes at the lower limit where $E = -\hat{\mu}_B B < 0$, and $f(E)$ vanishes at the upper limit $E\rightarrow\infty$. The second term in Eq. {eq}`eq-p3-ch04-8` selects the density of states at the Fermi level because of the delta function properties of $f'(E) = -\delta(E-E_F)$, and we therefore obtain:

```{math}
:label: eq-p3-ch04-9
n_{+} = \frac{1}{2}n_0 + \frac{1}{2}\hat{\mu}_B B\,\rho(E_F) .
```

Similarly, we can carry out the corresponding calculation for $n_{-}$ to obtain

```{math}
:label: eq-p3-ch04-10
n_{-} = \frac{1}{2}\int_{\hat{\mu}_B B}^{\infty} dE\,f(E)\,\rho(E - \hat{\mu}_B B) = \frac{1}{2}n_0 - \frac{1}{2}\hat{\mu}_B B\,\rho(E_F) .
```

The magnetic moment per unit volume is proportional to the net number of electrons contributing to the magnetic moment times $\hat{\mu}_B$, and can be written as

```{math}
:label: eq-p3-ch04-11
M = \hat{\mu}_B(n_{+} - n_{-}) = \mu_B^2 B\,\rho(E_F)
```

so that

```{math}
:label: eq-p3-ch04-12
\chi = \mu_B^2\,\rho(E_F) .
```

We note that since $\chi$ depends on the square of $\mu_B$, there is no distinction between $\hat{\mu}_B^2$ and $\mu_B^2$. It is to be noted that the derivation for $\chi$ given here does not take into account the effect of the magnetic field on the electronic states. This effect is, in fact, of significant importance but beyond the scope of the simple discussion presented here.

For free electrons we can easily evaluate the density of states at the Fermi level $\rho(E_F)$ to obtain

```{math}
:label: eq-p3-ch04-13
\rho(E_F) = \frac{3}{2}\frac{n}{E_F} = \frac{3n}{2k_B T_F}
```

so that

```{math}
:label: eq-p3-ch04-14
M = \frac{3}{2}\frac{n\mu_B^2 B}{k_B T_F}
```

from which we obtain

```{math}
:label: eq-p3-ch04-15
\chi = \frac{3}{2}\frac{n\hat{\mu}\mu_B^2}{k_B T_F}
```

which except for the numerical factor is the same result as was obtained by the hand-waving approach given by Eq. {eq}`eq-p3-ch04-4` in the first "derivation" of the Pauli paramagnetic susceptibility. Measurements of the Pauli paramagnetic contribution are difficult to carry out and interpret because of difficulties in separating the various physical contributions to the experimentally determined $\chi(T)$. The most effective method to measure the Pauli contribution is a comparison between the susceptibilities implied by electron spin resonance and nuclear magnetic resonance.

## 4.3 Introduction to Landau Diamagnetism

The orbital motion of the nearly free electrons in a magnetic field gives rise to diamagnetism. The magnetic energy levels associated with this diamagnetism are called Landau levels and the diamagnetism is called *Landau diamagnetism*, named after the famous Russian physicist Lev Davidovich Landau, who first studied this phenomenon theoretically back in 1930.

In this chapter we discuss the fundamental properties associated with the Landau levels insofar as they determine Landau diamagnetism. Since the Landau levels imply a variety of magneto-oscillatory phenomena which are important for studies of the Fermi surface for crystalline solids, these topics are discussed in Chapter 5, while in Chapter 6 we discuss magnetic effects in the quantized 2D electron gas which have recently become important because of quantum wells and superlattices. In our discussion of the diamagnetism associated with nearly free electrons, we will first discuss the magnetic energy levels (or Landau levels) which form the basis for Landau diamagnetism.

## 4.4 Quantized Magnetic Energy Levels in 3D

The Hamiltonian for a free electron in a magnetic field uses the basic Schrödinger equation

```{math}
:label: eq-p3-ch04-16
\left[\frac{(\vec{p} - (e/c)\vec{A})^2}{2m} - \vec{\mu}\cdot\vec{B}\right]\psi = E\psi
```

in which the square on the first term implies the scalar product of each of the factors $[\vec{p} - (e/c)\vec{A}]$. To represent a magnetic field along the $z$ axis, we choose the asymmetric gauge (Landau gauge) for the vector potential $\vec{A}$:

```{math}
:label: eq-p3-ch04-17
A_x = -By, \qquad A_y = 0, \qquad A_z = 0
```

and we note that $\vec{\mu}$ in Eq. {eq}`eq-p3-ch04-16` is the magnetic moment associated with the electron spin, where $\vec{\mu} = g_s\mu_B\vec{S}/\hbar$.

Since the only coordinate in the problem (Eqs. {eq}`eq-p3-ch04-16` and {eq}`eq-p3-ch04-17`) is $y$, the form of $\psi(x,y,z)$ in Eq. {eq}`eq-p3-ch04-16` is chosen to make the differential equation separable into plane wave motion in the $x$ and $z$ directions. The wave function $\psi(x,y,z)$ is thus written as

```{math}
:label: eq-p3-ch04-18
\psi(x,y,z) = e^{ik_x x}e^{ik_z z}\varphi(y) .
```

Substitution of Eq. {eq}`eq-p3-ch04-18` in Eq. {eq}`eq-p3-ch04-16` results in the expression

```{math}
:label: eq-p3-ch04-19
\left[\frac{(\hbar k_x + (e/c)By)^2}{2m} + \frac{p_y^2}{2m} + \frac{\hbar^2 k_z^2}{2m} - \frac{g_s\mu_B}{\hbar}\vec{S}\cdot\vec{B}\right]\varphi(y) = E\varphi(y)
```

where $g_s$ and $\mu_B$ are, respectively, the free electron $g$--factor ($g_s = 2.0023$) and the Bohr magneton $\mu_B = e\hbar/(2mc)$. We see immediately that the orbital portion of Eq. {eq}`eq-p3-ch04-19` is of the form of the harmonic oscillator equation

```{math}
:label: eq-p3-ch04-20
\left[\frac{p_x^2}{2m} + \frac{1}{2}m x^2\omega_c^2\right]\psi^{(\ell)}_{\text{H.O.}} = E_\ell \psi^{(\ell)}_{\text{H.O.}}
```

where $\psi^{(\ell)}_{\text{H.O.}}$ is a harmonic oscillator function and $E_\ell = \hbar\omega_c(\ell+1/2)$ are the harmonic oscillator eigenvalues in which $\ell$ is an integer, $\ell = 0, 1, \ldots$. A comparison of Eq. {eq}`eq-p3-ch04-19` with the harmonic oscillator equation Eq. {eq}`eq-p3-ch04-20` shows that the characteristic frequency for the harmonic oscillator is the cyclotron frequency $\omega_c = eB/(mc)$ and the harmonic oscillator is centered about

```{math}
:label: eq-p3-ch04-21
y_0 = -\frac{\hbar k_x}{m\omega_c} .
```

These identifications yield the harmonic oscillator equation

```{math}
:label: eq-p3-ch04-22
\left[\frac{p_y^2}{2m} + \frac{\omega_c^2}{2m}(y - y_0)^2 + \frac{\hbar^2 k_z^2}{2m} - \frac{g_s\mu_B}{\hbar}\vec{S}\cdot\vec{B}\right]\varphi(y) = E\varphi(y) .
```

Thus, the energy eigenvalues of Eq. {eq}`eq-p3-ch04-22` for a free electron in a magnetic field can be written down immediately as

```{math}
:label: eq-p3-ch04-23
E_{\ell,m_s}(k_z) = \frac{\hbar^2 k_z^2}{2m} + \hbar\omega_c\left(\ell + \frac{1}{2}\right) - g_s\mu_B m_s B
```

recognizing that in the direction parallel to $\vec{B}$ we have plane wave motion, since there is no force acting along $\vec{B}$, and in the plane perpendicular to $\vec{B}$ we have harmonic oscillator motion. The last term in Eq. {eq}`eq-p3-ch04-23` gives the contribution from spin terms with spin up corresponding to $m_s = 1/2$ and spin down corresponding to $m_s = -1/2$.

For a band electron in a solid, the energy eigenvalues in a magnetic field are given in the "effective mass approximation" by an expression which is very similar to Eq. {eq}`eq-p3-ch04-23` except that the free electron mass is replaced by an effective mass tensor and the free electron $g$-factor $g_s = 2.0023$ is replaced by an effective $g$-factor $g_{\text{eff}}$. Thus Landau levels for carriers in a simple parabolic band in a semiconductor are given by

```{math}
:label: eq-p3-ch04-24
E_{\ell,m_s}(k_z) = \frac{\hbar^2 k_z^2}{2m^*_{\parallel}} + \hbar\omega_c^*\left(\ell + \frac{1}{2}\right) - g_{\text{eff}}\mu_B m_s B
```

where the various band parameters in Eq. {eq}`eq-p3-ch04-24` are defined as follows: $m^*_{\parallel}$ is the effective mass tensor component along the magnetic field, $\omega_c^* = eB/(m_c^* c)$ is the cyclotron frequency, $m_c^*$ is the cyclotron effective mass for motion in the plane normal to the magnetic field, and $g_{\text{eff}}$ is the effective $g$-factor.

The quantum numbers describing the energy eigenvalues $E_{\ell,m_s}(k_z)$ are as follows:

1. $\ell$ is the Landau level index (or harmonic oscillator level index), $\ell = 0, 1, 2, 3, \ldots$.
2. $m_s$ is the spin quantum number, $1/2$ for $\uparrow$ and $-1/2$ for $\downarrow$.
3. $k_z$ assumes values between $-\infty$ and $+\infty$ in free space and is a quasi-continuous variable in the first Brillouin zone for a real solid.
4. $k_x$ is the wave vector in the plane $\perp$ to $\vec{B}$ and does not enter into Eq. {eq}`eq-p3-ch04-24` for the energy levels.

Since the magnetic energy levels $E_{\ell,m_s}(k_z)$ are independent of $k_x$, the quantum number $k_x$ contributes directly to the density of states in a magnetic field. This degeneracy factor is discussed in §4.4.1. The form of $E_{\ell,m_s}(k_z)$ is then discussed in §4.4.2 and finally the effective mass parameters $m^*_{\parallel}$ and $m_c^*$ and the effective $g$-factor are discussed in §4.4.3.

### 4.4.1 Degeneracy of the Magnetic Energy Levels in $k_x$

The degeneracy of the magnetic energy levels $E_{\ell,m_s}(k_z)$ in $k_x$ is found by considering the center of the harmonic oscillator function, which from Eq. {eq}`eq-p3-ch04-21` is at $y_0 = -\hbar k_x/(m\omega_c)$. Since $y_0$ lies in the interval

```{math}
:label: eq-p3-ch04-25
-\frac{L_y}{2} < y_0 < \frac{L_y}{2} ,
```

and since the center of the harmonic oscillator is inside the sample, we have the requirement

```{math}
:label: eq-p3-ch04-26
-\frac{m\omega_c L_y}{2\hbar} < k_x < \frac{m\omega_c L_y}{2\hbar} .
```

Thus the limits on the range of the quantum number $k_x$ are between $k_x^{\min}$ and $k_x^{\max}$ which are given by

```{math}
:label: eq-p3-ch04-27
k_x^{\min} = -\frac{m\omega_c L_y}{2\hbar}, \qquad k_x^{\max} = \frac{m\omega_c L_y}{2\hbar} .
```

With the limits on $k_z$ imposed by Eq. {eq}`eq-p3-ch04-27`, the sum over states (using Fermi statistics) becomes

```{math}
:label: eq-p3-ch04-28
\mathcal{Z} = \sum_{\ell=0}^{\infty}\sum_{k_z=-\infty}^{\infty}\sum_{k_x=k_x^{\min}}^{k_x^{\max}}\sum_{m_s=-1/2}^{1/2} \ln\!\left[1 + e^{(E_F - E_{\ell,m_s}(k_z))/k_B T}\right] .
```

Since the energy levels are independent of $k_x$, we can sum Eq. {eq}`eq-p3-ch04-28` over $k_x$ to obtain a degeneracy factor which is important in all magnetic energy level phenomena

```{math}
:label: eq-p3-ch04-29
\sum_{k_x} \rightarrow \int_{k_x^{\min}}^{k_x^{\max}}\frac{dk_x\,L_x}{2\pi} = \frac{L_x L_y m\omega_c}{2\pi\hbar}
```

utilizing the uncertainty principle which requires that there is one $k_x$ state per $2\pi/L_x$ since $N_x a = L_x$, in which $a$ is the lattice constant. It is important to emphasize that the sum over $k_x$ in Eq. {eq}`eq-p3-ch04-29` is proportional to the magnetic field since $\omega_c \propto B$.

Referring to Fig. {numref}`fig-p3-ch04-2`(d) we see how upon application of a magnetic field in the $z$ direction the wave vector quantum numbers $k_x$ and $k_y$ in the plane normal to the magnetic field are transformed into the Landau level index $\ell$ and the quantum number $k_x$ which has a high degeneracy factor per unit area of $(m\omega_c/h)$. It is convenient to introduce the characteristic magnetic length $\lambda$ defined by

```{math}
:label: eq-p3-ch04-30
\lambda^2 \equiv \frac{\hbar c}{eB}
```

so that from Eq. {eq}`eq-p3-ch04-29` the degeneracy factor per unit area becomes $1/(2\pi\lambda^2)$. From Fig. {numref}`fig-p3-ch04-2`(d) we see a qualitative difference between the states in a magnetic field and the states in zero field. For fields too small to confine the carriers into a cyclotron orbit with a characteristic length less than $\lambda$, the electrons are best described in the zero field limit, or we can say that the Landau level description applies for magnetic fields large enough to define a cyclotron orbit within the sample dimensions and for electron relaxation times long enough for an electron not to be scattered before completing an electron orbit, $\omega_c\tau > 1$. We return to the discussion of this degeneracy factor in discussion the 2D electron gas in Chapter 6.

### 4.4.2 Dispersion of the Magnetic Energy Levels Along the Magnetic Field

The dispersion of the magnetic energy levels is given by Eq. {eq}`eq-p3-ch04-24` and is displayed in Fig. {numref}`fig-p3-ch04-2`(a). In this figure it is seen that the dispersion relations $E_{\ell,m_s}(k_z)$ are parabolic in $k_z$ for each Landau level, each level $\ell$ being displaced from levels $\ell+1$ and $\ell-1$ by the Landau level separation $\hbar\omega_c$. The lowest Landau level ($\ell = 0$) is at an energy $(\hbar\omega_c/2)$ above the energy of electrons in zero magnetic field. The occupation of each Landau level is found by integration up to the Fermi level $E_F$. Figure {numref}`fig-p3-ch04-2`(b) shows special $k_z$ values where either a Landau level crosses the Fermi level or a Landau level pops through the Fermi level $E_F$. As the magnetic field increases the Landau level separation increases until a Landau level pops through $E_F$, requiring a redistribution of electrons through the remaining Landau levels.

:::{figure} images/fig-p3-ch04-2.png
:name: fig-p3-ch04-2
:width: 85%
:align: center
Fig. 4.2: Various aspects of Landau levels. (a) $E$ vs $k_z$ for the first few Landau levels $\ell = 0, 1, \ldots, 4$. The $B = 0$ parabola (dashed curve) refers to the ordinary free electron case with zero magnetic field. (b) $k$--space showing Landau levels in 3D. The allowed $k$-values lie on the concentric cylinders, and the spherical Fermi surface cuts these cylinders. (c) The solid line is the density of states for all the Landau levels while the dashed-solid curves give the density of states in a magnetic field for each of the Landau levels. Singularities in the density of states occur whenever a Landau level pops through the Fermi level. The dashed curve labeled $B = 0$ refers to the density of states in zero field, and shows the expected $\sqrt{E}$ dependence. (d) A schematic diagram showing how the states in zero field go into Landau levels when the $B$ field is applied. The diagram also shows the effect of electron-spin splitting on the Landau levels.
:::

In this section we focus on the $k_z$ dependence of the magnetic energy levels. First we obtain the sum of the number density over $k_z$ which involves conversion of the sum on states to an integral

```{math}
:label: eq-p3-ch04-31
\sum_{k_z} \rightarrow \frac{2}{L_z}\int_0^\infty \frac{dk_z}{2\pi} .
```

Using Fermi statistics we then obtain for the number density:

```{math}
:label: eq-p3-ch04-32
n(L_x,L_y,L_z) = \sum_{\text{states}}\frac{1}{1 + e^{(E_{\ell,m_s}(k_z)-E_F)/k_B T}} = \frac{L_x L_y m\omega_c}{2\pi\hbar}\,\frac{2L_z}{2\pi}\sum_{\ell,m_s}\int_0^\infty \frac{dk_z}{1 + e^{(E_{\ell,m_s}(k_z)-E_F)/k_B T}} ,
```

so that the degeneracy factor per unit volume is $(1/2\pi^2\lambda^2)$. Keeping the Fermi level constant, the electron density is found by summing the Fermi distribution over all states in the magnetic field, where the Fermi function

```{math}
:label: eq-p3-ch04-33
f(E_{\ell,m_s}(k_z)) = \frac{1}{1 + e^{(E_{\ell,m_s}(k_z)-E_F)/k_B T}}
```

gives the probability that the state $(\ell, m_s, k_z)$ is occupied. In a magnetic field, the 3D electron density $n$ of a nearly free electron solid (neglecting spin splitting effects) is

```{math}
:label: eq-p3-ch04-34
n = \frac{2eB}{(2\pi)^2\hbar c}\sum_{\ell=0}^{\ell_{\max}}\int_{-\pi/a}^{\pi/a} dk_z\, f(E_{\ell,m_s}(k_z))
```

in which a factor of $2$ for the electron spin degeneracy has been inserted.

For simplicity, we further consider the magnetic energy levels for a simple 3D parabolic band (neglecting spin)

```{math}
:label: eq-p3-ch04-35
E_\ell(k_z) = \frac{\hbar^2 k_z^2}{2m^*} + \hbar\omega_c^*\left(\ell + \frac{1}{2}\right)
```

so that

```{math}
:label: eq-p3-ch04-36
k_z = \left(\frac{2eB}{c\hbar}\right)^{1/2}\left[\frac{E}{\hbar\omega_c^*} - \left(\ell + \frac{1}{2}\right)\right]^{1/2}
```

where we have written $E$ to denote $E_\ell(k_z)$. Differentiating Eq. {eq}`eq-p3-ch04-36` gives

```{math}
:label: eq-p3-ch04-37
dk_z = \left(\frac{2eB}{c\hbar}\right)^{1/2}\frac{dE}{2\hbar\omega_c^*}\left[\frac{E}{\hbar\omega_c^*} - \left(\ell + \frac{1}{2}\right)\right]^{-1/2} .
```

For the case of a 2D electron gas, the electrons are confined in the $z$ direction and exhibit bound states. Thus no integration over $k_z$ (see Eq. {eq}`eq-p3-ch04-34`) is needed for a 2D electron gas. However, for the 3D electron gas, integration of Eq. {eq}`eq-p3-ch04-34` thus yields a carrier density at $T = 0$ of

```{math}
:label: eq-p3-ch04-38
n = \frac{1}{\pi^2\lambda^2}\sum_{\ell=0}^{\ell_F}\left(\frac{2eB}{c\hbar}\right)^{1/2}\int_{E(k_z=0)}^{E_F}\frac{dE}{2\hbar\omega_c^*}\left[\frac{E}{\hbar\omega_c^*} - \left(\ell + \frac{1}{2}\right)\right]^{-1/2}
```

where the characteristic magnetic length $\lambda$ is given by Eq. {eq}`eq-p3-ch04-30`. Carrying out the integration in Eq. {eq}`eq-p3-ch04-38`, we obtain the result

```{math}
:label: eq-p3-ch04-39
n = \frac{1}{\pi^2\lambda^2}\sum_{\ell=0}^{\ell_F}\left(\frac{2eB}{c\hbar}\right)^{1/2}\left[\frac{E_F}{\hbar\omega_c^*} - \left(\ell + \frac{1}{2}\right)\right]^{1/2}
```

where $\ell_F$ is the highest occupied Landau level. The oscillatory effects associated with Eq. {eq}`eq-p3-ch04-39` are discussed in Chapter 5.

From differentiation of Eq. {eq}`eq-p3-ch04-39` with respect to energy, we obtain the density of states in a magnetic field $\rho_B(E) = (\partial n/\partial E)$

```{math}
:label: eq-p3-ch04-40
\rho_B(E) = \frac{\sqrt{2eB/\hbar c}}{2\pi^2\hbar\omega_c^*(\hbar c/eB)}\sum_{\ell}\left[\frac{E}{\hbar\omega_c^*} - \left(\ell + \frac{1}{2}\right)\right]^{-1/2}
```

which is plotted in Fig. {numref}`fig-p3-ch04-2`(c), showing singularities at each magnetic subband extrema. Because of the singular behavior of physical quantities associated with these extrema, the subband extrema contribute resonantly to magneto-optical spectra, as discussed in Chapter 5.

To illustrate the oscillatory behavior of Eq. {eq}`eq-p3-ch04-39` in $1/B$, we write Eq. {eq}`eq-p3-ch04-39` as the sum over Landau levels and can be written as

```{math}
:label: eq-p3-ch04-41
n = \frac{\sqrt{2}}{\pi^2\lambda^3}\sum_{\ell=0}^{\ell_F}\left(\ell_F' - \ell\right)^{1/2}
```

and the resonance condition is

```{math}
:label: eq-p3-ch04-42
\ell_F' = \frac{E_F}{\hbar\omega_c^*} - \frac{1}{2}
```

gives a measure of the occupation level as is illustrated in Fig. {numref}`fig-p3-ch04-2`(a). The oscillatory behavior of $n$ and other physical observables is the subject of Chapter 5.

### 4.4.3 Band Parameters Describing the Magnetic Energy Levels

The magnetic energy levels given by Eq. {eq}`eq-p3-ch04-24` depend on several band parameters $m^*_{\parallel}$, $m_c^*$ and $g_{\text{eff}}$. In this section we summarize the properties of these band parameters. To observe the effects associated with the Landau levels we require that $\omega_c\tau \gg 1$, which implies that an electron can execute at least one cyclotron orbit before being scattered. Because of the small effective masses of carriers in semiconductors, the cyclotron frequency is high, and the spacing between magnetic energy levels also becomes large in comparison to free electrons.

The effective mass parameters $m^*_{\parallel}$ and $m_c^*$ which enter Eq. {eq}`eq-p3-ch04-24` can be simply written for semiconductors because of the simplicity of their Fermi surfaces. For arbitrary magnetic field directions, it is often convenient to use the formula

```{math}
:label: eq-p3-ch04-43
m_c^* = \frac{[\det(\overleftrightarrow{m}^*)]^{1/2}}{[\hat{b}\cdot\overleftrightarrow{m}^*\cdot\hat{b}]^{1/2}}
```

to find the cyclotron effective mass $m_c^*$ for an ellipsoidal constant energy surface, where $\det(\overleftrightarrow{m}^*)$ is the determinant of the effective mass tensor $\overleftrightarrow{m}^*$ and $\hat{b}$ is a unit vector in the direction of the magnetic field so that

```{math}
:label: eq-p3-ch04-44
m^*_{\parallel} = \hat{b}\cdot\overleftrightarrow{m}^*\cdot\hat{b} .
```

Equations {eq}`eq-p3-ch04-43` and {eq}`eq-p3-ch04-44` are particularly useful when the constant energy ellipsoidal surface does not have its major axes along the crystalline axes and the magnetic field is arbitrarily directed with respect to the major axes of the ellipsoidal constant energy surface. For ellipsoidal constant energy surfaces, neither $m^*_{\parallel}$ nor $m_c^*$ depend on $k_z$. For more general Fermi surfaces, $m_c^*$ is found by integration of $k/(\partial E/\partial k)$ around a constant energy surface normal to the magnetic field and $m_c^*$ will depend on $k_z$ in general. The effective mass component along the magnetic field $m^*_{\parallel}$ is unaffected by the applied field.

The calculation of $g_{\text{eff}}$ is more complicated than for the effective mass components, and makes considerable use of group theory to handle symmetry phenomena. Therefore we will treat $g_{\text{eff}}$ as an experimentally determined band parameter.

In materials with large spin-orbit coupling (see Fig. {numref}`fig-p3-ch04-3`) the effective $g$--factor, $g_{\text{eff}}$, is found experimentally to be quite different from the free electron value of $2$ and $g_{\text{eff}}$ can be either positive or negative. For example, for the conduction band of InSb, $g_{\text{eff}}\simeq -50$ and the cyclotron effective mass for the electron carriers is small ($m_c^* \simeq 0.014m$) and isotropic. The extremum ($k_z = 0$) of each magnetic sub-band (indexed by the quantum number $\ell = $ integer) is indicated in Fig. 5.2 (original). For the case of InSb, the lowest magnetic energy level is a spin $\uparrow$ state, with the spin oriented along the magnetic field due to the negative effective $g$-factor of InSb. This negative $g$-factor arises because of the large orbital contribution to the $g$-factor which can occur in solids with a large spin-orbit interaction, an effect that is totally absent in atomic systems.

:::{figure} images/fig-p3-ch04-3.png
:name: fig-p3-ch04-3
:width: 55%
:align: center
Fig. 4.3: Simplified view of the band edge structure of a direct gap semiconductor, e.g., GaAs at $\vec{k} = 0$. Note that the spin-orbit splitting in the valence band is nearly as large as the bandgap.
:::

## 4.5 The Magnetic Susceptibility for Conduction Electrons

Having obtained the magnetic energy levels for the conduction electrons, we can then use statistical mechanics to obtain the magnetization per unit volume using

```{math}
:label: eq-p3-ch04-45
M = +k_B T\,\frac{1}{V}\frac{\partial\ln\mathcal{Z}}{\partial H}
```

where the partition function $\mathcal{Z}$ for the conduction electrons is given by Eq. {eq}`eq-p3-ch04-28` and the magnetic susceptibility is given by $\chi = \partial M/\partial H$. Most interest in studies of the magnetic susceptibility has focussed on the magneto-oscillatory phenomena exhibited by the partition function $\mathcal{Z}$ as is further discussed in Chapter 5.
