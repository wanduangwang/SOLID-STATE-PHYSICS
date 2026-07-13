---
title: "Appendix C — Harmonic Oscillators, Phonons, and Electron-Phonon Interaction"
abstract: "A review of quantum harmonic oscillators via raising and lowering operators, the mapping from lattice vibrations to phonons (normal modes, quantization, creation/annihilation operators), and the derivation of the electron-phonon interaction Hamiltonian in second-quantized form."
---

# Appendix C — Harmonic Oscillators, Phonons, and Electron-Phonon Interaction

## C.1 Harmonic Oscillators

In this section we review the solution of the harmonic oscillator problem in quantum mechanics using raising and lowering operators. This is aimed at providing a quick review as background for the lecture on phonon scattering processes and other topics in this course.

The Hamiltonian for the harmonic oscillator in one-dimension is written as:

```{math}
:label: eq-apptransport-C-1
\mathcal{H} = \frac{p^2}{2m} + \frac{1}{2}\kappa x^2.
```

We know classically that the frequency of oscillation is given by $\omega = \sqrt{\kappa/m}$ so that

```{math}
:label: eq-apptransport-C-2
\mathcal{H} = \frac{p^2}{2m} + \frac{1}{2}m\omega^2 x^2
```

Define the lowering and raising operators $a$ and $a^\dagger$ respectively by

```{math}
:label: eq-apptransport-C-3
a = \frac{p - im\omega x}{\sqrt{2\hbar m\omega}}
```

```{math}
:label: eq-apptransport-C-4
a^\dagger = \frac{p + im\omega x}{\sqrt{2\hbar m\omega}}
```

Since $[p,x] = \hbar/i$, then $[a,a^\dagger] = 1$ so that

```{math}
:label: eq-apptransport-C-5
\begin{aligned}
\mathcal{H}
&= \frac{1}{2m}\Bigl[(p + i\omega mx)(p - i\omega mx) + m\hbar\omega\Bigr] \\
&= \hbar\omega(a^\dagger a + 1/2).
\end{aligned}
```

Let $N = a^\dagger a$ denote the number operator and its eigenstates $|n\rangle$ so that $N|n\rangle = n|n\rangle$ where $n$ is any real number. However

```{math}
:label: eq-apptransport-C-7
\langle n | N | n \rangle = \langle n | a^\dagger a | n \rangle = \langle y | y \rangle = n \ge 0
```

where $|y\rangle = a|n\rangle$ and the absolute value square of the eigenvector cannot be negative. Hence $n$ is a positive number or zero.

$$Na|n\rangle = a^\dagger aa|n\rangle = (aa^\dagger - 1)a|n\rangle = (n - 1)a|n\rangle \tag{C.8}$$

Hence $a|n\rangle = c|n - 1\rangle$ and $(n|a^\dagger a|n\rangle = |c|^2$. However from Eq. {eq}`eq-apptransport-C-7` $(n|a^\dagger a|n\rangle = n$ so that $c = \sqrt{n}$ and $|n-1\rangle = (1/\sqrt{n})a|n\rangle$. Since the operator $a$ lowers the quantum number of the state by unity, $a$ is called the annihilation operator. Therefore $n$ also has to be an integer, so that the null state is eventually reached by applying operator $a$ for a sufficient number of times.

$$Na^\dagger|n\rangle = a^\dagger aa^\dagger|n\rangle = a^\dagger(1 + a^\dagger a)|n\rangle = (n+1)a^\dagger|n\rangle \tag{C.9}$$

Hence $a^\dagger|n\rangle = \sqrt{n+1}|n+1\rangle$ so that $a^\dagger$ is called a raising operator or a creation operator. Finally,

```{math}
:label: eq-apptransport-C-10
\mathcal{H}|n\rangle = \hbar\omega[N + 1/2]|n\rangle = \hbar\omega(n + 1/2)|n\rangle
```

so the eigenvalues become

```{math}
:label: eq-apptransport-C-11
E = \hbar\omega(n + 1/2), \qquad n = 0,1,2,\ldots
```

:::{figure} images/fig-apptransport-C-1.png
:name: fig-apptransport-C-1
:width: 40%
:align: center
Figure C.1: Simple harmonic oscillator with single spring.
:::

## C.2 Phonons

In this section we relate the lattice vibrations to harmonic oscillators and identify the quanta of the lattice vibrations with phonons. Consider the 1-D model of atoms connected by springs (see Fig. {numref}`fig-apptransport-C-1`). The Hamiltonian for this case is written as:

```{math}
:label: eq-apptransport-C-12
\mathcal{H} = \sum_{s=1}^{N} \left( \frac{p_s^2}{2m} + \frac{1}{2}\kappa(x_{s+1}-x_s)^2 \right)
```

This equation doesn't look like a set of independent harmonic oscillators since $x_s$ and $x_{s+1}$ are coupled. Let

```{math}
:label: eq-apptransport-C-13
x_s = 1/\sqrt{N} \sum_k Q_k e^{iksa}
```

$$p_s = 1/\sqrt{N} \sum_k P_k e^{iksa}. \tag{C.13'}$$

These $Q_k$, $P_k$'s are called phonon coordinates. It can be verified that the commutation relation for momentum and coordinate implies a commutation relation between $P_k$ and $Q_{k'}$

```{math}
:label: eq-apptransport-C-14
[p_s, x_{s'}] = \frac{\hbar}{i}\delta_{ss'} \Longrightarrow [P_k, Q_{k'}] = \frac{\hbar}{i}\delta_{kk'}.
```

:::{figure} images/fig-apptransport-C-2.png
:name: fig-apptransport-C-2
:width: 90%
:align: center
Figure C.2: Schematic for a one dimensional phonon model and the corresponding dispersion relation.
:::

The Hamiltonian in phonon coordinates is:

```{math}
:label: eq-apptransport-C-15
\mathcal{H} = \sum_k \left( \frac{1}{2m} P'_k P_k + \frac{1}{2} m \omega_k^2 Q_k Q_k \right)
```

with the dispersion relation given by

```{math}
:label: eq-apptransport-C-16
\omega_k = \sqrt{2\kappa}(1-\cos ka)
```

This is all in Kittel ISSP, pp. 611–613. (see Fig. {numref}`fig-apptransport-C-2`) Again let

```{math}
:label: eq-apptransport-C-17
a_k = \frac{iP'_k + m\omega_k Q_k}{\sqrt{2\hbar m\omega_k}}
```

```{math}
:label: eq-apptransport-C-18
a^\dagger_k = \frac{-iP_k + m\omega_k Q'_k}{\sqrt{2\hbar m\omega_k}}
```

so that the Hamiltonian is written as:

```{math}
:label: eq-apptransport-C-19
\mathcal{H} = \sum_k \hbar\omega_k (a^\dagger_k a_k + 1/2) \Leftrightarrow E = \sum_k (n_k + 1/2)\hbar\omega_k
```

The quantum of energy $\hbar\omega_k$ is called a **phonon**. The state vector of a system of phonons is written as $|n_1,n_2,\ldots,n_k,\ldots\rangle$, upon which the raising and lowering operator can act:

```{math}
:label: eq-apptransport-C-20
a_k |n_1, n_2, \ldots, n_k, \ldots \rangle = \sqrt{n_k} |n_1, n_2, \ldots, n_k-1, \ldots\rangle
```

```{math}
:label: eq-apptransport-C-21
a^\dagger_k |n_1, n_2, \ldots, n_k, \ldots \rangle = \sqrt{n_k+1} |n_1, n_2, \ldots, n_k+1, \ldots\rangle
```

From Eq. {eq}`eq-apptransport-C-21` it follows that the probability of annihilating a phonon of mode $k$ is the absolute value squared of the diagonal matrix element or $n_k$.

## C.3 Electron-Phonon Interaction

The basic Hamiltonian for the electron-lattice system is

```{math}
:label: eq-apptransport-C-22
\mathcal{H} = \sum_k \frac{p_k^2}{2m} + \frac{1}{2}\sum_{k'} \frac{e^2}{|\vec{r}_k - \vec{r}_{k'}|}
+ \sum_i \frac{P_i^2}{2M} + \frac{1}{2}\sum_{i'} V_{\rm ion}(\vec{R}_i - \vec{R}_{i'})
+ \sum_{k,i} V_{\rm el-ion}(\vec{r}_k - \vec{R}_i)
```

where the first two terms constitute $\mathcal{H}_{\rm electron}$, the third and fourth terms are denoted by $\mathcal{H}_{\rm ion}$ and the last term is $\mathcal{H}_{\rm electron-ion}$. The electron-ion interaction term can be separated into two parts: the interaction of electrons with ions in their equilibrium positions, and an additional term due to lattice vibrations:

```{math}
:label: eq-apptransport-C-23
\mathcal{H}_{\rm el-ion} = \mathcal{H}_{\rm el-ion}^0 + \mathcal{H}_{\rm el-ph}
```

$$\sum_{k,i} V_{\rm el-ion}(\vec{r}_k - \vec{R}_i) = \sum_{k,i} V_{\rm el-ion}[\vec{r}_k - (\vec{R}_i^0 + \vec{s}_i)] \tag{C.24}$$

where $\vec{R}_i^0$ is the equilibrium lattice site position and $\vec{s}_i$ is the displacement of the atoms from their equilibrium positions in a lattice vibration so that

```{math}
:label: eq-apptransport-C-25
\mathcal{H}_{\rm el-ion}^0 = \sum_{k,i} V_{\rm el-ion}(\vec{r}_k - \vec{R}_i^0)
```

and

```{math}
:label: eq-apptransport-C-26
\mathcal{H}_{\rm el-ph} = - \sum_{k,i} \vec{s}_i \cdot \vec{\nabla} V_{\rm el-ion}(\vec{r}_k - \vec{R}_i^0).
```

In solving the Hamiltonian we use an adiabatic approximation, which solves the electronic part of the Hamiltonian by

```{math}
:label: eq-apptransport-C-27
(\mathcal{H}_{\rm electron} + \mathcal{H}_{\rm el-ion}^0)|\psi\rangle = E_{\rm el}|\psi\rangle
```

and seeks a solution of the total problem as

```{math}
:label: eq-apptransport-C-28
\Psi = \psi(\vec{r}_1, \vec{r}_2, \cdots \vec{R}_1, \vec{R}_2, \cdots)
\varphi(\vec{R}_1, \vec{R}_2, \cdots)
```

such that $\mathcal{H}\Psi = E\Psi$. Here $\Psi$ is the wave function for the electron-lattice system. Plugging this into the Eq. {eq}`eq-apptransport-C-22`, we find

```{math}
:label: eq-apptransport-C-29
E\Psi = \mathcal{H}\Psi = \psi(\mathcal{H}_{\rm ion} + E_{\rm el})\varphi
- \sum_i \frac{\hbar^2}{2M_i}\bigl(
\varphi\nabla_i^2\psi + 2\vec{\nabla}_i\varphi \cdot \vec{\nabla}_i\psi\bigr)
```

Neglecting the last term, which is small, we have

```{math}
:label: eq-apptransport-C-30
\mathcal{H}_{\rm ion}\varphi = (E - E_{\rm el})\varphi
```

Hence we have decoupled the electron-lattice system.

```{math}
:label: eq-apptransport-C-31
(\mathcal{H}_{\rm electron} + \mathcal{H}_{\rm el-ion}^0)|\psi\rangle = E_{\rm el}|\psi\rangle
```

which gives us the energy band structure and $\psi$ satisfies Bloch's theorem while $\varphi$ is the wave function for the ions

```{math}
:label: eq-apptransport-C-32
\mathcal{H}_{\rm ion}\varphi = E_{\rm ion}\varphi
```

which gives us phonon spectra and harmonic oscillator like wave functions, as we have already seen in Sec. C.2.

The discussion has thus far left out the electron-phonon interaction $\mathcal{H}_{\rm el-ph}$

```{math}
:label: eq-apptransport-C-33
\mathcal{H}_{\rm el-ph} = -\sum_{k,i} \vec{s}_i \cdot \vec{\nabla}V_{\rm el-ion}(\vec{r}_k - \vec{R}_i^0)
```

which is then treated as a perturbation. Since the displacement vector can be written in terms of the normal coordinates $Q_{j\tilde{j}}$

```{math}
:label: eq-apptransport-C-34
\vec{s}_i = \frac{1}{\sqrt{NM}} \sum_j \sum_{\tilde{j}} Q_{j\tilde{j}} e^{i\vec{j}\cdot\vec{R}_i^0} \hat{e}_j
```

where $j$ denotes the polarization index, $N$ is the total number of ions and $M$ is the ion mass. Hence

```{math}
:label: eq-apptransport-C-35
\mathcal{H}_{\rm el-ph} = -\sum_{k,i} \frac{1}{\sqrt{NM}} \sum_j \sum_{\tilde{j}}
Q_{j\tilde{j}} e^{i\vec{j}\cdot\vec{R}_i^0} \hat{e}_j
\cdot \vec{\nabla}V_{\rm el-ion}(\vec{r}_k - \vec{R}_i^0)
```

where the normal coordinate can be expressed in terms of the lowering and raising operators

```{math}
:label: eq-apptransport-C-36
Q_{j\tilde{j}} = \left(\frac{\hbar}{2M\omega_{j\tilde{j}}}\right)^{\!1/2}
\!(a_{j\tilde{j}} + a^\dagger_{-j\tilde{j}}).
```

Writing out the time dependence explicitly,

```{math}
:label: eq-apptransport-C-37
a_{j\tilde{j}}(t) = a_{j\tilde{j}} e^{-i\omega_{j\tilde{j}}t}
```

```{math}
:label: eq-apptransport-C-38
a^\dagger_{j\tilde{j}}(t) = a^\dagger_{j\tilde{j}} e^{i\omega_{j\tilde{j}}t}
```

we obtain

```{math}
:label: eq-apptransport-C-39
\begin{aligned}
\mathcal{H}_{\rm el-ph} &= -\sum_{j\tilde{j}} \left(\frac{\hbar}{2NM\omega_{j\tilde{j}}}\right)^{\!\!1/2}
\bigl( a_{j\tilde{j}} e^{-i\omega_{j\tilde{j}}t} + a^\dagger_{j\tilde{j}} e^{i\omega_{j\tilde{j}}t} \bigr) \\
&\quad \times \sum_{k,i} \bigl(e^{i\vec{j}\cdot\vec{R}_i^0} + e^{-i\vec{j}\cdot\vec{R}_i^0}\bigr)
\hat{e}_j \cdot \vec{\nabla}V_{\rm el-ion}(\vec{r}_k - \vec{R}_i^0)
\end{aligned}
```

```{math}
:label: eq-apptransport-C-40
\begin{aligned}
= {} & -\sum_{j\tilde{j}} \left(\frac{\hbar}{2NM\omega_{j\tilde{j}}}\right)^{\!\!1/2}
\Biggl( a_{j\tilde{j}} \sum_{k,i} e^{i[\vec{j}\cdot\vec{R}_i^0 - \omega_{j\tilde{j}}t]}
\cdot \hat{e}_j \vec{\nabla}V_{\rm el-ion}(\vec{r}_k - \vec{R}_i^0) \\
&\quad + \text{ c.c.})
\end{aligned}
```

If we are only interested in the interaction between one electron and a phonon on a particular branch, say the longitudinal acoustic (LA) branch, then we drop the summation over $j$ and $k$

```{math}
:label: eq-apptransport-C-41
\mathcal{H}_{\rm el-ph} = -\left(\frac{\hbar}{2NM\omega_q}\right)^{\!1/2}
\Bigl( a_{\vec{q}} \sum_i e^{i[\vec{q}(\vec{R}_i^0-\vec{q}t)]} \cdot
\vec{\nabla}V_{\rm el-ion}(\vec{r} - \vec{R}_i^0) + \text{c.c.} \Bigr)
```

where the first term in the bracket corresponds to the phonon absorption and the c.c. term corresponds to phonon emission.

With $\mathcal{H}_{\rm el-ph}$ at hand, we can solve transport problems (e.g., $\tau$, due to phonon scattering) and optical problems (e.g., indirect transitions) exactly since all of these problems involve the matrix element $\langle f|\mathcal{H}_{\rm el-ph}|i\rangle$ of $\mathcal{H}_{\rm el-ph}$ linking states $|i\rangle$ and $|f\rangle$.
