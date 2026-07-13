---
title: "3 Diamagnetism and Paramagnetism of Bound Electrons"
abstract: "Diamagnetic and paramagnetic response of bound (core) electrons: the magnetic interaction Hamiltonian, Larmor diamagnetism, Van Vleck paramagnetism, the Langevin and Brillouin functions, crystal-field theory, and quenching of orbital angular momentum."
---

# 3 Diamagnetism and Paramagnetism of Bound Electrons

## 3.1 Introductory Remarks

The magnetic properties of solids are described quantitatively in terms of the magnetization $\vec{M}$ which is defined as the magnetic moment per unit volume. Most solids are only weakly magnetic and develop a magnetization only when an external magnetic field is applied. In such cases, the amount of magnetization that is developed depends upon the magnitude of the magnetic susceptibility $\chi$ which is defined by

```{math}
:label: eq-p3-ch03-1
\vec{M} = \overleftrightarrow{\chi}\cdot\vec{H}
```

where $\overleftrightarrow{\chi}$ is in general a tensor in a crystalline solid. In Gaussian units, $\chi$ is dimensionless since $\vec{M}$ and $\vec{H}$ are both measured in the same units -- gauss. Materials for which $\chi > 0$ are denoted as paramagnetic and $\chi < 0$ are diamagnetic. Materials with a spontaneous magnetization (i.e., which exhibit a magnetization $\vec{M}$ without application of a magnetic field) typically have much larger values for $\chi$ and can be either ferromagnetic, antiferromagnetic or ferrimagnetic, as discussed in Chapter 7. In the present Chapter we focus on materials which are either diamagnetic or paramagnetic and do not exhibit spontaneous magnetization.

Magnetic moments in solids can be associated with both the conduction electrons and the ions (or closed shell valence electrons). In the case of electrons, magnetic moments are associated both with the orbital motion and with the spin angular momentum of these electrons. To understand the intimate connection between magnetic moments and angular momenta, we review here a few basic definitions.

In cgs units, the magnetic induction $\vec{B}$ is related to the magnetic field $\vec{H}$ through the permeability

```{math}
:label: eq-p3-ch03-2
\vec{B} = \overleftrightarrow{\mu}\cdot\vec{H} = \vec{H} + 4\pi\vec{M} = \vec{H} + 4\pi\overleftrightarrow{\chi}\cdot\vec{H} = (\overleftrightarrow{1} + 4\pi\overleftrightarrow{\chi})\cdot\vec{H}
```

and

```{math}
:label: eq-p3-ch03-3
\overleftrightarrow{\mu} = \overleftrightarrow{1} + 4\pi\overleftrightarrow{\chi} \geq 0
```

where $\overleftrightarrow{1}$ is the unit second rank tensor having $1$'s along the main diagonal and zero elsewhere. The condition $1 + 4\pi\chi \geq 0$ is required by thermodynamic stability so that the maximum diamagnetic susceptibility is $\chi = -1/4\pi$, which is the value of $\chi$ for a superconductor that has complete exclusion of the magnetic flux ($B = 0$).

The field variables $\vec{B}$ and $\vec{E}$ are directly derived from the vector and scalar potentials $\vec{A}$ and $\phi$ respectively:

```{math}
:label: eq-p3-ch03-4
\vec{E} = -\vec{\nabla}\phi - \frac{1}{c}\frac{\partial\vec{A}}{\partial t}
```

```{math}
:label: eq-p3-ch03-5
\vec{B} = \vec{\nabla}\times\vec{A} .
```

The field variables are unique, but the potentials are not (i.e., a gauge transformation yields a new equivalent potential implying the same field variables)

```{math}
:label: eq-p3-ch03-6
\vec{A}' = \vec{A} + \vec{\nabla}g(\vec{r},t)
```

```{math}
:label: eq-p3-ch03-7
\phi' = \phi - \frac{1}{c}\frac{\partial g(\vec{r},t)}{\partial t}
```

where $g(\vec{r},t)$ is any analytic function and the gauge transformation given by Eqs. {eq}`eq-p3-ch03-6` and {eq}`eq-p3-ch03-7` does not change the fields in any way. In fact, we require that all measurable quantities be invariant under a gauge transformation.

The magnetic moment associated with the orbital angular momentum is (see §1.3)

```{math}
:label: eq-p3-ch03-8
\vec{\mu} = \frac{e}{2mc}\vec{L}
```

in which angular momentum for electrons in atomic states is quantized in units of $\hbar$ and therefore the magnetic moment is quantized in units of Bohr magnetons $\mu_B$

```{math}
:label: eq-p3-ch03-9
\mu_B = \frac{e\hbar}{2mc} = -0.923\times 10^{-20}\ \text{ergs/gauss} .
```

The charged particles of solids, electrons and nuclei, not only have orbital angular momentum, but can also have spin angular momentum $\vec{S}$. A magnetic moment $\vec{\mu}$ is also associated with the spin angular momentum $\vec{S}$. Experimental studies of atomic spectra show that the magnetic moment associated with the electron spin can be related to $\vec{S}$ by

```{math}
:label: eq-p3-ch03-10
\vec{\mu} = \frac{e g_s}{2mc}\vec{S}
```

where $g_s$ is the $g$--factor which is $2$ for free electrons. Since $e$ is a negative number, the magnetic moment and spin are antiparallel. This $g$--factor is introduced so that an equivalent relation between the angular momentum and the magnetic moment will be valid for both spin and orbital angular momentum. In a solid, the $g$--factor (or effective $g$--factor) can differ from $2$, and can in fact be either positive or negative.

In general for free electrons,

```{math}
:label: eq-p3-ch03-11
\vec{\mu} = \frac{e g_\ell}{2mc}\vec{L} + \frac{e g_s}{2mc}\vec{S} = \frac{e}{2mc}(\vec{L} + 2\vec{S}) = \frac{e}{2mc}(\vec{J} + \vec{S}) = \frac{\mu_B}{\hbar}(\vec{J} + \vec{S}) .
```

Because the $g$--factor for the electron spin $g_s$ is $2$, and not unity, we say that $g_s$ is anomalous. Furthermore, since $g_s = 2$, the magnetic moment $\vec{\mu}$ is not directed along $\vec{J}$, so that $\vec{\mu}$ and $\vec{J}$ cannot be simultaneously diagonalized, and $\vec{\mu}$ and $\vec{J}$ are operators that do not commute.

Magnetic moment can be associated with either orbital motion or with spin. Because of the larger nuclear mass, nuclear moments are several orders of magnitude smaller than are the electronic magnetic moments. Nuclear moments are widely studied by the nuclear magnetic resonance technique and provide a valuable and sensitive local probe for studying solids. Nevertheless, the small magnitude of the nuclear moments allows us to neglect them in computing the static magnetization of solids.

The magnetic moment associated with the spin is a permanent moment which is present whether or not a magnetic field is present. On the other hand, the magnetic moment associated with the orbital motion of the electrons is proportional to the applied magnetic field and is called an *induced moment*. By Lenz's law, the induced moment is always negative and leads to diamagnetic effects.

In calculating the magnetization, we will often need to resort to a statistical approach, because we cannot hope to specify the detailed state of the system. In treating the orbital and spin angular momenta, we must also consider the coupling between $\vec{L}$ and $\vec{S}$ through the spin-orbit interaction. For atoms with high atomic number, the spin-orbit interaction will be large compared with effects associated with laboratory magnetic fields. To determine whether the spin-orbit interaction or the energy associated with magnetic field interactions is larger, we now consider the orders of magnitude of magnetic interactions in solids. Magnetic energies in solids are generally small compared with electronic energies. That is, electronic energy gaps are of the order $1$ eV while magnetic energies are typically in the millivolt range. A useful table showing the order of magnitude of magnetic quantities is given in Table {numref}`tab-p3-ch03-1`. We note that the highest dc fields presently available are under $40$ tesla, though pulsed fields of over $100$ tesla have been achieved.

:::{table} Table 3.1: The magnitude of various magnetic quantities at several values of magnetic field.
:name: tab-p3-ch03-1

| Quantity | $0.1$ tesla | $1.0$ tesla | $10.0$ tesla | units |
|---|---:|---:|---:|---|
| Energy of 1 Bohr magneton $\mu_B B$ | $0.5\times 10^{-5}$ | $0.5\times 10^{-4}$ | $0.5\times 10^{-3}$ | eV |
| Equivalent temperature $\mu_B B/k_B$ | $0.06$ | $0.6$ | $6$ | deg K |
| Cyclotron frequency $eB/mc = \omega_c$ | $2\times 10^{10}$ | $2\times 10^{11}$ | $2\times 10^{12}$ | rad/sec |
| $f_c = \omega_c/2\pi$ | $3\times 10^{9}$ | $3\times 10^{10}$ | $3\times 10^{11}$ | Hz |
| $\lambda_c = c/f_c$ | $10$ | $1$ | $0.1$ | cm |
| $\hbar\omega_c$ | $10^{-5}$ | $10^{-4}$ | $10^{-3}$ | eV |
:::

Inspection of Table {numref}`tab-p3-ch03-1` shows us immediately why most experiments involving magnetic energies of these magnitudes must be carried out at high magnetic fields and low temperatures. To have sharply defined magnetic energy levels we require the magnetic energies $\mu_B B \gg k_B T$, where $k_B$ is Boltzmann's constant. Inspection of Table {numref}`tab-p3-ch03-1` also shows why cyclotron resonance experiments are easier to carry out in semiconductors where the effective masses are typically in the range $m^*/m \sim 0.1$ so that the cyclotron frequency in such semiconductors is one order of magnitude higher than for a free electron at the same value of the $B$ field. Typical semimetals also have carriers with small effective masses, and therefore exhibit relatively large magnetic field interactions.

Typical energies for nuclear magnetic effects are reduced by three to four orders of magnitude from the values given in Table {numref}`tab-p3-ch03-1`. For this reason nuclear resonance experiments are usually performed at radio frequencies whereas electron spin resonance experiments are performed at microwave frequencies. The lower energies for nuclear magnetism can be exploited in such experiments as adiabatic magnetization and nuclear polarization (Overhauser effect). In adiabatic demagnetization, the demagnetization of the electronic system results in the generation of temperatures in the millidegree K range. On the other hand, the demagnetization of the nuclear system yields temperatures in the $10^{-6}$ deg K range because $\mu_N \sim 10^{-3}\mu_B$ where $\mu_N$ is the nuclear magneton. Although the magnitude of nuclear magnetism is small compared with electronic effects, nuclear magnetism is of considerable theoretical and practical interest for ultra-low temperature science and technology, as well as for magnetic imaging and for the chemical characterization of crystalline materials.

## 3.2 The Hamiltonian for Magnetic Interactions for Bound Electrons

Now that we have a feeling for the small order of magnitude involved in the weak magnetic effects in solids, let us look more closely into how we would calculate the energies of electrons in magnetic systems. Using the one-electron Hamiltonian approach to solids, we can write the Hamiltonian which includes the effects of the electromagnetic field and of the permanent magnetic moments as:

```{math}
:label: eq-p3-ch03-12
H = \frac{[\vec{p} - (e/c)\vec{A}]^2}{2m} + e\phi + V(\vec{r}) - \vec{\mu}_p\cdot\vec{B}
```

in which we have not included the spin-orbit interaction but have included the effect of a magnetic field through the vector potential $\vec{A}$, an electric field through the potential $\phi$, the periodic potential through $V(\vec{r})$, and permanent magnetic moments through the $\vec{\mu}_p\cdot\vec{B}$ term. To include the spin-orbit interaction, we must add to Eq. {eq}`eq-p3-ch03-12` a term $H_{s-o} = [1/(2m^2 c^2)]\vec{S}\cdot(\vec{\nabla}V\times\vec{p})$ and in the presence of electromagnetic fields we replace $\vec{p}\rightarrow\vec{p}-(e/c)\vec{A}$ in this relation for $H_{s-o}$. If we are dealing with the problem of a static electric field, we can set the vector potential equal to zero and consider only the scalar potential $\phi$. If we are considering a static magnetic field, we can set the scalar potential $\phi = 0$ and consider only the vector potential $\vec{A}$. If we are considering an electromagnetic field ($\omega\neq 0$), then we can also choose our gauge so that $\phi = 0$.

The $\vec{\mu}_p\cdot\vec{B}$ term takes into account the permanent magnetic moments in a solid which arise, for example, from the electron spin. Thus (neglecting for the moment the spin-orbit interaction), we can write the Hamiltonian (Eq. {eq}`eq-p3-ch03-12`) for an electron in a magnetic field as

```{math}
:label: eq-p3-ch03-13
H = H_0 - \frac{e}{2mc}(\vec{p}\cdot\vec{A} + \vec{A}\cdot\vec{p}) + \frac{e^2 A^2}{2mc^2} + e\phi - \vec{\mu}_p\cdot\vec{B}
```

where $H_0 = p^2/2m + V(\vec{r})$ is the Hamiltonian for an electron in a crystalline solid in zero field. No assumption on the commutivity of $\vec{p}$ and $\vec{A}$ is made in writing Eq. {eq}`eq-p3-ch03-13`. For simplicity we can neglect $\phi$ and the commutator $[p, A]$ to obtain a perturbation Hamiltonian for an electron in a solid

```{math}
:label: eq-p3-ch03-14
H' = -\frac{e}{mc}\vec{p}\cdot\vec{A} + \frac{e^2 A^2}{2mc^2} - \vec{\mu}_p\cdot\vec{B} .
```

We can also introduce the interaction of an electron in a magnetic field through the perturbation Hamiltonian

```{math}
:label: eq-p3-ch03-15
H' = -\vec{\mu}_{\text{total}}\cdot\vec{B} = -\frac{e}{mc}(\vec{L} + 2\vec{S}) .
```

For specific solid state problems either Eq. {eq}`eq-p3-ch03-13` or Eq. {eq}`eq-p3-ch03-15` are used.

Since Eq. {eq}`eq-p3-ch03-13` contains the vector potential explicitly it is convenient to use a specific gauge to write the Hamiltonian for magnetic interactions. In the case of a static magnetic field, we can set $\phi = 0$ and the uniform magnetic field in the $z$ direction is derived from a vector potential

```{math}
:label: eq-p3-ch03-16
\vec{A} = \frac{1}{2}(\vec{B}\times\vec{r})
```

with components (in the symmetric gauge)

```{math}
:label: eq-p3-ch03-17
A_x = -\frac{1}{2}yB, \qquad A_y = \frac{1}{2}xB, \qquad A_z = 0
```

which is substituted into the perturbation Hamiltonian of Eq. {eq}`eq-p3-ch03-14`. Then writing $p_j = (\hbar/i)(\partial/\partial x_j)$ and

```{math}
:label: eq-p3-ch03-18
\vec{\mu}_p = \frac{g_s e}{2mc}\vec{S}
```

the perturbation Hamiltonian of Eq. {eq}`eq-p3-ch03-14` for an electron in an external magnetic field becomes

```{math}
:label: eq-p3-ch03-19
H' = \frac{ie\hbar B}{2mc}\left(x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x}\right) + \frac{e^2 B^2}{8mc^2}(x^2 + y^2) - \frac{g_s e}{2mc}\vec{S}\cdot\vec{B}
```

where the first term follows from $-(e/2mc)\vec{L}\cdot\vec{B}$ and gives rise to a paramagnetic contribution to $\chi$. However, the second term in Eq. {eq}`eq-p3-ch03-19` which is proportional to $B^2$ gives rise to a diamagnetic contribution to the susceptibility. The final term in Eq. {eq}`eq-p3-ch03-19` is again paramagnetic and proportional to $\vec{B}$ and is due to the interaction of the spin angular momentum of the electron with the magnetic field.

## 3.3 Diamagnetism of Bound Electrons

All atoms in gases, liquids and solids exhibit a diamagnetic contribution to the total susceptibility. The origin of this effect can be understood from very elementary considerations, both from the standpoint of classical physics and quantum mechanics.

We first give a classical derivation of the diamagnetic susceptibility of bound electrons. When a magnetic field is applied, the electrons will move to set up a current to oppose the change in magnetic flux. According to the definition of the magnetic moment $\vec{\mu}$ (given in §1.3), we will now show that each electron will contribute to the diamagnetic moment $\vec{\mu}$. Suppose that there are $Z$ electrons in an atom. Then

```{math}
:label: eq-p3-ch03-20
\vec{\mu} = \frac{Ze}{2c}(\vec{r}\times\vec{v}) = \frac{Ze}{2c}\,\omega\langle\rho_r^2\rangle\,\hat{b}
```

where $\hat{b}$ is a unit vector along $\vec{B}$ and $\rho_r$ is the distance of an electron from the center of its magnetic field-induced orbit in a plane $\perp$ to the magnetic field, and $\omega$ is the Larmor frequency of precession for a bound electron, where $\omega = -eB/2mc$. We therefore obtain

```{math}
:label: eq-p3-ch03-21
\vec{\mu} = -\frac{Ze^2\vec{B}}{4mc^2}\langle\rho_r^2\rangle
```

which is independent of temperature. This moment is induced and is not present as $B\rightarrow 0$. The diamagnetic susceptibility is then [$\chi = (\partial\vec{\mu}/\partial\vec{H})/\text{volume}$]

```{math}
:label: eq-p3-ch03-22
\chi = -\frac{Ne^2 Z}{4mc^2}\,\hat{\mu}\,\langle\rho_r^2\rangle
```

where $N$ is the atomic density and the permeability $\hat{\mu}\simeq 1$. The quantity $\langle\rho_r^2\rangle$ in Eq. {eq}`eq-p3-ch03-22` is related to the orbit made by an electron moving in a magnetic field is not well defined classically. However, Eq. {eq}`eq-p3-ch03-22` tells us that if $\langle\rho_r^2\rangle$ is large, the electrons will give a greater contribution to the diamagnetic susceptibility. The simple classical approach given above provides us with the magnitude and functional dependence for the diamagnetic contribution to $\chi$, though we must still calculate $\langle\rho_r^2\rangle$. Our classical model is that electrons in an atom are arranged in shells. Without a magnetic field, the electrons assume a spherically symmetric state of motion in each shell. In a magnetic field, it is only the motion perpendicular to the field that is relevant to the magnetic properties. In this plane there will be a net circulation of charge for each atomic shell, characterized by the Larmor frequency.

To give a more satisfactory description of orbital diamagnetism, we will now give a quantum mechanical derivation of $\chi(T)$ and explicitly consider the charge distribution for electrons in bound states. The one-electron perturbation Hamiltonian of Eq. {eq}`eq-p3-ch03-19` is the basis of the quantum mechanical treatment.

Let us for the moment just deal with the diamagnetic term

```{math}
:label: eq-p3-ch03-23
H'_{\text{dia}} = \frac{e^2 B^2}{8mc^2}(x^2 + y^2)
```

that appears in Eq. {eq}`eq-p3-ch03-19`. Since it is small, it can be handled in perturbation theory. Then, in first-order perturbation theory, we get a correction to the electron energy $E^{(1)}_{\text{dia}}$ due to the diamagnetism of the bound electrons:

```{math}
:label: eq-p3-ch03-24
E^{(1)}_{\text{dia}} = \frac{e^2 B^2}{8mc^2}\sum_i \langle\psi_i^0|\rho_r^2|\psi_i^0\rangle
```

and the matrix element of $\rho_r^2$ is summed over all electrons. In the spirit of perturbation theory the diagonal matrix element of $\rho_r^2 = (x^2+y^2)$ in Eq. {eq}`eq-p3-ch03-24` is generally calculated for zero magnetic field between ground state electronic wave functions $\psi_i^0$.

We can interpret the diamagnetic energy of Eq. {eq}`eq-p3-ch03-24` as arising from a magnetic moment induced by the field and directed along the field. Thus, according to the definition of the magnetic moment we obtain

```{math}
:label: eq-p3-ch03-25
\vec{\mu} = -\frac{\partial\vec{E}_{\text{dia}}}{\partial\vec{B}} = -\frac{e^2\vec{B}}{4mc^2}\sum_i \langle\rho_r^2\rangle
```

where $\langle\rho_r^2\rangle$ denotes the diagonal matrix elements appearing in Eq. {eq}`eq-p3-ch03-24` and the sum in Eq. {eq}`eq-p3-ch03-25` is over all electrons in the atom. The quantum mechanical calculation of Eqs. {eq}`eq-p3-ch03-24` and {eq}`eq-p3-ch03-25` thus yield the same result for $\chi$ as was obtained classically (see Eq. {eq}`eq-p3-ch03-21`), only now we have a well-defined method for calculating this expectation value of $\rho_r^2$. For homework, we will evaluate $\vec{\mu}$ for a specific atomic system, hydrogen.

:::{figure} images/fig-p3-ch03-1.png
:name: fig-p3-ch03-1
:width: 55%
:align: center
Fig. 3.1: Diagram showing the orientation of the magnetic field relative to the axis of quantization of angular momentum in a crystal.
:::

If the magnitude of the diamagnetic interaction is sufficiently large, we must go to 2nd order perturbation theory. Then we get a second order contribution to $E_{\text{dia}}$ from the various excited states

```{math}
:label: eq-p3-ch03-26
E^{(2)}_{\text{dia}} = \sum \frac{|\langle\psi_0|H'_{\text{dia}}|\psi_{\text{excited}}\rangle|^2}{E_{\text{ground}} - E_{\text{excited}}}
```

where $H'_{\text{dia}}$ is given by Eq. {eq}`eq-p3-ch03-23`. Terms obtained in second order perturbation theory using Eq. {eq}`eq-p3-ch03-26` are sometimes important and must be considered for the following reason. Up until now we have assumed that the quantization of angular momentum is along the magnetic field. In a solid, we are likely to carry out the quantization in terms of the crystallographic axes. But then the magnetic field direction must be expressed with respect to the crystal coordinates, in which case the perturbation Hamiltonian (Eq. {eq}`eq-p3-ch03-23`) requires minor revision:

```{math}
:label: eq-p3-ch03-27
H' = \sum_i \frac{e^2 B^2}{8mc^2}\, r_i^2\cos^2\theta_i
```

where the summation is over all the electrons and $\theta_i$ is the angle between the magnetic field and the axis of quantization of the angular momentum (see Fig. {numref}`fig-p3-ch03-1`). In a solid the diamagnetic contribution to the magnetic moment may vanish in 1st order perturbation theory for certain magnetic field directions and we must go to 2nd order. It often turns out that the 2nd order term $E^{(2)}_{\text{dia}}$ is of the opposite sign to the 1st order term $E^{(1)}_{\text{dia}}$ and, therefore, $E^{(2)}_{\text{dia}}$ gives a paramagnetic contribution to $\chi$ (compare with the first order term in Eq. {eq}`eq-p3-ch03-24` which gives a diamagnetic contribution to $\chi$):

```{math}
:label: eq-p3-ch03-28
E^{(2)}_{\text{dia}} = +2\frac{|\langle\psi_0|H'_{\text{dia}}|\psi_{\text{excited}}\rangle|^2}{E_0 - E_{\text{excited}}} = -2\frac{|\langle\psi_0|H'_{\text{dia}}|\psi_{\text{excited}}\rangle|^2}{E_g}
```

where for simplicity we consider only one excited state and $E_g$ is the energy gap between the ground state and the excited state. The paramagnetic contribution in Eq. {eq}`eq-p3-ch03-28` is called *Van-Vleck paramagnetism*. Like $E^{(1)}_{\text{dia}}$, the second order term $E^{(2)}_{\text{dia}}$ originates from purely orbital motion and like $E^{(1)}_{\text{dia}}$ is temperature independent. In general, the most important contribution from the orbital motion comes in first-order perturbation theory and we don't have to worry about second order terms. We have just included this idea into the present discussion to show that the orbital motion may give rise to both diamagnetic and paramagnetic contributions.

For the inert gases, the only contribution to the magnetism from the bound state electrons is the diamagnetic contribution and typical experimental values for the magnetic susceptibility are:

- Helium ($Z=2$): $\chi_{\text{molar}} \sim -1.9\times 10^{-6}\ \text{cm}^3/\text{mole}$
- Xenon ($Z=54$): $\chi_{\text{molar}} \sim -43\times 10^{-6}\ \text{cm}^3/\text{mole}$

Neglecting for the moment that the electrons in xenon occupy several different atomic shells (or have different principal quantum numbers), since xenon has $54$ electrons compared to $2$ for helium, we can get a rough check on the idea that all electrons contribute to diamagnetism from the product $(1.9)(27) \simeq 51$.

## 3.4 Paramagnetism of Bound Electrons

Whereas all atoms possess core diamagnetism, not all atoms possess core paramagnetism. Referring to Eq. {eq}`eq-p3-ch03-19`, the perturbation Hamiltonian which describes the paramagnetism due to the bound electrons is

```{math}
:label: eq-p3-ch03-29
H'_{\text{para}} = \sum_i -\frac{e}{2mc}(\vec{L}_i + 2\vec{S}_i)\cdot\vec{B} = -\vec{\mu}_{\text{para}}\cdot\vec{B}
```

where

```{math}
:label: eq-p3-ch03-30
\vec{\mu}_{\text{para}} = \frac{e}{2mc}\sum_i (\vec{L}_i + 2\vec{S}_i) .
```

Thus if we have a closed atomic shell, the total $\vec{L}$ and total $\vec{S}$ both vanish and $H'_{\text{para}}$ vanishes too. For helium, as an example, both electrons are in $s$-states (zero angular momentum) and have antiparallel spins, so that there is no paramagnetic contribution due to the bound electrons.

The calculation for the paramagnetism for the bound electrons characteristically is treated in two parts:

1. determination of the moment $\vec{\mu}_{\text{para}}$
2. a statistical calculation of the average of $\vec{\mu}_{\text{para}}$.

With regard to the calculation of $\vec{\mu}_{\text{para}}$, it may be carried out either classically (approximately valid for large values of the angular momentum) or quantum mechanically. With regard to the statistical problem, thermal disorder acts to randomize the alignment of the moments by the magnetic field so that the average value of $\vec{\mu}_{\text{para}}$ will be temperature dependent, in contrast to the situation for the diamagnetism for the bound electrons which is independent of temperature.

For paramagnetic materials, Eq. {eq}`eq-p3-ch03-30` shows that the magnetic moment is independent of the magnetic field but is a property of the atomic system; such moments are called *permanent moments*, in contrast to moments which are induced by the presence of a magnetic field, such as the case for the diamagnetic contribution to $\chi$ which is discussed in §3.3. The magnetic field tends to line up the moments and thermal energy tends to randomize the orientation of the magnetic moments.

We will first give a classical derivation of Curie's law which provides a good way to think about paramagnetic systems, even if it must later be refined to take into account the quantum mechanical aspects of the problem.

The interaction energy of a magnetic moment with the magnetic field is

```{math}
:label: eq-p3-ch03-31
E = -\vec{\mu}_{\text{para}}\cdot\vec{B} .
```

Insofar as the magnetic energy tends to be small compared with the thermal energy, the permanent moments can be excited by thermal excitation to higher energy states whereby $\vec{\mu}_{\text{para}}$ is no longer along $\vec{B}$. Thus the average energy at temperature $T$ is found by performing a statistical average through summing over all states

```{math}
:label: eq-p3-ch03-32
\langle E\rangle = \frac{\sum [-\vec{\mu}_{\text{para}}\cdot\vec{B}]\,e^{\vec{\mu}_{\text{para}}\cdot\vec{B}/k_B T}}{\sum e^{\vec{\mu}_{\text{para}}\cdot\vec{B}/k_B T}}
```

where we have written $k_B$ for Boltzmann's constant. In doing the problem classically, $\vec{\mu}_{\text{para}}$ and $\vec{B}$ can make any arbitrary angle with respect to each other (this is not so quantum-mechanically). Classically we can write

```{math}
:label: eq-p3-ch03-33
\cos\theta = \frac{\vec{\mu}_{\text{para}}\cdot\vec{B}}{|\mu_{\text{para}}|B}
```

so that the sums in Eq. {eq}`eq-p3-ch03-32` become integrals over $\theta$. Let $x = \mu_{\text{para}}B/k_B T \ll 1$ where $x$ denotes the ratio of the magnetic energy to the thermal energy and also let $y = \cos\theta$. We now perform an angular integration as indicated in

```{math}
:label: eq-p3-ch03-34
\int_0^{2\pi} d\phi \int_0^\pi \sin\theta\,d\theta ,
```

where we use the coordinate system in Fig. 1.1 (original). If we set $y = \cos\theta$, then

```{math}
:label: eq-p3-ch03-35
\langle E\rangle = -\mu_{\text{para}}B\,\frac{\int_{-1}^{1}e^{xy}y\,dy}{\int_{-1}^{1}e^{xy}\,dy}
```

and

```{math}
:label: eq-p3-ch03-36
\langle E\rangle = -\mu_{\text{para}}B\,\frac{d}{dx}\ln\int_{-1}^{1}e^{xy}\,dy = -\mu_{\text{para}}B\cdot\frac{d}{dx}\ln(e^x - e^{-x}) - \frac{d}{dx}\ln x
```

```{math}
:label: eq-p3-ch03-37
= -\mu_{\text{para}}B\left(\coth x - \frac{1}{x}\right) \equiv -\mu_{\text{para}}B\,L(x)
```

where $L(x)$ is the dimensionless Langevin function shown in Fig. {numref}`fig-p3-ch03-2`. A Taylor expansion of $\coth x$ for small $x$ is

```{math}
:label: eq-p3-ch03-38
\coth x = \frac{1}{x} + \frac{x}{3} - \frac{x^3}{45} + \cdots
```

so that

```{math}
:label: eq-p3-ch03-39
L(x) = \frac{x}{3} - \frac{x^3}{45} + \cdots
```

is the expansion of $L(x)$ for small $x$. For very small $x$, we retain only the leading term or

```{math}
:label: eq-p3-ch03-40
L(x) \simeq \frac{x}{3} = \frac{\mu_{\text{para}}B}{3k_B T} .
```

:::{figure} images/fig-p3-ch03-2.png
:name: fig-p3-ch03-2
:width: 60%
:align: center
Fig. 3.2: Plot of the dependence of the Langevin function $L(x)$ on $x$ (solid curve) where $L(x) = \coth x - (1/x)$ and $x = \mu_{\text{para}}B/k_B T$. For small $x$, $L(x) \sim x/3$ (dashed curve).
:::

Since $\langle E\rangle = -\langle\mu_{\text{para}}\rangle B$ we have for the thermal average $\langle\mu_{\text{para}}\rangle$

```{math}
:label: eq-p3-ch03-41
\langle\mu_{\text{para}}\rangle = \frac{\mu_{\text{para}}^2 B}{3k_B T}
```

so that

```{math}
:label: eq-p3-ch03-42
\chi_{\text{para}} = \frac{N\mu_{\text{para}}^2\hat{\mu}}{3k_B T} = \frac{C}{T}
```

where $C$ is Curie's constant and $\hat{\mu}$ is the permeability. Equation {eq}`eq-p3-ch03-42` which expresses a proportionality between $\chi_{\text{para}}$ and $1/T$ is called the *Curie law*.

From this treatment you see that the Curie law, which gives the functional form of $\chi_{\text{para}}(T)$ as $1/T$ is only approximate. That is, classically the temperature dependence of $\chi_{\text{para}}$ is given by the Langevin function $L(x)$ shown in Fig. {numref}`fig-p3-ch03-2`, which reduces to the Curie relation for small $x$ when the magnetic energy is much less than the thermal energy. At low temperatures we would expect departures from the $1/T$ law according to the plot shown in Fig. {numref}`fig-p3-ch03-2`. When we do the problem quantum-mechanically below, we will find that yet another function applies. Nevertheless, saturation effects, as suggested by the Langevin function, are observed experimentally as shown in Fig. {numref}`fig-p3-ch03-3`. From the discussion given so far, we conclude that if we want to enhance the paramagnetic behavior, we need to go to low temperatures and if we want to enhance the diamagnetic behavior we need to go to high fields.

:::{figure} images/fig-p3-ch03-3.png
:name: fig-p3-ch03-3
:width: 60%
:align: center
Fig. 3.3: Plot of magnetic moment versus $H/T$ for spherical samples of (I) potassium chromium alum, (II) ferric ammonium alum, and (III) gadolinium sulfate octahydrate. Over 99.5% magnetic saturation is achieved at a low temperature of $1.3$ K and a field of about $50{,}000$ gauss. The fit to the experimental data makes use of Eq. {eq}`eq-p3-ch03-52` which expresses the magnetic moment in terms of a Brillouin function. [After W.E. Henry, Phys. Rev. 88, 559 (1952)]
:::

Now let us think about the changes that we must make in the above treatment to make it quantum-mechanical. For one thing, we must find an explicit expression for $\mu_{\text{para}}$ by finding the expectation value of the magnetic moment operator in an eigenstate of the total Hamiltonian $H'_{\text{para}}$ in Eq. {eq}`eq-p3-ch03-29` in the $|\ell, s, j, m_j\rangle$ representation. The magnetic moment can be found easily using the vector model.

By treating the magnetic moment as a quantized operator, we can using Eqs. 1.127 and 1.133 (original) write the quantum mechanical energy levels in the form

```{math}
:label: eq-p3-ch03-43
E_j = -m_j g\mu_B B
```

:::{figure} images/fig-p3-ch03-4.png
:name: fig-p3-ch03-4
:width: 70%
:align: center
Fig. 3.4: (a) Equally spaced levels for different $m_j$ values $-j \leq m_j \leq j$ in a magnetic field where the Zeeman splitting between adjacent levels is $g\mu_B B$ where $g$ is the Landé $g$--factor. (b) For a 2-level, spin up and spin down system, the Zeeman splitting is $2\mu_B B$.
:::

where $g$ is the Landé $g$--factor

```{math}
:label: eq-p3-ch03-44
g = 1 + \frac{j(j+1) + s(s+1) - \ell(\ell+1)}{2j(j+1)}
```

and $\mu_B$ is the Bohr magneton. These magnetic energy levels are equally spaced, since the quantum number $m_j$ is either an integer or half-integer and can assume values

```{math}
:label: eq-p3-ch03-45
m_j = j,\, j-1,\, \ldots,\, -j .
```

For a two level spin up and spin down system, we have $s = 1/2$ and $\ell = 0$, $g = 2$, $m_j = \pm 1/2$ and $E = \pm\mu_B B$, while for a more general set of quantum numbers we have an equally spaced set of Zeeman levels shown in Fig. {numref}`fig-p3-ch03-4`(a).

Quantum mechanically the mean value for the magnetic moment is found, as before, by computing the mean energy

```{math}
:label: eq-p3-ch03-46
\langle E\rangle = \frac{\sum_{m_j} e^{m_j g\mu_B B/k_B T}(-m_j g\mu_B B)}{\sum_{m_j} e^{m_j g\mu_B B/k_B T}} .
```

To simplify the notation let $x = g\mu_B B j/k_B T$ where $j$ is the maximum value which $m_j$ can assume. Physically, $x$ denotes the ratio between the magnetic energy and the thermal energy. The sums in Eq. {eq}`eq-p3-ch03-46` can be related to geometric series by recognizing that

```{math}
:label: eq-p3-ch03-47
\langle E\rangle = -\frac{g\mu_B B}{j}\frac{\sum_{m_j}(m_j/j)e^{m_j x/j}}{\sum_{m_j}e^{m_j x/j}} = -\frac{g\mu_B B}{j}\left(\frac{\partial}{\partial x}\right)\ln\sum_{m_j=-j}^{j}e^{m_j x/j} .
```

The geometric sum in Eq. {eq}`eq-p3-ch03-47` then yields

```{math}
:label: eq-p3-ch03-48
\sum_{m_j=-j}^{j}e^{m_j x/j} = \frac{e^{(j+1)x/j} - e^{-j x/j}}{e^{x/j} - 1} = \frac{e^{(j+1/2)x/j} - e^{-(j+1/2)x/j}}{e^{x/2j} - e^{-x/2j}}
```

thereby giving the following results for the mean energy

```{math}
:label: eq-p3-ch03-49
\langle E\rangle = -g\mu_B B j\,\frac{\partial}{\partial x}\left[\ln\sinh\left(\frac{2j+1}{2j}x\right) - \ln\sinh\left(\frac{x}{2j}\right)\right]
```

```{math}
:label: eq-p3-ch03-50
= -g\mu_B B j\left[\frac{2j+1}{2j}\frac{\cosh\!\left(\frac{2j+1}{2j}x\right)}{\sinh\!\left(\frac{2j+1}{2j}x\right)} - \frac{1}{2j}\frac{\cosh(x/2j)}{\sinh(x/2j)}\right]
```

so that

```{math}
:label: eq-p3-ch03-51
\langle E\rangle = -g\mu_B B j\left[\frac{2j+1}{2j}\coth\!\left(\frac{2j+1}{2j}x\right) - \frac{1}{2j}\coth\!\left(\frac{x}{2j}\right)\right] = -(g\mu_B B j)B_j(x)
```

where $B_j(x)$ is defined as the *Brillouin function*. By writing $\langle E\rangle = -\langle\mu_{\text{para}}\rangle B$, we can obtain the mean magnetic moment (thermal average) as

```{math}
:label: eq-p3-ch03-52
\langle\mu_{\text{para}}\rangle = g\mu_B j\,B_j(x)
```

and by multiplying $\langle\mu_{\text{para}}\rangle$ by $N$, the number of magnetic moments per unit volume, we obtain $N\langle E\rangle = -N\langle\mu_{\text{para}}\rangle B$, where $N\langle\mu_{\text{para}}\rangle$ is the magnetization per unit volume. The quantity $\langle\mu_{\text{para}}\rangle$ is plotted in Fig. {numref}`fig-p3-ch03-3` for several magnetic compounds with different $j = S$ values, yielding excellent agreement between the experimental data and $\langle\mu_{\text{para}}\rangle$ calculated from Eq. {eq}`eq-p3-ch03-52`.

The expansion of the Brillouin function for small $x$ is

```{math}
:label: eq-p3-ch03-53
B_j(x) = \frac{j+1}{3j}x - \frac{(j+1)^2 + j^2}{(j+1)\,90\,j^3}\,x^3 + \cdots
```

and this result can be used to derive Curie's law by writing $B_j(x) \simeq (j+1)/(3j)\,x$ for small $x$. Thus for $x\ll 1$,

```{math}
:label: eq-p3-ch03-54
\langle\mu_{\text{para}}\rangle \simeq g\mu_B j\,\frac{j+1}{3j}\,\frac{g\mu_B B j}{k_B T} = \frac{g^2\mu_B^2 j(j+1)}{3k_B T}
```

or

```{math}
:label: eq-p3-ch03-55
\chi_{\text{para}} = \frac{N\hat{\mu} g^2\mu_B^2 j(j+1)}{3k_B T} .
```

It is of interest to compare the quantum mechanical derivation of the Curie law to the classical derivation of Eq. {eq}`eq-p3-ch03-42`. A comparison of Eq. {eq}`eq-p3-ch03-42` and {eq}`eq-p3-ch03-55` suggests the identification of

```{math}
:label: eq-p3-ch03-56
\mu_{\text{para}}^2 \equiv g^2\mu_B^2 j(j+1)
```

where the $j$ and Landé $g$--factor $g$ for a particular magnetic species are found by quantum mechanics (see §1.6 original).

By making measurements of the temperature dependence of the magnetic susceptibility, we can determine the Curie constant $C$ which is defined by the Curie law

```{math}
:label: eq-p3-ch03-57
\chi_{\text{para}} = \frac{C}{T}
```

through Eq. {eq}`eq-p3-ch03-55` as

```{math}
:label: eq-p3-ch03-58
C = \frac{N\hat{\mu} g^2\mu_B^2 j(j+1)}{3k_B} .
```

The Curie law is very well obeyed by paramagnetic salts, as shown in Fig. {numref}`fig-p3-ch03-5` where $\chi$ is plotted vs. $1/T$. The points are experimental and the fit is to Eq. {eq}`eq-p3-ch03-57`.

:::{figure} images/fig-p3-ch03-5.png
:name: fig-p3-ch03-5
:width: 60%
:align: center
Fig. 3.5: Plot of the susceptibility per gram versus reciprocal temperature for powdered $\text{CuSO}_4\cdot\text{K}_2\text{SO}_4\cdot 6\text{H}_2\text{O}$, showing the Curie law temperature dependence. [After J.C. Hupse, Physica 9, 633 (1942).]
:::

In deriving Curie's law, we neglected any interactions between magnetic moments (called the dipole-dipole interaction). The dipole-dipole interaction $H_{\text{dip}}$ between magnetic moments $\vec{\mu}_1$ and $\vec{\mu}_2$ is given by

```{math}
:label: eq-p3-ch03-59
H_{\text{dip}} = \frac{1}{r^3}\left[\vec{\mu}_1\cdot\vec{\mu}_2 - 3(\vec{\mu}_1\cdot\hat{r})(\vec{\mu}_2\cdot\hat{r})\right]
```

where $\vec{r}$ is the vector between the dipoles and $\hat{r}$ is a unit vector along $\vec{r}$. The dipole-dipole interaction tends to line up a dipole due to the magnetic field generated by neighboring dipoles.

## 3.5 Angular Momentum States in Paramagnetic Ions

Some paramagnetic systems that have important practical applications (such as laser materials) are insulating host crystals containing a small concentration of paramagnetic impurities. The paramagnetic susceptibility in the low field limit is found by the Curie law

```{math}
:label: eq-p3-ch03-60
\chi_{\text{para}} = \frac{N\hat{\mu}\mu_{\text{para}}^2}{3k_B T}
```

where $\mu_{\text{para}}$ is given by Eq. {eq}`eq-p3-ch03-56` in which $j$ and $g$ are found by the vector model. Experimental values for $\mu_{\text{para}}$ for the rare earth ions are given in Table {numref}`tab-p3-ch03-2` where $p$ is defined by $p^2 = g^2 j(j+1)$ where $p$ physically denotes the effective number of Bohr magnetons.

:::{table} Table 3.2: Effective magneton numbers $p$ for trivalent lanthanide group ions (near room temperature).
:name: tab-p3-ch03-2

| Ion | Configuration | Basic level | $p$ (calc) | $p$ (exp) |
|---|---|---|---:|---:|
| $\text{Ce}^{3+}$ | $4f^1 5s^2 p^6$ | $^2F_{5/2}$ | $2.54$ | $2.4$ |
| $\text{Pr}^{3+}$ | $4f^2 5s^2 p^6$ | $^3H_4$ | $3.58$ | $3.5$ |
| $\text{Nd}^{3+}$ | $4f^3 5s^2 p^6$ | $^4I_{9/2}$ | $3.62$ | $3.5$ |
| $\text{Pm}^{3+}$ | $4f^4 5s^2 p^6$ | $^5I_4$ | $2.68$ | $-$ |
| $\text{Sm}^{3+}$ | $4f^5 5s^2 p^6$ | $^6H_{5/2}$ | $0.84$ | $1.5$ |
| $\text{Eu}^{3+}$ | $4f^6 5s^2 p^6$ | $^7F_0$ | $0$ | $3.4$ |
| $\text{Gd}^{3+}$ | $4f^7 5s^2 p^6$ | $^8S_{7/2}$ | $7.94$ | $8.0$ |
| $\text{Tb}^{3+}$ | $4f^8 5s^2 p^6$ | $^7F_6$ | $9.72$ | $9.5$ |
| $\text{Dy}^{3+}$ | $4f^9 5s^2 p^6$ | $^6H_{15/2}$ | $10.63$ | $10.6$ |
| $\text{Ho}^{3+}$ | $4f^{10} 5s^2 p^6$ | $^5I_8$ | $10.60$ | $10.4$ |
| $\text{Er}^{3+}$ | $4f^{11} 5s^2 p^6$ | $^4I_{15/2}$ | $9.59$ | $9.5$ |
| $\text{Tm}^{3+}$ | $4f^{12} 5s^2 p^6$ | $^3H_6$ | $7.57$ | $7.3$ |
| $\text{Yb}^{3+}$ | $4f^{13} 5s^2 p^6$ | $^2F_{7/2}$ | $4.54$ | $4.5$ |
:::

The comparison between the calculated and experimental values of $p$ in Table {numref}`tab-p3-ch03-2` shows the excellent agreement between the calculated and experimental values for $\mu_{\text{para}}$ for the various rare earth ions.

Although Table {numref}`tab-p3-ch03-2` is useful for describing the ground state of rare earth paramagnetic ions, it does not give information about the excited states. Information about the energy levels of the excited states are of great value to people who design laser materials. Such information is largely established by optical techniques. Many of the high power solid state lasers used commercially today involve a population inversion created between some excited levels of a paramagnetic rare earth ion in an ionic host material -- e.g. Nd:YAG. A R&D field that has been on-going for some time is the development of more efficient laser materials with lower operating thresholds and at more laser frequencies based on excited states of these rare earth ions.

## 3.6 Paramagnetic Ions and Crystal Field Theory

Crystal field theory is important for the discussion of the properties of paramagnetic ions (such as rare earth ions or transition metal ions) in a host crystal. Since the magnetic ions are well separated from each other, they behave like atomic entities and the treatment we have given in §3.5 is appropriate. There are several effects, however, that are different for paramagnetic ions in a solid as compared with a gas, including crystal field splittings and, in the case of transition metal ions, the quenching of the orbital angular momentum.

The basic assumption of crystal field theory is that the crystal is ionic. Each atom gives up or receives electrons to make a closed shell or a more stable electron configuration. Examples where crystal field theory applies are host materials, such as $\text{Al}_2\text{O}_3$ and MgO. Here, each ion is bonded to ions of opposite charge and the bonds are called ligands. We may assign a radius to each ion or ion core.

In crystal field theory (also called ligand field theory) we assume that the paramagnetic ion is surrounded by a set of point charges. We then find the electric potential $eV(r_i, \theta_i, \phi_i)$ produced by these ions and ligands and include this term in the Hamiltonian $H$ for the paramagnetic ion. This theory is most useful in magnetically dilute substances where paramagnetic ions are far apart. Examples where crystal field theory applies include $1\%$ $\text{Cr}^{3+}$ in $\text{Al}_2\text{O}_3$ (which constitutes a common laser material), and $1\%$ $\text{Er}^{3+}$ in $\text{LaCl}_3$. The Hamiltonian for the paramagnetic ion is given by

```{math}
:label: eq-p3-ch03-61
H = \sum_{i=1}^{n}\left[\frac{p_i^2}{2m} - \frac{e^2 Z}{r_i} + e^2\sum_{j>i}\frac{1}{r_{ij}}\right] + \lambda\vec{L}\cdot\vec{S} + \sum_{i=1}^{n} eV(r_i,\theta_i,\phi_i)
```

which can be written as:

```{math}
:label: eq-p3-ch03-62
H = H_{\text{ion}} + H_{s-o} + H_{\text{crystal field}}
```

where the sums are over all the electrons and $V(r_i,\theta_i,\phi_i)$ is the crystal field potential produced by the ligands at the site $r_i$. Figure {numref}`fig-p3-ch03-6` shows the splittings of the ionic energy levels by the crystal field and the spin-orbit interaction. There are three cases of interest, depending on the relative magnitudes of the crystal field potential and the spin-orbit interaction.

:::{figure} images/fig-p3-ch03-6.png
:name: fig-p3-ch03-6
:width: 70%
:align: center
Fig. 3.6: Crystal field splittings for a paramagnetic ion with a $(3d)^7$ configuration in the regime where the crystal field is much larger than the spin-orbit interaction. The transition metal compounds having incomplete $3d$-shells are in this category. Orbital angular momentum is quenched by the strong crystal field.
:::

1. **Strong Crystal Field** -- Here the crystal field is large compared with the spin-orbit interaction. Thus the crystal field breaks up the $\vec{L}\cdot\vec{S}$ coupling of the atomic electrons. Orbital angular momentum is quenched by the strong crystal field.

2. **Medium Crystal Field** -- Here the crystal field is of comparable magnitude to the spin-orbit interaction. Thus the crystal field breaks up the $\vec{L}\cdot\vec{S}$ coupling, but $\ell$ and $s$ remain good quantum numbers. $\text{Co}^{2+}$ and $\text{Ni}^{2+}$ with an incomplete $3d$ shell are in this category. Orbital angular momentum is usually quenched in part for this case.

3. **Weak Crystal Field** -- Here the crystal field is small compared with the spin-orbit interaction. Thus in this case $j$ is a good quantum number. Rare earth ions which have an incomplete $4f$ level belong to this case. $4f$ electrons are more shielded from their ligands than $3d$ electrons, and hence the crystal field is weaker for the $4f$ electrons.

The crystal field $V(r_i,\theta_i,\phi_i)$ is invariant under every symmetry operation which leaves the crystal structure invariant. The crystal field potential can be found by summing the potential of point charges of nearest neighbors, next nearest neighbors, etc. Therefore, the crystal field potential does not exhibit spherical symmetry but rather the symmetry of the crystalline lattice. Once the spherical symmetry is lifted, $\vec{J}$ is no longer a constant of the motion. By lowering the symmetry from full rotational symmetry of the free ion to the crystal symmetry of the lattice, certain degeneracies in the energy are lifted, as shown in Fig. {numref}`fig-p3-ch03-6`. A more detailed discussion of crystal field theory is given in a course on group theory.

A second effect which occurs in crystals with strong crystal fields is the quenching of the orbital angular momentum, which is discussed in the next section.

## 3.7 Quenching of Orbital Angular Momentum

Let us consider the quenching of the orbital angular momentum which occurs in materials with a strong crystal field. For simplicity consider an ion with a single electron in a $p$-state, with all other electrons being accommodated in a closed shell. Neglecting both the effect of the electron spin and of the spin-orbit interaction, we can write down three degenerate $p$-states:

```{math}
:label: eq-p3-ch03-63
Y_{1,1}(\theta,\phi)R_{n,\ell}(r) \propto \frac{x+iy}{\sqrt{2}}\,f(r)\quad [m=1], \qquad Y_{1,0}(\theta,\phi)R_{n,\ell}(r)\propto z\,f(r)\quad [m=0], \qquad Y_{1,-1}(\theta,\phi)R_{n,\ell}(r) \propto \frac{x-iy}{\sqrt{2}}\,f(r)\quad [m=-1].
```

Since $p$-states are degenerate in the free atom, we write them in a form that displays the crystal symmetry, as shown in Fig. {numref}`fig-p3-ch03-7`. The proper eigenfunctions to display a $p$-function in a cubic crystal field are $x f(r)$, $y f(r)$ and $z f(r)$ (see Fig. {numref}`fig-p3-ch03-7`). The energy levels are also indicated in this figure.

:::{figure} images/fig-p3-ch03-7.png
:name: fig-p3-ch03-7
:width: 70%
:align: center
Fig. 3.7: A schematic representation of the eigenfunctions (a), (b), (c) and energy eigenvalues (d) for a uniaxial crystal field along the $z$--direction and $L = 1$. In the free atom the states $m = +1, 0, -1$ have identical energies so that the states are degenerate. In the crystal the atom has a lower energy when the electron cloud is coupled to positive ions as in (a) than when it is oriented midway between them, as in (b) and (c). The wavefunctions that give rise to these charge densities are of the form $z f(r)$, $x f(r)$ and $y f(r)$ and are called the $p_z$, $p_x$, $p_y$ orbitals, respectively. In an axially symmetric field, as shown, the $p_x$ and $p_y$ orbitals are degenerate.
:::

Let us find the average value of $L_z$ (denoted by $\langle L_z\rangle$) for the $x f(r)$ state:

```{math}
:label: eq-p3-ch03-64
x f(r) = \frac{1}{\sqrt{2}}\left[\frac{x+iy}{\sqrt{2}}f(r) + \frac{x-iy}{\sqrt{2}}f(r)\right]
```

so that the expectation value for $L_z$ should be found from the following integral which we show below goes to zero

```{math}
:label: eq-p3-ch03-65
\int d^3r\; x f(r)\,L_z\,x f(r) = 0 .
```

More generally, using time inversion symmetry we see that, if the ground state eigenfunction is real, then $L_z$ is given by

```{math}
:label: eq-p3-ch03-66
L_z = \frac{\hbar}{i}\left(x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x}\right) ,
```

so that the expectation values for $L_z$ becomes

```{math}
:label: eq-p3-ch03-67
\langle\psi_0|L_z|\psi_0\rangle = \int \psi_0^* \frac{\hbar}{i}\left(x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x}\right)\psi_0\,d^3r .
```

For a ground state wave function $\psi_0$ that is real,

```{math}
:label: eq-p3-ch03-68
\langle L_z\rangle = \frac{\hbar}{i}\int \psi_0 \left(x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x}\right)\psi_0\,d^3r
```

which implies that $\langle L_z\rangle$ is pure imaginary. But $\langle L_z\rangle$ is an observable, so that $\langle L_z\rangle$ must be real. Hence $\langle L_z\rangle \equiv 0$ for the case of cubic symmetry. Similar arguments follow for crystals with other symmetries.

The quenching of the orbital angular momentum is important in the limit where the crystal field is large compared with the spin-orbit interaction. In this case, we continue to label states in the $|\ell, s, m_\ell, m_s\rangle$ representation so that the magnetic moment $(\vec{L} + 2\vec{S})$ yields an eigenvalue $(m_\ell + 2m_s)$. With the quenching of $\vec{L}$, we eliminate $\vec{L}$ from the problem and take $\vec{J} = \vec{S}$. This seems to be a good approximation for the transition metal ions, especially those with less than a half-filled $3d$ shell, as shown in Table {numref}`tab-p3-ch03-3`. Only partial quenching of $\vec{L}$ occurs experimentally for more than half-filled $3d$ shells. When the orbital angular momentum is quenched, then the effective paramagnetic moment is $p = 2\sqrt{s(s+1)}$ and we can forget about $\vec{L}$ in calculating both the Landé $g$--factor and the total angular momentum, consistent with the results in Table {numref}`tab-p3-ch03-3`.

:::{table} Table 3.3: A table showing the effective Bohr magnetons for various configurations of the $3d$ transition metal ions.
:name: tab-p3-ch03-3

| Ion | Config. | Basic Level | $p(\text{calc}) = g[j(j+1)]^{1/2}$ | $p(\text{calc}) = 2[s(s+1)]^{1/2}$ | $p(\text{exp})^a$ |
|---|---|---|---:|---:|---:|
| $\text{Ti}^{3+}, \text{V}^{4+}$ | $3d^1$ | $^2D_{3/2}$ | $1.55$ | $1.73$ | $1.8$ |
| $\text{V}^{3+}$ | $3d^2$ | $^3F_2$ | $1.63$ | $2.83$ | $2.8$ |
| $\text{Cr}^{3+}, \text{V}^{2+}$ | $3d^3$ | $^4F_{3/2}$ | $0.77$ | $3.87$ | $3.8$ |
| $\text{Mn}^{3+}, \text{Cr}^{2+}$ | $3d^4$ | $^5D_0$ | $0.00$ | $4.90$ | $4.9$ |
| $\text{Fe}^{3+}, \text{Mn}^{2+}$ | $3d^5$ | $^6S_{5/2}$ | $5.92$ | $5.92$ | $5.9$ |
| $\text{Fe}^{2+}$ | $3d^6$ | $^5D_4$ | $6.70$ | $4.90$ | $5.4$ |
| $\text{Co}^{2+}$ | $3d^7$ | $^4F_{9/2}$ | $6.63$ | $3.87$ | $4.8$ |
| $\text{Ni}^{2+}$ | $3d^8$ | $^3F_4$ | $5.59$ | $2.83$ | $3.2$ |
| $\text{Cu}^{2+}$ | $3d^9$ | $^2D_{5/2}$ | $3.55$ | $1.73$ | $1.9$ |
:::

$^a$ Representative values.
