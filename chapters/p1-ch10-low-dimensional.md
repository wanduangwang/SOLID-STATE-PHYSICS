---
title: "10 Transport in Low Dimensional Systems"
abstract: "Highlights quantum transport effects in low-dimensional systems (quantum wells, wires, and dots), including the density of states, the Einstein relation, the Landauer formula, quantized ballistic conductance, and single-electron charging devices."
---

# 10 Transport in Low Dimensional Systems

## 10.0 Overview

This chapter discusses transport in low-dimensional systems such as quantum wells (2D), quantum wires (1D), and quantum dots (0D), where quantum effects dominate. We review the density of states in low dimensions, the Einstein relation and Landauer formula, the quantization of ballistic conductance, and single-electron charging effects.

## 10.1 Introduction

Transport phenomena in low dimensional systems such as in quantum wells (2D), quantum wires (1D), and quantum dots (0D) are dominated by quantum effects not included in the classical treatments based on the Boltzmann equation and discussed in Chapters 4-6. With the availability of experimental techniques to synthesize materials of high chemical purity and of nanometer dimensions, transport in low dimensional systems has become an active current research area. In this chapter we consider some highlights on the subject of transport in low dimensional systems.

## 10.2 Observation of Quantum Effects in Reduced Dimensions

Quantum effects dominate the transport in quantum wells and other low dimensional systems such as quantum wires and quantum dots when the de Broglie wavelength of the electron

```{math}
:label: eq-p1-ch10-1
\lambda_{\mathrm{dB}} = \frac{\hbar}{(2m^{*}E)^{1/2}}
```

exceeds the dimensions of a quantum structure of characteristic length $L_z$ ($\lambda_{\mathrm{dB}} > L_z$) or likewise for tunneling through a potential barrier of length $L_z$. To get some order of magnitude estimates of the electron kinetic energies $E$ below which quantum effects become important we look at {numref}`fig-p1-ch10-1` where a log-log plot of $\lambda_{\mathrm{dB}}$ vs $E$ in Eq. {eq}`eq-p1-ch10-1` is shown for GaAs and InAs.

:::{figure} images/fig-p1-ch10-1.png
:name: fig-p1-ch10-1
:width: 80%
:align: center
Fig. 10.1: Plot of the electron de Broglie wavelength $\lambda_{\mathrm{dB}}$ vs the electron kinetic energy $E$ for GaAs ($\square$) and InAs ($\circ$).
:::

From the plot we see that an electron energy of $E \sim 0.1$ eV for GaAs corresponds to a de Broglie wavelength of 200 Å. Thus wave properties for electrons can be expected for structures smaller than $\lambda_{\mathrm{dB}}$.

To observe quantum effects, the thermal energy must also be less than the energy level separation, $k_B T < \Delta E$, where we note that room temperature corresponds to 25 meV. Since quantum effects depend on the phase coherence of electrons, scattering can also destroy quantum effects. The observation of quantum effects thus requires that the carrier mean free path be much larger than the dimensions of the quantum structures (wells, wires or dots).

The limit where quantum effects become important has been given the name of **mesoscopic physics**. Carrier transport in this limit exhibits both particle and wave characteristics. In this ballistic transport limit, carriers can in some cases transmit charge or energy without scattering.

The small dimensions required for the observation of quantum effects can be achieved by the direct fabrication of semiconductor elements of small dimensions (quantum wells, quantum wires and quantum dots). Another approach is the use of gates on a field effect transistor to define an electron gas of reduced dimensionality. In this context, negatively charged metal gates can be used to control the source to drain current of a 2D electron gas formed near the GaAs/AlGaAs interface as shown in {numref}`fig-p1-ch10-2`. Between the dual gates shown on this figure, a thin conducting wire is formed out of the 2D electron gas. Controlling the gate voltage controls the amount of charge in the depletion region under the gates, as well as the charge in the quantum wire. Thus lower dimensional channels can be made in a 2D electron gas by using metallic gates. In the following sections a number of important applications are made of this concept.

:::{figure} images/fig-p1-ch10-2.png
:name: fig-p1-ch10-2
:width: 80%
:align: center
Fig. 10.2: (a) Schematic diagram of a lateral resonant tunneling field-effect transistor which has two closely spaced fine finger metal gates; (b) schematic of an energy band diagram for the device. A 1D quantum wire is formed in the 2D electron gas between the gates.
:::

## 10.3 Density of States in Low Dimensional Systems

We showed in Eq. 8.40 that the density of states for a 2D electron gas is a constant for each 2D subband

```{math}
:label: eq-p1-ch10-2
g_{2D} = \frac{m^{*}}{\pi \hbar^{2}} .
```

This is shown in {numref}`fig-p1-ch10-3` (a) where the inset is appropriate to the quantum well formed near a modulation doped GaAs-AlGaAs interface. In the diagram only the lowest bound state is occupied.

:::{figure} images/fig-p1-ch10-3.png
:name: fig-p1-ch10-3
:width: 90%
:align: center
Fig. 10.3: Density of states $g(E)$ as a function of energy. (a) Quasi-2D density of states, with only the lowest subband occupied (hatched). Inset: Confinement potential perpendicular to the plane of the 2DEG. The discrete energy levels correspond to the bottoms of the first and second 2D subbands. (b) Quasi-1D density of states, with four 1D subbands occupied. Inset: Square-well lateral confinement potential with discrete energy levels indicating the 1D subband extrema.
:::

Using the same argument, we now derive the density of states for a 1D electron gas

```{math}
:label: eq-p1-ch10-3
N_{1D} = \frac{2}{2\pi}(k) = \frac{1}{\pi}(k)
```

which for a parabolic band $E = E_n + \hbar^{2}k^{2}/(2m^{*})$ becomes

```{math}
:label: eq-p1-ch10-4
N_{1D} = \frac{2}{2\pi}(k) = \frac{1}{\pi}\left(\frac{2m^{*}(E-E_n)}{\hbar^{2}}\right)^{1/2}
```

yielding an expression for the density of states $g_{1D}(E) = \partial N_{1D}/\partial E$

```{math}
:label: eq-p1-ch10-5
g_{1D}(E) = \frac{1}{2\pi}\left(\frac{2m^{*}}{\hbar^{2}}\right)^{1/2}(E-E_n)^{-1/2} .
```

The interpretation of this expression is that at each doubly confined bound state level $E_n$ there is a singularity in the density of states, as shown in {numref}`fig-p1-ch10-3` (b) where the first four levels are occupied.

### 10.3.1 Quantum Dots

This is an example of a zero dimensional system. Since the levels are all discrete any averaging would involve a sum over levels and not an integral over energy. If, however, one chooses to think in terms of a density of states, then the DOS would be a delta function positioned at the energy of the localized state. For more extensive treatment see the review by Marc Kastner (Appendix D).

## 10.4 The Einstein Relation and the Landauer Formula

In the classical transport theory (Chapter 4) we related the current density $\vec{j}$ to the electric field $\vec{E}$ through the conductivity $\sigma$ using the Drude formula

```{math}
:label: eq-p1-ch10-6
\sigma = \frac{ne^{2}\tau}{m^{*}} .
```

This equation is valid when many scattering events occur within the path of an electron through a solid, as shown in {numref}`fig-p1-ch10-4` (a). As the dimensions of device structures become smaller and smaller, other regimes become important, as shown in {numref}`fig-p1-ch10-4` (b) and {numref}`fig-p1-ch10-4` (c).

:::{figure} images/fig-p1-ch10-4.png
:name: fig-p1-ch10-4
:width: 80%
:align: center
Fig. 10.4: Electron trajectories characteristic of the diffusive ($\ell < W, L$), quasi-ballistic ($W < \ell < L$), and ballistic ($W, L < \ell$) transport regimes, for the case of specular boundary scattering. Boundary scattering and internal impurity scattering (asterisks) are of equal importance in the quasi-ballistic regime. A nonzero resistance in the ballistic regime results from backscattering at the connection between the narrow channel and the wide 2DEG regions. Taken from H. Van Houten et al. in "Physics and Technology of Submicron Structures" (H. Heinrich, G. Bauer and F. Kuchar, eds.) Springer, Berlin, 1988.
:::

To relate transport properties to device dimensions it is often convenient to rewrite the Drude formula by explicitly substituting for the carrier density $n$ and for the relaxation time $\tau$ in Eq. {eq}`eq-p1-ch10-6`. Writing $\tau = \ell/v_F$ where $\ell$ is the mean free path and $v_F$ is the Fermi velocity, and writing $n = k_F^{2}/(2\pi)$ for the carrier density for a 2D electron gas (2DEG) we obtain

```{math}
:label: eq-p1-ch10-7
\sigma = \frac{k_F^{2}}{2\pi} e^{2}\frac{\ell}{m^{*}v_F} = \frac{k_F^{2}e^{2}\ell}{2\pi \hbar k_F} = \frac{e^{2}}{h}k_F\ell
```

where $e^{2}/h$ is a universal constant and is equal to $\sim (26\ \mathrm{k}\Omega)^{-1}$.

Two general relations that are often used to describe transport in situations where collisions are not important within device dimensions are the Einstein relation and the Landauer formula. We discuss these relations below. The Einstein relation follows from the continuity equation

```{math}
:label: eq-p1-ch10-8
\vec{j} = eD\vec{\nabla}n
```

where $D$ is the diffusion coefficient and $\vec{\nabla}n$ is the gradient of the carrier density involved in the charge transport. In equilibrium the gradient in the electrochemical potential $\vec{\nabla}\mu$ is zero and is balanced by the electrical force and the change in Fermi energy

```{math}
:label: eq-p1-ch10-9
\vec{\nabla}\mu = 0 = -e\vec{E} + \vec{\nabla}n\frac{dE_F}{dn} = -e\vec{E} + \vec{\nabla}n/g(E_F)
```

where $g(E_F)$ is the density of states at the Fermi energy. Substitution of Eq. {eq}`eq-p1-ch10-9` into Eq. {eq}`eq-p1-ch10-8` yields

```{math}
:label: eq-p1-ch10-10
\vec{j} = eDg(E_F)e\vec{E} = \sigma\vec{E}
```

yielding the Einstein relation

```{math}
:label: eq-p1-ch10-11
\sigma = e^{2}Dg(E_F)
```

which is a general relation valid for 3D systems as well as systems of lower dimensions.

The Landauer formula is an expression for the conductance $G$ which is the proportionality between the current $I$ and the voltage $V$,

```{math}
:label: eq-p1-ch10-12
I = GV .
```

For 2D systems the conductance and the conductivity have the same dimensions, and for a large 2D conductor we can write

```{math}
:label: eq-p1-ch10-13
G = (W/L)\sigma
```

where $W$ and $L$ are the width and length of the conducting channel in the current direction, respectively. If $W$ and $L$ are both large compared to the mean free path $\ell$, then we are in the diffusive regime (see {numref}`fig-p1-ch10-4` (a)). However when we are in the opposite regime, the ballistic regime, where $\ell > W, L$, then the conductance is written in terms of the Landauer formula which is obtained from Eqs. {eq}`eq-p1-ch10-7` and {eq}`eq-p1-ch10-13`. Writing the number of quantum modes $N$, then $N\pi = k_F W$ or

```{math}
:label: eq-p1-ch10-14
k_F = \frac{N\pi}{W}
```

and noting that the quantum mechanical transition probability coupling one channel to another in the ballistic limit $|t_{\alpha,\beta}|^{2}$ is $\pi\ell/(2LN)$ per mode, we obtain the general Landauer formula

```{math}
:label: eq-p1-ch10-15
G = \frac{2e^{2}}{h}\sum_{\alpha,\beta}^{N} |t_{\alpha,\beta}|^{2} .
```

We will obtain the Landauer formula below for some explicit examples, which will make the derivation of the normalization factor more convincing.

## 10.5 One Dimensional Transport and Quantization of the Ballistic Conductance

In the last few years one dimensional ballistic transport has been demonstrated in a two dimensional electron gas (2DEG) of a GaAs-GaAlAs heterojunction by constricting the electron gas to flow in a very narrow channel (see {numref}`fig-p1-ch10-5`). Ballistic transport refers to carrier transport without scattering. As we show below, in the ballistic regime, the conductance of the 2DEG through the constriction shows quantized behavior with the conductance changing in quantized steps of $(e^{2}/\pi\hbar)$ when the effective width of the constricting channel is varied by controlling the voltages of the gate above the 2DEG. We first give a derivation of the quantization of the conductance.

:::{figure} images/fig-p1-ch10-5.png
:name: fig-p1-ch10-5
:width: 80%
:align: center
Fig. 10.5: Point contact conductance as a function of gate voltage at 0.6 K, obtained from the raw data after subtraction of the background resistance. The conductance shows plateaus at multiples of $e^{2}/\pi\hbar$. Inset: Point-contact layout [from B.J. van Wees, et al., Phys. Rev. Lett. 60, 848 (1988)].
:::

The current $I_x$ flowing between source and drain (see {numref}`fig-p1-ch10-2`) due to the contribution of one particular 1D electron subband is given by

```{math}
:label: eq-p1-ch10-16
I_x = ne\delta v
```

where $n$ is the carrier density (i.e., the number of carriers per unit length of the channel) and $\delta v$ is the increase in electron velocity due to the application of a voltage $V$. The carrier density in 1D is

```{math}
:label: eq-p1-ch10-17
n = \frac{2}{2\pi}k_F = \frac{k_F}{\pi}
```

and the gain in velocity $\delta v$ resulting from an applied voltage $V$ is

```{math}
:label: eq-p1-ch10-18
eV = \frac{1}{2}m^{*}(v_F+\delta v)^{2} - \frac{1}{2}m^{*}v_F^{2} = m^{*}v_F\delta v + \frac{1}{2}m^{*}(\delta v)^{2} .
```

Retaining only the first order term in Eq. {eq}`eq-p1-ch10-18` yields

```{math}
:label: eq-p1-ch10-19
\delta v = \frac{eV}{m^{*}v_F}
```

so that from Eq. {eq}`eq-p1-ch10-16` we get for the source-drain current (see {numref}`fig-p1-ch10-5`)

```{math}
:label: eq-p1-ch10-20
I_x = \frac{k_F}{\pi}e\frac{eV}{m^{*}v_F} = \frac{e^{2}}{\pi\hbar}V
```

since $\hbar k_F = m^{*}v_F$. This yields a conductance per 1D electron subband $G_i$ of

```{math}
:label: eq-p1-ch10-21
G_i = \frac{e^{2}}{\pi\hbar}
```

or summing over all occupied subbands $i$ we obtain

```{math}
:label: eq-p1-ch10-22
G = \sum_i \frac{e^{2}}{\pi\hbar} = \frac{i e^{2}}{\pi\hbar} .
```

Two experimental observations of these phenomena were simultaneously published [D.A. Wharam, T.J. Thornton, R. Newbury, M. Pepper, H. Ahmed, J.E.F. Frost, D.G. Hasko, D.C. Peacock, D.A. Ritchie, and G.A.C. Jones, J. Phys. C: Solid State Phys. 21, L209 (1988); and B.J. van Wees, H. van Houten, C.W.J. Beenakker, J.G. Williamson, L.P. Kouwenhoven, D. van der Marel, and C.T. Foxon, Phys. Rev. Lett. 60, 848 (1988)]. The experiments by Van Wees et al. were done using ballistic point contacts on a gate structure placed over a two-dimensional electron gas as shown schematically in the inset of {numref}`fig-p1-ch10-5`. The width $W$ of the gate (in this case 2500 Å) defines the effective width $W'$ of the conducting electron channel, and the applied gate voltage is varied in order to control the effective width $W'$. Superimposed on the raw data for the resistance vs gate voltage is a collection of periodic steps as shown in {numref}`fig-p1-ch10-5` after subtracting off the background resistance of 400 $\Omega$.

There are several conditions necessary to observe perfect $2e^{2}/h$ quantization of the 1D conductance. One requirement is that the electron mean free path $l_e$ be much greater than the length of the channel $L$. This limits the values of channel lengths to $L < 5{,}000$ Å even though mean free path values are much larger, $l_e = 8.5$ $\mu$m. It is important to note, however, that $l_e = 8.5$ $\mu$m is the mean free path for the 2D electron gas. When the channel is formed, the screening effect of the 2D electron gas is no longer present and the effective mean free path becomes much shorter.

A second condition is that there are adiabatic transitions at the inputs and outputs of the channel. This minimizes reflections at these two points, an important condition for the validity of the Landauer formula to be discussed later in this section. A third condition requires the Fermi wavelength $\lambda_F = 2\pi/k_F$ (or $k_F L > 2\pi$) to satisfy the relation $\lambda_F < L$ by introducing a sufficient carrier density ($3.6\times 10^{11}\ \mathrm{cm}^{-2}$) into the channel.

Finally, as discussed earlier, it is necessary that the thermal energy $k_B T \ll E_j - E_{j-1}$ where $E_j - E_{j-1}$ is the subband separation between the $j$ and $j-1$ one dimensional energy levels. Therefore, the quantum conductance measurements are done at low temperatures ($T < 1$ K).

The point contacts in {numref}`fig-p1-ch10-5` were made on high-mobility molecular-beam-epitaxy-grown GaAs-AlGaAs heterostructures using electron beam lithography. The electron density of the material is $3.6\times 10^{11}/\mathrm{cm}^{2}$ and the mobility is $8.5\times 10^{5}\ \mathrm{cm}^{2}/\mathrm{V\,s}$ (at 0.6 K). These values were obtained directly from measurements of the devices themselves. For the transport measurements, a standard Hall bar geometry was defined by wet etching. At a gate voltage of $V_g = -0.6$ V the electron gas underneath the gate is depleted, so that conduction takes place through the point contact only. At this voltage, the point contacts have their maximum effective width $W'_{\max}$, which is about equal to the opening $W$ between the gates. By a further decrease (more negative) of the gate voltage, the width of the point contacts can be reduced, until they are fully pinched off at $V_g = -2.2$ V.

The results agree well with the appearance of conductance steps that are integral multiples of $e^{2}/\pi h$, indicating that the conductance depends directly on the number of 1D subbands that are occupied with electrons. To check the validity of the proposed explanation for these steps in the conductance (see Eq. {eq}`eq-p1-ch10-22`), the effective width $W'$ for the gate was estimated from the voltage $V_g = -0.6$ V to be 3600 Å, which is close to the geometric value for $W$. In {numref}`fig-p1-ch10-5` we see that the average conductance varies linearly with $V_g$ which in turn indicates a linear relation between the effective point contact width $W'$ and $V_g$. From the 16 observed steps and a maximum effective point contact width $W'_{\max} = 3600$ Å, an estimate of 220 Å is obtained for the increase in width per step, corresponding to $\lambda_F/2$.

Theoretical work done by Rolf Landauer nearly 20 years ago shows that transport through the channel can be described by summing up the conductances for all the possible transmission modes, each with a well defined transmission coefficient $t_{nm}$. The conductance of the 1D channel can then be described by the Landauer formula

```{math}
:label: eq-p1-ch10-23
G = \frac{e^{2}}{\pi\hbar}\sum_{n,m=1}^{N_c} |t_{nm}|^{2}
```

where $N_c$ is the number of occupied subbands. If the conditions for perfect quantization described earlier are satisfied, then the transmission coefficient reduces to $|t_{nm}|^{2} = \delta_{nm}$. This corresponds to purely ballistic transport with no scattering or mode mixing in the channel (i.e., no back reflections).

A more explicit derivation of the Landauer formula for the special case of a 1D system can be done as follows. The current flowing in a 1D channel can be written as

```{math}
:label: eq-p1-ch10-24
I_j = \int_{E_i}^{E_f} e g_j(E) v_z(E) T_j(E)\, dE
```

where the electron velocity is given by

```{math}
:label: eq-p1-ch10-25
m^{*}v_z = \hbar k_z
```

and

```{math}
:label: eq-p1-ch10-26
E = E_j + \frac{\hbar^{2} k_z^{2}}{2m^{*}}
```

while the 1D density of states is from Eq. {eq}`eq-p1-ch10-5` given by

```{math}
:label: eq-p1-ch10-27
g_j(E) = \frac{(2m^{*})^{1/2}}{h(E-E_g)^{1/2}}
```

and $T_j(E)$ is the probability that an electron injected into subband $j$ with energy $E$ will get across the 1D wire ballistically. Substitution of Eqs. {eq}`eq-p1-ch10-25`, {eq}`eq-p1-ch10-26` and {eq}`eq-p1-ch10-27` into Eq. {eq}`eq-p1-ch10-24` then yields

```{math}
:label: eq-p1-ch10-28
I_j = \frac{2e}{h}\int_{E_i}^{E_j} T_j(E)\, dE = \frac{2e^{2}}{h} T_j \Delta V
```

where we have noted that the potential energy difference is the difference between initial and final energies $e\Delta V = E_f - E_i$. Summing over all occupied states $j$ we then obtain the Landauer formula

```{math}
:label: eq-p1-ch10-29
G = \frac{2e^{2}}{h}\sum_j T_j .
```

## 10.6 Ballistic Transport in 1D Electron Waveguides

Another interesting quantum-effect structure proposed and implemented by C. Eugster and J. del Alamo is a split-gate dual electron waveguide device shown in {numref}`fig-p1-ch10-6` [C.C. Eugster, J.A. del Alamo, M.J. Rooks and M.R. Melloch, Applied Physics Letters 60, 642 (1992)]. By applying the appropriate negative biases on patterned gates at the surface, two electron waveguides can be formed at the heterointerface of a MODFET structure. As shown in {numref}`fig-p1-ch10-6`, the two electron waveguides are closely spaced over a certain length and their separation is controlled by the middle gate bias ($V_{GM}$). The conductance of each waveguide, shown in {numref}`fig-p1-ch10-7`, is measured simultaneously and independently as a function of the side gate biases ($V_{GT}$ and $V_{GB}$) and each show the quantized $2e^{2}/h$ conductance steps. Such a device can be used to study 1D coupled electron waveguide interactions. An electron directional coupler based on such a structure has also been proposed [J. del Alamo and C. Eugster, Appl. Phys. Lett. 56, 78 (1990)]. Since each gate can be independently accessed, various other regimes can be studied in addition to the coupled waveguide regime.

:::{figure} images/fig-p1-ch10-6.png
:name: fig-p1-ch10-6
:width: 90%
:align: center
Fig. 10.6: (a) Schematic illustration of the split-gate dual electron waveguide device. The top plane shows the patterned gates at the surface of the MODFET structure. The bottom plane shows the implementation of two closely spaced electron waveguides when the gates (indicated by $V_{GT}$, $V_{GB}$ and $V_{GM}$) are properly biased. Shading represents the electron concentration. Also shown are the four ohmic contacts which allow access to the inputs and outputs of each waveguide. (b) Schematic of the "leaky" electron waveguide implementation. The bottom gate is grounded ($V_{GB}=0$) so that only one waveguide is in an "on" state. $V_{GM}$ is fixed such that only a small tunneling current crosses it. The current flowing through the waveguide as well as the tunneling current (depicted by arrows) are monitored simultaneously.
:::

:::{figure} images/fig-p1-ch10-7.png
:name: fig-p1-ch10-7
:width: 70%
:align: center
Fig. 10.7: Conductance of each waveguide in {numref}`fig-p1-ch10-6` (a) as a function of side gate bias of an $L = 0.5$ $\mu$m, $W = 0.3$ $\mu$m split-gate dual electron waveguide device. The inset shows the biasing conditions (i.e., in the depletion regime) and the direction of current flow for the measurements.
:::

One interesting regime is that of a "leaky" electron waveguide [C.C. Eugster and J.A. del Alamo, Physical Review Letters 67, 3586 (1991)]. For such a scheme, one of the side gates is grounded so that the 2D electron gas underneath it is unaffected, as shown in {numref}`fig-p1-ch10-6` (b). The middle gate is biased such that only a small tunneling current can flow from one waveguide to the other in the 2D electron gas. The other outer gate bias $V_{GT}$ is used to sweep the subbands in the waveguide through the Fermi level. In such a scheme, there is only one waveguide which has a thin side wall barrier established by the middle gate bias. The current flowing through the waveguide as well as the current leaking out of the thin middle barrier are independently monitored. {numref}`fig-p1-ch10-8` shows the $I-V_{GS}$ characteristics for the leaky electron waveguide implementation. As discussed earlier, conductance steps of order $2e^{2}/h$ are observed for the current flowing through the waveguide. However what is unique to the leaky electron experiment is that the tunneling current leaking from the thin side wall is monitored. As seen in {numref}`fig-p1-ch10-8`, very strong oscillations in the tunneling current are observed as the Fermi level is modulated in the waveguide. We show below that the tunneling current is directly tracing out the 1D density of states of the waveguide.

:::{figure} images/fig-p1-ch10-8.png
:name: fig-p1-ch10-8
:width: 80%
:align: center
Fig. 10.8: The waveguide current vs gate-source voltage characteristics of a leaky electron waveguide implemented with the proper biases for the device. For this case one of the side-gates in {numref}`fig-p1-ch10-6` (b) is grounded so that only one leaky electron waveguide is on. $I_{S1}$ is the current flowing through the waveguide and $I_{S2}$ is the current tunneling through the thin middle side barrier. The bias voltage $V_{DS}$ between the contacts is 100 $\mu$V.
:::

An expression for the tunneling current $I_{S2}$ flowing through the sidewall of the waveguide can be obtained by the following integral,

```{math}
:label: eq-p1-ch10-30
I_{S2} = e\sum_j \int_{-\infty}^{\infty} v_{\perp j}(E-E_j) g_{1D,j}(E-E_j) T_j(E-E_b) \bigl[f(E-E_F-e\Delta V, T) - f(E-E_F, T)\bigr]\, dE
```

where we have accounted for the contribution to the current from each occupied subband $j$. Here $E_j$ is the energy at the bottom of the $j$th subband and $E_b$ is the height of the tunneling energy barrier. The normal velocity against the tunneling barrier is $v_{\perp j}(E) = \hbar k_{\perp j}/m^{*}$. The transmission coefficient, $T_j(E-E_b)$, to first order, is the same for the different 1D electron subbands since the barrier height relative to the Fermi level $E_F$ is fixed (see {numref}`fig-p1-ch10-9`). The Fermi function, $f$, gives the distribution of electrons as a function of temperature and applied bias $\Delta V$ between the input of the waveguide and the 2DEG on the other side of the tunneling barrier (see {numref}`fig-p1-ch10-9`).

:::{figure} images/fig-p1-ch10-9.png
:name: fig-p1-ch10-9
:width: 50%
:align: center
Fig. 10.9: Cross-section of a leaky electron waveguide. Shaded regions represent electrons. The dashed line is the Fermi level and the solid lines depict the energy levels in the waveguide. The three figures are from top to bottom (a), (b), (c) at increasingly negative gate-source voltage $V_{GT}$.
:::

For low enough temperatures and small $\Delta V$, we can approximate Eq. {eq}`eq-p1-ch10-30` by

```{math}
:label: eq-p1-ch10-31
I_{S2} \cong \frac{e^{2}\hbar}{m^{*}}\sum_j k_{\perp j} T_j(E_F-E_b) g_{1D,j}(E_F-E_j)\, \Delta V
```

where $k_{\perp j}$ is a constant for each subband and has a value determined by the confining potential. As seen by Eq. {eq}`eq-p1-ch10-31`, the tunneling current $I_{S2}$ is proportional to $g_{1D,j}(E_F-E_j)$, the 1D density of states (see {numref}`fig-p1-ch10-10` a). Increasing $V_{GT}$ to less negative values sweeps the subbands through the Fermi level as shown in {numref}`fig-p1-ch10-9` and since $k_{\perp j}$ and $T_j(E_F-E_b)$ are constant for a given subband (see {numref}`fig-p1-ch10-10` d), the 1D density of states $g_{1D,j}$ summed over each subband, can be extracted from measurement of $I_{S2}$ (see {numref}`fig-p1-ch10-10` e).

{numref}`fig-p1-ch10-9` shows a schematic of the cross-section of the waveguide for three different values of the gate source voltage $V_{GT}$. The middle gate bias $V_{GM}$ is fixed and is the same for all three cases. The parabolic potential in {numref}`fig-p1-ch10-9` is a result of the fringing fields and is characteristic of the quantum well for split-gate defined channels. By making $V_{GT}$ more negative, the sidewall potential of the waveguide is raised with respect to the Fermi level. As seen in {numref}`fig-p1-ch10-9`, this results in having fewer energy levels below the Fermi level (i.e., fewer occupied subbands). In {numref}`fig-p1-ch10-9` a, which corresponds to a very negative $V_{GT}$, only the first subband is occupied. At less negative values of $V_{GT}$, the second subband becomes occupied ({numref}`fig-p1-ch10-9` b) and then the third ({numref}`fig-p1-ch10-9` c) and so on.

There is no tunneling current until the first level has some carrier occupation. The tunneling current increases as a new subband crosses below the Fermi-level. The difference between $E_F$ in the quantum well (on the left) and in the metallic contact (on the right) is controlled by the bias voltage between the input and output contacts of the waveguide $V_{DS}$. In fact, a finite voltage $V_{DS}$ and a finite temperature gives rise to lifetime effects and a broadening of the oscillations in $I_{S2}$ (see {numref}`fig-p1-ch10-10` e).

:::{figure} images/fig-p1-ch10-10.png
:name: fig-p1-ch10-10
:width: 90%
:align: center
Fig. 10.10: Summary of leaky electron waveguide phenomena. Top picture (a) represents the 1D density of states for the waveguide. The two left pictures (b) and (c) are for the current flowing through the waveguide ($k_{\parallel}$ is the wavevector along waveguide). Quantized conductance steps result from sweeping subbands through the Fermi level as $I_{S1}$ in {numref}`fig-p1-ch10-8`. The two right hand pictures (d) and (e) are for the tunneling current ($k_{\perp}$ is transverse wavevector). Oscillations in the tunneling current $I_{S2}$ in {numref}`fig-p1-ch10-8` arise from sweeping each subband through the Fermi level.
:::

A summary of the behavior of a leaky electron waveguide is shown in {numref}`fig-p1-ch10-10`. Included in this figure are (a) the 1D density of states $g_{1D}$. The measurement of $I_{S1}$ as shown in {numref}`fig-p1-ch10-8` is modeled in terms of $\sum k_{\parallel} g_{1D,j}$ and the results for $I_{S1}(V_{GT})$ which relate to the steps in the conductance can be used to extract $g_{1D}$ as indicated in {numref}`fig-p1-ch10-10` b and {numref}`fig-p1-ch10-10` c. In contrast, {numref}`fig-p1-ch10-10` d and {numref}`fig-p1-ch10-10` e indicate the multiplication of $k_{\perp,j}$ and $g_{1D,j}$ to obtain $\sum k_{\perp,j} g_{1D,j}$ summed over occupied levels which is measured by the tunneling current $I_{S2}$ in {numref}`fig-p1-ch10-8`. The 1D density of states $g_{1D}$ can then be extracted from either $I_{S1}$ or $I_{S2}$ as indicated in {numref}`fig-p1-ch10-10`.

## 10.7 Single Electron Charging Devices

By making even narrower channels it has been possible to observe single electron charging in a nanometer field-effect transistor, shown schematically in {numref}`fig-p1-ch10-11`. In studies, a metal barrier is placed in the middle of the channel and the width of the metal barrier and the gap between the two constricted gates are of very small dimensions.

:::{figure} images/fig-p1-ch10-11.png
:name: fig-p1-ch10-11
:width: 55%
:align: center
Fig. 10.11: A split gate nanometer field-effect transistor, shown schematically. In the narrow channel a 1D electron gas forms when the gate is biased negatively. The potential of the 1D barrier is shown.
:::

The first experimental observation of single electron charging was by Meirav et al. [U. Meirav, M.A. Kastner and S.J. Wind, Phys. Rev. Lett. 65, 771 (1990); see also M.A. Kastner, Physics Today, page 24, January 1993], working with a double potential barrier GaAs device, as shown in {numref}`fig-p1-ch10-12`. The two dimensional gas forms near the GaAs-GaAlAs interface.

:::{figure} images/fig-p1-ch10-12.png
:name: fig-p1-ch10-12
:width: 90%
:align: center
Fig. 10.12: Schematic drawing of the device structure along with a scanning electron micrograph of one of the double potential barrier samples. An electron gas forms at the top GaAs-AlGaAs interface, with an electron density controlled by the gate voltage $V_g$. The patterned metal electrodes on top define a narrow channel with two potential barriers.
:::

Each of the constrictions in {numref}`fig-p1-ch10-12` is 1000 Å long and the length of the channel between constrictions is 1$\mu$m. When a negative bias voltage ($V_b \sim -0.5$V) is applied to the gate, the electron motion through the gates is constrained. At a threshold gate voltage of $V_t$, the current in the channel goes to zero. This is referred to as Coulomb blockade. If the gate voltage is now increased (positively) above $V_t$, a series of periodic oscillations are observed, as shown in {numref}`fig-p1-ch10-13`. The correlation between the period of the conductance oscillations and the electron density indicates that a single electron is flowing through the double gated structure per oscillation.

:::{figure} images/fig-p1-ch10-13.png
:name: fig-p1-ch10-13
:width: 80%
:align: center
Fig. 10.13: Periodic oscillations of the conductance vs gate voltage $V_g$, measured at $T \approx 50$ mK on a sample-dependent threshold $V_t$. Traces (a) and (b) are for two samples with the same electrode geometry and hence show the same period. Traces (c) and (d) show data for progressively shorter distances between the two constrictions, with a corresponding increase in period. Each oscillation corresponds to the addition of a single electron between the barriers.
:::

The oscillations in {numref}`fig-p1-ch10-13` show the same periodicity when prepared under the same conditions [as in traces (a) and (b)]. As the length $L_0$ between the constrictions is reduced below 1$\mu$m, the oscillation period gets longer. To verify that they had seen single electron charging behavior, Meirav et al. fit the experimental lineshape for a single oscillation to the functional form for the conductance

```{math}
:label: eq-p1-ch10-32
G(\mu) \sim \frac{\partial F}{\partial E} \sim \cosh^{-2}\left[\frac{E-\mu}{2k_B T}\right] .
```

where $\mu$ is the chemical potential, $F(E-\mu, T)$ is the Fermi function and $E$ is the single electron energy in the 2DEG.
