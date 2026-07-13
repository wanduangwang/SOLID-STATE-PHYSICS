---
title: "2 Examples of Energy Bands in Solids"
abstract: 'This chapter surveys representative energy band diagrams for metals, semiconductors, semimetals and insulators, using the $E(\vec{k})$ relations to identify carriers, Fermi surfaces, effective masses, and optical thresholds.'
---

# 2 Examples of Energy Bands in Solids

## 2.0 Overview

We present here some examples of energy bands which are representative of metals, semiconductors and insulators, and we point out some of the characteristic features in each case. For each $E(\vec{k})$ diagram we ask: What type of material is it? Which atomic levels correspond to the bands? What are the bandwidths and band gaps? Where are the carriers in the Brillouin zone? What is the shape of the Fermi surface? What do the optical thresholds tell us?

**References:**

- J.C. Slater – *Quantum Theory of Atoms and Molecules*, Chapter 10.
- R.E. Peierls – *Quantum Theory of Solids*, Chapter 4.
- F. Bassani and G. Pastori Paravicini – *Electronic States and Optical Transitions in Solids*, Chapter 4.

## 2.1 General Issues

Figure 2.1 distinguishes in a schematic way between insulators (a), metals (b), semimetals (c), a thermally excited semiconductor (d) for which at $T = 0$ all states in the valence band are occupied and all states in the conduction band are unoccupied, assuming no impurities or crystal defects. Finally in {numref}`fig-p1-ch02-1`(e), we see a p-doped semiconductor which is deficient in electrons, not having sufficient electrons to fill the valence band completely as in (d). The semiconductor (e) will have a non-zero carrier density at $T = 0$ while for semiconductor (d) the carrier density will be zero at $T = 0$.

:::{figure} images/fig-p1-ch02-1.png
:name: fig-p1-ch02-1
:width: 80%
:align: center
Fig. 2.1: Schematic electron occupancy of allowed energy bands for an insulator, metal, semimetal and semiconductor. The vertical extent of the boxes indicates the allowed energy regions; the shaded areas indicate the regions filled with electrons. In a semimetal (such as bismuth) one band is almost filled and another band is nearly empty at a temperature of absolute zero. A pure semiconductor (such as silicon) becomes an insulator at $T = 0$. Panel (d) shows an intrinsic semiconductor at a finite temperature, with carriers that are thermally excited. Panel (e) shows a p-doped semiconductor that is electron-deficient, as, for example, because of the introduction of acceptor impurities.
:::

{numref}`fig-p1-ch02-2` shows a schematic view of the electron dispersion relations for an insulator (a), while (c) shows dispersion relations for a metal. In the case of {numref}`fig-p1-ch02-2`(b), we have a semimetal if the number of electrons equals the number of holes, but a metal otherwise.

:::{figure} images/fig-p1-ch02-2.png
:name: fig-p1-ch02-2
:width: 80%
:align: center
Fig. 2.2: Occupied states and band structures giving (a) an insulator, (b) a metal or a semimetal because of band overlap, and (c) a metal because of partial occupation of an electron band. In (b) the band overlap for a 3D solid need not occur along the same direction of the wave vector in the Brillouin zone.
:::

In this chapter we examine a number of representative $E(\vec{k})$ diagrams for illustrative materials. For each of the $E(\vec{k})$ diagrams we consider the following questions:

1. Is the material a metal, a semiconductor (direct or indirect gap), semimetal or insulator?
2. To which atomic (molecular) levels do the bands on the band diagram correspond? Which bands are important in determining the electronic structure? What are the bandwidths, bandgaps?
3. What information does the $E(\vec{k})$ diagram provide concerning the following questions:
   - (a) Where are the carriers in the Brillouin zone?
   - (b) Are the carriers electrons or holes?
   - (c) Are there many or few carriers?
   - (d) How many carrier pockets of each type are there in the Brillouin zone?
   - (e) What is the shape of the Fermi surface?
   - (f) Are the carrier velocities high or low?
   - (g) Are the carrier mobilities for each carrier pocket high or low?
4. What information is provided concerning the optical properties?
   - (a) Where in the Brillouin Zone is the threshold for optical transitions?
   - (b) At what photon energy does the optical threshold occur?
   - (c) For semiconductors, does the threshold correspond to a direct gap or an indirect gap (phonon-assisted) transition?

## 2.2 Metals

### 2.2.1 Alkali Metals – e.g., Sodium

For the alkali metals the valence electrons are nearly free and the weak binding approximation describes these electrons quite well. The Fermi surface is nearly spherical and the band gaps are small. The crystal structure for the alkali metals is body centered cubic (BCC) and the $E(\vec{k})$ diagram is drawn starting with the bottom of the half-filled conduction band. For example, the $E(\vec{k})$ diagram in {numref}`fig-p1-ch02-3` for sodium begins at $\sim -0.6$ Rydberg and represents the $3s$ conduction band. The filled valence bands lie much lower in energy and are not shown in {numref}`fig-p1-ch02-3`.

:::{figure} images/fig-p1-ch02-3.png
:name: fig-p1-ch02-3
:width: 80%
:align: center
Fig. 2.3: (a) Energy dispersion relations for the nearly free electron metal sodium which has an atomic configuration $1s^2 2s^2 2p^6 3s$. (b) The Brillouin zone for the BCC lattice showing the high symmetry points and axes. Sodium can be considered as a prototype alkali metal crystalline solid for discussing the dispersion relations for nearly free electron metals.
:::

For the case of sodium, the $3s$ conduction band is very nearly free electron–like and the $E(\vec{k})$ relations are closely isotropic. Thus the $E(\vec{k})$ relations along the $\Delta(100)$, $\Sigma(110)$ and $\Lambda(111)$ directions [see {numref}`fig-p1-ch02-3`(b)] are essentially coincident and can be so plotted, as shown in {numref}`fig-p1-ch02-3`(a). For these metals, the Fermi level is determined so that the $3s$ band is exactly half-occupied, since the Brillouin zone is large enough to accommodate 2 electrons per unit cell. Thus the radius of the Fermi surface $k_F$ satisfies the relation

```{math}
:label: eq-p1-ch02-1
\frac{4}{3}\pi k_F^3 = \frac{1}{2} V_{B.Z.} = \frac{1}{2}(2)\left(\frac{2\pi}{a}\right)^3, \qquad \text{or} \qquad \frac{k_F a}{2\pi} \sim 0.63,
```

where $V_{B.Z.}$ and $a$ are, respectively, the volume of the Brillouin zone and the lattice constant. For the alkali metals, the effective mass $m^*$ is nearly equal to the free electron mass $m_0$ and the Fermi surface is nearly spherical and never comes close to the Brillouin zone boundary. The zone boundary for the $\Sigma$, $\Lambda$ and $\Delta$ directions are indicated in the $E(\vec{k})$ diagram of {numref}`fig-p1-ch02-3` by vertical lines. For the alkali metals, the band gaps are very small compared to the band widths and the $E(\vec{k})$ relations are parabolic ($E = \hbar^2 k^2 / 2m^*$) almost up to the Brillouin zone boundaries. By comparing $E(\vec{k})$ for Na with the BCC empty lattice bands (see {numref}`fig-p1-ch02-4`) for which the potential $V(\vec{r}) = 0$, we can see the effect of the very weak periodic potential in partially lifting the band degeneracy at the various high symmetry points in the Brillouin zone.

:::{figure} images/fig-p1-ch02-4.png
:name: fig-p1-ch02-4
:width: 80%
:align: center
Fig. 2.4: (a) $E(\vec{k})$ for a BCC lattice in the empty lattice approximation, $V \equiv 0$. (b) $E(\vec{k})$ for sodium, showing the effect of a weak periodic potential in lifting accidental band degeneracies at $k = 0$ and at the zone boundaries (high symmetry points) in the Brillouin zone. Note that the splittings are quite different for the various bands and at different high symmetry points.
:::

The threshold for optical transitions corresponds to photons having sufficient energy to take an electron from an occupied state at $k_F$ to an unoccupied state at $k_F$, since the wave vector for photons is very small compared with the Fermi wave vector $k_F$ and since wave vector conservation (i.e., crystal momentum conservation) is required for optical transitions. The threshold for optical transitions is indicated by $\hbar\omega$ and a vertical arrow in {numref}`fig-p1-ch02-3`. Because of the low density of initial and final states for a given energy separation, we would expect optical interband transitions for alkali metals to be very weak and this is in agreement with experimental observations for all the alkali metals. The notation a.u. in {numref}`fig-p1-ch02-3` stands for atomic units and expresses lattice constants in units of Bohr radii. The electron energy is given in Rydbergs where $1$ Rydberg $= 13.6$ eV, the ionization energy of a hydrogen atom.

### 2.2.2 Noble Metals

The noble metals are copper, silver and gold and they crystallize in a face centered cubic (FCC) structure; the usual notation for the high symmetry points in the FCC Brillouin zone are shown on the diagram in {numref}`fig-p1-ch02-5`(a). As in the case of the alkali metals, the noble metals have one valence electron/atom and therefore one electron per primitive unit cell. However, the free electron picture does not work so well for the noble metals, as you can see by looking at the energy band diagram for copper given in {numref}`fig-p1-ch02-5`(b).

:::{figure} images/fig-p1-ch02-5.png
:name: fig-p1-ch02-5
:width: 70%
:align: center
Fig. 2.5: (a) Brillouin zone for a FCC lattice showing high symmetry points. (b) The calculated energy bands for copper along the various symmetry axes of the FCC Brillouin zone shown in (a).
:::

In the case of copper, the bands near the Fermi level are derived from the $4s$ and $3d$ atomic levels. The so-called $4s$ and $3d$ bands accommodate a total of 12 electrons, while the number of available electrons is 11. Therefore the Fermi level must cross these bands. Consequently copper is metallic. In {numref}`fig-p1-ch02-5`(b) we see that the $3d$ bands are relatively flat and show little dependence on wave vector $\vec{k}$. We can trace the $3d$ bands by starting at $\vec{k} = 0$ with the $\Gamma_{25'}$ and $\Gamma_{12}$ levels. On the other hand, the $4s$ band has a strong $k$-dependence and a large curvature. This band can be traced by starting at $\vec{k} = 0$ with the $\Gamma_1$ level. About halfway between $\Gamma$ and $X$, the $4s$ level approaches the $3d$ levels and mixing or hybridization occurs. As we further approach the $X$-point, we can again pick up the $4s$ band (beyond where the interaction with the $3d$ bands occurs) because of its high curvature. This $4s$ band eventually crosses the Fermi level before reaching the Brillouin Zone boundary at the $X$ point. A similar mixing or hybridization between $4s$ and $3d$ bands occurs in going from $\Gamma$ to $L$, except that in this case the $4s$ band reaches the Brillouin Zone boundary before crossing the Fermi level.

Of particular significance for the transport properties of copper is the band gap that opens up at the $L$-point. In this case, the band gap is between the $L_2'$ level below the Fermi level $E_F$ and the $L_1$ level above $E_F$. Since this bandgap is comparable with the typical bandwidths in copper, we cannot expect the Fermi surface to be free electron–like. By looking at the energy bands $E(\vec{k})$ along the major high symmetry directions such as the $(100)$, $(110)$ and $(111)$ directions, we can readily trace the origin of the copper Fermi surface [see {numref}`fig-p1-ch02-6`(a)]. Here we see basically a spherical Fermi surface with necks pulled out in the $(111)$ directions and making contact with the Brillouin zone boundary through these necks, thereby linking the Fermi surface in one zone to that in the next zone in the extended zone scheme.

:::{figure} images/fig-p1-ch02-6.png
:name: fig-p1-ch02-6
:width: 80%
:align: center
Fig. 2.6: (a) The copper Fermi surface in the extended zone scheme. (b) A sketch of the Fermi surface of copper inscribed within the FCC Brillouin zone.
:::

In the $(100)$ direction, the cross section of the Fermi surface is nearly circular, indicative of the nearly parabolic $E(\vec{k})$ relation of the $4s$ band at the Fermi level in going from $\Gamma$ to $X$. In contrast, in going from $\Gamma$ to $L$, the $4s$ band never crosses the Fermi level. Instead the $4s$ level is depressed from the free electron parabolic curve as the Brillouin zone boundary is reached, thereby producing a higher density of states. Thus, near the zone boundary, more electrons can be accommodated per unit energy range, or to say this another way, there will be increasingly more $\vec{k}$ vectors with approximately the same energy. This causes the constant energy surfaces to be pulled out in the direction of the Brillouin zone boundary [see {numref}`fig-p1-ch02-6`(b)]. This “pulling out” effect follows both from the weak binding and tight binding approximations and the effect is more pronounced as the strength of the periodic potential (or $V_{\vec{G}}$) increases.

If the periodic potential is sufficiently strong so that the resulting bandgap at the zone boundary straddles the Fermi level, as occurs at the $L$-point in copper, the Fermi surface makes contact with the Brillouin zone boundary. The resulting Fermi surfaces are called open surfaces because the Fermi surfaces between neighboring Brillouin zones are connected, as seen in {numref}`fig-p1-ch02-6`(a). The electrons associated with the necks are contained in the electron pocket shown in the $E(\vec{k})$ diagram away from the $L$-point in the $LW$ direction which is $\perp$ to the $\{111\}$ direction. The copper Fermi surface shown in {numref}`fig-p1-ch02-6`(a) bounds electron states. Hole pockets are formed in copper [see {numref}`fig-p1-ch02-6`(a)] in the extended zone and constitute the unoccupied space between the electron surfaces. Direct evidence for hole pockets is provided by Fermi surface measurements to be described later in this course.

From the $E(\vec{k})$ diagram for copper [{numref}`fig-p1-ch02-5`(b)] we see that the threshold for optical interband transitions occurs for photon energies sufficient to take an electron at constant $\vec{k}$-vector from a filled $3d$ level to an unoccupied state above the Fermi level. Such interband transitions can be made near the $L$-point in the Brillouin zone [as shown by the vertical arrow on {numref}`fig-p1-ch02-5`(b)]. Because of the high density of initial states in the $d$-band, these transitions will be quite intense. The occurrence of these interband transitions at $\sim 2$ eV gives rise to a large absorption of electromagnetic energy in this photon energy region. The reddish color of copper metal is thus due to a higher reflectivity for photons in the red (below the threshold for interband transitions) than for photons in the blue (above this threshold).

### 2.2.3 Polyvalent Metals

The simplest example of a polyvalent metal is aluminum with 3 electrons/atom and having a $3s^2 3p$ electronic configuration for the valence electrons. (As far as the number of electrons/atom is concerned, two electrons/atom completely fill a non-degenerate band—one for spin up, the other for spin down.) Because of the partial filling of the $3s^2 3p^6$ bands, aluminum is a metal. Aluminum crystallizes in the FCC structure so we can use the same notation as for the Brillouin zone in {numref}`fig-p1-ch02-5`(a).

:::{figure} images/fig-p1-ch02-7.png
:name: fig-p1-ch02-7
:width: 70%
:align: center
Fig. 2.7: Electronic energy band diagram for aluminum which crystallizes in a FCC structure. The dashed lines correspond to the free electron model and the solid curves include the effect of the periodic potential $V(\vec{r})$.
:::

The energy bands for aluminum (see {numref}`fig-p1-ch02-7`) are very free electron–like. This follows from the small magnitudes of the band gaps relative to the band widths on the energy band diagram shown in {numref}`fig-p1-ch02-7`. The lowest valence band shown in {numref}`fig-p1-ch02-7` is the $3s$ band which can be traced by starting at zero energy at the $\Gamma$ point ($\vec{k} = 0$) and going out to $X_4$ at the $X$-point, to $W_3$ at the $W$-point, to $L_2'$ at the $L$-point and back to $\Gamma_1$ at the $\Gamma$ point ($\vec{k} = 0$). Since this band always lies below the Fermi level, it is completely filled, containing 2 electrons. The third valence electron partially occupies the second and third $p$-bands (which are more accurately described as hybridized $3p$-bands with some admixture of the $3s$ bands with which they interact). From {numref}`fig-p1-ch02-7` we can see that the second band is partly filled; the occupied states extend from the Brillouin zone boundary inward toward the center of the zone; this can be seen in going from the $X$ point to $\Gamma$, on the curve labeled $\Delta_1$. Since the second band states near the center of the Brillouin zone remain unoccupied, the volume enclosed by the Fermi surface in the second band is a hole pocket.

:::{figure} images/fig-p1-ch02-8.png
:name: fig-p1-ch02-8
:width: 50%
:align: center
Fig. 2.8: The three valence electrons for aluminum occupy three Brillouin zones. Zone 1 is completely occupied. Zone 2 is nearly filled with electrons and is best described as a hole surface, where the holes occupy the interior portion of the second zone, shown in the figure. Zone 3 is a complex electron structure with occupied electron states near the Brillouin zone boundaries, and the occupied states are shown only in part for clarity.
:::

The aluminum Fermi surface showing the Zone 2 holes is presented in {numref}`fig-p1-ch02-8`. Because $E(\vec{k})$ for the second band in the vicinity of $E_F$ is free electron–like, the masses for the holes are approximately equal to the free electron mass. The 3rd zone electron pockets are small and are found around the $K$- and $W$-points as can be seen in {numref}`fig-p1-ch02-7`. These electron pockets are $\vec{k}$-space volumes that enclose electron states (see {numref}`fig-p1-ch02-8`), and because of the large curvature of $E(\vec{k})$, these electrons have relatively small masses. {numref}`fig-p1-ch02-7` gives no evidence for any 4th zone pieces of Fermi surface, and for this reason we can conclude that all the electrons are either in the second band or in the third band as shown in {numref}`fig-p1-ch02-8`. The total electron concentration is sufficient to exactly fill a half of the volume of the Brillouin zone $V_{BZ}$:

```{math}
:label: eq-p1-ch02-2
V_{e,2} + V_{e,3} = \frac{V_{BZ}}{2} .
```

With regard to the second zone, it is partially filled with electrons and the rest of the zone is empty (since holes correspond to the unfilled states):

```{math}
:label: eq-p1-ch02-3
V_{h,2} + V_{e,2} = V_{BZ},
```

with the volume that is empty slightly exceeding the volume that is occupied. Therefore we focus attention on the more dominant second zone holes. Substitution of {eq}`eq-p1-ch02-2` into {eq}`eq-p1-ch02-3` then yields for the second zone holes and the third zone electrons

```{math}
:label: eq-p1-ch02-4
V_{h,2} - V_{e,3} = \frac{V_{BZ}}{2}
```

where the subscripts $e, h$ on the volumes in $\vec{k}$ space refer to electrons and holes and the Brillouin zone (B.Z.) index is given for each of the carrier pockets. Because of the small masses and high mobility of the 3rd zone electrons, they play a more important role in the transport properties of aluminum than would be expected from their small numbers.

From the $E(\vec{k})$ diagram in {numref}`fig-p1-ch02-7` we see that at the same $\vec{k}$-points (near the $K$- and $W$-points in the Brillouin zone) there are occupied $3s$ levels and unoccupied $3p$ levels separated by $\sim 1$ eV. From this we conclude that optical interband transitions should be observable in the 1 eV photon energy range. Such interband transitions are in fact observed experimentally and are responsible for the departures from nearly perfect reflectivity of aluminum mirrors in the vicinity of 1 eV.

## 2.3 Semiconductors

Assume that we have a semiconductor at $T = 0$ K with no impurities. The Fermi level will then lie within a band gap. Under these conditions, there are no carriers, and no Fermi surface. We now illustrate the energy band structure for several representative semiconductors in the limit of $T = 0$ K and no impurities. Semiconductors having no impurities or defects are called intrinsic semiconductors.

### 2.3.1 PbTe

In {numref}`fig-p1-ch02-9` we illustrate the energy bands for PbTe. This direct gap semiconductor [see {numref}`fig-p1-ch02-10`(a)] is chosen initially for illustrative purposes because the energy bands in the valence and conduction bands that are of most importance to determine the physical properties of PbTe are non-degenerate. Therefore, the energy states in PbTe near $E_F$ are simpler to understand than for the more common semiconductors silicon and germanium, and for many of the III–V and II–VI compound semiconductors.

:::{figure} images/fig-p1-ch02-9.png
:name: fig-p1-ch02-9
:width: 80%
:align: center
Fig. 2.9: (a) Energy band structure and density of states for PbTe obtained from an empirical pseudopotential calculation. (b) Theoretical values for the $L$ point bands calculated by different models (labeled a, b, c, d on the x-axis) (Ref. Landolt and Bornstein).
:::

:::{figure} images/fig-p1-ch02-10.png
:name: fig-p1-ch02-10
:width: 80%
:align: center
Fig. 2.10: Optical absorption processes for (a) a direct band gap semiconductor, (b) an indirect band gap semiconductor, and (c) a direct band gap semiconductor with the conduction band filled to the level shown.
:::

In {numref}`fig-p1-ch02-9`, we show the position of $E_F$ for the idealized conditions of the intrinsic (no carriers at $T = 0$) semiconductor PbTe. From a diagram like this, we can obtain a great deal of information which could be useful for making semiconductor devices. For example, we can calculate effective masses from the band curvatures, and electron velocities from the slopes of the $E(\vec{k})$ dispersion relations shown in {numref}`fig-p1-ch02-9`.

Suppose we add impurities (e.g., donor impurities) to PbTe. The donor impurities will raise the Fermi level and an electron pocket will eventually be formed in the $L_6^-$ conduction band about the $L$-point. This electron pocket will have an ellipsoidal Fermi surface because the band curvature is different as we move away from the $L$ point in the $L\Gamma$ direction as compared with the band curvature as we move away from $L$ on the Brillouin zone boundary containing the $L$ point (e.g., $LW$ direction). {numref}`fig-p1-ch02-9` shows $E(\vec{k})$ from $L$ to $\Gamma$ corresponding to the $(111)$ direction. Since the effective masses

```{math}
:label: eq-p1-ch02-5
\frac{1}{m^*_{ij}} = \frac{1}{\hbar^2} \frac{\partial^2 E(\vec{k})}{\partial k_i \partial k_j}
```

for both the valence and conduction bands in the longitudinal $L\Gamma$ direction are heavier than in the $LK$ and $LW$ directions, the ellipsoids of revolution describing the carrier pockets are prolate for both holes and electrons. The $L$ and $\Sigma$ point room temperature band gaps are $0.311$ eV and $0.360$ eV, respectively. For the electrons, the effective mass parameters are $m_\perp = 0.053 m_e$ and $m_\parallel = 0.620 m_e$. The experimental hole effective masses at the $L$ point are $m_\perp = 0.0246 m_e$ and $m_\parallel = 0.236 m_e$ and at the $\Sigma$ point, the hole effective mass values are $m_\perp = 0.124 m_e$ and $m_\parallel = 1.24 m_e$. Thus for the $L$-point carrier pockets, the semi-major axis of the constant energy surface along $L\Gamma$ will be longer than along $LK$.

From the $E(\vec{k})$ diagram for PbTe in {numref}`fig-p1-ch02-9` one would expect that hole carriers could be thermally excited to a second band at the $\Sigma$ point, which is indicated on the $E(\vec{k})$ diagram. At room temperature, these $\Sigma$ point hole carriers contribute significantly to the transport properties. Because of the small gap ($0.311$ eV) in PbTe at the $L$-point, the threshold for interband transitions will occur at infrared frequencies. PbTe crystals can be prepared either p-type or n-type, but never perfectly stoichiometrically (i.e., intrinsic PbTe has not been prepared). Therefore, at room temperature the Fermi level $E_F$ often lies in either the valence or conduction band for actual PbTe crystals. Since optical transitions conserve wavevector, the interband transitions will occur at $k_F$ [see {numref}`fig-p1-ch02-10`(c)] and at a higher photon energy than the direct band gap. This increase in the threshold energy for interband transitions in degenerate semiconductors (where $E_F$ lies within either the valence or conduction bands) is called the Burstein shift.

### 2.3.2 Germanium

We will next look at the $E(\vec{k})$ relations for: (1) the group IV semiconductors which crystallize in the diamond structure and (2) the closely related III–V compound semiconductors which crystallize in the zincblende structure (see {numref}`fig-p1-ch02-11` for a schematic diagram for this class of semiconductors). These semiconductors have degenerate valence bands at $\vec{k} = 0$ [see {numref}`fig-p1-ch02-11`(d)] and for this reason have more complicated $E(\vec{k})$ relations for carriers than is the case for the lead salts discussed in §2.3.1. The $E(\vec{k})$ diagram for germanium is shown in {numref}`fig-p1-ch02-12`. Ge is a semiconductor with a bandgap occurring between the top of the valence band at $\Gamma_{25'}$, and the bottom of the lowest conduction band at $L_1$. Since the valence and conduction band extrema occur at different points in the Brillouin zone, Ge is an indirect gap semiconductor [see {numref}`fig-p1-ch02-10`(b)].

:::{figure} images/fig-p1-ch02-11.png
:name: fig-p1-ch02-11
:width: 80%
:align: center
Fig. 2.11: Important details of the band structure of typical group IV and III–V semiconductors.
:::

:::{figure} images/fig-p1-ch02-12.png
:name: fig-p1-ch02-12
:width: 70%
:align: center
Fig. 2.12: Electronic energy band structure of Ge (a) without spin-orbit interaction. (b) The electronic energy bands near $k = 0$ when the spin-orbit interaction is included.
:::

Using the same arguments as were given in §2.3.1 for the Fermi surface of PbTe, we see that the constant energy surfaces for electrons in germanium are ellipsoids of revolution [see {numref}`fig-p1-ch02-11`(c)]. As for the case of PbTe, the ellipsoids of revolution are elongated along $\Gamma L$ which is the heavy mass direction in this case. Since the multiplicity of $L$-points is 8, we have 8 half-ellipsoids of this kind within the first Brillouin zone, just as for the case of PbTe. By translation of these half-ellipsoids by a reciprocal lattice vector we can form 4 full-ellipsoids. The $E(\vec{k})$ diagram for germanium (see {numref}`fig-p1-ch02-12`) further shows that the next highest conduction band above the $L$ point minimum is at the $\Gamma$-point ($\vec{k}=0$) and after that along the $\Gamma X$ axis at a point commonly labeled as a $\Delta$-point. Because of the degeneracy of the highest valence band, the Fermi surface for holes in germanium is more complicated than for electrons. The lowest direct band gap in germanium is at $\vec{k} = 0$ between the $\Gamma_{25'}$ valence band and the $\Gamma_{2'}$ conduction band. From the $E(\vec{k})$ diagram we note that the electron effective mass for the $\Gamma_{2'}$ conduction band is very small because of the high curvature of the $\Gamma_{2'}$ band about $\vec{k} = 0$, and this effective mass is isotropic so that the constant energy surfaces are spheres.

:::{figure} images/fig-p1-ch02-13.png
:name: fig-p1-ch02-13
:width: 50%
:align: center
Fig. 2.13: Illustration of the indirect emission of light due to carriers and phonons in Ge. [$h\nu$ is the photon energy; $\Delta E$ is the energy delivered to an electron; $E_p$ is the energy delivered to the lattice (phonon energy)].
:::

The optical properties for germanium show a very weak optical absorption for photon energies corresponding to the indirect gap (see {numref}`fig-p1-ch02-13`). Since the valence and conduction band extrema occur at a different $\vec{k}$-point in the Brillouin zone, the indirect gap excitation requires a phonon to conserve crystal momentum. Hence the threshold for this indirect transition is

```{math}
:label: eq-p1-ch02-6
(\hbar\omega)_{\text{threshold}} = E_{L_1} - E_{\Gamma_{25'}} - E_{\text{phonon}} .
```

The optical absorption for germanium increases rapidly above the photon energy corresponding to the direct band gap $E_{\Gamma_{2'}} - E_{\Gamma_{25'}}$, because of the higher probability for the direct optical excitation process. However, the absorption here remains low compared with the absorption at yet higher photon energies because of the low density of states for the $\Gamma$-point transition, as seen from the $E(\vec{k})$ diagram. Very high optical absorption, however, occurs for photon energies corresponding to the energy separation between the $L_3'$ and $L_1$ bands which is approximately the same for a large range of $\vec{k}$ values, thereby giving rise to a very large joint density of states (the number of states with constant energy separation per unit energy range). A large joint density of states arising from the tracking of conduction and valence bands is found for germanium, silicon and the III–V compound semiconductors, and for this reason these materials tend to have high dielectric constants (to be discussed in Part II of this course which focuses on optical properties).

### 2.3.3 Silicon

From the energy band diagram for silicon shown in {numref}`fig-p1-ch02-14`, we see that the energy bands of Si are quite similar to those for germanium. They do, however, differ in detail. For example, in the case of silicon, the electron pockets are formed around a $\Delta$ point located along the $\Gamma X$ $(100)$ direction. For silicon there are 6 electron pockets within the first Brillouin zone instead of the 8 half-pockets which occur in germanium. The constant energy surfaces are again ellipsoids of revolution with a heavy longitudinal mass and a light transverse effective mass [see {numref}`fig-p1-ch02-11`(e)]. The second type of electron pocket that is energetically favored is about the $L_1$ point, but to fill electrons there, we would need to raise the Fermi energy by $\sim 1$ eV.

:::{figure} images/fig-p1-ch02-14.png
:name: fig-p1-ch02-14
:width: 70%
:align: center
Fig. 2.14: Electronic energy band structure of Si.
:::

Silicon is of course the most important semiconductor for device applications and is at the heart of semiconductor technology for transistors, integrated circuits, and many electronic devices. The optical properties of silicon also have many similarities to those in germanium, but show differences in detail. For Si, the indirect gap [see {numref}`fig-p1-ch02-10`(b)] occurs at $\sim 1$ eV and is between the $\Gamma_{25'}$ valence band and the $\Delta$ conduction band extrema. Just as in the case for germanium, strong optical absorption occurs for large volumes of the Brillouin zone at energies comparable to the $L_3' \to L_1$ energy separation, because of the “tracking” of the valence and conduction bands. The density of electron states for Si covering a wide energy range is shown in {numref}`fig-p1-ch02-15` where the corresponding energy band diagram is also shown. Most of the features in the density of states can be identified with the band model.

:::{figure} images/fig-p1-ch02-15.png
:name: fig-p1-ch02-15
:width: 80%
:align: center
Fig. 2.15: (a) Density of states in the valence and conduction bands of silicon, and (b) the corresponding $E(\vec{k})$ curves showing the symbols of the high symmetry points of the band structure.
:::

### 2.3.4 III–V Compound Semiconductors

Another important class of semiconductors is the III–V compound semiconductors which crystallize in the zincblende structure; this structure is like the diamond structure except that the two atoms/unit cell are of a different chemical species. The III–V compounds also have many practical applications, such as semiconductor lasers for fast electronics and communications, GaAs in light emitting diodes, and InSb for infrared detectors. In {numref}`fig-p1-ch02-16` the $E(\vec{k})$ diagram for GaAs is shown and we see that the electronic levels are very similar to those of Si and Ge. One exception is that the lowest conduction band for GaAs is at $\vec{k} = 0$ so that both valence and conduction band extrema are at $\vec{k} = 0$. Thus GaAs is a direct gap semiconductor [see {numref}`fig-p1-ch02-10`(a)], and for this reason, GaAs shows a stronger and more sharply defined optical absorption threshold than Si or Ge.

:::{figure} images/fig-p1-ch02-16.png
:name: fig-p1-ch02-16
:width: 70%
:align: center
Fig. 2.16: Electronic energy band structure of the III-V compound GaAs.
:::

{numref}`fig-p1-ch02-11`(b) shows a schematic of the conduction bands for GaAs. Here we see that the lowest conduction band for GaAs has high curvature and therefore a small effective mass. This mass is isotropic so that the constant energy surface for electrons in GaAs is a sphere and there is just one such sphere in the Brillouin zone. The next lowest conduction band is at a $\Delta$ point and a significant carrier density can be excited into this $\Delta$-point pocket at high temperatures.

:::{figure} images/fig-p1-ch02-17.png
:name: fig-p1-ch02-17
:width: 70%
:align: center
Fig. 2.17: Electronic energy band structure of the III-V compound InSb.
:::

The constant energy surface for electrons in the direct gap semiconductor InSb shown in {numref}`fig-p1-ch02-17` is likewise a sphere, because InSb is also a direct gap semiconductor. InSb differs from GaAs in having a very small band gap ($\sim 0.2$ eV), occurring in the infrared. Both direct and indirect band gap materials are found in the III–V compound semiconductor family. Except for optical phenomena close to the band gap, these compound semiconductors all exhibit very similar optical properties which are associated with the band-tracking phenomena discussed in §2.3.2.

### 2.3.5 “Zero Gap” Semiconductors – Gray Tin

It is also possible to have “zero gap” semiconductors. An example of such a material is gray tin which also crystallizes in the diamond structure. The energy band model for gray tin without spin–orbit interaction is shown in {numref}`fig-p1-ch02-18`(a). On this diagram the zero gap occurs between the $\Gamma_{25'}$ valence band and the $\Gamma_{2'}$ conduction band, and the Fermi level runs right through this degeneracy point between these bands. Spin–orbit interaction (to be discussed later in this course) is very important for gray tin in the region of the $\vec{k} = 0$ band degeneracy, and a detailed diagram of the energy bands near $\vec{k} = 0$ and including the effect of spin–orbit interaction is shown in {numref}`fig-p1-ch02-18`(b). In gray tin the effective mass for the conduction band is much lighter than for the valence band, as can be seen by the band curvatures shown in {numref}`fig-p1-ch02-18`(b).

:::{figure} images/fig-p1-ch02-18.png
:name: fig-p1-ch02-18
:width: 80%
:align: center
Fig. 2.18: (a) Electronic energy band structure of gray Sn, neglecting the spin-orbit interaction. (b) Detailed diagram of the energy bands of gray tin near $k = 0$, including the spin-orbit interaction. The Fermi level goes through the degenerate point between the filled valence band and the empty conduction band in the idealized model for gray tin at $T = 0$. The $\Gamma_7^-$ hole band has the same symmetry as the conduction band for Ge when spin-orbit interaction is included, as shown in {numref}`fig-p1-ch02-12`(b). The $\Gamma_7^+$ hole band has the same symmetry as the “split-off” valence band for Ge when spin-orbit interaction is included.
:::

Optical transitions in {numref}`fig-p1-ch02-18`(b) labeled B occur in the far infrared spectral region from the upper valence band to the conduction band. In the near infrared, interband transitions labeled A are induced from the $\Gamma_7^-$ valence band to the $\Gamma_8^+$ conduction band. We note that gray tin is classified as a zero gap semiconductor rather than a semimetal (see §2.4) because there are no band overlaps in a zero-gap semiconductor anywhere in the Brillouin zone. Because of the zero band gap in grey tin, impurities play a major role in determining the position of the Fermi level. Gray tin is normally prepared n-type which means that there are some electrons present in the conduction band (for example, a typical electron concentration would be $10^{15}/\mathrm{cm}^3$ which amounts to less than 1 carrier/$10^7$ atoms).

### 2.3.6 Molecular Semiconductors – Fullerenes

Other examples of semiconductors are molecular solids such as C$_{60}$ (see {numref}`fig-p1-ch02-19`). For the case of solid C$_{60}$, we show in {numref}`fig-p1-ch02-19`(a) a C$_{60}$ molecule, which crystallizes in a FCC structure with four C$_{60}$ molecules per conventional simple cubic unit cell. A small distortion of the bonds, lengthening the C–C bond lengths of the single bonds to $1.46$ Å and shortening the double bonds to $1.40$ Å, stabilizes a band gap of $\sim 1.5$ eV [see {numref}`fig-p1-ch02-19`(b)]. In this semiconductor, the energy bandwidths are very small compared with the band gaps, so that this material can be considered as an organic molecular semiconductor. The transport properties of C$_{60}$ differ markedly from those for conventional group IV or III–V semiconductors.

:::{figure} images/fig-p1-ch02-19.png
:name: fig-p1-ch02-19
:width: 80%
:align: center
Fig. 2.19: (a) Structure of the icosahedral C$_{60}$ molecule, and (b) the calculated one-electron electronic energy band structure of FCC solid C$_{60}$. The Fermi energy lies between the occupied valence levels and the empty conduction levels.
:::

## 2.4 Semimetals

Another type of material that commonly occurs in nature is the semimetal. Semimetals have exactly the correct number of electrons to completely fill an integral number of Brillouin zones. Nevertheless, in a semimetal the highest occupied Brillouin zone is not filled up completely, since some of the electrons find lower energy states in “higher” zones (see {numref}`fig-p1-ch02-2`). For semimetals the number of electrons that spill over into a higher Brillouin zone is exactly equal to the number of holes that are left behind. This is illustrated schematically in {numref}`fig-p1-ch02-20`(a) where a two-dimensional Brillouin zone is shown and a circular Fermi surface of equal area is inscribed. Here we can easily see the electrons in the second zone at the zone edges and the holes at the zone corners that are left behind in the first zone. Translation by a reciprocal lattice vector brings two pieces of the electron surface together to form a surface in the shape of a lens, and the 4 pieces at the zone corners form a rosette shaped hole pocket. Typical examples of semimetals are bismuth and graphite. For these semimetals the carrier density is on the order of one carrier/$10^6$ atoms.

:::{figure} images/fig-p1-ch02-20.png
:name: fig-p1-ch02-20
:width: 80%
:align: center
Fig. 2.20: (a) Schematic diagram of a semimetal in two dimensions. (b) Schematic diagram of the energy bands $E(\vec{k})$ of bismuth showing electron pockets at the $L$ point and a hole pocket at the $T$ point. The $T$ point is the point at the Brillouin zone boundary in the $\{111\}$ direction along which a stretching distortion occurs in real space, and the $L$ points refer to the 3 other equivalent $\{1\bar{1}\bar{1}\}$, $\{\bar{1}1\bar{1}\}$, and $\{\bar{1}\bar{1}1\}$ directions.
:::

The carrier density of a semimetal is thus not very different from that which occurs in doped semiconductors, but the behavior of the conductivity $\sigma(T)$ as a function of temperature is very different. For intrinsic semiconductors, the carriers which are excited thermally contribute significantly to conduction. Consequently, the conductivity tends to rise rapidly with increasing temperature. For a semimetal, the carrier concentration does not change significantly with temperature because the carrier density is determined by the band overlap. Since the electron scattering by lattice vibrations increases with increasing temperature, the conductivity of semimetals tends to fall as the temperature increases.

A schematic diagram of the energy bands of the semimetal bismuth is shown in {numref}`fig-p1-ch02-20`(b). Electron and hole carriers exist in equal numbers but at different locations in the Brillouin zone. For Bi, electrons are at the $L$-point, and holes at the $T$-point [see {numref}`fig-p1-ch02-20`(b)]. The crystal structure for Bi can be understood from the NaCl structure by considering a very small displacement of the Na FCC structure relative to the Cl FCC structure along one of the body diagonals and an elongation of that body diagonal relative to the other 3 body diagonals. The special $\{111\}$ direction corresponds to $\Gamma-T$ in the Brillouin zone, while the other three $\{111\}$ directions are labeled as $\Gamma-L$.

Instead of a band gap between valence and conduction bands (as occurs for semiconductors), semimetals are characterized by a band overlap in the millivolt range. In bismuth, a small band gap also occurs at the $L$-point between the conduction band and a lower filled valence band. Because the coupling between these $L$-point valence and conduction bands is strong, some of the effective mass components for the electrons in bismuth are anomalously small. As far as the optical properties of bismuth are concerned, bismuth behaves much like a metal with a high reflectivity at low frequencies due to the presence of free carriers.

## 2.5 Insulators

The electronic structure of insulators is similar to that of semiconductors, in that both insulators and semiconductors have a band gap separating the valence and conduction bands. However, in the case of insulators, the band gap is so large that thermal energies are not sufficient to excite a significant number of carriers.

The simplest insulator is a solid formed of rare gas atoms. An example of a rare gas insulator is solid argon which crystallizes in the FCC structure with one Ar atom/primitive unit cell. With an atomic configuration $3s^2 3p^6$, argon has filled $3s$ and $3p$ bands which are easily identified in the energy band diagram in {numref}`fig-p1-ch02-21`. These occupied bands have very narrow band widths compared to their band gaps and are therefore well described by the tight binding approximation. This figure shows that the higher energy states forming the conduction bands (the hybridized $4s$ and $3d$ bands) show more dispersion than the more tightly bound valence bands. The band diagram shows argon to have a direct band gap at the $\Gamma$ point of about 1 Rydberg or 13.6 eV. Although the $4s$ and $3d$ bands have similar energies, identification with the atomic levels can easily be made near $k = 0$ where the lower lying $4s$-band has considerably more band curvature than the $3d$ levels which are easily identified because of their degeneracies [the so called three-fold $t_g$ ($\Gamma_{25'}$) and the two-fold $e_g$ ($\Gamma_{12}$) crystal field levels for $d$-bands in a cubic crystal].

:::{figure} images/fig-p1-ch02-21.png
:name: fig-p1-ch02-21
:width: 70%
:align: center
Fig. 2.21: Electronic energy band structure of Argon.
:::

Another example of an insulator formed from a closed shell configuration is found in {numref}`fig-p1-ch02-22`. Here the closed shell configuration results from charge transfer, as occurs in all ionic crystals. For example in the ionic crystal LiF (or in other alkali halide compounds), the valence band is identified with the filled anion orbitals (fluorine $p$-orbitals in this case) and at much higher energy the empty cation conduction band levels will lie (lithium $s$-orbitals in this case). Because of the wide band gap separation in the alkali halides between the valence and conduction bands, such materials are transparent at optical frequencies.

:::{figure} images/fig-p1-ch02-22.png
:name: fig-p1-ch02-22
:width: 70%
:align: center
Fig. 2.22: Band structure of the alkali halide insulator LiF. This ionic crystal is used extensively for UV optical components because of its large band gap.
:::

Insulating behavior can also occur for wide bandgap semiconductors with covalent bonding, such as diamond, ZnS and GaP (see {numref}`fig-p1-ch02-23`). The $E(\vec{k})$ diagrams for these materials are very similar to the dispersion relations for typical III–V semiconducting compounds and for the group IV semiconductors silicon and germanium; the main difference, however, is the large band gap separating valence and conduction bands.

:::{figure} images/fig-p1-ch02-23.png
:name: fig-p1-ch02-23
:width: 80%
:align: center
Fig. 2.23: Electronic energy band structure of (a) cubic ZnS, a direct gap semi-insulating II–VI semiconductor, and (b) cubic GaP, an indirect gap semi-insulating III–V semiconductor. These wide bandgap semiconductors are of current interest for their optical properties.
:::

Even in insulators there is often a measurable electrical conductivity. For these materials the band electronic transport processes become less important relative to charge hopping from one atom to another by over-coming a potential barrier. Ionic conduction can also occur in insulating ionic crystals. From a practical point of view, one of the most important applications of insulators is for the control of electrical breakdown phenomena.

The principal experimental methods for studying the electronic energy bands depend on the nature of the solid. For insulators, the optical properties are the most important, while for semiconductors both optical and transport studies are important. For metals, optical properties are less important and Fermi surface studies become more important.

In the case of insulators, electrical conductivity can arise through the motion of lattice ions as they move from one lattice vacancy to another, or from one interstitial site to another. Ionic conduction therefore occurs through the presence of lattice defects, and is promoted in materials with open crystal structures. In ionic crystals there are relatively few mobile electrons or holes even at high temperature, so that conduction in these materials is predominantly due to the motions of ions.

Ionic conductivity ($\sigma_{\text{ionic}}$) is proportional both to the density of lattice defects (vacancies and interstitials) and to the diffusion rate, so that we can write

```{math}
:label: eq-p1-ch02-7
\sigma_{\text{ionic}} \sim e^{-(E+E_0)/k_B T}
```

where $E_0$ is the activation energy for ionic motion and $E$ is the energy for formation of a defect (a vacancy, a vacancy pair, or an interstitial). Being an activated process, ionic conduction is enhanced at elevated temperatures. Since defects in ionic crystals can be observed visibly as the migration of color through the crystal, ionic conductivity can be distinguished from electronic conductivity by comparing the transport of charge with the transport of mass, as can, for example, be measured by the material plated out on electrodes in contact with the ionic crystal.

In this course, we will spend a good deal of time studying optical and transport properties of solids. In connection with topics on magnetism, we will also study Fermi surface measurements which are closely connected to issues relevant to transport properties. Since Fermi surface studies, for the most part, are resonance experiments and involve the use of a magnetic field, it is pedagogically more convenient to discuss these topics in Part III of the course, devoted to Magnetism. We have presented this review of the electronic energy bands of solids because the $E(\vec{k})$ relations are closely connected with a large number of common measurements in the laboratory, and because a knowledge of the $E(\vec{k})$ relations forms the basis for many device applications.

## 2.6 Summary

- Metals (alkali, noble, polyvalent) have partially filled bands, often free-electron-like $E(\vec{k})$ with small gaps, and Fermi surfaces that determine transport and optical interband thresholds.
- Semiconductors have a filled valence band and empty conduction band separated by a gap; direct or indirect gaps and carrier pockets with anisotropic effective masses ({eq}`eq-p1-ch02-5`) follow from the band curvatures.
- Semimetals have equal numbers of electrons and holes due to band overlap, with carrier densities much lower than ordinary metals.
- Insulators have wide band gaps; ionic conduction is thermally activated ({eq}`eq-p1-ch02-7`).
