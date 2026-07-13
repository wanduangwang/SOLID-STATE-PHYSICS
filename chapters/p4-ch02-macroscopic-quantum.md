---
title: "2 Macroscopic Quantum Description of Superconductivity"
abstract: "A macroscopic quantum description of superconductivity is developed, introducing Cooper pairs, the Ginzburg-Landau order parameter wave function, the London equations governing electrodynamics and the Meissner effect, flux quantization, vortex physics in type II materials, and Josephson tunneling effects including SQUID interference."
---

# 2 Macroscopic Quantum Description of Superconductivity

In this chapter, a simple picture of the macroscopic quantum description of superconductivity is presented. The concept of the **Cooper pair** of electrons with equal and opposite vectors and opposite spins is introduced, along with the wave function for all the electrons in the superconductor. From this macroscopic description of the wavefunction, we derive an expression for the super-current, the London equations for the electro-dynamics, the Meissner effect, perfect conductivity, flux quantization, and the Josephson Effect.

## 2.1 The Cooper Pair

Most of the distinctive properties of superconductivity are explained by the macroscopic quantum description of superconductivity. The starting point of this description is that all the superconducting electrons, all $10^{23}$ of them, can be represented quantum mechanically by a single wave function $\Psi(\vec{r})$. Although the exact form of the wave function comes from the Bardeen-Cooper-Schrieffer (BCS) theory, most of the physics of superconductivity follows from the existence of a macroscopic wave function, regardless of the exact form of $\Psi(\vec{r})$.

The physical mechanism for superconducting viability lies in the pairing of the Fermi particles to form a Bose gas of paired quasiparticles. The mechanism for this pairing in conventional superconductors is the **electron-phonon coupling**.

The physical basis for an attraction between two electrons via the electron-phonon interaction was pointed out by Frohlich in 1950. Suppose that one electron passes through the lattice [see Fig. 2.1(a)]. In so doing, it polarizes the positive ion cores and leaves a lattice distortion in the immediate vicinity of the electron trail. If a second electron enters this region before the lattice relaxes, its energy will be lowered because the lattice is already polarized by the first electron. The mechanism shown in Fig. 2.1(a) thus provides an attractive interaction between the two electrons.

This attractive Frohlich interaction is represented by the diagram in Fig. 2.1(b) showing an electron of wave vector $\vec{k}_1$ emitting a phonon of wave vector $\vec{q}$ and being scattered into a state $\vec{k}'_1$ where $\vec{k}_1 + \vec{q} = \vec{k}'_1$. Likewise the second electron with wave vector $k_2$ absorbs the phonon so that $\vec{k}_2 + \vec{q} = \vec{k}'_2$ from which it follows that

```{math}
:label: eq-p4-ch02-1
\vec{k}_1 + \vec{k}_2 = \vec{k}'_1 + \vec{k}'_2 = \vec{b}
```

which shows the conservation of crystal momentum between the initial and final electron states. The vector $\vec{b}$ denotes the sum of the crystal momentum of this electron pair. If $E_1$ and $E'_1$ denote the energy of the first electron before and after scattering, respectively, it follows that $\Delta E_1 = |E_1 - E'_1| < \hbar\omega_q$ where $\hbar\omega_q$ is the phonon energy. This argument shows that the energies involved in this attractive interaction are small, since $\omega_q < \omega_D$ (the Debye frequency) $(\hbar\omega_D/E_F) \sim 10^{-3}$.

The electron-phonon coupling mechanism for superconductivity explains why the highest $T_c$ superconductors are usually metals with the highest resistance in the normal state, since the same mechanism that produces superconductivity (the electron-phonon interaction) also gives rise to carrier scattering in metals in the normal state. The experimental linking of the superconductivity mechanism with the electron-phonon interaction came through the observation of the **isotope effect** (see section 1.7) which showed that for the various mercury isotopes $T_c \propto M^{-1/2}$, where $M$ is the ion mass for each isotope.

Cooper's seminal contribution to the pairing mechanism was to observe that the energy change implied by the pairing mechanism was

```{math}
:label: eq-p4-ch02-2
\Delta E = \frac{\hbar^2}{m}k_F^2 \Delta k \simeq \hbar\omega_D
```

also implies

```{math}
:label: eq-p4-ch02-3
\Delta k \simeq \frac{m\omega_D}{\hbar k_F}
```

and that the maximum number of electron pairs that would obey Eqs. 2.2 and 2.3 occurs when $\vec{b} = 0$ or when $\vec{k}'_1 = -\vec{k}'_2$ (as shown in Fig. 2.2). The Cooper pair is then formed by the electron-phonon interaction between states with wave vectors $\vec{k}$ and $-\vec{k}$ and with opposite spins to maximize the probability that the electrons are close together. The BCS ground state involves the construction of a many body wave function for pairing all the electrons in the Fermi sea to form Cooper pairs with equal and opposite wave vectors and opposite spins. According to BCS theory the energy of this ensemble of paired states is lowered by $2\Delta \sim 3.5k_BT_c$. The energy gap observed experimentally (see section 1.4 and 1.6 of Part IV). From Eq. 2.2, we see that $2\Delta \le \hbar\omega_D$ corresponds to an estimate of $\sim 30$ K for the upper limit of $T_c$ for a superconductor for which the pairing mechanism is the electron-phonon interaction. Therefore the discovery in 1987 of a high $T_c$ superconductor with $T_c \sim 100$ K was so surprising.

:::{figure} images/fig-p4-ch02-1.png
:name: fig-p4-ch02-1
:width: 80%
:align: center
Figure 2.1: (A) A schematic diagram of an electron polarizing positive ions in its vicinity to create an attractive potential for a second electron following in the wake of the first electron. (B) A schematic diagram of an electron-electron interaction transmitted by a phonon of wave vector $\vec{q}$, such that $\vec{k}_1+\vec{q}=\vec{k}'_1+\vec{k}'_2$.
:::

:::{figure} images/fig-p4-ch02-2.png
:name: fig-p4-ch02-2
:width: 55%
:align: center
Figure 2.2: Schematic diagram showing two shells in $\vec{k}$-space of radius $k_F$ and thickness $\Delta k$ corresponding to the two electrons forming a Cooper pair. The cross-hatched section is a cross section of the ring in which the electrons satisfy the conditions $\Delta k=m\omega_D/(\hbar k_F)$ and $\vec{k}_1 + \vec{k}_2 = \vec{b}$. The volume of this ring has a very sharp maximum when the spheres are concentric and $\vec{k}_1=-\vec{k}_2$.
:::

## 2.2 Macroscopic Quantum Description of the Supercurrent

Following the discussion in section 2.1, the wave function for the superconducting electrons can be represented by a single-valued complex function $\Psi(\vec{r})$, having both a real and imaginary part, and possessing the properties described below. These comments are quite general and not dependent on the pairing mechanism. Therefore, if the pairing mechanism for high $T_c$ superconductivity is not through the electron-phonon interaction, many of the properties of superconductors summarized here will still be valid.

We now give a summary of the interpretations of the wave function $\Psi(\vec{r})$:

1. The squared modulus of $\Psi(\vec{r})$ is equal to the density $n_s^*(\vec{r})$ of superconducting Cooper pairs:

```{math}
:label: eq-p4-ch02-4
|\Psi(\vec{r})|^2 = \Psi^*(\vec{r})\Psi(\vec{r})=n_s^*(\vec{r})
```

The asterisk on the wave function signifies complex conjugation, but the asterisk on $n_s^*$ signifies the density of Cooper pairs which is half the density of superconducting electrons $n_s$. That is $2n_s^* = n_s$, since two electrons with wave vectors $\vec{k}$ and $-\vec{k}$ are bound in a Cooper pair. The wavefunction $\Psi(\vec{r})$ thus denotes the degree of superconducting order, and is in that sense an order parameter, which vanishes for $T \ge T_c$ in the normal state.

2. The superconducting current $\vec{j}_s$ is a generalization of the probability current in quantum mechanics

```{math}
:label: eq-p4-ch02-5
\vec{j}_s = \frac{q^*}{2m^*}\left[\Psi^*\!\left(\frac{\hbar}{i}\nabla - \frac{q^*}{c}\vec{A}\right)\!\Psi + \left[\left(\frac{\hbar}{i}\nabla - \frac{q^*}{c}\vec{A}\right)\!\Psi\right]^*\!\Psi\right]
```

where $q^* = -2|e|$ is the charge on the Cooper pair, $m^* = 2m_0$ is the mass of the Cooper pair, and $\vec{A}$ is the magnetic vector potential, where $\nabla \times \vec{A} = \vec{B}$, and $m_0$ is the free electron mass.

3. The time evolution of the wave function is given by Schrodinger's Equation

```{math}
:label: eq-p4-ch02-6
-\frac{\hbar}{i}\frac{\partial\Psi}{\partial t}=\mathcal{H}\Psi=E\Psi
```

where $E$ is the energy for the quantum mechanical state.

## 2.3 The Quantum Mechanical Current

For completeness, we give here a brief derivation of the quantum mechanical current density $\vec{j}$ for a general potential $V(\vec{r})$. This current density $\vec{j}$ was used to write Eq. 2.5. The derivation relies on the continuity equation

```{math}
:label: eq-p4-ch02-7
\frac{\partial\rho}{\partial t} + \vec{\nabla} \cdot \vec{j}=0
```

where $\vec{j}$ is the current density, and $\rho(\vec{r}) = q n(\vec{r})$ denotes the charge density. Then we can write

```{math}
:label: eq-p4-ch02-8
\frac{\partial\rho}{\partial t} = q\frac{\partial}{\partial t} n(\vec{r}) = q\frac{\partial}{\partial t} (\Psi\Psi^*) = q\left[ \left( \frac{\partial\Psi}{\partial t} \right)\!\Psi^* + \Psi \left( \frac{\partial\Psi^*}{\partial t} \right)\right].
```

Using the time-dependent Schrodinger equation Eq. 2.6 and its complex conjugate, we obtain

```{math}
:label: eq-p4-ch02-9
\frac{\partial\rho}{\partial t}=q\left[-\left(-\frac{i}{\hbar}\right)\Psi^*\mathcal{H}\Psi+\Psi\left(\frac{i}{\hbar}\right)\mathcal{H}\Psi^*\right]
```

and substitution of the Hamiltonian

```{math}
:label: eq-p4-ch02-10
\mathcal{H}=\frac{p^2}{2m}+V(\vec{r})=-\left(\frac{\hbar^2\nabla\cdot\nabla}{2m}\right)+V(\vec{r})
```

into Eq. 2.9 consequently yields

```{math}
:label: eq-p4-ch02-11
\frac{\partial\rho}{\partial t}=\left(\frac{q\hbar i}{2m}\right)(\Psi^*\vec{\nabla}\cdot\vec{\nabla}\Psi-\Psi\vec{\nabla}\cdot\vec{\nabla}\Psi^*) = \vec{\nabla}\cdot\left[\left(\frac{q\hbar i}{2m}\right)(\Psi^*\vec{\nabla}\Psi-\Psi\vec{\nabla}\Psi^*)\right]=-\vec{\nabla}\cdot\vec{j}
```

making use of the continuity equation and the fact that since $\Psi$ and $\Psi^*$ only differ by a phase factor, $\vec{\nabla}\Psi$ and $\vec{\nabla}\Psi^*$ commute

```{math}
:label: eq-p4-ch02-12
[\vec{\nabla}\Psi^*, \vec{\nabla}\Psi] =0.
```

We thus identify the current density with

```{math}
:label: eq-p4-ch02-13
\vec{j}=\frac{q}{2m}\left[\Psi^*\!\left(\frac{\hbar}{i}\vec{\nabla}\right)\!\Psi-\Psi\left(\frac{\hbar}{i}\vec{\nabla}\right)\!\Psi^*\right]=\frac{q}{2m}\left[\Psi^*p\Psi+\text{c.c.}\right]
```

showing that the second term in Eq. 2.13 is the complex conjugate of the first, thereby guaranteeing that $\vec{j}$'s a Hermitian operator that will yield real eigenvalues. In the presence of a magnetic field, we replace $\vec{p}$ by

```{math}
:label: eq-p4-ch02-14
\vec{p}\rightarrow\vec{p}-\frac{q}{c}\vec{A}
```

so that Eq. 2.13 then becomes

```{math}
:label: eq-p4-ch02-15
\vec{j}=\left(\frac{q}{2m}\right)\!\left\{\Psi^*\!\left(\frac{\hbar}{i}\vec{\nabla}-\frac{q}{c}\vec{A}\right)\!\Psi+\left[\Psi^*\!\left(\frac{\hbar}{i}\vec{\nabla}-\frac{q}{c}\vec{A}\right)\!\Psi\right]^*\right\}
```

where again the second term in Eq. 2.15 is the complex conjugate of the first. If we identify the charge $q$ and the mass $m$ with the effective charge $q'$ and the effective mass $m^*$, respectively, then Eq. 2.15 yields Eq. 2.5 for the superconducting current $\vec{j}_s$.

## 2.4 The Supercurrent Equation

In considering the role of the wave function $\Psi(\vec{r})$ in the superconductivity problem, the current density given by Eq. 2.15 is a very important and useful equation. Ginzburg and Landau observed that all the Cooper pairs are in the same two-electron state, and therefore a single complex wavefunction can denote the order parameter of the superconducting state. With this interpretation of $\Psi(\vec{r})$ as a complex order parameter for a Cooper pair, then $\Psi(\vec{r})$ can be written in terms of an amplitude and a phase

```{math}
:label: eq-p4-ch02-16
\Psi(\vec{r})=|\Psi(\vec{r})|e^{i\theta(\vec{r})}=[n_{s*}^{1/2}] e^{i\theta(\vec{r})}
```

where we have not explicitly considered the time dependence of $\Psi(\vec{r})$. Here we assume that the significant spatial variation of the wave function is through the phase $\theta(\vec{r})$, so that the density of Cooper pairs is essentially independent of position and time. Putting this form of $\Psi(\vec{r})$ into Eq. 2.5 gives:

```{math}
:label: eq-p4-ch02-17
\vec{j}_s=\left(-\frac{{q^*}^2 n_s^*}{m^* c}\right)\!\vec{A}+\left(\frac{{q^*} n_s^* \hbar}{m^*}\right)\!\vec{\nabla}\theta=\left[-\frac{{q^*}^2}{m^* c}\vec{A}+\frac{q^* \hbar}{m^*}\vec{\nabla}\theta\right]|\Psi|^2
```

or

```{math}
:label: eq-p4-ch02-18
\vec{j}_s=-\frac{\vec{A}}{\Lambda_s c}+\frac{\hbar}{q^*\Lambda_s}\vec{\nabla}\theta
```

which is the **Supercurrent Equation** in which

```{math}
:label: eq-p4-ch02-19
\frac{1}{\Lambda_s}=\frac{{q^*}^2 n_s^*}{m^*}=\frac{e^2 n_s}{m_0}.
```

From Eq. 2.18 we see that the supercurrent $\vec{j}_s$ is driven by two terms. The first term is strictly a classical term which is proportional to the classical vector potential $\vec{A}$. The second term is a partly quantum mechanical term which is proportional to the gradient of the phase $\theta(\vec{r})$ of the wave function. Although the second term looks purely quantum mechanical, the change of phase can also result from a classical field. For example, if Eq. 2.16 is substituted into the time-dependent Schrodinger equation Eq. 2.6, and if we assume the amplitude of the wave function is independent of time (which is equivalent to saying that the density of Cooper pairs is time independent), we have simply that

```{math}
:label: eq-p4-ch02-20
\frac{\partial\theta}{\partial t}=-\frac{\mathcal{H}}{\hbar}.
```

Therefore, in an applied electrical field, the Hamiltonian is perturbed by the scalar potential $\phi(\vec{r})$

```{math}
:label: eq-p4-ch02-21
\mathcal{H}=\mathcal{H}_0+q^*\phi(\vec{r}).
```

From Eq. 2.20, we see that a classical voltage $q^*\phi(\vec{r})$ causes the quantum mechanical phase of the wavefunction $\theta(\vec{r})$ to change with time.

## 2.5 The London Equations

We now derive the two London equations which describe the electrodynamics of superconductors from the supercurrent equation (Eq. 2.18). The first London equation relates to the perfect conductivity of superconductors, while the second London equation follows from the perfect diamagnetism condition, or the Meissner effect.

### 1. Perfect Conductivity - First London Equation

By assuming that the density of Cooper pairs $n_s^*$ is independent of time, then differentiation of Eq. 2.18 yields

```{math}
:label: eq-p4-ch02-22
\frac{\partial\vec{j}_s}{\partial t}=-\left(\frac{1}{c\Lambda_s}\right)\frac{\partial\vec{A}}{\partial t}+\left(\frac{\hbar}{q^*\Lambda_s}\right)\vec{\nabla}\frac{\partial\theta}{\partial t}.
```

We can write $(\partial\theta/\partial t)$ in terms of the Hamiltonian from Eq. 2.20 and in the presence of an applied electric field as

```{math}
:label: eq-p4-ch02-23
\hbar\frac{\partial\theta}{\partial t}=-\left(\mathcal{H}_0+q^*\phi(\vec{r})\right).
```

Assuming that $\mathcal{H}_0$ is independent of position, Eq. 2.22 becomes

```{math}
:label: eq-p4-ch02-24
\frac{\partial\vec{j}_s}{\partial t}=-\Lambda_s^{-1}\left(\frac{\partial\vec{A}}{c\partial t}+\vec{\nabla}\phi\right)=\Lambda_s^{-1}\vec{E},
```

which states that current flows under the influence of an electric field without any damping, $m\vec{v}=e\vec{E}$. This equation relates to the perfect conductivity of superconductors and is known as the **first London equation**. This equation is usually written as

```{math}
:label: eq-p4-ch02-25
\vec{E}=\Lambda_s\frac{\partial\vec{j}_s}{\partial t}
```

where $\Lambda_s=m^*/({q^*}^2 n_s^*)$.

### 2. Perfect Diamagnetism - Second London Equation

By taking the curl of Eq. 2.18, the supercurrent equation, we obtain the second London equation

```{math}
:label: eq-p4-ch02-26
\vec{\nabla}\times\vec{j}_s=-\frac{1}{\Lambda_s c}\vec{B}
```

where we note that $\vec{\nabla}\times\vec{\nabla}\theta=0$ because the curl of a gradient vanishes. Using Maxwell's equation $\vec{\nabla}\times\vec{H}=(4\pi/c)\vec{j}$, neglecting the displacement current, and noting that $\vec{B}=\mu\vec{H}$, we obtain

```{math}
:label: eq-p4-ch02-27
\vec{\nabla}\times\vec{\nabla}\times\vec{B}=-\left(\frac{4\pi\mu}{c^2\Lambda_s}\right)\vec{B}.
```

Since

```{math}
:label: eq-p4-ch02-28
\vec{\nabla}\times\vec{\nabla}\times\vec{B}=\vec{\nabla}(\vec{\nabla}\cdot\vec{B})-\nabla^2\vec{B}
```

and since $\vec{\nabla}\cdot\vec{B}=0$, we further obtain

```{math}
:label: eq-p4-ch02-29
\nabla^2\vec{B}=\frac{1}{\lambda_s^2}\vec{B}
```

where $\lambda_s$ is the superconducting penetration depth and from Eqs. 2.27 and 2.29 we obtain:

```{math}
:label: eq-p4-ch02-30
\lambda_s=(\Lambda_s c^2)^{1/2}=\left(\frac{m^*c^2}{4\pi\mu q^{*2}n_s^*}\right)^{1/2}.
```

The penetration depth $\lambda_s$ has a magnitude $\lambda_s \sim 1000$ Angstroms, which is obtained by assuming that there are $n_s \sim 10^{23}$ electrons/cm$^3$ and using Eq. 2.19 to yield $\Lambda_s \sim 10^{-31}$ sec$^2$. The second London equation thus implies an exponential spatial decay of the $\vec{B}$ field in the superconductor with a functional dependence,

```{math}
:label: eq-p4-ch02-31
B(z)=B(0)\exp(-z/\lambda_s).
```

Equation 2.31 is the physical manifestation of the **Meissner effect**, which states that the $\vec{B}$ field is excluded from the interior of the superconductor. The exponential decay of the $\vec{B}$ field in a superconductor, also leads to the decay of the current density $\vec{j}_s$ in the same superconducting penetration depth. This result is obtained by taking the curl of the second London equation (Eq. 2.26) which gives

```{math}
:label: eq-p4-ch02-32
\vec{\nabla}\times\vec{\nabla}\times\vec{j}_s=-\frac{1}{\Lambda_s c}\vec{\nabla}\times\vec{B}=-\frac{\hat{\mu}}{\Lambda_s c}\left(\frac{4\pi}{c}\right)\vec{j}_s.
```

From the continuity equation we can write $\vec{\nabla}\cdot\vec{j}=0$ for the steady state condition, and we thus obtain a differential equation for $\vec{j}_s$

```{math}
:label: eq-p4-ch02-33
-\nabla^2\vec{j}_s=-\left(\frac{\hat{\mu}}{\Lambda_s c}\right)\frac{4\pi}{c}\vec{j}_s=-\left(\frac{1}{\lambda_s^2}\right)\vec{j}_s.
```

Thus we see that the second London equation in the steady state leads to an exponential decay of both the $\vec{B}$ field and the supercurrent $\vec{j}_s$ as we move away from the surface into the superconductor. This rapid exponential decay of $\vec{B}, \vec{j}_s$ and also $\vec{H}$ (since $\vec{B}=\mu\vec{H}$)

```{math}
:label: eq-p4-ch02-34
B(z)=B(0)e^{-z/\lambda_s}
```

```{math}
:label: eq-p4-ch02-35
H(z)=H(0)e^{-z/\lambda_s}.
```

```{math}
:label: eq-p4-ch02-36
j_s(z)=j_s(0)e^{-z/\lambda_s}.
```

clarifies the Meissner effect regarding the exclusion of flux in a superconductor.

## 2.6 The Two-Fluid Model

The London equations are appropriate at $T = 0$ where all the electrons are in Cooper pairs. To describe the electrodynamics at a finite temperature, a two-fluid model is introduced. According to this model the total current density in a superconductor is considered to be a superposition of the contributions to the current from the superconducting electron pairs and from the normal electrons, which are identified with quasi-electrons that are excited above the superconducting energy gap by breaking Cooper pairs. We then write:

```{math}
:label: eq-p4-ch02-37
j=j_n+j_s
```

as the superposition of a normal (resistive) current given by

```{math}
:label: eq-p4-ch02-38
\vec{j}_n=\sigma\vec{E}
```

and a superconducting current $\vec{j}_s$. Then from Maxwell's equations, we can write

```{math}
:label: eq-p4-ch02-39
\left(\frac{c}{\mu}\right)\vec{\nabla}\times\vec{B}=4\pi(\sigma\vec{E}+\vec{j}_s)+\epsilon\dot{\vec{E}},
```

in which we have also included the displacement current $\vec{D}=\epsilon\dot{\vec{E}}$. We can thus write

```{math}
:label: eq-p4-ch02-40
\left(\frac{c}{\mu}\right)\vec{\nabla}\times\vec{B}=-\left(\frac{c}{\mu}\right)\nabla^2\vec{B}=4\pi(\sigma\vec{\nabla}\times\vec{E}+\vec{\nabla}\times\vec{j}_s)+\epsilon\vec{\nabla}\times\dot{\vec{E}},
```

or, using Eq. 2.26 for $\vec{\nabla}\times\vec{j}_s$, we obtain

```{math}
:label: eq-p4-ch02-41
\frac{1}{\mu}\nabla^2\vec{B}=\frac{4\pi\sigma}{c^2}\dot{\vec{B}}+\frac{4\pi}{\Lambda_s c^2}\vec{B}+\frac{\epsilon}{c^2}\ddot{\vec{B}}.
```

If we seek a plane wave solution

```{math}
:label: eq-p4-ch02-42
B\sim\exp[-i(\omega t-\vec{k}\cdot\vec{r})],
```

then Eq. 2.41 gives

```{math}
:label: eq-p4-ch02-43
\frac{k^2c^2}{\hat{\mu}}=-\frac{4\pi}{\Lambda_s}+4\pi\sigma\omega i+\omega^2.
```

The successive terms on the right hand side of Eq. 2.43 represent the effects of the superconducting penetration depth, the ordinary eddy current skin depth, and the displacement current. Equation 2.43 determines the propagation characteristics at finite temperature of a superconductor in an electromagnetic field.

In the limit of low frequencies,

```{math}
:label: eq-p4-ch02-44
k\simeq i\left(\frac{4\pi\hat{\mu}}{\Lambda_s c^2}\right)^{\frac{1}{2}},
```

which represents the exponential decay of the $B$ field discussed in section 2.5, where the superconducting penetration depth $\lambda_s$, is given by

```{math}
:label: eq-p4-ch02-45
\lambda_s=(\Lambda_s c^2)^{\frac{1}{2}}=\left(\frac{mc^2}{4\pi n^2 e^2 \hat{\mu}}\right)^{\frac{1}{2}},
```

and $\Lambda_s$ is one of the important length scales in a superconductor. Here $m$, $n$ and $e$ refer to single electron states, utilizing the relation between the characteristics of Cooper pairs and the single electron states (see Eq. 2.19).

We recall that for a **normal conductor** in a time-varying ac magnetic field, that the magnetic field is confined to a skin depth near the surface of thickness $\delta_n=c(2\pi\mu\omega\sigma)^{-1/2}$. In the radio frequency range, $\delta_n \gg \lambda_s$, so that the superconducting wavelength length dominates the spatial variations of the field. In the millimeter wave range $\delta_n$ and $\lambda_s$ can be of comparable magnitudes, but then for most conventional superconductors the electromagnetic frequency would exceed the superconducting band gap, and would serve to break the Cooper pairs and give rise to behavior similar to that observed in a normal metal.

## 2.7 Flux Quantization

Besides perfect conductivity and perfect diamagnetism (Meissner effect), quantization of the magnetic flux is characteristic of superconductivity. Flux quantization follows directly from Eq. 2.18, the supercurrent equation, and from the interpretation of the wave function, as discussed below. Rearranging Eq. 2.18, we have

```{math}
:label: eq-p4-ch02-46
\vec{\nabla}\theta=q^*\left(\frac{\Lambda_s}{\hbar}\right)\vec{j}_s+\left(\frac{q^*}{hc}\right)\vec{A}.
```

Integrating Eq. 2.46 around a closed contour yields the phase difference around the contour

```{math}
:label: eq-p4-ch02-47
\oint_c\vec{\nabla}\theta\cdot d\vec{s}=q^*\frac{\Lambda_s}{\hbar}\oint_c\vec{j}_s\cdot d\vec{s}+\frac{q^*}{hc}\oint_c\vec{A}\cdot d\vec{s}.
```

Now, the first term on the left of Eq. 2.47 can be integrated directly to yield a phase difference

```{math}
:label: eq-p4-ch02-48
\oint_c(\vec{\nabla}\theta)\cdot d\vec{s}=\theta_2-\theta_1,
```

where $\theta_2-\theta_1$ is the phase difference of the wave function in going around a closed loop. Our interpretation of the complex wave function, $|\Psi(\vec{r})|e^{i\theta}$, where $|\Psi(\vec{r})|^2$ equals the density of Cooper pairs in $\vec{r}$, demands only that the modulus be a single-valued function. The phase can in general be multi-valued as long as the function $\Psi(\vec{r})$ is invariant under rotation by $2\pi$ or in other words $e^{i(\theta+2\pi)}=1$. From this argument it follows that $\theta_1-\theta_2=\pm2n\pi$.

The last term in Eq. 2.47 becomes, after using Stokes' theorem,

```{math}
:label: eq-p4-ch02-49
\oint\vec{A}\cdot d\vec{s}=\int(\vec{\nabla}\times\vec{A})\cdot d\vec{S}=\int\vec{B}\cdot d\vec{S}=\Phi
```

where $\Phi$ is the flux enclosed by the contour and $S$ is the area defined by the contour. Hence, Eq. 2.47 becomes

```{math}
:label: eq-p4-ch02-50
\pm2\pi n=\frac{q^*\Lambda_s}{\hbar}\oint\vec{j}_s\cdot ds+\frac{q^*}{hc}\Phi
```

where $n$ is an integer. If the path of the line integral for the supercurrent is chosen to be deep inside the superconducting material, so that $\vec{j}_s=0$, then

```{math}
:label: eq-p4-ch02-51
|\Phi|=\frac{hc}{q^*}2\pi n=\frac{hc}{q^*}n
```

which gives the quantization of flux in units of $(hc/q^*) = \Phi_0$, if the supercurrent flows around the path of the superconductor. For $|q^*|=|2e|$ we thus obtain a magnitude for the flux quantum $\Phi_0=ch/2e=2.07\times 10^{-7}$ gauss cm$^2 = 2.0678\times 10^{-15}$ tesla m$^2$. As an example of flux quantization, consider the metallic torus (see Fig. 1.2) which is cooled in a magnetic field to a temperature below $T_c$. If the magnetic field is then removed, flux will be trapped. Suppose that $a$ is the radius of the cross section of the torus. Then if $a \gg \lambda_s$, then all the currents decay exponentially from the surface of the torus. By considering a contour many penetration depths from the surface, the current density $j_s$ can be made negligibly small. Hence, the quantization condition of Eq. 2.51 states that the flux $\Phi$ passing through the torus is quantized in units of $\Phi_0$ or that $\Phi=n\Phi_0$.

:::{figure} images/fig-p4-ch02-3.png
:name: fig-p4-ch02-3
:width: 50%
:align: center
Figure 2.3: Triangular lattice of flux lines through the top surface of a superconducting cylinder as observed in an electron microscope. The points where the flux lines exit the surface are decorated with fine ferromagnetic particles.
:::

## 2.8 The Vortex Phase and Trapped Flux

Physically, the lower critical field $H_{c1}$ (see Fig. 1.6) denotes an applied magnetic field large enough to create one fluxoid in the area of flux penetration (estimated as $\lambda_s^2$)

```{math}
:label: eq-p4-ch02-52
\pi\lambda_s^2\hat{\mu}H_{c1}=\Phi_0
```

where $\Lambda_s$ is the superconducting penetration depth. Thus, $H_{c1}$ measures the initiation of flux penetration into a type II superconductor.

In the vortex state of a type-II superconductor, the vortices form a regular lattice (see Fig. 2.3). This can be understood physically if we recognize that two vortices of the same sign repel one another which maximizes their distance apart, while requiring a fixed number density to account for the specified flux penetration. There are many examples in physics of ordering caused by similar competing processes. For simplicity, we consider the vortex lattice to be a square array, although the results given below are independent of the type of regular array (i.e., whether it is triangular or square). Consider an infinite slab of a vortex array (such as Fig. 2.3) with the field perpendicular to the top surface. Suppose that the vortices are a distance $2a$ apart and have a non-superconducting (normal) core of radius $\xi_s$ which is surrounded by superconducting material.

Consider the contour $c$ for the line integral in Eq. 2.50 drawn along the perpendicular bisectors between one vortex and its nearest neighbor vortices. If flux goes through each vortex, there must be a circulating current around each vortex. By symmetry, the circulating currents are identically zero along a contour drawn along the bisectors of the distance between the vortices. (A similar contour with $\vec{j}_s=0$ can be found for any regular array.) Hence, the quantization condition (Eq. 2.51) requires the flux within the contour to be an integral number of flux quanta $n\Phi_0$. The same condition holds for each vortex, so that for a triangular lattice $n\Phi_0=\hat{\mu}H_a(3\sqrt{3}/2)a^2$, where $H_a$ is the applied magnetic field.

Experimentally, $n=1$ for type II superconductors at the closest packing of the vortices. Hence, $H_{a2}=\Phi_0/(\mu\xi_s^2(3\sqrt{3}/2))$ for the closest packing of the vortices, which we explain as follows. As the applied field is increased above $H_{c1}$, the spacing $2a$ between vortices becomes smaller and smaller. The spacing can only get as small as some minimal distance $a=\xi_s$, when the cores on adjacent vortices begin to overlap and the material becomes normal. This minimal distance $\xi_s$ is called the superconducting coherence distance, and is an important length scale in a superconductor. The externally applied field corresponding to $a=\xi_s$ is called the "**upper critical field**" $H_{c2}$, so that $H_{c2}=\Phi_0/(\hat{\mu}\beta\xi_s^2/2)$.

Since the magnetic field will be uniform within the core, the long, and hence the currents, will fall off exponentially from the edge of the core as long as $a \gg \lambda_s$. For most type-II superconductors $\lambda_s \gg \xi_s$, so that most of the flux is contained in an area $\lambda_s^2$ around the core, and a very small fraction of the flux $(\xi_s^2/\lambda_s^2)\Phi_0 \ll \Phi_0$ is in the core itself. Therefore, by considering a contour very near the edge of the core, the quantization condition gives

```{math}
:label: eq-p4-ch02-53
\Phi_0=\frac{4\pi|\lambda_s^2|}{c}\oint\vec{j}_s\cdot d\vec{s}+\frac{c\xi_s^2}{\lambda_s^2}\Phi_0
```

and neglecting the term in $(\xi_s^2/\lambda_s^2)\Phi_0$ we can write

```{math}
:label: eq-p4-ch02-54
\Phi_0=\frac{4\pi\tilde{\mu}\lambda_s^2}{c}\oint\vec{j}_s\cdot d\vec{s}.
```

That is, near the core it is the line integral of the current which is quantized in integral numbers of flux units. The circulating current near the core is in the $\hat{i}_{\circ}$ circumferential direction. Carrying out the line integral in Eq. 2.54 thus yields

```{math}
:label: eq-p4-ch02-55
\Phi_0=\frac{4\pi\tilde{\mu}\lambda_s^2}{c}j_s 2\pi r
```

or

```{math}
:label: eq-p4-ch02-56
j_s=\frac{\Phi_0 c}{2(2\pi)^2\hat{\mu}\lambda_s^2}\frac{1}{r}.
```

Thus for a vortex we see that the current density decreases as $1/r$, which is also true for a hydrodynamic vortex (e.g., water flowing down a drain). By noting that

```{math}
:label: eq-p4-ch02-57
\vec{j}_s=n_s^*\vec{q}^*\vec{v}_s
```

and writing

```{math}
:label: eq-p4-ch02-58
\frac{4\pi\tilde{\mu}\lambda_s^2}{c^2}=\Lambda_s=\frac{m^*}{n_s^{*2}q^2}
```

we have,

```{math}
:label: eq-p4-ch02-59
j_s=n_s^*\vec{q}^*v_s=\frac{c^2 h/(2e)}{2\pi c^2(m^*/n_s^{*2}q^2)}\frac{1}{r}=\frac{hn_s^{*2}q^2)}{m^*}\frac{1}{r}
```

or

```{math}
:label: eq-p4-ch02-60
v_s=\frac{h}{m^*}\frac{1}{r}
```

yielding the quantization condition

```{math}
:label: eq-p4-ch02-61
\int\vec{v}_s\cdot d\vec{l'}=\frac{h}{m^*}.
```

Furthermore, velocity cannot be made arbitrarily large, because the minimum size of $r$ is the superconducting coherence distance $r \ge \xi_s$, the coherence distance, thus yielding

```{math}
:label: eq-p4-ch02-62
v_{max}=\frac{h}{m^*}\frac{1}{\xi_s}.
```

The circulating currents acquire an additional kinetic energy in circulating around the vortices. However, if this additional kinetic energy exceeds $\Delta_0$, where $2\Delta_0$ is the gap energy, the Cooper pairs will unbind. That is why the core region of a vortex cannot be superconducting but must be normal! To estimate the core size, note that

```{math}
:label: eq-p4-ch02-63
\Delta_0=\delta\left(\frac{1}{2}m^*v^2\right)=m^*\delta v v.
```

Since the electrons forming the Cooper pairs are at the Fermi surface, we can write $v=v_F$ and $\delta v=v_s$, where $v_s$ is the velocity of the Cooper pair. Therefore, using Eq. 2.62 and writing $\delta v_s$ as the maximum vortex velocity we obtain:

```{math}
:label: eq-p4-ch02-64
\Delta_0\simeq m^*v_F\left(\frac{h}{m^*}\frac{1}{\xi_s}\right)
```

so that

```{math}
:label: eq-p4-ch02-65
\xi_s\approx\frac{hv_F}{\Delta_0}.
```

From the BCS theory of superconductivity, $\xi_s$ for a clean material with very little scattering is given by

```{math}
:label: eq-p4-ch02-66
\xi_0=\frac{hv_F}{\pi\Delta_0}
```

where $\xi_0$ is called the "**BCS coherence length**", and is the length over which Cooper pairs are correlated in the absence of any scattering.

## 2.9 Summary of Length Scales

We list in Table 2.1 some of the characteristic lengths found in superconductors. In section 2.5, we discussed the superconducting penetration depth $\lambda_s$

```{math}
:label: eq-p4-ch02-67
\lambda_s=\left(\frac{m_0c^2}{4\pi\hat{\mu}e^2}\right)^{1/2}
```

which governs the penetration of magnetic fields and supercurrents in the superconducting state (see Eqs. 2.34 -- 2.36). In most cases, the superconducting penetration depth is much smaller than the penetration depth $\delta_n$ in the normal state $\delta_n$

```{math}
:label: eq-p4-ch02-68
\delta_n=\frac{c}{(2\pi\hat{\mu}\omega\sigma)^{1/2}}.
```

Important parameters for type II superconductors are the intrinsic superconducting coherence length $\xi_0$ which by the BCS theory is written as

```{math}
:label: eq-p4-ch02-69
\xi_0=\frac{hv_F}{\pi\Delta_0}
```

:::{table} Some characteristic length scales for superconducting materials. The superconductors with $\kappa=\lambda_s^0/\xi_0>1/\sqrt{2}=0.71$ are type II. Here $\lambda_s^0$ and $\xi_0$ are the superconducting penetration depth and coherence length in the clean limit.
:name: tab-p4-ch02-1
| Material | $\lambda_s^0$(Angstroms) | $\xi_0$(Angstroms) | $\lambda_s^0/\xi_0$ |
|----------|------------------------|---------------------|---------------------|
| Sn       | 3,400                  | 23,000              | 0.16                |
| Al       | 1,600                  | 160,000             | 0.01                |
| Pb       | 3,700                  | 8,300               | 0.45                |
| Cd       | 11,000                 | 76,000              | 0.14                |
| Nb       | 3,900                  | 3,800               | 1.02                |
| YBa$_2$Cu$_3$O$_{7-x}\parallel$ | 170 | 3.0   | 56                  |
| YBa$_2$Cu$_3$O$_{7-x}\perp$    | 6,400 | 16.4  | 390                 |
:::

and the coherence length $\xi_s$ in real superconducting materials (in the dirty limit) is given by

```{math}
:label: eq-p4-ch02-70
\xi_s=(\xi_0\ell_n)^{1/2}
```

where $\ell_n$ is the mean free path for the carriers in the normal state, and is temperature dependent. Likewise, the superconducting penetration depth $\lambda_s$ in dirty superconductors (i.e., $\ell_n \ll \xi_0$) is given by

```{math}
:label: eq-p4-ch02-71
\lambda_s=\lambda_s^0\left(\frac{\xi_0}{\ell_n}\right)^{1/2}
```

where $\lambda_s^0$ is the superconducting penetration depth (see Table 2.1) for large $\ell_n$ (e.g., $\ell_n > \xi_0$).

From Eqs. 2.70 and 2.71, we then conclude that

```{math}
:label: eq-p4-ch02-72
\kappa\equiv\frac{\lambda_s}{\xi_s}=\frac{\lambda_s^0}{\xi_0}.
```

The parameter $\kappa$ defined by Eq. 2.72 is used to distinguish type I superconductors ($\kappa<1/\sqrt{2}$) from type II superconductors ($\kappa>1/\sqrt{2}$), and typical values of $\kappa$ for some superconductors are given in Table 2.1. Thus the decrease in $\ell_n$ favors type II superconductivity (see Fig. 2.4), but in the limit of small $\ell_n$ we have $\xi_s \ll \xi_0$ with a relatively low $\lambda_s$. One major contrast between conventional superconductors and high $T_c$ superconductors is the relatively high $\kappa$ values for the high $T_c$ superconductors.

:::{figure} images/fig-p4-ch02-4.png
:name: fig-p4-ch02-4
:width: 65%
:align: center
Figure 2.4: Penetration depth $\Lambda_s$ and the coherence length $\xi$ as functions of the mean free path $\ell_n$ of the conduction electrons in the normal state. All lengths are in units of $\xi_0$, the intrinsic coherence length. The curves are sketched for $\xi_0 = 10\lambda_s^0$, where $\lambda_s^0$ is the superconducting penetration depth for large $\ell_n$. For short mean free paths the coherence length becomes shorter and the penetration depth becomes longer. A decrease in $\ell_n$ favors type II superconductivity.
:::

## 2.10 Weakly-Coupled Superconductors -- The Josephson Effect

Suppose that a thin nominally non-superconducting region connects two superconductors (see Fig. 2.5). Then the wavefunctions of the Cooper pairs in the two superconductors can overlap and produce a coupling between them. Put another way, we can say that the two regions of strong superconductivity are now connected by a region of weak superconductivity or by a weak link. It also seems plausible that the detailed properties of the non-superconducting region won't matter too much other than to establish the thickness required to get appreciable coupling between the superconductors.

:::{figure} images/fig-p4-ch02-5.png
:name: fig-p4-ch02-5
:width: 75%
:align: center
Figure 2.5: Schematic diagram for (a) a Josephson junction. (b) and (c) are schematic diagrams for various kinds of weak links. All of these cases exhibit the Josephson effect.
:::

Assume that at the two boundaries of the weak link region we set the wave functions across the boundaries equal to one another (see Fig. 2.5). Then, if we make the reasonable assumption that in general $\Psi(\vec{r})$ decays exponentially from the edges, we have to the first approximation (valid when $\ell_w \gg \xi_N$ where $\xi_N$ is the characteristic edge length of a Cooper pair wave function in the junction region and $\ell_w$ is the length of the weak link). Thus we write for the wave function in the weak link (normal state)

```{math}
:label: eq-p4-ch02-73
\Psi_N(x)=|\Psi_{N1}|e^{-(x/\xi_N)}+|\Psi_{N2}|e^{((\ell_w-x)/\xi_N)}e^{i\Delta\theta}
```

where the factor $e^{i\Delta\theta}$ accounts for the very important fact that the phase of the wave function for the Cooper pair on the two sides of the weak link will not in general be the same.

More generally, we could assume that $\Psi_N(x)$ is governed by the equation

```{math}
:label: eq-p4-ch02-74
\xi_N^2\frac{d^2\Psi_N(x)}{dx^2}=\Psi_N(x)
```

subject to the boundary conditions $\Psi_N(0)=\Psi_{N1}$ and $\Psi_N(\ell)=\Psi_{N2}$. In this case $\Psi_N(x)$ can be written in the form

```{math}
:label: eq-p4-ch02-75
\Psi_N(x)=f_1(x)+f_2(\ell_w-x)e^{i\Delta\theta}
```

where $f_1(x)$ and $f_2(x)$ are governed by an equation of the form

```{math}
:label: eq-p4-ch02-76
\xi_N^2\frac{df}{dx^2}=f
```

with the boundary conditions

```{math}
:label: eq-p4-ch02-77
f_{1,2}(0)=|\Psi_{N1,N2}|.
```

Neglecting the presence of magnetic fields for the moment, the current through the junction can be calculated using Eq. 2.13, and we obtain the result

```{math}
:label: eq-p4-ch02-78
\vec{j}_s=\frac{q^*\hbar}{2m^*i}\left(\Psi^*\vec{\nabla}\Psi-\Psi\vec{\nabla}\Psi^*\right)=\frac{q^*\hbar}{m^*}\text{Im}(\Psi^*\vec{\nabla}\Psi)
```

and using Eq. 2.73 for $\Psi$ we obtain

```{math}
:label: eq-p4-ch02-79
j_s=\frac{2q^*\hbar}{m^*\xi_N}|\Psi_{N1}||\Psi_{N2}|\sin\Delta\theta
```

which we write as

```{math}
:label: eq-p4-ch02-80
j_s=j_0\sin\Delta\theta
```

where

```{math}
:label: eq-p4-ch02-81
j_0=\frac{2q^*\hbar}{m^*\xi_N}|\Psi_{N1}||\Psi_{N2}|
```

and $\Delta\theta$ is the phase difference of the superconducting wave function across the weak link.

Equation 2.80 states that dc tunneling of Cooper pairs can occur when the current density is less than the maximum value $j_0$. For current density values above $j_0$, some of the current must be carried by normal electrons, and there must by a voltage drop across the junction. We thus interpret $j_0$ as the maximum current that can pass through a Josephson junction before driving it normal (see Fig. 2.6).

We thus obtain the remarkable result that the current is a sinusoidal function of the phase difference across the superconductor. Such behavior is known as the **dc Josephson effect**. Although Josephson predicted this result from the point of view of tunneling through an oxide barrier between two superconductors, it is a quite general property of weakly coupled superconductors as our discussion above suggests. Josephson recognized this fact and so one for the first thing to emphasize the generality of the Josephson effect. For his extremely important discovery, Josephson was awarded the Nobel Prize in 1973.

Referring to Eqs. 2.20 and 2.21 we see that the time derivative of the phase difference across a Josephson junction is given by

```{math}
:label: eq-p4-ch02-82
\frac{\partial}{\partial t}(\theta_2-\theta_1)=-\frac{2eV}{\hbar}
```

so that:

```{math}
:label: eq-p4-ch02-83
\theta_2-\theta_1=-\frac{2eV}{\hbar}t
```

which states that the current in Eq. 2.80 oscillates with a frequency

```{math}
:label: eq-p4-ch02-84
\omega_J=\frac{2eV}{\hbar}.
```

This time dependent oscillation is known as the ac Josephson effect. A dc voltage of 1 microvolt across the Josephson junction produces a phase oscillation frequency $\omega_J$ of 483.6 MHz. Equation 2.84 implies that when a Cooper pair crosses the weak link junction a photon of frequency $\omega J$ is emitted or absorbed.

:::{figure} images/fig-p4-ch02-6.png
:name: fig-p4-ch02-6
:width: 55%
:align: center
Figure 2.6: Current-voltage characteristics of a Josephson junction. Dc currents flow under zero applied voltage up to a critical current $j_c$ (or the critical current density $j_0$); this is the dc Josephson effect. At voltages above $V_c$ the junction has a finite resistivity. Below $V_c$ the current has an oscillatory component of frequency $\omega_J=2eV/h$: this is the ac Josephson effect.
:::

## 2.11 Effect of Magnetic Fields on Josephson Junctions -- Superconducting Quantum Interference

The fact that the current through a Josephson junction depends on the quantum phase difference across the junction gives rise to quantum interference effects in circuits containing these junctions. Moreover, from the supercurrent equation (Eq. 2.18) we see that the phase differences introduced by the Josephson junction will be sensitive to the presence of magnetic fields. These quantum interference effects are a spectacular demonstration of the quantum nature of superconductivity. The Josephson effect is also important from a practical point of view, because the great sensitivity of circuits containing Josephson junctions to magnetic fields, making possible very sensitive magnetometers using these quantum interference effects (these devices are called **SQUID**'s (superconducting quantum interference devices). At the same time the magnetic field provides a way of altering the electrical characteristics of single Josephson junctions, thereby providing a way to convert these junctions into three-terminal devices. As is well known, three-terminal devices are much more versatile than two-terminal devices in electronic circuitry.

:::{figure} images/fig-p4-ch02-7.png
:name: fig-p4-ch02-7
:width: 55%
:align: center
Figure 2.7: The geometrical arrangement demonstrating macroscopic superconducting quantum interference in a SQUID. A magnetic flux $\Phi$ passes through the interior of the loop containing two Josephson junctions.
:::

## 2.12 Quantum Interference Between Two Junctions

Consider a parallel-connected superconducting circuit in which each arm of the circuit contains a Josephson junction denoted as an insulator in Fig. 2.7. Assume for the moment that the junction behaves uniformly so that the phase change across the junction is the same over the entire junction. The total current flowing through the two junctions connected in parallel is then written as

```{math}
:label: eq-p4-ch02-85
I=I_1+I_2=I_{01}\sin\Delta\theta_1+I_{02}\sin\Delta\theta_2
```

where $I_{01}$ and $I_{02}$ are the current amplitudes through the individual junctions, while $\Delta\theta_1$ and $\Delta\theta_2$ are the phase differences across each of the junctions.

Clearly, the total current $I$ that can be passed through the two junctions depends on $\Delta\theta_1-\Delta\theta_2$. When $\Delta\theta_1=\Delta\theta_2$, the currents in the individual arms add, but when $\Delta\theta_1-\Delta\theta_2=\pi$, they cancel. In a quantum interference device a magnetic field is used to vary the flux through the current loop, as shown in Fig. 2.7, so that the phase difference $\Delta\theta_1-\Delta\theta_2$ can be varied by any desired amount of flux $\Phi$ enclosed within the circuit. This magnetic flux can be found by taking the line integral of the supercurrent equation (Eq. 2.18) and imposing the requirement that the wavefunction be single valued after completing a $2\pi$ excursion around the circuit.

More explicitly, from the single valuedness requirement, we have

```{math}
:label: eq-p4-ch02-86
\oint_c\vec{\nabla}\theta\cdot d\vec{l}=2\pi n.
```

Then using the relation Eq. 2.18 we obtain an expression for the gradient of the phase of the superconducting wave function in a magnetic field

```{math}
:label: eq-p4-ch02-87
\vec{\nabla}\theta=\left(\frac{m^*}{\hbar}\right)\vec{v}_s+\left(\frac{q^*}{ch}\right)\vec{A}
```

in the bulk superconductors connecting the junctions. Then applying Eq. 2.87 to 2.86 and noting the direction of current flow we obtain

```{math}
:label: eq-p4-ch02-88
\left(\Delta\theta_1-\Delta\sigma_2\right)+\frac{q^*}{hc}\oint\vec{A}\cdot d\vec{l'}=2\pi n
```

where we have taken the contour $c$ in Eq. 2.86 deep enough in the superconductor so that $\vec{v}_s=0$ along $c$ (except of course in the junctions themselves). We thus obtain

```{math}
:label: eq-p4-ch02-89
\Delta\theta_1-\Delta\theta_2+2\pi\frac{\Phi}{\Phi_0}=2\pi n
```

where we have expressed the magnetic flux within the current loop in units of the flux quantum $\Phi_0=ch/2e$.

Equation 2.89 shows that the phase difference $\Delta\theta_1-\Delta\theta_2$ between the two junctions is solely determined by the flux enclosed within the circuit. The flux depends on both the applied field present and upon any fields produced by the currents circulating in the circuit itself. Since the maximum possible circulating current around the circuit is $I_0$, the flux produced by $I$ will be negligible (i.e., there will be no self-shielding) if $I_0L \ll \Phi_0$, where $L$ is the loop inductance. In this case we can neglect the result $\Phi=\Phi_a$, where $\Phi_a$ is the applied flux.

Suppose that the two Josephson junctions in Fig. 2.7 are identical and have a phase difference $\Delta\theta=\Delta\theta_1=\Delta\theta_2$ in zero magnetic field. In a magnetic field the phase difference across each Josephson junction then becomes $\Delta\theta_1+\pi\frac{\Phi_b}{\Phi_0}$ and $\Delta\theta_2-\pi\frac{\Phi_b}{\Phi_0}$. Then using Eq. 2.80 for the Josephson current and assuming the two junctions in Fig. 2.7 to be identical, we obtain

```{math}
:label: eq-p4-ch02-90
I=I_{01}\sin\left(\Delta\theta+\frac{\pi\Phi}{\Phi_0}\right)+I_{02}\sin\left(\Delta\theta-\frac{\pi\Phi}{\Phi_0}\right)\\=I_0\left[(\sin\Delta\theta\cos\pi\Phi/\Phi_0+\sin\pi\Phi/\Phi_0\cos\Delta\theta)+(\sin\Delta\theta\cos\pi\Phi/\Phi_0-\sin\pi\Phi/\Phi_0\cos\Delta\theta)\right]\\=2I_0\sin\Delta\theta\cos\pi\Phi/\Phi_0
```

where $I_0=I_{01}=I_{02}$ and $\Delta\theta=\Delta\theta_1=\Delta\theta_2$. Equation 2.90 shows that the parallel combination of junctions in a magnetic field acts very much like a single junction in zero field that is now modulated by the magnetic flux passing through the current loop. Thus Eq. 2.90 has a periodicity shown in Fig. 2.8 with maxima occurring whenever

```{math}
:label: eq-p4-ch02-91
\frac{e\Phi}{\hbar c}=s\pi
```

where $s$ is an integer. The resulting interference pattern is shown in Fig. 2.8. The short period variation is produced by the interference condition between the two junctions as predicted by Eq. 2.91, and the longer period variation is a diffraction effect arising from the finite dimensions of each junction.

:::{figure} images/fig-p4-ch02-8.png
:name: fig-p4-ch02-8
:width: 95%
:align: center
Figure 2.8: Josephson interference from two parallel junctions such as in Fig. 2.7. Josephson interference is mathematically identical to a two-slit interferogram.
:::

The interference pattern in Fig. 2.8 is formally analogous to a two-slit interference pattern in physical optics. In the case of the SQUID device the "phase difference" is determined by the flux enclosed in the ring. Since a very small amount of flux can be detected in this way (a small fraction of the unit of quantum flux $\Phi_0=2.07\times 10^{-7}$gauss cm$^2$), SQUID's can be used as very sensitive magnetometers. Large arrays of Josephson junctions have also been used to model 2D phase transitions in magnetic systems, and SQUID magnetometers have become the standard equipment for magnetic susceptibility measurements.
