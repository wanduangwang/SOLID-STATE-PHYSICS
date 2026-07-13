---
title: "4 Superconductivity in High Transition Temperature Cuprate Materials"
abstract: "This chapter reviews the high-transition-temperature cuprate superconductors, including their layered crystal structures, anisotropic superconducting and normal-state transport properties, and the Hall effect."
---

# 4 Superconductivity in High Transition Temperature Cuprate Materials

## 4.0 Overview

This chapter turns to the cuprate superconductors discovered in the late 1980s, which exhibit transition temperatures far above those expected from conventional electron–phonon coupling. We discuss their layered crystal structures, the strongly anisotropic upper critical field, normal-state transport, and the Hall effect. The key equations relate the anisotropic upper critical field to coherence lengths (Eqs. {eq}`eq-p4-ch04-2`–{eq}`eq-p4-ch04-5`), describe the temperature dependence near $T_c$ (Eqs. {eq}`eq-p4-ch04-6`–{eq}`eq-p4-ch04-9`), and introduce phenomenological models for the normal-state resistivity and Hall coefficient (Eqs. {eq}`eq-p4-ch04-10`–{eq}`eq-p4-ch04-12`).

## 4.1 Introduction to High $T_c$ Materials

**References:**

- Tinkham and Lobb, *Solid State Physics*, edited by Ehrenreich and Turnbull, Academic Press, vol **42**, p. 91 (see also other articles in the same volume).
- Poole, Datta and Farach, *Copper Oxide Superconductors*, Wiley–Interscience (1988).
- Phillips, *Physics of High $T_c$ Superconductors*, Academic Press (1989).
- Kamimura and Oshiyama, *Mechanisms of High Temperature Superconductivity*, Springer Series in Materials Science, **11**.
- D.M. Ginsberg, *Physical Properties of High Temperature Superconductors I*, World Scientific (1989).

Using arguments based on the magnitude of the electron–phonon interaction, it was argued that the maximum expected $T_c$ would not exceed $\sim 30\,\mathrm{K}$. Therefore, the discovery of superconductivity in the lanthanum cuprates (La$_{2-x}$Sr$_x$CuO$_4$) in 1986 with $T_c$ values of $\sim 40\,\mathrm{K}$ and soon thereafter in the YBa$_2$Cu$_3$O$_7$ compounds with $T_c \sim 90\,\mathrm{K}$ was so very surprising. Equally surprising was the discovery of such high $T_c$'s in materials with magnetic properties and exhibiting insulating phases.

A number of researchers have drawn attention to the fact that almost all high $T_c$ superconductors are layered compounds. The layering introduces anisotropy into the problem which must be considered both in the normal state and in the superconducting state properties. Whereas many of the conventional superconductors are familiar materials that have been studied in depth, the cuprate superconductors relate to much less familiar materials, which are difficult to prepare in stoichiometric, single phase form, and cannot be described theoretically by simple one-electron band theory. We are now at an early stage in our understanding of the high $T_c$ superconducting materials. The problems are challenging and more difficult than initially envisaged.

:::{figure} images/fig-p4-ch04-1.png
:name: fig-p4-ch04-1
:width: 60%
:align: center
Fig. 4.1: A schematic phase diagram for La$_{2-x}$Sr$_x$CuO$_{4-y}$. The horizontal axis assumes $y = 0$ when $x \neq 0$ and $x = 0$ when $y \neq 0$. The dashed curve separates tetragonal and orthorhombic structures. The insulator (INS)–metal boundary is not shown because of experimental uncertainties. The diagram shows antiferromagnetic (AF) and superconducting (SC) phases which are common to the various high $T_c$ families: La$_{2-x}$Sr$_x$CuO$_{4-y}$, YBa$_2$Cu$_3$O$_{7-\delta}$, and Bi$_2$Sr$_2$Ca$_{1-x}$Y$_x$Cu$_2$O$_{8+y}$.
:::

It has been suggested that the construction of high $T_c$ superconductors can be engineered from basic building block units, consisting of electrically active slabs between which are sandwiched layers which transfer charge to the electrically active slab. Though we focus here on layered superconductors, it is not clear that all high $T_c$ superconductors are necessarily layered, insofar as the $T_c = 30\,\mathrm{K}$ superconductor BiKBaO is a cubic material which also has no copper ions and thus no magnetism.

All the currently studied high $T_c$ superconductor families seem to follow the common phase diagram shown in {numref}`fig-p4-ch04-1`. Here we see that below a threshold value for the hole concentration $x$, there is no superconducting state. According to {numref}`fig-p4-ch04-1`, the stoichiometric compounds are all non-conducting antiferromagnets.

To illustrate the basic building blocks of a typical high $T_c$ superconductor, consider the crystal structure for the layered YBa$_2$Cu$_3$O$_7$ compound in {numref}`fig-p4-ch04-2` where each of the layers is labeled. The structure in {numref}`fig-p4-ch04-2` can be considered in terms of two constituents: the electrically active slab (see {numref}`fig-p4-ch04-3`) which has a chemical formula YBa$_2$Cu$_2$O$_6$ and the intercalate layer CuO, where the Cu and O form chains. This intercalate layer allows entry and departure of oxygen, thereby providing a mechanism for creating a hole concentration necessary for observation of the superconducting phase. In {numref}`fig-p4-ch04-3` we see the basic building blocks and various guest layers that can be introduced between the electrically active YBa$_2$Cu$_2$O$_6$ slabs. If a single intercalate layer is introduced, the result is a $90\,\mathrm{K}$ $T_c$ material, such as YBa$_2$Cu$_3$O$_7$. Various substitutions for Y in terms of a rare earth, or the other substitutions indicated in {numref}`fig-p4-ch04-3`, make little difference to $T_c$. Insertion of two layers (indicated by the two TlO or BiO layers) give rise to a $110\,\mathrm{K}$ $T_c$ material and three layers result in a $125\,\mathrm{K}$ $T_c$ material (which has been prepared with the Tl compounds). If there is no spacer Y layer between the two CuO$_2$ layers we have the La$_2$CuO$_4$ series which yields a $40\,\mathrm{K}$ $T_c$ superconductor. In this case, holes are supplied by the substitution of Sr$^{2+}$ for La$^{3+}$ to yield a family of materials La$_{2-x}$Sr$_x$CuO$_4$.

:::{figure} images/fig-p4-ch04-2.png
:name: fig-p4-ch04-2
:width: 55%
:align: center
Fig. 4.2: The crystal structure of the "123" compound YBa$_2$Cu$_3$O$_7$. On the left, the constituents of each of the layers are indicated.
:::

:::{figure} images/fig-p4-ch04-3.png
:name: fig-p4-ch04-3
:width: 80%
:align: center
Fig. 4.3: Viewing high $T_c$ superconductors in terms of basic building blocks (host material) between which an intercalate layer (or multilayer) is introduced. In general, the larger the number of intercalate layers, the greater the $T_c$ value.
:::

One advantage of viewing the high $T_c$ materials in this way might perhaps be the prediction of new arrangements of the building blocks to achieve higher $T_c$ materials. It is still too soon to be able to judge whether this approach will indeed guide the synthesis of new high $T_c$ materials. It is likely that some new ideas might be needed to produce materials with $T_c$ in the $200\,\mathrm{K}$ range.

Most of the high $T_c$ materials are layered compounds with nearly tetragonal crystal structures. In the superconducting phase, they tend to be orthorhombic, but having lattice constants close to those in the corresponding tetragonal phase which is stable at high temperatures. The orthorhombic distortion causes the distance between two oxygens on one diagonal in the CuO$_2$ planes to be slightly different from the distance between the two oxygens along the other diagonal (see {numref}`fig-p4-ch04-4`).

:::{figure} images/fig-p4-ch04-4.png
:name: fig-p4-ch04-4
:width: 80%
:align: center
Fig. 4.4: Structures of the orthorhombic ($x = 0$) and tetragonal ($x = 0.7$) phases of YBa$_2$Cu$_3$O$_{7-x}$.
:::

Because of the basic layering of the crystal structure of the high $T_c$ materials, the critical magnetic fields and the critical currents are also anisotropic in contrast to the simpler superconductors discussed in Chapters 1–3. The transition temperature $T_c$ is a scalar and is unaffected by crystalline anisotropy. It should be emphasized that conventional BCS superconductors can also be anisotropic. On the other hand, since anisotropy is so widespread in the high $T_c$ superconductors, some generalization of the previous discussion of the critical field (see Chapter 1, §1.2.1) is necessary. A similar generalization of the critical current concept is also needed.

## 4.2 Anisotropic Superconducting Properties

The superconductivity of single crystal YBa$_2$Cu$_3$O$_{7-\delta}$ exhibits a distinct dependence on the magnitude of the magnetic field as well as the field orientation with respect to the crystalline axes. Similar effects are seen in the other families of high $T_c$ superconductors, e.g., La$_{2-x}$Sr$_x$CuO$_4$ and Bi$_2$Sr$_2$CaCu$_2$O$_{8+y}$. This anisotropy of the superconducting properties is seen more clearly in plots of the angular dependence of the upper critical field (see {numref}`fig-p4-ch04-5`). Here, values of the magnetic field at which the resistivity first appears and those at which it reaches $10\%$, $30\%$, $50\%$ are plotted against the angle $\theta$ between the magnetic field and the $c$-axis. Because of the extremely high $H_{c2}$, especially for $H \perp c$-axis, data of the sort shown in {numref}`fig-p4-ch04-5` can be taken for the whole angular range only at temperatures very close to $T_c$.

:::{figure} images/fig-p4-ch04-5.png
:name: fig-p4-ch04-5
:width: 55%
:align: center
Fig. 4.5: Angular dependence of the upper critical fields determined by different criteria, i.e., zero-resistance, $10\%$, $30\%$ and $50\%$ of the normal resistance. The angle $\theta$ denotes the angle of the magnetic field from the $c$-axis. The dashed curves represent the best fit of Eq. {eq}`eq-p4-ch04-1`.
:::

The angular dependence of the upper critical field (for all the definitions employed in {numref}`fig-p4-ch04-5`) follows the relation:

```{math}
:label: eq-p4-ch04-1
\left(\frac{H_{c2}(\theta)\cos\theta}{H_{c2}^{\parallel}}\right)^2 + \left(\frac{H_{c2}(\theta)\sin\theta}{H_{c2}^{\perp}}\right)^2 = 1,
```

where $\theta$ is the angle between the magnetic field and the $c$-axis direction and $H_{c2}^{\parallel}$ and $H_{c2}^{\perp}$ are the upper critical fields for $H \parallel c$-axis and that for $H \perp c$-axis, respectively. The dashed curves in this figure show the good fit of Eq. {eq}`eq-p4-ch04-1` to the experimental points. Although Eq. {eq}`eq-p4-ch04-1` is applicable to many anisotropic conventional (BCS) superconductors, the main difference for the high $T_c$ superconductors as mentioned above is the large magnitude of $H_{c2}$, which makes it difficult to carry out the measurements because of the limitations of laboratory fields ($\sim 30$ tesla for dc and $\sim 150$ tesla for pulsed fields). The critical fields $H_{c2}^{\parallel}$ and $H_{c2}^{\perp}$ of Eq. {eq}`eq-p4-ch04-1` are related (see Eqs. {eq}`eq-p4-ch04-2` and {eq}`eq-p4-ch04-3`) to the in-plane and the $c$-axis coherence lengths, $\xi_{ab}$ and $\xi_c$, by

```{math}
:label: eq-p4-ch04-2
H_{c2}^{\parallel} = \frac{\Phi_0}{2\pi\xi_{ab}^2}
```

```{math}
:label: eq-p4-ch04-3
H_{c2}^{\perp} = \frac{\Phi_0}{2\pi\xi_{ab}\xi_c}.
```

From these expressions we can expect that as $H_{c2}$ increases to very large values, the coherence lengths become small. Small $\xi$ values ($\xi_c \approx 3\,\mathring{\mathrm{A}}$ and $\xi_{ab} \approx 10\,\mathring{\mathrm{A}}$) and high anisotropy ratios $(\xi_{ab}/\xi_c) \sim 5$ are characteristic of high $T_c$ materials. The effective mass model (not discussed in these lectures) is applicable to the case where the anisotropy is not too large and the superconductivity can essentially be treated as three-dimensional. The $H_{c2}$ anisotropy is then related to the effective mass anisotropy by

```{math}
:label: eq-p4-ch04-4
\frac{H_{c2}^{\perp}}{H_{c2}^{\parallel}} = \frac{\xi_{ab}}{\xi_c} = \left(\frac{m_c}{m_{ab}}\right)^{1/2}
```

where $m_{ab}$ and $m_c$ are the in-plane and $c$-axis effective masses, respectively. In the simple case where the conductivity anisotropy is also determined by the mass anisotropy, the relation $(H_{c2}^{\perp}/H_{c2}^{\parallel})^2 \sim (\rho_c/\rho_{ab})$ is expected to hold. These relations between the superconducting and normal state parameters seem to hold well for the YBa$_2$Cu$_3$O$_{7-\delta}$ family of high $T_c$ superconductors, at least, as reported by some workers.

Another phenomenological model for the angular dependence of $H_{c2}(\theta)$ is the Tinkham model for a thin film superconductor, in which $H_{c2}(\theta)$ is given implicitly by the relation

```{math}
:label: eq-p4-ch04-5
\left(\frac{H_{c2}(\theta)\sin\theta}{H_{c2}^{\perp}}\right)^2 + \left|\frac{H_{c2}(\theta)\cos\theta}{H_{c2}^{\parallel}}\right| = 1.
```

Equation {eq}`eq-p4-ch04-5` was introduced to explain the critical anisotropy for thin film superconductors. Equation {eq}`eq-p4-ch04-5` seems to be more appropriate than Eq. {eq}`eq-p4-ch04-1` for the more two-dimensional family of high $T_c$ superconductors Bi$_2$Sr$_2$CaCu$_2$O$_{8+x}$ (Bi-1212) which have a larger anisotropy than YBa$_2$Cu$_3$O$_{7-\delta}$. A distinct feature of the Tinkham model is that $H_{c2}(\theta)$ shows a cusp at $\theta = \pi/2$ (i.e., for $\vec{H} \perp c$-axis). In practice, inhomogeneities in the high $T_c$ samples make it difficult to identify such features uniquely.

:::{figure} images/fig-p4-ch04-6.png
:name: fig-p4-ch04-6
:width: 55%
:align: center
Fig. 4.6: Temperature dependence of the $ab$-plane resistivity at various magnetic field values of a YBa$_2$Cu$_3$O$_{7-\delta}$ single crystal in magnetic fields applied parallel and perpendicular to the $c$-axis (Iye et al., *Physica* C153–155, 26 (1988)).
:::

The temperature dependence of the resistivity for various values of the magnetic field are shown in {numref}`fig-p4-ch04-6` and permit an evaluation of the temperature dependence of $H_{c2}^{\parallel}$ and $H_{c2}^{\perp}$. Two sets of $H_{c2}$ data corresponding to different definitions for $T_c$ are shown in {numref}`fig-p4-ch04-7`. The circle points associated with the solid curves in {numref}`fig-p4-ch04-7` are those defined by the zero-resistance points, and the triangles associated with the dashed curves are those defined by the mid-points of the resistive transition.

:::{figure} images/fig-p4-ch04-7.png
:name: fig-p4-ch04-7
:width: 80%
:align: center
Fig. 4.7: Temperature dependence of $H_{c2}^{\parallel}$ and $H_{c2}^{\perp}$, defined by the zero-resistance points and the mid-points. These $H_{c2}(T)$ data show positive curvature characteristic of many layered superconductors, but otherwise not generally found. The estimated coherence lengths are $\xi_{ab} \sim 25\,\mathring{\mathrm{A}}$ and $\xi_c \sim 6.3\,\mathring{\mathrm{A}}$ from the zero-resistance curves, and $\xi_{ab} \sim 17\,\mathring{\mathrm{A}}$ and $\xi_c \sim 3.9\,\mathring{\mathrm{A}}$ from the mid-point curves (Iye et al., *Physica* C153–155, 26 (1988)).
:::

Tinkham and coworkers have fit the resistivity vs. temperature curves in {numref}`fig-p4-ch04-6` to a model based on an activation energy, associated with the energy to unpin a vortex bound to a defect. For practical applications of type II superconductors, strong vortex pinning is necessary. The technology of solving the flux pinning problem in high $T_c$ superconductors is a major challenge with regard to practical utilization of these materials. Likewise, the technology to produce practical high $T_c$ materials with high current carrying capacity (i.e., high $j_c$) is another major challenge.

In the framework of the Ginzburg-Landau (GL) theory, the temperature dependence of $H_{c2}$ is given by the temperature dependence of the coherence length $\xi(T)$ which has a mean field form

```{math}
:label: eq-p4-ch04-6
\xi(T) \sim \left(1 - \frac{T}{T_c}\right)^{-1/2}.
```

A Taylor expansion of $H_{c2}(T)$ about $T_c$ yields a linear temperature dependence of $H_{c2}$ near $T_c$

```{math}
:label: eq-p4-ch04-7
H_{c2}^{\parallel} = \left|\frac{dH_{c2}^{\parallel}}{dT}\right|_{T_c} (T_c - T),
```

```{math}
:label: eq-p4-ch04-8
H_{c2}^{\perp} = \left|\frac{dH_{c2}^{\perp}}{dT}\right|_{T_c} (T_c - T),
```

where $\left|dH_{c2}^{\parallel}/dT\right|_{T_c}$ and $\left|dH_{c2}^{\perp}/dT\right|_{T_c}$ are the critical field slopes near $T_c$. Further assumptions are needed to obtain $H_{c2}(T)$ over a wider temperature range.

A method widely employed in deriving the low temperature coherence lengths is to estimate $H_{c2}^{\parallel}(0)$ and $H_{c2}^{\perp}(0)$ using the Werthamer-Helfand-Hohenberg (BCS) formula for a type II superconductor

```{math}
:label: eq-p4-ch04-9
H_{c2}(0) = 0.69 \left|\frac{dH_{c2}}{dT}\right|_{T_c} T_c
```

for both $H_{c2}^{\parallel}$ and $H_{c2}^{\perp}$, where the zero temperature values are deduced from the slope of the critical field curves near $T_c$. This formula unfortunately does not work well for layered conventional superconductors. But since ordinarily available laboratory magnetic fields are not large enough to probe $H_{c2}$ at low temperatures, Eq. {eq}`eq-p4-ch04-9` is used to obtain rough estimates for $H_{c2}$ near $T = 0$ (recently $H_{c2}$ has been measured directly using megagauss fields available at the University of Tokyo). From Eq. {eq}`eq-p4-ch04-9`, the measurements of $H_{c2}$ near $T_c$ can be used to estimate $\xi_{ab}(0)$ and $\xi_c(0)$ using Eqs. {eq}`eq-p4-ch04-2` and {eq}`eq-p4-ch04-3`. Experiments in YBa$_2$Cu$_3$O$_7$ by Worthington et al. estimated $H_{c2}^{\perp} \sim 64$ tesla and $H_{c2}^{\parallel} \sim 400$ tesla which correspond to $\xi_{ab} \sim 17\,\mathring{\mathrm{A}}$ and $\xi_c \sim 3.5\,\mathring{\mathrm{A}}$.

The experimental determination of $H_{c2}(0)$ and $\xi(0)$ in high $T_c$ superconductors is ambiguous to some degree because of the broadening of the resistive transition in magnetic fields (see {numref}`fig-p4-ch04-7`) and the upward curvature of $H_{c2}(T)$ (i.e., $\partial^2 H_{c2}(T)/\partial T^2 > 0$) near $T_c$. The values of the coherence length extracted from the $H_{c2}$ measurements appear to lie in the range, $15 < \xi_{ab} < 35\,\mathring{\mathrm{A}}$ and $2 < \xi_c < 7\,\mathring{\mathrm{A}}$, for YBa$_2$Cu$_3$O$_{7-\delta}$. For such small values for the $c$-axis coherence lengths, we see that $\xi_c$ is comparable to or less than the corresponding unit cell distances. Bi$_2$Sr$_2$CaCu$_2$O$_{8+x}$ shows a larger $H_{c2}$ anisotropy and a shorter $c$-axis coherence length compared with YBa$_2$Cu$_3$O$_{7-\delta}$, indicating that the former is more two-dimensional, a result consistent with the resistivity anisotropy data.

## 4.3 Anisotropic Normal State Transport Properties

A great deal of work has been done on all properties of high $T_c$ materials in normal and superconducting state: transport, thermal, optical, lattice, magnetic, elastic, microwave, to mention a few. We briefly discuss transport to give some perspective on the difficulties of these studies.

The anisotropic superconducting properties arise from anisotropic normal state properties. An overall view of the temperature dependence of the normal state resistivities of (La$_{1-x}$Sr$_x$)$_2$CuO$_4$ and YBa$_2$Cu$_3$O$_{7-\delta}$ (see {numref}`fig-p4-ch04-8`) show that the $\rho$ values are rather high for metallic systems but $\rho(T)$ still exhibits a remarkably large linear $T$ metallic behavior over a wide temperature range. {numref}`fig-p4-ch04-8` presents a comparison of the temperature dependences of the normal state resistivity of high $T_c$ compounds with those of a weak electron–phonon coupling metal (Cu) and a strong electron–phonon coupling metal (V$_3$Si) showing saturation in the resistivity $\rho(T)$ at high temperatures. The absence of resistivity saturation in the high $T_c$ superconductors at higher temperatures indicates that the carrier mean free path is longer than the atomic distance throughout the whole temperature range. From this result it is concluded that the electron–phonon coupling in high $T_c$ superconductors is weaker than that in the A15 superconductors which have high $T_c$ values in comparison to most conventional superconductors.

:::{figure} images/fig-p4-ch04-8.png
:name: fig-p4-ch04-8
:width: 55%
:align: center
Fig. 4.8: Comparison of the temperature dependence of the resistivity of the high $T_c$ superconductors with typical metals. The linear $T$ dependence of the resistivities of (La$_{1-x}$Sr$_x$)$_2$CuO$_4$ and YBa$_2$Cu$_3$O$_{7-\delta}$ are in marked contrast with the resistivity saturation in the strong electron–phonon coupling metal V$_3$Si. Also note the high values of $\rho$ for the high $T_c$ materials in the normal state. The increase in the resistivity of YBa$_2$Cu$_3$O$_{7-\delta}$ above $\sim 600\,\mathrm{K}$ is due to oxygen desorption (M. Gurvitch and A.T. Fiory, *Phys. Rev. Lett.* **59**, 1337 (1987)).
:::

The first measurement of the normal state resistivity anisotropy in YBa$_2$Cu$_3$O$_{7-\delta}$ (made with electrical contacts at the four corners of a $c$-axis containing facet of a single crystal sample) showed a metallic linear $T$ dependence for the $ab$-plane resistivity, $\rho_{ab}$, but the $c$-axis resistivity, $\rho_c$, showed a semiconductor-like temperature dependence. The anisotropy ratio $\rho_c/\rho_{ab}$ was about $30$ at room temperature and increased to $\sim 80$ at $T_c$. More detailed results (K. Murata, K. Hayashi, Y. Honda, M. Tokumoto, H. Ihara, M. Hirabayashi, N. Terada and Y. Kimura, *Jpn. J. Appl. Phys.* **26**, L1941 (1987)) as shown in {numref}`fig-p4-ch04-9` stimulated a great deal of theoretical interest.

:::{figure} images/fig-p4-ch04-9.png
:name: fig-p4-ch04-9
:width: 80%
:align: center
Fig. 4.9: Temperature dependence of $\rho_{ab}$ and $\rho_c$ of three single crystals (A, B, C) of YBa$_2$Cu$_3$O$_{7-\delta}$. The $\rho_c(T)$ curves show an upturn near $T_c$. The right hand side of the figure shows the $\rho_c T$ versus $T^2$ plot which was interpreted to support the validity of Anderson's RVB relation $\rho_c = AT + B/T$ (Hagen et al., *Phys. Rev.* **B37**, 7928 (1988)).
:::

Anderson and Zou (P.W. Anderson and Z. Zou, *Phys. Rev. Lett.* **60**, 132 (1988)) proposed that the $\rho_c$ data shown in {numref}`fig-p4-ch04-9` could be fitted to a functional form

```{math}
:label: eq-p4-ch04-10
\rho_c(T) = AT + \frac{B}{T}.
```

and claimed that the behavior $\rho_{ab} \sim T$ and $\rho_c \sim 1/T$ approximately fits the holon–spinon transport scheme of the "resonating valence bond" (RVB) theory. The scenario for transport in the RVB model is as follows.

The spin degrees of freedom in the two-dimensional CuO$_2$ network are carried by Fermion excitations called spinons. Chemical doping produces a hole which introduces a spin $1/2$ and a charge $+1$ into the system. These charge and spin degrees of freedom are decoupled in the RVB model to yield a spinon and a positively charged Boson called a holon. Transport current within each CuO$_2$ plane is carried by holons. The dominant scatterers for a holon are thermally excited spinons. The number of thermally excited spinons is proportional to $T$, from which the linear $T$ dependence of the in-plane resistivity arises. On the other hand, transport along the $c$-axis involves interlayer tunneling of electrons. Because a holon is an entity only meaningful within each CuO$_2$ layer, the interlayer tunneling requires real holes. The tunneling process therefore occurs by

- creation of a real hole by the temporary union of a holon and a spinon
- interlayer tunneling of the real hole
- dissociation of the hole to a holon and a spinon in the new layer.

The probability of the interlayer tunneling is determined by the frequency at which a holon encounters a spinon, and therefore is proportional to the number of available spinons. Thus, for the transport along the $c$-axis, the conductivity rather than the resistivity is proportional to $T$.

{numref}`fig-p4-ch04-10` shows more recent experimental results by Iye et al. of $\rho_{ab}$ and $\rho_c$ for two different single crystal samples of YBa$_2$Cu$_3$O$_{7-\delta}$. These results clarify previous work. Whether the intrinsic $\rho_c(T)$ is metallic or semiconducting is extremely important, because the latter result strongly suggests the RVB transport mechanism. The current experimental situation of the anisotropic resistivity of YBa$_2$Cu$_3$O$_{7-\delta}$ may be summarized as follows:

:::{figure} images/fig-p4-ch04-10.png
:name: fig-p4-ch04-10
:width: 80%
:align: center
Fig. 4.10: Temperature dependence of $\rho_{ab}$ and $\rho_c$ for two single crystal samples of YBa$_2$Cu$_3$O$_{7-\delta}$ with different oxygen stoichiometries. Sample A is a fully oxygenated sample, while sample B is a somewhat oxygen-deficient sample. The fully oxygenated sample shows a metallic $\rho_{ab}$ and $\rho_c$. The right hand side of the figure illustrates the electrode configuration for the measurements of various transport coefficients (Iye et al., *Physica* C153–155, 26 (1988)).
:::

- There is general consensus on the following two points:
  1. $\rho_{ab}$ increases linearly with temperature from $T_c$ up to $\sim 600\,\mathrm{K}$. The behavior above $\sim 600\,\mathrm{K}$ is related to oxygen desorption and therefore depends on the ambient oxygen pressure and diffusion kinetics. The linear $T$ dependence extrapolation to $T = 0$ gives a very small intercept for good samples.
  2. $\rho_c$ of an oxygen-deficient sample is semiconductor-like. In the case of a highly oxygen-deficient non-superconducting sample, both $\rho_{ab}$ and $\rho_c$ are of course semiconducting.

- The controversial point is whether the $\rho_c(T)$ of an ideally oxygenated sample is metallic or semiconductor-like.
  1. Those who regard the semiconductor-like behavior of $\rho_c$ as intrinsic attribute the metallic behavior observed by others to electrical shorting by $\rho_{ab}$ components due to imperfect crystallinity.
  2. Those who think that the intrinsic $\rho_c$ is metallic, regard the semiconductor-like data as a sign of presence of a microcrack and/or a poorly oxygenated interior region of a single crystal.

The disparity of the experimental data among different groups obviously stems from the strong dependence of electronic properties on the oxygen stoichiometry and from the difficulty of preparing defect-free large single crystals with controlled oxygen stoichiometry. Because the oxygen diffusion kinetics in single crystals is many orders of magnitude slower than in the case of sintered polycrystals, it is necessary to exercise great care when processing a single crystal by oxygen annealing to ensure uniform oxygen concentration. An oxygen concentration gradient from surface to interior of a single crystal can severely distort transport measurements.

An accurate determination of the anisotropy ratio $\rho_c/\rho_{ab}$ is very difficult experimentally. The two-dimensionality of the transport phenomena would seem to require a larger anisotropy than has yet been reported (e.g., $\rho_c/\rho_{ab} > 10^4$ would strongly suggest 2D behavior). The anisotropies reported to date suggest that the high $T_c$ superconductors are all anisotropic 3D materials as far as their normal state properties are concerned.

Let us now briefly review the results on other cuprates. While large single crystals of the undoped material La$_2$CuO$_4$ are available, high quality single crystals of the Sr doped materials La$_{2-x}$Sr$_x$CuO$_4$ are difficult to grow. The anisotropic resistivity of superconducting single crystals of La$_{2-x}$Sr$_x$CuO$_{4-y}$ ($x \sim 0.08$) were measured and the data show an upturn of $\rho_c$ at lower temperatures and the anisotropy of $\rho_c/\rho_{ab} \sim 10$. A few studies on the resistivity anisotropy of Bi$_2$Sr$_2$CaCu$_2$O$_{8+x}$ single crystals were recently published and were reported to both show metallic behavior with an extremely large anisotropy ratio ($\sim 10^5$). However other experimentalists disagree, so the case of Bi$_2$Sr$_2$CaCu$_2$O$_{8+x}$ is similar to that of YBa$_2$Cu$_3$O$_{7-\delta}$ where significant experimental questions remain to be resolved.

:::{figure} images/fig-p4-ch04-11.png
:name: fig-p4-ch04-11
:width: 55%
:align: center
Fig. 4.11: The plasmon dependence of $T_c$. The points labeled BiSC refer to Bi$_2$Sr$_2$CaCu$_2$O$_{8+x}$, those labeled YBC refer to YBa$_2$Cu$_3$O$_{7-\delta}$, while those labeled LSC refer to La$_{2-x}$Sr$_x$CuO$_4$.
:::

A number of optical experiments have been made on high $T_c$ superconductors. A scaling between $T_c$ and the plasma frequency is shown in {numref}`fig-p4-ch04-11`. These results show a clear correlation between $T_c$ and $\omega_p^2$, which in turn depends on the hole concentration.

## 4.4 The Hall Effect in High $T_c$ Materials

Hall effect measurements have been helpful in distinguishing between the carrier density and mobility contributions to the electrical conductivity and in determining the sign of the dominant carrier type. Because of the high anisotropy of the transport properties, single crystal samples are needed to obtain definitive information (see {numref}`fig-p4-ch04-12`).

:::{figure} images/fig-p4-ch04-12.png
:name: fig-p4-ch04-12
:width: 80%
:align: center
Fig. 4.12: Temperature dependence of the anisotropic Hall coefficient $\mathcal{R}_H$ of the same two single crystals of YBa$_2$Cu$_3$O$_{7-\delta}$ as in {numref}`fig-p4-ch04-10`. The Hall coefficient for $\vec{H} \parallel ab$-plane and $\vec{H} \parallel c$-axis show a striking difference in sign and temperature dependence. The insert shows the characteristic linear $T$ behavior of $1/\mathcal{R}_H$ of YBa$_2$Cu$_3$O$_{7-\delta}$ for two crystals with widely different carrier concentrations (Iye et al., *Physica* C153–155, 26 (1988)).
:::

Early measurements of the Hall constant $\mathcal{R}_H$ with Sr doped La$_{2-x}$Sr$_x$CuO$_4$ showed a positive sign of $\mathcal{R}_H$ and the functional dependence $1/\mathcal{R}_H \sim x$ which contradicted the prediction of the band model and suggested that electron correlation is essential in understanding the electronic structure of the present system. Similar conclusions were reached by studies of the variation of the Hall constant with oxygen-deficiency $\delta$ in the YBa$_2$Cu$_3$O$_{7-\delta}$ system.

The $ab$-plane Hall coefficient of YBa$_2$Cu$_3$O$_{7-\delta}$ has the following features:

1. The sign of the Hall coefficient $\mathcal{R}_H$ is positive, i.e., hole-like.
2. $\mathcal{R}_H$ is very sensitive to the oxygen stoichiometry and increases rapidly with increasing oxygen-deficiency $\delta$.
3. $\mathcal{R}_H$ exhibits a striking temperature dependence. For well oxygenated samples ($90\,\mathrm{K}$ superconductors) the temperature dependence is such that the apparent carrier density $1/e\mathcal{R}_H$ varies linearly with $T$ extrapolating to nearly zero at $T = 0$.

The Hall coefficient of polycrystalline samples essentially reflects that of single crystals for the experimental configuration $\vec{j} \parallel ab$-plane and $\vec{H} \parallel c$-axis.

The insert figures in {numref}`fig-p4-ch04-12` demonstrate the linear $T$ dependence of $1/e\mathcal{R}_H$. Normally, $\mathcal{R}_H$ for metals has a linear $T$ dependence. The unusual temperature dependence of {numref}`fig-p4-ch04-12` is commonly observed in YBa$_2$Cu$_3$O$_{7-\delta}$ samples, including samples with very different magnitudes of the Hall constant (due to different oxygen contents). A linear temperature dependence for $1/e\mathcal{R}_H$ would imply a diminishing carrier concentration at low temperatures, a strange occurrence for a metallic system. Moreover, essential constancy of the carrier concentration has been established by the penetration depth measurements by the muon spin rotation technique. Therefore, different interpretations have been proposed for the linear $T$ dependence of $1/e\mathcal{R}_H$.

Using a two-band model, the resistivity and the Hall mobility are expressed in terms of the densities $n_e$ and $n_h$ and mobilities $\mu_e$ and $\mu_h$ of electrons and holes:

```{math}
:label: eq-p4-ch04-11
\rho = \frac{1}{n_h |e| \mu_h + n_e |e| \mu_e}
```

```{math}
:label: eq-p4-ch04-12
\mathcal{R}_H = \frac{n_h \mu_h^2 - n_e \mu_e^2}{|e|c\,(n_h \mu_h + n_e \mu_e)^2}
```

In this model the temperature dependence of $\mathcal{R}_H$ reflects a temperature dependent compensation between electrons and holes. It is not generally possible to uniquely determine the values of the parameters $n_e$, $n_h$, $\mu_e$ and $\mu_h$ from experimental data of $\mathcal{R}_H(T)$ and $\rho(T)$. It has been recognized that in order to reproduce the $\mathcal{R}_H \sim 1/T$ and $\rho \sim T$ behavior in terms of the two-band model one has to assume a very unusual special relation among the parameters. The lack of a pressure dependence of $\mathcal{R}_H$ poses a further constraint on the simple two-band model. At present, the Hall effect data for YBa$_2$Cu$_3$O$_{7-\delta}$ remain to be fully elucidated.

Temperature dependent Hall measurements have also been observed in La$_{2-x}$Sr$_x$CuO$_4$ and Bi$_2$Sr$_2$CaCu$_2$O$_{8+x}$, though the temperature dependence of $\mathcal{R}_H$ is much weaker than for YBa$_2$Cu$_3$O$_{7-\delta}$ and what is more important, the unusual behavior of $1/\mathcal{R}_H \sim T$ is not observed. Since the $1/\mathcal{R}_H \sim T$ behavior may be specific to YBa$_2$Cu$_3$O$_{7-\delta}$, it is concluded that this effect probably does not have a direct relation to the mechanism of high temperature superconductivity. It may be that the $1/\mathcal{R}_H \sim T$ behavior is common to many high $T_c$ compounds and is a sign of the unconventional normal state from which high temperature superconductivity emerges. Whether this unusual $T$ dependence of the Hall constant can be explained within the framework of relatively conventional models or requires an exotic conduction mechanism (e.g., RVB) remains to be clarified.

Our current knowledge of the anisotropy of the Hall effect in YBa$_2$Cu$_3$O$_{7-\delta}$ may be summarized as follows:

1. The Hall effect for $\vec{H} \parallel c$-axis is positive and $1/e\mathcal{R}_H$ varies linearly with temperature.
2. $\mathcal{R}_H$ for $\vec{H} \parallel ab$-plane is much smaller than that for $\vec{H} \parallel c$-axis, which is the reason why the Hall data on ceramic samples essentially reflect the latter.
3. $\mathcal{R}_H$ for $\vec{H} \parallel ab$-plane is negative and seems to have a temperature dependence quite different from that for $\vec{H} \parallel c$-axis.

Such a complicated dependence of the Hall effect on the magnetic field orientation implies a complicated Fermi surface topology, or may provide evidence for an exotic transport mechanism along with the unusual temperature dependence.

:::{figure} images/fig-p4-ch04-13.png
:name: fig-p4-ch04-13
:width: 80%
:align: center
Fig. 4.13: Temperature dependence of the anisotropic thermoelectric power of single crystal samples of YBa$_2$Cu$_3$O$_{7-\delta}$. Note the qualitative difference in the temperature dependence for the two directions of heat flow.
:::

The anisotropy of the thermoelectric power of YBa$_2$Cu$_3$O$_{7-\delta}$ has been measured by a few groups (Ong et al., *Physica* C153–155, 1072 (1988)), but the results are not in good agreement from one group to another. Some authors show a positive thermopower for both $S_{ab}$ and $S_c$ (see {numref}`fig-p4-ch04-13`) while other authors show $S_{ab} < 0$ and $S_c > 0$. There is however agreement that the functional form of the temperature dependence $S_{ab}(T)$ is very different from $S_c(T)$.

:::{figure} images/fig-p4-ch04-14.png
:name: fig-p4-ch04-14
:width: 55%
:align: center
Fig. 4.14: Thermal conductivity of single crystal La$_2$CuO$_{4-y}$ for the heat flow $Q \parallel [001]$ (top, closed circles), $Q \parallel [221]$ (middle, open circles) and $Q \parallel [110]$ (bottom, triangles). The dashed line represents results on a polycrystalline sintered sample. The inset shows a schematic diagram of La$_2$CuO$_{4-y}$ in terms of the tetragonal coordinate system used (D.T. Morelli, J. Heremans, G.L. Doll, P.J. Picone, H.P. Jenssen and M.S. Dresselhaus, *Phys. Rev.* **B39**, 804 (1989)).
:::

Thermal conductivity experiments have also been carried out on both single crystal and polycrystalline of oxygen-deficient La$_2$CuO$_{4-y}$ samples (see {numref}`fig-p4-ch04-14`), showing interesting magnon contributions to the thermal conductivity and a high degree of anisotropy.
