---
title: "6 Electron and Phonon Scattering"
abstract: "The transport properties of solids depend on carrier availability and on their scattering rates. This chapter focuses on the scattering mechanisms that restore a perturbed electronic (and phonon) system to equilibrium: electron–phonon, impurity, defect, boundary, and electron–electron scattering, together with screening effects and their temperature dependence in semiconductors and metals."
---

# 6 Electron and Phonon Scattering

References:

- Kittel, *Introduction to Solid State Physics*, 6th Ed., Wiley, 1986, Appendix C.
- Ashcroft and Mermin, *Solid State Physics*, Holt, Rinehart and Winston, 1976, Chapters 16 and 26.
- Haug, *Theoretical Solid State Physics*, Volume 2, Pergamon 1972, Chapter 4.

## 6.0 Overview

The transport properties of solids depend on the availability of carriers and on their scattering rates. In the previous chapters we focused on the carriers and their generation. In this chapter we focus on the scattering mechanisms. Electron scattering brings an electronic system which has been subjected to external perturbations back to equilibrium. Collisions also alter the momentum of the carriers as the electrons are brought back into equilibrium. Electron collisions can occur through a variety of mechanisms such as electron–phonon, electron–impurity, electron–defect, and electron–electron scattering processes. Electron scattering is handled by the collision term in the Boltzmann equation.

## 6.1 Electron Scattering

In principle, the collision rates can be calculated from scattering theory. To do this we introduce a transition probability $S(\vec{k},\vec{k}')$ for scattering from a state $\vec{k}$ to a state $\vec{k}'$. Since electrons obey the Pauli principle, scattering will occur from an occupied to an unoccupied state. The process of scattering from $\vec{k}$ to $\vec{k}'$ decreases the distribution function $f(\vec{r},\vec{k},t)$ and depends on the probability that $\vec{k}$ is occupied and that $\vec{k}'$ is unoccupied. The process of scattering from $\vec{k}'$ to $\vec{k}$ increases the distribution function $f(\vec{r},\vec{k},t)$ and depends on the probability that state $\vec{k}'$ is occupied and state $\vec{k}$ is unoccupied. We will use the following notation for describing the scattering process:

- $f_k$ is the probability that an electron occupies a state $\vec{k}$
- $[1-f_k]$ is the probability that state $\vec{k}$ is unoccupied
- $S(\vec{k},\vec{k}')$ is the probability per unit time that an electron in state $\vec{k}$ will be scattered to state $\vec{k}'$
- $S(\vec{k}',\vec{k})$ is the probability per unit time that an electron in state $\vec{k}'$ will be scattered back into state $\vec{k}$.

Using these definitions, the rate of change in the distribution function in the Boltzmann equation (see {eq}`eq-p1-ch04-4`) due to collisions can be written as:

```{math}
:label: eq-p1-ch06-1
\left(\frac{\partial f(\vec{r},\vec{k},t)}{\partial t}\right)_{\text{collisions}}
= \int d^3k'\,\bigl[f_{k'}(1-f_k)S(\vec{k}',\vec{k})
- f_k(1-f_{k'})S(\vec{k},\vec{k}')\bigr]
```

where $d^3k'$ is a volume element in $\vec{k}'$ space. The integration in {eq}`eq-p1-ch06-1` is over $\vec{k}$ space and the spherical coordinate system is shown in {numref}`fig-p1-ch06-1`, together with the arbitrary force $\vec{F}$ responsible for the scattering event that introduces a perturbation described by

```{math}
:label: eq-p1-ch06-2
f_{\vec{k}} = f_{0\vec{k}} + \frac{\partial f_{0\vec{k}}}{\partial E}\,
\hbar\frac{\vec{k}}{m^*}\cdot\vec{F} + \cdots
```

Using Fermi's Golden Rule for the transition probability per unit time between states $\vec{k}$ and $\vec{k}'$ we can write

```{math}
:label: eq-p1-ch06-3
S(\vec{k},\vec{k}') \simeq \frac{2\pi}{\hbar}\,
|H_{\vec{k}\vec{k}'}|^2\Bigl\{\delta[E(\vec{k})]-\delta[E(\vec{k}')]\Bigr\}
```

where the matrix element of the Hamiltonian coupling states $\vec{k}$ and $\vec{k}'$ is

```{math}
:label: eq-p1-ch06-4
H_{\vec{k}\vec{k}'} = \frac{1}{N}\int_V \psi_{\vec{k}}^*(\vec{r})\,\nabla V\,\psi_{\vec{k}'}(\vec{r})\,d^3r
```

in which $N$ is the number of unit cells in the sample and $\nabla V$ is the perturbation Hamiltonian responsible for the scattering event associated with the force $\vec{F}$.

:::{figure} images/fig-p1-ch06-1.png
:name: fig-p1-ch06-1
:align: center
:width: 70%

Spherical coordinate system in reciprocal space for an electron with wavevector $\vec{k}$ (along the $k_z$ axis) scattering into a state with wavevector $\vec{k}'$ in an arbitrary force field $\vec{F}$. The scattering center is at the origin. For simplicity the event is rotated so that $\vec{F}$ has no $k_y$ component.
:::

At equilibrium $f_k = f_0(E)$ and the principle of detailed balance applies

```{math}
:label: eq-p1-ch06-5
S(\vec{k}',\vec{k})\,f_0(E')[1-f_0(E)]
= S(\vec{k},\vec{k}')\,f_0(E)[1-f_0(E')]
```

so that the distribution function does not experience a net change via collisions when in the equilibrium state

```{math}
:label: eq-p1-ch06-6
\left.\frac{\partial f(\vec{r},\vec{k},t)}{\partial t}\right|_{\text{collisions}} = 0 .
```

We define collisions as elastic when $E(\vec{k}') = E(\vec{k})$ and in this case $f_0(E') = f_0(E)$ so that $S(\vec{k}',\vec{k}) = S(\vec{k},\vec{k}')$. Collisions for which $E(\vec{k}')\neq E(\vec{k})$ are termed inelastic. The term quasi-elastic is used to characterize collisions where the percentage change in energy is small. For our purposes here, we shall consider $S(\vec{k},\vec{k}')$ as a known function which can be calculated quantum mechanically by a detailed consideration of the scattering mechanisms which are important for a given practical case; this statement is true in principle, but in practice $S(\vec{k},\vec{k}')$ is usually specified in an approximate way.

The return to equilibrium depends on the frequency of collisions and the effectiveness of a scattering event in randomizing the motion of the electrons. Thus, small angle scattering is not as effective in restoring a system to equilibrium as large angle scattering. For this reason we distinguish between $\tau_D$, the time for the system to be restored to equilibrium, and $\tau_c$, the time between collisions. These times are related by

```{math}
:label: eq-p1-ch06-7
\tau_D = \frac{\tau_c}{1-\cos\theta}
```

where $\theta$ is the mean change of angle of the electron velocity on collision (see {numref}`fig-p1-ch06-1`). The time $\tau_D$ is the quantity which enters into Boltzmann's equation while $1/\tau_c$ determines the actual scattering rate.

The mean free time between collisions, $\tau_c$, is related to several other quantities of interest: the mean free path $\ell_f$, the scattering cross section $\sigma_d$, and the concentration of scattering centers $N_c$ by

```{math}
:label: eq-p1-ch06-8
\tau_c = \frac{1}{N_c\sigma_d v}
```

where $v$ is the drift velocity given by

```{math}
:label: eq-p1-ch06-9
v = \frac{\ell_f}{\tau_c}
= \frac{1}{N_c\sigma_d\tau_c}
```

and $v$ is in the direction of the electron transport. From {eq}`eq-p1-ch06-9` we see that $\ell_f = 1/N_c\sigma_d$. The drift velocity is of course very much smaller in magnitude than the instantaneous velocity of the electron at the Fermi level, which is typically of magnitude $v_F\sim 10^8$ cm/sec. Electron scattering centers include phonons, impurities, dislocations, the crystal surface, etc.

The most important electron scattering mechanism for both metals and semiconductors is electron–phonon scattering (scattering of electrons by the thermal motion of the lattice), though the scattering process for metals differs in detail from that in semiconductors. In the case of metals, much of the Brillouin zone is occupied by electrons, while in the case of semiconductors, most of the Brillouin zone is unoccupied and represents states into which electrons can be scattered. In the case of metals, electrons are scattered from one point on the Fermi surface to another point, and a large change in momentum occurs, corresponding to a large change in $\vec{k}$. In the case of semiconductors, changes in wave vector from $\vec{k}$ to $-\vec{k}$ normally correspond to a very small change in wave vector, and thus changes from $\vec{k}$ to $-\vec{k}$ can be accomplished much more easily in the case of semiconductors. By the same token, small angle scattering (which is not so efficient for returning the system to equilibrium) is especially important for semiconductors where the change in wavevector is small. Since the scattering processes in semiconductors and metals are quite different, they will be discussed separately below.

Scattering probabilities for more than one scattering process are taken to be additive and therefore so are the reciprocal scattering times or scattering rates:

```{math}
:label: eq-p1-ch06-10
\left(\frac{1}{\tau}\right)_{\text{total}} = \sum_i \frac{1}{\tau_i}
```

since $1/\tau$ is proportional to the scattering probability. Metals have large Fermi wavevectors $k_F$, and therefore large momentum transfers $\Delta k$ can occur as a result of electronic collisions. In contrast, for semiconductors, $k_F$ is small and so also is $\Delta k$ on collision.

## 6.2 Scattering Processes in Semiconductors

### 6.2.1 Electron–Phonon Scattering

Electron–phonon scattering is the dominant scattering mechanism in crystalline semiconductors except at very low temperatures. Conservation of energy in the scattering process, which creates or absorbs a phonon of energy $\hbar\omega(\vec{q})$, is written as:

```{math}
:label: eq-p1-ch06-11
E_i - E_f = \pm\hbar\omega(\vec{q})
= \frac{\hbar^2}{2m^*}(k_i^2 - k_f^2)
```

where $E_i$ is the initial energy, $E_f$ is the final energy, $k_i$ the initial wavevector, and $k_f$ the final wavevector. Here, the "$+$" sign corresponds to the creation of phonons (the phonon emission process), while the "$-$" sign corresponds to the absorption of phonons. Conservation of momentum in the scattering by a phonon of wavevector $\vec{q}$ yields

```{math}
:label: eq-p1-ch06-12
\vec{k}_i - \vec{k}_f = \pm\vec{q} .
```

For semiconductors, the electrons involved in the scattering event generally remain in the vicinity of a single band extremum and involve only a small change in $\vec{k}$ and hence only low phonon $\vec{q}$ vectors participate. The probability that an electron makes a transition from an initial state $i$ to a final state $f$ is proportional to:

(a) the availability of final states for electrons,
(b) the probability of absorbing or emitting a phonon,
(c) the strength of the electron–phonon coupling or interaction.

The first factor, the availability of final states, is proportional to the density of final electron states $\rho(E_f)$ times the probability that the final state is unoccupied. (This occupation probability for a semiconductor is assumed to be unity since the conduction band is essentially empty.) For a simple parabolic band $\rho(E_f)$ is (from {eq}`eq-p1-ch04-64`):

```{math}
:label: eq-p1-ch06-13
\rho(E_f) = \frac{(2m^*)^{3/2}E_f^{1/2}}{2\pi^2\hbar^3}
= \frac{(2m^*)^{3/2}[E_i\pm\hbar\omega(\vec{q})]^{1/2}}{2\pi^2\hbar^3} ,
```

where {eq}`eq-p1-ch06-11` has been employed and the "$+$" sign corresponds to absorption of a phonon and the "$-$" sign corresponds to phonon emission.

The probability of absorbing or emitting a phonon is proportional to the electron–phonon coupling $G(\vec{q})$ and to the phonon density $n(\vec{q})$ for absorption, and $[1+n(\vec{q})]$ for emission, where $n(\vec{q})$ is given by the Bose–Einstein factor

```{math}
:label: eq-p1-ch06-14
n(\vec{q}) = \frac{1}{e^{\hbar\omega(\vec{q})/k_BT}-1} .
```

Combining the terms in {eq}`eq-p1-ch06-13` and {eq}`eq-p1-ch06-14` gives a scattering probability (or $1/\tau_c$) proportional to a sum over final states

```{math}
:label: eq-p1-ch06-15
\frac{1}{\tau_c} \sim \frac{(2m^*)^{3/2}}{2\pi^2\hbar^3}
\sum_{\vec{q}} G(\vec{q})
\left[
\frac{[E_i+\hbar\omega(\vec{q})]^{1/2}}{e^{\hbar\omega(\vec{q})/k_BT}-1}
+
\frac{[E_i-\hbar\omega(\vec{q})]^{1/2}}{1-e^{-\hbar\omega(\vec{q})/k_BT}}
\right]
```

where the first term in the big bracket of {eq}`eq-p1-ch06-15` corresponds to phonon absorption and the second term to phonon emission. If $E_i < \hbar\omega(\vec{q})$, only the phonon absorption process is energetically allowed.

The electron–phonon coupling coefficient $G(\vec{q})$ in {eq}`eq-p1-ch06-15` depends on the electron–phonon coupling mechanism. There are three important coupling mechanisms in semiconductors which we briefly describe below: electromagnetic coupling, piezoelectric coupling, and deformation–potential coupling.

Electromagnetic coupling is important only for semiconductors where the charge distribution has different signs on neighboring ion sites. In this case, the oscillatory electric field can give rise to oscillating dipole moments associated with the motion of neighboring ion sites in the optical modes (see {numref}`fig-p1-ch06-2`). The electromagnetic coupling mechanism is important in coupling electrons to optical phonon modes in III–V and II–VI compound semiconductors, but does not contribute in the case of silicon. To describe the optical modes we can use the Einstein approximation, since $\omega(\vec{q})$ is only weakly dependent on $\vec{q}$ for the optical modes of frequency $\omega_0$. In this case $\hbar\omega_0 \gg k_BT$ and $\hbar\omega_0 \gg E$ where $E$ is the electron energy, so that from {eq}`eq-p1-ch06-15` the collision rate is proportional to

```{math}
:label: eq-p1-ch06-16
\frac{1}{\tau_c} \sim \frac{m^{*3/2}(\hbar\omega_0)^{1/2}}{e^{\hbar\omega_0/k_BT}-1} .
```

Thus, the collision rate depends on the temperature $T$, the optical phonon frequency $\omega_0$ and the electron effective mass $m^*$. The corresponding mobility for the optical phonon scattering is

```{math}
:label: eq-p1-ch06-17
\mu = \frac{e\langle\tau\rangle}{m^*}
\sim \frac{e\,(e^{\hbar\omega_0/k_BT}-1)}{m^{*5/2}(\hbar\omega_0)^{1/2}}
```

Thus for optical phonon scattering, the mobility $\mu$ is independent of the electron energy $E$ and decreases with increasing temperature.

:::{figure} images/fig-p1-ch06-2.png
:name: fig-p1-ch06-2
:align: center
:width: 80%

Displacements $\vec{u}(\vec{r})$ of a diatomic chain of atoms for longitudinal optical (LO) and transverse optical (TO) phonons at (a) the center and (b) the edge of the Brillouin zone. The lighter mass atoms are indicated by open circles. For zone edge optical phonons, only the lighter atoms are displaced.
:::

As in the case of electromagnetic coupling, piezoelectric coupling is important in semiconductors which are ionic or partly ionic. If these crystals lack inversion symmetry, then acoustic mode vibrations generate regions of compression and rarefaction in a crystal which lead to electric fields (see {numref}`fig-p1-ch06-3`). The piezoelectric scattering mechanism is thus associated with the coupling between electrons and phonons arising from these electromagnetic fields.

:::{figure} images/fig-p1-ch06-3.png
:name: fig-p1-ch06-3
:align: center
:width: 80%

Displacements $\vec{u}(\vec{r})$ of a diatomic chain of atoms for longitudinal acoustic (LA) and transverse acoustic (TA) phonons at (a) the center and (b) the edge of the Brillouin zone. The lighter mass atoms are indicated by open circles. For zone edge acoustic phonons, only the heavier atoms are displaced.
:::

The zincblende structure of the III–V compounds (e.g., GaAs) lacks inversion symmetry. In this case the perturbation potential is given by

```{math}
:label: eq-p1-ch06-18
\Delta V(\vec{r},t) = -i e\,\varepsilon_{pz}\,\vec{u}(\vec{r},t)\cdot\bigl(\nabla\cdot\vec{u}(\vec{r},t)\bigr)
```

where $\varepsilon_{pz}$ is the piezoelectric coefficient and $\vec{u}(\vec{r},t)=u\exp(i\vec{q}\cdot\vec{r}-\omega t)$ is the displacement during a normal mode oscillation. Note that the phase of $\Delta V(\vec{r},t)$ in piezoelectric coupling is shifted by $\pi/2$ relative to the case of electromagnetic coupling.

The deformation–potential coupling mechanism is associated with energy shifts of the energy band extrema caused by the compression and rarefaction of crystals during acoustic mode vibrations. The deformation potential scattering mechanism is important in crystals like silicon which have inversion symmetry (and hence no piezoelectric scattering coupling) and have the same species on each site (and hence no electromagnetic coupling). The longitudinal acoustic modes are important for phonon coupling in n–type Si and Ge where the conduction band minima occur away from $\vec{k}=0$.

For deformation potential coupling, it is the LA acoustical phonons that are most important, though contributions by LO optical phonons still make some contribution. For the acoustic phonons, we have the condition $\hbar\omega\ll k_BT$ and $\hbar\omega\ll E$, while for the optical phonons it is usually the case that $\hbar\omega\gg k_BT$ at room temperature. For the range of acoustic phonon modes of interest, $G(\vec{q})\sim q$, where $q$ is the phonon wave vector and $\omega\sim q v_q$ for acoustic phonons. Furthermore for the LA phonon branch the phonon absorption process will depend on $n(q)$ in accordance with the Bose factor

```{math}
:label: eq-p1-ch06-19
\frac{1}{e^{\hbar\omega/k_BT}-1}
\simeq \frac{1}{[1+(\hbar\omega/k_BT+\cdots)-1]}
\sim \frac{k_BT}{\hbar\omega}
\sim \frac{k_BT}{q\,v_q} ,
```

while for phonon emission

```{math}
:label: eq-p1-ch06-20
\frac{1}{1-e^{-\hbar\omega/k_BT}}
\simeq \frac{1}{1-[1-(\hbar\omega/k_BT+\cdots)]}
\sim \frac{k_BT}{\hbar\omega}
\sim \frac{k_BT}{q\,v_q} .
```

Therefore, in considering both phonon absorption and phonon emission, the factors $G(\vec{q})[e^{\hbar\omega/k_BT}-1]^{-1}$ and $G(\vec{q})[1-e^{-\hbar\omega/k_BT}]^{-1}$ are independent of $q$ for the LA branch. Consequently for the acoustic phonon scattering process, the carrier mobility $\mu$ decreases with increasing $T$ according to (see {eq}`eq-p1-ch06-15`)

```{math}
:label: eq-p1-ch06-21
\mu = \frac{e\langle\tau\rangle}{m^*}
\sim m^{*-5/2} E^{-1/2} (k_BT)^{-1} .
```

For the optical LO contribution, we have $G(\vec{q})$ independent of $\vec{q}$ but an $E^{1/2}$ factor is introduced by {eq}`eq-p1-ch06-15` for both phonon absorption and emission, leading to the same basic dependence as given by {eq}`eq-p1-ch06-21`. Thus, we find that the temperature and energy dependence of the mobility $\mu$ is different for the various electron–phonon coupling mechanisms. These differences in the $E$ and $T$ dependences can thus be used to identify which scattering mechanism is dominant in specific semiconducting samples. Furthermore, when explicit account is taken of the energy dependence of $\tau$, departures from the strict Drude model $\sigma = ne^2\tau/m^*$ can be expected.

### 6.2.2 Ionized Impurity Scattering

As the temperature is reduced, phonon scattering becomes less important so that in this regime, ionized impurity scattering and other defect scattering mechanisms can become dominant. Ionized impurity scattering can also be important in heavily doped semiconductors over a wider temperature range because of the larger defect density. This scattering mechanism involves the deflection of an electron with velocity $v$ by the Coulomb field of an ion with charge $Ze$, as modified by the dielectric constant $\varepsilon$ of the medium and by the screening of the impurity ion by free electrons (see {numref}`fig-p1-ch06-4`). Most electrons are scattered through small angles as they are scattered by ionized impurities. The perturbation potential is given by

```{math}
:label: eq-p1-ch06-22
\Delta V(\vec{r}) = \pm\frac{Z e^2}{4\pi\varepsilon_0 r}
```

and the $\pm$ signs denote the different scattering trajectories for electrons and holes (see {numref}`fig-p1-ch06-4`). In {eq}`eq-p1-ch06-22` the screening of the electron by the semiconductor environment is handled by the static dielectric constant of the semiconductor $\varepsilon_0$. Because of the long–range nature of the Coulomb interaction, screening by other free carriers and by other ionized impurities could be important. Such screening effects are further discussed in §6.2.4.

:::{figure} images/fig-p1-ch06-4.png
:name: fig-p1-ch06-4
:align: center
:width: 70%

Trajectories of electrons and holes in ionized impurity scattering. The scattering center is at the origin.
:::

The scattering rate $1/\tau_I$ due to ionized impurity scattering is given to a good approximation by the Conwell–Weisskopf formula

```{math}
:label: eq-p1-ch06-23
\frac{1}{\tau_I} \sim \frac{Z^2 N_I}{m^{*1/2}E^{3/2}}
\ln\!\left[\left(1+\frac{4\pi\varepsilon E}{Z e^2 N_I^{1/3}}\right)^2\right]
```

in which $N_I$ is the ionized charged impurity density. The Conwell–Weisskopf formula works quite well for heavily doped semiconductors. We note here that $\tau_I\sim E^{3/2}$, so that it is the low energy electrons that are most affected by ionized impurity scattering (see {numref}`fig-p1-ch04-10`).

Neutral impurities also introduce a scattering potential, but it is much weaker than that for the ionized impurity. Free carriers can polarize a neutral impurity and interact with the resulting dipole moment, or can undergo an exchange interaction. In the case of neutral impurity scattering, the perturbation potential is given by

```{math}
:label: eq-p1-ch06-24
\Delta V(\vec{r}) \simeq \frac{\hbar^2}{m^*}\left(\frac{r_B}{r^5}\right)^{1/2}
```

where $r_B$ is the ground state Bohr radius of the electron in a doped semiconductor and $r$ is the distance of the electron to the impurity scattering center.

### 6.2.3 Other Scattering Mechanisms

Other scattering mechanisms in semiconductors include:

(a) neutral impurity centers — these make contributions at very low temperatures, and are mentioned in §6.2.2.
(b) dislocations — these defects give rise to anisotropic scattering at low temperatures.
(c) boundary scattering by crystal surfaces — this scattering becomes increasingly important the smaller the crystal size. Boundary scattering can become a dominant scattering mechanism in nanostructures (e.g., quantum wells, quantum wires and quantum dots), when the sample size in the confinement direction is smaller than the bulk mean free path.
(d) intervalley scattering from one equivalent conduction band minimum to another. This scattering process requires a phonon with large $q$ and consequently results in a relatively large energy transfer.
(e) electron–electron scattering – similar to charged impurity scattering in being dominated by a Coulomb scattering mechanism, except that spin effects become important. This mechanism can be important in distributing energy and momentum among the electrons in the solid and thus can act in conjunction with other scattering mechanisms in establishing equilibrium.
(f) electron–hole scattering — depends on having both electrons and holes present. Because the electron and hole motions induced by an applied electric field are in opposite directions, electron–hole scattering tends to reverse the direction of the incident electrons and holes. Radiative recombination, i.e., electron–hole recombination with the emission of a photon, must also be considered.

### 6.2.4 Screening Effects in Semiconductors

In the vicinity of a charged impurity or an acoustic phonon, charge carriers are accumulated or depleted by the scattering potential, giving rise to a charge density

```{math}
:label: eq-p1-ch06-25
\rho(\vec{r}) = e\bigl[n(\vec{r})-p(\vec{r})+N_a^-(\vec{r})-N_d^+(\vec{r})\bigr]
= e\,n^*(\vec{r})
```

where $n(\vec{r})$, $p(\vec{r})$, $N_a^-(\vec{r})$, $N_d^+(\vec{r})$, and $n^*(\vec{r})$ are, respectively, the electron, hole, ionized acceptor, ionized donor, and effective total carrier concentrations as a function of distance $r$ to the scatterer. We can then write expressions for these quantities in terms of their excess charge above the uniform potential in the absence of the charge perturbation

```{math}
:label: eq-p1-ch06-26
n(\vec{r}) = n + \delta n(\vec{r}),\qquad
N_d^+(\vec{r}) = N_d^+ + \delta N_d^+(\vec{r}) ,
```

and similarly for the holes and acceptors. The space charge $\rho(\vec{r})$ is related to the perturbing potential by Poisson's equation

```{math}
:label: eq-p1-ch06-27
\nabla^2\varphi(\vec{r}) = -\frac{\rho(\vec{r})}{\varepsilon_0} .
```

Approximate relations for the excess concentrations are

```{math}
:label: eq-p1-ch06-28
\frac{\delta n(\vec{r})}{n} \simeq -\frac{e\varphi(\vec{r})}{k_BT},\qquad
\frac{\delta N_d^+(\vec{r})}{N_d^+} \simeq \frac{e\varphi(\vec{r})}{k_BT}
```

and similar relations for the holes. Substitution of {eq}`eq-p1-ch06-25` into {eq}`eq-p1-ch06-26` and {eq}`eq-p1-ch06-28` yield

```{math}
:label: eq-p1-ch06-29
\nabla^2\varphi(\vec{r}) = -\frac{n^* e^2}{\varepsilon_0 k_BT}\,\varphi(\vec{r}) .
```

We define an effective Debye screening length $\lambda$ such that

```{math}
:label: eq-p1-ch06-30
\lambda^2 = \frac{\varepsilon_0 k_BT}{n^* e^2} .
```

For a spherically symmetric potential {eq}`eq-p1-ch06-29` becomes

```{math}
:label: eq-p1-ch06-31
\frac{d^2}{dr^2}\left[r\varphi(r)\right] = \frac{r\varphi(r)}{\lambda^2}
```

which yields a solution

```{math}
:label: eq-p1-ch06-32
\varphi(r) = \frac{Z e^2}{4\pi\varepsilon_0 r}\,e^{-r/\lambda} .
```

Thus, the screening effect produces an exponential decay of the scattering potential $\varphi(r)$ with a characteristic length $\lambda$ that depends through {eq}`eq-p1-ch06-30` on the effective electron concentration. When the concentration gets large, $\lambda$ decreases and screening becomes more effective.

When applying screening effects to the ionized impurity scattering problem, we Fourier expand the scattering potential to take advantage of the overall periodicity of the lattice

```{math}
:label: eq-p1-ch06-33
\Delta V(\vec{r}) = \sum_{\vec{G}} A_{\vec{G}}\,e^{i\vec{G}\cdot\vec{r}}
```

where the Fourier coefficients are given by

```{math}
:label: eq-p1-ch06-34
A_{\vec{G}} = \frac{1}{V}\int_V \nabla V(\vec{r})\,e^{-i\vec{G}\cdot\vec{r}}\,d^3r
```

and the matrix element of the perturbation Hamiltonian in {eq}`eq-p1-ch06-4` becomes

```{math}
:label: eq-p1-ch06-35
H_{\vec{k},\vec{k}'} = \frac{1}{N}\sum_{\vec{G}}\int_V
e^{-i\vec{k}\cdot\vec{r}} u_{\vec{k}}^*(\vec{r})\,
A_{\vec{G}} e^{-i\vec{G}\cdot\vec{r}} e^{i\vec{k}'\cdot\vec{r}} u_{\vec{k}'}(\vec{r})\,d^3r .
```

We note that the integral in {eq}`eq-p1-ch06-35` vanishes unless $\vec{k}-\vec{k}'=\vec{G}$ so that

```{math}
:label: eq-p1-ch06-36
H_{\vec{k},\vec{k}'} = \frac{A_{\vec{k}-\vec{k}'}}{N}
\int_V u_{\vec{k}}^*(\vec{r})\,u_{\vec{k}'}(\vec{r})\,d^3r
```

within the first Brillouin zone so that for parabolic bands $u_{\vec{k}}(\vec{r})=u_{\vec{k}'}(\vec{r})$ and

```{math}
:label: eq-p1-ch06-37
H_{\vec{k},\vec{k}'} = \frac{A_{\vec{k}-\vec{k}'}}{N} .
```

Now substituting for the scattering potential in {eq}`eq-p1-ch06-34` we obtain

```{math}
:label: eq-p1-ch06-38
A_{\vec{G}} = \frac{Z e^2}{4\pi\varepsilon_0 V}
\int_V e^{-i\vec{G}\cdot\vec{r}}\,d^3r
```

where $d^3r = r^2\sin\theta\,d\theta\,d\varphi\,dr$ so that, for $\varphi(r)$ depending only on $r$, the angular integration gives $4\pi$ and the spatial integration gives

```{math}
:label: eq-p1-ch06-39
A_{\vec{G}} = \frac{Z e^2}{\varepsilon_0 V\,|\vec{G}|^2}
```

and

```{math}
:label: eq-p1-ch06-40
H_{\vec{k},\vec{k}'} = \frac{Z e^2}{\varepsilon_0 V\,|\vec{k}-\vec{k}'|^2} .
```

Equations {eq}`eq-p1-ch06-39` and {eq}`eq-p1-ch06-40` are for the scattering potential without screening. When screening is included in considering the ionized impurity scattering mechanism, the integration becomes

```{math}
:label: eq-p1-ch06-41
A_{\vec{G}} = \frac{Z e^2}{4\pi\varepsilon_0 V}
\int_V e^{-r/\lambda}e^{-i\vec{G}\cdot\vec{r}}\,d^3r
= \frac{Z e^2}{\varepsilon_0 V\,\bigl(|\vec{G}|^2 + |1/\lambda|^2\bigr)}
```

and

```{math}
:label: eq-p1-ch06-42
H_{\vec{k},\vec{k}'} = \frac{Z e^2}{\varepsilon_0 V\,\bigl(|\vec{k}-\vec{k}'|^2 + |1/\lambda|^2\bigr)}
```

so that screening clearly reduces the scattering due to ionized impurity scattering. The discussion given here also extends to the case of scattering in metals, which is treated below.

Combining the various scattering mechanisms discussed above for semiconductors, the picture given by {numref}`fig-p1-ch06-5` emerges. Here we see the temperature dependence of each of the important scattering mechanisms and the effect of each of these processes on the carrier mobility. Here it is seen that screening effects are important for carrier mobilities at low temperature.

:::{figure} images/fig-p1-ch06-5.png
:name: fig-p1-ch06-5
:align: center
:width: 80%

Typical temperature dependence of the carrier mobility in semiconductors, showing the effect of the dominant scattering mechanisms and the temperature dependence of each.
:::

## 6.3 Electron Scattering in Metals

Basically the same scattering mechanisms are present in metals as in semiconductors, but because of the large number of occupied states in the conduction bands of metals, the temperature dependences of the various scattering mechanisms are quite different.

### 6.3.1 Electron–Phonon Scattering

For a review of phonons in the harmonic oscillator approximation see Appendix C. In metals as in semiconductors, the dominant scattering mechanism is usually electron–phonon scattering. In the case of metals, electron scattering is mainly associated with an electromagnetic interaction of ions with nearby electrons, the longer range interactions being screened by the numerous mobile electrons. For metals, we must therefore consider explicitly the probability that a state $\vec{k}$ is occupied $f_0(\vec{k})$ or unoccupied $[1-f_0(\vec{k})]$. The scattering rate is found by explicit consideration of the scattering rate into a state $\vec{k}$ and the scattering out of that state. Using the same arguments as in §6.2.1, the collision term in Boltzmann's equation is given by

```{math}
:label: eq-p1-ch06-43
\left(\frac{\partial f}{\partial t}\right)_{\text{collisions}}
\sim \frac{1}{\tau}\sum_{\vec{q}} G(\vec{q})\,
\Biggl\{
\underbrace{[1-f_0(\vec{k})]\, f_0(\vec{k}-\vec{q})\, n(\vec{q})
+ f_0(\vec{k}+\vec{q})\,[1+n(\vec{q})]}_{\text{scattering into }\vec{k}}
-
\underbrace{[f_0(\vec{k})]\,[1-f_0(\vec{k}+\vec{q})]\, n(\vec{q})
+ [1-f_0(\vec{k}-\vec{q})]\,[1+n(\vec{q})]}_{\text{scattering out of }\vec{k}}
\Biggr\}
```

Here the first term in {eq}`eq-p1-ch06-43` is associated with scattering electrons into an element of phase space at $\vec{k}$ with a probability given by $[1-f_0(\vec{k})]$ that state $\vec{k}$ is unoccupied and has contributions from both phonon absorption processes and phonon emission processes. The second term arises from electrons scattered out of state $\vec{k}$ and here, too, there are contributions from both phonon absorption processes and phonon emission processes. The equilibrium distribution function $f_0(\vec{k})$ for the electron is the Fermi distribution function while the function $n(\vec{q})$ for the phonons is the Bose distribution function ({eq}`eq-p1-ch06-14`). Phonon absorption depends on the phonon density $n(\vec{q})$, while phonon emission depends on the factor $\{1+n(\vec{q})\}$. These factors arise from the properties of the creation and annihilation operators for phonons (to be reviewed in recitation). The density of final states for metals is the density of states at the Fermi level which is consequently approximately independent of energy and temperature. The condition that, in metals, electron scattering takes place to states near the Fermi level implies that the largest phonon wave vector in an electron collision is $2k_F$ where $k_F$ is the electron wave vector at the Fermi surface.

:::{figure} images/fig-p1-ch06-6.png
:name: fig-p1-ch06-6
:align: center
:width: 80%

Universal curve of the temperature dependence of the ideal resistivity of various metals normalized to the value at the Debye temperature as a function of the dimensionless temperature $T/\Theta_D$.
:::

Of particular interest is the temperature dependence of the phonon scattering mechanism in the limit of low and high temperatures. Experimentally, the temperature dependence of the resistivity of metals can be plotted on a universal curve (see {numref}`fig-p1-ch06-6`) in terms of $\rho_T/\rho_{\Theta_D}$ vs. $T/\Theta_D$ where $\Theta_D$ is the Debye temperature. This plot includes data for several metals, and values for the Debye temperature of these metals are given with the figure. In accordance with the plot in {numref}`fig-p1-ch06-6`, $T\ll\Theta_D$ defines the low temperature limit and $T\gg\Theta_D$ the high temperature limit. Except for the very low temperature defect scattering limit, the electron–phonon scattering mechanism dominates, and the temperature dependence of the scattering rate depends on the product of the density of phonon states and the phonon occupation, since the electron–phonon coupling coefficient is essentially independent of $T$. The phonon concentration in the high temperature limit becomes

```{math}
:label: eq-p1-ch06-44
n(\vec{q}) = \frac{1}{\exp(\hbar\omega/k_BT)-1}
\approx \frac{k_BT}{\hbar\omega}
```

since $(\hbar\omega/k_BT)\ll 1$, so that from {eq}`eq-p1-ch06-44` we have $1/\tau\sim T$ and $\sigma = ne\mu\sim T^{-1}$. In this high temperature limit, the scattering is quasi–elastic and involves large–angle scattering, since phonon wave vectors up to the Debye wave vector $q_D$ are involved in the electron scattering, where $q_D$ is related to the Debye frequency $\omega_D$ and to the Debye temperature $\Theta_D$ according to

```{math}
:label: eq-p1-ch06-45
\hbar\omega_D = k_B\Theta_D = \hbar q_D v_q
```

where $v_q$ is the velocity of sound. We can interpret $q_D$ as the radius of a Debye sphere in $\vec{k}$–space which defines the range of accessible $\vec{q}$ vectors for scattering, i.e., $0<q<q_D$. The magnitude of $q_D$ is comparable to the Brillouin zone dimensions but the energy change of an electron ($\Delta E$) on scattering by a phonon will be less than $k_B\Theta_D\lesssim 1/40$ eV so that the restriction of $(\Delta E)_{\text{max}}\lesssim k_B\Theta_D$ implies that the maximum electronic energy change on scattering will be small compared with the Fermi energy $E_F$. We thus obtain that for $T>\Theta_D$ (the high temperature regime), $\Delta E < k_BT$ and the scattering will be quasi–elastic as illustrated in {numref}`fig-p1-ch06-7`(a). In the opposite limit, $T\ll\Theta_D$, we have $\hbar\omega_q\ll k_BT$ (because only low frequency acoustic phonons are available for scattering) and in the low temperature limit there is the possibility that $\Delta E > k_BT$, which implies inelastic scattering. In the low temperature limit, $T\ll\Theta_D$, the scattering is also small–angle scattering, since only low energy (low $q$ wave vector) phonons are available for scattering (as illustrated in {numref}`fig-p1-ch06-7`(b)).

:::{figure} images/fig-p1-ch06-7.png
:name: fig-p1-ch06-7
:align: center
:width: 80%

(a) Scattering of electrons on the Fermi surface of a metal. Large angle scattering dominates at high temperature ($T>\Theta_D$) and this regime is called the "quasi–elastic" limit. (b) Small angle scattering is important at low temperature ($T<\Theta_D$) and is in general an inelastic scattering process.
:::

At low temperature, the phonon density contributes a factor of $T^3$ to the scattering rate ({eq}`eq-p1-ch06-43`) when the sum over phonon states is converted to an integral and $q^2dq$ is written in terms of the dimensionless variable $\hbar\omega_q/k_BT$ with $\omega = v_q q$. Since small momentum transfer gives rise to small angle scattering, the diagram in {numref}`fig-p1-ch06-8` involves {eq}`eq-p1-ch06-7`. Because of the small energy transfer we can write,

```{math}
:label: eq-p1-ch06-46
|\vec{k}_i-\vec{k}_f| \sim k_f(1-\cos\theta)
\approx \frac{1}{2}k_f\theta^2
\approx \frac{1}{2}k_f\left(\frac{q}{k_f}\right)^2
```

:::{figure} images/fig-p1-ch06-8.png
:name: fig-p1-ch06-8
:align: center
:width: 60%

Geometry of the scattering process, where $\theta$ is the scattering angle between the incident and scattered electron wave vectors $\vec{k}_i$ and $\vec{k}_f$, respectively, and $\vec{q}$ is the phonon wave vector.
:::

so that another factor of $q^2$ appears in the integration over $\vec{q}$ when calculating $(1/\tau_D)$. Thus, the electron scattering rate at low temperature is predicted to be proportional to $T^5$ so that $\sigma\sim T^{-5}$ (Bloch–Grüneisen formula). Thus, when phonon scattering is the dominant scattering mechanism in metals, the following results are obtained:

```{math}
:label: eq-p1-ch06-47
\sigma \sim \frac{\Theta_D}{T},\qquad T\gg\Theta_D
```

```{math}
:label: eq-p1-ch06-48
\sigma \sim \left(\frac{\Theta_D}{T}\right)^5,\qquad T\ll\Theta_D
```

In practice, the resistivity of metals at very low temperatures is dominated by other scattering mechanisms, such as impurities, boundary scattering, etc., and at very low $T$ electron–phonon scattering (see {eq}`eq-p1-ch06-48`) is relatively unimportant.

The possibility of umklapp processes further increases the range of phonon modes that can contribute to electron scattering in electron–phonon scattering processes. In an umklapp process, a non–vanishing reciprocal lattice vector can be involved in the momentum conservation relation, as shown in the schematic diagram of {numref}`fig-p1-ch06-9`. In this diagram, the relation between the wave vectors for the phonon and for the incident and scattered electrons $\vec{G} = \vec{k}+\vec{q}+\vec{k}'$ is shown when crystal momentum is conserved for a non–vanishing reciprocal lattice vector $\vec{G}$. Thus, phonons involved in an umklapp process have large wave vectors with magnitudes of about $1/3$ of the Brillouin zone dimensions. Therefore, substantial energies can be transferred on collision through an umklapp process. At low temperatures, normal scattering processes (i.e., normal as distinguished from umklapp processes) play an important part in completing the return to equilibrium of an excited electron in a metal, while at high temperatures, umklapp processes become more important.

:::{figure} images/fig-p1-ch06-9.png
:name: fig-p1-ch06-9
:align: center
:width: 70%

Schematic diagram showing the relation between the phonon wave vector $\vec{q}$ and the electron wave vectors $\vec{k}$ and $\vec{k}'$ in two Brillouin zones separated by the reciprocal lattice vector $\vec{G}$ (umklapp process).
:::

The discussion presented up to this point is applicable to the creation or absorption of a single phonon in a particular scattering event. Since the restoring forces for lattice vibrations in solids are not strictly harmonic, anharmonic corrections to the restoring forces give rise to multiphonon processes where more than one phonon can be created or annihilated in a single scattering event. Experimental evidence for multiphonon processes is provided in both optical and transport studies. In some cases, more than one phonon at the same frequency can be created (harmonics), while in other cases, multiple phonons at different frequencies (overtones) are involved.

### 6.3.2 Other Scattering Mechanisms in Metals

At very low temperatures where phonon scattering is of less importance, other scattering mechanisms become important, and we can write

```{math}
:label: eq-p1-ch06-49
\frac{1}{\tau} = \sum_i \frac{1}{\tau_i}
```

where the sum is over all the scattering processes.

(a) Charged impurity scattering — The effect of charged impurity scattering ($Z$ being the difference in the charge on the impurity site as compared with the charge on a regular lattice site) is of less importance in metals than in semiconductors, because of the strong screening effects by the free electrons in metals.

(b) Neutral impurities — This process pertains to scattering centers having the same charge as the host. Such scattering has less effect on the transport properties than scattering by charged impurity sites, because of the much weaker scattering potential.

(c) Vacancies, interstitials, dislocations, size–dependent effects — the effects for these defects on the transport properties are similar to those for semiconductors. Boundary scattering can become very important in metal nanostructures when the sample length in some direction becomes less than the mean free path in the corresponding bulk crystal.

For most metals, phonon scattering is relatively unimportant at liquid helium temperatures, so that resistivity measurements at 4 K provide a method for the detection of impurities and crystal defects. In fact, in characterizing the quality of a high purity metal sample, it is customary to specify the resistivity ratio $\rho(300\,\text{K})/\rho(4\,\text{K})$. This quantity is usually called the residual resistivity ratio (RRR), or the residual resistance ratio. In contrast, a typical semiconductor is characterized by its conductivity and Hall coefficient at room temperature and at 77 K.

## 6.4 Phonon Scattering

Whereas electron scattering is important in electronic transport properties, phonon scattering is important in thermal transport, particularly for the case of insulators where heat is carried mainly by phonons. The major scattering mechanisms for phonons are phonon–phonon scattering, phonon–boundary scattering, defect–phonon scattering, and phonon–electron scattering which are briefly discussed in the following subsections.

### 6.4.1 Phonon–Phonon Scattering

The dominant phonon scattering process in crystalline materials is usually phonon–phonon scattering. Phonons are scattered by other phonons because of anharmonic terms in the restoring potential. This scattering process permits:

- two phonons to combine to form a third phonon or
- one phonon to break up into two phonons.

In these anharmonic processes, energy and wavevector conservation apply:

```{math}
:label: eq-p1-ch06-50
\vec{q}_1 + \vec{q}_2 = \vec{q}_3
\quad\text{(normal processes)}
```

or

```{math}
:label: eq-p1-ch06-51
\vec{q}_1 + \vec{q}_2 = \vec{q}_3 + \vec{Q}
\quad\text{(umklapp processes)}
```

where $\vec{Q}$ corresponds to a phonon wave vector of magnitude equal to a non–zero reciprocal lattice vector. Umklapp processes are important when $q_1$ or $q_2$ are large, i.e., comparable to a reciprocal lattice vector (see {numref}`fig-p1-ch06-10`). When umklapp processes (see {numref}`fig-p1-ch06-10`) are present, the scattered phonon wavevector $\vec{q}_3$ can be in a direction opposite to the energy flow, thereby giving rise to thermal resistance. Because of the high momentum transfer and the large phonon energies that are involved, umklapp processes dominate the thermal conductivity at high $T$.

:::{figure} images/fig-p1-ch06-10.png
:name: fig-p1-ch06-10
:align: center
:width: 70%

Phonon–phonon umklapp processes. Here $\vec{Q}$ is a non–zero reciprocal lattice vector, and $\vec{q}_1$ and $\vec{q}_2$ are the incident phonon wavevectors involved in the scattering process, and $\vec{q}_3$ is the wavevector of the scattered phonon.
:::

The phonon density is proportional to the Bose factor so that the scattering rate is proportional to

```{math}
:label: eq-p1-ch06-52
\frac{1}{\tau_{ph}} \sim \frac{1}{e^{\hbar\omega/(k_BT)}-1} .
```

At high temperatures $T\gg\Theta_D$, the scattering time thus varies as $T^{-1}$ since

```{math}
:label: eq-p1-ch06-53
\tau_{ph} \sim \left(e^{\hbar\omega/k_BT}-1\right)
\sim \frac{\hbar\omega}{k_BT}
```

while at low temperatures $T\sim\Theta_D$, an exponential temperature dependence for $\tau_{ph}$ is found

```{math}
:label: eq-p1-ch06-54
\tau_{ph} \sim e^{\hbar\omega/k_BT}-1 .
```

These temperature dependences are important in considering the lattice contribution to the thermal conductivity (see §5.2.4).

### 6.4.2 Phonon–Boundary Scattering

Phonon–boundary scattering is important at low temperatures where the phonon density is low. In this regime, the scattering time is independent of $T$. The thermal conductivity in this range is proportional to the phonon density which is in turn proportional to $T^3$. Phonon–boundary scattering is also very important for low dimensional systems where the sample size in some dimension is less than the corresponding phonon mean free path in the bulk 3D crystal. Phonon–boundary scattering combined with phonon–phonon scattering results in a thermal conductivity $\kappa$ for insulators with the general shape shown in {numref}`fig-p1-ch06-11` (see §5.2.4). The lattice thermal conductivity follows the relation

```{math}
:label: eq-p1-ch06-55
\kappa_L = \frac{C_p v_q \Lambda_{ph}}{3}
```

where the phonon mean free path $\Lambda_{ph}$ is related to the phonon scattering probability ($1/\tau_{ph}$) by

```{math}
:label: eq-p1-ch06-56
\tau_{ph} = \frac{\Lambda_{ph}}{v_q}
```

:::{figure} images/fig-p1-ch06-11.png
:name: fig-p1-ch06-11
:align: center
:width: 70%

For insulators, we often plot both the thermal conductivity $\kappa$ and the temperature $T$ on log scales. The various curves are for LiF with different concentrations of Li isotopes $^6$Li and $^7$Li. For highly perfect crystals, it is possible to observe the scattering effects due to Li ions of different masses, which act as lattice defects.
:::

in which $v_q$ is the velocity of sound and $C_p$ is the heat capacity at constant pressure. Phonon–boundary scattering becomes more important as the crystallite size decreases. The scattering conditions at the boundary can be specular (where after scattering only $q_\perp$ is reversed and $q_\parallel$ is unchanged) for a very smooth surface or diffuse (where after scattering the $\vec{q}$ is randomized) for a rough surface. Periodic corrugations on a surface can also give rise to interesting scattering effects for both electrons and phonons.

### 6.4.3 Defect–Phonon Scattering

Defect–phonon scattering includes a variety of crystal defects, charged and uncharged impurities and different isotopes of the host constituents. The thermal conductivity curves in {numref}`fig-p1-ch06-11` show the scattering effects due to different isotopes of Li. The low mass of Li makes it possible to see such effects clearly. Isotope effects are also important in graphite and diamond which have the highest thermal conductivity of any solid.

### 6.4.4 Electron–Phonon Scattering

If electrons scatter from phonons, the reverse process also occurs. When phonons impart momentum to electrons, the electron distribution is affected. Thus, the electrons will also carry energy as they are dragged also by the stream of phonons. This phenomenon is called phonon drag. In the case of phonon drag we must simultaneously solve the Boltzmann equations for the electron and phonon distributions which are coupled by the phonon drag term.

## 6.5 Temperature Dependence of the Electrical and Thermal Conductivity

For the electrical conductivity, at very low temperatures, impurity, defect, and boundary scattering dominate. In this regime $\sigma$ is independent of temperature. At somewhat higher temperatures but still far below $\Theta_D$ the electrical conductivity for metals exhibits a strong temperature dependence (see {eq}`eq-p1-ch06-48`)

```{math}
:label: eq-p1-ch06-57
\sigma \propto \left(\frac{\Theta_D}{T}\right)^5,\qquad T\ll\Theta_D .
```

At higher temperatures where $T\gg\Theta_D$, scattering by phonons with any $q$ vector is possible and the formula

```{math}
:label: eq-p1-ch06-58
\sigma \sim \frac{\Theta_D}{T},\qquad T\gg\Theta_D
```

applies. We now summarize the corresponding temperature ranges for the thermal conductivity. Although the thermal conductivity was formally discussed in §5.2, a meaningful discussion of the temperature dependence of $\kappa$ depends on scattering processes. The total thermal conductivity $\kappa$ in general depends on the lattice and electronic contributions, $\kappa_L$ and $\kappa_e$, respectively. The temperature dependence of the lattice contribution is discussed in §5.2.4 with regard to the various phonon scattering processes and their temperature dependence. For the electronic contribution, we must consider the temperature dependence of the electron scattering processes discussed in §5.2 and §6.2.

At very low temperatures, in the impurity/defect/boundary scattering range, $\sigma$ is independent of $T$ and the same scattering processes apply for both the electronic thermal conductivity and the electrical conductivity so that $\kappa_e\propto T$ in the impurity scattering regime where $\sigma\sim$ constant and the Wiedemann–Franz law is applicable. From {numref}`fig-p1-ch05-1` we see that for copper, defect and boundary scattering are dominant below $\sim 20$ K, while phonon scattering becomes important at higher $T$.

At low temperatures $T\ll\Theta_D$, but with $T$ in a regime where phonon scattering has already become the dominant scattering mechanism, the thermal transport depends on the electron–phonon collision rate which in turn is proportional to the phonon density. At low temperatures the phonon density is proportional to $T^3$. This follows from the proportionality of the phonon density of states arising from the integration of $\int q^2dq$, and from the dispersion relation for the acoustic phonons $\omega = q v_q$

```{math}
:label: eq-p1-ch06-59
q = \frac{\omega}{v_q} = \frac{x k_BT}{\hbar v_q},\qquad x = \frac{\hbar\omega}{k_BT}
```

where $x = \hbar\omega/k_BT$. Thus in the low temperature range of phonon scattering where $T\ll\Theta_D$ and the Wiedemann–Franz law is no longer satisfied, the temperature dependence of $\tau$ is found from the product $T(T^{-3})$ so that $\kappa_e\propto T^{-2}$. One reason why the Wiedemann–Franz law is not satisfied in this temperature regime is that $\kappa_e$ depends on the collision rate $\tau_c$ while $\sigma$ depends on the time to reach thermal equilibrium, $\tau_D$. At low temperatures where only low $q$ phonons participate in scattering events the times $\tau_c$ and $\tau_D$ are not the same.

At high $T$ where $T\gg\Theta_D$ and the Wiedemann–Franz law applies, $\kappa_e$ approaches a constant value corresponding to the regime where $\sigma$ is proportional to $1/T$. This occurs at temperatures much higher than those shown in {numref}`fig-p1-ch05-1`. The decrease in $\kappa$ above the peak value at $\sim 17$ K follows a $1/T^2$ dependence quite well.

In addition to the electronic thermal conductivity, heat can be carried by the lattice vibrations or phonons. The phonon thermal conductivity mechanism is in fact the principal mechanism operative in semiconductors and insulators, since the electronic contribution in this case is negligibly small. Since $\kappa_L$ contributes also to metals, the total measured thermal conductivity for metals should exceed the electronic contribution $(\pi^2 k_B^2 T\sigma)/(3e^2)$. In good metallic conductors of high purity, the electronic thermal conductivity dominates and the phonon contribution tends to be small. On the other hand, in conductors where the thermal conductivity due to phonons makes a significant contribution to the total thermal conductivity, it is necessary to separate the electronic and lattice contributions before applying the Wiedemann–Franz law to the total $\kappa$.

With regard to the lattice contribution, $\kappa_L$ at very low temperatures is dominated by defect and boundary scattering processes. From the relation

```{math}
:label: eq-p1-ch06-60
\kappa_L = \frac{1}{3}C_p v_q \Lambda_{ph}
```

we can determine the temperature dependence of $\kappa_L$, since $C_p\sim T^3$ at low $T$ while the sound velocity $v_q$ and phonon mean free path $\Lambda_{ph}$ at very low $T$ are independent of $T$. In this regime the number of scatterers is independent of $T$. In the regime where only low $q$ phonons contribute to transport and to scattering, only normal scattering processes contribute. In this regime $C_p$ is still increasing as $T^3$, $v_q$ is independent of $T$, but $1/\Lambda_{ph}$ increases in proportion to the phonon density of states. With increasing $T$, the temperature dependence of $C_p$ becomes less pronounced and that for $\Lambda_{ph}$ becomes more pronounced as more scatterers participate, leading eventually to a decrease in $\kappa_L$. We note that it is only the inelastic collisions that contribute to the decrease in $\Lambda_{ph}$, since elastic phonon–phonon scattering has a similar effect as impurity scattering for phonons. The inelastic collisions are of course due to anharmonic forces. Eventually phonons with wavevectors large enough to support umklapp processes are thermally activated. Umklapp processes give rise to thermal resistance and in this regime $\kappa_L$ decreases as $\exp(-\Theta_D/T)$. In the high temperature limit $T\gg\Theta_D$, the heat capacity and phonon velocity are both independent of $T$. The $\kappa_L\sim 1/T$ dependence arises from the $1/T$ dependence of the mean free path, since in this limit the scattering rate becomes proportional to $k_BT$.
