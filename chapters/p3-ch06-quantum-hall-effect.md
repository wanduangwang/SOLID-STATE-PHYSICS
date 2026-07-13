---
title: "6 The Quantum Hall Effect (QHE)"
abstract: "The step-like quantization of the Hall resistance $\\rho_{xy}$ in units of $h/e^2$ in a two-dimensional electron gas, including the integer quantum Hall effect, edge channel interpretation, and the fractional quantum Hall effect."
---

# 6 The Quantum Hall Effect (QHE)

**References**

- Prange and Girvin, *The Quantum Hall Effect*, Springer-Verlag (1987).

## 6.1 Introduction to Quantum Hall Effect

The observations of the quantum hall effect (QHE), and the fractional quantum hall effect (FQHE) which is mentioned in section 6.6, were made possible by advances in the preparation of high mobility materials with physical realizations of a 2D electron gas. The MOSFET devices (see Part I, 9.2) and the modulation-doped heterostructures (see Part I, 9.3) give rise to the formation of a 2D electron gas in a narrow interface region. In this Chapter we present a simple view of the physics of the quantum hall effect and the two-dimensional electron gas.

The "Quantum Hall Effect" (QHE) is the step-like increase in the Hall resistance $\rho_{xy}$ in units of $h/e^2$ with magnetic field (see {numref}`fig-p3-ch06-1`). Each step in $\rho_{xy}$ is accompanied by a vanishing of the magnetoresistance (i.e., $\rho_{xx} = 0$) as shown in {numref}`fig-p3-ch06-1`. For an ordinary 3D electron gas, $\rho_{xy}$ increases linearly with magnetic field $B$ and the magnetoresistance $\rho_{xx}$ increases as $B^2$ (see Part I, 8.2). The quantum hall effect is a strictly 2D phenomenon which can be observed in semiconductors containing a 2D electron gas region (e.g., in a modulation-doped superlattice as in Part I, 9.3). A second requirement for observation of the Quantum Hall Effect is a very high carrier mobility, so that no carrier scattering occurs until the carrier has completed many cyclotron orbits ($\omega_c\tau \gg 1$).

A third prerequisite for the observation of the quantum hall effect is that the Landau level separation of the magnetic levels is large compared with $k_B T$. Thus the QHE is normally observed at very high magnetic fields, very low temperatures and in very high mobility samples, as shown in {numref}`fig-p3-ch06-1`.

:::{figure} images/fig-p3-ch06-1.png
:name: fig-p3-ch06-1
:width: 75%
:align: center
Fig. 6.1: The quantum Hall effect. As shown in the upper panel, the Hall resistance shows plateaux which coincide with the disappearance of the sample's electrical resistance. On the plateaux, the Hall resistance remains constant while the magnetic field strength is varied. At each of these plateaux, the value of the Hall resistance is precisely equal to $h/(\ell e^2)$, where $\ell$ is an integer, while the magnetoresistance component vanishes $\rho_{xx} = 0$. (Note: plateaux is the preferred plural of plateau.)
:::

## 6.2 Basic Relations for 2D Hall Resistance

The conventional 3D Hall effect is usually measured in a long sample in which a fixed current $I_x$ is flowing in the $x$-direction and a magnetic field $B$ is applied in the $z$-direction. The Lorentz force on the electrons $e(\vec{v}/c)\times\vec{B}$ is compensated by the Hall electric field $E_H$ in the $y$-direction to prevent the flow of current in the $y$-direction.

:::{figure} images/fig-p3-ch06-2.png
:name: fig-p3-ch06-2
:width: 65%
:align: center
Fig. 6.2: Typical geometry of a sample used for Hall effect measurements. The formation of a 2D electron gas (2DEG) in a GaAs heterostructure is shown in the enlargement of the cross section. The Hall voltage $V_H$ and the voltage drop $V_x$ are measured under the constant current condition $I_x = \text{constant}$ as a function of the magnetic field $B_z$ perpendicular to the 2D electron gas.
:::

The geometry for the Hall measurements is shown in {numref}`fig-p3-ch06-2`. The two voltages $V_x$ (driving voltage) and $V_H$ (Hall voltage) are measured. The longitudinal ($R_x$) and Hall ($R_H$) resistances are defined in terms of the current flow $I_x$ as:

```{math}
:label: eq-p3-ch06-1
R_x = V_x/I_x, \quad R_H = V_H/I_x.
```

In general, the conductivity tensor ($\vec{\vec{\sigma}}$) and the resistivity ($\vec{\vec{\rho}}$) tensors relate the current density ($\vec{j}$) and the electric field ($\vec{E}$) vectors, and the vector relations in 2D are written as:

```{math}
:label: eq-p3-ch06-2
\begin{pmatrix} j_x \\ j_y \end{pmatrix}
= \vec{\vec{\sigma}} \cdot \vec{E} =
\begin{pmatrix} \sigma_{xx} & \sigma_{xy} \\ \sigma_{yx} & \sigma_{yy} \end{pmatrix}
\begin{pmatrix} E_x \\ E_y \end{pmatrix},
```

and in terms of the resistivity as

```{math}
:label: eq-p3-ch06-3
\begin{pmatrix} E_x \\ E_y \end{pmatrix}
= \vec{\vec{\rho}} \cdot \vec{J} =
\begin{pmatrix} \rho_{xx} & \rho_{xy} \\ \rho_{yx} & \rho_{yy} \end{pmatrix}
\begin{pmatrix} j_x \\ j_y \end{pmatrix},
```

with the required relation between $\vec{\vec{\sigma}}$ and $\vec{\vec{\rho}}$

```{math}
:label: eq-p3-ch06-4
\vec{\vec{\sigma}} \cdot \vec{\vec{\rho}} = \vec{\vec{1}},
```

where $\vec{\vec{1}}$ is the unit matrix with components $(\delta_{ij})$. Since the off-diagonal $xy$ components of $\vec{\vec{\rho}}$ result from the magnetic field, they are odd under reversal of the magnetic field direction (time reversal symmetry), yielding the relation between components

```{math}
:label: eq-p3-ch06-5
\sigma_{xx}=\sigma_{yy}, \quad \sigma_{yx}=-\sigma_{xy}, \quad
\rho_{xx}=\rho_{yy}, \quad \rho_{yx}=-\rho_{xy}.
```

Equations {eq}`eq-p3-ch06-4` and {eq}`eq-p3-ch06-5` imply that for the 2D electron gas:

```{math}
:label: eq-p3-ch06-6
\begin{aligned}
\rho_{xx} &= \sigma_{xx}/(\sigma_{xx}^2+\sigma_{xy}^2), &
\rho_{xy} &= -\sigma_{xy}/(\sigma_{xx}^2+\sigma_{xy}^2), \\
\sigma_{xx} &= \rho_{xx}/(\rho_{xx}^2+\rho_{xy}^2), &
\sigma_{xy} &= -\rho_{xy}/(\rho_{xx}^2+\rho_{xy}^2).
\end{aligned}
```

An especially interesting implication of these formulae is that in a 2D system, when $\sigma_{xx}=0$ but $\sigma_{xy}\neq 0$, then $\rho_{xx}$ is also zero (and vice versa). This means that (as long as $\sigma_{xy}$ is finite), the vanishing of the longitudinal conductivity implies that the longitudinal resistivity also vanishes.

This is precisely the situation that occurs in the quantum Hall effect, and is fundamental to this phenomenon.

We now relate the resistance parameters that are measured ($R_x$ and $R_H$) to the current density $\vec{j}$ and the electric fields $\vec{E}$. For a long device (as shown in {numref}`fig-p3-ch06-2`), $j_y=0$, so that $R_H$ is related to the resistivity components $\rho_{xx}$ and $\rho_{xy}$ via:

```{math}
:label: eq-p3-ch06-7
R_x = V_x/I_x = (L/W)\cdot(E_x/j_x)|_{j_y=0} = (L/W)\,\rho_{xx}, \quad
R_H = V_H/I_x = (E_y/j_x)|_{j_y=0} = \rho_{xy}.
```

Note that the dimensions of the resistivity in 2D is $\Omega/\square$, and that $R_H$ in 2D has the same dimensions as $\rho_{xy}$.

In the presence of a DC magnetic field $\vec{B}=B\hat{z}$, and in the relaxation-time approximation, the classical equation of motion for the carriers is written as:

```{math}
:label: eq-p3-ch06-8
\frac{d\vec{v}}{dt} = \frac{e}{m^*}\left(\mu\vec{E}+\frac{1}{c}\vec{v}\times\vec{B}\right)-\vec{v}/\tau,
```

where $\vec{v}$ denotes the drift velocity of the carriers, and the charge on the electron is taken as a negative number. Using the relation $\vec{j}=ne\vec{v}$, we can write

```{math}
:label: eq-p3-ch06-9
\sigma_0 E_x=j_x-\omega_c\tau j_y, \quad \sigma_0 E_y=\omega_c\tau j_x+j_y,
```

where $\sigma_0=ne^2\tau/m^*$ and $\omega_c=eB/m^*c$. Finally, combining Eqs. {eq}`eq-p3-ch06-7` and {eq}`eq-p3-ch06-9` with the condition $j_y=0$, we can write:

```{math}
:label: eq-p3-ch06-10
E_y = \frac{\omega_c\tau}{\sigma_0}\,j_x
```

and the Hall resistance $R_H$ becomes

```{math}
:label: eq-p3-ch06-11
R_H \equiv \frac{E_y}{j_x} = \frac{\omega_c\tau}{\sigma_0}
= \frac{(eB/m^*c)\tau}{(ne^2\tau/m^*)} = \frac{B}{nec} = R B,
```

where $R=(1/nec)$ is called the Hall coefficient. We note here that $R_H$ is proportional to the magnetic field. The result derived in Eq. {eq}`eq-p3-ch06-11` is valid for a classical system that ignores the quantization of the magnetic energy levels. This quantization effect becomes important in the limit $\omega_c\tau\gg1$. The classical result for a 2D system is the same result as was previously obtained for the 3D system (see Part I, 8.2). Yet the experimental results for the 2D electron gas in a modulation-doped GaAs/Ga$_{1-x}$Al$_x$As interface ({numref}`fig-p3-ch06-1`) exhibit the quantum Hall effect, where $V_H$ or $\rho_{xy}$ shows a series of flat plateaux as a function of magnetic field rather than a simple linear dependence in $B$ (Eq. {eq}`eq-p3-ch06-11`). The reason for the steps in $\rho_{xy}$ (or $R_H$) as a function of $B$ is due to the density of states of the 2D electron gas in a magnetic field, as discussed below.

## 6.3 The 2D Electron Gas

We refer to the phenomenon shown in {numref}`fig-p3-ch06-1` as the quantum Hall effect because the values of $R_H$ exhibit a plateau whenever

```{math}
:label: eq-p3-ch06-12
R_H = \frac{h}{\ell e^2}, \quad \ell=1,2,3,\ldots,
```

where $\ell$ is an integer. Figure 6.1 shows the results of Hall measurements on a modulation-doped GaAs/Al$_x$Ga$_{1-x}$As heterostructure. Here $\rho_{xx}$ and $\rho_{xy}$ are shown as a function of magnetic field for a heterostructure with a fixed density of carriers. These experiments are done at a low temperature (4.2 K), and the plateaux for $\rho_{xy}$ can be observed very clearly, especially in the limit of small $\ell$. (The plural of plateau is plateaux.) The results shown in Figure 6.1, indicate that $R_H$ for the 2D electron gas is quantized. Detailed measurements show that $R_H$ is given by Eq. {eq}`eq-p3-ch06-12` to an accuracy of better than 0.1 ppm (parts per million). This quantization is reported to be independent of the sample geometry, the temperature, the scattering mechanisms, or other parameters, including the physical system giving rise to the 2D electron gas. The exactness of these results and their apparent independence of experimental parameters are very intriguing and, as we discuss below, are ultimately due to a fundamental physical principle. A schematic diagram summarizing the general behavior of the 2D electron gas is given in {numref}`fig-p3-ch06-3` for $\rho_{xy}$, $\rho_{xx}$ and $\sigma_{xx}$ vs $B$, and also included in this diagram is the comparison with the behavior of a 3D electron gas.

Referring to the 2D conductivity $\vec{\vec{\sigma}}$ and resistivity $\vec{\vec{\rho}}$ tensors defined in Eqs. {eq}`eq-p3-ch06-2` and {eq}`eq-p3-ch06-3`, we can write $\vec{\vec{\rho}}$ and $\vec{\vec{\sigma}}$ in the region of the plateaux as

```{math}
:label: eq-p3-ch06-13
\vec{\vec{\rho}}=
\begin{pmatrix}
0 & -R_Q/i \\[4pt]
R_Q/i & 0
\end{pmatrix}
```

and

```{math}
:label: eq-p3-ch06-14
\vec{\vec{\sigma}}=
\begin{pmatrix}
0 & i/R_Q \\[4pt]
-i/R_Q & 0
\end{pmatrix}
```

:::{figure} images/fig-p3-ch06-3.png
:name: fig-p3-ch06-3
:width: 50%
:align: center
Fig. 6.3: Qualitative behavior for $\sigma_{xx}$, $\rho_{xx}$ and $\rho_{xy}$ of a two-dimensional electron gas with a fixed carrier density as a function of the magnetic field. The dotted lines represent the classical curves for a 3D electron gas. The effect of spin degeneracy is not included in these curves.
:::

where $R_Q=h/e^2$, and where $\rho_{xx}=\rho_{yy}=0$ and $\sigma_{xx}=\sigma_{yy}=0$. At these plateaux the power dissipation $P_{\rm diss}$ vanishes because

```{math}
:label: eq-p3-ch06-15
P_{\rm diss} = \vec{j}\cdot\vec{E}
= \vec{j}\cdot\vec{\vec{\rho}}\cdot\vec{j}
= \frac{1}{i}\begin{pmatrix}j_x & j_y\end{pmatrix}
\begin{pmatrix} 0 & -R_Q \\ R_Q & 0 \end{pmatrix}
\begin{pmatrix}j_x \\ j_y\end{pmatrix}
= \frac{1}{i}(-R_Q j_x j_y + R_Q j_y j_x) = 0.
```

Thus at the plateaux we have no power dissipation and $\rho_{xy}=R_Q/\ell$ independent of material, impurity level, sample geometry, and $\rho_{xy}$ is just dependent on the fundamental constants $h$ and $e$.

To explain the quantized Hall effect, let us first consider the carriers of the two dimensional electron gas to be free electrons at $T=0$, but subjected to an applied magnetic field $B$ normal to the plane of the 2D electron gas. The Landau quantization for $B$ normal to the film surface gives completely quantized sub-band energies (for a simple band)

```{math}
:label: eq-p3-ch06-16
E_{n,\ell} = E_n + (\ell+1/2)\hbar\omega_c \pm g^*\mu_B B = E_n + E_\ell,
```

where $\omega_c\equiv eB/m^*c$ is the cyclotron frequency and $g^*$ is the effective $g$-factor as also for the 3D case, but now $E_n$ pertains to the $z$-dependent bound state energy levels of the 2D electron gas. For the simplest case, the carrier density is arranged to be low so that only the lowest bound state ($n=1$) is occupied. **The number of states per unit area** is found by noting that the energy is independent of the harmonic oscillator center.

Since the energy levels do not depend on the central position of the harmonic oscillator $y_0$, we can sum on all the $k_x$ states to obtain the $k_x$ degeneracy (see Eq. 4.28) per unit area

```{math}
:label: eq-p3-ch06-17
g_{2D} = \frac{eB}{ch}.
```

This degeneracy factor is the same for each Landau level and is proportional to the magnetic field $B$ and depends only on fundamental physical constants (i.e., $e$, $c$, $h$). In addition there is a degeneracy factor of 2 for the electron spin if the electron spin is not considered explicitly in writing the energy level equation.

Since there is no $k_z$ dispersion for the 2D electron gas, the density of states in a magnetic field in two-dimensions consists of a series of singularities ($\delta$-functions) as shown in {numref}`fig-p3-ch06-4`b in contrast to the continuum of states in 3D, also shown in the figure. Multiplying $(eB/ch)$ by $\hbar\omega_c$ gives the number of 2D states in zero magnetic field that coalesce to form each Landau level. This number increases proportionally to the magnetic field as does also the Landau level separation. If at a given magnetic field there are $\ell'$ filled Landau levels, the carrier concentration (neglecting spin) is given by $n_{2D}=\ell'(eB/2\pi\hbar c)$, where $n_{2D}$ is the carrier density associated with a given bound state $n=1$. Thus the Hall resistance $R_H$ in 2D becomes

```{math}
:label: eq-p3-ch06-18
R_H = \frac{B}{n_{2D}ec} = \frac{h}{\ell' e^2} = \frac{R_Q}{\ell'},
```

for $\ell'$ filled magnetic energy levels. Thus we can see that the unique property of the density of states of a 2D electron gas in a magnetic field (see {numref}`fig-p3-ch06-4`) leads to a Hall conductance at $T=0$ that is quantized in multiples of $e^2/h$.

:::{figure} images/fig-p3-ch06-4.png
:name: fig-p3-ch06-4
:width: 55%
:align: center
Fig. 6.4: Schematic density of states in a magnetic field for: (a) three-dimensions, where the energy is referred to the bottom of the band ($E=0$) and (b) two-dimensions, where the energy is referred the lowest bound state energy $E_1$. The energy is plotted in units of the cyclotron energy $\hbar\omega_c$. Dotted curves represent the density of states without a magnetic field. We note that in the 2D case the density of states in zero field is $m/\pi\hbar^2$, indicated by the dashed line. The filling per Landau level $\ell$ in a magnetic field is the degeneracy factor $g_{2D}=eB/(2\pi\hbar c)$ or $eB/hc$.
:::

Carrier filling in 2D is fundamentally different from that in 3D. As the Fermi level rises in 3D, because of the $k_z$ degeneracy, all the Landau levels with subband extrema below $E_F$ will fill. To the extent that the electron density is low enough so that only one bound state is occupied, each magnetic subband fills to the same number of carriers at a given $B$ field.

In the region of the plateaux all Landau levels for $\ell\le\ell'$ are filled and all Landau levels for $\ell>\ell'$ are empty so that for $k_B T\ll\hbar\omega_c$, very little carrier scattering can occur.

The electrons in the semiconductor heterostructure, however, are not free carriers: their behavior is influenced by the presence of the periodic ionic potential, impurities, and scattering phenomena (see {numref}`fig-p3-ch06-5`). Therefore the simple explanation given above for a perfect crystal needs to be extended to account for these complicating effects. In {numref}`fig-p3-ch06-5` the two-dimensional density of states in a magnetic field is shown schematically in the presence of disorder. The $\delta$-functions of Fig. 6.5(a) are now replaced by a continuous function $D(E)$ as shown in Fig. 6.5(b). The figure shows that the magnetic field range over which conduction occurs is broadened. The figure further shows that in the tails of each Landau sub-band there exist regions of localized states (the shaded areas). The electrons associated with the mobility gap are in localized states that do not contribute to conduction. Much research has been done to show that the simple model described above accurately describes $\rho_{xy}$ and $\rho_{xx}$ for the 2D electron gas within the region of the plateaux in actual semiconductor devices.

:::{figure} images/fig-p3-ch06-5.png
:name: fig-p3-ch06-5
:width: 100%
:align: center
Fig. 6.5: Schematic representation of the 2D density of states in a magnetic field (a) without disorder and (b) with disorder. The shaded regions correspond to localized states.
:::

Let us consider the diagram for the 2D density of states in a magnetic field shown in {numref}`fig-p3-ch06-6` for a single Landau level. Suppose the magnetic field is just large enough so that the indicated 2D Landau level is completely filled and $E_F$ lies at $\nu=1$, where $\nu$ represents the fractional filling of the 2D Landau level. Then as the magnetic field is further increased, the Fermi level falls. So long as the Fermi level remains within the region of the localized states, then $\sigma_{xx}=0$. Thus when $E_F$ lies in the shaded region, $E_F$ is effectively in an energy gap where $\sigma_{xx}\equiv 0$ and the Hall conductance $\sigma_{xy}$ remains on a plateau determined by $\ell' e^2/h$. As $B$ increases further, $E_F$ eventually reaches the unshaded region where $\sigma_{xx}$ no longer vanishes and $E_F$ passes through the mobile states (see {numref}`fig-p3-ch06-6`), causing $\sigma_{xy}$ to jump from $\ell' e^2/h$ to $(\ell'-1)e^2/h$ as $E_F$ passes through the mobile states. When the magnetic field is large enough for $E_F$ to reach the localized states near $\nu=0$, then $\sigma_{xx}$ again vanishes and $\sigma_{xy}$ now remains at the plateau $(\ell'-1)e^2/h$.

:::{figure} images/fig-p3-ch06-6.png
:name: fig-p3-ch06-6
:width: 45%
:align: center
Fig. 6.6: The density of states [$D(E)$], d.c. conductivity ($\sigma_{xx}$), and the Hall conductivity ($\sigma_{xy}$) are schematically shown as a function of the fractional filling factor $\nu$ for a Landau subband. Shaded regions in the density of states denote the regions of localized carriers corresponding to an effective energy gap between magnetic subbands.
:::

From these arguments we can conclude that the steps in $\rho_{xy}$ and the zeros in $\rho_{xx}$ are caused by the passage of a 2D Landau level through the Fermi level. When the effect of the electron spin is included, spin splitting of the Landau levels is expected in the quantum Hall effect measurements. To see spin splittings effects the measurements must be made at sufficiently low temperatures (e.g., $T=0.35$ K). Spin splitting effects of the $\ell=1$ Landau level ($1\downarrow$ and $1\uparrow$) have been clearly seen. The observation of spin splitting in the Quantum Hall Effect thus requires high fields, low $m^*_c$, high mobility samples to achieve $\omega_c\tau\gg 1$ and low temperatures $k_B T\ll\hbar\omega_c$ to prevent thermal excitation between Landau levels.

## 6.4 Effect of Edge Channels

In the simple explanation of the Quantum Hall effect, it is necessary to assume both localized states ($\sigma_{xx}=0$) and extended states ($\sigma_{xx}\neq 0$). In taking into account the so-called edge channels, it is possible to explain more clearly why the quantization is so precise in the Quantum Hall Effect for real systems.

Referring to the derivation of the Landau levels for motion in a plane perpendicular to the magnetic field (see 4.4), we assume that only the lowest band state $n=1$ is occupied and we neglect the interaction of the electron spin with the magnetic field.

The wave function for an electron in the 2D electron gas can then be written as

```{math}
:label: eq-p3-ch06-19
\Psi_{\rm 2D}(x,y)=e^{ik_xx}\phi(y),
```

where $\phi(y)$ satisfies the harmonic oscillator equation

```{math}
:label: eq-p3-ch06-20
\left[\frac{p_y^2}{2m^*_c}+\frac{1}{2}m^*_c\omega^*_c(y-y_0)^2\right]\phi(y)
=\left[\frac{p_y^2}{2m^*_c}+V(y)\right]\phi(y)=E_\ell\phi(y),
```

in which the harmonic oscillator center is given by

```{math}
:label: eq-p3-ch06-21
y_0 = \frac{\hbar k_x}{m^*_c\omega^*_c} = \lambda_B^2 k_x,
```

and the harmonic oscillator energies are

```{math}
:label: eq-p3-ch06-22
E_\ell=(\ell+1/2)\hbar\omega^*_c.
```

The characteristic magnetic length

```{math}
:label: eq-p3-ch06-23
\lambda_B=\sqrt{\frac{\hbar c}{eB}}=\frac{250\text{\AA}}{\sqrt{B({\rm tesla})}}
```

relates to the real space orbit of the electron in a harmonic oscillator state (Eq. 5.11) and except for universal constants depends only on the magnetic field. Since the energy in Eq. {eq}`eq-p3-ch06-22` is independent of $k_x$, the electron velocity component $x_x$ vanishes

```{math}
:label: eq-p3-ch06-24
v_x=\frac{1}{\hbar}\frac{\partial E}{\partial k_x}=0,
```

and there is no net current along $\hat{x}$.

The argument that the energy is independent of $k_x$, however, only applies to those harmonic oscillator centers $y_0$ that are interior to the sample. But if $y_0$ takes on a value close to the sample edge, i.e., $y_0\simeq 0$ or $y_0\simeq L_y$, then the electron is more influenced by the infinite potential barrier at the edge than the harmonic oscillator potential $V(y)$ associated with the magnetic field. Electrons in these edge orbits will be reflected at the edge potential barriers and $V(y)$ is no longer strictly a harmonic oscillator potential. Since the potential $V(y)$ is perturbed, the energy will also be perturbed and the energy will then become dependent on $k_x$. Since the harmonic oscillator orbit size is $\lambda_B\sqrt{\ell+1}$, the energy of the 2D electron gas depends on $k_x$ only for a distance of approximately $\lambda_B\sqrt{\ell+1}$ from the sample edge.

The effect of the sample edges can be understood in terms of the skipping orbits illustrated in {numref}`fig-p3-ch06-7`. All the harmonic oscillator orbits with $y_0$ values within $\lambda_B$ of the edge will contribute to the current density $j_x$ by the argument in {numref}`fig-p3-ch06-7`. The current $I_\ell$ contributed by the $\ell^{\rm th}$ edge channel is

```{math}
:label: eq-p3-ch06-25
I_\ell=e v_{\ell,x}\left(\frac{dn}{dE_\ell}\right)\Delta\mu,
```

where $(dn/dE_\ell)$ is the 1D density of states and $\Delta\mu$ is the drop in chemical potential along the edge channel. Now we can write

```{math}
:label: eq-p3-ch06-26
\frac{dn}{dE_\ell}=\frac{dn}{dk_x}\frac{dk_x}{dE_\ell}
=\left(\frac{1}{2\pi}\right)\!\left(\frac{1}{\hbar v_{\ell,x}}\right)
=\frac{1}{\hbar v_{\ell,x}},
```

where $v_{\ell,x}$ is the velocity of the electrons in the $x$ direction due to the carriers in channel $\ell$. Substitution of Eq. {eq}`eq-p3-ch06-26` into {eq}`eq-p3-ch06-25` yields $I_\ell=(e/h)\Delta\mu$, which is independent of $\ell$, so that the total current is obtained by summing over the edge channels to yield

```{math}
:label: eq-p3-ch06-27
I_x=\ell_c\frac{e}{h}\Delta\mu,
```

where $\ell_c$ is the number of edge channels.

:::{figure} images/fig-p3-ch06-7.png
:name: fig-p3-ch06-7
:width: 90%
:align: center
Fig. 6.7: Location of the edge skipping orbits in a magnetic field. The edge regions shown in (a) are defined by the characteristic length $\lambda_B=(\hbar c/eB)^{1/2}$. Along each edge, (b) shows that all orbits give rise to current $j_x$ in the same direction but the current direction is opposite for the two edges. The bulk orbits do not give rise to a current $j_x$.
:::

If the conditions $\lambda_B\ll\ell_\phi$ and $\lambda_B\ll\ell_e$ are satisfied, where $\ell_\phi$ and $\ell_e$ are, respectively, the inelastic and elastic scattering lengths, electrons are not likely to scatter across the sample (backscattering) because of the electron localization in the variable $y$ ($\psi\sim\exp[-y^2/\lambda_B^2]$). The opposing directions of $j_x$ along the two edges guarantees that the continuity equation is satisfied.

Let us now consider the electrochemical potential $\mu$, which has a constant value along each edge channel, because of the absence of back scattering, as noted above. Two edge channels are shown in {numref}`fig-p3-ch06-8`. From Eq. {eq}`eq-p3-ch06-27` we obtain the total current $I_x$ in the upper and lower edges. The quantity $\Delta\mu$ in Eq. {eq}`eq-p3-ch06-25` denotes the potential drop between two points where the transmission coefficient $T$ is unity ($T\equiv 1$). Thus for the upper edge channel,

```{math}
:label: eq-p3-ch06-28
I_A=\ell_{cA}(e/h)(\mu_2-\mu_A),
```

indicating that there is a reflection between the edge channel and $\mu$ reservoir and $T\neq 1$. For the lower channel

```{math}
:label: eq-p3-ch06-29
I_B=\ell_{cB}(e/h)(\mu_B-\mu_2).
```

the number of edge channels for the two edges is the same, so that $\ell_{cA}=\ell_{cB}=\ell_c$. We thus obtain:

```{math}
:label: eq-p3-ch06-30
I_x = I_A+I_B = \ell_c(e/h)(\mu_B-\mu_A).
```

:::{figure} images/fig-p3-ch06-8.png
:name: fig-p3-ch06-8
:width: 55%
:align: center
Fig. 6.8: Schematic diagram of current flow for edge channels. The dark circles denote the contacts between the edge channels and the electron reservoirs at electrochemical potential $\mu_2$ and $\mu_1$.
:::

Since the Hall voltage $V_y$ is given by the difference in electrochemical potential in the $y$ direction of the sample, we obtain

```{math}
:label: eq-p3-ch06-31
eV_y = \mu_B - \mu_A,
```

so that

```{math}
:label: eq-p3-ch06-32
I_x = \ell_c(e^2/h)V_y.
```

The Hall resistance $R_H$ then becomes

```{math}
:label: eq-p3-ch06-33
R_H = \frac{V_y}{I_x} = \frac{h}{e^2\ell_c} = \frac{R_Q}{\ell_c},
```

where $R_Q=h/e^2$ is the fundamental unit of resistance and $\ell_c$ is a quantum number denoting the number of edge channels. The edge channel picture thus provides another way to understand why the quantum Hall effect is associated with a fundamental constant of nature.

## 6.5 Applications of the Quantized Hall Effect

Because of the high precision with which the Hall resistance is quantized at integer fractions of $h/e^2$, we obtain

```{math}
:label: eq-p3-ch06-34
\ell'R_H = \frac{h}{e^2} = R_Q = 25{,}812.200~\Omega, \quad \ell'=1,2,3,\ldots.
```

This quantity called the Klitzing (after the man who discovered the Quantum Hall Effect experimentally) has become the new IEEE resistance standard since 1990 and is known to an accuracy of $\sim 3\times10^{-8}$. When combined with the high precision with which the velocity of light is known, $c=299{,}792{,}458\pm 1.2$m/s, the quantum Hall effect has become the primary technique for measuring the fine structure constant:

```{math}
:label: eq-p3-ch06-35
\alpha \equiv \frac{e^2}{c\hbar}.
```

The fine structure constant must be known to high accuracy in tests of quantum electrodynamics (QED). The results for $\alpha$ from the QHE are not only of comparable accuracy to those obtained by other methods, but this determination of $\alpha$ is also independent of the QED theory. The QHE measurement thus acts as another verification of QED. It is interesting to note that the major source of uncertainty in the QHE result is the uncertainty in the calibration of the standard resistor used as a reference.

## 6.6 Fractional Quantum Hall Effect (FQHE)

When a two-dimensional electron gas is subjected to a sufficiently low temperature and an intense magnetic field ($B\parallel z$-axis), of magnitude greater than necessary to achieve the lowest quantum state in the quantum Hall effect, all electrons could be expected to remain in their lowest Landau level and spin state.

In this limit, however, the possibility also exists, that the electrons will further order under the influence of their mutual interactions. Such ordering phenomena have been seen in GaAs/Ga$_{1-x}$Al$_x$As and other quantum well structures, where an apparent succession of correlated electron states has been found at fractional occupations, $\nu$, of the lowest Landau level.

This ordering effect is called the fractional quantum hall effect (FQHE).

Just as for the quantum Hall effect discussed in 6.3, the fractional quantum Hall effect is characterized by minima in the electrical resistance and plateaux in the Hall resistance for current flow in the two-dimensional layers ($x$-direction). Whereas the integral quantum Hall effect occurs because of gaps in the density of mobile electron states at energies between the 2D Landau levels (see {numref}`fig-p3-ch06-4`), the fractional quantization is interpreted in terms of new gaps in the spectrum of electron energy levels appearing predominantly at magnetic fields higher than the plateau for the $\ell=0$ integral quantum Hall effect and associated with electron-electron interactions.

The fractional quantum Hall effect (FQHE) was first observed in the extreme quantum limit, for fractional filling factors $\nu$

```{math}
:label: eq-p3-ch06-36
\nu = \frac{n_{2D}hc}{eB} < 1,
```

where the 2D carrier density $n_{2D}$ is given by

```{math}
:label: eq-p3-ch06-37
n_{2D} = \nu\left(\frac{eB}{hc}\right).
```

This regime can be achieved experimentally at low carrier densities $n_{2D}$, high magnetic fields $B$, and very low temperatures $T$. The observations of the FQHE thus requires the Landau level spacing $\hbar\omega_c$ to exceed the zero field Fermi level

```{math}
:label: eq-p3-ch06-38
\hbar\omega_c = \frac{\hbar e B}{m^* c} > E_F,
```

where the Fermi level for a single spin orientation is given by

```{math}
:label: eq-p3-ch06-39
E_F = \frac{2\pi n_{2D}\hbar^2}{m^*}.
```

This condition is equivalent to requiring the magnetic length or cyclotron radius to be less than the inter-particle spacing $n_{2D}^{-1/2}$, where $n_{2D}$ is the 2D electron density.

To observe electron ordering, it is desirable that electron-electron interactions be large and that electron-impurity interactions be small. This requires the minimization of uncertainty broadening of the electron levels and inhomogeneous broadening caused by potential fluctuations and electron scattering. Thus the observation of the fractional quantum Hall effect is linked to the availability of very high mobility samples containing a 2D electron gas in the lowest bound state level. The best samples for observing the FQHE are the modulation-doped GaAs/Al$_x$Ga$_{1-x}$As interfaces, as shown in {numref}`fig-p3-ch06-9`. In the fabrication the $n$-doped regions have been confined to a single atomic layer (i.e., $\delta$-doping), far from the quantum well to achieve high carrier mobility.

:::{figure} images/fig-p3-ch06-9.png
:name: fig-p3-ch06-9
:width: 55%
:align: center
Fig. 6.9: Schematic diagram of a modulation-doped $n$-type semiconductor GaAs/Al$_x$Ga$_{1-x}$As heterostructure and of its energy band structure. CB and VB refer to conduction band and valence band edges; $E_{g1}$ and $E_{g2}$ are, respectively, the energy gaps of the Al$_x$Ga$_{1-x}$As and GaAs regions, while $\Delta E$ is the energy corresponding to the zero-magnetic-field filling of the lowest quantum subband of the two-dimensional electron gas, and $E_F$ is the Fermi energy. $W$ is the step height (band offset energy) between the GaAs conduction band and the Al$_x$Ga$_{1-x}$As conduction band at the interface. The two-dimensional electron gas lies in the GaAs region close to the undoped Al$_x$Ga$_{1-x}$As (see lowest diagram). The dopants used to introduce the $n$-type carriers are located in the region called $n$-doped AlGaAs.
:::

The highest mobility materials that have been reported for modulation-doped MBE samples have been used for observation of the FQHE. Measurements are made on photolithographically-defined Hall bridges using microampere currents and Ohmic current and potential contacts. Experimental results for the resistivity and Hall resistance versus magnetic field in the fractional quantum Hall effect regime are shown in {numref}`fig-p3-ch06-10`. Minima develop in the diagonal (in-plane) resistivity $\rho_{xx}$ at magnetic fields corresponding both to integral filling and to certain fractional fillings of the Landau levels. The Hall resistivity $\rho_{xy}$ develops plateaux at the same integral and fractional filling factors. The classical value of the Hall resistance $\rho_{xy}$ for $n$ carriers per unit area is $\rho_{xy}=B/(nec)$ and $B/n$ is interpreted as the magnetic flux per carrier which is the flux quantum $\varphi_0=ch/e$ divided by the Landau level filling $\nu$, so that $B/n=ch/(e\nu)$ at filling factor $\nu$.

The value of $\rho_{xy}$ is $h/\nu e^2$ at filling factor $\nu$. Plateaux were first measured at $\nu=1/3$ (see {numref}`fig-p3-ch06-10`) with $\rho_{xy}$ equal to $h/\nu e^2$ to within one part in $10^4$.

In addition to quantization at quantum number 1/3, quantization has been observed at a number of other fractions $\nu=2/3$, $4/3$, $5/3$, $2/5$, $3/5$, $4/5$, $2/7$ and others (see {numref}`fig-p3-ch06-11`), suggesting that fractional quantization exists in multiple series, with each series based on the inverse of an odd integer. With the highest mobility materials, a fractional quantum Hall effect has recently been observed for an even integer denominator.

Only a certain specified set of fractions exhibit the fractional quantum Hall effect, corresponding to the relation

```{math}
:label: eq-p3-ch06-40
\nu = \frac{1}{p+\dfrac{\alpha_1}{p_1+\dfrac{\alpha_2}{p_2+\cdots}}},
```

where the integers $p$ is odd, $p_i$ is even, and $\alpha_i=0,\pm 1$. For example, $p=3$, $p_i=0$ and $\alpha_i=0$ for all $i$ yields a fractional filling factor of $1/3$, where the most intense fractional quantum Hall effect is observed. For $p=3$, $p_1=1$ and $\alpha_1=1$ and all other coefficients taken to be zero gives $\nu=2/3$. Equation {eq}`eq-p3-ch06-40` accounts for all the observed examples of the fractional quantum Hall effect except for the case of the recently observed case of $\nu=5/2$ mentioned above.

:::{figure} images/fig-p3-ch06-10.png
:name: fig-p3-ch06-10
:width: 70%
:align: center
Fig. 6.10: First observation of the FQHE in a GaAs/Al$_x$Ga$_{1-x}$As modulation-doped heterostructure with an areal carrier density of $n=1.23\times 10^{11}$ electrons/cm$^2$ and an electron mobility of $\mu=90{,}000$ cm$^2$/Vsec. The Hall resistance $\rho_{xy}$ assumes a plateau at fractional filling $\nu=1/3$ indicating a fractional quantum number $\ell=1/3$. [D.C. Tsui, H.L. Stormer and A.C. Gossard, Phys. Rev. Lett. 48, 1559 (1982)].
:::

To explain the characteristics of the fractional quantum Hall effect, Laughlin proposed a many-electron wavefunction to account for the electron correlations responsible for the fractional quantum Hall effect:

```{math}
:label: eq-p3-ch06-41
\psi_m(z_1,z_2,z_3,\ldots z_N)
= C\prod_{i<j}^{N}(z_i-z_j)^m
\exp\!\left(-\frac{1}{4}\sum_k |z_k|^2\right),
```

where $m=1/\nu$ and $\nu$ is the filling factor. Research at the fundamental level is still being carried out to understand the fractional quantum Hall effect and related phenomena in more detail.

:::{figure} images/fig-p3-ch06-11.png
:name: fig-p3-ch06-11
:width: 85%
:align: center
Fig. 6.11: Present high-field, low-temperature ($T\sim0.1$K) data on the FQHE (fractional quantum Hall effect) taken from a high mobility ($\mu\sim1.3\times 10^6$cm$^2$/V sec) quantum well sample of GaAs/Ga$_{1-x}$Al$_x$As. The familiar IQHE (integer quantum Hall effect) characteristics appear at filling factors of $\nu=1,2,3,\ldots$. All fractional numbers are a result of the FQHE. Fractions as high as 7/13 are now being observed. [R. Willett, J.P. Eisenstein, H.L. Stormer, D.C. Tsui, A.C. Gossard, and J.H. English Phys. Rev. Lett. 59, 1776 (1987)].
:::
