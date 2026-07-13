---
title: "E Transport in 1D materials"
abstract: "A review of the electronic and transport properties of single-walled carbon nanotubes, including their geometric and electronic structure, on-tube junctions and defects, nanotube ropes, crossed-tube junctions, and the effects of long-range disorder."
---

# E Transport in 1D materials

## E.0 Overview

This appendix reviews the unusual electronic and transport properties of carbon nanotubes as a paradigm for one-dimensional materials. Topics include the geometric and electronic structure of single-walled nanotubes, on-tube junctions and defects, quantum conductance, nanotube ropes, crossed-tube junctions, and the effects of long-range disorder on metallic and semiconducting tubes.

## E.1 Carbon Nanotubes

The nanometer dimensions of the carbon nanotubes together with the unique electronic structure of a graphene sheet make the electronic properties of these one-dimensional structures highly unusual. This Chapter reviews some theoretical work on the relation between the atomic structure and the electronic and transport properties of single-walled carbon nanotubes. In addition to the ideal tubes, results on the quantum conductance of nanotube junctions and tubes with defects will be discussed. On-tube metal-semiconductor, semiconductor-semiconductor, and metal-metal junctions have been studied. Other defects such as substitutional impurities and pentagon-heptagon defect pairs on tube walls are shown to produce interesting effects on the conductance. The effects of static external perturbations on the transport properties of metallic nanotubes and doped semiconducting nanotubes are examined, with the metallic tubes being much less affected by long-range disorder. The structure and properties of crossed nanotube junctions and ropes of nanotubes have also been studied. The rich interplay between the structural and the electronic properties of carbon nanotubes gives rise to new phenomena and the possibility of nanoscale device applications.

## E.2 Introduction

Carbon nanotubes are tubular structures that are typically several nanometers in diameter and many microns in length. This fascinating new class of materials was first discovered by S. Iijima [1] in the soot produced in the arc-discharge synthesis of fullerenes. Because of their nanometer dimensions, there are many interesting and often unexpected properties associated with these structures, and hence there is the possibility of using them to study new phenomena and employing them in applications [2, 3, 4]. In addition to the multi-walled tubes, single-walled nanotubes [5, 6, 7], and ropes of close-packed single-walled tubes have been synthesized [8]. Also, carbon nanotubes may be filled with foreign materials [9, 10] or collapsed into flat, flexible nanoribbons [11]. Carbon nanotubes are highly unusual electrical conductors, the strongest known fibers, and excellent thermal conductors. Many potentially important applications have been explored, including the use of nanotubes as nanoprobe tips [12], field emitters [13, 14], storage or filtering media [15], and nanoscale electronic devices [16, 17, 18, 19, 20, 21, 22, 23, 24]. Further, it has been found that nanotubes may also be formed with other layered materials [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]. In particular, BN, BC$_3$, and other B$_x$C$_y$N$_z$ nanotubes have been theoretically predicted [25, 26, 27, 28, 29] and experimentally synthesized [30, 31, 32, 33, 34, 35].

Many different aspects of carbon nanotubes are treated in the various sections of this Volume. In this Chapter, we focus on a review of some selected theoretical studies on the electronic and transport properties of carbon nanotube structures, in particular, those of junctions, impurities, and other defects. Structures such as ropes of nanotubes and crossed nanotubes are also discussed.

The organization of the Chapter is as follows. Section E.2 contains an introduction to the geometric and electronic structure of ideal single-walled carbon nanotubes. Section E.3 gives a discussion of the electronic and transport properties of various on-tube structures. Topics presented include on-tube junctions, impurities, and local defects. On-tube metal-semiconductor, semiconductor-semiconductor, and metal-metal junctions may be formed by introducing topological structural defects. These junctions have been shown to behave like nanoscale device elements. Other defects such as substitutional impurities and Stone–Wales defects on tube walls also are shown to produce interesting effects on the conductance. Crossed nanotubes provide another means to obtain junction behavior. The crossed-tube junctions, nanotube ropes, and effects of long-range disorder are the subjects of Section E.5. Intertube interactions strongly modify the electronic properties of a rope. The effects of long-range disorder on metallic nanotubes are quite different from those on doped semiconducting tubes. Finally, a summary and some conclusions are given in Section E.6.

## E.3 Geometric and Electronic Structure of Carbon Nanotubes

In this Section, we give an introduction to the structure and electronic properties of the single-walled carbon nanotubes (SWNTs). Shortly after the discovery of the carbon nanotubes in the soot of fullerene synthesis, single-walled carbon nanotubes were synthesized in abundance using arc discharge methods with transition metal catalysts [5, 6, 7]. These tubes have quite small and uniform diameter, on the order of one nanometer. Crystalline ropes of single-walled nanotubes with each rope containing tens to hundreds of tubes of similar diameter closely packed have also been synthesized using a laser vaporization method [8] and other techniques, such as arc-discharge and CVD techniques. These developments have provided ample amounts of sufficiently characterized samples for the study of the fundamental properties of the SWNTs. As illustrated in {numref}`fig-apptransport-E-1`, a single-walled carbon nanotube is geometrically just a rolled up graphene strip. Its structure can be specified or indexed by its circumferential periodicity [37]. In this way, a SWNT's geometry is completely specified by a pair of integers $(n, m)$ denoting the relative position $\vec{c} = n\vec{a}_1 + m\vec{a}_2$ of the pair of atoms on a graphene strip which, when rolled onto each other, form a tube.

:::{figure} images/fig-apptransport-E-1.png
:name: fig-apptransport-E-1
:width: 80%
:align: center
Fig. E.1: Geometric structure of an $(n, m)$ single-walled carbon nanotube.
:::

Theoretical calculations [38, 39, 40, 41] have shown early on that the electronic properties of the carbon nanotubes are very sensitive to their geometric structure. Although graphene is a zero-gap semiconductor, theory has predicted that the carbon nanotubes can be metals or semiconductors with different size energy gaps, depending very sensitively on the diameter and helicity of the tubes, i.e., on the indices $(n, m)$. As seen below, the intimate connection between the electronic and geometric structure of the carbon nanotubes gives rise to many of the fascinating properties of various nanotube structures, in particular nanotube junctions.

The physics behind this sensitivity of the electronic properties of carbon nanotubes to their structure can be understood within a band-folding picture. It is due to the unique band structure of a graphene sheet, which has states crossing the Fermi level at only 2 inequivalent points in $k$-space, and to the quantization of the electron wavevector along the circumferential direction. An isolated sheet of graphite is a zero-gap semiconductor whose electronic structure near the Fermi energy is given by an occupied $\pi$ band and an empty $\pi^*$ band. These two bands have linear dispersion and, as shown in {numref}`fig-apptransport-E-2`, meet at the Fermi level at the $K$ point in the Brillouin zone. The Fermi surface of an ideal graphite sheet consists of the six corner $K$ points. When forming a tube, owing to the periodic boundary conditions imposed in the circumferential direction, only a certain set of $\vec{k}$ states of the planar graphite sheet is allowed. The allowed set of $k$'s, indicated by the lines in {numref}`fig-apptransport-E-2`, depends on the diameter and helicity of the tube. Whenever the allowed $k$'s include the point $K$, the system is a metal with a nonzero density of states at the Fermi level, resulting in a one-dimensional metal with 2 linear dispersing bands. When the point $K$ is not included, the system is a semiconductor with different size energy gaps. It is important to note that the states near the Fermi energy in both the metallic and the semiconducting tubes are all from states near the $K$ point, and hence their transport and other properties are related to the properties of the states on the allowed lines. For example, the conduction band and valence bands of a semiconducting tube come from states along the line closest to the $K$ point.

:::{figure} images/fig-apptransport-E-2.png
:name: fig-apptransport-E-2
:width: 80%
:align: center
Fig. E.2: (Top) Tight-binding band structure of graphene (a single basal plane of graphite). (Bottom) Allowed $\vec{k}$-vectors of the $(7,1)$ and $(8,0)$ tubes (solid lines) mapped onto the graphite Brillouin zone.
:::

The general rules for the metallicity of the single-walled carbon nanotubes are as follows: $(n, n)$ tubes are metals; $(n, m)$ tubes with $n - m = 3j$, where $j$ is a nonzero integer, are very tiny-gap semiconductors; and all others are large-gap semiconductors. Strictly within the band-folding scheme, the $n - m = 3j$ tubes would all be metals, but because of tube curvature effects, a tiny gap opens for the case that $j$ is nonzero. Hence, carbon nanotubes come in three varieties: large-gap, tiny-gap, and zero gap. The $(n, n)$ tubes, also known as armchair tubes, are always metallic within the single-electron picture, independent of curvature because of their symmetry. As the tube radius $R$ increases, the band gaps of the large-gap and tiny-gap varieties decrease with a $1/R$ and $1/R^2$ dependence, respectively. Thus, for most experimentally observed carbon nanotube sizes, the gap in the tiny-gap variety which arises from curvature effects would be so small that, for most practical purposes, all the $n - m = 3j$ tubes can be considered as metallic at room temperature. Thus, in {numref}`fig-apptransport-E-2`, a $(7,1)$ tube would be metallic, whereas a $(8,0)$ tube would be semiconducting.

This band-folding picture, which was first verified by tight-binding calculations [38, 39, 40], is expected to be valid for larger diameter tubes. However, for a small radius tube, because of its curvature, strong rehybridization among the $\sigma$ and $\pi$ states can modify the electronic structure. Experimentally, nanotubes with a radius as small as 3.5 Å have been produced. *Ab initio* pseudopotential local density functional (LDA) calculations [41] indeed revealed that sufficiently strong hybridization effects can occur in small radius nanotubes which significantly alter their electronic structure. Strongly modified low-lying conduction band states are introduced into the band gap of insulating tubes because of hybridization of the $\sigma^*$ and $\pi^*$ states. As a result, the energy gaps of some small radius tubes are decreased by more than 50%. For example, the $(6,0)$ tube which is predicted to be semiconducting in the band-folding scheme is shown to be metallic. For nanotubes with diameters greater than 1 nm, these rehybridization effects are unimportant. Strong $\sigma$-$\pi$ rehybridization can also be induced by bending a nanotube [42].

Energetically, *ab initio* total energy calculations have shown that carbon nanotubes are stable down to very small diameters. {numref}`fig-apptransport-E-3` depicts the calculated strain energy per atom for different carbon nanotubes of various diameters [41]. The strain energy scales nearly perfectly as $d^{-2}$ where $d$ is the tube diameter (solid curve in {numref}`fig-apptransport-E-3`), as would be the case for rolling a classical elastic sheet. Thus, for the structural energy of the carbon nanotubes, the elasticity picture holds down to a subnanometer scale. The elastic constant may be determined from the total energy calculations. This result has been used to analyze collapsed tubes [11] and other structural properties of nanotubes. Also shown in {numref}`fig-apptransport-E-3` is the energy/atom for a $(6,0)$ carbon strip. It has an energy which is well above that of a $(6,0)$ tube because of the dangling bonds on the strip edges. Because in general the energy per atom of a strip scales as $d^{-1}$, the calculation predicts that carbon nanotubes will be stable with respect to the formation of strips down to below 4 Å in diameter, in agreement with classical force-field calculations [43].

:::{figure} images/fig-apptransport-E-3.png
:name: fig-apptransport-E-3
:width: 80%
:align: center
Fig. E.3: Strain energy/atom for carbon nanotubes from *ab initio* total energy calculations [44].
:::

There have been many experimental studies on carbon nanotubes in an attempt to understand their electronic properties. The transport experiments [19, 20, 45, 46, 47] involved both two- and four-probe measurements on a number of different tubes, including multiwalled tubes, bundles of single-walled tubes, and individual single-walled tubes. Measurements showed that there are a variety of resistivity behaviors for the different tubes, consistent with the above theoretical picture of having both semiconducting and metallic tubes. In particular, at low temperature, individual metallic tubes or small ropes of metallic tubes act like quantum wires [19, 20]. That is, the conduction appears to occur through well-separated discrete electron states that are quantum-mechanically coherent over distances exceeding many hundreds of nanometers. At sufficiently low temperature, the system behaves like an elongated quantum dot.

:::{figure} images/fig-apptransport-E-4.png
:name: fig-apptransport-E-4
:width: 80%
:align: center
Fig. E.4: Experimental set-up for the electrical measurement of a single-walled nanotube rope, visible as the diagonal curved line [20].
:::

{numref}`fig-apptransport-E-4` depicts the experimental set up for such a low temperature transport measurement on a single-walled nanotube rope from Ref. [20]. At a few degrees Kelvin, the low-bias conductance of the system is suppressed for voltages less than a few millivolts, and there are dramatic peaks in the conductance as a function of gate voltage that modulates the number of electrons in the rope. (See {numref}`fig-apptransport-E-5`.) These results have been interpreted in terms of single-electron charging and resonant tunneling through the quantized energy levels of the nanotubes. The data are explained quite well using the band structure of the conducting electrons of a metallic tube, but these electrons are confined to a small region defined either by the contacts or by the sample length, thus leading to the observed quantum confinement effects of Coulomb blockade and resonant tunneling.

:::{figure} images/fig-apptransport-E-5.png
:name: fig-apptransport-E-5
:width: 80%
:align: center
Fig. E.5: Measured conductance of a single-walled carbon nanotube rope as a function of gate voltage [20].
:::

There have also been high resolution low temperature scanning tunneling microscopy (STM) studies, which directly probe the relationship between the structural and electronic properties of the carbon nanotubes [48, 49]. {numref}`fig-apptransport-E-6` is a STM image for a single carbon nanotube at 77 K on the surface of a rope. In these measurements, the resolution of the measurements allowed for the identification of the individual carbon rings. From the orientation of the carbon rings and the diameter of the tube, the geometric structure of the tube depicted in {numref}`fig-apptransport-E-6` was deduced to be that of a $(11,2)$ tube. Measurement of the normalized conductance in the scanning tunneling spectroscopy (STS) mode was then used to obtain the local density of states (LDOS). Data on the $(11,2)$ and the $(12,3)$ nanotubes gave a constant density of states at the Fermi level, showing that they are metals as predicted by theory. On another sample, a $(14, -3)$ tube was studied. Since $14+3$ is not equal to 3 times an integer, it ought to be a semiconductor. Indeed, the STS measurement gives a band gap of 0.75 eV, in very good agreement with calculations.

:::{figure} images/fig-apptransport-E-6.png
:name: fig-apptransport-E-6
:width: 80%
:align: center
Fig. E.6: STM images at 77 K of a single-walled carbon nanotube at the surface of a rope [49].
:::

The electronic states of the carbon nanotubes, being band-folded states of graphene, lead to other interesting consequences, including a striking geometry dependence of the electric polarizability. {numref}`fig-apptransport-E-7` presents some results from a tight-binding calculation for the static polarizabilities of carbon nanotubes in a uniform applied electric field [50]. Results for 17 single-walled tubes of varying size and chirality, and hence varying band gaps, are given. The unscreened polarizability $\alpha^0$ is calculated within the random phase approximation. The cylindrical symmetry of the tubes allows the polarizability tensor to be divided into components perpendicular to the tube axis, $\alpha^0_\perp$, and a component parallel to the tube axis, $\alpha^0_\parallel$.

:::{figure} images/fig-apptransport-E-7.png
:name: fig-apptransport-E-7
:width: 90%
:align: center
Fig. E.7: Calculated static polarizability of single wall carbon nanotubes, showing results both for $\alpha^0_\perp$ vs $R^2$ on the left and $\alpha_\parallel$ vs $R/E_g^2$ on the right [50].
:::

Values for $\alpha^0_\perp$ predicted within this model are found to be totally independent of the band gap $E_g$ and to scale linearly as $R^2$, where $R$ is the tube radius. The latter dependence may be understood from classical arguments, but the former is rather unexpected. The insensitivity of $\alpha^0_\perp$ to $E_g$ results from selection rules in the dipole matrix elements between the highest occupied and the lowest unoccupied states of these tubes. On the other hand, {numref}`fig-apptransport-E-7` shows that $\alpha^0_\parallel$ is proportional to $R/E_g^2$, which is consistent with the static dielectric response of standard insulators. Also, using arguments analogous to those for C$_{60}$ [51, 52], local field effects relevant to the screened polarizability tensor $\alpha$ may be included classically, resulting in a saturation of $\alpha_\perp$ for large $\alpha^0_\perp$, but leaving $\alpha_\parallel$ unaffected. Thus, in general, the polarizability tensor of a carbon nanotube is expected to be highly anisotropic with $\alpha_\parallel \gg \alpha_\perp$. And the polarizability of small gap tubes is expected to be greatly enhanced among tubes of similar radius.

Just as for the electronic states, the phonon states in carbon nanotubes are also quantized into phonon subbands. This has led to a number of interesting phenomena [2, 3] which are discussed elsewhere in this Volume [53]. Here we mention several of them. It has been shown that twisting motions of a tube can lead to the opening up of a minuscule gap at the Fermi level, leading to the possibility of strong coupling between the electronic states and the twisting modes or twistons [54]. The heat capacity of the nanotubes is also expected to show a dimensionality dependence. Analysis [55] shows that the phonon contributions dominate the heat capacity, with single-walled carbon nanotubes having a $C_{\mathrm{ph}} \sim T$ dependence at low temperature. The temperature below which this should be observable decreases with increasing nanotube radius $R$, but the linear $T$ dependence should be accessible to experimental investigations with presently available samples. In particular, a tube with a 100 Å radius should have $C_{\mathrm{ph}} \sim T$ for $T < 7$ K. Since bulk graphite has $C_{\mathrm{ph}} \sim T^{2-3}$, a sample of sufficiently small radius tubes should show a deviation from graphitic behavior. Multi-walled tubes, on the other hand, are expected to show a range of behavior intermediate between $C_{\mathrm{ph}} \sim T$ and $C_{\mathrm{ph}} \sim T^{2-3}$, depending in detail on the tube radii and the number of concentric walls.

In addition to their fascinating electronic properties, carbon nanotubes are found to have exceptional mechanical properties [56]. Both theoretical [57, 58, 59, 60, 61, 62, 63] and experimental [64, 65] studies have demonstrated that they are the strongest known fibers. Carbon nanotubes are expected to be extremely strong along their axes because of the strength of the carbon-carbon bonds. Indeed, the Young's modulus of carbon nanotubes has been predicted and measured to be more than an order of magnitude higher than that of steel and several times that of common commercial carbon fibers. Similarly, BN nanotubes are shown [66] to be the world's strongest large-gap insulating fiber.

## E.4 Electronic and Transport Properties of On-tube Structures

In this section, we discuss the electronic properties and quantum conductance of nanotube structures that are more complex than infinitely long, perfect nanotubes. Many of these systems exhibit novel properties and some of them are potentially useful as nanoscale devices.

### E.4.1 Nanotube junctions

Since carbon nanotubes are metals or semiconductors depending sensitively on their structures, they can be used to form metal-semiconductor, semiconductor-semiconductor, or metal-metal junctions. These junctions have great potential for applications since they are of nanoscale dimensions and made entirely of a single element. In constructing this kind of on-tube junction, the key is to join two half-tubes of different helicity seamlessly with each other, without too much cost in energy or disruption in structure. It has been shown that the introduction of pentagon-heptagon pair defects into the hexagonal network of a single carbon nanotube can change the helicity of the carbon nanotube and fundamentally alter its electronic structure [16, 17, 18, 67, 68, 69, 70, 71]. This led to the prediction that these defective nanotubes behave as the desired nanoscale metal-semiconductor Schottky barriers, semiconductor heterojunctions, or metal-metal junctions with novel properties, and that they could be the building blocks of nanoscale electronic devices.

In the case of nanotubes, being one-dimensional structures, a local topological defect can change the properties of the tube at an infinitely long distance away from the defect. In particular, the chirality or helicity of a carbon nanotube can be changed by creating topological defects into the hexagonal network. The defects, however, must induce zero net curvature to prevent the tube from flaring or closing. The smallest topological defect with minimal local curvature (hence less energy cost) and zero net curvature is a pentagon-heptagon pair [16, 17, 18, 67, 68, 69, 70, 71]. Such a pentagon-heptagon defect pair with its symmetry axis nonparallel to the tube axis changes the chirality of a $(n, m)$ tube by transferring one unit from $n$ to $m$ or vice versa. If the pentagon-heptagon defect pair is along the $(n, m)$ tube axis, then one unit is added or subtracted from $m$. {numref}`fig-apptransport-E-8` depicts a $(8,0)$ carbon tube joined to a $(7,1)$ tube via a 5-7 defect pair. This system forms a quasi-1D semiconductor/metal junction, since within the band-folding picture the $(7,1)$ half tube is metallic and the $(8,0)$ half tube is semiconducting.

:::{figure} images/fig-apptransport-E-8.png
:name: fig-apptransport-E-8
:width: 80%
:align: center
Fig. E.8: Atomic structure of an $(8,0)/(7,1)$ carbon nanotube junction. The large light-gray balls denote the atoms forming the heptagon-pentagon pair [16].
:::

{numref}`fig-apptransport-E-9` and {numref}`fig-apptransport-E-10` show the calculated local density of states (LDOS) near the $(8,0)/(7,1)$ junction. These results are from a tight-binding calculation for the $\pi$ electrons [16]. In both figures, the bottom panel depicts the density of states of the perfect tube, with the sharp features corresponding to the van Hove singularities of a quasi-1D system. The other panels show the calculated LDOS at different distances away from the interface, with cell 1 being the closest to the interface in the semiconductor side and ring 1 the closest to the interface in the metal side. Here, cell refers to one unit cell of the tube and "ring" refers to a ring of atoms around the circumference. These results illustrate the spatial behavior of the density of states as it transforms from that of a metal to that of a semiconductor across the junction. The LDOS very quickly changes from that of the metal to that of the semiconductor within a few rings of atoms as one goes from the metal side to the semiconductor side. As the interface is approached, the sharp van Hove singularities of the metal are diluted. Immediately on the semiconductor side of the interface, a different set of singular features, corresponding to those of the semiconductor tube, emerges. There is, however, still a finite density of states in the otherwise bandgap region on the semiconductor side. These are metal induced gap states [72], which decay to zero in about a few Å into the semiconductor. Thus, the electronic structure of this junction is very similar to that of a bulk metal-semiconductor junction, such as Al/Si, except it has a nanometer cross-section and is made out of entirely the element carbon.

:::{figure} images/fig-apptransport-E-9.png
:name: fig-apptransport-E-9
:width: 80%
:align: center
Fig. E.9: Calculated LDOS of the $(8,0)/(7,1)$ metal-semiconductor junction at the semiconductor side. From top to bottom, LDOS at cells 1, 2, and 3 of the $(8,0)$ side. Cell 1 is at the interface [16].
:::

:::{figure} images/fig-apptransport-E-10.png
:name: fig-apptransport-E-10
:width: 80%
:align: center
Fig. E.10: Calculated LDOS of the $(8,0)/(7,1)$ metal-semiconductor junction at the metal side. From top to bottom, the LDOS at rings 1, 2, and 3 of the $(7,1)$ side. Ring 1 is at the interface [16].
:::

Similarly, semiconductor-semiconductor and metal-metal junctions may be constructed with the proper choices of tube diameters and pentagon-heptagon defect pairs. For example, by inserting a 5-7 pair defect, a $(10,0)$ carbon nanotube can be matched to a $(9,1)$ carbon nanotube [16]. Both of these tubes are semiconductors, but they have different bandgaps. The $(10,0)/(9,1)$ junction thus has the electronic structure of a semiconductor heterojunction. In this case, owing to the rather large structural distortion at the interface, there are interesting localized interface states at the junction. Theoretical studies have also been carried out for junctions of B-C-N nanotubes [73], showing very similar behaviors as the carbon case, and for other geometric arrangements, such as carbon nanotube T-junctions, where one tube joins to the side of another tube perpendicularly to form a "T" structure [74].

Calculations have been carried out to study the quantum conductance of the carbon nanotube junctions. Typically these calculations are done within the Landauer formalism [75, 76]. In this approach, the conductance is given in terms of the transmission matrix of the propagating electron waves at a given energy. In particular, the conductance of metal-metal nanotube junctions is shown to exhibit a quite interesting new effect which does not have an analog in bulk metal junctions [67]. It is found that certain configurations of pentagon-heptagon pair defects in forming the junction completely stop the flow of electrons, while other arrangements permit the transmission of current through the junction. Such metal-metal junctions thus have the potential for use as nanoscale electrical switches. This phenomenon is seen in the calculated conductance of a $(12,0)/(6,6)$ carbon nanotube junction in {numref}`fig-apptransport-E-11`. Both the $(12,0)$ and $(6,6)$ tubes are metallic within the tight-binding model, and they can be matched perfectly to form a straight junction. However, the conductance is zero for electrons at the Fermi level, $E_F$. This peculiar effect is not due to a lack of density of states at $E_F$. As shown in {numref}`fig-apptransport-E-11`, there is finite density of states at $E_F$ everywhere along the whole length of the total system for this junction. The absence of conductance arises from the fact that there is discrete rotational symmetry along the axis of the combined tube. But, for electrons near $E_F$, the states in one of the half tubes are of a different rotational symmetry from those in the other half tube. As an electron propagates from one side to the other, the electron encounters a symmetry gap and is completely reflected at the junction.

:::{figure} images/fig-apptransport-E-11.png
:name: fig-apptransport-E-11
:width: 90%
:align: center
Fig. E.11: Calculated results for the $(12,0)/(6,6)$ metal-metal junction. Top: conductance of a matched tube (solid line), a perfect $(12,0)$ tube (dashed line), and a perfect $(6,6)$ tube (dotted line). Center: LDOS at the interface on the $(12,0)$ side (full line) and of the perfect $(12,0)$ tube (dotted line). Bottom: LDOS at the interface on the $(6,6)$ side (full line) and of the perfect $(6,6)$ tube (dashed line) [67].
:::

The same phenomenon occurs in the calculated conductance of a $(9,0)/(6,3)$ metal-metal carbon nanotube junction. However, in forming this junction, there are two distinct ways to match the two halves, either symmetrically or asymmetrically. In the symmetric matched geometry, the conductance is zero at $E_F$ for the same symmetry reason as discussed above. (See {numref}`fig-apptransport-E-12`.) But, in the asymmetric matched geometry, the discrete rotational symmetry of the total system is broken and the electrons no longer have to preserve their rotational quantum number as they travel across the junction. The conductance for this case is now nonzero. Consequently, in some situations, bent junctions can conduct better than straight junctions for the nanotubes. This leads to the possibility of using these metal-metal or other similar junctions as nanoswitches or strain gauges, i.e., one can imagine using some symmetry breaking mechanisms such as electron-photon, electron-phonon or mechanical deformation to switch a junction from a non-conducting state to a conducting state [67].

:::{figure} images/fig-apptransport-E-12.png
:name: fig-apptransport-E-12
:width: 80%
:align: center
Fig. E.12: Calculated conductance of the $(9,0)/(6,3)$ junction -- matched system (solid line), perfect $(6,3)$ tube (dotted line), and perfect $(9,0)$ tube (dashed line) [67].
:::

Junctions of the kind discussed above may be formed during growth, but they can also be generated by mechanical stress [77]. There is now considerable experimental evidence of this kind of on-tube junction and device behavior predicted by theory. An experimental signature of a single pentagon-heptagon pair defect would be an abrupt bend between two straight sections of a nanotube. Calculations indicate that a single pentagon-heptagon pair would induce bend angles of roughly 0-15 degrees, with the exact value depending on the particular tubes involved. Several experiments have reported sightings of localized bends of this magnitude for multiwalled carbon nanotubes [23, 78, 79]. Having several 5-7 defect pairs at a junction would allow the joining of tubes of different diameters and add complexity to the geometry. The first observation of nonlinear junction-like transport behavior was made on a rope of SWNTs [22], where the current-voltage properties were measured along a rope of single-walled carbon nanotubes using a scanning tunneling microscopy tip and the behavior shown in {numref}`fig-apptransport-E-13` was found in some samples. At one end of the tube, the system behaves like a semimetal showing a typical $I$-$V$ curve of metallic tunneling, but after some distance at the other end it becomes a rectifier, presumably because a defect of the above type has been introduced at some point on the tube. A more direct measurement was carried out recently [23]. A kinked single-walled nanotube lying on several electrodes was identified and its electrical properties in the different segments were measured. The kink was indicative of two half tubes of different chiralities joined by a pentagon-heptagon defect pair. {numref}`fig-apptransport-E-14` shows the measured $I$-$V$ characteristics of a kinked nanotube. The inset is the $I$-$V$ curve for the upper segment showing that this part of the tube is a metal; but the $I$-$V$ curve across the kink shows a rectifying behavior indicative of a metal-semiconductor junction.

:::{figure} images/fig-apptransport-E-13.png
:name: fig-apptransport-E-13
:width: 55%
:align: center
Fig. E.13: Current-voltage characteristic measured along a rope of single-walled carbon nanotubes. Panels A, B, C, and D correspond to successive different locations on the rope [22].
:::

:::{figure} images/fig-apptransport-E-14.png
:name: fig-apptransport-E-14
:width: 70%
:align: center
Fig. E.14: Measured current-voltage characteristic of a kinked single-walled carbon nanotube [23].
:::

### E.4.2 Impurities, Stone–Wales defects, and structural deformations in metallic nanotubes

An unanswered question in the field has been why do the metallic carbon nanotubes have such long mean free paths. This has led to consideration of the effects of impurities and defects on the conductance of the metallic nanotubes. We focus here on the $(10,10)$ tubes; however, the basic physics is the same for all $(n, n)$ tubes. In addition to tight-binding studies, there are now first-principles calculations on the quantum conductance of nanotube structures based on an *ab initio* pseudopotential density functional method with a wavefunction matching technique [80, 81]. The advantages of the *ab initio* approach are that one can obtain the self-consistent electronic and geometric structure in the presence of the defects and, in addition to the conductance, obtain detailed information on the electronic wavefunction and current density distribution near the defect.

Several rather surprising results have been found concerning the effects of local defects on the quantum conductance of the $(n, n)$ metallic carbon nanotubes [81]. For example, the maximum reduction in the conductance due to a local defect is itself often quantized, and this can be explained in terms of resonant backscattering by quasi-bound states of the defect. Here we discuss results for three simple defects: boron and nitrogen substitutional impurities and the bond rotation or Stone–Wales defect. A Stone–Wales defect corresponds to the rotation of one of the bonds in the hexagonal network by 90 degrees, resulting in the creation of a quite low energy double 5-7 defect pair, without changing the overall helicity of the tube.

{numref}`fig-apptransport-E-15` depicts several results for a $(10,10)$ carbon nanotube with a single boron substitutional impurity. The top panel is the calculated conductance as a function of the energy of the electron. For a perfect tube, the conductance (indicated here by the dashed line) is 2 in units of the quantum of conductance, $2e^2/h$, since there are two conductance channels available for the electrons near the Fermi energy. For the result with the boron impurity, a striking feature is that the conductance is virtually unchanged at the Fermi level of the neutral nanotube. That is, the impurity potential does not scatter incoming electrons of this energy. On the other hand, there are two dips in the conductance below $E_F$. The amount of the reduction at the upper dip is one quantum unit of conductance and its shape is approximately Lorentzian. In fact, the overall structure of the conductance is well described by the superposition of two Lorentzian dips, each with a depth of 1 conductance quantum. These two dips can be understood in terms of a reduction in conductance due to resonant backscattering from quasi-bound impurity states derived from the boron impurity. The calculated results thus show that boron behaves like an acceptor with respect to the first lower subband (i.e., the first subband with energy below the conduction states) and forms two impurity levels that are split off from the top of the first lower subband. These impurity states become resonance states or quasi-bound states due to interaction with the conduction states. The impurity states can be clearly seen in the calculated LDOS near the boron impurity (middle panel of {numref}`fig-apptransport-E-15`). The two extra peaks correspond to the two quasi-bound states. The LDOS would be a constant for a perfect tube in the region between the van Hove singularity of the first lower subband and that of the first upper subband. Because a $(n, n)$ tube with a substitutional impurity still has a mirror plane perpendicular to the tube axis, the defect states have definite parity with respect to this plane. The upper energy state (broader peak) in {numref}`fig-apptransport-E-15` has even parity and the lower energy state (narrower peak) has odd parity, corresponding to s-like and p-like impurity states, respectively.

:::{figure} images/fig-apptransport-E-15.png
:name: fig-apptransport-E-15
:width: 80%
:align: center
Fig. E.15: Energy dependence of the calculated conductance, local density of states, and phase shifts of a $(10,10)$ carbon nanotube with a substitutional boron impurity [81].
:::

The conductance behavior in {numref}`fig-apptransport-E-15` may be understood by examining how electrons in the two eigen-channels interact with the impurity. At the upper dip, an electron in one of the two eigen-channels is reflected completely (99.9%) by the boron impurity, but an electron in the other channel passes by the impurity with negligible reflection (0.1%). The same happens at the lower dip but with the behavior of the two eigen-channels switched. The bottom panel shows the calculated scattering phase shifts. The phase shift of the odd parity state changes rapidly as the energy sweeps past the lower quasi-bound state level, with its value passing through $\pi/2$ at the peak position of the quasi-bound state. The same change occurs to the phase shift of the even parity state at the upper impurity-state energy. The total phase shift across a quasi-bound level is $\pi$ in each case, in agreement with the Friedel sum rule. The picture is that an incoming electron with energy exactly in resonance with the impurity state is being scattered back totally in one of the channels but not the other. This explains the exact reduction of one quantum of conductance at the dip. The upper-energy impurity state has a large binding energy (over 0.1 eV) with respect to the first lower subband and hence is quite localized. It has an approximate extent of $\sim 10$ Å, whereas the lower impurity state has an extent of $\sim 250$ Å.

The results for a nitrogen substitutional impurity on the $(10,10)$ tube are presented in {numref}`fig-apptransport-E-16`. Nitrogen has similar effects on the conductance as boron, but with opposite energy structures. Again, the conductance at the Fermi level is virtually unaffected, but there are two conductance dips above the Fermi level just below the first upper subband. Thus, the nitrogen impurity behaves like a donor with respect to the first upper subband, forming an s-like quasi-bound state with stronger binding energy and a p-like state with weaker binding energy. As in the case of boron, the reduction of one quantum unit of conductance at the dips is caused by the fact that, at resonance, the electron in one of the eigen channels is reflected almost completely by the nitrogen impurity but the electron in the other channel passes by the impurity with negligible reflection. The LDOS near the nitrogen impurity shows two peaks corresponding to the two quasi-bound states. The phase shifts of the two eigen channels show similar behavior as in the boron case.

:::{figure} images/fig-apptransport-E-16.png
:name: fig-apptransport-E-16
:width: 80%
:align: center
Fig. E.16: Calculated conductance, local density of states and phase shifts of a $(10,10)$ carbon nanotube with a substitutional nitrogen impurity [81].
:::

For a $(10,10)$ tube with a Stone–Wales or double 5-7 pair defect, the calculations also find that the conductance is virtually unchanged for the states at the Fermi energy. Thus these results show that the transport properties of the neutral $(n, n)$ metallic carbon nanotube are very robust with respect to these kinds of intra-tube local defects. As in the impurity case, there are two dips in the quantum conductance in the conduction band energy range, one above and one below the Fermi level. These are again due to the existence of defect levels, and the reduction at the two dips is very close to one quantum of conductance for the same reason, as discussed above. The symmetry of the Stone–Wales defect in this case does not cause mixing between the $\pi$ and $\pi^*$ bands, and these two bands remain as eigen channels in the defective system. The lower dip is due to a complete reflection of the $\pi^*$ band and the upper dip is due to complete reflection of the $\pi$ band. This implies that the conductance of the nanotube, when there are more than one double 5-7 pair defect, would not sensitively depend on their relative positions, but only on their total numbers, as long as the distance between defects is far enough to be able to neglect inter-defect interactions. The analysis of the phase shifts show that the lower quasi-bound state is even with respect to a mirror plane perpendicular to the tube axis, while the upper quasi-bound state is odd with respect to the same plane. ({numref}`fig-apptransport-E-17`.)

:::{figure} images/fig-apptransport-E-17.png
:name: fig-apptransport-E-17
:width: 80%
:align: center
Fig. E.17: Energy dependence of the calculated conductance, local density of states, and phase shifts of a $(10,10)$ carbon nanotube with a Stone–Wales defect [81].
:::

The conductance of nanotubes can also be affected by structural deformations. Two types of deformations involving bending or twisting the nanotube structure have been considered in the literature. It was found that a smooth bending of the nanotube does not lead to scattering [54], but formation of a local kink induces strong $\sigma$-$\pi$ mixing and backscattering similar to that discussed earlier for boron impurity [82]. Twisting has a much stronger effect [54]. A metallic armchair $(n, n)$ nanotube upon twisting develops a band-gap which scales linearly with the twisting angle up to the critical angle at which the tube collapses.

## E.5 Nanotube Ropes, Crossed-Tube Junctions, and Effects of Long-Range Perturbations

### E.5.1 Ropes of nanotubes

Another interesting carbon nanotube system is that of ropes of single-walled carbon nanotubes which have been synthesized in high yield [8]. These ropes, containing up to tens to hundreds of single-walled nanotubes in a close-packed triangular lattice, are made up of tubes of nearly uniform diameter, close to that of the $(10,10)$ tubes (see {numref}`fig-apptransport-E-18`.) Because of the rather weak interaction between these tubes, a naive picture would be that the packing of individual metallic nanotubes into ropes would not change their electronic properties significantly. Theoretical studies [83, 84, 85] however showed that this is not the case for a rope of $(10,10)$ carbon nanotubes. A broken symmetry of the $(10,10)$ nanotube caused by interactions between tubes in a rope induces formation of a pseudogap in the density of states of about 0.1 eV. The existence of this pseudogap alters many of the fundamental electronic properties of the rope.

:::{figure} images/fig-apptransport-E-18.png
:name: fig-apptransport-E-18
:width: 80%
:align: center
Fig. E.18: Perspective view of a model of a rope of $(10,10)$ carbon nanotubes into a ribbon [82].
:::

As discussed above, an isolated $(n, n)$ carbon nanotube has two linearly dispersing conduction bands which cross at the Fermi level forming two "Dirac" points, as schematically presented in {numref}`fig-apptransport-E-19` (a). This linear band dispersion in a one-dimensional system gives rise to a finite and constant density of electronic states at the Fermi energy. Thus, an $(n, n)$ tube is a metal within the one-electron picture. The question of interest is: How does the electronic structure change when the metallic tubes are bundled up to form a closely packed two-dimensional crystal, as in the case of the $(10,10)$ ropes. In the calculation, a large $(10,10)$ rope is modeled by a triangular lattice of $(10,10)$ tubes infinitely extended in the lateral directions. For such a system, the electronic states, instead of being contained in the 1-D Brillouin zone of a single tube, are now extended to a three-dimensional irreducible Brillouin zone wedge. If tube-tube interactions are negligibly small, the electronic energy band structure along any line in the wedge parallel to the rope axis would be exactly the same as the band dispersion of an isolated tube. In particular, at the $k$-wavevector corresponding to the band crossing point, there will be a two-fold degenerate state at the Fermi energy. This allowed band crossing is due to the mirror symmetry of the $(10,10)$ tube. For a tube in a rope, this symmetry is however broken because of intertube interactions. The broken symmetry causes a quantum level repulsion and opens up a gap almost everywhere in the Brillouin zone, as schematically shown in {numref}`fig-apptransport-E-19` (b).

:::{figure} images/fig-apptransport-E-19.png
:name: fig-apptransport-E-19
:width: 80%
:align: center
Fig. E.19: Band crossing and band repulsion. (a) Schematic band structure of an isolated $(n, n)$ carbon nanotube near the Fermi energy. (b) Repulsion of bands due to the breaking of mirror symmetry.
:::

The band repulsion resulting from the broken-symmetry strongly modifies the density of states (DOS) of the rope near the Fermi energy compared to that of an isolated $(10,10)$ tube. The calculated DOS is presented in {numref}`fig-apptransport-E-20` (a). Shown are the results for two cases: aligned and misaligned tubes in the rope. In both cases, there is a pseudogap of the order of 0.1 eV in the density of states. Examination of the electronic structure reveals that the system is a semimetal with both electron and hole carriers. The existence of the pseudogap in the rope makes the conductivity and other transport properties of the metallic rope significantly different from those of isolated tubes, even without considering the effect of local disorder in low dimensions. Since the DOS increases rapidly away from the Fermi level, the carrier density of the rope is sensitive to temperature and doping. The existence of both electron and hole carriers leads to qualitatively different thermopower and Hall-effect behaviors from those expected for a normal metal. The optical properties of the rope are also affected by the pseudogap. As illustrated by the calculated joint density of states (JDOS) in {numref}`fig-apptransport-E-20` (b), there would be a finite onset in the infrared absorption spectrum for a large perfectly ordered $(10,10)$ rope, where one can assume $k$-conserving optical transitions. In the case of high disorder, an infrared experiment would more closely reflect the DOS rather than the JDOS. For most actual samples, the fraction of $(10,10)$ carbon nanotubes (compared with other nanotubes of the same diameter) in the experimentally synthesized ropes appears to be small. However, the conclusion that broken symmetry induces a gap in the $(n, n)$ tubes is a general result which is of relevance for tubes under any significant asymmetric perturbations, such as those due to structural deformations or external fields.

:::{figure} images/fig-apptransport-E-20.png
:name: fig-apptransport-E-20
:width: 90%
:align: center
Fig. E.20: (a) Calculated density of states for a rope of misaligned $(10,10)$ carbon nanotubes (broken line) and aligned tubes (solid line). The Fermi energy is at zero. (b) Calculated joint density of states for a rope of misaligned (broken line) and aligned (solid line) $(10,10)$ tubes. Results are in units of states per meV per atom [83, 84].
:::

### E.5.2 Crossed-tube junctions

The discussion of nanotube junctions in the previous section is focused on the on-tube junctions, i.e., forming a junction by joining two half tubes together. These systems are extremely interesting, but difficult to synthesize in a controlled manner at this time. Another way to form junctions is to have two tubes crossing each other in contact [86]. (See {numref}`fig-apptransport-E-21`.) This kind of crossed-tube junction is much easier to fabricate and control with present experimental techniques. When two nanotubes cross in free space, one expects that the tubes at their closest contact point will be at a van der Waals distance away from each other and that there will not be much intertube or junction conductance. However, as shown by Avouris and coworkers [87], for two crossed tubes lying on a substrate, there is a substantial force pressing one tube against the other due to the substrate attraction. For a crossed-tube junction composed of SWNTs with the experimental diameter of 1.4 nm, this contact force has been estimated to be about 5 nN [87]. This substrate force would then be sufficient to deform the crossed-tube junction and lead to better junction conductance.

:::{figure} images/fig-apptransport-E-21.png
:name: fig-apptransport-E-21
:width: 90%
:align: center
Fig. E.21: AFM image of a crossed SWNT device (A). Calculated structure of a crossed $(5,5)$ SWNT junction with a force of 0 nN (B) and 15 nN (C) [86].
:::

In {numref}`fig-apptransport-E-21`, panel A is an AFM image of a crossed-tube junction fabricated from two single-walled carbon nanotubes of 1.4 nm in diameter with electrical contacts at each end [86]. Panels B and C show the calculated structure corresponding to a $(5,5)$ carbon nanotube pressed against another one with zero and 15 nN force, respectively. Because of the smaller diameter of the $(5,5)$ tube, a larger contact force is required to produce a deformation similar to that of the experimental crossed-tube junction. The calculation was done using the *ab initio* pseudopotential density functional method with a localized basis [86]. As seen in panel C, there is considerable deformation, and the atoms on the different tubes are much closer to each other. At this distance, the closest atomic separation between the two tubes is 0.25 nm, significantly smaller than the van der Waals distance of 0.34 nm.

For the case of zero contact force (panel B in {numref}`fig-apptransport-E-21`), the calculated intra-tube conductance is virtually unchanged from that of an ideal, isolated metallic tube, and the intertube conductance is negligibly small. However, when the tubes are under a force of 15 nN, there is a sizable intertube or junction conductance. As shown in {numref}`fig-apptransport-E-22`, the junction conductance at the Fermi energy is about 5% of a quantum unit of conductance $G_0 = 2e^2/h$. The junction conductance is thus very sensitive to the force or distance between the tubes.

:::{figure} images/fig-apptransport-E-22.png
:name: fig-apptransport-E-22
:width: 80%
:align: center
Fig. E.22: Calculated conductance (expressed in units of $e^2/h$) of a crossed $(5,5)$ carbon nanotube junction with a contact force of 15 nN on a linear (top) and log (bottom) scale. The dashed (dotted-dashed) curve corresponds to the intra-tube (intertube) conductance [86].
:::

Experimentally, the conductance of various types of crossed carbon nanotube junctions has been measured, including metal-metal, semiconductor-semiconductor, and metal-semiconductor crossed-tube junctions. The experimental results are presented in {numref}`fig-apptransport-E-23`. For the metal-metal crossed-tube junctions, a conductance of 2 to 6% of $G_0$ is found, in good agreement with the theoretical results. Of particular interest is the metal-semiconductor case in which experiments demonstrated Schottky diode behavior with a Schottky barrier in the range of 200–300 meV, which is very close to the value of 250 meV expected from theory for nanotubes with diameters of 1.4 nm [86].

:::{figure} images/fig-apptransport-E-23.png
:name: fig-apptransport-E-23
:width: 80%
:align: center
Fig. E.23: Current-voltage characteristics of several crossed SWNT junctions [86] (see text).
:::

### E.5.3 Effects of Long-Range Disorder and External Perturbations

The effects of disorder on the conducting properties of metal and semiconducting carbon nanotubes are quite different. Experimentally, the mean free path is found to be much longer in metallic tubes than in doped semiconducting tubes [19, 20, 21, 24, 88]. This result can be understood theoretically if the disorder potential is long range. As discussed below, the internal structure of the wavefunction of the states connected to the sublattice structure of graphite lead to a suppression of scattering in metallic tubes, but not in semiconducting tubes. {numref}`fig-apptransport-E-24` shows the measured conductance for a semiconducting nanotube device as a function of gate voltage at different temperatures [88]. The diameter of the tube as measured by AFM is 1.5 nm, consistent with a single-walled tube. The complex structure in the Coulomb blockade oscillations in {numref}`fig-apptransport-E-24` is consistent with transport through a number of quantum dots in series. The temperature dependence and typical charging energy indicates that the tube is broken up into segments of length of about 100 nm. Similar measurements on intrinsic metal tubes, on the other hand, yield lengths that are typically a couple of orders of magnitude longer [19, 20, 21, 24, 88].

:::{figure} images/fig-apptransport-E-24.png
:name: fig-apptransport-E-24
:width: 80%
:align: center
Fig. E.24: Conductance vs. gate voltage $V_g$ for a semiconducting single-walled carbon nanotube at various temperatures. The upper insert schematically illustrates the sample geometry and the lower insert shows $dI/dV$ vs. $V$ and $V_g$ plotted as a gray scale [88].
:::

Theoretical calculations have been carried out to examine the effects of long-range external perturbations [88]. In the calculation, to model the perturbation, a 3-dimensional Gaussian potential of a certain width is centered on one of the atoms on the carbon nanotube wall. The conductance with the perturbation is computed for different Gaussian widths, but keeping the integrated strength of the potential the same. Some typical tight-binding results are presented in {numref}`fig-apptransport-E-25`. The solid lines show the results for the conductance of a disorder-free tube, while the dashed and the dot-dashed lines are, respectively, for a single long-range ($\sigma = 0.348$ nm, $\Delta V = 0.5$ eV) and a short-range ($\sigma = 0.116$ nm, $\Delta V = 10$ eV) scatterer. Here $\Delta V$ is the shift in the on-site energy at the potential center. The conduction bands (i.e., bands crossing the Fermi level) of the metallic tube are unaffected by the long-range scatterer, unlike the lower and upper subbands of both the metallic and semiconducting tubes, which are affected by both long- and short-range scatterers. All subbands are influenced by the short-range scatterer. The inset shows an expanded view of the onset of conduction in the semiconducting tube at positive $E$, with each division corresponding to 1 meV. Also, the sharp step edges in the calculated conductance of the perfect tubes are rounded off by both types of perturbations.

:::{figure} images/fig-apptransport-E-25.png
:name: fig-apptransport-E-25
:width: 90%
:align: center
Fig. E.25: Tight-binding calculation of the conductance of a (a) metallic $(10,10)$ tube and (b) semiconducting $(17,0)$ tube in the presence of a Gaussian scatterer. The energy scale on the abscissa is 0.2 eV per division in each graph [88].
:::

Both the experimental and theoretical findings strongly suggest that long-range scattering is suppressed in the metallic tubes. One can actually understand this qualitatively from the electronic structure of a graphene sheet [89, 90]. The graphene structure has two atoms per unit cell. The properties of electrons near the Fermi energy are given by those states near the corner of the Brillouin zone. (See {numref}`fig-apptransport-E-26`.) If we look at the states near this point and consider them in terms of a $k$-vector away from the corner $K$ point, then they can be described by a Dirac Hamiltonian. For these states, the wavefunctions can be written in terms of a product of a plane wave component (with a vector $k$) and a pseudo-spin which describes the bonding character between the two atoms in the unit cell. The interesting result is that this pseudo-spin points along $k$. For example, if the state at $k$ is bonding, then the state at $-k$ is antibonding in character. Within this framework, one can work out the scattering between the allowed states in a carbon nanotube due to long-range disorder, i.e., disorder with Fourier components $V(q)$ such that $q \ll K$. This, for example, will be the case for scattering by charged trap states in the substrate (oxide traps). In this case, the disorder does not couple to the pseudo-spin portion of the wavefunction, since the disorder potential is approximately constant on the scale of the interatomic distance. The resulting matrix element between states is then [89, 90]:

$$
|\langle k'|V(r)|k\rangle|^2 = |V(k-k')|^2 \cos^2\left[\frac{1}{2}\theta_{k,k'}\right],
$$

where $\theta_{k,k'}$ is the angle between the initial and final states. The first term in $V(k-k')$ is the Fourier component at the difference in $k$ values of the initial and final envelope wavefunctions. The cosine term is the overlap of the initial and final spinor states.

:::{figure} images/fig-apptransport-E-26.png
:name: fig-apptransport-E-26
:width: 90%
:align: center
Fig. E.26: (a) Filled states (shaded) in the first Brillouin zone of a p-type graphene sheet. There are two carbon atoms per unit cell (lower right inset). The dispersions of the states near $E_F$ are cones whose vertices are located at the corner points of the Brillouin zone. The Fermi circle, defining the allowed $k$ vectors, and the band dispersions are shown in (b) and (c) for a metallic and a semiconducting tube, respectively [88].
:::

For a metallic tube [{numref}`fig-apptransport-E-26` (b)], backscattering in the conduction band corresponds to scattering between $k$ and $-k$. Such scattering is forbidden, because the molecular orbitals of these two states are orthogonal. In semiconducting tubes, however, the situation is quite different [{numref}`fig-apptransport-E-26` (c)]. The angle between the initial and final states is less than $\pi$, and scattering is thus only partially suppressed by the spinor overlap. As a result, semiconducting tubes should be sensitive to long-range disorder, while metallic tubes should not. However, short-range disorder which has Fourier components $q \sim K$ will couple the molecular orbitals together and lead to scattering in all of the subbands. These theoretical considerations agree well with experiment and with the detailed calculations discussed above. Long-range disorder due to, e.g., localized charges near the tube, breaks the semiconducting tube into a series of quantum dots with large barriers, resulting in a dramatically reduced conductance and a short mean free path. On the other hand, metallic tubes are insensitive to this disorder and remain near-perfect 1D conductors.

## E.6 Summary

This Chapter gives a short review of some of our theoretical understanding of the structural and electronic properties of single-walled carbon nanotubes and of various structures formed from these nanotubes. Because of their nanometer dimensions, the nanotube structures can have novel properties and yield unusual scientific phenomena. In addition to the multi-walled carbon nanotubes, single-walled nanotubes, nanotube ropes, nanotube junctions, and non-carbon nanotubes have been synthesized.

These quasi-one-dimensional objects have highly unusual electronic properties. For the perfect tubes, theoretical studies have shown that the electronic properties of the carbon nanotubes are intimately connected to their structure. They can be metallic or semiconducting, depending sensitively on tube diameter and chirality. Experimental studies using transport, scanning tunneling, and other techniques have basically confirmed the theoretical predictions. The dielectric responses of the carbon nanotubes are found to be highly anisotropic in general. The heat capacity of single-wall nanotubes is predicted to have a characteristic linear $T$ dependence at low temperature.

On-tube metal-semiconductor, semiconductor-semiconductor, and metal-metal junctions may be formed by introducing topological structural defects, and these junctions have been shown to behave like nanoscale device elements. For example, different half-tubes may be joined with 5-member ring/7-member ring pair defects to form a metal-semiconductor Schottky barrier. The calculated electronic structure of these junctions is very similar to that of standard metal-semiconductor interfaces, and in this sense, they are molecular level devices composed of the single element, carbon. Recent experimental measurements have confirmed the existence of such Schottky barrier behavior in nanotube ropes and across kinked nanotube junctions. Similarly, 5-7 defect pairs in different carbon and non-carbon nanotubes can produce semiconductor-semiconductor and metal-metal junctions. The existence of metal-metal nanotube junctions in which the conductance is suppressed for symmetry reasons has also been predicted. Thus, the carbon nanotube junctions may be used as nanoscale electronic elements.

The influence of impurities and local structural defects on the conductance of carbon nanotubes has also been examined. It is found that local defects in general form well defined quasi-bound states even in metallic nanotubes. These defect states give rise to peaks in the LDOS and reduce the conductance at the energy of the defect levels by a quantum unit of conductance via resonant backscattering. The theoretical studies show that, owing to the unique electronic structure of the graphene sheet, the transport properties of $(n, n)$ metallic tubes appear to be very robust against defects and long-range perturbations near $E_F$. Doped semiconducting tubes are much more susceptible to long-range disorder. These results explain the experimental findings of the long coherence length in metallic tubes and the large difference in mean free path between the metallic and doped semiconducting tubes. For nanotube ropes, intertube interactions are shown to alter the electronic structure of $(n, n)$ metallic tubes because of broken symmetry effects, leading to a pseudogap in the density of states and to semimetallic behavior. Crossed-tube junctions have also been fabricated experimentally and studied theoretically. These systems show significant intertube conductance for metal-metal junctions and exhibit Schottky behavior for metal-semiconductor junctions when the tubes are subjected to contact force from the substrate.

The carbon nanotubes are hence a fascinating new class of materials with many unique and desirable properties. The rich interplay between the geometric and electronic structure of the nanotubes has given rise to many interesting, new physical phenomena. At the practical level, these systems have the potential for many possible applications.

## Bibliography

[1] S. Iijima, Nature (London) 354, 56 (1991).

[2] M. S. Dresselhaus, G. Dresselhaus, and P. C. Eklund, *Science of Fullerenes and Carbon Nanotubes* (Academic Press, New York, NY, 1996).

[3] P. M. Ajayan and T. W. Ebbesen, Rep. Prog. Phys. 60, 1025 (1997).

[4] C. Dekker, Phys. Today 52, 22 (1999).

[5] S. Iijima and T. Ichihashi, Nature (London) 363, 603 (1993).

[6] D. S. Bethune, C. H. Kiang, M. S. de Vries, G. Gorman, R. Savoy, J. Vazquez, and R. Beyers, Nature (London) 363, 605 (1993).

[7] P. M. Ajayan, J. M. Lambert, P. Bernier, L. Barbedette, C. Colliex, and J. M. Planeix, Chem. Phys. Lett. 215, 509 (1993).

[8] T. Guo, C.-M. Jin, and R. E. Smalley, Chem. Phys. Lett. 243, 49–54 (1995).

[9] M. R. Pederson and J. Q. Broughton, Phys. Rev. Lett. 69, 2689 (1992).

[10] P. M. Ajayan and S. Iijima, Nature (London) 361, 333 (1993).

[11] N. G. Chopra, L. X. Benedict, V. H. Crespi, M. L. Cohen, S. G. Louie, and A. Zettl, Nature (London) 377, 135 (1995).

[12] H. Dai, E. W. Wong, and C. M. Lieber, Nature (London) 384, 147 (1996).

[13] W. A. de Heer, A. Châtelain, and D. Ugarte, Science 270, 1179 (1995). see also ibid page 1119.

[14] A. G. Rinzler, J. H. Hafner, P. Nikolaev, L. Lou, S. G. Kim, D. Tománek, P. Nordlander, D. T. Colbert, and R. E. Smalley, Science 269, 1550 (1995).

[15] A. C. Dillon, K. M. Jones, T. A. Bekkedahl, C. H. Kiang, D. S. Bethune, and M. J. Heben, Nature (London) 386, 377–379 (1997).

[16] L. Chico, V. H. Crespi, L. X. Benedict, S. G. Louie, and M. L. Cohen, Phys. Rev. Lett. 76, 971–974 (1996).

[17] Ph. Lambin, A. Fonseca, J. P. Vigneron, J. B. Nagy, and A. A. Lucas, Chem. Phys. Lett. 245, 85–89 (1995).

[18] R. Saito, G. Dresselhaus, and M. S. Dresselhaus, Phys. Rev. B 53, 2044–2050 (1996).

[19] S. J. Tans, M. H. Devoret, H. Dai, A. Thess, R. E. Smalley, L. J. Geerligs, and C. Dekker, Nature (London) 386, 474–477 (1997).

[20] M. Bockrath, D. H. Cobden, P. L. McEuen, N. G. Chopra, A. Zettl, A. Thess, and R. E. Smalley, Science 275, 1922–1924 (1997).

[21] R. Martel, T. Schmidt, H. R. Shea, T. Hertel, and Ph. Avouris, Appl. Phys. Lett. 73, 2447 (1998).

[22] P. G. Collins, A. Zettl, H. Bando, A. Thess, and R. E. Smalley, Science 278, 5335 (1997).

[23] Zhen Yao, H. W. C. Postma, L. Balents, and C. Dekker, Nature (London) 402, 273 (1999).

[24] S. J. Tans, R. M. Verschueren, and C. Dekker, Nature 393, 49–52 (1998).

[25] X. Blase, A. Rubio, S. G. Louie, and M. L. Cohen, Europhys. Lett. 28, 335 (1994).

[26] Y. Miyamoto, A. Rubio, M. L. Cohen, and S. G. Louie, Phys. Rev. B 50, 18360 (1994).

[27] Y. Miyamoto, A. Rubio, S. G. Louie, and M. L. Cohen, Phys. Rev. B 50, 4976 (1994).

[28] X. Blase, A. Rubio, S. G. Louie, and M. L. Cohen, Phys. Rev. B 51, 6868 (1995).

[29] Y. Miyamoto, M. L. Cohen, and S. G. Louie, Solid State Comm. 102, 605 (1997).

[30] Z. Weng-Sieh, K. Cherrey, N. G. Chopra, X. Blase, Y. Miyamoto, A. Rubio, M. L. Cohen, S. G. Louie, A. Zettl, and R. Gronsky, Phys. Rev. B 51, 11229 (1995).

[31] O. Stephan, P. M. Ajayan, C. Colliex, Ph. Redlich, J. M. Lambert, P. Bernier, and P. Lefin, Science 266, 1683 (1994).

[32] N. G. Chopra, J. Luyken, K. Cherry, V. H. Crespi, M. L. Cohen, S. G. Louie, and A. Zettl, Science 269, 966 (1995).

[33] A. Loiseau, F. Willaime, N. Demoncy, G. Hug, and H. Pascard, Phys. Rev. Lett. 76, 4737 (1996).

[34] K. Suenaga, C. Colliex, N. Demoncy, A. Loiseau, H. Pascard, and F. Willaime, Science 278, 653 (1997).

[35] P. Gleize, S. Herreyre, P. Gadelle, M. Mermoux, M. C. Cheynet, and L. Abello, J. Materials Science Letters 13, 1413 (1994).

[36] See also the chapter by R. Tenne and A. Zettl in this Volume.

[37] R. Saito and H. Kataura. In *Carbon Nanotubes*, edited by M. S Dresselhaus and P. Avouris, Springer-Verlag, Berlin, 2000. to be published.

[38] N. Hamada, S. Sawada, and A. Oshiyama, Phys. Rev. Lett. 68, 1579–1581 (1992).

[39] R. Saito, M. Fujita, G. Dresselhaus, and M. S. Dresselhaus, Appl. Phys. Lett. 60, 2204–2206 (1992).

[40] J. W. Mintmire, B. I. Dunlap, and C. T. White, Phys. Rev. Lett. 68, 631–634 (1992).

[41] X. Blase, L. X. Benedict, E. L. Shirley, and S. G. Louie, Phys. Rev. Lett. 72, 1878 (1994).

[42] A. Rochefort, D. S. Salahub and Ph. Avouris, Chem. Phys. Lett. 297, 45 (1998).

[43] S. I. Sawada and N. Hamada, Solid State Commun. 83, 917–919 (1992).

[44] X. Blase and S. G. Louie, unpublished.

[45] L. Langer, V. Bayot, E. Grivei, J. P. Issi, J. P. Heremans, C. H. Olk, L. Stockman, C. Van Haesendonck, and Y. Bruynseraede, Phys. Rev. Lett. 76, 479–482 (1996).

[46] T. W. Ebbesen, H. J. Lezec, H. Hiura, J. W. Bennett, H. F. Ghaemi, and T. Thio, Nature (London) 382, 54–56 (1996).

[47] H. Dai, E. W. Wong, and C. M. Lieber, Science 272, 523–526 (1994).

[48] J. W. G. Wildöer, L. C. Venema, A. G. Rinzler, R. E. Smalley, and C. Dekker, Nature (London) 391, 59–62 (1998).

[49] T. W. Odom, J. L. Huang, P. Kim, and C. M. Lieber, Nature (London) 391, 62–64 (1998).

[50] L. X. Benedict, S. G. Louie, and M. L. Cohen, Phys. Rev. B 52, 8541 (1995).

[51] G. F. Bertsch, A. Bulgac, D. Tománek, and Y. Wang, Phys. Rev. Lett. 67, 2690 (1991).

[52] B. Koopmans, PhD Thesis, University of Groningen, 1993.

[53] See also the chapter by J. Hone in this Volume.

[54] C. L. Kane and E. J. Mele, Phys. Rev. Lett. 78, 1932 (1997).

[55] L. X. Benedict, S. G. Louie, and M. L. Cohen, Solid State Commun. 100, 177–180 (1996).

[56] See also the chapter by B. Yakobson in this Volume.

[57] D. H. Robertson, D. W. Brenner, and J. W. Mintmire, Phys. Rev. B 45, 12592 (1992).

[58] R. S. Ruoff and D. C. Lorents, Carbon 33, 925 (1995).

[59] J. M. Molina, S. S. Savinsky, and N. V. Khokhriakov, J. Chem. Phys. 104, 4652 (1996).

[60] B. I. Yakobson, C. J. Brabec, and J. Bernholc, Phys. Rev. Lett. 76, 2411 (1996).

[61] C. F. Cornwell and L. T. Wille, Solid State Commun. 101, 555 (1997).

[62] S. Iijima, C. J. Brabec, A. Maiti, and J. Bernholc, J. Chem. Phys. 104, 2089 (1996).

[63] J. P. Lu, Phys. Rev. Lett. 79, 1297 (1997).

[64] M. M. J. Treacy, T. W. Ebbesen, and J. M. Gibson, Nature (London) 381, 678 (1996).

[65] E. W. Wong, P. E. Sheehan, and C. M. Lieber, Science 277, 1971 (1997).

[66] N. G. Chopra and A. Zettl, Solid State Comm. 105, 297 (1998).

[67] L. Chico, L. X. Benedict, S. G. Louie, and M. L. Cohen, Phys. Rev. B 54, 2600 (1996).

[68] B. I. Dunlap, Phys. Rev. B 49, 5643 (1994).

[69] J.-C. Charlier, T. W. Ebbesen, and Ph. Lambin, Phys. Rev. B 53, 11108 (1996).

[70] T. W. Ebbesen and T. Takada, Carbon 33, 973 (1995).

[71] Ph. Lambin, L. Philippe, J.-C. Charlier, and J. P. Michenaud, Synthetic Metals 2, 350–356 (1996).

[72] S. G. Louie and M. L. Cohen, Phys. Rev. B 13, 2461 (1976).

[73] X. Blase, J. C. Charlier, A. de Vila, and R. Car, Appl. Phys. Lett. 70, 197 (1997).

[74] M. Menon and D. Srivastava, Phys. Rev. Lett. 79, 4453–4456 (1997).

[75] R. Landauer, Phil. Mag. 21, 863 (1970).

[76] D. S. Fisher and P. A. Lee, Phys. Rev. B 23, 6851 (1981).

[77] M. Nardelli, B. I. Yakobson, and J. Bernholc, Phys. Rev. Lett. 81, 4656 (1998).

[78] N. Koprinarov, M. Marinov, G. Pchelarov, M. Konstantinove, and R. Stefanov, Phys. Rev. Lett. 99, 2042 (1996).

[79] A. Zettl, private communications.

[80] H. J. Choi and J. Ihm, Phys. Rev. B 59, 2267 (1999).

[81] H. J. Choi, J. Ihm, S. G. Louie, and M. L. Cohen, Phys. Rev. Lett. 84, 2917 (2000).

[82] A. Rochefort, Ph. Avouris, F. Lesage, and R. R. Salahub, Phys. Rev. B 60, 13824 (1999).

[83] P. Delaney, H. J. Choi, J. Ihm, S. G. Louie, and M. L. Cohen, Nature (London) 391, 466 (1998).

[84] P. Delaney, H. J. Choi, J. Ihm, S. G. Louie, and M. L. Cohen, Phys. Rev. B 60, 7899 (1999).

[85] Y. K. Kwon, S. Saito, and D. Tománek, Phys. Rev. B 58, R13314 (1998).

[86] M. S. Fuhrer, J. Nygard, L. Shih, M. Forero, Y. G. Yoon, M. S. C. Mazzone, H. J. Choi, J. Ihm, S. G. Louie, A. Zettl, and P. L. McEuen, Science 288, 494 (2000).

[87] I. V. Hertel, R. E. Walkup, and P. Avouris, Phys. Rev. B 58, 13870 (1998).

[88] P. L. McEuen, M. Bockrath, D. H. Cobden, Y. G. Yoon, and S. G. Louie, Phys. Rev. Lett. 83, 5098 (1999).

[89] T. Ando, T. Nakkanishi, and R. Saito, J. Phys. Soc. Jpn. 67, 2857 (1998).

[90] T. Ando and T. Nakkanishi, J. Phys. Soc. Jpn. 67, 1704 (1998).
