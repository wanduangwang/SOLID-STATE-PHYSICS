---
title: "9 Two Dimensional Electron Gas, Quantum Wells & Semiconductor Superlattices"
abstract: "This chapter discusses two-dimensional electronic systems, including MOSFETs, quantum wells, superlattices, bound states, tunneling through potential barriers, the WKB approximation, the Kronig-Penney model, and resonant tunneling in quantum wells."
---

# 9 Two Dimensional Electron Gas, Quantum Wells & Semiconductor Superlattices

**References:**

- Ando, Fowler and Stern, *Rev. Mod. Phys.* **54** 437 (1982).
- R.F. Pierret, *Field Effect Devices*, Vol. IV of Modular Series on Solid State Devices, Addison-Wesley (1983).
- B.G. Streetman, *Solid State Electronic Devices*, Series in Solid State Physical Electronics, Prentice-Hall (1980).

## 9.1 Two-Dimensional Electronic Systems

One of the most important recent developments in semiconductors, both from the point of view of physics and for the purpose of device developments, has been the achievement of structures in which the electronic behavior is essentially two-dimensional (2D). This means that, at least for some phases of operation of the device, the carriers are confined in a potential such that their motion in one direction is restricted and thus is quantized, leaving only a two-dimensional momentum or $k$-vector which characterizes motion in a plane normal to the confining potential. The major systems where such 2D behavior has been studied are MOS structures, quantum wells and superlattices. More recently, quantization has been achieved in 1-dimension (the quantum wires) and "zero"-dimensions (the quantum dots). These topics are further discussed in Chapter 10 and in the course on semiconductor physics (6.735J).

## 9.2 MOSFETS

One of the most useful and versatile of these structures is the metal-insulator-semiconductor (MIS) layered structures, the most important of these being the metal-oxide-semiconductor (MOS) structures. As shown in Fig. {numref}`fig-p1-ch09-1`, the MOS device is fabricated from a substrate of usually moderately-doped $p$-type or $n$-type silicon which together with its grounded electrode is called the base and labeled B in the figure. On the top of the base is grown an insulating layer of silicon dioxide, followed by a metal layer; this structure is the gate (labeled G in the figure) and is used to apply an electric field through the oxide to the silicon. For the MOS device shown in the figure the base region is $p$-type and the source (S) and drain (D) regions are $n$-type. Measurements of the changes in the properties of the carriers in the silicon layer immediately below the gate (the conductance in the source-drain channel), in response to changes in the applied electric field at the gate electrode, are called field-effect measurements. As we show below, the field dramatically changes the conducting properties of the carriers beneath the gate. Use is made of this effect in the so-called metal-oxide-semiconductor field-effect transistor (MOSFET).

:::{figure} images/fig-p1-ch09-1.png
:name: fig-p1-ch09-1
:width: 70%
:align: center
Fig. 9.1: Cross-sectional view of the basic MOSFET structure showing the terminal designations and standard biasing conditions.
:::

To understand the operation of this device, we first consider the schematic energy band diagram of the MOS structure as shown in Fig. {numref}`fig-p1-ch09-2`, for four different values of $V_G$, the gate potential relative to the substrate. For each $V_G$ value, the diagram shows from left to right the metal (M) - oxide (O) - semiconductor (S) regions. In the semiconductor regions each of the diagrams show from top to bottom: the Si conduction band edge $E_c$, the "intrinsic" Fermi level for undoped Si as the dashed line, the Fermi level $E_F$ in the $p$-type Si, and the valence band edge $E_v$. In each diagram, the central oxide region shows the valence band edge for the oxide. On the left hand side of each diagram, the Fermi level for the metal is shown and the dashed line gives the extension of the Si Fermi level. In the lower part of the figure, the charge layers of the interfaces for each case are illustrated.

:::{figure} images/fig-p1-ch09-2.png
:name: fig-p1-ch09-2
:width: 90%
:align: center
Fig. 9.2: Energy band and block charge diagrams for a $p$-type device under flat band, accumulation, depletion and inversion conditions.
:::

We now explain the diagrams in Fig. {numref}`fig-p1-ch09-2` as a function of the gate voltage $V_G$. For $V_G=0$ (the flat-band case), there are (ideally) no charge layers, and the energy levels of the metal (M) and semiconducting (S) regions line up to yield the same Fermi level (chemical potential). The base region is doped $p$-type. For a negative gate voltage ($V_G<0$, the accumulation case), an electric field is set up in the oxide. The negative gate voltage causes the Si bands to bend up at the oxide interface (see Fig. {numref}`fig-p1-ch09-2`) so that the Fermi level is closer to the valence-band edge. Thus extra holes accumulate at the semiconductor-oxide interface and electrons accumulate at the metal-oxide interface (see lower part of Fig. {numref}`fig-p1-ch09-2`). In the third (depletion) case, the gate voltage is positive but less than some threshold value $V_T$. The voltage $V_T$ is defined as the gate voltage where the intrinsic Fermi level and the actual Fermi level are coincident at the interface (see lower part of Fig. {numref}`fig-p1-ch09-2`). For the "depletion" regime, the Si bands bend down at the interface resulting in a depletion of holes, and a negatively charged layer of localized states is formed at the semiconductor-oxide interface. The size of this "depletion region" increases as $V_G$ increases. The corresponding positively charged region at the metal-oxide interface is also shown. Finally, for $V_G>V_T$, the intrinsic Fermi level at the interface drops below the actual Fermi level, forming the "inversion layer", where mobile electrons reside. It is the electrons in this inversion layer which are of interest, both because they can be confined so as to exhibit two-dimensional behavior, and because they can be controlled by the gate voltage in the MOSFET (see Fig. {numref}`fig-p1-ch09-3`).

:::{figure} images/fig-p1-ch09-3.png
:name: fig-p1-ch09-3
:width: 70%
:align: center
Fig. 9.3: Visualization of various phases of $V_G>V_T$ MOSFET operation. (a) $V_D=0$, (b) channel (inversion layer) narrowing under moderate $V_D$ biasing, (c) pinch-off, and (d) post-pinch-off ($V_D>V_{Dsat}$) operation. (Note that the inversion layer widths, depletion widths, etc. are not drawn to scale.)
:::

The operation of a metal-oxide semiconductor field-effect transistor (MOSFET) is illustrated in Fig. {numref}`fig-p1-ch09-3`, which shows the electron inversion layer under the gate for $V_G>V_T$ (for a $p$-type substrate), with the source region grounded, for various values of the drain voltage $V_D$. The inversion layer forms a conducting "channel" between the source and drain (as long as $V_G>V_T$). The dashed line in Fig. {numref}`fig-p1-ch09-3` shows the boundaries of the depletion region which forms in the $p$-type substrate adjoining the $n^+$ and $p$ regions.

For $V_D=0$ there is obviously no current between the source and the drain since both are at the same potential. For $V_D>0$, the inversion layer or channel acts like a resistor, inducing the flow of electric current $I_D$. As shown in Fig. {numref}`fig-p1-ch09-3`, increasing $V_D$ imposes a reverse bias on the $n^+$-$p$ drain-substrate junction, thereby increasing the width of the depletion region and decreasing the number of carriers and narrowing the channel in the inversion layer as shown in Fig. {numref}`fig-p1-ch09-3`. Finally as $V_D$ increases further, the channel reaches the "pinched-off" condition $V_{Dsat}$ shown in Fig. {numref}`fig-p1-ch09-3`c. Further increase in $V_D$ does not increase $I_D$ but rather causes "saturation". We note that at saturation, $V_{Dsat}=V_G-V_T$. Saturation is caused by a decrease in the carrier density in the channel due to the pinch-off phenomena.

In Fig. {numref}`fig-p1-ch09-4` $I_D$ vs. $V_D$ curves are plotted for fixed values of $V_G>V_T$. We note that $V_{Dsat}$ increases with increasing $V_G$. These characteristic curves are qualitatively similar to the curves for the bipolar junction transistor. The advantage of MOSFET devices lie in the speed of their operation and in the ease with which they can be fabricated into ultra-small devices.

:::{figure} images/fig-p1-ch09-4.png
:name: fig-p1-ch09-4
:width: 60%
:align: center
Fig. 9.4: General form of the $I_D-V_D$ characteristics expected from a long channel ($\Delta L\ll L$) MOSFET.
:::

The MOSFET device, or an array of a large number of MOSFET devices, is fabricated starting with a large Si substrate or "wafer". At each stage of fabrication, areas of the wafer which are to be protected are masked off using a light-sensitive substance called photoresist, which is applied as a thin film, exposed to light (or an electron or x-ray beam) through a mask of the desired pattern, then chemically developed to remove the photoresist from only the exposed (or, sometimes only the un-exposed) area. First the source and drain regions are formed by either diffusing or implanting (bombarding) donor ions into the $p$-type substrate. Then a layer of SiO$_2$ (which is an excellent and stable insulator) is grown by exposing the desired areas to an atmosphere containing oxygen; usually only a thin layer is grown over the gate regions and, in a separate step, thicker oxide layers are grown between neighboring devices to provide electrical isolation. Finally, the metal gate electrode, the source and drain contacts are formed by sputtering or evaporating a metal such as aluminum onto the desired regions.

## 9.3 Two-Dimensional Behavior

Other systems where two-dimensional behavior has been observed include heterojunctions of III-V compounds such as GaAs/Ga$_{1-x}$Al$_x$As, layer compounds such as GaSe, GaSe$_2$ and related III-VI compounds, graphite and intercalated graphite, and electrons on the surface of liquid helium. The GaAs/Ga$_{1-x}$Al$_x$As heterojunctions are important for device applications because the lattice constants and the coefficient of expansion of GaAs and Ga$_{1-x}$Al$_x$As are very similar. This lattice matching permits the growth of high mobility thin films of Ga$_{1-x}$Al$_x$As on a GaAs substrate.

The interesting physical properties of the MOSFET lie in the two-dimensional behavior of the electrons in the channel inversion layer at low temperatures. Studies of these electrons have provided important tests of modern theories of localization, electron-electron interactions and many-body effects. In addition, the MOSFETs have exhibited a highly unexpected property that, in the presence of a magnetic field normal to the inversion layer, the transverse or Hall resistance $\rho_{xy}$ is quantized in integer values of $e^2/h$. This quantization is accurate to parts in $10^7$ or $10^8$ and provides the best measure to date of the fine structure constant $\alpha=e^2/hc$, when combined with the precisely-known velocity of light $c$. We will further discuss the quantized Hall effect later in the course (Part III).

We now discuss the two-dimensional behavior of the MOSFET devices in the absence of a magnetic field. The two-dimensional behavior is associated with the nearly plane wave electron states in the inversion layer. The potential $V(z)$ is associated with the electric field $V(z)=eEz$ and because of the negative charge on the electron, a potential well is formed containing bound states described by quantized levels. A similar situation occurs in the two-dimensional behavior for the case of electrons in quantum wells produced by molecular beam epitaxy. Explicit solutions for the bound states in quantum wells are given in \S 9.4. We discuss in the present section the form of the differential equation and of the resulting eigenvalues and eigenfunctions.

A single electron in a one-dimensional potential well $V(z)$ will, from elementary quantum mechanics, have discrete allowed energy levels $E_n$ corresponding to bound states and usually a continuum of levels at higher energies corresponding to states which are not bound. An electron in a bulk semiconductor is in a three-dimensional periodic potential. In addition the potential causing the inversion layer of a MOSFET or a quantum well in GaAs/Ga$_{1-x}$Al$_x$As can be described by a one-dimensional confining potential $V(z)$ and can be written using the effective-mass theorem

```{math}
:label: eq-p1-ch09-1
[E(-i\vec{\nabla}) + \mathcal{H}'] \Psi = i\hbar \left( \frac{\partial \Psi}{\partial t} \right)
```

where $\mathcal{H}'=V(z)$. The energy eigenvalues near the band edge can be written as

```{math}
:label: eq-p1-ch09-2
E(\vec{k}) = E(\vec{k}_0) + \frac{1}{2} \sum_{i,j} \left( \frac{\partial^2 E}{\partial k_i \partial k_j} \right) k_i k_j
```

so that the operator $E(-i\vec{\nabla})$ in Eq. {eq}`eq-p1-ch09-1` can be written as

```{math}
:label: eq-p1-ch09-3
E(-i\vec{\nabla}) = \sum_{i,j} \frac{p_i p_j}{2m_{i,j}}
```

where the $p_i$'s are the operators

```{math}
:label: eq-p1-ch09-4
p_i = \frac{\hbar}{i} \frac{\partial}{\partial x_i}
```

which are substituted into Schr\"odinger's equation. The effect of the periodic potential is contained in the reciprocal of the effective mass tensor

```{math}
:label: eq-p1-ch09-5
\frac{1}{m_{ij}} = \frac{1}{\hbar^2} \frac{\partial^2 E(\vec{k})}{\partial k_i \partial k_j} \bigg|_{\vec{k}=\vec{k}_0}
```

where the components of $1/m_{ij}$ are evaluated at the band edge at $\vec{k}_0$.

If $1/m_{ij}$ is a diagonal matrix, the effective-mass equation $\mathcal{H}\Psi=E\Psi$ is solved by a function of the form

```{math}
:label: eq-p1-ch09-6
\Psi_{n,k_x,k_y} = e^{ik_x x} e^{ik_y y} f_n(z)
```

where $f_n(z)$ is a solution of the equation

```{math}
:label: eq-p1-ch09-7
-\frac{\hbar^2}{2m_{zz}} \frac{d^2 f_n}{dz^2} + V(z) f_n = E_{n,z} f_n
```

and the total energy is

```{math}
:label: eq-p1-ch09-8
E_n(k_x,k_y) = E_{n,z} + \frac{\hbar^2}{2m_{xx}} k_x^2 + \frac{\hbar^2}{2m_{yy}} k_y^2 .
```

Since the $E_{n,z}$ energies $(n=0,1,2,...)$ are discrete, the energies states $E_n(k_x,k_y)$ for each $n$ value form a "sub-band". We give below (in \S 9.3.1) a simple derivation for the discrete energy levels for considering a particle in various potential wells (i.e., quantum wells). The electrons in these "sub-bands" form a 2D electron gas.

### 9.3.1 Quantum Wells and Superlattices

Many of the quantum wells and superlattices that are commonly studied today do not occur in nature, but rather are deliberately structured materials (see Fig. {numref}`fig-p1-ch09-5`). In the case of superlattices formed by molecular beam epitaxy, the quantum wells result from the different bandgaps of the two constituent materials. The additional periodicity is in one-dimension (1-D) which we take along the $z$-direction, and the electronic behavior is usually localized on the basal planes ($x$-$y$ planes) normal to the $z$-direction, giving rise to two-dimensional behavior.

:::{figure} images/fig-p1-ch09-5.png
:name: fig-p1-ch09-5
:width: 90%
:align: center
Fig. 9.5: (a) A heterojunction superlattice of periodicity $d$. (b) Each superlattice unit cell consists of a thickness $d_1$ of material \#1 and $d_2$ of material \#2. Because of the different band gaps in the two semiconductors, a periodic array of potential wells and potential barriers is formed. When the band offsets are both positive as shown in this figure, the structure is called a type I superlattice.
:::

A schematic representation of a semiconductor heterostructure superlattice is shown in Fig. {numref}`fig-p1-ch09-5` where $d$ is the superlattice periodicity composed of a distance $d_1$, of semiconductor $S_1$, and $d_2$ of semiconductor $S_2$. Because of the different band gaps in the two semiconductors, potential wells and barriers are formed. For example in Fig. {numref}`fig-p1-ch09-5`, the barrier heights in the conduction and valence bands are $\Delta E_c$ and $\Delta E_v$ respectively. In Fig. {numref}`fig-p1-ch09-5` we see that the difference in bandgaps between the two semiconductors gives rise to band offsets $\Delta E_c$ and $\Delta E_v$ for the conduction and valence bands. In principle, these band offsets are determined by matching the Fermi levels for the two semiconductors. In actual materials, the Fermi levels are highly sensitive to impurities, defects and charge transfer at the heterojunction interface.

The two semiconductors of a heterojunction superlattice could be different semiconductors such as InAs with GaP (see Table {numref}`tab-p1-ch09-1` for parameters related to these compounds) or a binary semiconductor with a ternary alloy semiconductor, such as GaAs with Al$_x$Ga$_{1-x}$As (sometimes referred to by their slang names "Gaas" and "Algaas"). In the typical semiconductor superlattices the periodicity $d=d_1+d_2$ is repeated many times (e.g., 100 times). The period thicknesses typically vary between a few layers and many layers (10\AA\ to 500\AA). Semiconductor superlattices are today an extremely active research field internationally.

The electronic states corresponding to the heterojunction superlattices are of two fundamental types--bound states in quantum wells and nearly free electron states in zone-folded energy bands. In this course, we will limit our discussion to the bound states in a single infinite quantum well. Generalizations to multiple quantum wells will be made subsequently.

:::{table} Table 9.1: Material parameters of GaAs, GaP, InAs, and InP.
:name: tab-p1-ch09-1
| Property | Parameter (units) | GaAs | GaP | InAs | InP |
|----------|-------------------|------|-----|------|-----|
| Lattice constant | $a$ (\AA) | 5.6533 | 5.4512 | 6.0584 | 5.8688 |
| Density | $g$ (g/cm$^3$) | 5.307 | 4.130 | 5.667 | 4.787 |
| Thermal expansion | $\alpha_{th}$ ($\times 10^{-6}/{}^\circ$C) | 6.63 | 5.91 | 5.16 | 4.56 |
| $\Gamma$ point band gap | $E_0$ (eV) | 1.42 | 2.74 | 0.36 | 1.35 |
| plus spin orbit | $E_0+\Delta_0$ (eV) | 1.76 | 2.84 | 0.79 | 1.45 |
| $L$ point band gap | $E_1$ (eV) | 2.925 | 3.75 | 2.50 | 3.155 |
| plus spin orbit | $E_1+\Delta_1$ (eV) | 3.155 | ... | 2.78 | 3.305 |
| $\Gamma$ axis band gap | $E_0'$ (eV) | 4.44 | 4.78 | 4.44 | 4.72 |
| $\Delta$ axis band gap | $E_2$ (eV) | 4.99 | 5.27 | 4.70 | 5.04 |
| plus spin orbit | $E_2+\delta$ (eV) | 5.33 | 5.74 | 5.18 | 5.60 |
| Gap pressure coefficient | $\partial E_0/\partial P$ ($\times 10^{-6}$ eV/bar) | 11.5 | 11.0 | 10.0 | 8.5 |
| Gap temperature coefficient | $\partial E_0/\partial T$ ($\times 10^{-4}$ eV/$^\circ$C) | $-3.95$ | $-4.6$ | $-3.5$ | $-2.9$ |
| Electron mass | $m^*/m_0$ | 0.067 | 0.17 | 0.023 | 0.08 |
| light hole | $m_{\ell h}{}^*/m_0$ | 0.074 | 0.14 | 0.027 | 0.089 |
| heavy hole | $m_{hh}{}^*/m_0$ | 0.62 | 0.79 | 0.60 | 0.85 |
| spin orbit hole | $m_{so}{}^*/m_0$ | 0.15 | 0.24 | 0.089 | 0.17 |
| Dielectric constant: static | $\epsilon_s$ | 13.1 | 11.1 | 14.6 | 12.4 |
| Dielectric constant: optic | $\epsilon_\infty$ | 11.1 | 8.46 | 12.25 | 9.55 |
| Ionicity | $f_1$ | 0.310 | 0.327 | 0.357 | 0.421 |
| Polaron coupling | $\alpha_F$ | 0.07 | 0.20 | 0.05 | 0.08 |
| Elastic constants | $c_{11}$ ($\times 10^{11}$ dyn/cm$^2$) | 11.88 | 14.120 | 8.329 | 10.22 |
|  | $c_{12}$ ($\times 10^{11}$ dyn/cm$^2$) | 5.38 | 6.253 | 4.526 | 5.76 |
|  | $c_{44}$ ($\times 10^{11}$ dyn/cm$^2$) | 5.94 | 7.047 | 3.959 | 4.60 |
| Young's modulus | $Y$ ($\times 10^{11}$ dyn/cm$^2$) | 8.53 | 10.28 | 5.14 | 6.07 |
|  | $P$ | 0.312 | 0.307 | 0.352 | 0.360 |
| Bulk modulus | $B$ ($\times 10^{11}$ dyn/cm$^2$) | 7.55 | 8.88 | 5.79 | 7.25 |
|  | $A$ | 0.547 | 0.558 | 0.480 | 0.485 |
| Piezo-electric coupling | $e_{14}$ (C/m$^2$) | $-0.16$ | $-0.10$ | $-0.045$ | $-0.035$ |
|  | $K_{[110]}$ | 0.0617 | 0.0384 | 0.0201 | 0.0158 |
| Deformation potential | $a$ (eV) | 2.7 | 3.0 | 2.5 | 2.9 |
|  | $b$ (eV) | $-1.7$ | $-1.5$ | $-1.8$ | $-2.0$ |
|  | $d$ (eV) | $-4.55$ | $-4.6$ | $-3.6$ | $-5.0$ |
| Deformation potential | $\Xi_{eff}$ (eV) | 6.74 | 6.10 | 6.76 | 7.95 |
| Donor binding | $G$ (meV) | 4.4 | 10.0 | 1.2 | 5.5 |
| Donor radius | $a_B$ (\AA) | 136 | 48 | 406 | 106 |
| Thermal conductivity | $\kappa$ (watt/deg $-$ cm) | 0.46 | 0.77 | 0.273 | 0.68 |
| Electron mobility | $\mu_n$ (cm$^2$/V $-$ sec) | 8000 | 120 | 30000 | 4500 |
| Hole mobility | $\mu_p$ (cm$^2$/V $-$ sec) | 300 | $-$ | 450 | 100 |
:::

$^1$Table from *J. Appl. Physics* **53**, 8777 (1982).

## 9.4 Bound Electronic States

From the diagram in Fig. {numref}`fig-p1-ch09-5` we see that the heterojunction superlattice consists of an array of potential wells. The interesting limit to consider is the case where the width of the potential well contains only a small number of crystallographic unit cells ($L_z<100$ \AA), in which case the number of bound states in the well is a small number.

From a mathematical standpoint, the simplest case to consider is an infinitely deep rectangular potential well. In this case, a particle of mass $m^*$ in a well of width $L_z$ in the $z$ direction satisfies the free particle Schr\"odinger equation

```{math}
:label: eq-p1-ch09-9
-\frac{\hbar^2}{2m^*} \frac{d^2 \psi}{dz^2} = E \psi
```

with eigenvalues

```{math}
:label: eq-p1-ch09-10
E_n = \frac{\hbar^2}{2m^*} \left(\frac{n\pi}{L_z}\right)^2 = \left(\frac{\hbar^2 \pi^2}{2m^* L_z^2}\right) n^2
```

and the eigenfunctions

```{math}
:label: eq-p1-ch09-11
\psi_n = A \sin(n\pi z / L_z)
```

where $n=1,2,3,...$ are the plane wave solutions that satisfy the boundary conditions that the wave functions in Eq. {eq}`eq-p1-ch09-11` must vanish at the walls of the quantum wells ($z=0$ and $z=L_z$).

We note that the energy levels are not equally spaced, but have energies $E_n \sim n^2$, though the spacings $E_{n+1}-E_n$ are proportional to $n$. We also note that $E_n \sim L_z^{-2}$, so that as $L_z$ becomes large, the levels become very closely spaced as expected for a 3D semiconductor. However when $L_z$ decreases, the number of states in the quantum well decreases, so that for a well depth $E_d$ it would seem that there is a critical width $L_z{}^c$ below which there would be no bound states

```{math}
:label: eq-p1-ch09-12
L_z{}^c = \frac{\hbar \pi}{(2m^* E_d)^{1/2}} .
```

An estimate for $L_z{}^c$ is obtained by taking $m^*=0.1m_0$ and $E_d=0.1$ eV to yield $L_z{}^c=61$\AA. There is actually a theorem in quantum mechanics that says that there will be at least one bound state for an arbitrarily small potential well. More exact calculations considering quantum wells of finite thickness have been carried out, and show that the infinite well approximation gives qualitatively correct results.

:::{figure} images/fig-p1-ch09-6.png
:name: fig-p1-ch09-6
:width: 60%
:align: center
Fig. 9.6: The eigenfunctions and bound state energies of an infinitely deep potential well used as an approximation to the states in two finite wells. The upper well applies to electrons and the lower one to holes. This diagram is a schematic representation of a quantum well in the GaAs region formed by the adjacent wider gap semiconductor Al$_x$Ga$_{1-x}$As.
:::

The closer level spacing of the valence band bound states in Fig. {numref}`fig-p1-ch09-6` reflects the heavier masses in the valence band. Since the states in the potential well are quantized, the structures in Figs. {numref}`fig-p1-ch09-5` and {numref}`fig-p1-ch09-6` are called quantum well structures.

If the potential energy of the well $V_0$ is not infinite but finite, the wave functions are similar to those given in Eq. {eq}`eq-p1-ch09-11`, but will have decaying exponentials on either side of the potential well walls. The effect of the finite size of the well on the energy levels and wave functions is most pronounced near the top of the well. When the particle has an energy greater than $V_0$, its eigenfunction corresponds to a continuum state $\exp(ik_z z)$.

In the case of MOSFETs, the quantum well is not of rectangular shape as shown in Fig. {numref}`fig-p1-ch09-7`, but rather is approximated as a triangular well. The solution for the bound states in a triangular well cannot be solved exactly, but can only be done approximately, as for example using the WKB approximation described in \S 9.6.

:::{figure} images/fig-p1-ch09-7.png
:name: fig-p1-ch09-7
:width: 70%
:align: center
Fig. 9.7: Schematic of a potential barrier.
:::

## 9.5 Review of Tunneling Through a Potential Barrier

When the potential well is finite, the wave functions do not completely vanish at the walls of the well, so that tunneling through the potential well becomes possible. We now briefly review the quantum mechanics of tunneling through a potential barrier. We will return to tunneling in semiconductor heterostructures after some introductory material.

Suppose that the potential $V$ shown in Fig. {numref}`fig-p1-ch09-7` is zero ($V=0$) in regions \#1 and \#3, while $V=V_0$ in region \#2. Then in regions \#1 and \#3

```{math}
:label: eq-p1-ch09-13
E = \frac{\hbar^2 k^2}{2m^*}
```

```{math}
:label: eq-p1-ch09-14
\psi = e^{ikz}
```

while in region \#2 the wave function is exponentially decaying

```{math}
:label: eq-p1-ch09-15
\psi = \psi_0 e^{-\beta z}
```

so that substitution into Schr\"odinger's equation gives

```{math}
:label: eq-p1-ch09-16
\frac{-\hbar^2}{2m^*} \beta^2 \psi + (V_0-E)\psi = 0
```

or

```{math}
:label: eq-p1-ch09-17
\beta^2 = \frac{2m^*}{\hbar^2} (V_0 - E) .
```

The probability that the electron tunnels through the rectangular potential barrier is then given by

```{math}
:label: eq-p1-ch09-18
\mathcal{P} = \exp\left\{-2\int_0^{L_z} \beta(z) dz\right\} = \exp\left\{-2\left(\frac{2m^*}{\hbar^2}\right)^{1/2} (V_0-E)^{1/2} L_z\right\}
```

As $L_z$ increases, the probability of tunneling decreases exponentially. Electron tunneling phenomena frequently occur in solid state physics.

:::{figure} images/fig-p1-ch09-8.png
:name: fig-p1-ch09-8
:width: 70%
:align: center
Fig. 9.8: Schematic of a rectangular well.
:::

## 9.6 Quantum Wells of Different Shape and the WKB Approximation

With the sophisticated computer control available with state of the art molecular beam epitaxy systems it is now possible to produce quantum wells with specified potential profiles $V(z)$ for semiconductor heterojunction superlattices. Potential wells with non-rectangular profiles also occur in the fabrication of other types of superlattices (e.g., by modulation doping). We therefore briefly discuss (in the recitation class) bound states in general potential wells.

In the general case where the potential well has an arbitrary shape, solution by the WKB (Wentzel-Kramers-Brillouin) approximation is very useful (see for example, Shanker, "Principles of Quantum Mechanics", Plenum press, chapter 6). According to this approximation, the energy levels satisfy the Bohr-Sommerfeld quantization condition

```{math}
:label: eq-p1-ch09-19
\int_{z_1}^{z_2} p_z dz = \hbar \pi (r + c_1 + c_2)
```

where $p_z=(2m^*[E-V])^{1/2}$ and the quantum number $r$ is an integer $r=0,1,2,...$ while $c_1$ and $c_2$ are the phases which depend on the form of $V(z)$ at the turning points $z_1$ and $z_2$ where $V(z_i)=E$. If the potential has a sharp discontinuity at a turning point, then $c=1/2$, but if $V$ depends linearly on $z$ at the turning point then $c=1/4$.

For example for the infinite rectangular well (see Fig. {numref}`fig-p1-ch09-8`)

```{math}
:label: eq-p1-ch09-20
V(z) = 0 \quad \text{for } |z|<a \quad \text{(inside the well)}
```

```{math}
:label: eq-p1-ch09-21
V(z) = \infty \quad \text{for } |z|>a \quad \text{(outside the well)}
```

By the WKB rules, the turning points occur at the edges of the rectangular well and therefore $c_1=c_2=1/2$. In this case $p_z$ is a constant, independent of $z$ so that $p_z=(2m^*E)^{1/2}$ and Eq. {eq}`eq-p1-ch09-19` yields

```{math}
:label: eq-p1-ch09-22
(2m^*E)^{1/2} L_z = \hbar \pi (r+1) = \hbar \pi n
```

where $n=r+1$ and

```{math}
:label: eq-p1-ch09-23
E_n = \frac{\hbar^2 \pi^2}{2m^* L_z^2} n^2
```

in agreement with the exact solution given by Eq. {eq}`eq-p1-ch09-10`. The finite rectangular well shown in Fig. {numref}`fig-p1-ch09-8` is thus approximated as an infinite well with solutions given by Eq. {eq}`eq-p1-ch09-10`.

As a second example consider a harmonic oscillator potential well shown in Fig. {numref}`fig-p1-ch09-9`, where $V(z)=m^*\omega^2 z^2/2$. The harmonic oscillator potential well is typical of quantum wells in periodically doped (nipi which is $n$-type; insulator; $p$-type; insulator) superlattices. In this case

```{math}
:label: eq-p1-ch09-24
p_z = (2m^*)^{1/2} \left(E - \frac{m^*\omega^2}{2} z^2\right)^{1/2} .
```

:::{figure} images/fig-p1-ch09-9.png
:name: fig-p1-ch09-9
:width: 70%
:align: center
Fig. 9.9: Schematic of a harmonic oscillator well.
:::

The turning points occur when $V(z)=E$ so that the turning points are given by $z=\pm (2E/m^*\omega^2)^{1/2}$. Near the turning points $V(z)$ is approximately linear in $z$, so the phase factors become $c_1=c_2=1/4$. The Bohr-Sommerfeld quantization thus yields

```{math}
:label: eq-p1-ch09-25
\int_{z_1}^{z_2} p_z dz = \int_{z_1}^{z_2} (2m^*)^{1/2} \left(E - \frac{m^*\omega^2}{2} z^2\right)^{1/2} dz = \hbar \pi \left(r + \frac{1}{2}\right) .
```

:::{figure} images/fig-p1-ch09-10.png
:name: fig-p1-ch09-10
:width: 70%
:align: center
Fig. 9.10: Schematic of a triangular well.
:::

Making use of the integral relation

```{math}
:label: eq-p1-ch09-26
\int \sqrt{a^2-u^2}\, du = \frac{u}{2}\sqrt{a^2-u^2} + \frac{a^2}{2}\sin^{-1}\frac{u}{a}
```

we obtain upon substitution of Eq. {eq}`eq-p1-ch09-26` into {eq}`eq-p1-ch09-25`:

```{math}
:label: eq-p1-ch09-27
(2m^*)^{1/2} \left(\frac{m^*\omega^2}{2}\right)^{1/2} \left(\frac{E_r}{m^*\omega^2}\right) \pi = \frac{E_r \pi}{\omega} = \hbar \pi \left(r+\frac{1}{2}\right)
```

which simplifies to the familiar relation for the harmonic oscillator energy levels:

```{math}
:label: eq-p1-ch09-28
E_r = \hbar\omega\left(r+\frac{1}{2}\right) \quad \text{where} \quad r=0,1,2...
```

another example of an exact solution. For homework, you will use the WKB method to find the energy levels for an asymmetric triangular well. Such quantum wells are typical of the interface of metal-insulator-semiconductor (MOSFET) device structures (see Fig. {numref}`fig-p1-ch09-10`).

## 9.7 The Kronig–Penney Model

We review here the Kronig-Penney model which gives an explicit solution for a one-dimensional array of finite potential wells shown in Fig. {numref}`fig-p1-ch09-11`. Starting with the one dimensional Hamiltonian with a periodic potential (see Eq. {eq}`eq-p1-ch09-7`)

```{math}
:label: eq-p1-ch09-29
-\frac{\hbar^2}{2m^*} \frac{d^2\psi}{dz^2} + V(z)\psi = E\psi
```

:::{figure} images/fig-p1-ch09-11.png
:name: fig-p1-ch09-11
:width: 80%
:align: center
Fig. 9.11: Kronig-Penney square well periodic potential.
:::

we obtain solutions in the region $0<z<a$ where $V(z)=0$

```{math}
:label: eq-p1-ch09-30
\psi(z) = A e^{iKz} + B e^{-iKz}
```

```{math}
:label: eq-p1-ch09-31
E = \frac{\hbar^2 K^2}{2m^*}
```

and in the region $-b<z<0$ where $V(z)=V_0$ (the barrier region)

```{math}
:label: eq-p1-ch09-32
\psi(z) = C e^{\beta z} + D e^{-\beta z}
```

where

```{math}
:label: eq-p1-ch09-33
\beta^2 = \frac{2m^*}{\hbar^2} [V_0 - E] .
```

Continuity of $\psi(z)$ and $d\psi(z)/dz$ at $z=0$ and $z=a$ determines the coefficients $A,B,C,D$. At $z=0$ we have:

```{math}
:label: eq-p1-ch09-34
\begin{aligned}
A+B &= C+D \\
iK(A-B) &= \beta(C-D)
\end{aligned}
```

At $z=a$, we apply Bloch's theorem (see Fig. {numref}`fig-p1-ch09-11`), introducing a factor $\exp[ik(a+b)]$ to obtain $\psi(a)=\psi(-b)\exp[ik(a+b)]$

```{math}
:label: eq-p1-ch09-35
\begin{aligned}
Ae^{iKa} + Be^{-iKa} &= (Ce^{-\beta b} + De^{\beta b}) e^{ik(a+b)} \\
iK(Ae^{iKa} - Be^{-iKa}) &= \beta(Ce^{-\beta b} - De^{\beta b}) e^{ik(a+b)} .
\end{aligned}
```

These 4 equations (Eqs. {eq}`eq-p1-ch09-34` and {eq}`eq-p1-ch09-35`) in 4 unknowns determine $A,B,C,D$. The vanishing of the coefficient determinant restricts the conditions under which solutions to the Kronig-Penney model are possible, leading to the algebraic equation

```{math}
:label: eq-p1-ch09-36
\frac{\beta^2 - K^2}{2\beta K} \sinh \beta b \sin Ka + \cosh \beta b \cos Ka = \cos k(a+b)
```

which has solutions for a limited range of $\beta$ values.

:::{figure} images/fig-p1-ch09-12.png
:name: fig-p1-ch09-12
:width: 60%
:align: center
Fig. 9.12: Plot of energy vs. $k$ for the Kronig-Penney model with $P=3\pi/2$. (After Sommerfeld and Bethe.)
:::

Normally the Kronig-Penney model in the textbooks is solved in the limit $b\to 0$ and $V_0\to\infty$ in such a way that $[\beta^2 b a/2]=P$ remains finite. The restricted solutions in this limit lead to the energy bands shown in Fig. {numref}`fig-p1-ch09-12`.

For the superlattice problem we are interested in solutions both within the quantum wells and in the continuum. This is one reason for discussing the Kronig-Penney model. Another reason for discussing this model is because it provides a review of boundary conditions and the application of Bloch's theorem. In the quantum wells, the permitted solutions give rise to narrow bands with large band gaps while in the continuum regions the solutions correspond to wide bands and small band gaps.

## 9.8 3D Motion within a 1-D Rectangular Well

The thin films used for the fabrication of quantum well structures (see \S 9.4) are very thin in the $z$-direction but have macroscopic size in the perpendicular $x$-$y$ plane. An example of a quantum well structure would be a thin layer of GaAs sandwiched between two thicker Al$_x$Ga$_{1-x}$As layers, as shown in the Fig. {numref}`fig-p1-ch09-5`. For the thin film, the motion in the $x$ and $y$ directions is similar to that of the corresponding bulk solid which can be treated by the conventional 1-electron approximation and the Effective Mass Theorem. Thus the potential can be written as a sum of a periodic term $V(x,y)$ and the quantum well term $V(z)$. The electron energies thus are superimposed on the quantum well energies, the periodic solutions obtained from solution of the 2-D periodic potential

```{math}
:label: eq-p1-ch09-37
E_n(k_x,k_y) = E_{n,z} + \frac{\hbar^2(k_x^2+k_y^2)}{2m^*} = E_{n,z} + E_\perp
```

:::{figure} images/fig-p1-ch09-13.png
:name: fig-p1-ch09-13
:width: 60%
:align: center
Fig. 9.13: Subbands associated with bound states for the 2D electron gas.
:::

in which the quantized bound state energies $E_{n,z}$ are given by Eq. {eq}`eq-p1-ch09-10`. A plot of the energy levels is given in Fig. {numref}`fig-p1-ch09-13`. At $(k_x,k_y)=(0,0)$ the energy is precisely the quantum well energy $E_n$ for all $n$. The band of energies associated with each state $n$ is called a subband.

Of particular interest is the density of states for the quantum well structures. Associated with each two-dimensional subband is a constant density of states, as derived below. From elementary considerations the number of electrons per unit area in a 2-dimensional circle is given by

```{math}
:label: eq-p1-ch09-38
N_{2D} = \frac{2}{(2\pi)^2} \pi k_\perp^2
```

where $k_\perp^2=k_x^2+k_y^2$ and

```{math}
:label: eq-p1-ch09-39
E_\perp = \frac{\hbar^2 k_\perp^2}{2m^*}
```

so that for each subband the density of states $g_{2D}(E)$ contribution becomes

```{math}
:label: eq-p1-ch09-40
\frac{\partial N_{2D}}{\partial E} = g_{2D}(E) = \frac{m^*}{\pi\hbar^2} .
```

If we now plot the density of states corresponding to the 3D motion in a 1-D rectangular well, we have $g_{2D}(E)=0$ until the bound state energy $E_1$ is reached, when a step function contribution of $(m^*/\pi\hbar^2)$ is made. The density of states $g_{2D}(E)$ will then remain constant until the minimum of subband $E_2$ is reached when an additional step function contribution of $(m^*/\pi\hbar^2)$ is made, hence yielding the staircase density of states shown in Fig. {numref}`fig-p1-ch09-14`. Two generalizations of Eq. {eq}`eq-p1-ch09-40` for the density of states for actual quantum wells are needed, as we discuss below. The first generalization takes into account the finite size $L_z$ of the quantum well, so that the system is not completely two dimensional and some $k_z$ dispersion must occur. Secondly, the valence bands of typical semiconductors are degenerate so that coupling between the valence band levels occurs, giving rise to departures from the simple parabolic bands discussed below.

:::{figure} images/fig-p1-ch09-14.png
:name: fig-p1-ch09-14
:width: 60%
:align: center
Fig. 9.14: Two dimensional density of states $g_{2D}(E)$ for rectangular quantum well structures.
:::

A generalization of the simple 2D density of states in Fig. {numref}`fig-p1-ch09-14` is also necessary to treat the complex valence band of a typical III-V compound semiconductor. The $E(\vec{k})$ diagram (where $k_\perp$ is normal to $k_z$) for the heavy hole and light hole levels can be calculated using $\vec{k}\cdot\vec{p}$ perturbation theory to be discussed later in the course.

The most direct evidence for bound states in quantum wells comes from optical absorption measurements (to be discussed later in the course) and resonant tunneling effects which we discuss below.

## 9.9 Resonant Tunneling in Quantum Wells

Resonant tunneling (see Fig. {numref}`fig-p1-ch09-18`) provides direct evidence for the existence of bound states in quantum wells. We review first the background material for tunneling across potential barriers in semiconductors and then apply these concepts to the resonant tunneling phenomenon.

The carriers in the quantum well structures are normally described in terms of the effective mass theorem where the wave functions for the carriers are given by the one electron approximation. The effective mass equation is written in terms of slowly varying wavefunctions corresponding to a slowly varying potential which satisfies Poisson's equation when an electric field is applied (e.g., a voltage is imposed across the quantum well structure).

Further simplifications that are made in treating the tunneling problem include:

1. The wavefunctions for the tunneling particle are expanded in terms of a single band on either side of the junction.

2. Schr\"odinger's equation is separated into two components, parallel and perpendicular to the junction plane, leading to a 1-dimensional tunneling problem.

3. The eigenstates of interest have energies sufficiently near those of critical points in the energy band structure on both sides of the interface so that the simplified form of the effective mass theorem can be used.

4. The total energy, $E$, and the momentum parallel to the interface or perpendicular to the layering direction, $k_\perp$, are conserved in the tunneling process. Since the potential acts only in the $z$-direction, the 1-dimensional Schr\"odinger equation becomes:

```{math}
:label: eq-p1-ch09-41
\left[-\frac{\hbar^2}{2m} \frac{d^2}{dz^2} + V(z) - E\right] \psi_e = 0
```

where $V(z)$ is the electrostatic potential, and $\psi_e$ is an envelope function. The wave function $\psi_e$ is subject, at an interface $z=z_1$ (see Fig. {numref}`fig-p1-ch09-16`), to the following boundary conditions that guarantee current conservation:

```{math}
:label: eq-p1-ch09-42
\psi_e(z_1^-) = \psi_e(z_1^+)
```

```{math}
:label: eq-p1-ch09-43
\frac{1}{m_1} \frac{d\psi_e}{dz}\bigg|_{z_1^-} = \frac{1}{m_2} \frac{d\psi_e}{dz}\bigg|_{z_1^+}
```

:::{figure} images/fig-p1-ch09-15.png
:name: fig-p1-ch09-15
:width: 80%
:align: center
Fig. 9.15: Schematic diagrams of (a) energy dispersion and (b) density of states. Indicated are the two-dimensional (dotted), three-dimensional (dashed), and intermediate (solid) cases.
:::

The current density for tunneling through a barrier becomes

```{math}
:label: eq-p1-ch09-44
J_z = \frac{e}{4\pi^3 \hbar} \int dk_z\, d^2k_\perp\, f(E)\, T(E_z)\, \frac{dE}{dk_z}
```

:::{figure} images/fig-p1-ch09-16.png
:name: fig-p1-ch09-16
:width: 80%
:align: center
Fig. 9.16: Rectangular-potential model (a) used to describe the effect of an insulator, 2, between two metals, 1 and 3. When a negative bias is applied to 1, electrons, with energies up to the Fermi energy $E_F$, can tunnel through the barrier. For small voltages, (b), the barrier becomes trapezoidal, but at high bias (c), it becomes triangular.
:::

where $f(E)$ is the Fermi-Dirac distribution, and $T(E_z)$ is the probability of tunneling through the potential barrier. Here $T(E_z)$ is expressed as the ratio between the transmitted and incident probability currents.

If an external bias $V$ is applied to the barrier (see Fig. {numref}`fig-p1-ch09-16`), the net current flowing through it is the difference between the current from left to right and that from right to left. Thus, we obtain:

```{math}
:label: eq-p1-ch09-45
J_z = \frac{e}{4\pi^3 \hbar} \int dE_z\, d^2k_\perp\, [f(E) - f(E+eV)]\, T(E_z)
```

where $E_z$ represents the energy from the $k_z$ component of crystal momentum, i.e., $E_z=\hbar^2 k_z^2/(2m)$. Since the integrand is not a function of $k_\perp$ in a plane normal to $k_z$, we can integrate over $d^2k_\perp$ by writing

```{math}
:label: eq-p1-ch09-46
dk_x dk_y = d^2k_\perp = \frac{2m}{\hbar^2} dE_\perp
```

where $E_\perp=\hbar^2 k_\perp^2/(2m)$ and after some algebra, the tunneling current can be written as,

```{math}
:label: eq-p1-ch09-47
\begin{aligned}
J_z &= \frac{em}{2\pi^2 \hbar^3} \left[ eV \int_0^{E_F-eV} dE_z\, T(E_z) + \int_{E_F-eV}^{E_F} dE_z\, (E_F-E_z) T(E_z) \right] \quad \text{if } eV \le E_F \\
J_z &= \frac{em}{2\pi^2 \hbar^3} \int_0^{E_F} dE_z\, (E_F-E_z) T(E_z) \qquad\qquad\qquad\qquad\qquad\qquad\qquad \text{if } eV \ge E_F
\end{aligned}
```

(see Fig. {numref}`fig-p1-ch09-16` for the geometry of the model) which can be evaluated as long as the tunneling probability through the barrier is known. We now discuss how to find the tunneling probability.

An enhanced tunneling probability occurs for certain voltages as a consequence of the constructive interference between the incident and the reflected waves in the barrier region between regions 1 and 3. To produce an interference effect the wavevector $\vec{k}$ in the plane wave solution $e^{ikz}$ must have a real component so that an oscillating (rather than a decaying exponential) solution is possible. To accomplish this, it is necessary for a sufficiently high electric field to be applied (as in Fig. {numref}`fig-p1-ch09-16`(c)) so that a virtual bound state is formed. As can be seen in Fig. {numref}`fig-p1-ch09-17`a, the oscillations are most pronounced when the difference between the electronic mass at the barrier and at the electrodes is the largest. This interference phenomenon is frequently called resonant Fowler-Nordheim tunneling and has been observed in metal-oxide-semiconductor (MOS) heterostructures and in GaAs/Ga$_{1-x}$Al$_x$As/GaAs capacitors. Since the WKB method is semiclassical, it does not give rise to the resonant tunneling phenomenon, which is a quantum interference effect.

:::{figure} images/fig-p1-ch09-17.png
:name: fig-p1-ch09-17
:width: 90%
:align: center
Fig. 9.17: (a) Tunneling current through a rectangular barrier (like the one of Fig. 9.16a) calculated as a function of bias for different values of $m_1$, in the quantum well. (b) Comparison of an exact calculation of the tunneling probability through a potential barrier under an external bias with an approximate result obtained using the WKB method. The barrier parameters are the same as in (a), and the energy of an incident electron, of mass $0.2m_0$, is $0.05$ eV. (From the book of E.E. Mendez and K. von Klitzing, "Physics and Applications of Quantum Wells and Superlattices", NATO ASI Series, Vol. 170, p.159 (1987).)
:::

For the calculation of the resonant tunneling phenomenon, we must therefore use the quantum mechanical solution. In this case, it is convenient to use the transfer matrix method to find the tunneling probability. In region (\#1) of Fig. {numref}`fig-p1-ch09-16`, the potential $V(z)$ is constant and solutions to Eq. {eq}`eq-p1-ch09-41` have the form

```{math}
:label: eq-p1-ch09-48
\psi_e(z) = A \exp(ikz) + B \exp(-ikz)
```

with

```{math}
:label: eq-p1-ch09-49
\frac{\hbar^2 k^2}{2m} = E - V .
```

When $E-V>0$, then $k$ is real and the wave functions are plane waves. When $E-V<0$, then $k$ is imaginary and the wave functions are growing or decaying waves. The boundary conditions Eqs. {eq}`eq-p1-ch09-42` and {eq}`eq-p1-ch09-43` determine the coefficients $A$ and $B$ which can be described by a $(2\times 2)$ matrix $R$ such that

```{math}
:label: eq-p1-ch09-50
\begin{pmatrix}
A_1 \\ B_1
\end{pmatrix}
= R
\begin{pmatrix}
A_2 \\ B_2
\end{pmatrix}
```

where the subscripts on $A$ and $B$ refer to the region index and $R$ can be written as

```{math}
:label: eq-p1-ch09-51
R = \frac{1}{2k_1 m_2}
\begin{pmatrix}
(k_1 m_2 + k_2 m_1)\exp[i(k_2-k_1)z_1] & (k_1 m_2 - k_2 m_1)\exp[-i(k_2+k_1)z_1] \\
(k_1 m_2 - k_2 m_1)\exp[i(k_2+k_1)z_1] & (k_1 m_2 + k_2 m_1)\exp[-i(k_2-k_1)z_1]
\end{pmatrix}
```

and the terms in $R$ of Eq. {eq}`eq-p1-ch09-51` are obtained by matching boundary conditions as given in Eqs. {eq}`eq-p1-ch09-42` and {eq}`eq-p1-ch09-43`.

In general, if the potential profile consists of $n$ regions, characterized by the potential values $V_i$ and the masses $m_i$ ($i=1,2,...n$), separated by $n-1$ interfaces at positions $z_i$ ($i=1,2,...(n-1)$), then

```{math}
:label: eq-p1-ch09-52
\begin{pmatrix}
A_1 \\ B_1
\end{pmatrix}
= (R_1 R_2 \ldots R_{n-1})
\begin{pmatrix}
A_n \\ B_n
\end{pmatrix} .
```

The matrix elements of $R_i$ are

```{math}
:label: eq-p1-ch09-53
\begin{aligned}
(R_i)_{1,1} &= \left(\frac{1}{2} + \frac{k_{i+1}m_i}{2k_i m_{i+1}}\right) \exp[i(k_{i+1}-k_i)z_i] \\
(R_i)_{1,2} &= \left(\frac{1}{2} - \frac{k_{i+1}m_i}{2k_i m_{i+1}}\right) \exp[-i(k_{i+1}+k_i)z_i] \\
(R_i)_{2,1} &= \left(\frac{1}{2} - \frac{k_{i+1}m_i}{2k_i m_{i+1}}\right) \exp[i(k_{i+1}+k_i)z_i] \\
(R_i)_{2,2} &= \left(\frac{1}{2} + \frac{k_{i+1}m_i}{2k_i m_{i+1}}\right) \exp[-i(k_{i+1}-k_i)z_i]
\end{aligned}
```

where the $k_i$ are defined by Eq. {eq}`eq-p1-ch09-49`. If an electron is incident from the left (region \#1) only a transmitted wave will appear in the last region \#$n$, and therefore $B_n=0$. The transmission probability is then given by

```{math}
:label: eq-p1-ch09-54
T = \left(\frac{k_1 m_n}{k_n m_1}\right) \frac{|A_n|^2}{|A_1|^2} .
```

This is a general solution to the problem of transmission through multiple barriers. Under certain conditions, a particle incident on the left can appear on the right essentially without attenuation. This situation, called resonant tunneling, corresponds to a constructive interference between the two plane waves coexisting in the region between the barriers (quantum well).

The tunneling probability through a double rectangular barrier is illustrated in Fig. {numref}`fig-p1-ch09-18`. In this figure, the mass of the particle is taken to be $0.067m_0$, the height of the barriers is 0.3 eV, their widths are 50\AA\ and their separations are 60\AA. As observed in the figures, for certain energies below the barrier height, the particle can tunnel without attenuation. These energies correspond precisely to the eigenvalues of the quantum well; this is understandable, since the solutions of Schr\"odinger's equation for an isolated well are standing waves. When the widths of the two barriers are different (see Fig. {numref}`fig-p1-ch09-18`b), the tunneling probability does not reach unity, although the tunneling probability shows maxima for incident energies corresponding to the bound and virtual states.

:::{figure} images/fig-p1-ch09-18.png
:name: fig-p1-ch09-18
:width: 90%
:align: center
Fig. 9.18: (a) Probability of tunneling through a double rectangular barrier as a function of energy. The carrier mass is taken to be $0.1m_0$ in the barrier and $0.067m_0$ outside, and the width of the quantum well is 60\AA. (b) Tunneling probability through a double-barrier structure, subject to an electric field of $1\times10^5$ V/cm. The width of the left barrier is 50\AA, while that of the right barrier is varied between 50\AA\ and 100\AA. The peak at $\sim 0.16$ eV corresponds to resonant tunneling through the first excited state ($E_1$) of the quantum well. The optimum transmission is obtained when the width of the right barrier is $\sim 75$\AA.
:::
