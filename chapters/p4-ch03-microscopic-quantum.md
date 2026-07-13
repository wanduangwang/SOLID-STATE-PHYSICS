---
title: "3 Microscopic Quantum Description of Superconductivity"
abstract: "The Bardeen-Cooper-Schrieffer (BCS) microscopic theory is presented, starting from the Cooper instability and the formation of bound electron pairs, through the reduced Hamiltonian formalism with creation/annihilation operators, to the ground state solution, gap parameter determination, condensation energy, and quantitative predictions for critical temperature, energy gap, critical field, and specific heat."
---

# 3 Microscopic Quantum Description of Superconductivity

## 3.1 Bardeen-Cooper-Schrieffer (BCS) Theory

### 3.1.1 The Cooper Instability

**References:**

* L. N. Cooper, "Bound Electron Pairs in a Degenerate Fermi Gas," *Phys. Rev.* **104**, 1189 (1956).
* J. Bardeen, L. N. Cooper, and J. R. Schrieffer, "Theory of Superconductivity," *Phys. Rev.* **108**, 1175 (1957).
* T. van Duzer and C.W. Turner, *Principles of Superconductive Devices and Circuits*, Elsevier, NY (1981).

Cooper's 1956 paper demonstrated that the energy of a Fermi system can be lowered by the formation of weakly bound electron pairs at $T = 0$ for any attractive interaction, no matter how small. This landmark paper paved the way for the full-blown BCS theory, which was published shortly afterward. Here we will show the derivation of the famous BCS formula for $T_c$, as given in Cooper's paper, which contains many of the important ideas of the BCS paper.

Let us therefore follow Cooper's derivation. Consider an arbitrarily weak interaction between electrons $\mathcal{H}_1$. If the interaction is small, then there is a minimum energy $\epsilon_{\min} = (\hbar^2 q_{\max}^2)/2m$ below which its effect will be so small that it can approximately be ignored. Likewise there should also be a maximum energy, $\epsilon_{\max} = (\hbar^2 q_{\max}^2)/2m$. Since we know that in real superconductors the electron-electron interaction is phonon-mediated, we can assume that the minimum energy for which the perturbation $\mathcal{H}_1$ is non-negligible is about $(E_F - \hbar\omega_D)$, and the maximum energy is about $(E_F + \hbar\omega_D)$ where $\omega_D$ is the Debye frequency, so that $\epsilon_{\max} - \epsilon_{\min} = 2\hbar\omega_D$.

For the wavefunctions of the assumed electron pairs, we can take the simplest possible form,

```{math}
:label: eq-p4-ch03-1
\phi(\vec{k}_1,\vec{k}_2;\vec{r}_1,\vec{r}_2)=\frac{1}{V}e^{i(\vec{k}_1\cdot\vec{r}_1+\vec{k}_2\cdot\vec{r}_2)}
```

where the spins of the two electrons in question must be antiparallel, so that their overall wavefunction will be antisymmetric under interchange of their coordinates, as is required for Fermions. If we now let

```{math}
:label: eq-p4-ch03-2
\begin{aligned}
\vec{R}&=\tfrac{1}{2}(\vec{r}_1+\vec{r}_2),\\
\vec{r}&=(\vec{r}_2-\vec{r}_1),\\
\vec{K}&=(\vec{k}_1+\vec{k}_2), \quad\text{and}\\
\vec{k}&=\tfrac{1}{2}(\vec{k}_2-\vec{k}_1)
\end{aligned}
```

in order to change to center of mass coordinates, then

```{math}
:label: eq-p4-ch03-3
\phi(\vec{k}_1,\vec{k}_2;\vec{r}_1,\vec{r}_2)=\frac{1}{V}e^{i(\vec{K}\cdot\vec{R}+\vec{k}\cdot\vec{r})}
```

and the energy becomes

```{math}
:label: eq-p4-ch03-4
E=\frac{\hbar^2}{2m}(k_1^2+k_2^2)=\frac{\hbar^2}{m}\!\left(\frac{K^2}{4}+k^2\right)=\epsilon_K+\epsilon_k
```

We can equally well write the Cooper pair wave function as

```{math}
:label: eq-p4-ch03-5
\Psi_K(\vec{R},\vec{r})=\frac{1}{V}e^{i(\vec{K}\cdot\vec{R})}\sum_{\vec{k}}a_{\vec{k}} e^{i\vec{k}\cdot\vec{r}}
```

where the coefficients $a_{\vec{k}}$ must be chosen so that $\tilde{\nabla}_{\vec{k}}\Psi_K(\vec{R},\vec{r})=ik\Psi_K(\vec{R},\vec{r})$. (So far all we have done is notational, in order to make what follows plausible.) If we now substitute the wavefunction of Eq. (3.5) into the Schrodinger equation, with the energy defined in Eq. (3.4), we get

```{math}
:label: eq-p4-ch03-6
\left[-\frac{\hbar^2}{m}\left(\vec{\nabla}_{\vec{r}}^2+\frac{1}{4}\vec{\nabla}_{\vec{R}}^2\right)+\mathcal{H}_1\right]\Psi_K(\vec{R},\vec{r})=E\Psi_K(\vec{R},\vec{r})
```

If we take the dot product of Eq. (3.6) with $\langle e^{-i(\vec{k}'\vec{r}+\vec{K}'\vec{R})}|$ and perform the integrations over $\vec{R}$ and $\vec{r}$, we get for the kinetic energy term

```{math}
:label: eq-p4-ch03-7
\langle e^{-i(\vec{k}'\vec{r}+\vec{K}'\vec{R})}| -\frac{\hbar^2}{m}(\vec{\nabla}_{\vec{r}}^2+\frac{1}{4}\vec{\nabla}_{\vec{R}}^2)\mid\Psi_K(\vec{R},\vec{r})\rangle=(\epsilon_{K'}+\epsilon_{k'})\frac{a_{\vec{k}'}}{V}
```

and the perturbation term becomes

```{math}
:label: eq-p4-ch03-8
\langle e^{-i(\vec{k}'\vec{r}+\vec{K}'\vec{R})}\mid\mathcal{H}_1\mid\Psi_K(\vec{R},\vec{r})\rangle=\frac{\delta(\vec{K}'-\vec{K}')}{V}\sum_{\vec{k}'}a_{\vec{k}'}\left[\int_{-\infty}^{\infty}d^3re^{-i\vec{k}'\vec{r}}\mathcal{H}_1e^{i\vec{k}\vec{r}}\right]
```

Therefore, if we use the notation $\lvert\vec{k}\rangle$ for a plane wave, the Schrodinger equation may be written as

```{math}
:label: eq-p4-ch03-9
(E-\epsilon_{K'}-\epsilon_{k'})a_{\vec{k}'}=\delta(\vec{K}-\vec{K}')\sum_{\substack{k'\\\vec{k}'\le q_{\min}}}a_{\vec{k}'}\langle\vec{k}'|\mathcal{H}_1|\vec{k}'\rangle
```

Since the perturbation $\mathcal{H}_1$ couples only electrons with $k$ and $k'$ in a small shell around the Fermi surface, Cooper made the approximation that

```{math}
:label: eq-p4-ch03-10
\langle\vec{K}'|\mathcal{H}_1|\vec{k}\rangle\simeq\begin{cases}-|V|,&q_{\min}\le k,k'\le q_{\max}\\0,&\text{otherwise}\end{cases}
```

With this approximation, the Schrodinger equation reduces to

```{math}
:label: eq-p4-ch03-11
a_{\vec{k}}=\frac{-|V|}{(E-\epsilon_{K'}-\epsilon_{k'})}\sum_{\vec{k}'}a_{\vec{k}'}
```

as long as $\vec{K}=\vec{K}'$. Since from normalization we must have

```{math}
:label: eq-p4-ch03-12
\sum_{\vec{k}}a_{\vec{k}}=C,
```

Eq. (3.11) becomes

```{math}
:label: eq-p4-ch03-13
\sum_{\vec{k}}a_{\vec{k}}=C=-|V|\sum_{\vec{k}}\frac{C}{(E-\epsilon_{K'}-\epsilon_{k'})}=-|V|\frac{2C}{(2\pi)^3}\int_{q_{\min}}^{q_{\max}}\frac{d\vec{k}'}{(E-\epsilon_{K'}-\epsilon_{k'})}
```

We can change the variable of integration to energy:

```{math}
:label: eq-p4-ch03-14
-|V|\int_{\epsilon_{\min}}^{\epsilon_{\max}}\frac{d\epsilon_k N(E)}{(E-\epsilon_K-\epsilon_k)}=1
```

and using the fact that the range of the limits of integration is small, we can take the density of states at the Fermi energy $N(E)\approx N(K,E_F)$. If we then integrate the above equation, and make use of

$$\int d x/x = \ln x \quad\text{and}\quad \ln x - \ln y = \ln(x/y)$$

we find

```{math}
:label: eq-p4-ch03-15
\exp\!\left[\frac{1}{N(K,E_F)|V|}\right]=\frac{E-\epsilon_K-\epsilon_{\max}}{E-\epsilon_K-\epsilon_{\min}}.
```

Then, by simplifying Eq. (3.15), we get for the energy of the pair

```{math}
:label: eq-p4-ch03-16
E=\epsilon_K+\epsilon_{\min}-\frac{2\hbar\omega_D}{\exp[|N(K,E_F)||V|]-1}
```

There are several interesting points to be made about Eq. (3.16), as Cooper himself pointed out. The first is that the energy of the electron pair is lower than that of the individual electrons, and the energy of the pair is lowest if $\epsilon_K$, the center-of-mass energy, is zero. A zero center of mass energy implies that the electrons have both opposite spin and momenta (see Fig. 2.2); such a state has henceforth been known as a Cooper pair. The energy of such a pair is lower than that of the individual electrons by an amount $\Delta$ defined by

```{math}
:label: eq-p4-ch03-17
\Delta=\frac{2\hbar\omega_D}{\exp[N(|E_F\rangle||V|)]-1}\simeq2\hbar\omega_D\exp\!\left[\frac{-1}{N(|E_F\rangle||V|)}\right]
```

where we neglected the 1 since in the exponential term the product $N(E_F)V$ is small.

If $\Delta \simeq 2k_BT_c$, then we recover the famous BCS equation for $T_c$.

What has been presented above is the substance of Cooper's original paper, from which many of the important ideas, if not the details, of the BCS theory can be extracted. The BCS paper makes many useful predictions, and continues today to be widely read because of its great physical utility. However, the theory is limited to utility as far as calculation of the properties of actual materials goes, and has been largely supplanted by modern Green's functions methods for first principles calculations. For understanding the properties of superconducting systems with complex geometries, like layered materials, the phenomenological Ginzburg-Landau theory of superconductivity (see Chapter 2) has proven to be very useful.

### 3.1.2 Ground State From Cooper Pairs

The preceding section gave a description of a Cooper pair for two electrons in a Fermi sea. BCS took the essential step in providing a full microscopic description of the superconducting state by constructing a ground state wave function in which all the electrons form bounded pairs. The BCS approximation to the electronic ground state wave function can be described as follows: group the $N$ conduction electrons into $N/2$ Cooper pairs described by the wave function $\phi(\vec{r}s,\vec{r}'s')$, where $\vec{r}$ is the electronic position and $s$ is the spin quantum number. Then consider the $N$-electron wave function as a product of $N/2$ identical Cooper pair wave functions

```{math}
:label: eq-p4-ch03-18
\Psi_N(\vec{r}_1s_1,\cdots,\vec{r}_Ns_N)=\phi(\vec{r}_1s_1,\vec{r}_2s_2)\cdots\phi(\vec{r}_{N-1}s_{N-1},\vec{r}_Ns_N).
```

Though this state describes a state in which all electrons are bound, in pairs, into identical two electron states, it lacks the symmetry required by the Pauli principle:

```{math}
:label: eq-p4-ch03-19
\Psi_{\rm BCS}=\mathcal{A}\Psi_N
```

where $\mathcal{A}$ is the antisymmetrization operator.

### 3.1.3 Hamiltonian for the Superconducting Ground State

In this section and the next we shall introduce the theory of the superconducting ground state, which is a part of the microscopic theory of superconductivity published by Bardeen, Cooper, and Schrieffer in 1957. The method of finding the ground state involves

1. devising a Hamiltonian operator, which we do in this section,
2. using an assumed ground-state wave function to find an expression for the energy, and finally
3. minimizing the energy to find the coefficients in the ground-state wave function.

The latter two parts are done in the following section.

The BCS theory is presented in the formalism of second quantization involving creation and annihilation operators. For a systematic introduction to operator algebra, consult a quantum mechanics text. The equations are written in terms of the creation and annihilation operators introduced earlier for single electrons and now extended to electron pairs. The creation operator $c_{\vec{k}\uparrow}^\star$ places an electron in state $\vec{k}$ with spin up, so that if $c_{\vec{k}\uparrow}^\star$ operates on the "vacuum" state, in which all $\vec{k}$ states are empty, it produces a new state with one spin-up electron in state $\vec{k}$:

```{math}
:label: eq-p4-ch03-20
c_{\vec{k}\uparrow}^\star|0\rangle=|\vec{k}\rangle.
```

Likewise, the annihilation operator $c_{\vec{k}\uparrow}$ causes the elimination of an electron in state $\vec{k}$ with spin $\uparrow$:

```{math}
:label: eq-p4-ch03-21
c_{\vec{k}\uparrow}|\vec{1}_{\vec{k}\uparrow}\rangle=|0\rangle.
```

These operators are used to formulate the Hamiltonian. It is only necessary to consider the differences from the normal ground state, which are referred to as **reduced energies**. Each electron-phonon-electron interaction of the type shown in Fig. 2.2 and discussed in section 3.1.1 contributes to the potential energy of the superconducting state relative to the ground state. As the Cooper model, we restrict consideration for paired states $k\uparrow$ to $-\vec{k}\downarrow$. The pair transition can be represented by the product of creation and annihilation operators,

```{math}
:label: eq-p4-ch03-22
c_{-\vec{k}\downarrow}^\star c_{\vec{k}\uparrow}^\star c_{-\vec{q}\downarrow} c_{\vec{q}\uparrow}.
```

If this operator operates on the ground state, it first removes the electrons from $\vec{k}$ and $-\vec{k}$ states and then places them in $\vec{k}+\vec{q}$ and $-\vec{k}-\vec{q}$ with their spin unaffected. Taking the sum of all such scattering events, one obtains the potential energy relative to the normal state, which we call the reduced potential energy:

```{math}
:label: eq-p4-ch03-23
V_{red}=\sum_{\vec{k},\vec{q}}V_{\vec{k}\vec{q}}c_{\vec{k}+\vec{q}\uparrow}^\star c_{-\vec{k}-\vec{q}\downarrow}^\star c_{-\vec{k}\downarrow} c_{\vec{k}\uparrow}
```

where $\vec{k}'=\vec{k}+\vec{q}$. It can be shown that this gives a lowering of the energy for the superconducting state and this lowering of the energy becomes more pronounced as the number of scattering events increases, thus adding justification for using $\vec{k},-\vec{k}$ pairs.

Since the BCS theory involves only pairs of a certain kind (i.e., $\vec{k}\uparrow$ and $-\vec{k}\downarrow$), single-electron operators are replaced by pair operators

```{math}
:label: eq-p4-ch03-24
b_{\vec{k}}^\star=c_{\vec{k}\uparrow}^\star c_{-\vec{k}\downarrow}^\star
```

and

```{math}
:label: eq-p4-ch03-25
b_{\vec{k}}=c_{-\vec{k}\downarrow}c_{\vec{k}\uparrow}
```

Since these pairs consist of a spin $\uparrow$ and a spin $\downarrow$ electron, it might be expected that the pairs would behave like bosons. However, this is not strictly the case because the Pauli principle applies: no $\vec{k}\uparrow,-\vec{k}\downarrow$ state may be occupied by more than one pair at a time. It does turn out that the pair behavior is close enough to that of a boson so that boson electrodynamics gives a very good representation of the actual behavior of superconductors.

Using Eqs. 3.24 and 3.25, the reduced potential energy in Eq. 3.23 may be rewritten as

```{math}
:label: eq-p4-ch03-26
V_{red}=\sum_{\vec{k}\vec{k}'}V_{\vec{k}\vec{k}'}b_{\vec{k}'}^\star b_{\vec{k}}
```

The kinetic energy can be written as the sum of the pair energies in each of the occupied pair states. The corresponding Hamiltonian thus must contain the number operator $\hat{n}_{\vec{k}}$ which has the property

```{math}
:label: eq-p4-ch03-27
\hat{n}_{\vec{k}}|\eta'_{\vec{k}}\rangle=n|\eta'_{\vec{k}}\rangle
```

which states that the eigenstate of $\hat{n}_{\vec{k}}$ is the state having the wave number $\vec{k}$ and occupancy $n$, and the eigenvalue of $\hat{n}_{\vec{k}}$ is the occupancy. The number operator in the case of pairs is $b_{\vec{k}}^\star b_{\vec{k}}$. Then the pair kinetic energy relative to the Fermi energy is

```{math}
:label: eq-p4-ch03-28
\mathcal{H}_{KE}=2\sum_{\vec{k}<k_F}\epsilon_{\vec{k}} b_{\vec{k}}^\star b_{\vec{k}}
```

where $\epsilon_{\vec{k}}=(\hbar^2k^2/2m)-E_F$ is a single particle energy representing the kinetic energy of a Bloch state measured relative to the Fermi level. To express the energy in reduced form (i.e., the kinetic energy relative to the normal ground state), we subtract

```{math}
:label: eq-p4-ch03-29
2\sum_{\vec{k}<k_F}\epsilon_{\vec{k}}
```

from the kinetic energy given by Eq. 3.28 and the factor of 2 arises because $\epsilon_{\vec{k}}$ denotes the single particle energy for each of the electrons in the pair. This can be done by using the pair commutation relations:

```{math}
:label: eq-p4-ch03-30
[b_{\vec{k}},b_{\vec{k}'}^\star]=[1-\hat{n}_{\vec{k}}-\hat{n}_{-\vec{k}}]\delta_{\vec{k}\vec{k}'}
```

and the anti-commutator

```{math}
:label: eq-p4-ch03-31
\{b_{\vec{k}},b_{\vec{k}'}\}=2b_{\vec{k}}b_{\vec{k}'}(1-\delta_{\vec{k}\vec{k}'})
```

where the square bracket denotes the commutator $[x,y]=xy-yx$ and the curly bracket denotes the anti-commutator $\{x,y\}=xy+yx$. Performing this operation on Eq. 3.28 and adding to Eq. 3.26, we get the total reduced Hamiltonian:

```{math}
:label: eq-p4-ch03-32
\mathcal{H}_{red}=2\sum_{\vec{k}<k_F}|\epsilon_{\vec{k}}|b_{\vec{k}}^\star b_{\vec{k}}+2\sum_{\vec{k}>k_F}\epsilon_{\vec{k}} b_{\vec{k}}^\star b_{\vec{k}}+\sum_{\vec{k}\vec{k}'}V_{\vec{k}\vec{k}'}b_{\vec{k}'}^\star b_{\vec{k}}
```

When operating on the ground state $|0\rangle$ only the operator $b_{\vec{k}}^\star$ can yield a non-vanishing result and likewise the operator $b_{\vec{k}}$ is required to operate on an excited state. To explain the factor of 2 in Eqs. 3.28--3.32 another way, these factors arise because we count pairs where there are two possible spins for each $\vec{k}$. The summation considers only the case where we put a spin-up electron in each $\vec{k}$ state and a spin-down electron in the corresponding $-\vec{k}$ state with the factor of 2. Each state for $k<k_F$ contains the full complement of both spin-up electrons and spin-down electrons.

### 3.1.4 Superconducting Ground State

In this section we use the reduced Hamiltonian Eq. 3.32, to find the distribution of pair occupancy in the superconducting ground state. According to the BCS theory, the ground state should be written as the product of the occupation operators for all pair states.

```{math}
:label: eq-p4-ch03-33
|\Psi\rangle=\prod_{\vec{k}}\left[u_{\vec{k}}+v_{\vec{k}}b_{\vec{k}}^\star\right]|0\rangle
```

Here $|0\rangle$ is the vacuum state, $v_{\vec{k}}^2$ is the probability of pair occupancy, and $u_{\vec{k}}^2=1-v_{\vec{k}}^2$ is the probability of pair vacancy. The first term in Eq. 3.33 is included since it is needed for normalization of $|\Psi\rangle$. The formation of the BCS ground state of Eq. 3.33 is illustrated in Fig. 3.1 where the successive addition of pairs is schematically shown.

The energy of the superconducting ground state relative to the normal ground state is the expectation value of the reduced Hamiltonian:

```{math}
:label: eq-p4-ch03-34
W=\langle\Psi|\mathcal{H}_{red}|\Psi\rangle
```

Substituting Eq. 3.33 and Eq. 3.32 into Eq. 3.34, one obtains

```{math}
:label: eq-p4-ch03-35
W=2\sum_{\vec{k}<k_F}\epsilon_{\vec{k}}v_{\vec{k}}^2+2\sum_{\vec{k}>k_F}|\epsilon_{\vec{k}}|v_{\vec{k}}^2+\sum_{\vec{k}\vec{k}'}V_{\vec{k}\vec{k}'}u_{\vec{k}}v_{\vec{k}}u_{\vec{k}'}v_{\vec{k}'}v_{\vec{k}'}
```

To find the equilibrium we must minimize Eq. 3.35 with respect to $v_{\vec{k}}^2$ by setting $[\partial W/\partial(v_{\vec{k}}^2)]=0$. The resulting probability of occupancy is found to be

```{math}
:label: eq-p4-ch03-36
v_{\vec{k}}^2=\frac{1}{2}[1-\epsilon_{\vec{k}}/(\Delta_{\vec{k}}^2+\epsilon_{\vec{k}}^2)^{1/2}].
```

The parameter $\Delta_{\vec{k}}$ called the **gap parameter** will be seen in section 3.2 to have a special significance and is defined by

```{math}
:label: eq-p4-ch03-37
\Delta_{\vec{k}}=-\sum_{\vec{k}'}V_{\vec{k}\vec{k}'}v_{\vec{k}'}u_{\vec{k}'}
```

We can put Eq. 3.36 in a simpler form by defining another energy

```{math}
:label: eq-p4-ch03-38
E_{\vec{k}}=(\Delta_{\vec{k}}^2+\epsilon_{\vec{k}}^2)^{1/2}.
```

Using Eq. 3.38 the probability of occupancy (see Eq. 3.36) becomes

```{math}
:label: eq-p4-ch03-39
v_{\vec{k}}^2=\frac{1}{2}[1-\epsilon_{\vec{k}}/E_{\vec{k}}]
```

which is plotted in Fig. 3.2. This figure shows that the probability of pair occupancy does not vanish above $E_F$. Pairs move to $\vec{k}$ states of higher kinetic energy [first term in Eq. (3.35)] in order to maximize scattering possibilities since that reduces the potential energy [third term in Eq. 3.35] by more than the increase of kinetic energy. The equilibrium distribution is reached when a further increase of kinetic energy is not offset by a decrease of potential energy. The distribution is reminiscent of the normal state with $T\neq 0$, but for the superconducting state, this distribution occurs at $T=0$. The region of $\epsilon_{\vec{k}}$ over which $v_{\vec{k}}^2$ is significantly different from both unity and zero is of the order of a few $\Delta_{E_F}$ (typically, a few milli-electron volt!).

:::{figure} images/fig-p4-ch03-1.png
:name: fig-p4-ch03-1
:width: 90%
:align: center
Figure 3.1: Formation of the BCS ground state by successive addition of pairs. Not illustrated are the weighting $v_{\vec{k}}$ of the pairs. The oppositely directed spins are shown. (i) shows the vacuum state and (ii)--(iv) show successive additions of pairs.
:::

:::{figure} images/fig-p4-ch03-2.png
:name: fig-p4-ch03-2
:width: 50%
:align: center
Figure 3.2: Probability of pair occupancy in the superconducting ground state.
:::

### 3.1.5 Long-range Coherence

The electron occupation of the paired $\vec{k}$ states can considered to be that of the Cooper pair. Within a spatial region having a diameter on the order of $1~\mu$m, there is a phase coherence much like that in a de Broglie wave packet for a single electron. This distance is called the **coherence length** and is denoted by the symbol $\xi$. The center-of-mass coordinates of about a million interacting pairs lie within a sphere of diameter $\xi$. It is energetically favorable for overlapping pairs to lock phases. The whole superconducting fluid can be viewed as consisting of a large number of overlapping pairs. The individual pairs are comprised of a large number of $\vec{k}$ states centered in magnitude about $k_F$. The resulting wave packet has a wavelength of about one-thousandth of the pair diameter. The waves oscillate at a frequency $\omega=2E_F/\hbar$. In the absence of a net pair momentum, the phases of all pairs are locked together and they oscillate in unison.

If the pairs of $\vec{k}$ states have a nonzero net wave vector $\vec{K}$, the wave function representing the superconducting fluid is multiplied by $\exp(i\vec{K}\cdot\vec{r})$. We can represent the fluid by an ensemble-average function $\Psi=|\Psi(\vec{r})|e^{i\theta(\vec{r})}$ when $K=0$ and by

```{math}
:label: eq-p4-ch03-40
\Psi=|\Psi(\vec{r})|e^{i\theta(\vec{r})}e^{i\vec{K}\cdot\vec{r}}
```

when $K\neq 0$. This is usually written in the more general form

```{math}
:label: eq-p4-ch03-41
\Psi=|\Psi(\vec{r})|e^{i\theta(\vec{r})}
```

where $\theta$ is the phase of the electron pairs, thereby giving a mathematical basis for the ansatz used in Eq. 2.16. Figure 3.3 shows the situation where there is a phase variation, as in Eq. 3.41. In Fig. 3.3 the phases of just two pairs are shown to avoid confusion; the phases of these pairs are seen to differ from one another by $180^\circ$. The phases of all the pairs evolve at the angular frequency $2E_F/\hbar$ while maintaining the $\theta(\vec{r})$ relative phase differences.

:::{figure} images/fig-p4-ch03-3.png
:name: fig-p4-ch03-3
:width: 90%
:align: center
Figure 3.3: The superconducting ground state is composed of a very large number of overlapping Cooper pairs. The phases are locked together to minimize the energy. If there is net momentum, there is a gradient of phase, as illustrated by the dashed line.
:::

## 3.2 Gap Parameter and Condensation Energy at $T=0$

Let us examine further the gap parameter $\Delta_{\vec{k}}$. Substitution of Eq. 3.39 into Eq. 3.37 gives

```{math}
:label: eq-p4-ch03-42
\Delta_{\vec{k}}=-\sum_{\vec{k}'}V_{\vec{k}\vec{k}'}\frac{\Delta_{\vec{k}'}}{2E_{\vec{k}'}}
```

At this point some simplifying assumptions are made to solve Eq. 3.42. First, we assume that $V_{\vec{k}\vec{k}'}=-V$ if both $|\epsilon_{\vec{k}}|$ and $|\epsilon_{\vec{k}'}|$ are less than $\hbar\omega_D$ and is zero otherwise following Eq. 3.8. It is further assumed that $\Delta_{\vec{k}}=\Delta$, a constant, for $|\epsilon_{\vec{k}}|<\hbar\omega_D$ and is zero otherwise. Thus the quantity in Eq. 3.42 becomes

```{math}
:label: eq-p4-ch03-43
E=(\Delta^2+\epsilon^2)^{1/2}
```

in which $\Delta$ taken as a constant and $\epsilon$ and $E$ understood to be functions of $\vec{k}$. Next, the summation over $\vec{k}$ in Eq. 3.42 is replaced by an integral over the corresponding energy range. Further, we make use of the fact that the density of states is nearly constant close to $E_F$, so $N(\epsilon)\simeq N(0)$ over the range $|\epsilon_{\vec{k}}|<\hbar\omega_D$. With these simplifications, Eq. 3.42 becomes

```{math}
:label: eq-p4-ch03-44
\frac{N(0)V}{2}=\int_{-\hbar\omega_D}^{\hbar\omega_D}\frac{d\epsilon}{[\epsilon^2+\Delta^2]^{1/2}}.
```

Performing the integration in Eq. 3.44 and rearranging terms, we obtain

```{math}
:label: eq-p4-ch03-45
\Delta=\frac{\hbar\omega_D}{\sinh\!\bigl[\frac{1}{N(0)V}\bigr]}
```

If $N(0)V\ll 1$, the superconductor has **weak coupling** between electrons and phonons, as is the case in most of the elemental superconducting materials, and in this limit Eq. 3.45 reduces to

```{math}
:label: eq-p4-ch03-46
\Delta=2\hbar\omega_D\exp\!\Bigl[\frac{-1}{N(0)V}\Bigr]
```

A typical value of $\Delta$ for conventional superconductors is about 1 meV.

### 3.2.1 Condensation Energy

We now calculate the difference in energy between the superconducting and normal states; this is called the energy of condensation into the superconducting state. The difference of kinetic energies is

```{math}
:label: eq-p4-ch03-47
(KE)_s-(KE)_n=2\sum_{\vec{k}<k_F}|\epsilon_{\vec{k}}|(v_{\vec{k}}^2-1)+2\sum_{\vec{k}>k_F}\epsilon_{\vec{k}} v_{\vec{k}}^2
```

Using Eqs. 3.38, 3.39 and 3.46 we can rewrite Eq. 3.47 as

```{math}
:label: eq-p4-ch03-48
(KE)_s-(KE)_n=N(0)\Delta^2\left[\frac{1}{N(0)V}-\frac{(1-e^{-2/N(0)V})}{2}\right]
```

Similarly, the difference of potential energies from Eq. 3.35 is

```{math}
:label: eq-p4-ch03-49
V_s-V_n=-\frac{\Delta^2}{V}
```

since $V_n=0$. The total difference of energies is the sum of Eqs. 3.48 and 3.49. Noting that the change of potential energy is just canceled by the first term of Eq. 3.48 We have the following for the condensation energy:

```{math}
:label: eq-p4-ch03-50
W_s-W_n=-\frac{1}{2}N(0)\Delta^2\Bigl[1-e^{-2/N(0)V)}\Bigr]\simeq-\frac{1}{2}N(0)\Delta^2
```

A useful physical understanding of Eq. 3.50 can be derived by taking the energy range of pairing interactions to be $\Delta$ and noting that the number of pairs in this energy range is about $N(0)\Delta$. If $2\Delta$ to be the binding energy of each electron pair, then the product of the number of pairs and the binding energy is approximately the condensation energy. Thus it is clear that although the BCS theory of the ground state has all electrons paired, only those in a narrow energy range of order $\Delta$ participate in the condensation. The electrons below the Fermi level are also described mathematically as pairs but they are too far from the Fermi surface to be scattered by the electron-phonon interaction, and hence do not participate in the reduction of the energy of the system.

## 3.3 Some Quantitative Predictions of BCS

The BCS theory makes a number of quantitative predictions about observables. We summarize results for the critical temperature, energy gap, critical field and specific heat. At present, many of these observables are being measured for the high $T_c$ materials in an attempt to look for deviations from the BCS theoretical predictions. Agreement with the BCS theory may be explained by the existence of pairs, and for this reason may not provide direct information on whether the pairing mechanism is the electron-phonon interaction or is some other attractive pairing mechanism.

### 3.3.1 Critical Temperature

In zero field, ordering sets in at a critical temperature $T_c$ given by

```{math}
:label: eq-p4-ch03-51
k_BT_c=1.13\hbar\omega_De^{-1/N_0V_0}
```

No matter how weak the electron-phonon coupling, BCS predicts a transition to a superconducting state for an attractive interaction described by the attractive potential $V_0$ where $N_0$ is the density of states at the Fermi level and $\omega_D$ is the Debye frequency.

### 3.3.2 Energy Gap

The zero-temperature energy gap is given by

```{math}
:label: eq-p4-ch03-52
\Delta(0)=2\hbar\omega_D e^{-1/N_0V_0}
```

The ratio of Eq. 3.52 to Eq. 3.51 gives a fundamental formula independent of the phenomenological parameters

```{math}
:label: eq-p4-ch03-53
\Delta(0)=1.76k_BT_c.
```

This result seems to hold to within 10% for a large number of superconductors including some of the new high $T_c$ materials, though the results for the high $T_c$ materials must be considered to be preliminary.

The BCS theory also predicts the temperature dependence of the energy gap for $T$ near to $T_c$ as

```{math}
:label: eq-p4-ch03-54
\frac{\Delta(T)}{\Delta(0)}\approx1.74\left(1-\frac{T}{T_c}\right)^{1/2}
```

### 3.3.3 Critical Field

The BCS prediction for $H_c(T)$ is usually expressed in terms of deviations from the empirical law:

```{math}
:label: eq-p4-ch03-55
\frac{H_c(T)}{H_c(0)}\simeq1-\left(\frac{T}{T_c}\right)^2
```

The BCS prediction is that near $T_c$ the relation is linear

```{math}
:label: eq-p4-ch03-56
\frac{H_c(T)}{H_c(0)}\sim1.74\left[1-\left(\frac{T}{T_c}\right)\right]
```

whereas at very low temperatures the prediction is

```{math}
:label: eq-p4-ch03-57
\frac{H_c(T)}{H_c(0)}\sim1-1.06\left(\frac{T}{T_c}\right)^2.
```

:::{figure} images/fig-p4-ch03-4.png
:name: fig-p4-ch03-4
:width: 60%
:align: center
Figure 3.4: The critical field plotted as a deviation from the empirical relation (Eq. 3.55). Measurements are for several metals. The weak-coupling theory of Swihart is shown.
:::

Figure 3.4 shows the deviation from Eq. 3.55 for typical type I superconductors where Al is a weak coupling superconductor while Hg and Pb are strong coupling type I superconductors. The Werthamer-Helfand-Hohenberg (WHH) equation which is also based on the BCS theory

```{math}
:label: eq-p4-ch03-58
H_{c2}(0)=0.7\left.\left(\frac{\partial H_{c2}}{\partial T}\right)\right|_{T_c}T_c
```

relates the value of the upper critical field of a typical type II superconductor $H_{c2}(0)$ to the slope at $T_c$ with no adjustable parameters. The WHH formula (Eq. 3.58) works well for isotropic type II superconductors. The application of WHH theory to anisotropic type II high $T_c$ superconductors is currently under investigation.

### 3.3.4 Specific Heat

BCS predicts a discontinuity at $T_c$ of magnitude

```{math}
:label: eq-p4-ch03-59
\frac{C_s-C_n}{C_n}\biggr\rvert_{T_c}=1.43
```

In zero magnetic field. The BCS theory also predicts the low temperature heat capacity which can be written as

```{math}
:label: eq-p4-ch03-60
\frac{C_s}{\gamma T_c}=1.34\left(\frac{\Delta(0)}{k_BT}\right)^{3/2}e^{-\Delta(0)/k_BT}
```

where $\gamma$ is the coefficient of the linear specific heat. Equation 3.60 shows that the experimental dependence of the specific heat at low temperature gives a direct measure of the superconducting band gap $\Delta$.
