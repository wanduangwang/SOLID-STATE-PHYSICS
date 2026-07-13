---
title: "13 Amorphous Semiconductors"
abstract: >
  This chapter discusses the structure and electronic, optical, and transport
  properties of amorphous semiconductors. It covers the absence of long-range
  order, the persistence of short-range order, the Mott mobility-edge and
  Cohen–Fritzsche–Ovshinsky (CFO) models of localized versus extended states,
  the valence-alternation-pair model for chalcogenides, broadened optical
  absorption edges, and the fabrication and properties of amorphous
  semiconductor superlattices.
---

# 13 Amorphous Semiconductors

There are many materials which are of scientific and technological interest which are not
single crystals, or even microcrystalline. The general category of amorphous materials is
defined as including materials which have no crystalline order; that is, their x-ray
diffraction patterns consist of thick diffuse rings or halos instead of sharp spots. Usually
excluded from this definition are polycrystalline materials which consist of small crystallites
in random orientations. Since, as we shall discuss below, amorphous materials often do
possess considerable short-range order, the distinction between polycrystalline and amorphous
materials blurs as the crystallite size is reduced. There are a number of substances, such as
Ge and Si, which can be prepared in all three forms: single-crystal, polycrystalline and
amorphous.

Amorphous materials can be prepared in several ways, depending on the material. Materials
called glasses can be formed by cooling from the liquid state. These materials are not in
thermal equilibrium and can be classified as super-cooled liquids with an extremely high
viscosity. Some materials cannot be cooled fast enough to avoid crystallization. Splat cooling
(or rapid solidification) is often used to prepare metallic glasses. In this process a liquid
stream is shot onto a thermally conducting substrate. Some of the splat-cooled metals exhibit
microcrystalline ordering. There are also a number of techniques for deposition from the
vapor state, such as sputtering, or for condensation from a chemically reactive vapor such as
silane ($\mathrm{SiH_4}$) to prepare (hydrogenated) amorphous Si.

Many amorphous materials can be called semiconductors in the sense that they are neither good
conductors nor good insulators, but instead are poor conductors. Many are also similar to
their crystalline counterparts in that they possess an optical gap. The reason for this general
behavior seems to be that, even though the amorphous structure is quite random over long
distances, there still seems to be considerable short-range order with local bonding
requirements generally satisfied. Although these materials are full of defects, there are not
many electrons which are involved in the process to carry electric current. In addition,
because of the spatial disorder resulting in strong carrier scattering, the carriers mobilities
are low. A further consequence of the tendency for bonding to be satisfied is that the
electrical properties of many amorphous semiconductors tend to be insensitive to the presence
of large concentrations of impurities.

There are two major categories of amorphous semiconductors. The first consists of the
tetrahedrally bonded materials, primarily Ge and Si but also including amorphous III–V
semiconductors. The second major category consists of the chalcogenide or lone-pair
semiconductors, which means the elements Se, S or Te (column VI) and compounds and alloys
containing these elements.

**References**

- Kittel, *Introduction to Solid State Physics*
- Ziman, *Models of Disorder*, Cambridge, 1979.

## 13.1 Introduction

### 13.1.1 Structure of Amorphous Semiconductors

The major attribute of the structure of amorphous materials is the lack of long-range order or
the absence of a periodic lattice. In spite of this, there is considerable similarity in the
local environments of amorphous and crystalline materials. For example, the EXAFS
measurements for Ge shown in {numref}`fig-p2-ch13-1` indicate that the first and
second-nearest-neighbor distances are the same and that differences only appear at the
third-and higher-neighbor distances.

Not only are these short-range bond lengths usually preserved, but also bond angles tend to be
the same. Some amorphous materials have been modeled successfully as continuously perturbed
from their crystalline form. However there is also some evidence from x-ray diffraction for
more drastic changes. For example, one can view crystalline germanium or silicon as containing
distorted 6-fold rings (see {numref}`fig-p2-ch13-2` for the diamond structure). Amorphous
germanium and silicon also seem to contain some 5-fold rings.

:::{figure} images/fig-p2-ch13-1.png
:name: fig-p2-ch13-1
:width: 60%
:align: center

Figure 13.1: Distribution of neighbor distances $G(r)$ for Ge, from EXAFS data, shown for both crystalline and amorphous germanium.
:::

:::{figure} images/fig-p2-ch13-2.png
:name: fig-p2-ch13-2
:width: 60%
:align: center

Figure 13.2: The diamond structure showing the atoms 1 and 2 are in a staggered configuration and are crystallographically distinct in the perfect crystal.
:::

### 13.1.2 Electronic States

It is evident that Bloch's theorem no longer holds in amorphous materials; hence electronic
states cannot be characterized by a $\vec{k}$ vector confined to a single Brillouin zone. In
other words, $\vec{k}$ is no longer a good quantum number. Thus one can no longer use the
powerful energy-band theory which predicts bands of extended electronic states with forbidden
gaps, and which we use to differentiate conductors from insulators.

In practice the electronic properties of an amorphous material do not differ as drastically as
one might expect from those of the crystalline material. Consider the data for the resistivity
of a number of materials at temperatures near their melting points, as shown in
{numref}`fig-p2-ch13-3`. Where small jumps do occur at the melting point, these are correlated
with small discontinuous volume changes. When the volume does not change, as for HgTe or CdTe,
neither does the resistivity. Evidently the conduction properties are remarkably similar even
though the structure has changed drastically. We note here that for the column IV
semiconductors (Si, Ge, Sn), the molten material is metallic and octahedrally coordinated.

Without the powerful simplification of Bloch's theorem, it is extremely difficult to calculate
the electronic states in amorphous materials. Without a $\vec{k}$-vector one cannot calculate
$E(\vec{k})$. Instead one attempts to calculate directly a density of states $\rho(E)$, and
also an average energy-dependent mobility $\mu(E)$. One starts by noting the similarity of
amorphous and crystalline electronic properties and especially their similarity with respect to
short-range order. Recently much progress has been made using various types of cluster models.
The general result, as shown in {numref}`fig-p2-ch13-4`, is that the crystalline density of
states, which has sharp features called Van Hove singularities at critical points where
$\partial E / \partial \vec{k} = 0$, is smoothed out and broadened at the critical points (see
§4.2). This is shown experimentally in the photoemission results in {numref}`fig-p2-ch13-5` for
the valence bands of trigonal (crystalline) and amorphous Se and Te.

:::{figure} images/fig-p2-ch13-3.png
:name: fig-p2-ch13-3
:width: 60%
:align: center

Figure 13.3: Resistivity as a function of temperature for several materials in both the crystalline and liquid states. The melting temperature in each case is indicated by an arrow.
:::

:::{figure} images/fig-p2-ch13-4.png
:name: fig-p2-ch13-4
:width: 60%
:align: center

Figure 13.4: (a) Density of electronic states as a function of energy for a single band of a crystalline solid. The sharp behavior at the band edges and in the interior represents the effects of Van Hove singularities. (b) Density of electronic states as a function of energy for a single band of an amorphous solid. All Van Hove singularities have disappeared. (The Van Hove singularities are the $M_0$, $M_1$, $M_2$, $M_3$ singularities in the joint density of states discussed in §4.2.)
:::

:::{figure} images/fig-p2-ch13-5.png
:name: fig-p2-ch13-5
:width: 60%
:align: center

Figure 13.5: Ultraviolet photoemission results (top) for the density of states for trigonal (solid line) and amorphous (dashed line) Se. Photoemission results (bottom) on trigonal (solid line) and amorphous (dashed line) Te.
:::

In order to find the transport properties of an amorphous material, one needs to know not only
the density of states $\rho(E)$ at each energy $E$, but also the mobility $\mu(E)$ which may
be a function of $\rho(E)$. Broadly, one distinguishes extended states, similar to states in
periodic crystals which have finite amplitude throughout the material, and finite mobility,
from localized states which have a significant amplitude only in a small region of the material
and have extremely small mobility. An example of such a localized state, in a nearly perfect
crystal, is an impurity state in which the electron is localized in a hydrogen-like orbit around
a donor ion. Such states have sharp features in a density-of-states diagram near the
conduction-band minimum or, for acceptors near, the valence-band maximum, as shown in
{numref}`fig-p2-ch13-6`(b). If there is a large enough impurity concentration, these states can
broaden into impurity bands which can merge into the conduction or valence bands. However, if
the material itself is disordered or amorphous, the states near the band edges are themselves
localized.

This subject of localized vs. extended states has been treated extensively, most notably by
Mott and by Anderson who shared the Nobel Prize in Physics in 1977 for this work. Mott
developed the concept of the mobility edge, postulating a relatively sharp demarcation between
localized and extended states, giving rise to a mobility gap which is considerably larger than
the forbidden gap in the density of states, as illustrated in {numref}`fig-p2-ch13-7`. The
mechanism for localization in states near the energy band edges is illustrated in
{numref}`fig-p2-ch13-8`, and is due to Fritzsche. According to this model disorder produces a
spatial variation in the conduction and valence band edges, giving rise to local
conduction-band minima or valence-band maxima which trap electrons or holes.

:::{figure} images/fig-p2-ch13-6.png
:name: fig-p2-ch13-6
:width: 60%
:align: center

Figure 13.6: Density of states $n(E)$ for (a) a perfect crystal, (b) a crystal with a few donors and acceptors, and (c) a crystal with a larger number of imperfections where the impurity levels have broadened into impurity bands.
:::

:::{figure} images/fig-p2-ch13-7.png
:name: fig-p2-ch13-7
:width: 60%
:align: center

Figure 13.7: Sketch of the Mott–CFO (Cohen–Fritzsche–Ovshinsky) model for covalent disordered semiconductors having a three-dimensional cross-linked network structure. The critical energies $E_c$ and $E_v$ define the mobility gap. For $T > 0$, the mobility $\mu(E)$ may be finite in the gap because of thermally assisted tunneling. Here $E_F$ denotes the Fermi energy. The distribution of localized gap states may be non-monotonic when defect states of a certain energy are prevalent.
:::

:::{figure} images/fig-p2-ch13-8.png
:name: fig-p2-ch13-8
:width: 70%
:align: center

Figure 13.8: Potential fluctuations of the initial and final electron states for the optical transitions corresponding to the optical gap $E_0$. The left hand side shows the density of states. The region of localized states lies between $E_c$ and $E_v$. Note that the short range potential wells which give rise to many of the localized states are not shown here. This figure shows only that part of the long wavelength potential fluctuations which cause a parallel shift of the valence and conduction band states. The part which causes a spatial variation of $E_0$ is omitted for clarity (after Fritzsche).
:::

An important difference between the tetrahedrally-bonded amorphous semiconductors and the
chalcogenide materials is that the former have large numbers of unpaired spins, as observed in
electron spin resonance experiments, and the chalcogenides have no measurable density of spins.
A large number of unpaired spins is expected in a material containing a large number of broken
or "dangling" bonds, each bond being occupied only by one electron instead of two electrons of
opposite spin. The lack of unpaired spins has been explained by the valence-alternation-pair
model of Kastner, Adler and Fritzsche. The chalcogen atoms have 4 electrons in an outer
(unfilled) $p$ shell. In the lowest-energy bonding configuration, two of these electrons form
bonds with neighboring atoms, and two are in non-bonding or "lone-pair" states. Thus both
crystalline and amorphous Se, for example, contain chains of atoms, each bonded to two
neighbors. In the amorphous material a Se atom can also be triply-bonded in a trigonal
configuration, leaving the fourth $p$ electron in a higher-energy, non-bonding state (with
unpaired spin). However, the total energy can be reduced if this extra electron migrates to
another triply-bonded Se atom nearby. First, two of the bonds on this second atom break,
leaving only one electron in a bonding orbital. The two electrons from the broken bonds join
the single electron in the lone-pair orbitals. Then the new electron can enter this atom as a
fourth lone-pair electron. Kastner, Adler and Fritzsche argued that this is an energetically
favorable configuration. The result, as shown in {numref}`fig-p2-ch13-9`, is a large density of
equal number of positive and negative ions but with all electron spins paired. Structurally,
this picture implies that chalcogenide glasses contain a large number of linked chains (by
triply-bonded atoms) as well as nearby broken chains (ending in singly-bonded atoms), which
provides an explanation for the fact that these materials are more resistant to crystallization
("better glasses") than the tetrahedrally-bonded materials.

At the left of {numref}`fig-p2-ch13-9` two selenium atoms, each of which is triply bonded,
serve to cross-link two molecular chains of doubly bonded atoms. A valence-alternation pair can
be produced (right) by a spontaneous break of the cross-linkage, combined with the simultaneous
transfer of an electron from one of the triply bonded selenium atoms to an atom near the one
where the cross-link was broken. Since such electronic transfers reduce the total energy of the
solid, nearly all the trigonally bonded selenium atoms become members of a valence-alternation
pair. Important physical consequences follow, including the almost complete disappearance of
electrons with unpaired spins and the appearance of large but equal concentrations of
positively and negatively charged traps in chalcogenide glasses. The consequences of this high
disorder (in the chalcogenides) for the electronic density of states is shown in
{numref}`fig-p2-ch13-10`.

:::{figure} images/fig-p2-ch13-9.png
:name: fig-p2-ch13-9
:width: 70%
:align: center

Figure 13.9: Valence-alternation pairs can form in a neutral chalcogenide-glass matrix without any major displacement of its atoms, leading to a sharp reduction in total energy.
:::

:::{figure} images/fig-p2-ch13-10.png
:name: fig-p2-ch13-10
:width: 70%
:align: center

Figure 13.10: Amorphous semiconductors that are not strongly disordered (left) have valence and conduction bands similar to those in the corresponding crystalline semiconductor. If the disorder is large, as is expected in multicomponent glasses (right), the band tails of the valence and conduction bands can overlap in the mobility gap. This leads to a redistribution of electric charge as electrons move from one localized state to another in order to lower their energy.
:::

On the left is shown the broadened conduction band and valence bands, with the mobility edges,
for an amorphous tetrahedrally bonded semiconductor. Cohen, Ovshinsky and Fritzsche postulated
that (whatever the details of the structure), the high disorder in the chalcogenides produces
overlapping densities of states, as shown in the right side of the figure, so that electrons
will lower their energy by migrating to new localized states, creating large charge separation
as in the valence-alternation model.

The distinguishing feature of the bands in amorphous solids is the replacement of the sharp
band edges present in crystals by what are called "band tails" or localized states, that extend
into the energy gap. The localized states are separated from the extended states in the main
part of the bands by "mobility edges". The region that lies between the mobility edges of the
valence and conduction bands is the "mobility gap" (see {numref}`fig-p2-ch13-10`). It plays the
same role in amorphous semiconductors that the energy gap plays in crystalline semiconductors.
Chemical impurities or defects in the configuration of local bands can lead to sharp structural
changes (not shown) in the mobility gap. The result of the large density of localized states in
the mobility gap is a high density of positively and negatively charged traps, which decrease
the mobility of the carriers and make the material less sensitive to efforts to control its
conductivity by doping.

This density of states model explains the fact that the chalcogenide glasses are much less
sensitive to doping than the tetrahedrally coordinated materials. Impurity states, introduced in
or just outside the band tails, make only a negligible change in the already-appreciable density
of states in this region. If, on the other hand, the bands do not overlap, impurity states in or
just outside the band tails can make a large change in the density of states. Thus they can, at
finite temperatures, become a source of carriers in the conducting or extended states.

### 13.1.3 Optical Properties

Amorphous semiconductors have optical spectra similar to their crystalline counterparts in that
they possess an optical gap or absorption edge. However, all sharp features, including the band
edge absorption, are considerably broadened, as shown for the case of the chalcogenide
semiconductor $\mathrm{As_2S_3}$ in {numref}`fig-p2-ch13-11`. The reflectance spectra for
crystalline, amorphous and liquid Ge are given in {numref}`fig-p2-ch13-12`. These data show that
the amorphous material more closely resembles the crystalline material than the liquid which
shows metallic behavior at low frequencies.

As was the case for the photoemission measurements, the broadened optical spectra result from
the broadened density of states for the amorphous materials. In fact, since $\vec{k}$ is no
longer a good quantum number, one can expect that transitions would be allowed between any pair
of valence and conduction band states. The absorption coefficient in this picture is
proportional to

```{math}
:label: eq-p2-ch13-1
\alpha(\omega) = \frac{\text{const}}{\omega} \int dE\, \rho(E)\,\rho(E + \hbar\omega)\, \left| M(E) \right|^2
```

where $\rho(E)$ is the density of states, $\omega$ is the optical frequency, and $M(E)$ is a
generalized momentum matrix element. Mott has argued that $M = 1$ for transitions involving two
extended states and for one extended and one localized state, but that $M$ is negligible for
transitions involving two localized states (which will have negligible spatial overlap). Thus
the optical gap should be at a different energy $\hbar\omega = E_{\text{opt}}$ than the mobility
edge. Mott argued that the density of states $\rho(E) \simeq (E - E_0)$ is a linear function of
$E$ near the band edges $E_0$, giving

```{math}
:label: eq-p2-ch13-2
\alpha(\omega) = \text{const}\, \frac{(\hbar\omega - E_{\text{opt}})^2}{\omega}.
```

Unfortunately this argument is not of general validity, but is nevertheless used to estimate
$E_{\text{opt}}$ by plotting $(\alpha\hbar\omega)^{1/2}$ vs. $\omega$ and extrapolating the
straight-line behavior to zero frequency.

:::{figure} images/fig-p2-ch13-11.png
:name: fig-p2-ch13-11
:width: 60%
:align: center

Figure 13.11: Absorption edge of crystalline c–$\mathrm{As_2S_3}$ for 2 directions of light polarization relative to the c–axis compared with the absorption edge of amorphous a–$\mathrm{As_2S_3}$.
:::

:::{figure} images/fig-p2-ch13-12.png
:name: fig-p2-ch13-12
:width: 60%
:align: center

Figure 13.12: Fundamental reflection spectra due to electronic transitions in crystalline, amorphous and liquid Ge. The results are consistent with the metallic transport properties of liquid Ge.
:::

The amorphous chalcogenides exhibit remarkable luminescence behavior, with a large shift to
lower energy of the luminescence peak relative to $E_{\text{opt}}$, by as much as $1/2
E_{\text{opt}}$. This is attributed to a large electron-lattice interaction: the excited state of
the optical transition produces an atomic or bond rearrangement sufficient to cause a large
shift in the energies of both the excited and ground states.

### 13.1.4 Transport Properties

Transport measurements on amorphous semiconductors have proved difficult to interpret, partly
because of differences in the measured transport results arising from differences in methods of
sample preparation. Because of the low mobilities, Hall data have been difficult to obtain, and
thermopower data have been difficult to interpret. Attempts to measure mobilities using
transition-time methods resulted in the discovery of non-dispersive transport: a pocket of
charge injected at one side of the sample does not propagate to the other side with fixed
velocity but instead spreads out in time because of the large number of traps which have a large
distribution of release times. These measurements have been exploited by Professor Kastner's
group at MIT to give new data on the electronic density of states in amorphous
$\mathrm{As_2Se_3}$.

### 13.1.5 Applications of Amorphous Semiconductors

The most successful application of amorphous semiconductors has been the use of amorphous Se
films for Xerography. In this process, one surface of the film is charged. When light reflected
from the white area of the original page strikes the Se film, electron-hole pairs are formed,
which then migrate to the surface and neutralize the charge. These areas on the Se film do not
attract the small charged black "toner" particles, resulting in areas which do not print (white
on the copy). The unaffected (black) areas retain their charge, do attract toner, and do print
on the copy.

Another important application is for solar cells and thin film transistors, where the
substantial reduction in cost of producing large areas of amorphous rather than crystalline
films has the potential to offset their lower efficiency.

An effect which caused some excitement several years ago was the observation by Ovshinsky and
others of reversible switching behavior in chalcogenide semiconductors. This has been shown to
be due to an electronic mechanism, the filling of traps with carriers above a threshold current,
producing a sharp drop in the resistance. A second type of switching is associated with the
formation of small crystalline regions. These effects have been exploited in computer memory
devices.

## 13.2 Amorphous Semiconductor Superlattices

The extraction of quantitative information from the study of amorphous semiconductor
superlattices offers considerable challenge, because the number of variables is large (band
offsets, masses, band gaps, mobility edges, chemistry, etc.) On the other hand, superlattices
introduce one element of order ($z$–axis periodicity) in an otherwise disordered system; the
superlattice periodicity may perhaps be exploited to learn new physics about this class of
materials.

Early achievements in the field of amorphous semiconductor superlattices (B. Abeles and T.
Tiedje, *Phys. Rev. Lett.* **51**, 2003 (1983)) indicated that superlattices can be synthesized
with alternate layers of amorphous semiconductors such as a–Si:H, a–Ge:H, a–$\mathrm{SiN_x}$:H
and a–$\mathrm{Si_{1-x}C_x}$:H where the a denotes amorphous and the :H denotes the addition of
hydrogen to tie up the dangling bonds in the amorphous semiconductor. Unlike the case in
crystalline materials, lattice matching is not an issue in the synthesis of amorphous
semiconductor superlattices.

The amorphous superlattices are prepared by a plasma-assisted chemical vapor deposition (CVD)
method in which the composition of the reactive gases is changed periodically in the reaction
chamber. This process has some similarities to the MOCVD technique discussed in connection with
heterojunction crystalline semiconductor superlattices. The plasma assisted technique allows
deposition to occur at lower substrate temperatures, thereby achieving sharper interfaces. The
amorphous films can be deposited on quartz substrates. The residence time of the gases in the
reactor ($\mathrm{SiH_4}$ for preparing a–Si:H, and $\mathrm{SiH_4} + \mathrm{NH_3}$ for
preparing a–$\mathrm{Si_{1-x}N_x}$:H) can be as short as 1 sec while the time to grow a monolayer
is $\sim 3$ sec. (see {numref}`fig-p2-ch13-13`). Thus the gases in the reactor can be exchanged
rapidly enough to achieve sharp interfaces. The plasma discharge is maintained continuously
while the gases are changed.

The superlattice periodicity is monitored during the growth process, and the periodicity is
confirmed after the film is deposited by x-ray diffraction, as shown in {numref}`fig-p2-ch13-13`.
Because of the random atomic arrangements in the layer planes of the two constituents a–Si:H and
a–$\mathrm{Si_{1-x}N_x}$:H, there is no periodicity within the layers $d_1$ and $d_2$, so that
the only periodicity found with the x-ray characterization experiment is that due to the
periodicity $d = d_1 + d_2$. From the width of the x-ray peaks, the authors deduce an rms
fluctuation in the layer thickness of $\Delta d \sim 5$ Å where $d = 41 + 27 = 68$ Å.

Although no direct observation has been made of bound states in the quantum wells of amorphous
semiconductors, the optical absorption measurements of {numref}`fig-p2-ch13-14` show an increase
in the optical bandgap $E_g$ as the quantum well width decreases, where the optical gap was
determined from the energy dependence of the absorption coefficient using the relation
$\alpha \sim (\hbar\omega - E_g)^2/\omega$, which normally is valid for bulk amorphous
semiconductors.

The temperature dependence of the photoluminescence of the amorphous semiconductor superlattice
is similar to that of the bulk, showing an $\exp(-T/T_0)$ dependence, except that for the
superlattice the characteristic temperature, $T_0$ increases as the width of the quantum well
decreases, as shown in {numref}`fig-p2-ch13-15`. Also, the energy width $E_0$ of the localized
state distribution in the Urbach tail for amorphous semiconductors shows a similar increase as
the width of the quantum well decreases (see {numref}`fig-p2-ch13-15`), indicating that the
distribution of localized states broadens as the layer thickness decreases. It is expected that
the superlattices will have a small effect on localized states that are deep in the band tail,
but a large effect on the energy of the weakly localized shallow states.

:::{figure} images/fig-p2-ch13-13.png
:name: fig-p2-ch13-13
:width: 60%
:align: center

Figure 13.13: X-ray (1.54 Å) diffraction pattern vs. scattering angle (lower scale) and $d$ spacing (upper scale) of a a–Si:H (41 Å)/a–$\mathrm{SiN_x}$:H (27 Å) superlattice with 41 periods on a quartz substrate. The inset shows the energy-band diagram assumed for the superlattice. The conduction band offset $U = 1.05$ eV is indicated on the figure.
:::

:::{figure} images/fig-p2-ch13-14.png
:name: fig-p2-ch13-14
:width: 60%
:align: center

Figure 13.14: Optical-absorption coefficient $\alpha$ vs. photon energy $E$ for a–Si:H/a–$\mathrm{SiN_x}$:H superlattices with varying a–Si:H layer thickness $L$ and a constant a–$\mathrm{SiN_x}$:H layer thickness of 27 Å. Also given in the figure is the absorption coefficient $\alpha$ for a–$\mathrm{SiN_x}$:H films prepared under the same conditions.
:::

:::{figure} images/fig-p2-ch13-15.png
:name: fig-p2-ch13-15
:width: 60%
:align: center

Figure 13.15: Dependence of the optical gap on the a–Si:H sublayer thickness $L$ with the a–$\mathrm{SiN_x}$:H thickness held fixed at 27 Å. The solid line is a calculated curve based on the band diagram in Figure 13.13, assuming effective masses of unity. Dependence of the Urbach slope parameter $E_0$ (left scale) and photoluminescence quenching parameter $T_0$ (right side) on the a–Si:H layer thickness.
:::
