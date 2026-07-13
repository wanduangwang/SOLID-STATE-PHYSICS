---
title: "G Ion Implantation and Rutherford Backscattering Spectroscopy"
abstract: "Introduces ion–solid interactions and their use in semiconductor processing and materials analysis. Covers ion implantation (range, stopping power, radiation damage, applications), the basic two-body Coulomb scattering kinematics, the LSS picture of energy loss, and ion beam analysis by Rutherford backscattering spectrometry (RBS) and channeling for composition, depth profiling, and lattice location of impurities."
---

# G Ion Implantation and Rutherford Backscattering Spectroscopy

## G.0 Overview

This appendix reviews the physics of the interaction of ion beams with solids and some of the uses of ion beams in semiconductors. Two energy regimes are emphasized: (1) ion implantation in the $\sim 100\ \mathrm{keV}$ region for introducing controlled impurity profiles, and (2) ion beam analysis (Rutherford backscattering and channeling) by MeV light-mass particles ($\mathrm{H}^{+}$, $\mathrm{He}^{+}$) for characterizing composition and crystalline perfection. Useful general references are listed below.

**References:**

- S. T. Picraux, *Physics Today*, November (1984), p. 38.
- S. T. Picraux and P. S. Peercy, *Scientific American*, March (1985), p. 102.
- J. W. Mayer, L. Eriksson, and J. A. Davies, *Ion Implantation of Semiconductors*, Stanford University Press (1970).
- G. Carter and W. A. Grant, *Ion Implantation of Semiconductors*, Edward Arnold Publishers (1976).
- J. K. Hirvonen, *Ion Implantation*, Treatise on Materials Science and Technology, Vol. 18, Academic Press (1980).
- W. K. Chu, J. W. Mayer, and M. A. Nicolet, *Backscattering Spectrometry*, Academic Press (1978).

## G.1 Introduction to the Technique

Ions of all energies incident on a solid influence its materials properties. Ions are used in many different ways in research and technology. We here review some of the physics of the interaction of ion beams with solids and some of the uses of ion beams in semiconductors. Some useful reviews are listed above.

We start by noting that the interaction of ion beams with solids depends on the energy of the incident ion. A directed low energy ion ($\sim 10$–$100\ \mathrm{eV}$) comes to rest at or near the surface of a solid, possibly growing into a registered epitaxial layer upon annealing (see {numref}`fig-apptransport-G-1`). A 1–keV heavy ion beam is the essential component in the sputtering of surfaces. For this application, a large fraction of the incident energy is transferred to the atoms of the solid resulting in the ejection of surface atoms into the vacuum. The surface is left in a disordered state. Sputtering is used for removal of material from a sample surface on an almost layer-by-layer basis. It is used both in semiconductor device fabrication, ion etching or ion milling, and more generally in materials analysis, through depth profiling. The sputtered atoms can also be used as a source for the sputter deposition technique discussed in connection with the growth of superlattices.

At higher energies, $\sim 100$–$300\ \mathrm{keV}$, energetic ions are used as a source of atoms to modify the properties of materials. Low concentrations, $\ll 0.1$ atomic percent, of implanted atoms are used to change and control the electrical properties of semiconductors. The implanted atom comes to rest $\sim 1000\ \text{\AA}$ below the surface in a region of disorder created by the passage of the implanted ion. The electrical properties of the implanted layer depend on the species and concentration of impurities, the lattice position of the impurities and the amount of lattice disorder that is created.

Lattice site and lattice disorder as well as epitaxial layer formation can readily be analyzed by the channeling of high energy light ions (such as $\mathrm{H}^{+}$ and $\mathrm{He}^{+}$), using the Rutherford backscattering technique. In this case MeV ions are used because they penetrate deeply into the crystal (microns) without substantially perturbing the lattice. This is an attractive ion energy regime because scattering cross sections, flux distributions in the crystal, and the rate of energy loss are quantitatively established. Particle–solid interactions in the range from about $0.1\ \mathrm{MeV}$ to $5\ \mathrm{MeV}$ are understood and one can use this well-characterized tool for investigations of solid state phenomena. Outside of this range many of the concepts discussed below remain valid; however, the use of MeV ions is favored in solid state characterization applications because of both experimental convenience and the ability to probe both surface and bulk properties.

In §6.2 and §6.3, we will review the two last energy regimes, namely ion implantation in the 100 keV region and ion beam analysis (Rutherford backscattering and channeling) by MeV light mass particles ($\mathrm{H}^{+}$, $\mathrm{He}^{+}$). We start by describing the most important features of ion implantation. Then we will review a two atom collision in order to introduce the basic atomic scattering concepts needed to describe the slowing down of ions in a solid. Then we will state the results of the LSS theory (J. Lindhard, M. Scharff and H. Schiøtt, *Mat. Fys. Medd. Dan. Vid. Selsk.* **33**, No. 14 (1963)) which is the most successful basic theory for describing the distribution of ion positions and the radiation-induced disorder in the implanted sample. A number of improvements to this model have been made in the last two decades and are used for current applications. We will conclude this introduction to ion implantation with a discussion of the lattice damage caused by the slowing down of the energetic ions in the solid.

We then go on and describe the use of a beam of energetic ($1$–$2\ \mathrm{MeV}$) light mass particles ($\mathrm{H}^{+}$, $\mathrm{He}^{+}$) to study material properties in the near surface region ($< \mu\mathrm{m}$) of a solid. We will then see how to use Rutherford backscattering spectrometry (RBS) to determine the stoichiometry of a sample composed of multiple chemical species and the depth distribution of implanted ions. Furthermore, we see that with single-crystal targets, the effect of channeling also allows investigation of the crystalline perfection of the sample as well as the lattice location of the implanted atomic species. Finally, we will review some examples of the modification of material properties by ion implantation, including the use of ion beam analysis in the study of these materials modifications.

## G.2 Ion Implantation

Ion implantation is an important technique for introducing impurity atoms in a controlled way, thus leading to the synthesis of new classes of materials, including metastable materials. The technique is important in the semiconductor industry for making p–n junctions by, for example, implanting n-type impurities into a p-type host material. From a materials science point of view, ion implantation allows essentially any element of the periodic table to be introduced into the near surface region of essentially any host material, with quantitative control over the depth and composition profile by proper choice of ion energy and fluence. More generally, through ion implantation, materials with increased strength and corrosion resistance or other desirable properties can be synthesized.

A schematic diagram of an ion implanter is shown in {numref}`fig-apptransport-G-2`. In this diagram the "target" is the sample that is being implanted. In the implantation process, ions of energy $E$ and beam current $i_{b}$ are incident on a sample surface and come to rest at some characteristic distance $R_{p}$ with a Gaussian distribution of half width at half maximum $\Delta R_{p}$. Typical values of the implantation parameters are: ion energies $E \sim 100\ \mathrm{keV}$, beam currents $i_{b} \sim 50\ \mu\mathrm{A}$, penetration depths $R_{p} \sim 1000\ \text{\AA}$ and half-widths $\Delta R_{p} \sim 300\ \text{\AA}$ (see {numref}`fig-apptransport-G-3`). In the implanted regions, implant concentrations of $10^{-3}$ to $10^{-5}$ relative to the host materials are typical. In special cases, local concentrations as high as 20 at.% (atomic percent) of implants have been achieved.

Some characteristic features of ion implantation are the following:

1. The ions characteristically only penetrate the host material to a depth $R_{p} \leq 1\ \mu\mathrm{m}$. Thus ion implantation is a near surface phenomenon. To achieve a large percentage of impurity ions in the host, the host material must be thin (comparable to $R_{p}$), and high fluences of implants must be used ($\phi > 10^{16}/\mathrm{cm}^{2}$).
2. The depth profile of the implanted ions ($R_{p}$) is controlled by the ion energy. The impurity content is controlled by the ion fluence $\phi$.
3. Implantation is a non-equilibrium process. Therefore there are no solubility limits on the introduction of dopants. With ion implantation one can thus introduce high concentrations of dopants, exceeding the normal solubility limits. For this reason ion implantation permits the synthesis of metastable materials.
4. The implantation process is highly directional with little lateral spread. Thus it is possible to implant materials according to prescribed patterns using masks. Implantation proceeds in the regions where the masks are not present. An application of this technology is to the ion implantation of polymers to make photoresists with sharp boundaries. Both positive and negative photoresists can be prepared using ion implantation, depending on the choice of the polymer. These masks are widely used in the semiconductor industry.
5. The diffusion process is commonly used for the introduction of impurities into semiconductors. Efficient diffusion occurs at high temperatures. With ion implantation, impurities can be introduced at much lower temperatures, as for example room temperature, which is a major convenience to the semiconductor industry.
6. The versatility of ion implantation is another important characteristic. With the same implanter, a large number of different implants can be introduced by merely changing the ion source. The technique is readily automated, and thus is amenable for use by technicians in the semiconductor industry. The implanted atoms are introduced in an atomically dispersed fashion, which is also desirable. Furthermore, no oxide or interfacial barriers are formed in the implantation process.
7. The maximum concentration of ions that can be introduced is limited. As the implantation process proceeds, the incident ions participate in both implantation into the bulk and the sputtering of atoms off the surface. Sputtering occurs because the surface atoms receive sufficient energy to escape from the surface during the collision process. The dynamic equilibrium between the sputtering and implantation processes limits the maximum concentration of the implanted species that can be achieved. Sputtering causes the surface to recede slowly during implantation.
8. Implantation causes radiation damage. For many applications, this radiation damage is undesirable. To reduce the radiation damage, the implantation can be carried out at elevated temperatures or the materials can be annealed after implantation. In practice, the elevated temperatures used for implantation or for post-implantation annealing are much lower than typical temperatures used for the diffusion of impurities into semiconductors.

A variety of techniques are used to characterize the implanted alloy. Ion backscattering of light ions at higher energies (e.g., 2 MeV $\mathrm{He}^{+}$) is used to determine the composition versus depth with $\sim 10\ \mathrm{nm}$ depth resolution. Depth profiling by sputtering in combination with Auger or secondary ion mass spectroscopy is also used. Lateral resolution is provided by analytical transmission electron microscopy. Electron microscopy, glancing angle x-ray analysis and ion channeling in single crystals provide detailed information on the local atomic structure of the alloys formed. Ion backscattering and channeling are discussed in Section 6.3.

### G.2.1 Basic Scattering Equations

An ion penetrating into a solid will lose its energy through the Coulomb interaction with the atoms in the target. This energy loss will determine the final penetration of the projectile into the solid and the amount of disorder created in the lattice of the sample. When we look more closely into one of these collisions (see {numref}`fig-apptransport-G-4`) we see that it is a very complicated event in which:

- The two nuclei with masses $M_{1}$ and $M_{2}$ and charges $Z_{1}$ and $Z_{2}$, respectively, repel each other by a Coulomb interaction, screened by the respective electron clouds.
- Each electron is attracted by the two nuclei (again with the corresponding screening) and is repelled by all other electrons.

In addition, the target atom is bonded to its neighbors through bonds which usually involve its valence electrons. The collision is thus a many-body event described by a complicated Hamiltonian. However experience has shown that very accurate solutions for the trajectory of the nuclei can be obtained by making some simplifying assumptions. The most important assumption for us, is that the interaction between the two atoms can be separated into two components: ion (projectile)–nucleus (target) interaction and ion (projectile)–electron (target) interaction.

Let us now use the very simple example of a collision between two masses $M_{1}$ and $M_{2}$ to determine the relative importance of these two processes and to introduce the basic atomic scattering concepts required to describe the stopping of ions in a solid. {numref}`fig-apptransport-G-5` shows the classical collision between the incident mass $M_{1}$ and the target mass $M_{2}$ which can be a target atom or a nearly free target electron.

By applying conservation of energy and momentum, the following relations can be derived (you will do it as homework).

- The energy transferred ($T$) in the collision from the incident projectile $M_{1}$ to the target particle $M_{2}$ is given by

```{math}
:label: eq-apptransport-G-1
T = T_{\max}\sin^{2}\!\left(\frac{\Theta}{2}\right) ,
```

where

```{math}
:label: eq-apptransport-G-2
T_{\max} = \frac{4E_{0}M_{1}M_{2}}{(M_{1}+M_{2})^{2}}
```

is the maximum possible energy transfer from $M_{1}$ to $M_{2}$.

- The scattering angle of the projectile in the laboratory system of coordinates is given by

```{math}
:label: eq-apptransport-G-3
\cos\theta = 1 - \frac{(1+M_{2}/M_{1})(T/2E)}{\sqrt{1-T/E}} .
```

- The energies of the projectile before ($E_{0}$) and after ($E_{1}$) scattering are related by

```{math}
:label: eq-apptransport-G-4
E_{1} = k^{2}E_{0} ,
```

where the kinematic factor $k$ is given by

```{math}
:label: eq-apptransport-G-5
k = \frac{M_{1}\cos\theta \pm (M_{2}^{2} - M_{1}^{2}\sin^{2}\theta)^{1/2}}{M_{1}+M_{2}} .
```

These relations are absolutely general no matter how complex the force between the two particles, so long as the force acts along the line joining the particles and the electron is nearly free so that the collision can be taken to be elastic. In reality, the collisions between the projectile and the target electrons are inelastic because of the binding energy of the electrons. The case of inelastic collisions will be considered in what follows.

Using Eqs. {eq}`eq-apptransport-G-2` and {eq}`eq-apptransport-G-3` and assuming either that $M_{2}$ is of the same atomic species as the projectile ($M_{2} = M_{1}$), or that $M_{2}$ is a nearly free electron ($M_{2} = m_{e}$) we construct {numref}`tab-apptransport-G-1`.

With the help of the previous example, we can formulate a qualitative picture of the slowing down process of the incident energetic ions. As the incident ions penetrate into the solid, they lose energy. There are two dominant mechanisms for this energy loss:

1. The interaction between the incident ion and the electrons of the host material. This inelastic scattering process gives rise to electronic energy loss.
2. The interaction between the incident ions and the nuclei of the host material. This is an elastic scattering process which gives rise to nuclear energy loss.

The ion–electron interaction (see {numref}`tab-apptransport-G-1`) induces small losses in the energy of the incoming ion as the electrons in the atom are excited to higher bound states or are ionized. These interactions do not produce significant deviations in the projectile trajectory. In contrast, the ion–nucleus interaction results in both energy loss and significant deviation in the projectile trajectory. In the ion–nucleus interaction, the atoms of the host are also significantly dislodged from their original positions giving rise to lattice defects, and the deviations in the projectile trajectory will give rise to the lateral spread of the distribution of implanted species.

Let us now further develop our example of a "nuclear" collision. For a given interaction potential $V(r)$, each ion coming into the annular ring of area $2\pi p\,dp$ with energy $E$, will be deflected through an angle $\theta$ where $p$ is the impact parameter (see {numref}`fig-apptransport-G-6`). We define $T = E_{0} - E_{1}$ as the energy transfer from the incoming ion to the host and we define $2\pi p\,dp = d\sigma$ as the differential cross section. When the ion moves a distance $\Delta x$ in the host material, it will interact with $N\Delta x\,2\pi p\,dp$ atoms where $N$ is the atom density of the host. The energy $\Delta E$ lost by an ion traversing a distance $\Delta x$ will be

```{math}
:label: eq-apptransport-G-6
\Delta E = N\Delta x \int T\, 2\pi p\, dp ,
```

so that as $\Delta x \to 0$, we have for the stopping power

```{math}
:label: eq-apptransport-G-7
\frac{dE}{dx} = N\int T\, d\sigma ,
```

where $\sigma$ denotes the cross sectional area. We thus obtain for the stopping cross section $E$

```{math}
:label: eq-apptransport-G-8
E = \frac{1}{N}\frac{dE}{dx} = \int T\, d\sigma .
```

The total stopping power is due to both electronic and nuclear processes

```{math}
:label: eq-apptransport-G-9
\frac{dE}{dx} = \left(\frac{dE}{dx}\right)_{e} + \left(\frac{dE}{dx}\right)_{n} = N(\mathcal{E}_{e} + \mathcal{E}_{n}) ,
```

where $N$ is the target density and $\mathcal{E}_{e}$ and $\mathcal{E}_{n}$ are the electronic and nuclear stopping cross sections, respectively. Likewise for the stopping cross section $E$ we can write

```{math}
:label: eq-apptransport-G-10
E = \mathcal{E}_{e} + \mathcal{E}_{n} .
```

### G.2.2 Radiation Damage

The energy transferred from the projectile ion to the target atom is usually sufficient to result in the breaking of a chemical bond and the permanent displacement of the target atom from its original site (see {numref}`fig-apptransport-G-9`). The condition for this process is that the energy transfer per collision $T$ is greater than the binding energy $E_{d}$.

Because of the high incident energy of the projectile ions, each incident ion can dislodge multiple host ions. The damage profile for low dose implantation gives rise to isolated regions of damage as shown in {numref}`fig-apptransport-G-10`. As the fluence is increased, these damaged regions coalesce as shown in {numref}`fig-apptransport-G-10`. The damage profile also depends on the mass of the projectile ion, with heavy mass ions of a given energy causing more local lattice damage as the ions come to rest. Since $(dE/dx)_{n}$ increases as the energy decreases, more damage is caused as the ions are slowed down and come to rest. The damage pattern is shown in {numref}`fig-apptransport-G-11` schematically for light ions (such as boron in silicon) and for heavy ions (such as antimony in silicon). Damage is caused both by the incident ions and by the displaced energetic (knock-on) ions.

A schematic diagram of the types of defects caused by ion implantation is shown in {numref}`fig-apptransport-G-12`. Here we see the formation of vacancies and interstitials, Frenkel pairs (the pair formed by the Coulomb attraction of a vacancy and an interstitial). The formation of multiple vacancies leads to a depleted zone while multiple interstitials lead to ion crowding.

### G.2.3 Applications of Ion Implantation

For the case of semiconductors, ion implantation is dominantly used for doping purposes, to create sharp p-n junctions in the near-surface region. To reduce radiation damage, implantation is sometimes done at elevated temperatures. Post implantation annealing is also used to reduce radiation damage, with elevated temperatures provided by furnaces, lasers or flash lamps. The ion implanted samples are characterized by a variety of experimental techniques for the implant depth profile, the lattice location of the implant, the residual lattice disorder subsequent to implantation and annealing, the electrical properties (Hall effect and conductivity) and the device performance.

A major limitation of ion implantation for modifying metal surfaces has been the shallow depth of implantation. In addition, the sputtering of atoms from the surface sets a maximum concentration of elements which can be added to a solid, typically $\sim 20$ to $40\ \mathrm{at.}\%$. To form thicker layers and higher concentrations, combined processes involving ion implantation and film deposition are being investigated. Intense ion beams are directed at the solid to bring about alloying while other elements are simultaneously brought to the surface, for example by sputter deposition, vapor deposition or the introduction of reactive gases. One process of interest is ion beam mixing, where thin films are deposited onto the surface first and then bombarded with ions. The dense collision cascades of the ions induce atomic-scale mixing between elements. Ion beam mixing is also a valuable tool to study metastable phase formation.

With regard to polymers, ion implantation can enhance the electrical conductivity by many orders of magnitude, as is for example observed (see {numref}`fig-apptransport-G-13`) for ion implanted polyacrylonitrile (PAN, a graphite fiber precursor). Some of the attendant property changes of polymers due to ion implantation include cross-linking and scission of polymer chains, gas evolution as volatile species are released from polymer chains and free radical formation when vacancies or interstitials are formed. Implantation produces solubility changes in polymers and therefore can be utilized for the patterning of resists for semiconductor mask applications. For the positive resists, implantation enhances the solubility, while for negative resists, the solubility is reduced. The high spatial resolution of the ion beams makes ion beam lithography a promising technique for sub-micron patterning applications. For selected polymers (such as PAN), implantation can result in transforming a good insulator into a conducting material with an increase in conductivity by more than 10 orders of magnitude upon irradiation. Thermoelectric power measurements on various implanted polymers show that implantation can yield either p-type or n-type conductors and in fact a p–n junction has recently been made in a polymer through ion implantation (T. Wada, A. Takeno, M. Iwake, H. Sasabe, and Y. Kobayashi, *J. Chem. Soc. Chem. Commun.*, **17**, 1194 (1985)). The temperature dependence of the conductivity for many implanted polymers is of the form $\sigma = \sigma_{0}\exp(T_{0}/T)^{1/2}$ which is also the relation characteristic of the one-dimensional hopping conductivity model for disordered materials. Also of interest is the long term chemical stability of implanted polymers.

Due to recent developments of high brightness ion sources, focused ion beams to sub-micron dimensions can now be routinely produced, using ions from a liquid metal source. Potential applications of this technology are to ion beam lithography, including the possibility of maskless implantation doping of semiconductors. Instruments based on these ideas may be developed in the future. The applications of ion implantation represent a rapidly growing field.

From the energy loss we can obtain the ion range or penetration depth

```{math}
:label: eq-apptransport-G-11
R = \int_{0}^{E_{0}} \frac{dE}{dE/dx} .
```

Since we know the energy transferred to the lattice (including both phonon generation and displacements of the host ions), we can calculate the energy of the incoming ions as a function of distance into the medium $E(x)$.

At low energies of the projectile ion, nuclear stopping is dominant, while electron stopping dominates at high energies as shown in the characteristic stopping power curves of {numref}`fig-apptransport-G-7` and {numref}`fig-apptransport-G-8`. Note the three important energy parameters on the curves shown in {numref}`fig-apptransport-G-7`: $E_{1}$ is the energy where the nuclear stopping power is a maximum, $E_{3}$ where the electronic stopping power is a maximum, and $E_{2}$ where the electronic and nuclear stopping powers are equal. As the atomic number of the ion increases for a fixed target, the scale of $E_{1}$, $E_{2}$ and $E_{3}$ increases. Also indicated on the diagram is the functional form of the energy dependence of the stopping power in several of the regimes of interest. Typical values of the parameters $E_{1}$, $E_{2}$ and $E_{3}$ for various ions in silicon are given in {numref}`tab-apptransport-G-2`. Ion implantation in semiconductors is usually done in the regime where nuclear energy loss is dominant. The region in {numref}`fig-apptransport-G-7` where $(dE/dx) \sim 1/E$ corresponds to the regime where light ions like $\mathrm{H}^{+}$ and $\mathrm{He}^{+}$ have incident energies of 1–2 MeV and is therefore the region of interest for Rutherford backscattering and channeling phenomena.

## G.3 Ion Backscattering

In Rutherford backscattering spectrometry (RBS), a beam of mono-energetic (1–2 MeV), collimated light mass ions ($\mathrm{H}^{+}$, $\mathrm{He}^{+}$) impinges (usually at near normal incidence) on a target and the number and energy of the particles that are scattered backwards at a certain angle $\theta$ are monitored (as shown in {numref}`fig-apptransport-G-14`) to obtain information about the composition of the target (host species and impurities) as a function of depth. With the help of {numref}`fig-apptransport-G-15` we will review the fundamentals of the RBS analysis.

Particles scattered at the surface of the target will have the highest energy $E$ upon detection. Here the energy of the backscattered ions $E$ is given by the relation

```{math}
:label: eq-apptransport-G-12
E = k^{2}E_{0} ,
```

where

```{math}
:label: eq-apptransport-G-13
k = \frac{M_{1}\cos\theta \pm (M_{2}^{2} - M_{1}^{2}\sin^{2}\theta)^{1/2}}{M_{1}+M_{2}}
```

as discussed in Section G.2. For a given mass species, the energy $E_{s}$ of particles scattered from the surface corresponds to the edge of the spectrum (see {numref}`fig-apptransport-G-15`). In addition, the scattered energy depends through $k$ on the mass of the scattering atom. Thus different species will appear displaced on the energy scale of {numref}`fig-apptransport-G-15`, thereby allowing for their chemical identification. We next show that the displacement along the energy scale from the surface contribution gives information about the depth where the backscattering took place. Thus the energy scale is effectively a depth scale.

The height $H$ of the RBS spectrum corresponds to the number of detected particles in each energy channel $\Delta E$.

## G.4 Channeling

If the probing beam is aligned nearly parallel to a close-packed row of atoms in a single crystal target, the particles in the beam will be steered by the potential field of the rows of atoms, resulting in an undulatory motion in which the "channeled" ions will not approach the atoms in the row to closer than 0.1–0.2 Å. This is called the channeling effect (D. V. Morgan, *Channeling*, Wiley, 1973). Under this channeling condition, the probability of large angle scattering is greatly reduced. As a consequence, there will be a drastic reduction in the scattering yield from a channeled probing beam relative to the yield from a beam incident in a random direction (see {numref}`fig-apptransport-G-16`). Two characteristic parameters for channeling are the normalized minimum yield $\chi_{\min} = H_{A}/H$ which is a measure of the crystallinity of the target, and the critical angle for channeling $\psi_{1/2}$ (the halfwidth at half maximum intensity of the channeling resonance) which determines the degree of alignment required to observe the channeling effect.

The RBS–channeling technique is frequently used to study radiation-induced lattice disorder by measuring the fraction of atom sites where the channel is blocked. In general, the channeled ions are steered by the rows of atoms in the crystal. However if some portion of the crystal is disordered and lattice atoms are displaced so that they partially block the channels, the ions directed along nominal channeling directions can now have a close collision with these displaced atoms, so that the resulting scattered yield will be increased above that for an undisturbed channel. Furthermore, since the displaced atoms are of equal mass to those of the surrounding lattice, the increase in the yield occurs at a position in the yield vs. energy spectrum corresponding to the depth at which the displaced atoms are located. The increase in the backscattering yield from a given depth will depend upon the number of displaced atoms, so the depth (or equivalently, the backscattering energy $E$) dependence of the yield, reflects the depth dependence of displaced atoms, and integrations over the whole spectrum will give a measure of the total number of displaced atoms. This effect is shown schematically in {numref}`fig-apptransport-G-17`.

Another very useful application of the RBS–channeling technique is in the determination of the location of foreign atoms in a host lattice. Since channeled ions cannot approach the rows of atoms which form the channel closer than $\sim 0.1\ \text{\AA}$, we can think of a "forbidden region", as a cylindrical region along each row of atoms with radius $\sim 0.1\ \text{\AA}$, such that there are no collisions between the channeled particles and atoms located within the forbidden zone. In particular, if an impurity is located in a forbidden region it will not be detected by the channeled probing beam. On the other hand, any target particle can be detected by (i.e., will scatter off) probing particles from a beam which impinges in a random direction. Thus, by comparing the impurity peak observed for channeling and random alignments, the fraction of impurities sitting in the forbidden region of a particular channel (high symmetry crystallographic axis) can be determined. Repeating the procedure for other crystallographic directions allows the identification of the lattice location of the impurity atom in many cases.

Rutherford backscattering will not always reveal impurities embedded in a host matrix, in particular if the mass of the impurities is smaller than the mass of the host atoms. In such cases, ion induced x-rays and ion induced nuclear reactions are used as signatures for the presence of the impurities inside the crystal, and the lattice location is derived from the changes in yield of these processes for random and channeled impingement of the probing beam.

Ion markers consist of a very thin layer of a guest atomic species embedded in an otherwise uniform host material of a different species to establish reference distances. Backscattering spectra are taken before and after introduction of the marker. The RBS spectrum taken after insertion of the marker can be used as a reference for various applications. Some examples where marker references are useful include:

- Estimation of surface sputtering by ion implantation. In this case, recession of the surface from the reference position set by the marker (see {numref}`fig-apptransport-G-18`) can be measured by RBS and can be analyzed to yield the implantation-induced surface sputtering.
- Estimation of surface material vaporized through laser annealing, rapid thermal annealing or laser melting of a surface.
- Estimation of the extent of ion beam mixing.

---

**Tables**

```{table} Maximum energy transfer $T_{\max}$ and scattering angle $\theta$ for nuclear ($M_{2} = M_{1}$) and electronic ($M_{2} = m_{e}$) collisions
:name: tab-apptransport-G-1
| | "nuclear" collision | "electronic" collision |
|---|---|---|
| $T_{\max}$ | $T_{\max} \simeq E_{0}$ | $T_{\max} \simeq (4m/M_{1})E_{0}$ |
| $\theta$ | $0 < \theta \leq \pi/2$ | $\theta = 0^{\circ}$ |
```

```{table} Typical values of $E_{1}$, $E_{2}$, $E_{3}$ for silicon
:name: tab-apptransport-G-2
$a$See {numref}`fig-apptransport-G-7` for the definition of the notation.
| Ion | $E_{1}$ (keV) | $E_{2}$ (keV) | $E_{3}$ (keV) |
|---|---|---|---|
| B  | 3    | 17    | 3000      |
| P  | 17   | 140   | $\sim 3\times 10^{4}$ |
| As | 73   | 800   | $> 10^{5}$ |
| Sb | 180  | 2000  | $> 10^{5}$ |
```

:::{figure} images/fig-apptransport-G-1.png
:name: fig-apptransport-G-1
:width: 80%
:align: center
Fig. G.1: Schematic illustrating the interactions of ion beams with a single-crystal solid. Directed beams of $\sim 10\ \mathrm{eV}$ are used for film deposition and epitaxial formation. Ion beams of energy $\sim 1\ \mathrm{keV}$ are employed in sputtering applications; $\sim 100\ \mathrm{keV}$ ions are used in ion implantation. Both the sputtering and implantation processes damage and disorder the crystal. Higher energy light ions are used for ion beam analysis.
:::

:::{figure} images/fig-apptransport-G-2.png
:name: fig-apptransport-G-2
:width: 80%
:align: center
Fig. G.2: Schematic diagram of an ion implanter.
:::

:::{figure} images/fig-apptransport-G-3.png
:name: fig-apptransport-G-3
:width: 80%
:align: center
Fig. G.3: Typical ion implantation parameters.
:::

:::{figure} images/fig-apptransport-G-4.png
:name: fig-apptransport-G-4
:width: 80%
:align: center
Fig. G.4: Penetration of ions into solids.
:::

:::{figure} images/fig-apptransport-G-5.png
:name: fig-apptransport-G-5
:width: 70%
:align: center
Fig. G.5: The upper figure defines the scattering variables in a two-body collision. The projectile has mass $M_{1}$ and an initial velocity $v_{0}$, and an impact parameter, $p$, with the target particle. The projectile's final angle of deflection is $\theta$ and its final velocity is $v_{1}$. The target particle with mass $M_{2}$ recoils at an angle $\phi$ with velocity $v_{2}$. The lower figure is the same scattering event in the center-of-mass (CM) coordinates in which the total momentum of the system is zero. The coordinate system moves with velocity $v_{c}$ relative to the laboratory coordinates, and the angles of scatter and recoil are $\Theta$ and $\Phi$ in the center of mass system.
:::

:::{figure} images/fig-apptransport-G-6.png
:name: fig-apptransport-G-6
:width: 80%
:align: center
Fig. G.6: Classical model for the collision of a projectile of energy $E$ with a target at rest. The open circles denote the initial state of the projectile and target atoms, and the full circles denote the two atoms after the collision.
:::

:::{figure} images/fig-apptransport-G-7.png
:name: fig-apptransport-G-7
:width: 80%
:align: center
Fig. G.7: Nuclear and electronic energy loss (stopping power) vs. energy.
:::

:::{figure} images/fig-apptransport-G-8.png
:name: fig-apptransport-G-8
:width: 80%
:align: center
Fig. G.8: Nuclear and electronic energy loss (stopping power) vs. $\epsilon^{1/2}$ (reduced units of LSS theory).
:::

:::{figure} images/fig-apptransport-G-9.png
:name: fig-apptransport-G-9
:width: 80%
:align: center
Fig. G.9: Energy transfer from projectile ion to target atoms for a single scattering event for the condition $T > E_{d}$ where $E_{d}$ is the binding energy and $T$ is the energy transfer per collision.
:::

:::{figure} images/fig-apptransport-G-10.png
:name: fig-apptransport-G-10
:width: 80%
:align: center
Fig. G.10: Schematic diagram showing the range of lattice damage for low dose and high dose implants.
:::

:::{figure} images/fig-apptransport-G-11.png
:name: fig-apptransport-G-11
:width: 80%
:align: center
Fig. G.11: Schematic diagram of the damage pattern for light ions and heavy ions in the same target (silicon).
:::

:::{figure} images/fig-apptransport-G-12.png
:name: fig-apptransport-G-12
:width: 80%
:align: center
Fig. G.12: Example of typical defects induced by ion implantation.
:::

:::{figure} images/fig-apptransport-G-13.png
:name: fig-apptransport-G-13
:width: 70%
:align: center
Fig. G.13: Implantation induced conductivity of a normally insulating polymer.
:::

:::{figure} images/fig-apptransport-G-14.png
:name: fig-apptransport-G-14
:width: 80%
:align: center
Fig. G.14: In the RBS experiment, the scattering chamber where the analysis/experiment is actually performed contains the essential elements: the sample, the beam, the detector, and the vacuum pump.
:::

:::{figure} images/fig-apptransport-G-15.png
:name: fig-apptransport-G-15
:width: 70%
:align: center
Fig. G.15: Schematic diagram showing the energy distribution of ions back-scattered from a Si sample (not aligned) which was implanted with As atoms.
:::

:::{figure} images/fig-apptransport-G-16.png
:name: fig-apptransport-G-16
:width: 80%
:align: center
Fig. G.16: Schematic backscattering spectrum and angular yield profile.
:::

:::{figure} images/fig-apptransport-G-17.png
:name: fig-apptransport-G-17
:width: 70%
:align: center
Fig. G.17: Schematic random and aligned spectra for MeV $^4\mathrm{He}$ ions incident on a crystal containing disorder. The aligned spectrum for a perfect crystal without disorder is shown for comparison. The difference (shaded portion) in the aligned spectra between disordered and perfect crystals can be used to determine the concentration $N_{D}(0)$ of displaced atoms at the surface.
:::

:::{figure} images/fig-apptransport-G-18.png
:name: fig-apptransport-G-18
:width: 80%
:align: center
Fig. G.18: Schematic of the marker experiment which demonstrates surface recession through surface sputtering.
:::
