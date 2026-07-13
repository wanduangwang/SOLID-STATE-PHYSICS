---
title: "B Harmonic Oscillators, Phonons, and the Electron-Phonon Interaction"
abstract: >
  A review of the quantum harmonic oscillator in terms of raising and lowering operators,
  the quantization of lattice vibrations into phonons and their dispersion relations in one
  and three dimensions, and the derivation of the electron-phonon interaction Hamiltonian
  from the electron-ion potential expanded to first order in the ionic displacements.
---

# B Harmonic Oscillators, Phonons, and the Electron-Phonon Interaction

## B.1 Harmonic Oscillators

In this section we review the solution of the harmonic oscillator problem in quantum mechanics
using raising and lowering operators. The Hamiltonian for this problem is written as:

```{math}
:label: eq-p2-appB-1
H = \frac{p^2}{2m} + \frac{1}{2}\kappa x^2.
```

Classically, we know that the frequency of oscillation is given by $\omega = \sqrt{\kappa/m}$ so that

```{math}
:label: eq-p2-appB-2
H = \frac{p^2}{2m} + \frac{1}{2} m\omega^2 x^2.
```

We define the lowering and raising operators $a$ and $a^\dagger$, respectively, by

```{math}
:label: eq-p2-appB-3
a = \frac{p - i\omega m x}{\sqrt{2\hbar\omega m}}
```

and

```{math}
:label: eq-p2-appB-4
a^\dagger = \frac{p + i\omega m x}{\sqrt{2\hbar\omega m}}.
```

Since $[p, x] = \hbar/i$, then it follows that

```{math}
:label: eq-p2-appB-5
[a, a^\dagger] = 1
```

so that

```{math}
:label: eq-p2-appB-6
H = \frac{1}{2m}(p + i\omega m x)(p - i\omega m x) + m\hbar\omega
```

```{math}
:label: eq-p2-appB-7
= \hbar\omega[a^\dagger a + 1/2].
```

Let

```{math}
:label: eq-p2-appB-8
N = a^\dagger a
```

denote the number operator and we denote its eigenstates by $|n\rangle$, so that

```{math}
:label: eq-p2-appB-9
N|n\rangle = n|n\rangle
```

where $n$ is any real integer. However

```{math}
:label: eq-p2-appB-10
\langle n|N|n\rangle = \langle n|a^\dagger a|n\rangle = \langle y|y\rangle = n \ge 0
```

where $|y\rangle = a|n\rangle$ implies that $n$ is a non-negative integer. We note with regard to
{eq}`eq-p2-appB-10` that the absolute value square of any wavefunction cannot be negative,
because quantum mechanically, this quantity signifies a probability. Hence $n$ is positive number
or zero. The action of the lowering operator is found from consideration of

```{math}
:label: eq-p2-appB-11
N a|n\rangle = a^\dagger a a|n\rangle = (a a^\dagger - 1) a|n\rangle = (n - 1) a|n\rangle.
```

Hence we find that

```{math}
:label: eq-p2-appB-12
a|n\rangle = c|n - 1\rangle.
```

However from {eq}`eq-p2-appB-10`, we have

```{math}
:label: eq-p2-appB-13
\langle n|a^\dagger a|n\rangle = |c|^2,
```

and also from {eq}`eq-p2-appB-10` we have

```{math}
:label: eq-p2-appB-14
\langle n|a^\dagger a|n\rangle = n,
```

so that

```{math}
:label: eq-p2-appB-15
c = \sqrt{n}
```

and

```{math}
:label: eq-p2-appB-16
a|n\rangle = \sqrt{n}|n - 1\rangle.
```

Since the operator $a$ lowers the quantum number of the state, $a$ is called the annihilation or
lowering operator. From this argument you can also see that $n$ has to be an integer. The null
state is obtained for $n = 0$.

To obtain the raising operator consider,

```{math}
:label: eq-p2-appB-17
N a^\dagger|n\rangle = a^\dagger a a^\dagger|n\rangle = a^\dagger(1 + a^\dagger a)|n\rangle = (n + 1) a^\dagger|n\rangle.
```

Hence we obtain

```{math}
:label: eq-p2-appB-18
a^\dagger|n\rangle = \sqrt{n + 1}|n + 1\rangle
```

so that $a^\dagger$ is called a creation operator or a raising operator. Finally, for the
Hamiltonian in {eq}`eq-p2-appB-7` we write

```{math}
:label: eq-p2-appB-19
H|n\rangle = \hbar\omega[N + 1/2]|n\rangle = \hbar\omega(n + 1/2)|n\rangle
```

so that the eigenvalues for the harmonic oscillator are written as:

```{math}
:label: eq-p2-appB-20
E = \hbar\omega(n + 1/2), \qquad n = 0, 1, 2, \dots.
```

## B.2 Phonons

In this section we relate the lattice vibrations to harmonic oscillators and identify the quanta
of the lattice vibrations with phonons. Consider the 1-D model with springs shown in
{numref}`fig-p2-appB-1`. The Hamiltonian for this case is written as

```{math}
:label: eq-p2-appB-21
H = \sum_{s=1}^{N} \left( \frac{p_s^2}{2 m_s} + \frac{1}{2}\kappa (q_{s+1} - q_s)^2 \right).
```

This equation doesn't look like a set of independent harmonic oscillators since $q_s$ and
$q_{s+1}$ are coupled. To obtain normal mode solutions we write

```{math}
:label: eq-p2-appB-22
q_s = \sqrt{\frac{1}{N}} \sum_k Q_k e^{i k s a}, \qquad
p_s = \sqrt{\frac{1}{N}} \sum_k P_k e^{i k s a}.
```

These $Q_k$'s and $P_k$'s are called phonon coordinates. It can be verified that

```{math}
:label: eq-p2-appB-23
[p_s, q_{s'}] = (\hbar/i)\,\delta_{ss'}
```

implies that

```{math}
:label: eq-p2-appB-24
[P_k, Q_{k'}] = (\hbar/i)\,\delta_{kk'}.
```

The Hamiltonian for 1D lattice vibrations in phonon coordinates is

```{math}
:label: eq-p2-appB-25
H = \sum_k \left( \frac{1}{2} P_k^\dagger P_k + \frac{1}{2}\omega_k^2 Q_k^\dagger Q_k \right)
```

and gives rise to the 1-D phonon dispersion relation (see {numref}`fig-p2-appB-2`)

```{math}
:label: eq-p2-appB-26
\omega_k \equiv \sqrt{2\kappa(1 - \cos ka)}
= \left(\frac{4\kappa}{m}\right)^{1/2} |\sin(ka/2)|.
```

This is all in Kittel ISSP, see pp 611-615 (Sixth edition). Again let

```{math}
:label: eq-p2-appB-27
a_k = \frac{i P_k^\dagger + \omega_k Q_k}{\sqrt{2\hbar\omega_k}},
```

```{math}
:label: eq-p2-appB-28
a_k^\dagger = \frac{-i P_k + \omega_k Q_k^\dagger}{\sqrt{2\hbar\omega_k}}.
```

represent the annihilation and creation operators. The Hamiltonian written in terms of the
creation and annihilation operators becomes

```{math}
:label: eq-p2-appB-29
H = \sum_k \hbar\omega_k (a_k^\dagger a_k + 1/2)
```

yielding energy eigenvalues

```{math}
:label: eq-p2-appB-30
E = \sum_k (n_k + 1/2)\hbar\omega_k.
```

The quantum excitation in this case is called a phonon, and the state vector of a system of
phonons is written as $|n_1, n_2, \dots, n_k, \dots\rangle$. To annihilate or create a phonon in
mode $k$ we then write

```{math}
:label: eq-p2-appB-31
a_k |n_1, n_2, \dots, n_k, \dots\rangle = \sqrt{n_k} |n_1, n_2, \dots, n_k - 1, \dots\rangle
```

```{math}
:label: eq-p2-appB-32
a_k^\dagger |n_1, n_2, \dots, n_k, \dots\rangle = \sqrt{n_k + 1} |n_1, n_2, \dots, n_k + 1, \dots\rangle
```

from which the probabilities $n_k$ and $(n_k + 1)$ are obtained for the annihilation and creation
processes.

:::{figure} images/fig-p2-appB-1.png
:name: fig-p2-appB-1
:width: 50%
:align: center

Figure B.1: 1D spring model.
:::

:::{figure} images/fig-p2-appB-2.png
:name: fig-p2-appB-2
:width: 70%
:align: center

Figure B.2: Phonon dispersion relation.
:::

## B.3 Phonons in 3D Crystals

We give some examples of the phonon in 3D crystals. The first example is the zone center atomic
displacements in graphite shown in {numref}`fig-p2-appB-3`. Graphite has 4 carbon atoms per unit
cell, thus 12 zone center modes. There are 3 acoustic modes and 9 optic modes.

The next example is the phonon dispersion curves for diamond shown in {numref}`fig-p2-appB-4`.
Diamond has 2 carbon atoms per fcc unit cell, thus 6 branches. The zone center optic modes are
Raman active. There are 3 acoustic branches and 3 are optic modes.

The next example is the phonon dispersion curves for silicon shown in {numref}`fig-p2-appB-5`.
Silicon like diamond has 2 atoms per fcc unit cell, thus 6 branches. The zone center optic modes
are Raman active. There are 3 acoustic branches and 3 are optic modes.

:::{figure} images/fig-p2-appB-3.png
:name: fig-p2-appB-3
:width: 70%
:align: center

Figure B.3: Zone center optical phonon modes in graphite.
:::

:::{figure} images/fig-p2-appB-4.png
:name: fig-p2-appB-4
:width: 70%
:align: center

Figure B.4: Phonon dispersion curves in diamond.
:::

:::{figure} images/fig-p2-appB-5.png
:name: fig-p2-appB-5
:width: 70%
:align: center

Figure B.5: Phonon dispersion curves in silicon.
:::

The next example is the phonon dispersion curves for GaAs shown in {numref}`fig-p2-appB-6`. GaAs
like diamond has 2 atoms per fcc unit cell, thus 6 branches. However the two atoms are different
and GaAs lacks inversion symmetry. The zone center optic modes are both infrared and Raman
active. There are 3 acoustic branches and 3 are optic modes.

:::{figure} images/fig-p2-appB-6.png
:name: fig-p2-appB-6
:width: 70%
:align: center

Figure B.6: Phonon dispersion curves in silicon (GaAs).
:::

## B.4 Electron-Phonon Interaction

The basic Hamiltonian for the electron-lattice system is

```{math}
:label: eq-p2-appB-33
H = \sum_k \frac{p_k^2}{2m} + \frac{1}{2}\sum_{kk'} \frac{e^2}{|\vec{r}_k - \vec{r}_{k'}|}
+ \sum_i \frac{P_i^2}{2M} + \frac{1}{2}\sum_{ii'} V_{\text{ion}}(\vec{R}_i - \vec{R}_{i'})
+ \sum_{k,i} V_{\text{el-ion}}(\vec{r}_k - \vec{R}_i)
```

where

```{math}
:label: eq-p2-appB-34
H = H_{\text{electron}} + H_{\text{ion}} + H_{\text{electron-ion}}.
```

The electron-ion interaction term can be separated into two parts: the interaction of electrons
with ions in their equilibrium positions, and an additional term due to lattice vibrations:

```{math}
:label: eq-p2-appB-35
H_{\text{el-ion}} = H_{0,\text{el-ion}} + H_{\text{el-phonon}}
```

```{math}
:label: eq-p2-appB-36
\sum_{k,i} V_{\text{el-ion}}(\vec{r}_k - \vec{R}_i)
= \sum_{k,i} V_{\text{el-ion}}(\vec{r}_k - (\vec{R}_i^0 + \vec{s}_i))
```

```{math}
:label: eq-p2-appB-37
= \sum_{k,i} V_{\text{el-ion}}(\vec{r}_k - \vec{R}_i^0)
- \sum_{k,i} \vec{s}_i \cdot \nabla V_{\text{el-ion}}(\vec{r}_k - \vec{R}_i^0)
```

```{math}
:label: eq-p2-appB-38
= H_{0,\text{el-ion}} + H_{\text{el-phonon}}.
```

In solving the Hamiltonian $H$ of {eq}`eq-p2-appB-33` we seek a solution of the total problem in
the form

```{math}
:label: eq-p2-appB-39
\Psi = \psi(\vec{r}_1, \vec{r}_2, \dots, \vec{R}_1, \vec{R}_2, \dots)\,\phi(\vec{R}_1, \vec{R}_2, \dots)
```

such that

```{math}
:label: eq-p2-appB-40
H\Psi = E\Psi.
```

We then use an adiabatic approximation, which solves the electron part of the Hamiltonian by

```{math}
:label: eq-p2-appB-41
(H_{\text{electron}} + H_{0,\text{el-ion}})\psi = E_{\text{el}}\psi.
```

Neglecting the $H_{\text{el-phonon}}$ term, which we consider as a perturbation, we write:

```{math}
:label: eq-p2-appB-42
H_{\text{ion}}\phi = (E - E_{\text{el}})\phi = E_{\text{ion}}\phi
```

and we have thus decoupled the electron-lattice system.

Equation {eq}`eq-p2-appB-42` gives us the phonon spectra and harmonic oscillator like wave
functions, as discussed in the previous section (§B.2). The term that was left out in the above
discussion is the electron-phonon interaction

```{math}
:label: eq-p2-appB-43
H_{\text{el-phonon}} = - \sum_{k,i} \vec{s}_i \cdot \nabla V_{\text{el-ion}}(\vec{r}_k - \vec{R}_i^0)
```

which we now treat as a perturbation. We rewrite {eq}`eq-p2-appB-42` by introducing the normal
coordinates

```{math}
:label: eq-p2-appB-44
\vec{s}_i = \frac{1}{\sqrt{NM}} \sum_{\vec{q},j} Q_{\vec{q},j} e^{i\vec{q}\cdot\vec{R}_i^0} \hat{e}_j
```

where $j$ is polarization index and $\hat{e}_j$ is a unit displacement vector for mode $j$. Hence
we obtain

```{math}
:label: eq-p2-appB-45
H_{\text{el-phonon}} = - \sum_{k,i} \frac{1}{\sqrt{NM}} \sum_{\vec{q},j}
Q_{\vec{q},j} e^{i\vec{q}\cdot\vec{R}_i^0} \hat{e}_j \cdot \nabla V_{\text{el-ion}}(\vec{r}_k - \vec{R}_i^0)
```

where

```{math}
:label: eq-p2-appB-46
Q_{\vec{q},j} = \left( \frac{\hbar}{2\omega_{\vec{q},j}} \right)^{1/2}
(a_{\vec{q},j} + a_{-\vec{q},j}^\dagger).
```

Writing the time dependence explicitly for the raising and lowering operators

```{math}
:label: eq-p2-appB-47
a_{\vec{q},j}(t) = a_{\vec{q},j} e^{-i\omega_{\vec{q},j} t}
```

```{math}
:label: eq-p2-appB-48
a_{\vec{q},j}^\dagger(t) = a_{\vec{q},j}^\dagger e^{i\omega_{\vec{q},j} t}
```

we obtain

```{math}
:label: eq-p2-appB-49
H_{\text{el-phonon}} = - \sum_{\vec{q},j} \left( \frac{\hbar}{2 M N \omega_{\vec{q},j}} \right)^{1/2}
(a_{\vec{q},j} e^{-i\omega_{\vec{q},j} t} + a_{\vec{q},j}^\dagger e^{i\omega_{\vec{q},j} t})
\times \sum_{k,i} (e^{i\vec{q}\cdot\vec{R}_i^0} + e^{i\vec{q}\cdot\vec{R}_i^0})
\hat{e}_j \cdot \nabla V_{\text{el-ion}}(\vec{r}_k - \vec{R}_i^0)
```

which can be written as

```{math}
:label: eq-p2-appB-50
H_{\text{el-phonon}} = - \sum_{\vec{q},j} \left( \frac{\hbar}{2 N M \omega_{\vec{q},j}} \right)^{1/2}
\left[ a_{\vec{q},j} \sum_{k,i} e^{i(\vec{q}\cdot\vec{R}_i^0 - \omega_{\vec{q},j} t)}
\hat{e}_j \cdot \nabla(\vec{r}_k - \vec{R}_i^0) + \text{c.c.} \right].
```

If we are only interested in the interaction of one electron and a phonon on a particular branch,
say the longitudinal acoustic branch, then we drop the summation over $j$ and $k$ and write

```{math}
:label: eq-p2-appB-51
H_{\text{el-phonon}} = - \sum_{\vec{q}} \left( \frac{\hbar}{2 N M \omega_{\vec{q}}} \right)^{1/2}
\left[ a_{\vec{q}} \sum_i e^{i(\vec{q}\cdot\vec{R}_i^0 - \omega_{\vec{q}} t)}
\hat{e}\cdot\vec{\nabla} V_{\text{el-ion}}(\vec{r} - \vec{R}_i^0) + \text{c.c.} \right]
```

where the 1st term in the bracket corresponds to phonon absorption and the c.c. term corresponds
to phonon emission.

With $H_{\text{el-phonon}}$ in hand, we can solve transport problems (e.g., $\tau$ due to phonon
scattering) and optical problems (e.g., indirect transitions) directly, since all these problems
involve matrix elements $\langle f|H_{\text{el-phonon}}|i\rangle$ coupling initial and final
states $i$ and $f$, respectively.
