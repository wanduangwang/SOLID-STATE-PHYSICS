---
title: "3 Interband Transitions"
abstract: "Interband optical transitions are discussed in terms of the interband conductivity tensor, the momentum matrix elements, the form of the Hamiltonian in an electromagnetic field, and the connection between momentum matrix elements and the effective mass tensor. The spin-orbit interaction in solids is also introduced."
---

# 3 Interband Transitions

## 3.0 Overview

In a semiconductor at low frequencies the principal electronic conduction mechanism is associated with free carriers. As the photon energy increases and becomes comparable to the energy gap, a new conduction process can occur: a photon can excite an electron from an occupied state in the valence band to an unoccupied state in the conduction band. This process is called an interband transition and is represented schematically in Fig. {numref}`fig-p2-ch03-1`. In this process the photon is absorbed, an excited electronic state is formed and a hole is left behind. This chapter discusses the physical ideas and mathematical description of these quantum-mechanical transitions.

## 3.1 The Interband Transition Process

A number of factors are important in interband transitions.

1. We expect interband transitions to have a threshold energy at the energy gap. That is, we expect the frequency dependence of the real part of the conductivity $\sigma_1(\omega)$ due to an interband transition to exhibit a threshold as shown in Fig. {numref}`fig-p2-ch03-2` for an allowed electronic transition.

2. The transitions are either direct (conserve crystal momentum $\mathbf{k}$: $E_v(\mathbf{k}) \to E_c(\mathbf{k})$) or indirect (a phonon is involved because the $\mathbf{k}$ vectors for the valence and conduction bands differ by the phonon wave vector $\mathbf{q}$). Conservation of crystal momentum yields
   $$\mathbf{k}_{\text{valence}} = \mathbf{k}_{\text{conduction}} \pm \mathbf{q}_{\text{phonon}}.$$
   In discussing direct transitions, one might wonder about conservation of crystal momentum with regard to the photon. The reason we need not be concerned with the momentum of the photon is that it is very small in comparison to Brillouin-zone dimensions. For a typical optical wavelength of $6000\,\text{\AA}$, the wave vector for the photon $K = 2\pi/\lambda \sim 10^5\,\text{cm}^{-1}$, while a typical dimension across the Brillouin zone is $10^8\,\text{cm}^{-1}$. Thus, typical direct optical interband processes excite an electron from a valence to a conduction band without a significant change in the wave vector.

3. The transitions depend on the coupling between the valence and conduction bands and this is measured by the magnitude of the momentum matrix elements coupling the valence band state $v$ and the conduction band state $c$: $|\langle v|\mathbf{p}|c\rangle|^2$. This dependence results from Fermi's "Golden Rule" (see Chapter A) and from the discussion of the perturbation interaction $\mathcal{H}'$ for the electromagnetic field with electrons in the solid (discussed in §3.2). Selection rules can cause certain transitions to be forbidden.

4. Because of the Pauli Exclusion Principle, an interband transition occurs from an occupied state below the Fermi level to an unoccupied state above the Fermi level.

5. Since the optical properties are found by an integration over $\mathbf{k}$ space, the joint density of states (discussed in Chapter 4) is important. Photons of a particular energy are more effective in producing an interband transition if the energy separation between the two bands is nearly constant over many $\mathbf{k}$ values. In that case, there are many initial and final states which can be coupled by the same photon energy. This is perhaps easier to see if we allow a photon to have a small bandwidth. That bandwidth will be effective over many $\mathbf{k}$ values if $E_c(\mathbf{k}) - E_v(\mathbf{k})$ does not vary rapidly with $\mathbf{k}$. Thus, we expect the interband transitions to be most important for $\mathbf{k}$ values near band extrema. That is, in Fig. {numref}`fig-p2-ch03-1` we see that states around $\mathbf{k}=0$ make the largest contribution per unit bandwidth of the optical source. It is also for this reason that optical measurements are so important in studying energy band structure; the optical structure emphasizes band extrema and therefore provides information about the energy bands at specific points in the Brillouin zone. Because of the dependence of the density of states and the joint density of states on the dimensionality of the system, the optical properties will be very sensitive to the dimensionality of a sample.

:::{figure} images/fig-p2-ch03-1.png
:name: fig-p2-ch03-1
:width: 50%
:align: center
Fig. 3.1: Schematic diagram of an allowed interband transition.
:::

:::{figure} images/fig-p2-ch03-2.png
:name: fig-p2-ch03-2
:width: 50%
:align: center
Fig. 3.2: Real part of the conductivity for an allowed optical transition. We note that $\sigma_1(\omega) = (\omega/4\pi)\,\varepsilon_2(\omega)$.
:::

Although we will not derive the expression for the interband contribution to the conductivity, we will write it down here to show how all the physical ideas that were discussed above enter into the conductivity equation. We now write the conductivity tensor relating the interband current density $j_\alpha$ in the direction $\alpha$ which flows upon application of an electric field $E_\beta$ in direction $\beta$

```{math}
:label: eq-p2-ch03-1
j_\alpha = \sigma_{\alpha\beta} E_\beta
```

as

```{math}
:label: eq-p2-ch03-2
\sigma_{\alpha\beta} = -\frac{e^2}{m^2} \sum_{i,j} \frac{[f(E_i)-f(E_j)]}{E_i-E_j} \frac{\langle i|p_\alpha|j\rangle \langle j|p_\beta|i\rangle}{[-i\omega + 1/\tau + (i/\hbar)(E_i-E_j)]}
```

in which the sum in Eq. {eq}`eq-p2-ch03-2` is over all valence and conduction band states labeled by $i$ and $j$. Structure in the optical conductivity arises through a singularity in the resonant denominator of Eq. {eq}`eq-p2-ch03-2`, $[-i\omega + 1/\tau + (i/\hbar)(E_i-E_j)]$, discussed above under properties (1) and (5).

The appearance of the Fermi functions $f(E_i)-f(E_j)$ follows from the Pauli principle in property (4). The dependence of the conductivity on the momentum matrix elements accounts for the tensorial properties of $\sigma_{\alpha\beta}$ (interband) and relates to properties (2) and (3).

In semiconductors, interband transitions usually occur at frequencies above which free carrier contributions are important. If we now want to consider the total complex dielectric constant, we would write

```{math}
:label: eq-p2-ch03-3
\varepsilon = \varepsilon_{\text{core}} + \frac{4\pi i}{\omega} [\sigma_{\text{Drude}} + \sigma_{\text{interband}}].
```

The term $\varepsilon_{\text{core}}$ contains the contributions from all processes that are not considered explicitly in Eq. {eq}`eq-p2-ch03-3`; this would include both intraband and interband transitions that are not treated explicitly. We have now dealt with the two most important processes (intraband and interband) involved in studies of the electronic properties of solids.

If we think of the optical properties for various classes of materials, it is clear that major differences will be found from one class of materials to another.

### 3.1.1 Insulators

Here the band gap is sufficiently large so that at room temperature, essentially no carriers are thermally excited across the band gap. This means that there is no free carrier absorption and that interband transitions only become important at relatively high photon energies (above the visible). Thus, insulators frequently are optically transparent in the visible frequency range.

### 3.1.2 Semiconductors

Here the band gap is small enough so that appreciable thermal excitation of carriers occurs at room temperature. Thus there is often appreciable free carrier absorption at room temperature either through thermal excitation or doping. In addition, interband transitions occur in the infrared and visible. As an example, consider the direct interband transition in germanium and its relation to the optical absorption (see Fig. {numref}`fig-p2-ch03-3`). In the curve in Fig. {numref}`fig-p2-ch03-4`, we see that the optical absorption due to optical excitation across the indirect bandgap at $0.7\,\text{eV}$ is very small compared with the absorption due to the direct interband transition at $0.8\,\text{eV}$ shown in Fig. {numref}`fig-p2-ch03-4`. (For a brief discussion of the spin-orbit interaction as it affects interband transitions see §3.4.)

:::{figure} images/fig-p2-ch03-3.png
:name: fig-p2-ch03-3
:width: 55%
:align: center
Fig. 3.3: Structure of the valence band states and the lowest conduction band state at the $\Gamma$-point in germanium.
:::

:::{figure} images/fig-p2-ch03-4.png
:name: fig-p2-ch03-4
:width: 55%
:align: center
Fig. 3.4: Absorption coefficient of germanium at the absorption edge corresponding to the transitions $\Gamma_{25'}^{3/2} \to \Gamma_{2'}(D_1)$ and $\Gamma_{25'}^{1/2} \to \Gamma_{2'}(D_2)$. The energy separation between the $\Gamma_{25'}^{1/2}$ and $\Gamma_{25'}^{3/2}$ bands is determined by the energy differences between the $D_1$ and $D_2$ structures.
:::

### 3.1.3 Metals

Here free carrier absorption is extremely important. Typical plasma frequencies are $\hbar\omega_p \cong 10\,\text{eV}$ which occur far out in the ultraviolet. In the case of metals, interband transitions typically occur at frequencies where free carrier effects are still important. Semimetals, like metals, exhibit only a weak temperature dependence with carrier densities almost independent of temperature. Although the carrier densities are low, the high carrier mobilities nevertheless guarantee a large contribution of the free carriers to the optical conductivity.

## 3.2 Form of the Hamiltonian in an Electromagnetic Field

A proof that the optical field is inserted into the Hamiltonian in the form $\mathbf{p} \to \mathbf{p} - e\mathbf{A}/c$ follows. Consider the classical equation of motion:

```{math}
:label: eq-p2-ch03-4
\frac{d}{dt}(m\mathbf{v}) = e\left[\mathbf{E} + \frac{1}{c}(\mathbf{v}\times\mathbf{H})\right] = e\left[-\mathbf{\nabla}\phi - \frac{1}{c}\frac{\partial \mathbf{A}}{\partial t} + \frac{1}{c}\mathbf{v}\times(\mathbf{\nabla}\times\mathbf{A})\right]
```

where $\phi$ and $\mathbf{A}$ are, respectively, the scalar and vector potentials, and $\mathbf{E}$ and $\mathbf{B}$ are the electric and magnetic fields given by

```{math}
:label: eq-p2-ch03-5
\mathbf{E} = -\mathbf{\nabla}\phi - \frac{1}{c}\frac{\partial \mathbf{A}}{\partial t}, \qquad \mathbf{B} = \mathbf{\nabla}\times\mathbf{A}.
```

Using standard vector identities, the equation of motion Eq. {eq}`eq-p2-ch03-4` becomes

```{math}
:label: eq-p2-ch03-6
\frac{d}{dt}\left(m\mathbf{v} + \frac{e}{c}\mathbf{A}\right) = \mathbf{\nabla}(-e\phi) + \frac{e}{c}\mathbf{\nabla}(\mathbf{A}\cdot\mathbf{v})
```

where $[\mathbf{\nabla}(\mathbf{A}\cdot\mathbf{v})]_j$ denotes $v_i\,\partial A_i/\partial x_j$ in which we have used the Einstein summation convention that repeated indices are summed and where we have used the vector relation $\mathbf{a}\times(\mathbf{b}\times\mathbf{c}) = \mathbf{b}(\mathbf{a}\cdot\mathbf{c}) - \mathbf{c}(\mathbf{a}\cdot\mathbf{b})$ in Eq. {eq}`eq-p2-ch03-4`

```{math}
:label: eq-p2-ch03-7
\frac{d\mathbf{A}}{dt} = \frac{\partial \mathbf{A}}{\partial t} + (\mathbf{v}\cdot\mathbf{\nabla})\mathbf{A}
```

and

```{math}
:label: eq-p2-ch03-8
[\mathbf{v}\times(\mathbf{\nabla}\times\mathbf{A})]_i = v_j \frac{\partial A_j}{\partial x_i} - v_j \frac{\partial A_i}{\partial x_j}.
```

If we write the Hamiltonian as

```{math}
:label: eq-p2-ch03-9
\mathcal{H} = \frac{1}{2m}\left(\mathbf{p} - \frac{e}{c}\mathbf{A}\right)^2 + e\phi
```

and then use Hamilton's equations

```{math}
:label: eq-p2-ch03-10
\mathbf{v} = \frac{\partial \mathcal{H}}{\partial \mathbf{p}} = \frac{1}{m}\left(\mathbf{p} - \frac{e}{c}\mathbf{A}\right)
```

```{math}
:label: eq-p2-ch03-11
\dot{\mathbf{p}} = -\mathbf{\nabla}\mathcal{H} = -e\mathbf{\nabla}\phi + \frac{e}{c}\mathbf{v}\cdot\mathbf{\nabla}\mathbf{A}
```

we can show that Eqs. {eq}`eq-p2-ch03-4` and {eq}`eq-p2-ch03-6` are satisfied, thereby verifying that Eq. {eq}`eq-p2-ch03-9` is the proper form of the Hamiltonian in the presence of an electromagnetic field, which has the same form as the Hamiltonian without an optical field except that $\mathbf{p} \to \mathbf{p} - (e/c)\mathbf{A}$. The same transcription is used when light is applied to a solid and it is then called the Luttinger transcription. The Luttinger transcription is used in the effective mass approximation where the periodic potential is replaced by the introduction of $\mathbf{k} \to -(1/i)\mathbf{\nabla}$ and $m \to m^*$.

The reason why interband transitions depend on the momentum matrix element can be understood from perturbation theory. At any instant of time, the Hamiltonian for an electron in a solid in the presence of an optical field is

```{math}
:label: eq-p2-ch03-12
\mathcal{H} = \frac{(\mathbf{p} - e/c\mathbf{A})^2}{2m} + V(\mathbf{r}) = \frac{p^2}{2m} + V(\mathbf{r}) - \frac{e}{mc}\mathbf{A}\cdot\mathbf{p} + \frac{e^2 A^2}{2mc^2}
```

in which $\mathbf{A}$ is the vector potential due to the optical fields, and $V(\mathbf{r})$ is the periodic potential. Thus, the one-electron Hamiltonian without optical fields is

```{math}
:label: eq-p2-ch03-13
\mathcal{H}_0 = \frac{p^2}{2m} + V(\mathbf{r})
```

and the optical perturbation terms are

```{math}
:label: eq-p2-ch03-14
\mathcal{H}' = -\frac{e}{mc}\mathbf{A}\cdot\mathbf{p} + \frac{e^2 A^2}{2mc^2}.
```

Optical fields are generally very weak (unless generated by powerful lasers) and we usually consider only the term linear in $\mathbf{A}$, the linear response regime.

The form of the Hamiltonian in the presence of an electromagnetic field is derived in this section. The momentum matrix elements $\langle v|\mathbf{p}|c\rangle$ which determine the strength of optical transitions also govern the magnitudes of the effective mass components (see §3.3). This is another reason why optical studies are very important.

The coupling of the valence and conduction bands through the optical fields (Eq. {eq}`eq-p2-ch03-9`), depends on the matrix element for the coupling to the electromagnetic field perturbation

```{math}
:label: eq-p2-ch03-15
\mathcal{H}' \cong -\frac{e}{mc}\mathbf{p}\cdot\mathbf{A}.
```

With regard to the spatial dependence of the vector potential we can write

```{math}
:label: eq-p2-ch03-16
\mathbf{A} = \mathbf{A}_0 \exp[i(\mathbf{K}\cdot\mathbf{r} - \omega t)]
```

where for a loss-less medium $K = \tilde{n}\omega/c = 2\pi\tilde{n}/\lambda$ is a slowly varying function of $\mathbf{r}$ since $2\pi\tilde{n}/\lambda$ is much smaller than typical wave vectors in solids. Here $\tilde{n}$, $\omega$, and $\lambda$ are, respectively, the real part of the index of refraction, the optical frequency, and the wavelength of light.

## 3.3 Relation between Momentum Matrix Elements and the Effective Mass

Because of the relation between the momentum matrix element $\langle v|\mathbf{p}|c\rangle$, which governs the electromagnetic interaction with electrons and solids, and the band curvature $(\partial^2 E/\partial k_\alpha \partial k_\beta)$, the energy band diagrams provide important information on the strength of optical transitions. Correspondingly, knowledge of the optical properties can be used to infer experimental information about $E(\mathbf{k})$.

We now derive the relation between the momentum matrix element coupling the valence and conduction bands $\langle v|\mathbf{p}|c\rangle$ and the band curvature $(\partial^2 E/\partial k_\alpha \partial k_\beta)$. We start with Schrödinger's equation in a periodic potential $V(\mathbf{r})$ having the Bloch solutions

```{math}
:label: eq-p2-ch03-17
\psi_{n\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} u_{n\mathbf{k}}(\mathbf{r}),
```

```{math}
:label: eq-p2-ch03-18
\mathcal{H}\psi_{n\mathbf{k}}(\mathbf{r}) = E_n(\mathbf{k})\psi_{n\mathbf{k}}(\mathbf{r}) = \left[\frac{p^2}{2m} + V(\mathbf{r})\right] e^{i\mathbf{k}\cdot\mathbf{r}} u_{n\mathbf{k}}(\mathbf{r}) = E_n(\mathbf{k}) e^{i\mathbf{k}\cdot\mathbf{r}} u_{n\mathbf{k}}(\mathbf{r}).
```

Since $\mathbf{p}$ is an operator $(\hbar/i)\mathbf{\nabla}$, we can write

```{math}
:label: eq-p2-ch03-19
\mathbf{p} e^{i\mathbf{k}\cdot\mathbf{r}} u_{n\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} (\mathbf{p} + \hbar\mathbf{k}) u_{n\mathbf{k}}(\mathbf{r}).
```

Therefore the differential equation for $u_{n\mathbf{k}}(\mathbf{r})$ becomes

```{math}
:label: eq-p2-ch03-20
\left[\frac{p^2}{2m} + V(\mathbf{r}) + \frac{\hbar\mathbf{k}\cdot\mathbf{p}}{m} + \frac{\hbar^2 k^2}{2m}\right] u_{n\mathbf{k}}(\mathbf{r}) = E_n(\mathbf{k}) u_{n\mathbf{k}}(\mathbf{r})
```

giving the following differential equation for the periodic function $u_{n\mathbf{k}}(\mathbf{r}) = u_{n\mathbf{k}}(\mathbf{r}+\mathbf{R}_m)$

```{math}
:label: eq-p2-ch03-21
\left[\frac{p^2}{2m} + V(\mathbf{r}) + \frac{\hbar\mathbf{k}\cdot\mathbf{p}}{m}\right] u_{n\mathbf{k}}(\mathbf{r}) = \left[E_n(\mathbf{k}) - \frac{\hbar^2 k^2}{2m}\right] u_{n\mathbf{k}}(\mathbf{r})
```

which we write as follows to put Eq. {eq}`eq-p2-ch03-21` in the canonical form for application of the perturbation theory formulae

```{math}
:label: eq-p2-ch03-22
\mathcal{H}_0 = \frac{p^2}{2m} + V(\mathbf{r})
```

```{math}
:label: eq-p2-ch03-23
\mathcal{H}' = \frac{\hbar\mathbf{k}\cdot\mathbf{p}}{m}
```

```{math}
:label: eq-p2-ch03-24
\mathcal{E}_n(\mathbf{k}) = E_n(\mathbf{k}) - \frac{\hbar^2 k^2}{2m}
```

to yield

```{math}
:label: eq-p2-ch03-25
[\mathcal{H}_0 + \mathcal{H}'] u_{n\mathbf{k}}(\mathbf{r}) = \mathcal{E}_n(\mathbf{k}) u_{n\mathbf{k}}(\mathbf{r}).
```

Assume that we know the solution to Eq. {eq}`eq-p2-ch03-25` about a special point $\mathbf{k}_0$ in the Brillouin zone which could be a band extremum, such as $\mathbf{k}_0 = 0$. Then the perturbation formulae Eqs. {eq}`eq-p2-ch03-22`–{eq}`eq-p2-ch03-25` allow us to find the energy and wave function for states near $\mathbf{k}_0$. For simplicity, we carry out the expansion about the center of the Brillouin zone $\mathbf{k}=0$, which is the most important case in practice; the extension of this argument to an energy extremum at arbitrary $\mathbf{k}_0$ is immediate. Perturbation theory then gives:

```{math}
:label: eq-p2-ch03-26
\mathcal{E}_n(\mathbf{k}) = E_n(0) + (u_{n,0}|\mathcal{H}'|u_{n,0}) + \sum_{n'\neq n} \frac{(u_{n,0}|\mathcal{H}'|u_{n',0})(u_{n',0}|\mathcal{H}'|u_{n,0})}{E_n(0) - E_{n'}(0)}.
```

The first order term $(u_{n,0}|\mathcal{H}'|u_{n,0})$ in Eq. {eq}`eq-p2-ch03-26` normally vanishes about an extremum because of inversion symmetry, with $\mathcal{H}'$ being odd under inversion and the two wavefunctions $u_{n\mathbf{k}}(\mathbf{r})$ both being even or both being odd. Since

```{math}
:label: eq-p2-ch03-27
\mathcal{H}' = \frac{\hbar\mathbf{k}\cdot\mathbf{p}}{m}
```

the matrix element is then written as

```{math}
:label: eq-p2-ch03-28
(u_{n,0}|\mathcal{H}'|u_{n',0}) = \frac{\hbar}{m}\mathbf{k}\cdot(u_{n,0}|\mathbf{p}|u_{n',0}).
```

We now apply Eq. {eq}`eq-p2-ch03-26` to optical transitions, for the simplest case of a two band model. Here we assume that:

1. bands $n$ and $n'$ (valence ($v$) and conduction ($c$) bands) are close to each other and far from other bands
2. interband transitions occur between these two bands separated by an energy gap $E_g$.

We note that the perturbation theory is written in terms of the energy $\mathcal{E}_n(k)$

```{math}
:label: eq-p2-ch03-29
\mathcal{E}_n(k) = E_n(\mathbf{k}) - \frac{\hbar^2 k^2}{2m}.
```

Assuming that the first order term in perturbation theory (Eq. {eq}`eq-p2-ch03-26`) can be neglected by parity (even and oddness) arguments, we obtain for $\mathcal{E}_n(k)$ about $\mathbf{k}=0$

```{math}
:label: eq-p2-ch03-30
\mathcal{E}_n(\mathbf{k}) = E_n(0) + \frac{\hbar^2}{m^2} k_\alpha k_\beta \frac{|\langle v|p_\alpha|c\rangle \langle c|p_\beta|v\rangle|}{E_g}
```

or in terms of the energy eigenvalues of Schrödinger's equation (Eq. {eq}`eq-p2-ch03-18`)

```{math}
:label: eq-p2-ch03-31
E_n(\mathbf{k}) = E_n(0) + \frac{\hbar^2 k^2}{2m} + \frac{\hbar^2}{m^2} k_\alpha k_\beta \frac{|\langle v|p_\alpha|c\rangle \langle c|p_\beta|v\rangle|}{E_g}.
```

We define the effective mass tensor by the relation

```{math}
:label: eq-p2-ch03-32
E_n(\mathbf{k}) = E_n(0) + \frac{\hbar^2}{2} \sum_{\alpha,\beta} k_\alpha k_\beta \left(\frac{1}{m^*}\right)_{\alpha\beta}
```

so that

```{math}
:label: eq-p2-ch03-33
\left(\frac{1}{m^*}\right)_{\alpha\beta} = \frac{\delta_{\alpha\beta}}{m} + \frac{2}{m^2} \frac{|\langle v|p_\alpha|c\rangle \langle c|p_\beta|v\rangle|}{E_g}
```

where $\delta_{\alpha\beta}$ is the unit matrix. This discussion shows that the non-vanishing momentum matrix element is responsible for the inequality between the free electron $m$ and the effective mass $m^*$ in the solid. With regard to the optical properties of solids we note that the same momentum matrix element that governs the effective mass formula (Eq. {eq}`eq-p2-ch03-33`) also governs the electromagnetic interaction given by Eq. {eq}`eq-p2-ch03-15`. Thus small effective masses tend to give rise to strong coupling between valence and conduction bands and large values for $|\langle v|p|c\rangle|^2$. On the other hand, small effective masses lead to a small density of states because of the $m^{*3/2}$ dependence of the density of states.

## 3.4 Spin-Orbit Interaction in Solids

Reference:

- Jones and March, pp. 85-87, 89-94.
- Eisberg and Resnick, *Quantum Physics* pp. 278-281.

A spin angular momentum $S_z = \hbar/2$ and a magnetic moment $\mu_B = |e|\hbar/2mc = 0.927\times 10^{-20}\,\text{erg/gauss}$ is associated with each electron. The magnetic moment and spin angular momentum for the free electron are related by

```{math}
:label: eq-p2-ch03-34
\vec{\mu} = \frac{-|e|}{mc}\vec{S} = \frac{-|e|}{mc}\cdot\frac{\hbar}{2}\hat{S}
```

($\hat{S}$ is a unit vector along $\vec{S}$), and $\vec{\mu}$ and $\vec{S}$ are oppositely directed because the electron is negatively charged.

An electron in an atom sees a magnetic field because of its own orbital motion and consequently there is an interaction called the *spin-orbit interaction* whereby the magnetic field due to the orbital motion of the electron tends to line up its magnetic moment along the magnetic field:

```{math}
:label: eq-p2-ch03-35
\mathcal{H}'_{\text{S.O.}} = -\vec{\mu}\cdot\vec{H}.
```

:::{figure} images/fig-p2-ch03-5.png
:name: fig-p2-ch03-5
:width: 35%
:align: center
Fig. 3.5: Schematic diagram showing the splitting of the $\ell=1$ level by the spin-orbit interaction.
:::

```{math}
:label: eq-p2-ch03-36
\mathcal{H}'_{\text{S.O.}} = \frac{1}{2m^2c^2}(\nabla V \times \mathbf{p})\cdot\vec{S}
```

since $e\mathbf{E} \sim -\mathbf{\nabla}V$. For an atom Eq. {eq}`eq-p2-ch03-36` results in

```{math}
:label: eq-p2-ch03-37
\mathcal{H}'_{\text{S.O. atom}} = \xi(r)\vec{L}\cdot\vec{S}.
```

A detailed discussion of this topic is found in any standard quantum mechanics text.

This spin-orbit interaction gives rise to a spin-orbit splitting of the atomic levels corresponding to different values of the total angular momentum $\vec{J}$

```{math}
:label: eq-p2-ch03-38
\vec{J} = \vec{L} + \vec{S}
```

where $\vec{L}$ and $\vec{S}$, respectively, denote the orbital and spin angular momentum. Thus

```{math}
:label: eq-p2-ch03-39
\vec{J}\cdot\vec{J} = (\vec{L}+\vec{S})\cdot(\vec{L}+\vec{S}) = \vec{L}\cdot\vec{L} + \vec{S}\cdot\vec{S} + (\vec{L}\cdot\vec{S} + \vec{S}\cdot\vec{L})
```

in which the operators $\vec{L}$ and $\vec{S}$ commute.

We take matrix elements in the $|j,\ell,s,m_j\rangle$ representation, because $m_\ell$, $m_s$ are not good quantum numbers, to obtain, with $j = |\ell-s|,(|\ell-s|+1),\dots,\ell+s$,

```{math}
:label: eq-p2-ch03-40
j(j+1) = \ell(\ell+1) + s(s+1) + 2\langle\vec{L}\cdot\vec{S}\rangle
```

so that the expectation value of $\vec{L}\cdot\vec{S}$ in the $|j,\ell,s,m_j\rangle$ representation becomes:

```{math}
:label: eq-p2-ch03-41
\langle\vec{L}\cdot\vec{S}\rangle = \frac{1}{2}[j(j+1) - \ell(\ell+1) - s(s+1)]
```

For $p$ states, $\ell=1$, $s=1/2$ and $j=3/2$ or $1/2$ as shown in Fig. {numref}`fig-p2-ch03-5`. From Eq. {eq}`eq-p2-ch03-41` we can find the expectation value of $\langle\vec{L}\cdot\vec{S}\rangle$. In particular, we note that the degeneracy of an $s$-state is unaffected by the spin-orbit interaction. On the other hand, a $d$-state is split up into a doublet $D_{5/2}$ (6-fold degenerate) and $D_{3/2}$ (4-fold degenerate). Thus, the spin-orbit interaction does not lift all the degeneracy for atomic states. To lift this additional degeneracy it is necessary to apply a magnetic field.

The magnitude of the spin-orbit interaction depends also on the expectation value of $\xi(r)$ defined by the following relation,

```{math}
:label: eq-p2-ch03-42
\langle n,j,\ell,s,m_j|\mathcal{H}'_{\text{S.O.}}|n,j,\ell,s,m_j\rangle = \langle j,\ell,s,m_j|\vec{L}\cdot\vec{S}|j,\ell,s,m_j\rangle \int_0^\infty R_{n\ell}\,\xi(r)\,R_{n\ell}\,dr
```

where the atomic wave function is written

```{math}
:label: eq-p2-ch03-43
\Phi = Y_{\ell m}(\theta,\phi) R_{n\ell}(r)
```

and $R_{n\ell}(r)$ denotes the radial part of the atomic wave function. We note that the integral over $r$ in Eq. {eq}`eq-p2-ch03-42` increases rapidly with atomic number ($\sim Z^3$ or $Z^4$). The physical reason behind this sensitive dependence on $Z$ is that heavier atoms have more electrons generating larger $H$ fields, and therefore a greater spin-orbit splitting results.

References for tabulated spin-orbit splittings are:

- C.E. Moore — *Atomic Energy Levels* (National Bureau of Standards, Circular #467), vol. 1 (1949), vol. 2 (1952) and vol. 3 (1958). These references give the measured spectroscopic levels for any atom in a large number of excited configurations. The lowest $Z$ values are in vol. 1, the highest in vol. 3.
- F. Herman and S. Skillman — *Atomic Structure Calculation* (Prentice-Hall, Inc. 1963). Most complete listing of calculated atomic levels.
- Landolt and Bornstein — *Physical and Chemical Tables* (many volumes in Reference section in the Science Library).

For most atomic species that are important in semiconductor physics, the spin-orbit interaction is important. Some typical values are:

:::{table} Typical spin-orbit $\Gamma$-point splittings for several semiconductors.
:name: tab-p2-ch03-1
| semiconductor | atomic number | $\Gamma$-point splitting |
|:--------------|:---------------|:-------------------------|
| diamond | $Z=6$ | $\Delta = 0.006\,\text{eV}$ |
| silicon | $Z=14$ | $\Delta = 0.044\,\text{eV}$ |
| germanium | $Z=32$ | $\Delta = 0.290\,\text{eV}$ |
| tin | $Z=50$ | $\Delta = 0.527\,\text{eV}$ |
| InSb | $Z=49$ | $\Delta = 0.274\,\text{eV}$ |
| InSb | $Z=51$ | $\Delta = 0.815\,\text{eV}$ |
| GaAs | $Z=31$ | $\Delta = 0.103\,\text{eV}$ |
| GaAs | $Z=33$ | $\Delta = 0.364\,\text{eV}$ |
| PbTe | $Z=82$ | $\Delta = 1.746\,\text{eV}$ |
| HgTe | $Z=80$ | $\Delta = 1.131\,\text{eV}$ |
| PbTe, HgTe | $Z=52$ | $\Delta = 1.143\,\text{eV}$ |
:::

The listing above gives the $\Gamma$ point splittings. The spin-orbit splittings are $\mathbf{k}$-dependent and at the $L$-point are typically about $2/3$ of the $\Gamma$ point value.

The one-electron Hamiltonian for a solid including spin-orbit interaction is from Eq. {eq}`eq-p2-ch03-36`

```{math}
:label: eq-p2-ch03-44
\mathcal{H} = \frac{p^2}{2m} + V(r) - \frac{1}{2m^2c^2}(\nabla V \times \mathbf{p})\cdot\vec{S}.
```

When the electron spin is considered, the wave functions consist of a spatial and a spin part. The effect of the spin-orbit interaction is to introduce a partial lifting of the degeneracy of band states at high symmetry points in the Brillouin zone. Also, it is a convention in the literature to use a different labeling scheme for the energy bands when the spin-orbit interaction is included. To show the effect of the spin-orbit interaction on the energy bands of a semiconductor, consider the energy bands for germanium. We show in Fig. {numref}`fig-p2-ch03-6` the $E(\mathbf{k})$ vs. $\mathbf{k}$ along the $\Delta(100)$ axis, $\Lambda(111)$ axis and $\Sigma(110)$ axes for no spin-orbit interaction and with spin-orbit interaction.

:::{figure} images/fig-p2-ch03-6.png
:name: fig-p2-ch03-6
:width: 90%
:align: center
Fig. 3.6: Energy bands of Ge: (a) without and (b) with spin-orbit interaction.
:::

As an example of the effect of the spin-orbit interaction, consider the valence band at the $\Gamma$-point ($\mathbf{k}=0$) which is labeled by $\Gamma_{25'}$ when there is no spin-orbit interaction. The $\Gamma_{25'}$ band is triply degenerate at $\mathbf{k}=0$, each of the three orbital levels containing a spin up and a spin down electron. With spin-orbit interaction, this band splits into the $\Gamma_8^+$ (doubly degenerate) band and the $\Gamma_7^+$ (non-degenerate) band. In the literature, the $\Gamma_7^+$ band is called the *split-off band*. In germanium the band gap is $0.8\,\text{eV}$ and the splitting between the $\Gamma_8^+$ and $\Gamma_7^+$ bands is $0.3\,\text{eV}$. However, in InSb, the spin-orbit interaction is large and the separation between the upper valence band and the split-off band is $0.9\,\text{eV}$, which is much larger than the band gap of $0.2\,\text{eV}$ between the valence and conduction bands.
