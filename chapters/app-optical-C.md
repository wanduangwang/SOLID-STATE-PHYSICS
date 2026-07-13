---
title: "C Organic Materials for Solid State Devices"
abstract: >
  Guest lecture by Prof. Vladimir Bulovic on organic materials for solid-state devices.
  It surveys organic light-emitting devices and their fabrication, organic thin films and
  crystals, charge transport (space-charge-limited, band-like, trap-limited, polaronic),
  interfaces and electrodes, excitons and radiative processes (Jablonski diagram,
  Born-Oppenheimer approximation, fluorescence/phosphorescence), and donor-acceptor
  systems used in photodetectors, solar cells, and lasers.
---

# C Organic Materials for Solid State Devices

*Guest lecture by Prof. Vladimir Bulovic (bulovic@mit.edu).* This appendix is a brief
primer on organic materials and devices, organized around four themes: **A.** organic
materials, **B.** transport, **C.** excitons, and **D.** devices.

## C.1 Organic Light-Emitting Devices

:::{figure} images/fig-p2-appC-1.png
:name: fig-p2-appC-1
:width: 80%
:align: center

Organic Materials and Devices: A Very Brief Primer (Prof. Vladimir Bulovic).
:::

Organic materials fall into **two general classes**: (i) **polymers** such as PPV, and
(ii) **molecular (small-molecule) materials** such as Alq$_3$.

:::{figure} images/fig-p2-appC-2.png
:name: fig-p2-appC-2
:width: 80%
:align: center

Organic Materials — two general classes (PPV polymers and Alq$_3$ molecular materials).
:::

They are attractive because of:

- Integrability with inorganic semiconductors.
- Low cost (fabric dyes, biologically derived materials).
- Large-area bulk processing possible.
- Ability to tailor molecules for specific electronic or optical properties.
- Unusual properties not easily attainable with conventional materials.

But problems exist: stability, patterning, thickness control of polymers, and low carrier
mobility.

Device preparation is typically done by thermal evaporation in a vacuum chamber. Glass
substrates are precoated with ITO (≈ 94% transparent, ≈ 15 Ω/square), precleaned
(Tergitol, TCE, acetone, 2-propanol), and growth proceeds at ≈ $5\times10^{-7}$ Torr,
room temperature, with layer thicknesses from 20 to 2000 Å.

:::{figure} images/fig-p2-appC-3.png
:name: fig-p2-appC-3
:width: 80%
:align: center

Vacuum chamber and device preparation/growth of organic thin films.
:::

Transparent OLEDs (TOLEDs) use a thin (50–100 Å) Mg–Ag semitransparent cathode so that
light is emitted through the glass/ITO side; the active stack (ITO / HTL / ETL, ≈ 500 Å
each) can exceed 70% transparency.

:::{figure} images/fig-p2-appC-4.png
:name: fig-p2-appC-4
:width: 80%
:align: center

Transparent OLEDs (Parthasarathy et al., Appl. Phys. Lett. 72, 2138 (1998); Bulovic et al., Nature 380, 29 (1996)).
:::

:::{figure} images/fig-p2-appC-5.png
:name: fig-p2-appC-5
:width: 80%
:align: center

TOLED applications (UDC, Inc.).
:::

Stacked organic LEDs exploit microcavity effects to tune color. The device layers (glass /
ITO / $\alpha$-NPD / Alq$_3$ / Mg:Ag) support surface emission, waveguide modes, and
surface plasmons, and can produce red–green–blue (and white) emission from a stacked
structure.

:::{figure} images/fig-p2-appC-6.png
:name: fig-p2-appC-6
:width: 80%
:align: center

Stacked organic LEDs and microcavity effects (Shen et al., Science 276, 2009 (1997); Bulovic et al., Phys. Rev. B 58, 3730 (1998)).
:::

The 2000 Nobel Prize in Chemistry was awarded to Alan J. Heeger, Alan G. MacDiarmid, and
Hideki Shirakawa "for the discovery and development of conductive polymers." Doping
(oxidation or reduction) introduces holes or extra electrons that move along the polymer
chain, making it electrically conductive. Conductive polymers are used in anti-static
coatings, electromagnetic shields, "smart" windows, LEDs, solar cells, and displays, and
underpin molecular electronics.

:::{figure} images/fig-p2-appC-7.png
:name: fig-p2-appC-7
:width: 80%
:align: center

Nobel Prize in Chemistry 2000 — conductive polymers (Heeger, MacDiarmid, Shirakawa).
:::

## C.2 Organic Thin Films and Crystals

Organic thin films may be **amorphous or crystalline**. Detailed molecular-orbital
calculations of the electron density in the highest occupied molecular orbital of a PTCDA
molecule agree with STM experiments, showing the maturity of our understanding of the
electronic arrangement on molecules. However, the *dynamic electronic processes* in
molecules and molecular assemblies are **not well understood** and are an active research
topic.

:::{figure} images/fig-p2-appC-8.png
:name: fig-p2-appC-8
:width: 80%
:align: center

Organic thin films may be amorphous or crystalline (PTCDA molecular orbital and STM scan).
:::

In crystalline organic films (e.g. PTCDA, with unit-cell dimensions 11.96 Å × 17.34 Å and
a 3.21 Å stacking spacing), the **charged-carrier mobility increases with increased
$\pi$–$\pi$ orbital overlap**. Good mobility is obtained in the stacking direction:
$\mu \approx 0.1\ \text{cm}^2/\text{Vs}$ (stacking) versus $\mu \approx 10^{-5}\ \text{cm}^2/\text{Vs}$
(in-plane). The highest mobilities are obtained on single crystals — pentacene
$\mu = 10^5\ \text{cm}^2/\text{Vs}$ and tetracene $\mu = 10^4\ \text{cm}^2/\text{Vs}$ at 10 K
(Schön et al., Science 2000).

:::{figure} images/fig-p2-appC-9.png
:name: fig-p2-appC-9
:width: 80%
:align: center

Crystalline organic films — PTCDA and mobility versus $\pi$–$\pi$ overlap.
:::

:::{figure} images/fig-p2-appC-10.png
:name: fig-p2-appC-10
:width: 80%
:align: center

Growing organic crystals (Kloc et al., J. Cryst. Growth 182, 416 (1997)).
:::

## C.3 Charge Transport in Organic Solids

For **space-charge-limited conduction** (unipolar, no traps, observed in crystalline
organics) the current density follows the Child–Langmuir-like law

$$
J = \frac{9}{8}\,\frac{\varepsilon_r \varepsilon_0 \,\mu\, V^{2}}{L^{3}}, \qquad
C = \frac{\varepsilon_r \varepsilon_0 A}{L}, \qquad
t_{\text{tr}} = \frac{L^{2}}{\mu V}.
$$

:::{figure} images/fig-p2-appC-11.png
:name: fig-p2-appC-11
:width: 80%
:align: center

Space-charge-limited conduction: $J = (9/8)\, C V / (A t_{\text{tr}})$.
:::

Charge transport can be **band-like below room temperature** and **hopping-like above
room temperature** (Schön et al., PRL 86, 3843 (2001)). The crossover is governed by
electron–acoustic-phonon coupling ($g$).

:::{figure} images/fig-p2-appC-12.png
:name: fig-p2-appC-12
:width: 80%
:align: center

Band-like charge transport below RT; hopping transport above RT (Schön et al., PRL 86, 3843 (2001)).
:::

:::{figure} images/fig-p2-appC-13.png
:name: fig-p2-appC-13
:width: 80%
:align: center

Electron–acoustic-phonon coupling $g$ (Schön et al., PRL 86, 3843 (2001)).
:::

Many organic crystals collapse onto a **universal transport curve** when mobility is plotted
against a reduced temperature scale (Schön et al., PRL 86, 3843 (2001)).

:::{figure} images/fig-p2-appC-14.png
:name: fig-p2-appC-14
:width: 80%
:align: center

Universal transport curve for organic crystals (Schön et al., PRL 86, 3843 (2001)).
:::

Pentacene-based **organic thin-film transistors (TFTs)** achieve room-temperature
mobilities of ~1–3 cm$^2$/Vs, operating voltages < 10 V, and on/off ratios ~10$^8$
(comparable to amorphous Si), enabling integration with conventional electronics,
high-speed (~few GHz) transistors, molecular-size devices, and flexible-substrate
applications (video backplanes, smart cards). The challenge is large-area ordered growth
of crystalline organic thin films.

:::{figure} images/fig-p2-appC-15.png
:name: fig-p2-appC-15
:width: 80%
:align: center

Organic thin-film transistors — pentacene-based TFT.
:::

:::{figure} images/fig-p2-appC-16.png
:name: fig-p2-appC-16
:width: 80%
:align: center

Organic ambipolar transistor (Schön et al., Science 287, 1023 (2000)).
:::

In **amorphous organics**, conduction is **trap-limited**. Charge trapping can dominate;
a trap level below the LUMO captures carriers and the molecule distorts, lowering its
energy by $\Delta E$.

:::{figure} images/fig-p2-appC-17.png
:name: fig-p2-appC-17
:width: 80%
:align: center

Trap-limited space-charge conduction observed in amorphous organics.
:::

The temperature-dependent trap-limited current follows

$$
J \propto N_{\text{LUMO}}\,\mu_n\,N_t^{\,m}\,d^{-2m-1} V^{m+1}, \qquad m = T_t/T,
$$

with trap density $N_t \approx 3.1\times10^{18}\ \text{cm}^{-3}$ and
$\mu_n N_{\text{LUMO}} \approx 4.8\times10^{14}\ \text{cm}^{-1}\text{V}^{-1}\text{s}^{-1}$
(Shen, Burrows, Bulovic, McCarty, Thompson, Forrest, Jpn. J. Appl. Phys. 35, L401 (1996)).

:::{figure} images/fig-p2-appC-18.png
:name: fig-p2-appC-18
:width: 80%
:align: center

Trap-limited conduction in organic materials (trap distribution and temperature dependence).
:::

In disordered organic solids the traps form an **exponential distribution** $D(E)$ in
energy between HOMO and LUMO.

:::{figure} images/fig-p2-appC-19.png
:name: fig-p2-appC-19
:width: 80%
:align: center

Traps in disordered organic solids — exponential trap distribution $D(E)$.
:::

Charge in organic solids is carried by **polarons** — a carrier dressed by a local
distortion of the molecule/ lattice.

:::{figure} images/fig-p2-appC-20.png
:name: fig-p2-appC-20
:width: 80%
:align: center

Polarons — charge in organic solids.
:::

## C.4 Interfaces, Electrodes, and Electron Transfer

At **disordered interfaces** (e.g. organic/metal or organic/inorganic contacts such as
Alq$_3$/Mg:Ag on Si) the interface region contains defects that strongly affect the
current–voltage characteristics in both forward and reverse bias.

:::{figure} images/fig-p2-appC-21.png
:name: fig-p2-appC-21
:width: 80%
:align: center

Disordered interfaces and their I–V characteristics (interface region defects).
:::

A **dipole layer** at the metal/organic interface shifts the alignment of the organic
HOMO/LUMO relative to the metal Fermi level $E_F$, modifying injection.

:::{figure} images/fig-p2-appC-22.png
:name: fig-p2-appC-22
:width: 80%
:align: center

Dipoles at interfaces — metal/organic contact band alignment (a) and (b).
:::

The device performance shows a strong **dependence on the electrode** material (Ag, ITO,
Mg, or ITO–Ag / ITO–Mg composites), which changes the effective barrier and thus the
current.

:::{figure} images/fig-p2-appC-23.png
:name: fig-p2-appC-23
:width: 80%
:align: center

Dependence of device current on electrode material.
:::

The Marcus electron-transfer model describes how carriers move between molecules; the
transfer rate depends on the reorganization energy and the energy offset between donor and
acceptor (Baldo and Forrest, PRB 64 (2001)).

:::{figure} images/fig-p2-appC-24.png
:name: fig-p2-appC-24
:width: 80%
:align: center

Marcus electron-transfer model (Baldo and Forrest, PRB 64 (2001)) — part 1.
:::

:::{figure} images/fig-p2-appC-25.png
:name: fig-p2-appC-25
:width: 80%
:align: center

Marcus electron-transfer model (Baldo and Forrest, PRB 64 (2001)) — part 2.
:::

:::{figure} images/fig-p2-appC-26.png
:name: fig-p2-appC-26
:width: 80%
:align: center

Marcus electron-transfer model (Baldo and Forrest, PRB 64 (2001)) — summary.
:::

## C.5 Excitons and Radiative Processes

A radiative system can be excited in several ways: photoluminescence, electroluminescence,
cathodoluminescence, chemoluminescence, and bioluminescence. The light-generation mechanism
is the central question for devices.

:::{figure} images/fig-p2-appC-27.png
:name: fig-p2-appC-27
:width: 80%
:align: center

Question 1: How is the radiative system excited? (PL, EL, CL, chemoluminescence, bioluminescence).
:::

A photon is emitted when an electron drops from an upper to a lower energy level. The
luminescence quantum efficiency is

$$
\eta = \frac{P_R}{P_R + P_{NR}}
= \frac{1/t_R}{1/t_R + 1/t_{NR}}, \qquad
P_R = 1/t_R,\; P_{NR} = 1/t_{NR},
$$

where $P_R$ and $P_{NR}$ are the radiative and non-radiative transition probabilities. For
high-efficiency devices one must reduce the probability of non-radiative processes.

:::{figure} images/fig-p2-appC-28.png
:name: fig-p2-appC-28
:width: 80%
:align: center

Radiative transitions — efficiency (radiative vs. non-radiative).
:::

Electronic transitions in molecules are described by a molecular configuration-energy
diagram of the $S_0$ and $S_1$ states. The energy shift between the absorption peak
($E_A$) and the emission peak ($E_B$) is the **Franck–Condon shift**, set by the nuclear
displacement $\Delta r$ from the equilibrium distance $r_0$.

:::{figure} images/fig-p2-appC-29.png
:name: fig-p2-appC-29
:width: 80%
:align: center

Electronic transitions in molecules — Franck–Condon shift of the $S_0$/$S_1$ states.
:::

Molecular absorption and luminescence show a series of **vibronic peaks** (e.g. $S_1[0\text{–}0]$,
$S_1[0\text{–}1]$, $S_1[0\text{–}2]$, $S_1[0\text{–}3]$) in both solution (PTCDA in DMSO) and
solid; the 0–0, 0–1, 0–2, 0–3 progression reflects vibrational replicas.

:::{figure} images/fig-p2-appC-30.png
:name: fig-p2-appC-30
:width: 80%
:align: center

Examples of molecular absorption and luminescence — vibronic progression (PTCDA).
:::

The **Jablonski diagram** summarizes the electronic processes: absorption populates $S_1$;
from $S_1$ one can have fluorescence (~1–10 ns), internal conversion, or intersystem
crossing (ISC, ~10 ps) to the triplet $T_1$; from $T_1$ phosphorescence occurs (>100 ns).
Energy transfer (Förster, Dexter, or radiative) can move excitation between molecules.
$S$ denotes spin-0 (singlet) states and $T$ spin-1 (triplet) states.

:::{figure} images/fig-p2-appC-31.png
:name: fig-p2-appC-31
:width: 80%
:align: center

Electronic processes in molecules — Jablonski diagram.
:::

Combining two fermions gives three symmetric "triplet" spin states and one antisymmetric
"singlet" state:

$$
|S\rangle = |\uparrow\uparrow\rangle,\; |\downarrow\downarrow\rangle,\;
\frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle)
\quad\text{(triplets)},\qquad
\frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)
\quad\text{(singlet)}.
$$

Singlets comprise 25% of the excitons; the wavefunction $S$ describes the spin state of
the excited electron.

:::{figure} images/fig-p2-appC-32.png
:name: fig-p2-appC-32
:width: 80%
:align: center

Combination of two fermions — singlets and triplets.
:::

Within the **Born–Oppenheimer approximation**, the total wavefunction factors into
electronic, spin, and nuclear-vibration parts, $\Psi_m = \Theta_m S_m \Phi_m$. The
electronic transition (dipole) matrix element is

$$
\vec{\mu} = \sum_j q\,\vec{r}_j, \qquad
F_{i\to f} = \langle \Psi_i | \vec{\mu} | \Psi_f \rangle
= \langle \Theta_i | \langle \Phi_i | \vec{\mu} | \Phi_f \rangle | \Theta_f \rangle,
$$

where the rate is evaluated with Fermi's Golden Rule. Spin selection rules require
$\Delta S = 0$ during an electronic transition, so singlet$\leftrightarrow$triplet radiative
transitions are forbidden. Shortcomings: the approximation decouples electronic and nuclear
motion and breaks down near degeneracies, and it does not explain "forbidden" transitions
that arise from spin–orbit coupling.

:::{figure} images/fig-p2-appC-33.png
:name: fig-p2-appC-33
:width: 80%
:align: center

Born–Oppenheimer approximation — transition dipole matrix element.
:::

:::{figure} images/fig-p2-appC-34.png
:name: fig-p2-appC-34
:width: 80%
:align: center

Born–Oppenheimer approximation (cont.) — selection rules and shortcomings.
:::

**Fluorescence** is a fast (~10$^{-9}$ s), symmetry-conserving singlet $\to$ singlet-ground
transition. **Phosphorescence** is a slow (~1 s) triplet $\to$ ground-state transition that
is normally not permitted.

:::{figure} images/fig-p2-appC-35.png
:name: fig-p2-appC-35
:width: 80%
:align: center

Fluorescence and phosphorescence from singlet and triplet excitons.
:::

Excitons can be generated **photographically** (absorption of a photon leaves the molecular
symmetry unchanged $\Rightarrow$ only singlets) or **electrically** (electron–hole
recombination gives uncorrelated spins $\Rightarrow$ both singlets and triplets). Only
singlets contribute to fluorescence; triplets contribute to (low-efficiency) phosphorescence.

:::{figure} images/fig-p2-appC-36.png
:name: fig-p2-appC-36
:width: 80%
:align: center

Generation of excitons — photo- vs. electrical generation.
:::

There are two limiting exciton pictures: the **Wannier exciton** (typical of inorganic
semiconductors; binding energy ~10 meV, radius ~100 Å) and the **Frenkel exciton** (typical
of organic materials; binding energy ~1 eV, radius ~10 Å). One can treat excitons as
chargeless particles capable of diffusion, or as excited states of the molecule.

:::{figure} images/fig-p2-appC-37.png
:name: fig-p2-appC-37
:width: 80%
:align: center

Wannier exciton (semiconductor picture) vs. Frenkel exciton (molecular picture).
:::

Electrically pumped organic semiconducting lasers have been demonstrated (Schön et al.,
Science 288, 656 (2000)).

:::{figure} images/fig-p2-appC-38.png
:name: fig-p2-appC-38
:width: 80%
:align: center

Electrically pumped organic semiconducting "lasers" (Schön et al., Science 288, 656 (2000)).
:::

Organic solar cells (e.g. CuPc/PTCBI with a BCP layer) show a broad spectral response
(300–800 nm) and power efficiency $\eta_P \sim 3\%$ in a concentrator geometry; the I–V
response under solar illumination (AM1.5, 1300 mW/cm$^2$ ≈ 17 suns) gives the open-circuit
voltage $V_{\text{OC}}$ and short-circuit current $I_{\text{MAX}}$ (Peumans, Bulovic,
Forrest, Appl. Phys. Lett. 2000).

:::{figure} images/fig-p2-appC-39.png
:name: fig-p2-appC-39
:width: 80%
:align: center

Organic solar cells — I–V response under solar illumination (ISC/VOC).
:::

## C.6 Donor-Acceptor Systems and Devices

At a **donor–acceptor heterojunction** (D: CuPc, A: PTCBI) photoinduced charge transfer
proceeds in four steps: (1) exciton generation by absorption of light, (2) exciton
diffusion over the diffusion length $L_D$, (3) exciton dissociation by rapid and efficient
charge transfer, and (4) charge extraction by the internal electric field.

:::{figure} images/fig-p2-appC-40.png
:name: fig-p2-appC-40
:width: 80%
:align: center

Photoinduced charge-transfer processes at a donor-acceptor heterojunction.
:::

VOPc/PTCDA multilayers show that the incident-light quantum efficiency increases with the
number of interfaces (Arbour et al., Mol. Cryst. Liq. Cryst. 183, 307 (1990)).

:::{figure} images/fig-p2-appC-41.png
:name: fig-p2-appC-41
:width: 80%
:align: center

VOPc/PTCDA multilayers — quantum efficiency vs. number of interfaces.
:::

Donor–acceptor multilayer organic photodetectors achieve high external quantum efficiency
that depends on the layer thickness (e.g. $t = 5$ Å, 64 layers) and bias
(Peumans, Bulovic, Forrest, Appl. Phys. Lett. 2000).

:::{figure} images/fig-p2-appC-42.png
:name: fig-p2-appC-42
:width: 80%
:align: center

Donor-acceptor multilayer organic photodetectors.
:::

Organic semiconducting lasers have been made in both vertical (VCSEL-like, DBR/quartz)
and lateral structures, with laser wavelengths tunable via the dopant (DCM, DCM2, Rhodamine,
Perylene, C47, etc. in Alq$_3$ or CBP host). Organic lasers show remarkable temperature
insensitivity ($T_0 \approx 1000$) compared with inorganic lasers (Kozlov et al., Nature
389, 362 (1997); Bulovic et al., Science 279, 553 (1998)).

:::{figure} images/fig-p2-appC-43.png
:name: fig-p2-appC-43
:width: 80%
:align: center

Organic semiconducting lasers — vertical and lateral structures.
:::

In **doped organic films**, excitons are formed from recombining electrons and holes, then
transfer to a luminescent dye (dopant) hosted in a charge-transport matrix (e.g. a-NPD
host, Alq$_3$ transport). Energy levels: host transport ~2.6–2.7 eV, dopant ~5.7–6.0 eV.

:::{figure} images/fig-p2-appC-44.png
:name: fig-p2-appC-44
:width: 80%
:align: center

Electroluminescence in doped organic films (host/dopant energy-level picture).
:::

Dopants strongly modify the OLED electroluminescence spectrum: Alq$_3$ (green), DCM2:Alq$_3$
(red-orange), and PtOEP:Alq$_3$ (phosphorescent red) shift the emission wavelength.

:::{figure} images/fig-p2-appC-45.png
:name: fig-p2-appC-45
:width: 80%
:align: center

Effect of dopants on the OLED EL spectrum.
:::

The **solid-state solvation effect** shifts the emission of a chromophore (e.g. DCM2 in
Alq$_3$) as a function of dopant concentration (1%, 2%, 5%, 10%), tuning the EL spectrum
and its temporal response (sub-nanosecond to few-nanosecond) via the host dipole moment
$\mu$ (Bulovic et al., Chem. Phys. Lett. 287, 455 (1998); 308, 317 (1999)).

:::{figure} images/fig-p2-appC-46.png
:name: fig-p2-appC-46
:width: 80%
:align: center

Solid-state solvation effect — EL spectrum tuning and temporal response.
:::

The present and near-future of organic display technology include the Kodak/Sanyo 5.5"
AM-OLED display, the Pioneer multicolor display, and flexible, pixelated, monochrome
displays from Universal Display Corp.

:::{figure} images/fig-p2-appC-47.png
:name: fig-p2-appC-47
:width: 80%
:align: center

The present and future of organic display technology (AM-OLED, flexible displays).
:::
