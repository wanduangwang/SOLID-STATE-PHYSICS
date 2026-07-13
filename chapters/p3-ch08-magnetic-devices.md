---
title: "8 Magnetic Devices"
abstract: "This chapter surveys a number of magnetic and magneto-optic devices. After a brief introduction and a discussion of permanent magnets, we treat transformers and magnetic amplifiers, a range of data-storage technologies (magnetic cores, tape, bubbles, and magneto-optical media), the Faraday effect and its microwave/optical non-reciprocal applications (gyrators, circulators, isolators), and finally magnetic multilayer structures, including oscillating interlayer coupling and giant magnetoresistance."
---

# 8 Magnetic Devices

References

- E.W. Lee, *Magnetism: An Introductory Survey*, Dover, New York, 1970.
- S. Chikazumi, *Physics of Magnetism*, Wiley, New York 1966.
- R.S. Tebble and D.J. Craik, *Magnetic Materials*, Wiley–Interscience, New York 1969.
- R.J. Gambino, "Optical Storage Disk Technology", *Mat. Res. Soc. Bull.* **15**, 20 (1990).
- J.A.M. Greidanus and W. Bas Zeper, "Magneto-optical Storage Materials", *Mat. Res. Soc. Bull.* **15**, 31 (1990).

## 8.1 Introduction

In this chapter we briefly survey a number of magnetic devices. Many people are aware of the huge magnitude of the semiconductor industry. Far fewer people are aware of the fact that the magnetic device business is about 2/3 of the size of the semiconductor business. Therefore a brief review of some common magnetic and magneto-optic devices is in order.

## 8.2 Permanent Magnets

Permanent magnetic fields having strengths of the order of 10 kilogauss can be obtained using the remanent magnetization of so-called "hard" magnetic materials. These are characterized by (1) large permeabilities and (2) high coercive fields $H_c$. Important to the development of radar as components in magnetron microwave amplifier tubes, the most widespread modern applications are small motors and loudspeakers. Alloys of aluminum, nickel and cobalt (Alnico) and other more recent cobalt alloys are in common use. In the last few years a new NdFeB ($Nd_2Fe_{14}B$ alloys) compound has been developed with a very high $BH$ product.

## 8.3 Transformers

Reference:

- *Magnetic Circuits and Transformers*, M.I.T. Press, Cambridge, 1943.

Transformers consist of two or more coils linked by a magnetic flux path in which the driving (or primary) coil induces currents in the driven (or secondary) coils. The important features of the material used to couple the coils magnetically are (1) large permeabilities for efficient coupling through minimization of "leakage" flux, (2) very small coercive fields $H_c$, and (3) linear magnetization curves having little hysteresis. Hysteresis causes both distortion and power loss. Large permeabilities and small $H_c$ define "soft" magnetic materials. Pure iron is a good example of a soft magnetic material, especially when used in multi-layer or laminated construction in which the cross-section normal to the flux direction is composed of insulated stacks of thin plates. This construction prevents large induced circulating currents in the iron ("eddy" currents) and their attendant losses due to Joule heating.

### 8.3.1 Magnetic Amplifiers

Reference:

- H.F. Storm, *Magnetic Amplifiers*, John Wiley, NY, 1955.

A transformer with a non-linear $B$–$H$ curve may be used as a signal multiplier or magnetic amplifier if an additional coil, the control winding, is used to change the differential permeability at which the device is operating. In the diagram of {numref}`fig-p3-ch08-1`, the local slope of the $B$–$H$ curve is a function of the control current, $i_c$. The transfer characteristics of the device will have the input and output currents related by

```{math}
:label: eq-p3-ch08-1
i_{\text{out}} \propto \mu \left(\frac{dB}{dH}\right) i_{\text{in}}
```

and if

```{math}
:label: eq-p3-ch08-2
\frac{dB}{dH} = f(i_c) \approx f_0 i_c
```

so that the function $f(i_c)$ is linear in $i_c$, then

```{math}
:label: eq-p3-ch08-3
i_{\text{out}} \approx (f_0 i_{\text{in}}) i_c
```

where $i_{\text{out}}$ is proportional to $i_c$ and the product $(f_0 i_{\text{in}})$ may represent a large gain factor.

:::{figure} images/fig-p3-ch08-1.png
:name: fig-p3-ch08-1
:width: 3.2in
:align: center

Slopes of the $B$–$H$ curve that is exploited in designing a magnetic amplifier.
:::

## 8.4 Data Storage

### 8.4.1 Magnetic Core

Reference:

- T.C. Chen and A. Papoulis, "Domain Theory in Core Switching", *Proc. IRE*, 1958, Vol 46, pp. 839–849.

Remanent magnetism may be used to provide a fast, reliable electrical recording technique. For digital storage materials, (1) large permeabilities, and (2) intermediate but well-controlled coercive fields are desirable. In particular, toroidal-shaped elements called cores in which the magnetization is circumferentially directed became the main stay of computer mass memory (although continuing advances in semiconductor technology have made this form of memory largely obsolete). A typical $B$–$H$ curve for a core is given in {numref}`fig-p3-ch08-2`. In practice, the cores are threaded in a matrix of wires, as shown below. Data is entered ("written") into the array by applying a current $i$ to each of the horizontal and vertical wires called address lines. The magnitude of $i$ is such that its $H$-field is insufficient to cause a change in the magnetization of a core, but the coincidence of currents from two wires at a single core is sufficient to magnetize it. With the current returned to zero, the magnetization is at position (1) on the $B$–$H$ curve. To reverse the magnetization ("erase" the core), a coincidence of currents $-i$ are applied to the core, leaving the remanent magnetization at position (2) on the curve in {numref}`fig-p3-ch08-2`.

To determine ("read") the state of the core, a pair of currents $i$ are addressed to the core; if the previous state of the core was (2), there will be a sudden change in the core magnetization, which will induce a current in the third wire threading the cores (see {numref}`fig-p3-ch08-3`), the output or "sense" wire. This current is then amplified to usable levels. If the core had been in state (1), there would be no magnetization change, and hence no "sense" current. Note that a "read" operation destroys the original state of the core, so that it must be "rewritten" if it is needed in subsequent operations.

:::{figure} images/fig-p3-ch08-2.png
:name: fig-p3-ch08-2
:width: 3.2in
:align: center

$B$–$H$ curve with a nearly rectangular hysteresis loop.
:::

:::{figure} images/fig-p3-ch08-3.png
:name: fig-p3-ch08-3
:width: 3.5in
:align: center

Schematic diagram of a magnetic core memory, showing the address wires on the $x$ and $y$ axes, and the "sense" wire threading the cores.
:::

### 8.4.2 Data Storage: Magnetic Tape

Reference:

- H.G.M. Spratt, *Magnetic Tape Recording*, Temple Press Books, London, 1964.

Magnetic tape is a continuous strip of flexible dielectric (such as mylar plastic) to which is bonded a thin layer of magnetic particles dispersed in an insulating base. The particles have

1. large permeability,
2. intermediate coercive field values, and
3. large anisotropy.

The anisotropy of the particles determines the direction of their remanent magnetization. That is, for large applied fields ($H_0 \gg H_a$) normal to the tape, the normal component of the remanent magnetization is

```{math}
:label: eq-p3-ch08-4
B_r = \hat{\mu}\,\hat{\mathbf{H}}_0 \cdot \vec{H}_a = \pm \hat{\mu}\,|H_a|\cos\theta
```

where $\hat{\mu}$ is the particle permeability, $\vec{H}_a$ its anisotropy field, and $\theta$ the angle between the applied field $\vec{H}_0$ and the anisotropy field $\vec{H}_a$, as in {numref}`fig-p3-ch08-4`. This means that only the sign of the particle magnetization may be changed. The external magnetization of the tape will be an average over all possible $\theta$, with the additional complication of variation in the shapes of the particles causing variations in their external fields. A typical $B_r$–$H$ curve for a magnetic tape is shown in {numref}`fig-p3-ch08-5`, where $B_r$ is the remanent induction of the tape after the removal of the field $H$. If the field $H_0$ applied by an electromagnet (the recording head) changes with time, and the tape is simultaneously translated along its length $\ell$, then

```{math}
:label: eq-p3-ch08-5
B_r(\ell) = f[H_0(t)]
```

and the recorded $B_r(\ell)$ can be subsequently detected by moving it under another coil (the playback head). For faithful reproduction we would like

```{math}
:label: eq-p3-ch08-6
f[H_0(t)] = f_0 H_0(t)
```

which, from the shape of the $B_r$–$H$ curve, will clearly not be the case. A clever trick is used in nearly all modern audio recording to overcome this problem. The signal $H_0(t)$ is added to a high frequency ($\sim 100\,\text{kHz}$) bias field $H_B(t)$ which has sufficient magnitude to span the non-linear region in the $B_r$–$H$ curve as shown in {numref}`fig-p3-ch08-6`. The remanent induction $\langle B_r(\ell)\rangle$ averaged over several cycles of the bias field will then be approximately

```{math}
:label: eq-p3-ch08-7
\langle B_r(\ell)\rangle \approx f_0 H_0(t)
```

where $f_0$ is the local slope of the effective recording characteristic.

:::{figure} images/fig-p3-ch08-4.png
:name: fig-p3-ch08-4
:width: 3.5in
:align: center

$\theta$, the angle between $\vec{H}_0$ and $\vec{H}_a$.
:::

:::{figure} images/fig-p3-ch08-5.png
:name: fig-p3-ch08-5
:width: 3.5in
:align: center

Typical $B_r$–$H$ curve for a magnetic tape.
:::

:::{figure} images/fig-p3-ch08-6.png
:name: fig-p3-ch08-6
:width: 3.5in
:align: center

Use of bias field to improve recording fidelity for magnetic storage tape.
:::

### 8.4.3 Magnetic Bubbles

References:

- T.H. O'Dell, *Magnetic Bubbles*, John Wiley, NY, 1974.
- H. Chang, Ed., *Magnetic Bubble Technology: Integrated-Circuit Magnetics for Digital Storage and Processing*, I.E.E.E. Press, 1976.

One interesting development in magnetic memory devices is that of magnetic bubble technology. Small ($\sim 1$ micron diameter) circular domains in thin magnetic films can be generated, so that the magnetization of these domains is normal to the plane of the film and opposite to that of the surrounding material as shown in {numref}`fig-p3-ch08-7`. The film material, usually one of the many insulating magnetic garnets, is arranged to have its easy magnetic axis normal to the plane. Magnetic materials used for magnetic bubble memories should have

1. high uniaxial anisotropy energy in order to maintain the simple domain structure shown in {numref}`fig-p3-ch08-7`;
2. low saturation fields, so that domains may be created with practical applied fields;
3. low value for $H_c$, so that the domains may be propagated with reasonably small field gradients, and
4. high domain wall mobility, allowing high propagation velocities and hence high data rates.

Bubbles may be created by sudden changes in the bias field of uniformly magnetized material. Hydrodynamic instabilities prevent the film magnetization from changing instantaneously, and domains form analogously to the formation of fluid droplets due to surface-tension. Once formed, a bubble domain may be stably located by placing it in an in-plane field gradient, induced, perhaps, by the presence of an overlying "soft" magnetic structure of high permeability, such as rectangular layers of permalloy (80% nickel/20% iron alloy) (see {numref}`fig-p3-ch08-9`a). The high permeability layer concentrates the flux of the in-plane $B$-field (see {numref}`fig-p3-ch08-9`b), yielding a magnetic well at one end of the bar which can stabilize a bubble, as shown in {numref}`fig-p3-ch08-9`c. If the field well can be moved, the bubble will follow. A simple scheme for accomplishing this is the so-called TI bar structure shown in {numref}`fig-p3-ch08-8`. An in-plane magnetic drive induction $B_D$ is applied which rotates in the plane at a constant angular frequency. The demagnetization effect of the permalloy bars is largest when they are parallel to $B_D$, so that the field well minimum will always lie at the ends of the bar sections which have the longest cross sections in the direction of the applied field. As the direction of $B_D$ rotates, the field minima will propagate down the array carrying bubbles with them. {numref}`fig-p3-ch08-8` shows four intermediate steps in this process, and demonstrates how bubbles are "copied" from a large source domain. The "copy" process can be inhibited by an in-plane field, applied by a current loop at the "neck" of the source domain. In this way, a serial pattern of bubbles and vacancies can be propagated down the array, forming a digital shift register. The bubbles may be detected by a sense coil in a manner similar to that of magnetic tape playback.

The speed of propagation is limited by the domain wall mobility, $\mu_w$, which is related to $v_b$, the bubble velocity, by the magnetic drive induction $B_D$ by

```{math}
:label: eq-p3-ch08-8
v_b = \mu_w B_D .
```

The properties of a number of possible bubble domain materials are listed in {numref}`tab-p3-ch08-1`. Given are the film thickness $h$ in microns, the saturation magnetization $\mu_0 M$ in tesla ($1$ tesla $= 10^4$ gauss), the wall mobility $\mu_w$, and a time constant $\tau^*$ which characterizes the effective inertial response of bubbles in these materials.

```{math}
:label: eq-p3-ch08-9
\tau^* = \frac{h}{\mu_w \mu_0 M}
```

:::{figure} images/fig-p3-ch08-7.png
:name: fig-p3-ch08-7
:width: 3.5in
:align: center

Geometry of a magnetic bubble film.
:::

:::{figure} images/fig-p3-ch08-8.png
:name: fig-p3-ch08-8
:width: 3.0in
:align: center

Schematic of TI bar structure used to propagate magnetic bubbles.
:::

:::{figure} images/fig-p3-ch08-9.png
:name: fig-p3-ch08-9
:width: 3.0in
:align: center

Schematic diagrams of (a) bubble (b) flux lines (c) forces for magnetic bubble recording media.
:::

:::{table} tab-p3-ch08-1
:name: tab-p3-ch08-1
:align: center

| Material | $h$ ($\mu$m) | $\mu_0 M$ (T) | $\mu_w$ (m/s per T) | $\tau^*$ (ns) |
|---|---:|---:|---:|---:|
| $Gd_{2.3}Tb_{0.7}Fe_5O_{12}$ | 12.5 | 0.0142 | $1.08 \times 10^4$ | 82 |
| $Y_{2.4}Eu_{0.6}Ga_{1.1}Fe_{3.9}O_{12}$ | 10.8 | 0.0210 | $\approx 10^4$ | $\approx 50$ |
| $DyFeO_3$ | 42 | 0.0128 | $3.3 \times 10^4$ | 100 |
| $Sm_{0.55}Tb_{0.45}FeO_3$ | 50.0 | 0.0126 | $9.0 \times 10^4$ | 44 |
| $EuEr_2Ga_{0.7}Fe_{4.3}O_{12}$ | 5.7 | 0.0250 | $0.96 \times 10^4$ | 24 |
:::

**Table 8.1:** Properties of bubble film materials.

### 8.4.4 Magneto-optical Storage

Reference:

- Iwamura et al., *Electronic Letters* **15**, 830 (1979).

Magneto-optical storage of digital information exploits the optical properties of magnetic materials, in particular, their magneto-optical Kerr rotation and Faraday rotation. The media used is a thin magnetic film with the following characteristics:

1. Large uniaxial anisotropy to insure that the magnetization is directed normal to the plane of the film;
2. A high room temperature coercive field to insure stable magnetic domains;
3. A rectangular hysteresis loop; and
4. Small grain (crystalline) size for regularly-shaped magnetic domains.

Data is stored on the magnetic film as circular domains approximately $1\,\mu\text{m}$ in diameter. The magnetization of a domain is either up or down with respect to the film, indicating a 0 or 1 bit. A bit is read (see {numref}`fig-p3-ch08-10`) by examining the polarization of laser light reflected from such a domain. Polarized light will suffer a positive or negative Kerr rotation upon reflection, depending on whether the magnetization of the domain is up or down.

To write a bit of information, a magnetic field (see {numref}`fig-p3-ch08-11`) is applied to the film in the desired direction. Focused laser light then raises the temperature of the domain to be written, causing the coercive field, $H_c(T)$, to drop to a value at which the applied field is strong enough to switch the magnetization of the domain. Note that the coercive field of the material at room temperature $H_c(T_{RT})$ is large enough, and the hysteresis loop rectangular enough so that all other domains are unaffected by the applied magnetic field.

Using a similar principle, an optical circulator can be built (see {numref}`fig-p3-ch08-12`). Shown in this figure is an optical circulator used in fiber-optic communication links which has the virtue of being unaffected by the polarization of the input light. Unpolarized light enters port 1 and is split by a polarization beam splitter into two orthogonally polarized beams. Referring to {numref}`fig-p3-ch08-12`, rotator 1 is a Faraday rotator which rotates polarizations by $+45^\circ$. Rotator 2 is birefringent rotator which also rotates the polarization by $+45^\circ$ giving a total rotation of $90^\circ$ to the polarized beams. This allows unpolarized light to exit at port 2 after being recombined at the second polarization beam splitter.

Unpolarized light entering port 2 will also be split into two orthogonal polarizations. But, the birefringent rotator (2) will rotate the polarizations by $-45^\circ$. This gives a net rotation of $0^\circ$ to the two beams allowing light to exit at port 3 rather than port 1. In this way, signals can be sent and received simultaneously along the same optical fiber.

:::{figure} images/fig-p3-ch08-10.png
:name: fig-p3-ch08-10
:width: 3.0in
:align: center

Principle of magneto-optical read-out. The direction of the magnetization is detected by the rotation of a plane-polarized light wave upon reflection.
:::

:::{figure} images/fig-p3-ch08-11.png
:name: fig-p3-ch08-11
:width: 4.0in
:align: center

Principle of the thermo-magnetic writing process. (a) A laser generates a temperature profile $T(x)$ in the perpendicularly magnetized layer $M$; consequently, the coercive field $H_c$ decreases with temperature $T$ as in (b). When a magnetic field of suitable magnitude is now applied, the magnetization direction will be reversed for this domain, while all other domains have a sufficiently high coercive field to maintain their direction of magnetization.
:::

:::{figure} images/fig-p3-ch08-12.png
:name: fig-p3-ch08-12
:width: 6.0in
:align: center

Polarization-independent optical circulator. Device #1 denotes a $45^\circ$ YIG (Faraday) rotator, while device #2 denotes a $45^\circ$ quartz (birefringent) rotator. Devices #3 and #4 denote polarization beam-splitting cubes and devices #5 and #6 denote right-angle prisms. The circulation scheme is Port 1 $\to$ Port 2; Port 2 $\to$ Port 3; Port 3 $\to$ Port 4; Port 4 $\to$ Port 1.
:::

## 8.5 Faraday Effect

Reference:

- R.E. Collins, *Foundations for Microwave Engineering*, McGraw-Hill, NY (1966).

The Faraday effect results from the presence of two different propagation constants $\beta_+$ and $\beta_-$ for right- and left-circularly polarized radiation, respectively, in response to a magnetic field applied along the axis of propagation of the electromagnetic wave. This is equivalent to a rotation of the linear polarization about the $z$-axis (or propagation axis) with $\theta_\ell$, the angular rotation per unit length of propagation given by

```{math}
:label: eq-p3-ch08-10
\theta_\ell = \frac{\beta_- - \beta_+}{2}
```

the evolution of the rotation angle is shown in {numref}`fig-p3-ch08-13` as the electromagnetic wave propagates through the medium. Note that the Faraday effect is non-reciprocal in the sense that a wave passing through a thickness of material $\ell$, then reflected, and returning through the thickness $\ell$, would suffer successive rotations of the plane of polarization

```{math}
:label: eq-p3-ch08-11
\theta = \theta_\ell (2\ell) = (\beta_- - \beta_+)\ell
```

rather than being returned to its initial polarization state, $\theta = 0$. A number of different devices utilize this effect, including certain types of gyrators, circulators and isolators.

A gyrator (in microwave technology) is defined as a two-port device that has a relative difference in phase shift of $180^\circ$ for transmission from port 1 to port 2 as compared with the phase shift from port 2 to port 1 (see {numref}`fig-p3-ch08-14`). Going from $1 \to 2$ the polarization rotations of the $90^\circ$ twist and the $90^\circ$ rotation of the ferrite rod add, giving a total phase shift of $180^\circ$. However, going from $2 \to 1$, they cancel, for a net shift of $0^\circ$ (see {numref}`fig-p3-ch08-14`). The chief use of gyrators is as components in the construction of microwave circulators.

A circulator is a multiport device having the property that a wave incident in port 1 is coupled into port 2 only, port 2 is coupled only into port 3, etc. A four-port circulator is shown in {numref}`fig-p3-ch08-15`b, fabricated from a gyrator and two so-called "magic T" junctions (see {numref}`fig-p3-ch08-15`a). A magic-T microwave junction utilizes the $E$-field orthogonality of the $TE_{10}$ waveguide modes of different orientations, together with proper wave impedance matching elements, to effect the following coupling situation (see {eq}`eq-p3-ch08-12`):

```{math}
:label: eq-p3-ch08-12
\begin{pmatrix}
A_1^o \\ A_2^o \\ A_3^o \\ A_4^o
\end{pmatrix}
= \frac{\sqrt{2}}{2}
\begin{pmatrix}
0 & 1 & 1 & 0 \\
1 & 0 & 0 & 1 \\
1 & 0 & 0 & -1 \\
0 & 1 & -1 & 0
\end{pmatrix}
\begin{pmatrix}
A_1^i \\ A_2^i \\ A_3^i \\ A_4^i
\end{pmatrix}
```

The $A_n^o$ are the outgoing wave amplitudes at ports $n = 1, 2, 3, 4$ and the $A_n^i$ are the corresponding incoming amplitudes. The matrix denotes which linear combination of input amplitudes contribute to each output amplitude. For example

```{math}
:label: eq-p3-ch08-13
A_1^o = \frac{1}{\sqrt{2}}\left(A_2^i + A_3^i\right)
```

or ports 2 and 3 couple to port 1 in phase, and

```{math}
:label: eq-p3-ch08-14
A_4^o = \frac{1}{\sqrt{2}}\left(A_2^i - A_3^i\right)
```

ports 2 and 3 couple to port 4 out of phase.

A wave entering (1) is split into two in-phase components which add constructively and are coupled out through port (2). An input at (2) is split likewise, but one arm is shifted $180^\circ$ in this direction by the gyrator so that the sum interferes destructively for port (1) but constructively for port (3). Similarly, port (3) is coupled to (4), and (4) to (1). (For details of the properties of "magic-T's," see Collins Ref., p. 282.)

Non-reciprocal rotations of $45^\circ$ can be used to build isolators, which have low loss in one direction, and very high loss in the other. Such devices are used to protect microwave equipment from damage due to power reflected from mis-matched antennas.

We illustrate here also a device application at optical frequencies. High-power pulse laser systems (as is used for laser fusion and isotope separation) are currently built in separate stages, starting with an oscillator and followed by subsequent amplifier stages. This is done so that each laser amplifier stage can be optimized for the power levels it must handle. An amplifier stimulated by extraneous radiation can be driven to catastrophic oscillation and destruction. Hence it is critically important that an amplifier be isolated from light generated or reflected by subsequent stages.

This can be done as shown in {numref}`fig-p3-ch08-16`. The laser beam is plane-polarized at $45^\circ$ to the vertical, and passes unattenuated through a polarization analyzer which is oriented at the same angle. The beam then goes through a $45^\circ$ Faraday rotator, is brought to vertical polarization, and excites the next stage. Any reflected or regenerated light passes through the rotator again and is shifted by a further $45^\circ$. The resulting polarization is orthogonal to the analyzer, and is therefore blocked.

:::{figure} images/fig-p3-ch08-13.png
:name: fig-p3-ch08-13
:width: 3.5in
:align: center

Angles defining rotation for the Faraday effect.
:::

:::{figure} images/fig-p3-ch08-14.png
:name: fig-p3-ch08-14
:width: 4.0in
:align: center

Schematic of a microwave gyrator.
:::

:::{figure} images/fig-p3-ch08-15.png
:name: fig-p3-ch08-15
:width: 6.0in
:align: center

(a) A "magic T" microwave device (see text). (b) A four-port circulator consisting of a gyrator and two "magic T"s.
:::

:::{figure} images/fig-p3-ch08-16.png
:name: fig-p3-ch08-16
:width: 5.5in
:align: center

Schematic of an optical isolator.
:::

## 8.6 Magnetic Multilayer Structures

### 8.6.1 Introduction

Magnetic multilayers are usually made of alternating layers of magnetic and non-magnetic species, with the non-magnetic substance referred to as the spacer. The layer thickness for both spacer and magnetic species roughly ranges from a few angstroms to a few hundred angstroms. Due to the small dimension in the $z$-direction we may regard the research on magnetic multilayers as a subset of studies on thin films.

The physical phenomena to be studied include magneto-optics, magnetoresistance, magnetostriction, magnetostatics, magnetic exchange coupling, microwave properties and anisotropy at magnetic surfaces and interfaces. Not all these properties will show up in a single magnetic multilayer structure, which leads to the classifications of magnetic multilayers according to their different characteristics. One of these distinguishing characteristics is the electrical conductivity, i.e. magnetic multilayers can be divided into metallic magnetic multilayers and insulating magnetic multilayers. This choice of division is not arbitrary because magnetism is an electronically driven phenomenon, so that it is closely related to electrical conductivity.

### 8.6.2 Metallic Magnetic Multilayers

In this category, the most commonly used ferromagnets are Fe, Co, Ni, Ni-Fe, Fe-Co, Dy, Er, Gd, Ho and Tm. The most commonly used spacers are Cu, Ag, Au, Mg, Sn, V, Nb, Ta, Cr, Mo, W, Mn, Pd, Y and Lu. Notice that we have used the word ferromagnets to describe magnetic components of metallic magnetic multilayers. That is because most conducting magnetic materials are ferromagnets and most insulating magnetic materials are antiferromagnets.

Metallic magnetic multilayers exhibit two interesting properties: oscillating interlayer coupling and giant magnetoresistance[^gmr]. Research demonstrating those two effects has focused on Fe, Co, and Ni separated by Cr, Ru, Re, Cu and Ag.

**Interlayer Coupling**

Adjacent ferromagnetic layers, which are separated by a non-magnetic metal spacer, have their magnetization vectors either parallel (ferromagnetic coupling) or antiparallel (antiferromagnetic coupling) to each other (see {numref}`fig-p3-ch08-17`). Shown in {numref}`fig-p3-ch08-17` is a magnetic configuration whereby the magnetization vector lies in the plane of the layers, and the oscillation in the interlayer coupling is a function of spacer thickness. Typical oscillation periods reported in the literature are: $P_{Cu} = 10$ Å, $P_{Ru} = 11$ Å, and $P_{Cr} = 18\text{--}20$ Å[^pcr]. Furthermore, the experimental results also show that for sharp magnetic/spacer interfaces (MBE grown superlattices) the oscillation period is about two atomic layers, approximately three angstroms[^3al]. For all spacer materials, the oscillation (i.e., interlayer coupling) ceases to exist when the thickness of the spacer exceeds 50 Å[^3al][^4]. Although the coupling mechanism is not completely understood yet, theoretical calculations based on different models such as the RKKY mechanism, Fermi surface nesting, and quantum-size effect give good fits to the experimental data[^5][^6].

**Giant Magnetoresistance (GMR)**

The giant magnetoresistance effect shows up in samples in which the magnetic alignment is antiparallel. As the external magnetic field is gradually increased from zero gauss, the magnetic moments of different layers tend to line up with the field. At the same time the electrical resistivity decreases (see {numref}`fig-p3-ch08-18`). This negative magnetoresistance can be as large as 65% in samples that exhibit an initial resistance within a range useful for practical applications. The resistivity of metallic magnetic multilayers can be calculated by solving the Boltzmann transport equation with spin-dependent scattering at the interfaces. Calculations show in general the scattering is weaker and less effective when the arrangement between successive ferromagnetic layers is parallel[^7].

:::{figure} images/fig-p3-ch08-17.png
:name: fig-p3-ch08-17
:width: 3.5in
:align: center

Schematic representation of a magnetic metallic multilayer. (a) Successive magnetic layers are arranged with their magnetizations antiparallel. In this arrangement the electrical resistance of the film is high. (b) Parallel magnetization configuration results from applying a magnetic field to the magnetic arrangement in (a). The new arrangement has a lower electrical resistance. The film thus exhibits a negative magnetoresistance.
:::

:::{figure} images/fig-p3-ch08-18.png
:name: fig-p3-ch08-18
:width: 3.5in
:align: center

Magnetoresistance of a $GaAs[Fe(30\,\text{\AA})/Cr(9\,\text{\AA})]_{60}$ multilayer at 4.2 K. The current voltage drop and magnetic field are all in the plane of the layers.
:::

### 8.6.3 Insulating Magnetic Multilayers

As the name implies, the fundamental difference between metallic magnetic multilayers and insulating magnetic multilayers is their electrical resistivities. Different electrical conductivities lead to different kinds of magnetism. The magnetism of conducting magnetic materials can be described by the itinerant electron theory, whereas the magnetism of non-conducting magnetic materials can be better described by the local moment theory, i.e., mean-field theory. Therefore, it is intuitively simpler to consider interlayer couplings and general magnetic properties of insulating magnetic multilayers. Incidentally, magnets with localized moments are also called Heisenberg magnets.

Insulating magnetic multilayer structures that have been considered so far are $FeF_2/CoF_2$, $MnTe/ZnTe$, $Fe_3O_4/NiO$, $CoO/NiO$ and $EuTe/PbTe$. $FeF_2/CoF_2$ and $CoO/NiO$ belong to the same family of magnetic multilayers that consist of two antiferromagnetic materials. Studies show that, while the superlattices retain the antiferromagnetic spin order of the constituents, the magnetic behavior near the phase transition reflects the influence of one material on the other[^8][^9]. Specifically, measurements of the spatially modulated order parameter in a $72$ Å period sample $[NiO(43\,\text{\AA})/CoO(29\,\text{\AA})]$ suggest that the Ni and Co moments order at separate temperatures shifted from the $T_N$'s for bulk CoO and NiO (291 and 520 K respectively). In contrast, magnetic order develops simultaneously within the CoO and NiO layers, for two superlattices with 36 Å periods. The measured transition temperatures fall between the Neel temperatures for bulk CoO and NiO depending on the relative CoO and NiO layer thicknesses.

There is an ongoing study on the magnetic properties of $EuTe/PbTe$ at Prof. M.S. Dresselhaus group at M.I.T. $EuTe$ is an antiferromagnetic insulator and $PbTe$ is a nonmagnetic semiconductor. The lack of free carriers in the spacer, $PbTe$, effectively rules out the possibility for successive $EuTe$ layers interacting through $PbTe$ by a RKKY-like mechanism. Thus $EuTe/PbTe$ is truly a Heisenberg multilayer structure of the simplest kind. The magnetization results on $EuTe/PbTe$ superlattices (SL) show that $T_c$ has remained essentially the same as that of the bulk even when the thickness of $EuTe$ is reduced to 3 atomic monolayers. $EuTe$ is a type II antiferromagnet which has ferromagnetically ordered (111) planes and adjacent (111) planes are antiferromagnetically aligned (see {numref}`fig-p3-ch08-19`). Thus, intuitively one would expect that a multilayer structure made of repeated periods with three or five (111) planes in one period would show a ferrimagnetic phase transition, whereas a multilayer structure with four (111) planes in one period would show an antiferromagnetic phase transition. This difference is observed in short-period $EuTe/PbTe$ SLs (see {numref}`fig-p3-ch08-20`).

:::{figure} images/fig-p3-ch08-19.png
:name: fig-p3-ch08-19
:width: 4.5in
:align: center

The $EuTe$ structure showing both the chemical unit cell and the magnetic unit cell.
:::

:::{figure} images/fig-p3-ch08-20.png
:name: fig-p3-ch08-20
:width: 4.5in
:align: center

Magnetization curves for various $EuTe/PbTe$ superlattices.
:::

### 8.6.4 References

[^gmr]: For an introductory overview on metallic magnetic multilayers see L.M. Falicov, "Metallic Magnetic Superlattices", *PHYSICS TODAY* 1992, Vol 45, Issue 10, pp 46-51.
[^pcr]: S.S.P. Parkin, *Phys. Rev. Lett.* **67**, 3598 (1991).
[^3al]: J. Unguris, et al., *Phys. Rev. Lett.* **67**, 140 (1991).
[^4]: T. Giebultowicz et al., private communication.
[^5]: Y. Wang et al., *Phys. Rev. Lett.* **65**, 2732 (1992).
[^6]: M.C. Munoz et al., *Phys. Rev. Lett.* **72**, 2482 (1994).
[^7]: R.E. Camley et al., *Phys. Rev. Lett.* **63**, 664 (1989).
[^8]: C.A. Ramos et al., *Phys. Rev. Lett.* **65**, 2913 (1990).
[^9]: J.A. Borchers et al., *Phys. Rev. Lett.* **70**, 1878 (1993).
