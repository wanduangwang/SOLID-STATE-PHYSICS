---
title: "2 Magnetic Effects in Free Atoms"
abstract: "Zeeman and hyperfine interactions in free atoms, addition of angular momenta, Hund's rules, and the use of Clebsch-Gordan coefficients."
---

# 2 Magnetic Effects in Free Atoms

## 2.1 The Zeeman Effect

Suppose we now impose a small magnetic field on our atomic system. The magnetic moment $\vec{\mu}$ will try to line up along the magnetic field $\vec{B}$ yielding an interaction Hamiltonian

```{math}
:label: eq-p3-ch02-1
\mathcal{H}'_Z = -\vec{\mu} \cdot \vec{B} .
```

We will see below that the effect of a magnetic field is to lift the $(2j+1)$ degeneracy of the angular momentum states and this effect is called the Zeeman effect. We denote the perturbation Hamiltonian in Eq. {eq}`eq-p3-ch02-1` associated with the Zeeman effect by $\mathcal{H}'_Z$.

To evaluate the matrix elements of Eq. {eq}`eq-p3-ch02-1`, we choose the $z$ direction along the magnetic field. Then evaluation of $\mathcal{H}'_Z$ in the $| \ell, s, j, m_j \rangle$ representation yields

```{math}
:label: eq-p3-ch02-2
\langle \ell, s, j, m_j | \mathcal{H}'_Z | \ell, s, j, m_j \rangle = -\mu_B g B \langle \ell, s, j, m_j | J_z | \ell, s, j, m_j \rangle
```

following the discussion of the vector model in §1.6. As an illustration, take $j = 5/2$, and from Eq. {eq}`eq-p3-ch02-2` we find that the magnetic field will split the zero field level into $(2j+1) = 6$ equally spaced levels, the level spacing being proportional to $(\mu_B g B)$ and thus proportional to the magnetic field. What we mean by a small magnetic field in Eq. {eq}`eq-p3-ch02-1` is that $\mathcal{H}'_Z = -\vec{\mu} \cdot \vec{B}$ has an expectation value that is small compared with the spin-orbit interaction, i.e., $\mathcal{H}'_Z \ll \mathcal{H}'_{so}$. In this limit the Zeeman problem must be solved in the $| \ell, s, j, m_j \rangle$ representation.

If, on the other hand, the expectation value of the $\mathcal{H}'_Z = -\vec{\mu} \cdot \vec{B}$ interaction is large compared with the spin-orbit interaction, then we solve the problem in the $| \ell, s, m_\ell, m_s \rangle$ representation and consider the spin-orbit interaction as a perturbation. In the $| \ell, s, m_\ell, m_s \rangle$ representation, $\vec{\mu} \cdot \vec{B}$ is readily evaluated from Eq. 1.126

```{math}
:label: eq-p3-ch02-3
\langle \ell, s, m_\ell, m_s | \mathcal{H}'_Z | \ell, s, m_\ell, m_s \rangle = -\mu_B B \langle \ell, s, m_\ell, m_s | L_z + 2S_z | \ell, s, m_\ell, m_s \rangle / \hbar = -\mu_B B (m_\ell + 2m_s) .
```

In this case there will be a degeneracy in some of the states in Eq. {eq}`eq-p3-ch02-3` and this degeneracy is lifted by the spin-orbit interaction, which now acts as a perturbation on the Zeeman effect. For intermediate field values where the Zeeman energy and the spin-orbit interaction are of comparable magnitudes, the problem is more difficult to solve (see Schiff, chapter 12).

## 2.2 The Hyperfine Interaction

Closely related to the spin-orbit interaction is the hyperfine interaction. This interaction, though too small to be important for many solid state applications, is of great importance in nuclear magnetic resonance and Mössbauer spectroscopy studies. The hyperfine interaction arises through the interaction of the magnetic moment of the nucleus with the magnetic field produced by the electrons. Just as we introduce the magnetic moment of the free electron as (see Eq. 1.84)

```{math}
:label: eq-p3-ch02-4
\vec{\mu}_{\text{spin}} = \frac{g_s e}{2mc} \vec{S},
```

where $g_s = 2$, we introduce the nuclear magnetic moment

```{math}
:label: eq-p3-ch02-5
\vec{\mu}_{\text{spin-nucleus}} = \frac{g_I \mu_N \vec{I}}{\hbar}
```

where the $g$-factor for the nucleus $g_I$ is constant for a particular nucleus and $\vec{I}$ is the angular momentum of the nucleus. Values of $g_I$ are tabulated in handbooks. For nuclei, $g_I$ can be of either sign. If $g_I$ is positive, then the magnetic moment and spin are lined up; otherwise they are antiparallel as for electrons. The nuclear magneton $\mu_N$ is defined as a positive number:

```{math}
:label: eq-p3-ch02-6
\mu_N = \frac{|e| \hbar}{2Mc} = \frac{m}{M} |\mu_B| = \frac{\mu_B}{1836} \sim 5 \times 10^{-24} \text{ ergs/gauss}
```

where $M$ is the mass of the proton, so that the hyperfine interaction between the nuclear orbital motion and the nuclear spin is much smaller than the spin-orbit interaction. The magnetic field produced by the electrons at the nuclear position is denoted by $\vec{B}_J$ and will be proportional to $\vec{J}$ or more specifically to

```{math}
:label: eq-p3-ch02-7
\left( \frac{\vec{B}_J \cdot \vec{J}}{J^2} \right) \vec{J} .
```

Thus, the hyperfine interaction $\mathcal{H}'_{hf}$ will be of the form $\mathcal{H}'_{hf} = -\vec{\mu}_{\text{spin-nucleus}} \cdot \vec{B}_J$ so that from Eqs. {eq}`eq-p3-ch02-5` and {eq}`eq-p3-ch02-7` we obtain

```{math}
:label: eq-p3-ch02-8
\mathcal{H}'_{hf} = -\text{constant} (\vec{I} \cdot \vec{J}) .
```

To the extent that the $\mathcal{H}'_{hf}$ interaction is significant in magnitude, neither $m_i$ nor $m_j$ are good quantum numbers, and we must therefore introduce a new total angular momentum $\vec{F}$ which is the sum of the nuclear and electronic angular momenta

```{math}
:label: eq-p3-ch02-9
\vec{F} = \vec{I} + \vec{J}
```

so that

```{math}
:label: eq-p3-ch02-10
\vec{F} \cdot \vec{F} = (\vec{I} + \vec{J}) \cdot (\vec{I} + \vec{J})
```

and in the representation $|i, j, f, m_f\rangle$ we can evaluate $\vec{I} \cdot \vec{J}$ to obtain

```{math}
:label: eq-p3-ch02-11
\vec{I} \cdot \vec{J} = \frac{1}{2} [f(f+1) - i(i+1) - j(j+1)] .
```

The presence of this hyperfine interaction lifts some of the $(2i+1)(2j+1)$ degeneracy of the $f$ states. For example let $j=1/2$, $i=1/2$, then $f = 0, 1$ and we have $\vec{I} \cdot \vec{J} = 1$ or $0$. Thus the hyperfine interaction splits the 4-fold degenerate level into a 3-fold $f=1$ triplet level and a non-degenerate $f=0$ singlet level as shown in Fig. {numref}`fig-p3-ch02-1`.

:::{figure} images/fig-p3-ch02-1.png
:name: fig-p3-ch02-1
:width: 60%
:align: center
Fig. 2.1: Schematic diagram of the splitting of the 4-fold $j=1/2$, $i=1/2$ level under the hyperfine interaction between the nuclear spin and the orbital magnetic field. The level ordering for the hyperfine interaction may be opposite to that for the spin-orbit interaction, since the nuclear $g$-factor can be either positive or negative.
:::

## 2.3 Addition of Angular Momenta

We have until now considered the addition of angular momentum in terms of $(\vec{L} + \vec{S})$ for a single electron and $(\vec{J} + \vec{I})$ for the case of the nuclear spin angular momentum. In this section we consider the addition of orbital angular momenta associated with more than one electron. For example, for two electrons $\vec{L}$ could be written as $\vec{L}_1 + \vec{L}_2$. The addition of the angular momentum $\vec{L}_i$ for each electron to obtain a total orbital angular momentum $\vec{L}$ occurs in most atomic systems where we have more than one electron. We will consider here the case of $L$-$S$ (Russell-Saunders) coupling which is the more important case for atomic systems and for solids.

According to the $L$-$S$ coupling scheme we combine the orbital angular momenta for all the electrons

```{math}
:label: eq-p3-ch02-12
\vec{L} = \sum_i \vec{L}_i
```

and all the spin angular momenta

```{math}
:label: eq-p3-ch02-13
\vec{S} = \sum_i \vec{S}_i
```

and then, from the total $\vec{L}$ and the total $\vec{S}$, we form a total $\vec{J} = \vec{L} + \vec{S}$. The representation that we use for finding the matrix elements for $J$ is $| \ell, s, j, m_j \rangle$ where the quantum numbers correspond to the total $\vec{L}$, total $\vec{S}$ and $\vec{J} = \vec{L} + \vec{S}$. Our discussion of the magnetic properties of solids most often uses this representation.

In the following subsection (§2.3.1), we will give some examples of multi-electron systems. First we will find the lowest energy state or the ground state for a many-electron system. To find the lowest energy state we use Hund's rule.

### 2.3.1 Hund's Rule

Hund's Rule is used to find the ground state $s$, $\ell$ and $j$ values for a multi-electron atom and provides a recipe to find the $s$, $\ell$, and $j$ values for the ground state. The rules are applied in the following sequence:

1. The ground state has the maximum multiplicity $(2s+1)$ allowed by the Pauli Principle, which determines $\vec{S}$.
2. The ground state has the maximum $\vec{L}$ consistent with the multiplicity in $\vec{S}$ given by Hund's Rule (1).
3. The total $\vec{J}$ value is $|\vec{L} - \vec{S}|$ if the shell is less than half full and $|\vec{L} + \vec{S}|$ if the shell is more than half full.

The physical origin of the first Hund's rule is that to minimize the Coulomb repulsion between two electrons it is advantageous to keep them apart, and by selecting the same spin state, the two electrons are required to have different orbital states by the exclusion principle. The spin-orbit interaction which gives rise to the lowering of the ground state is proportional to $\xi(\vec{r}) \vec{L} \cdot \vec{S}$ (see §1.5). Thus the lowest energy state is expected to occur when $L$ and $S$ have their maximum values in accordance with the Pauli principle. Finally, $\xi(\vec{r})$ tends to be positive for less than half filled shells and negative for more than half filled shells. Thus $\vec{J}$ in the ground state tends to be a minimum $J = |L - S|$ when the shell is less than half full and a maximum $J = |L + S|$ when the shell is more than half full.

The notation used to specify a state $(s, \ell, j)$ is shown in Fig. {numref}`fig-p3-ch02-2` for the state: $s = 1/2$, $\ell = 3$, and $j = 5/2$, where the multiplicity $(2s+1)$ is given as the left hand superscript, $\ell$ is given by a Roman capital letter and $j$ is given as the right hand subscript. The notation for the total $L$ value is historic and listed here:

| $L$ | Letter | Name |
|----:|:------:|:----:|
| 0 | S | (Sharp) |
| 1 | P | (Paschen) |
| 2 | D | (Diffuse) |
| 3 | F | |
| 4 | G | |
| 5 | H | |
| 6 | I | |
| 7 | K | |
| etc. | | |

:::{figure} images/fig-p3-ch02-2.png
:name: fig-p3-ch02-2
:width: 60%
:align: center
Fig. 2.2: The notation used to specify the quantum numbers $s$, $\ell$, $j$ for an atomic configuration, which for the $^2F_{5/2}$ level is $s=1/2$, $\ell=3$, and $j=5/2$.
:::

Let us illustrate Hund's rule with a few examples.

* **one $4f$ electron in Ce$^{3+}$**

This simple configuration is for a single $4f$ electron for which $\ell = 3$. We have then $\ell = 3$, and $s = 1/2$. Hund's Rules (1) and (2) above are already satisfied. Rule (3) gives $\vec{J} = |\vec{L} - \vec{S}|$ or $j = 5/2$ so we have the result that the ground state of a $4f$ electronic configuration is $^2F_{5/2}$. The $g$-factor using Eq. 1.133 becomes

```{math}
:label: eq-p3-ch02-14
g = \frac{\frac{3}{2}(\frac{35}{4}) - \frac{3}{2}(4) + \frac{3}{8}}{\frac{35}{4}} = \frac{15}{2} .
```

* **the configuration $(4f)^2$ in Pr$^{3+}$**

For this configuration we have two $4f$ electrons. Applying Hund's Rule (1), the maximum $\vec{S}$ we can have is obtained by taking $(m_s)_{\text{total}} = 1/2 + 1/2 = 1$ so that $s = 1$, thus giving a multiplicity $2s+1 = 3$. But then we cannot take both electrons with $m_\ell = 3$ because, if we did, we would violate the Pauli principle. Thus the highest $\ell$ value we can make is to take $m_{\ell_1,\text{max}} = 3$ and $m_{\ell_2,\text{max}} = 2$. Thus $m_{\ell,\text{total,max}} = 5$ so that Hund's Rule (2) gives $\ell = 5$ which, from our table above, is an H state. Application of Rule (3) is made for two electrons filling a shell that can hold $2(2 \cdot 3 + 1) = 14$ electrons so that we are still less than half full. The $j$-value is then found as $(\ell - s)$ and is $j = 5 - 1 = 4$ so that our configuration gives a ground state $^3H_4$ and a Landé $g$-factor from Eq. 1.133

```{math}
:label: eq-p3-ch02-15
g = \frac{\frac{3}{2}(4)(5) - \frac{1}{2}(5)(6) + \frac{1}{2}(1)(2)}{(4)(5)} = \frac{4}{5} .
```

For homework you will have practice in applying Hund's rule to a different electronic configuration.

### 2.3.2 Electronic Configurations

It is also useful to find all the states that emerge from a particular electronic configuration, such as $nd\ n'p$. For example, for the $3d4p$ this two-electron configuration we have one $d$-electron ($\ell = 2$) and one $p$-electron ($\ell = 1$). Applying Hund's Rule (1) tells us that the $s_{\text{total}} = 1$ configuration will lie lower in energy than the $s_{\text{total}} = 0$ configuration. Taking $s_1 = 1/2$ and $s_2 = 1/2$ we can only have $s_{\text{total}}$ values of 0 or 1 as shown in Table {numref}`tab-p3-ch02-1`, and there is no way to make an $s_{\text{total}} = 1/2$.

:::{table} The $s=1$ level is 3-fold degenerate and has $m_s = 1, 0, -1$, while the $s=0$ level is non-degenerate and can only have $m_s = 0$.
:name: tab-p3-ch02-1
| $m_{s_1}$ | $m_{s_2}$ | $m_s$ |
|----------:|----------:|------:|
| 1/2 | 1/2 | 1 |
| 1/2 | -1/2 | 0 |
| -1/2 | 1/2 | 0 |
| -1/2 | -1/2 | -1 |
:::

Now for the $\ell_{\text{total}}$ we can make a state with $\ell = 3$ (state of lowest energy by Hund's Rule (2)). But as shown in Table {numref}`tab-p3-ch02-2` we can also make states with $\ell = 2$ and $\ell = 1$. In this table is listed the number of ways that a given $m_\ell$ value can be obtained. For example, $m_\ell = 1$ can be formed by: (1) $m_{\ell_1} = 2$, $m_{\ell_2} = -1$; (2) $m_{\ell_1} = 1$, $m_{\ell_2} = 0$; and (3) $m_{\ell_1} = 0$, $m_{\ell_2} = 1$.

:::{table} The multiplicities of the various $m_\ell$ levels for the $3d4p$ configuration yielding a total of 15 states.
:name: tab-p3-ch02-2
| $m_\ell$ value | number of states |
|-------------:|-----------------:|
| 3 | 1 |
| 2 | 2 |
| 1 | 3 |
| 0 | 3 |
| -1 | 3 |
| -2 | 2 |
| -3 | 1 |
:::

Since the shells for the two electron configuration $ndn'p$ are less than half-full, the $j$ value with lowest energy is $|\ell - s|$. For $s = 0$, we immediately have $j = \ell$ and no spin-orbit splitting results. For $s = 1$, we have three possible $j$-values: $\ell+1$, $\ell$, $\ell-1$.

We show below that the number of states is invariant whether we consider the $| \ell, s, m_\ell, m_s \rangle$ representation or the $| j, \ell, s, m_j \rangle$ representation. To demonstrate this point, consider an $\ell$-state associated with $s = 1$. This state has a degeneracy $(2\ell+1)(2s+1) = 3(2\ell+1)$. When the spin-orbit interaction is turned on we can make three different $j$ values with degeneracies

```{math}
:label: eq-p3-ch02-16
[2(\ell+1)+1] + (2\ell+1) + [2(\ell-1)+1] = 3(2\ell+1)
```

so that all levels are accounted for independent of the choice of representation. A diagram illustrating the possible states that can be made from the two-electron configuration $nd\ n'p = 3d\ 4p$ is shown in Fig. {numref}`fig-p3-ch02-3`. In order to familiarize yourself with this addition of angular momentum, you will construct one of these diagrams for homework. Figure {numref}`fig-p3-ch02-3` is constructed for the case where the two electrons go into different atomic shells. In the case where the two electrons are placed in the same atomic shell, the Pauli principle applies which states that the quantum numbers assigned to the two electrons must be different. Thus, there will be fewer allowed states by the Pauli principle where $n = n'$ and the angular momentum is also the same. To illustrate the effect of the Pauli principle we will consider two electrons in a $2p3p$ configuration (Fig. {numref}`fig-p3-ch02-4`) and in a $2p^2$ configuration (Fig. {numref}`fig-p3-ch02-5`). A list of possible states for the $2p^2$ configuration is given in Table {numref}`tab-p3-ch02-3`.

:::{figure} images/fig-p3-ch02-3.png
:name: fig-p3-ch02-3
:width: 70%
:align: center
Fig. 2.3: Level scheme for the $ndn'p = 3d4p$ electronic configuration where one electron is placed in a $3d$ shell and a second electron is in a $4p$ shell.
:::

:::{figure} images/fig-p3-ch02-4.png
:name: fig-p3-ch02-4
:width: 70%
:align: center
Fig. 2.4: States in the $2p\ 3p$ electronic configuration.
:::

We notice that in Table {numref}`tab-p3-ch02-3` there are only 15 states in the $2p^2$ configuration because if we have two electrons in a $2p$ level they are indistinguishable and $(m_{\ell_1}, m_{s_1}, m_{\ell_2}, m_{s_2}) = (1, 1/2, 1, -1/2)$ is identical to $(1, -1/2, 1, 1/2)$.

:::{table} List of states allowed in the $2p^2$ electronic configuration.
:name: tab-p3-ch02-3
| $m_{\ell_1}$ | $m_{s_1}$ | $m_{\ell_2}$ | $m_{s_2}$ | $m_\ell$ | $m_s$ | $m_j$ |
|------------:|----------:|------------:|----------:|---------:|------:|------:|
| 1 | 1/2 | 0 | 1/2 | 1 | 1 | 2 |
| 1 | 1/2 | -1 | 1/2 | 0 | 1 | 1 |
| 0 | 1/2 | -1 | 1/2 | -1 | 1 | 0 |
| 1 | 1/2 | 1 | -1/2 | 2 | 0 | 2 |
| 1 | 1/2 | 0 | -1/2 | 1 | 0 | 1 |
| 1 | 1/2 | -1 | -1/2 | 0 | 0 | 0 |
| 0 | 1/2 | 0 | -1/2 | 0 | 0 | 0 |
| 0 | 1/2 | -1 | -1/2 | -1 | 0 | -1 |
| -1 | 1/2 | -1 | -1/2 | -2 | 0 | -2 |
| 0 | 1/2 | 1 | -1/2 | 1 | 0 | 1 |
| -1 | 1/2 | 1 | -1/2 | 0 | 0 | 0 |
| -1 | 1/2 | 0 | -1/2 | -1 | 0 | -1 |
| 1 | -1/2 | 0 | -1/2 | 1 | -1 | 0 |
| 1 | -1/2 | -1 | -1/2 | 0 | -1 | -1 |
| 1 | -1/2 | -1 | -1/2 | -1 | -1 | -2 |
:::

The possible values for $s$ are

```{math}
:label: eq-p3-ch02-17
s_1 + s_2, s_1 + s_2 - 1, \cdots, |s_1 - s_2|
```

and for $\ell$ are

```{math}
:label: eq-p3-ch02-18
\ell_1 + \ell_2, \ell_1 + \ell_2 - 1, \cdots, |\ell_1 - \ell_2|
```

and for $j$ are

```{math}
:label: eq-p3-ch02-19
\ell + s, \ell + s - 1, \cdots, |\ell - s| .
```

Since the Pauli Exclusion Principle prohibits the state

$$
(m_{\ell_1}, m_{s_1}, m_{\ell_2}, m_{s_2}) = (1, 1/2, 1, 1/2)
$$

we cannot have $j = 3$ and the states for $s=1$, $\ell=2$ in Fig. {numref}`fig-p3-ch02-4` do not occur in the $2p^2$ configuration. The ground state is then a $^3P_0$ state with higher lying states in that multiplet being $^3P_1$ and $^3P_2$. To account for the $m_\ell$ value of $\pm 2$ in Table {numref}`tab-p3-ch02-3`, we have a state $^1D_2$; and this state is also consistent with the $m_j$ value of 2 when $m_\ell = 2$. With the $^3P$ states and the $^1D_2$ we have accounted for $9 + 5 = 14$ states and we have one more to go to get to 15. The only way to do this is with a $^1S_0$ state so our diagram becomes as shown in Fig. {numref}`fig-p3-ch02-5`.

:::{figure} images/fig-p3-ch02-5.png
:name: fig-p3-ch02-5
:width: 70%
:align: center
Fig. 2.5: Level scheme for the $2p^2$ configuration where the Pauli Exclusion Principle must be considered explicitly.
:::

A general rule to be used in selecting states allowed by the Pauli principle is that the total state must be antisymmetric under exchange of particles, so that if we have a symmetric spin state, the orbital state must be antisymmetric under interchange of particles. Thus for the $s=1$ symmetric ($\uparrow\uparrow$) spin state, only the antisymmetric orbital state $\ell=1$ is allowed. Likewise, for the $s=0$ antisymmetric ($\uparrow\downarrow$) spin state only the $\ell=0$ and $\ell=2$ symmetrical orbital states are allowed, consistent with the allowed states shown in Fig. {numref}`fig-p3-ch02-5`.

## 2.4 Clebsch-Gordan Coefficients

Up to this point we have used physical arguments (such as the vector model) for finding matrix elements of various operators in the $| \ell, s, j, m_j \rangle$ representation. We shall now view this problem from a more mathematical point of view. If we have a wave function in one representation, we can by a unitary transformation change from one representation to another. This is a mathematical statement of the fact that an arbitrary function can be expressed in terms of any complete set of functions. In quantum mechanics, we write such a transformation quite generally as

```{math}
:label: eq-p3-ch02-20
\psi_\alpha = \sum_\beta \phi_\beta \langle \beta | \alpha \rangle
```

where $\psi_\alpha$ is one member of a complete set of functions designated by quantum number $\alpha$, while $\phi_\beta$ is one member of a different complete set of functions labeled by quantum number $\beta$, and $\langle \beta | \alpha \rangle$ is the transformation coefficient expressing the projection of one "vector" on another, and the sum in Eq. {eq}`eq-p3-ch02-20` is taken over all quantum numbers $\beta$. Because the number of possible states $\alpha$ is equal to the number of states $\beta$ and because $|\psi_\alpha|^2$ is identified with the magnitude of an observable, $\langle \beta | \alpha \rangle$ is a square matrix which conserves lengths and is hence written as a unitary matrix. If now the function $\psi_\alpha$ is an eigenfunction of the total angular momentum and of its $z$ projection, then $\psi_\alpha$ denotes $| \ell, s, j, m_j \rangle$, where the Dirac ket, expressed in terms of all the four quantum numbers, can be written explicitly with appropriate spherical harmonics. Similarly the function $\phi_\beta$ in Eq. {eq}`eq-p3-ch02-20` denotes the wave function $| \ell, s, m_\ell, m_s \rangle$. Then Eq. {eq}`eq-p3-ch02-20` provides an expansion of the $| \ell, s, j, m_j \rangle$ function in terms of the $| \ell, s, m_\ell, m_s \rangle$ function which defines the Clebsch-Gordan coefficients $\langle \ell, s, m_\ell, m_s | \ell, s, j, m_j \rangle$ by

```{math}
:label: eq-p3-ch02-21
| \ell, s, j, m_j \rangle = \sum_{m_s, m_\ell; m_s + m_\ell = m_j} | \ell, s, m_\ell, m_s \rangle \langle \ell, s, m_\ell, m_s | \ell, s, j, m_j \rangle
```

where the sum is on all the $m_s$ and $m_\ell$ values which contribute to a particular $m_j$. Since the operator relation $\vec{J} = \vec{L} + \vec{S}$ is valid, we can write $J_z = L_z + S_z$ and also $m_j = m_\ell + m_s$. In writing Eq. {eq}`eq-p3-ch02-21` we also restrict $j$ to lie between $|\ell - s| \le j \le \ell + s$. These rules can be proved rigorously but we will not do so here. Instead, we will illustrate the meaning of the rules. As an example, take $\ell = 2$, $s = 1/2$. This gives us ten states with $m_j$ values as shown in Table {numref}`tab-p3-ch02-4`. We see that except for the $m_j = \pm 5/2$ states, we have two different states with the same $m_j$ value. This is exactly what is needed to provide six $m_j$ states for $j = 5/2$ and four $m_j$ states for $j = 3/2$. Successive $j$ values differ by one and not by 1/2, since we cannot make proper integral $m_j$ values for $j = \text{integer}$ in the case $\ell = 2$, $s = 1/2$.

:::{table} Listing of the states which couple to the $| \ell, s, j, m_j \rangle$ and $| \ell, s, m_\ell, m_s \rangle$ representations for $\ell = 2$, $s = 1/2$.
:name: tab-p3-ch02-4
| $m_\ell$ | $m_s$ | $m_j$ |
|---------:|------:|------:|
| 2 | 1/2 | 5/2 |
| 2 | -1/2 | 3/2 |
| 1 | 1/2 | 3/2 |
| 1 | -1/2 | 1/2 |
| 0 | 1/2 | 1/2 |
| 0 | -1/2 | -1/2 |
| -1 | 1/2 | -1/2 |
| -1 | -1/2 | -3/2 |
| -2 | 1/2 | -3/2 |
| -2 | -1/2 | -5/2 |
:::

Since the Clebsch-Gordan coefficients form a unitary matrix, we have orthogonality relations between rows and between columns of these coefficients

```{math}
:label: eq-p3-ch02-22
\sum_{m_s, m_\ell} \langle \ell, s, j, m_j | \ell, s, m_\ell, m_s \rangle \langle \ell, s, m_\ell, m_s | \ell, s, j', m'_j \rangle = \delta_{j,j'} \delta_{m_j,m'_j}
```

```{math}
:label: eq-p3-ch02-23
\sum_{m_j} \langle \ell, s, m_\ell, m_s | \ell, s, j, m_j \rangle \langle \ell, s, j, m_j | \ell, s, m'_\ell, m'_s \rangle = \delta_{m_\ell,m'_\ell} \delta_{m_s,m'_s} .
```

We now address ourselves to the problem of calculating the Clebsch-Gordan coefficients. In particular, the coefficient $\langle \ell, s, -\ell, -s | \ell, s, (\ell+s), -(\ell+s) \rangle$ is unity since the state $| \ell, s, -\ell, -s \rangle$ in the $| \ell, s, m_\ell, m_s \rangle$ representation is the same as the state $| \ell, s, (\ell+s), -(\ell+s) \rangle$ in the $| \ell, s, j, m_j \rangle$ representation. As an example of this point take $m_\ell = -2$, $m_s = -1/2$ in Table {numref}`tab-p3-ch02-4`. This makes an $m_j = -5/2$ state and it is the only way to prepare an $m_j = -5/2$ state.

So starting with this minimum $m_j$ value state, we will use the raising operator $J_+ = L_+ + S_+$ of Eq. 1.13 to act on both sides of the equation

```{math}
:label: eq-p3-ch02-24
J_+ | \ell, s, (\ell+s), -(\ell+s) \rangle = (L_+ + S_+) | \ell, s, -\ell, -s \rangle .
```

We then get for the left-hand side using the raising operator relation Eq. 1.13

```{math}
:label: eq-p3-ch02-25
\sqrt{([\ell+s]+[\ell+s])([\ell+s]-[\ell+s]+1)} \ | \ell, s, (\ell+s), (-\ell-s+1) \rangle
```

where the $m_j$ value has now been raised by unity. From the right hand side of Eq. {eq}`eq-p3-ch02-24` we get

```{math}
:label: eq-p3-ch02-26
\sqrt{(\ell+\ell)(\ell-\ell+1)} \ | \ell, s, -\ell+1, -s \rangle + \sqrt{(s+s)(s-s+1)} \ | \ell, s, -\ell, -s+1 \rangle
```

which from Eq. {eq}`eq-p3-ch02-24` gives an equation of the form

```{math}
:label: eq-p3-ch02-27
| \ell, s, (\ell+s), (-\ell-s+1) \rangle = \frac{1}{\sqrt{2(\ell+s)}} \left[ \sqrt{2\ell} \ | \ell, s, -\ell+1, -s \rangle + \sqrt{2s} \ | \ell, s, -\ell, -s+1 \rangle \right] .
```

Thus we have evaluated the Clebsch-Gordan coefficients:

```{math}
:label: eq-p3-ch02-28
\langle \ell, s, -\ell+1, -s | \ell, s, \ell+s, (-\ell-s+1) \rangle = \sqrt{\frac{\ell}{\ell+s}}
```

```{math}
:label: eq-p3-ch02-29
\langle \ell, s, -\ell, -s+1 | \ell, s, \ell+s, (-\ell-s+1) \rangle = \sqrt{\frac{s}{\ell+s}} .
```

And by repeated application of the raising operator $J_+$ we can find all the Clebsch-Gordan coefficients corresponding to a given $j$ value. To find the coefficients for the $(j-1)$ quantum states, we must use the orthogonality relations given by Eqs. {eq}`eq-p3-ch02-22` and {eq}`eq-p3-ch02-23` to construct one coefficient and then use raising and lowering operators to produce the remaining coefficients for the $(j-1)$ set of states.

As an example of the Clebsch-Gordan coefficients, consider the addition of angular momentum for two spins (e.g., take $\ell = 1/2$ and $s = 1/2$). The development given here is general and we can imagine this case to illustrate a $\vec{J}$ arising from the addition of two angular momenta, $\vec{J} = \vec{S}_1 + \vec{S}_2$. From Eqs. {eq}`eq-p3-ch02-28` and {eq}`eq-p3-ch02-29` we have for the Clebsch-Gordan coefficients:

```{math}
:label: eq-p3-ch02-30
\left\langle \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, -\frac{1}{2} \middle| \frac{1}{2}, \frac{1}{2}, 1, 0 \right\rangle = \frac{1}{\sqrt{2}} = \left\langle \frac{1}{2}, \frac{1}{2}, -\frac{1}{2}, \frac{1}{2} \middle| \frac{1}{2}, \frac{1}{2}, 1, 0 \right\rangle .
```

Clearly $\langle 1/2, 1/2, -1/2, -1/2 | 1/2, 1/2, 1, -1 \rangle = 1$. It is convenient to represent these results in matrix form

:::{table} Clebsch-Gordan coefficients for $\ell = 1/2$, $s = 1/2$.
:name: tab-p3-ch02-5
| $\langle \ell, s, m_\ell, m_s \vert \ / \ \vert \ell, s, j, m_j \rangle$ | $\vert 1/2, 1/2, 1, 1 \rangle$ | $\vert 1/2, 1/2, 1, 0 \rangle$ | $\vert 1/2, 1/2, 1, -1 \rangle$ | $\vert 1/2, 1/2, 0, 0 \rangle$ |
|------------------------------------------------------------|----------------------------|-----------------------------|------------------------------|----------------------------|
| $\langle 1/2, 1/2, 1/2, 1/2 \vert$ | 1 | 0 | 0 | 0 |
| $\langle 1/2, 1/2, 1/2, -1/2 \vert$ | 0 | $\frac{1}{\sqrt{2}}$ | 0 | $\frac{1}{\sqrt{2}}$ |
| $\langle 1/2, 1/2, -1/2, 1/2 \vert$ | 0 | $\frac{1}{\sqrt{2}}$ | 0 | $-\frac{1}{\sqrt{2}}$ |
| $\langle 1/2, 1/2, -1/2, -1/2 \vert$ | 0 | 0 | 1 | 0 |
:::

where the $\langle \ell, s, m_\ell, m_s |$ values label the rows and the $| \ell, s, j, m_j \rangle$ values label the columns. The zero entries in the last column are found by requiring $m_j = m_\ell + m_s$. The $1/\sqrt{2}$ and $-1/\sqrt{2}$ entries are found from normalization. The orthogonality and normalization requirements are valid because the Clebsch-Gordan coefficients form a unitary transformation.

Clebsch-Gordan coefficients are found tabulated in various quantum mechanics texts as well as in books on group theory (in a chapter on the full rotation group). For our present purposes in a solid state course, you should know how to construct such matrices for the addition of small angular momenta such as $\ell = 1$, $s = 1/2$ (homework problem). You should also know how to use tabulated Clebsch-Gordan matrices that you will find in books and journal articles.

Now let us see what the Clebsch-Gordan coefficients have to do with the evaluation of the various matrix elements that occur in problems on magnetism. Suppose we have an operator $L_z$ acting on an eigenfunction in the $| \ell, s, j, m_j \rangle$ representation. The wave function $| \ell, s, j, m_j \rangle$ is not an eigenfunction of $L_z$; that is, the operator $L_z$ does not act on $| \ell, s, j, m_j \rangle$ to give an eigenvalue times $| \ell, s, j, m_j \rangle$. We can find the action of $L_z$ on $| \ell, s, j, m_j \rangle$ by expressing this state in terms of states which are eigenstates of $L_z$, namely the states $| \ell, s, m_\ell, m_s \rangle$. We then get

```{math}
:label: eq-p3-ch02-31
L_z | \ell, s, j, m_j \rangle = \sum_{m_\ell, m_s; m_\ell + m_s = m_j} L_z | \ell, s, m_\ell, m_s \rangle \langle \ell, s, m_\ell, m_s | \ell, s, j, m_j \rangle
```

where the sum is restricted to $m_\ell$ and $m_s$ values for which $m_j = m_s + m_\ell$. We note that the action of $L_z$ on an eigenstate of $L_z$ gives $m_\ell \hbar | \ell, s, m_\ell, m_s \rangle$. Thus we get for the expectation value of $L_z$ in the $| \ell, s, j, m_j \rangle$ representation a sum over all $m_\ell$ and $m_s$ states that contribute to $m_j$:

```{math}
:label: eq-p3-ch02-32
\langle \ell, s, j, m_j | L_z | \ell, s, j, m_j \rangle = \sum_{m_\ell, m_s; m_\ell + m_s = m_j} \hbar m_\ell \langle \ell, s, j, m_j | \ell, s, m_\ell, m_s \rangle \langle \ell, s, m_\ell, m_s | \ell, s, j, m_j \rangle .
```

It is readily seen that the results obtained with the Clebsch-Gordan coefficients are in agreement with the vector model.

The Clebsch-Gordan coefficients are more general than the vector model discussed in §1.6 in that these coefficients allow the calculation of off-diagonal matrix elements as well as the diagonal matrix elements that can also be evaluated by the vector model. Operators that are not diagonalized by a given representation have non-vanishing off-diagonal matrix elements, as for example $\langle \ell, s, j', m'_j | L_z | \ell, s, j, m_j \rangle$, which enter when considering transitions between eigenstates.

The Clebsch-Gordan coefficients are also useful in finding explicit wave functions in the sense of wave mechanics. For example, we can use the Clebsch-Gordan coefficients to write the wave functions for a given $\ell$ and $s = 1/2$ namely

```{math}
:label: eq-p3-ch02-33
| \ell, s, m_\ell, m_s = 1/2 \rangle = Y_{\ell m_\ell}(\theta, \phi) \ \chi_\alpha
```

where $\chi_\alpha$ denotes the spin function for spin up. The spin function for spin down would then be written as $\chi_\beta$ and would correspond to $m_s = -1/2$. We can write an explicit expression for $| \ell, s, j, m_j \rangle$ by making use of the spherical harmonics and the Clebsch-Gordan coefficients. An alternate method for finding explicit expressions for the wave functions $| \ell, s, j, m_j \rangle$ is to remain entirely within the bounds of wave mechanics and to use the Addition Theorem for Spherical Harmonics which is discussed in many of the standard quantum mechanics texts.
