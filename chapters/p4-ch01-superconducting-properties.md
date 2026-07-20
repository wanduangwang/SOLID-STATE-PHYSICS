---
title: "1 Superconducting Properties of Solids"
abstract: "The defining properties of superconductors are surveyed: zero DC resistivity (perfect conductivity), perfect diamagnetism (Meissner effect), flux quantization, an energy gap in the excitation spectrum, isotope effect indicating electron-phonon coupling, and thermodynamic relations distinguishing first-order phase transitions."
---

# 1 Superconducting Properties of Solids

## References

* Ashcroft and Mermin, *Solid State Physics*, Chapter 34.
* Kittel, *Introduction to Solid State Physics*, 6th Ed., Chapter 12.
* T. van Duzer and C.W. Turner, *Principles of Superconductive Devices and Circuits*, Elsevier, NY (1981).
* M. Tinkham, *Introduction to Superconductivity*, McGraw-Hill, 1975.
* T.P. Orlando, *Foundations of Applied Superconductivity*. Addison-Wesley, 1991.

Superconductors exhibit a unique set of properties. These unique properties are summarized in this chapter.

## 1.1 Perfect Conductivity $R = 0$ (1911)

The resistance of a normal metal gradually decreases as the temperature is lowered and levels off at very low temperatures (see {numref}`fig-p4-ch01-1`). The resistance at absolute zero is determined by electrons scattered by impurities and defects in the metal (see Part I, Chapter 1). Many metals, however, undergo a phase transition to the superconducting state (see Fig. 1.1), whereby these metals have zero resistance below some temperature, $T_c$, the **superconducting transition temperature** (see {numref}`fig-p4-ch01-1`). The phase transition to a superconducting phase effect was discovered by Kamerlingh Onnes in 1911, shortly after he had for the first time liquefied helium (boiling point $= 4.2$ K). Some typical $T_c$'s for elemental superconductors are $9.25$ K for Niobium (Nb), $7.2$ K for lead (Pb), $1.1$ K for Al, and even silicon is superconducting under pressure at $7.1$ K! Some typical $T_c$'s for important elemental superconductors are given in Table 1.1. However, noble metals like copper (Cu), gold (Au) and silver (Ag) have not yet been found to undergo a superconducting transition for temperatures as low as a few millidegrees Kelvin. Until 1986, the highest known transition temperature was $23.2$ K for $\mathrm{Nb}_3\mathrm{Ge}$. This is one reason why the scientific community was so surprised by the discovery in 1986 of high $T_c$ superconductivity in transition metal cuprate compounds, with $T_c$ values far exceeding the previous record of $23.2$ K, and by 1987 $T_c$ values of $> 120$ K were reported, ushering in a new period of high research activity on high $T_c$ superconducting materials.

:::{figure} images/fig-p4-ch01-1.png
:name: fig-p4-ch01-1
:width: 60%
:align: center
Figure 1.1: Low temperature resistance of a typical normal metal (upper curve), showing a dc resistivity at low temperatures of the form $\rho = \rho_0 + AT^5$ and a superconductor (lower curve), showing zero resistivity below the superconducting transition temperature $T_c$.
:::

:::{table} Superconducting transition temperatures ($T_c$) and critical magnetic fields ($H_c$) for some typical elemental superconductors.
:name: tab-p4-ch01-1
| Material | $T_c$ (K) | $H_c$ (gauss) |
|----------|-----------|----------------|
| Al       | 1.1       | 99             |
| Sn       | 3.7       | 305            |
| Pb       | 7.2       | 803            |
| Nb       | 9.25      | 1980           |
| Hg       | 4.15      | 411            |
| V        | 5.38      | 1020           |
| In       | 3.4       | 293            |
| La       | 4.9       | 798            |
| Ta       | 4.48      | 830            |
| Tc       | 7.77      | 1410           |
| Pa       | 1.4       | --             |
| Re       | 1.7       | 198            |
| Tl       | 2.39      | 171            |
:::

An interesting consequence of perfect conductivity is that if a current is introduced into a ring of a superconducting material, then the current will persist indefinitely, without decaying (see {numref}`fig-p4-ch01-2`). On the other hand, the current carrying capacity of a superconductor is finite and cannot exceed a critical current density, $j_c$, above which it reverts back to the normal state.

:::{figure} images/fig-p4-ch01-2.png
:name: fig-p4-ch01-2
:width: 60%
:align: center
Figure 1.2: A superconducting ring showing persistent current threaded by magnetic lines of flux.
:::

## 1.2 Meissner Effect $B = 0$

Besides perfect conductivity, the other main characteristic of superconductivity is **perfect diamagnetism**: this means that $B = 0$ within a superconductor and that magnetic flux is excluded from a superconductor. This fundamental property of superconductors was first identified by Meissner in 1933 and is called the Meissner effect. {numref}`fig-p4-ch01-3` see the magnetic field lines for a perfect conductor (a) and for a perfect diamagnet (b), which is a superconductor. We shall see later that there is, in fact, an exponential decay of the magnetic flux at the surface of a superconductor $e^{-z/\lambda}$, and this decay is characterized by the superconducting penetration depth $\lambda$.

As shown in Fig. 1.3, no flux penetrates a superconductor for $T < T_c$ and $H < H_c$, whether it is cooled in a magnetic field or not. In contrast, a perfect conductor will have no flux inside, only if it is cooled below $T_c$ in zero field. This is evidence that **a superconductor is more than a perfect conductor**.

:::{figure} images/fig-p4-ch01-3.png
:name: fig-p4-ch01-3
:width: 80%
:align: center
Figure 1.3: Schematic diagram of the magnetic field behavior of (a) a "perfect electrical conductor" defined as a normal metal having zero resistance below $T_c$ and (b) a metal that is a superconductor below $T_c$. The lines with arrows indicate the magnetic flux lines. Whereas the normal metal has no flux exclusion, a superconductor exhibits full flux exclusion.
:::

### 1.2.1 Critical Fields

If an external magnetic field is increased above a critical value (see {numref}`tab-p4-ch01-1`), the superconductor will revert to the normal state with finite resistivity. For type I superconductors, $B$ remains zero until the sample exceeds the critical field $H_c$ (see Fig. 1.4a). Most elemental superconductors are Type-I superconductors and exhibit low critical fields (see {numref}`fig-p4-ch01-5`a) and a simple magnetization curve (see Fig. 1.6a). For a Type II superconductor, $B$ remains zero only for relatively small magnetic fields ($H < H_{c1}$) (see Fig. 1.4b). Then above this critical field value ($H_{c2}$), magnetic flux enters the superconductor in the form of vortices (see Figs. 1.4b and 1.6b). These vortices have a core of material in the normal state, around which super-currents circulate. As the magnetic field increases, the density of vortices increases until the upper critical field $H_{c2}$ is reached, where the vortex cores (which are in the normal phase) overlap with one another, and the material becomes a normal metal completely (see Figs. 1.4b and 1.6b). Most materials of practical interest are type II superconductors where typical values of $H_{c2}$ are in Tesla range (see {numref}`fig-p4-ch01-5`b). The critical parameters that characterize a type II superconductor are $T_c$, $H_{c2}$ and $j_c$, where $j_c$ is the critical current density. For current densities above $j_c$, superconductivity is destroyed and the normal resistive state is restored. For practical applications it is desirable for all three critical parameters ($T_c$, $H_{c2}$, $j_c$) to be large.

:::{figure} images/fig-p4-ch01-4.png
:name: fig-p4-ch01-4
:width: 85%
:align: center
Figure 1.4: Schematic magnetic phase diagrams of (a) type I and (b) type II superconductors. Note the formation of a vortex phase above $H_{c1}$ in a type II superconductor, where magnetic flux penetrates into the core of the vortices.
:::

:::{figure} images/fig-p4-ch01-5.png
:name: fig-p4-ch01-5
:width: 90%
:align: center
Figure 1.5: (a) Plot of $H_c$ versus $T$ for several type I superconductors, (b) Plot of $H_{c2}$ versus $T$ for several type II superconductors. Notice the great difference in scale for the critical fields between type I and type II superconductors. Because of their high critical fields, Type II superconductors are of particular interest for superconducting magnet applications.
:::

## 1.3 Flux Quantization

When a persistent (non-decaying) current is induced in a superconducting ring (see Fig. 1.2), the resulting flux within the ring is found to be quantized in units of $\Phi_0 = ch/2e = 2.0678 \times 10^{-7}\,\text{gauss\,cm}^2 = 2.0678 \times 10^{-15}\,\text{tesla\,m}^2$. The experimental confirmation of flux quantization in superconductor rings was first reported by 2 experimental groups in 1961 (B.S. Deaver and W.M. Fairbank, Phys. Rev. Lett. **7**, 43 (1961) and R. Doll and M. Nabauer, Phys. Rev. Lett. **7**, 51 (1961)). This observation strongly suggested that **superconductivity is a quantum mechanical phenomenon**. As a consequence of flux quantization, there are vortices in type II superconductors, and each vortex encloses a single quantized unit of flux $\Phi_0$.

:::{figure} images/fig-p4-ch01-6.png
:name: fig-p4-ch01-6
:width: 90%
:align: center
Figure 1.6: (a) Magnetization versus applied magnetic field for a bulk superconductor exhibiting a complete Meissner effect, i.e., perfect diamagnetism. A superconductor with this behavior is called a type I superconductor. Above the critical field $H_c$ the specimen becomes a normal conductor and the magnetization is too small to be seen on this scale. Note that $-4\pi M$ is plotted on the vertical scale (a negative value for the magnetic susceptibility corresponds to diamagnetism). (b) Magnetization curve for a type II superconductor. The flux starts to penetrate the specimen at a field $H_{c1}$ which is lower than the thermodynamic critical field $H_c$. The specimen is in a vortex state between $H_{c1}$ and $H_{c2}$, but has superconducting electrical properties up to $H_{c2}$. For a given type II superconductor, the area under the dashed magnetization curve in (b) is the same for a type II superconductor as for a type I superconductor.
:::

## 1.4 The Superconducting Energy Gap

Prior to the discovery of flux quantization, experiments on the heat capacity and on the absorption of microwave power were performed, each of which provided evidence for an **energy gap**, characteristic of the superconducting state. These two experiments were critical to the development of the microscopic theory of superconductivity. The existence of an energy gap was soon verified experimentally by the elegant tunneling experiments by Giaever (see {numref}`fig-p4-ch01-8`).

The heat capacity $C$ of a material is the amount of heat $\Delta Q$ needed to raise the temperature by $\Delta T = 1$ K per mole, namely $\Delta Q = C\Delta T$. For normal metals the heat capacity exhibits a temperature dependence $C = \gamma T + \beta T^3$. The first term ($C_e = \gamma T$) arises from the electronic contribution, while the second term ($C_L = \beta T^3$) arises from the lattice. At low temperatures the specific heat is dominated by the electronic part, $C_e = \gamma T$. As a metal is cooled below the transition temperature $T_c$, the electronic part of the heat capacity of a superconductor, increases abruptly and then decays rapidly with decreasing temperature (see {numref}`fig-p4-ch01-7`), falling off to zero exponentially as $T \to 0$. Such an exponential fall-off in $C(T)$ provided early evidence (1954) for an **energy gap**, $\Delta$ (see Fig. 1.7).

The microwave absorption experiment likewise provided direct evidence for an energy gap, including an early determination of the temperature dependence of the energy gap $\Delta(T)$ (see Fig. 1.8). In section 1.8 we present a simple model for the thermodynamics of superconductors, which provides background for the heat capacity studies of Fig. 1.7, while in section 2.5 we present the London equations, describing the electrodynamics of superconductors, which is based on a two-fluid model for superconductivity (see section 2.6). According to this model the electrons in a superconductor consist of superconducting electrons with no resistance and normal electrons which can dissipate energy at ac (microwave) frequencies.

:::{figure} images/fig-p4-ch01-7.png
:name: fig-p4-ch01-7
:width: 80%
:align: center
Figure 1.7: (a) The heat capacity of gallium in the normal and superconducting states. The normal state (which is restored by a 200 G magnetic field) has electronic, lattice and (at low temperatures) nuclear quadrupole contributions to the heat capacity. In (b) the electronic part $C_{el}$ of the heat capacity in the superconducting state is plotted on a log scale versus $T_c/T$: the exponential dependence of $C(T)$ on $1/T$ at low temperature is evident in the figure. (The coefficient $\gamma = 0.60\,\text{mJ mol}^{-1}\,\text{deg}^{-2}$ for Ga).
:::

## 1.5 Thermal Conductivity

In our study of transport properties (see Part I, section 6.2.2) we found that for metals, the electronic contribution $\kappa_e$ dominates the thermal conductivity $\kappa = \kappa_e + \kappa_L$. For normal metals, $\kappa_e$ is proportional to the electron density. However, for a superconductor at $T = 0$, the electrons are all in the superconducting state, bound in Cooper pairs, as we discuss in section 2.1. When the electrons are all bound in pairs, they do not contribute to $\kappa$, because they are in a fully ordered state and have no entropy. Thus at finite temperatures, $\kappa$, for a superconductor is very small (see {numref}`fig-p4-ch01-9`), since only the excited quasiparticles of the two fluid model (as discussed below) can contribute to $\kappa$. The low thermal conductivity of superconductors for $T \ll T_c$, can be utilized in a low temperature heat switch. Application of a magnetic field can be used to cause a superconducting-normal transition, thereby restoring high thermal conductivity and a good thermal conduction path to the metal.

:::{figure} images/fig-p4-ch01-8.png
:name: fig-p4-ch01-8
:width: 55%
:align: center
Figure 1.8: The reduced values of the observed energy gap $E_g(T)/E_g(0)$ as a function of reduced temperature $T/T_c$ for several superconductors. The solid curve is drawn for the BCS theory of superconductivity.
:::

:::{figure} images/fig-p4-ch01-9.png
:name: fig-p4-ch01-9
:width: 60%
:align: center
Figure 1.9: Ratio of the electronic thermal conductivity in the superconducting state to that in the normal state of aluminum (dots) as a function of temperature. The curve is calculated from the BCS theory of superconductivity, and shows the poor thermal conductivity of superconductors at low temperatures.
:::

## 1.6 Quasi-particle Tunneling

Measurements of the properties of the superconducting energy gap were greatly facilitated by the observation of tunneling in a superconductor. In this section, we explain quasiparticle tunneling in a superconductor and show how measurement of the $I-V$ characteristics of the tunnel junction yields information on the superconducting energy gap. The structure of a tunnel junction is shown in Fig. 1.10. Classical physics, of course, would say that no current could pass through the insulating barrier in Fig. 1.10. However, the quantum mechanical nature of the electrons allows them to tunnel through a thin insulating barrier.

Two types of tunneling can, in fact, occur if the counter-electrode is also a superconductor. The first is quasiparticle tunneling which was discovered by Giaever in 1960 and is discussed in this section, and the second type of tunneling is Josephson tunneling discovered by Josephson in 1962, and discussed in section 2.10. Both of these discoveries were made by two very young men, before either had completed their Ph.D. theses.

In the quasiparticle tunneling experiments, "electrons" tunnel through the insulating layers of the S/I/S sandwich of {numref}`fig-p4-ch01-10` until their energy exceeds the gap energy, above which the $I-V$ curve follows Ohm's law (see Fig. 1.11a). In Josephson tunneling (see Fig. 1.11b), a superconducting current can flow at zero voltage until the current reaches a critical current $I_c$ above which the $I-V$ curve switches to the resistive part of the tunnel-junction characteristic and again follows Ohm's law (see section 2.10).

Once quasiparticle tunneling was discovered, it became the standard method for measuring the superconducting energy gap and the dependence of the gap on temperature and magnetic field. The insulator in Fig. 1.10 normally acts as a barrier to the flow of conduction electrons from one metal to the other. If the barrier is sufficiently thin (less than 10 or 20 Angstroms), there is a significant probability that if a voltage is applied across the S/I/S device, an electron which impinges on the insulating barrier will tunnel from one metal electrode to the other.

When both metals are normal conductors (M), the current-voltage relation of the M/I/M sandwich or tunneling junction is ohmic at low voltages, with the current directly proportional to the applied voltage. Giaever (1960) discovered that if one of the metals becomes superconducting (S), the current-voltage characteristic of the M/I/S sandwich changes from the linear Ohmic behavior of Fig. 1.12(a) to the curve shown in Fig. 1.12(b). Giaever explained his observation in terms of the model of the density of states shown in Fig. 1.12(b) for the superconductor.

{numref}`fig-p4-ch01-12`(b) contrasts the electron density of states in the superconductor with that in the normal metal, shown in Fig. 1.12(a). In the superconductor there is an **energy gap** centered at the Fermi level. The electron states that had been in the energy gap range in the normal state, now pile up on either side of the energy gap, giving a very high density of states in the regions adjacent to the energy gap, and shown in Fig. 1.12(b). From the microscopic theory of superconductivity it is known that quasiparticle tunneling involves a pair of electrons (see section 2.1) rather than a single electron, as in the case of tunneling in a normal metal.

:::{figure} images/fig-p4-ch01-10.png
:name: fig-p4-ch01-10
:width: 65%
:align: center
Figure 1.10: Superconducting tunnel junction which consists of a superconductor-insulator-superconductor (S/I/S) sandwich, where tunneling occurs between the two superconducting layers (S) which are in black and an oxide layer is used as an insulator (I) between them.
:::

When the electron pair is involved, the current in the M/I/S sandwich starts to flow at $T = 0$K when $eV = \Delta$ where $\Delta$ is half the energy gap (see Fig. 1.12b). At finite temperatures there is a small current flow even at lower voltages, because of electrons in the superconductor that are thermally excited across the energy gap. Clearly Fig. 1.12b shows that quasiparticle tunneling provides a direct method for measuring the superconducting energy bandgap.

Of interest is case (c) of Fig. 1.12 for tunneling in a S/I/S junction, where the metals on either side of the tunnel barrier are superconducting. Near $T = 0$ all the electrons in the small gap superconductor [Fig. 1.12(c)] are paired and there are few excited electrons. Thus, it is only when the bias voltage exceeds $(\Delta_1 + \Delta_2)/e$ that there is a significant density of electrons to tunnel across the barrier. For bias voltages less than $(\Delta_1 - \Delta_2)/e$, only the low density of thermally excited electrons from the small gap superconductor can tunnel into the wide gap superconductor, so that only a small amount of tunneling occurs. In this case, $I$ increases until $V = (\Delta_1 - \Delta_2)/e$ is reached where the joint density of states is maximized. As the voltage is increased from $(\Delta_1 - \Delta_2)/e$ to $(\Delta_1 + \Delta_2)/2$, the joint density of states available for tunneling decreases and the tunneling current consequently also decreases. By increasing the temperature above $T_c$, or increasing the magnetic field above $H_{c2}$, the small bandgap material will go normal, and case (b) is reached. Thus when two superconductors are used, it is possible to get information on the bandgaps of both superconductors.

:::{figure} images/fig-p4-ch01-11.png
:name: fig-p4-ch01-11
:width: 95%
:align: center
Figure 1.11: $I-V$ characteristics for (a) quasiparticle tunneling in a tunnel junction for a S/I/S device (see Fig. 1.10), and (b) Josephson tunneling through a weak link Josephson tunnel junction.
:::

:::{figure} images/fig-p4-ch01-12.png
:name: fig-p4-ch01-12
:width: 100%
:align: center
Figure 1.12: The six density of states versus energy diagrams on the left are for $T = 0$K and the three diagrams on the right are all plots of the current versus voltage for the various types of metals on the left. (a) This shows two normal metals separated by a thin insulating film with zero applied voltage and then for $V > 0$. (b) The same situation as (a) but now one of the metals is a superconductor. (c) Now both of the metals are superconductors with different gaps. ($E_F$ is the Fermi energy).
:::

## 1.7 Isotope Effect

The first clue to the microscopic origin of superconductivity came from studying metals containing different isotopes of a particular elemental superconductor. In these experiments, the superconducting transition temperature $T_c$ was found to decrease with increasing isotopic mass according to the relation

```{math}
:label: eq-p4-ch01-1
M^\alpha T_c = \text{constant},
```

where $\alpha \simeq 1/2$. The discovery of the isotope effect was totally unexpected and indicated that superconductivity involved a strong interaction (electron-phonon coupling) between the electrons and the lattice.

## 1.8 Thermodynamics of Superconductors

In order to increase our understanding of the temperature dependence of the specific heat of superconductors and the nature of the normal-superconducting phase transition, we consider in this section a simple model for the thermodynamics of a metal in the normal state and in the superconducting state.

The Gibbs free energy per unit volume of a superconductor in a magnetic field can be written as

```{math}
:label: eq-p4-ch01-2
G = U - TS - HM
```

where $M$ is the magnetization, $S$ is the entropy and the usual $pV$ term is neglected. We may verify Eq. 1.2 by observing that the changes in internal energy density in the presence of a magnetic field is given by

```{math}
:label: eq-p4-ch01-3
dU = TdS + HdM.
```

Then, from Eqs. 1.2 and 1.3, we obtain

```{math}
:label: eq-p4-ch01-4
dG = -SdT - MdH.
```

Substituting $M = -H/4\pi$ for a perfect diamagnet ($B = 0$) and integrating Eq. 1.4, we obtain the following important relation for the superconducting state at a given temperature

```{math}
:label: eq-p4-ch01-5
G_s(H) = G_s(0) + \frac{1}{8\pi} H^2.
```

From thermodynamic theory we know that for two phases to be in equilibrium (at constant $T, P, H$), it is necessary that the Gibbs free energies be equal. Thus, along the critical field curve where the superconducting and normal states are in equilibrium,

```{math}
:label: eq-p4-ch01-6
G_n = G_s(0) + \frac{1}{8\pi} H_c^2,
```

where $G_n$ is the Gibbs free energy density of the normal state and is essentially independent of the magnetic field. From Eq. 1.4, we obtain

```{math}
:label: eq-p4-ch01-7
\left(\frac{\partial G}{\partial T}\right)_H = -S
```

so that Eqs. 1.5 and 1.6 give the important result that in equilibrium

```{math}
:label: eq-p4-ch01-8
S_n - S_s = -\frac{H_c}{4\pi} \frac{dH_c}{dT}
```

where $S_s$ denotes the entropy in the superconducting phase in zero field. Since $dH_c/dT$ is always found to be negative, the entropy of the normal state is always greater than that of the superconducting state.

Finally, the difference in heat capacity per unit volume in the superconducting and normal states is given by

```{math}
:label: eq-p4-ch01-9
\Delta C = C_s - C_n = T\frac{d}{dT}(S_s - S_n) = \frac{TH_c}{4\pi} \frac{d^2H_c}{dT^2} + \frac{T}{4\pi} \left[\frac{dH_c}{dT}\right]^2,
```

which is shown in Fig. 1.7. At $T = T_c$, where $H_c = 0$, we thus have

```{math}
:label: eq-p4-ch01-10
\Delta C = \frac{T_c}{4\pi} \left(\frac{dH_c}{dT}\right)^2.
```

```{math}
:label: eq-p4-ch01-11
E_g=2\hbar\omega_D\exp\left(-\frac{\lambda_{ep}}{NV}\right)\simeq3.5k_BT_c
```

We note from Eq. 1.8 that at the critical temperature $H_c = 0$ so that there is no latent heat of transition ($\Delta S = 0$), but there is, according to Eq. 1.10, a discontinuity in the heat capacity. For this reason the phase transition at $T = T_c$ (where $H_c = 0$) is of second order, but away from $T_c$, the phase transition has a latent heat and is a first order phase transition.
