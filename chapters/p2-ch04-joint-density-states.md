---
title: "4 The Joint Density of States and Critical Points"
abstract: "The joint density of states is introduced using the Fermi Golden Rule and is evaluated near critical points (Van Hove singularities) in 3D, 2D, and 1D systems, emphasizing the connection between optical structure and energy band extrema."
---

# 4 The Joint Density of States and Critical Points

## 4.0 References

- Jones and March, *Theoretical Solid State Physics*: pp. 806-814
- Bassani and Pastori–Parravicini, *Electronic States and Optical Transitions in Solids*: chapter 5
- Yu and Cardona, *Fundamentals of Semiconductors*, pp. 251-258
- Madelung, *Introduction to Solid State Theory*: pp. 262-271

## 4.1 The Joint Density of States

The detailed calculation of the contribution to the frequency dependent dielectric function $\varepsilon(\omega)$ due to interband transitions is rather difficult. It is therefore instructive to obtain an approximate answer by use of the Fermi Golden Rule (Eq. A.32). The Golden Rule gives us the probability per unit time $W_{\mathbf{k}}$ that a photon of energy $\hbar\omega$ makes a transition at a given $\mathbf{k}$ point in the Brillouin zone:

```{math}
:label: eq-p2-ch04-1
W_{\mathbf{k}} \cong \frac{2\pi}{\hbar} |\langle v|\mathcal{H}'|c\rangle|^2 \delta[E_c(\mathbf{k}) - E_v(\mathbf{k}) - \hbar\omega]
```

where the matrix element for the electromagnetic perturbation $\mathcal{H}'$ is taken between the valence and conduction band Bloch states at wave vector $\mathbf{k}$, and the $\delta$-function $\delta[E_c - E_v - \hbar\omega]$ which expresses energy conservation is also evaluated at $\mathbf{k}$. In writing Eq. {eq}`eq-p2-ch04-1`, we exploit the fact that the wave vector for the light is small compared to the Brillouin zone dimensions. Because the electronic states in the Brillouin zone are quasi-continuous functions of $\mathbf{k}$, to obtain the lineshape for an interband transition, we must integrate over $\mathbf{k}$. Recognizing that both the perturbation matrix elements and the joint density of states are $\mathbf{k}$-dependent, we obtain upon integration of Eq. {eq}`eq-p2-ch04-1` over $\mathbf{k}$ space

```{math}
:label: eq-p2-ch04-2
W = \frac{2\pi}{\hbar} \int |\langle v|\mathcal{H}'|c\rangle|^2 \frac{2}{8\pi^3} \delta(E_c(\mathbf{k}) - E_v(\mathbf{k}) - \hbar\omega)\,d^3k
```

for a 3D system. For 2D and 1D systems, we replace $[d^3k/(2\pi)^3]$ by $[d^2k/(2\pi)^2]$ and $[dk/(2\pi)]$, respectively. The perturbation Hamiltonian for the electromagnetic interaction is simply

```{math}
:label: eq-p2-ch04-3
\mathcal{H}' = -\frac{e\mathbf{A}\cdot\mathbf{p}}{mc}
```

where the time dependence of the vector potential $\mathbf{A}$ has already been taken into account in formulating time dependent perturbation theory and the golden rule (see Appendix A), so that $\mathbf{A}$ in Eq. {eq}`eq-p2-ch04-3` is a vector with only spatial dependence. In taking matrix elements of the perturbation Hamiltonian, we need then only consider matrix elements of the momentum operator connecting the valence and conduction bands. In practical cases it is often not necessary to evaluate these matrix elements explicitly because it is precisely these momentum matrix elements that determine the experimentally measured effective masses (see §3.3). If we assume for simplicity that $|\langle v|\mathcal{H}'|c\rangle|^2$ is independent of $\mathbf{k}$, then the remaining integral in Eq. {eq}`eq-p2-ch04-2` is the joint density of states between the valence and conduction bands $\rho_{cv}(\hbar\omega)$. For a 3D system, we thus define $\rho_{cv}(\hbar\omega)$ as

```{math}
:label: eq-p2-ch04-4
\rho_{cv}(\hbar\omega) \equiv \frac{2}{8\pi^3} \int \delta[E_c(\mathbf{k}) - E_v(\mathbf{k}) - \hbar\omega]\,d^3k
```

and $\rho_{cv}(\hbar\omega)$ is the number of states per unit volume per unit energy range which occur with an energy difference between the conduction and valence bands equal to the photon energy. As explained above, $\rho_{cv}(\hbar\omega)$ can be evaluated in a corresponding manner for 2D and 1D systems.

We would now like to look at this joint density of states (Eq. {eq}`eq-p2-ch04-4`) in more detail to see why the optical properties of solids give unique information about the energy band structure. The main point is that optical measurements preferentially provide information about the bands at particular $\mathbf{k}$ points in the Brillouin zone, usually points of high symmetry and near energy band extrema. This can be understood by casting $\rho_{cv}(\hbar\omega)$ in a more transparent form. We start with the definition of the joint density of states given in Eq. {eq}`eq-p2-ch04-4`. It is convenient to convert this integral over $\mathbf{k}$-space to an integral over energy. This is done by introducing a constant energy surface $S$ in $k$-space such that the energy difference $E_c - E_v = \hbar\omega$ is the photon energy. Then we can introduce the constant energy surfaces $S$ and $S+dS$ in reciprocal space (see Fig. {numref}`fig-p2-ch04-1`) as corresponding to a constant energy difference between the conduction and valence bands at each $\mathbf{k}$ point and:

```{math}
:label: eq-p2-ch04-5
d^3k = dS\,dk_n
```

where $dk_n$ is an element of a wave vector normal to $S$, as shown in Fig. {numref}`fig-p2-ch04-1`.

:::{figure} images/fig-p2-ch04-1.png
:name: fig-p2-ch04-1
:width: 40%
:align: center
Fig. 4.1: Adjacent constant energy difference surfaces in reciprocal space, $S$ and $S+dS$, where the energy difference is between valence and conduction bands, and $dk_n$ is the normal to these constant energy difference surfaces.
:::

By definition of the gradient, we have $|\nabla_k E|\,dk_n = dE$ so that for constant energy surfaces with energy difference $E_c - E_v$ we write:

```{math}
:label: eq-p2-ch04-6
|\nabla_k(E_c - E_v)|\,dk_n = d(E_c - E_v).
```

Therefore

```{math}
:label: eq-p2-ch04-7
d^3k = dk_n\,dS = dS\left[\frac{d(E_c - E_v)}{|\nabla_k(E_c - E_v)|}\right]
```

so that

```{math}
:label: eq-p2-ch04-8
\rho_{cv}(\hbar\omega) = \frac{2}{8\pi^3} \int\!\int\!\int \frac{dS\,d(E_c - E_v)\,\delta(E_c - E_v - \hbar\omega)}{|\nabla_k(E_c - E_v)|}.
```

We now carry out the integral over $d(E_c - E_v)$ to obtain

```{math}
:label: eq-p2-ch04-9
\rho_{cv}(\hbar\omega) = \frac{2}{8\pi^3} \int\!\int \frac{dS}{|\nabla_k(E_c - E_v)|_{E_c-E_v=\hbar\omega}}.
```

Of special interest are those points in the Brillouin zone where $(E_c - E_v)$ is stationary and $\nabla_k(E_c - E_v)$ vanishes. At such points, called joint critical points, the denominator of the integrand in Eq. {eq}`eq-p2-ch04-9` vanishes and especially large contributions can be made to $\rho_{cv}(\hbar\omega)$. This can be understood on the basis of physical considerations. Around critical points, the photon energy $\hbar\omega = (E_c - E_v)$ is effective in inducing electronic transitions over a relatively larger region of the Brillouin zone than would be the case for transitions about non-critical points. The relatively large contributions to the transition probability for critical points gives rise to "structure" observed in the frequency dependence of the optical properties of solids. Critical points generally occur at high symmetry points in the Brillouin zone, though this is not necessarily the case.

As an illustration, let us consider the energy bands of the semiconductor germanium (see Fig. {numref}`fig-p2-ch04-2`). Here we see that both the valence and conduction bands have extrema at the $\Gamma$ point, $\mathbf{k}=0$, although the lowest conduction band minimum is located at the $L$ point. For the band extrema at $\mathbf{k}=0$, the condition $[E_c(k=0) - E_v(k=0)] = \hbar\omega$ gives rise to critical points in the joint density of states. Notice also that around the $L$ points, extrema occur in both the valence and conduction bands, and a critical point therefore results. Since the energy difference $[E_c - E_v]$ has a relatively small gradient as we move away from the $L$ point, this critical point participates more fully in the interband transitions. In fact, for germanium, Fig. {numref}`fig-p2-ch04-2` shows that there are large regions along the $(100)$ and $(111)$ axes where the energy separation between valence and conduction bands $(E_c - E_v)$ is roughly constant. These large regions in $k$-space make very large contributions to the dielectric function. We can see these features directly by looking at the frequency dependence of the real and imaginary parts of the dielectric function for germanium (see Fig. {numref}`fig-p2-ch04-3`). Here we see that at low photon energies (below $\sim 2\,\text{eV}$), where the interband transitions from the $\Gamma_{25'}$ valence band to the $\Gamma_{2'}$ conduction band dominate, the contributions to the real and imaginary parts of the dielectric function are small. On the other hand, the contributions from the large regions of the Brillouin zone along the $(100)$ and $(111)$ axes between 2 and 5 eV are very much more important, as is seen in Fig. {numref}`fig-p2-ch04-3` for both $\varepsilon_1(\omega)$ and $\varepsilon_2(\omega)$.

:::{figure} images/fig-p2-ch04-2.png
:name: fig-p2-ch04-2
:width: 55%
:align: center
Fig. 4.2: $E(\mathbf{k})$ for a few high symmetry directions in germanium, neglecting the spin-orbit interaction.
:::

:::{figure} images/fig-p2-ch04-3.png
:name: fig-p2-ch04-3
:width: 80%
:align: center
Fig. 4.3: Frequency dependence of the real ($\varepsilon_1$) and imaginary ($\varepsilon_2$) parts of the dielectric function for germanium. The solid curves are obtained from an analysis of experimental normal-incidence reflectivity data while the dots are calculated from an energy band model. In particular $\varepsilon_2(\omega)$ provides an excellent example for illustrating the 4 kinds of critical points: $M_0$, $M_1$, $M_2$ and $M_3$.
:::

In describing this contribution to the dielectric function of germanium we say that the valence and conduction bands track each other, and in this way they produce a large contribution to the joint density of states over large regions of the Brillouin zone. A similar situation occurs in silicon and in common III-V semiconductors. The diagram in Fig. {numref}`fig-p2-ch04-2` shows that beyond $\sim 5\,\text{eV}$ there is no longer any significant tracking of the valence and conduction bands. Consequently, the magnitudes of $\varepsilon_1(\omega)$ and $\varepsilon_2(\omega)$ fall sharply beyond $\sim 5\,\text{eV}$. The absolute magnitudes of $\varepsilon_1$ and $\varepsilon_2$ for germanium and other semiconductors crystallizing in the diamond or zincblende structure are relatively large. We will see shortly, when we discuss the Kramers–Kronig relations in §6.1, that these large magnitudes of $\varepsilon_1$ and $\varepsilon_2$ are responsible for the large value of $\varepsilon_1(\omega \to 0)$ in these materials. For germanium $\varepsilon_1(0)$ is 16 from Fig. {numref}`fig-p2-ch04-3`.

## 4.2 Critical Points

For a 3D system, critical points (often called Van Hove singularities) are classified into four categories depending on whether the band separations are increasing or decreasing as we move away from the critical point. This information is found by expanding $[E_c(\mathbf{k}) - E_v(\mathbf{k})]$ in a Taylor series around the critical point $\mathbf{k}_0$ which is at an energy difference extremum, where we can write

```{math}
:label: eq-p2-ch04-10
E_c(\mathbf{k}) - E_v(\mathbf{k}) = E_g(\mathbf{k}_0) + \sum_{i=1}^{3} a_i (k_i - k_{0i})^2
```

where the energy gap at the expansion point is written as $E_g(\mathbf{k}_0)$ and the sum is over the three directions $x$, $y$, and $z$. The coefficients $a_i$ are related to the second derivative of the energy difference by $2a_i = \frac{\partial^2}{\partial k_i^2}[E_c(\mathbf{k}) - E_v(\mathbf{k})]$. The classification of the critical points in a 3D system shown in Fig. {numref}`fig-p2-ch04-4` is made according to how many $a_i$ coefficients in Eq. {eq}`eq-p2-ch04-10` are negative. The shapes given for the joint density of states curves of Fig. {numref}`fig-p2-ch04-4` are obtained, as is here illustrated, for the case of an $M_0$ singularity for a 3D system. In the case of 2D and 1D systems, there are 3 and 2 types of critical points, respectively, using the same definition of the coefficients $a_i$ to define the type of critical point.

:::{figure} images/fig-p2-ch04-4.png
:name: fig-p2-ch04-4
:width: 70%
:align: center
Fig. 4.4: Summary of the joint density of states for a 3D system near each of the distinct types of critical points.
:::

As an example, we will calculate $\rho_{cv}(\hbar\omega)$ for an $M_0$ singularity in a 3D system, assuming simple parabolic bands (see Fig. {numref}`fig-p2-ch04-5`). Here,

```{math}
:label: eq-p2-ch04-11
E_c(\mathbf{k}) = \frac{E_g}{2} + \frac{\hbar^2 k^2}{2m_c}
```

and

```{math}
:label: eq-p2-ch04-12
E_v(\mathbf{k}) = -\frac{E_g}{2} - \frac{\hbar^2 k^2}{2m_v}
```

where $E_g$ is the energy gap, and $m_c$ and $m_v$ are effective masses for the conduction and valence bands, respectively, and $m_v$ is taken as a positive number. We thus obtain

```{math}
:label: eq-p2-ch04-13
E_c(\mathbf{k}) - E_v(\mathbf{k}) = E_g + \frac{\hbar^2 k^2}{2}\left(\frac{1}{m_c} + \frac{1}{m_v}\right) = E_g + \frac{\hbar^2 k^2}{2m_r}
```

where we define the reduced mass $m_r$ through the relation

```{math}
:label: eq-p2-ch04-14
\frac{1}{m_r} = \frac{1}{m_c} + \frac{1}{m_v}.
```

Taking the gradient of $E_c - E_v$ yields

```{math}
:label: eq-p2-ch04-15
\nabla_k(E_c - E_v) = \frac{\hbar^2 \mathbf{k}}{m_r}
```

so that the joint density of states becomes

```{math}
:label: eq-p2-ch04-16
\rho_{cv}(\hbar\omega) = \frac{2}{8\pi^3} \int \frac{dS}{|\nabla_k(E_c - E_v)|_{E_c-E_v=\hbar\omega}}
```

or

```{math}
:label: eq-p2-ch04-17
\rho_{cv}(\hbar\omega) = \frac{2}{8\pi^3} \left[\frac{4\pi}{\hbar^2}\left(\frac{k^2 m_r}{k}\right)\right]_{E_c-E_v=\hbar\omega} = \left[\frac{m_r}{\pi^2 \hbar^2} k\right]_{E_c-E_v=\hbar\omega}.
```

We evaluate $k$ in Eq. {eq}`eq-p2-ch04-17` from the condition

```{math}
:label: eq-p2-ch04-18
E_c - E_v = \hbar\omega = E_g + \frac{\hbar^2 k^2}{2m_r}
```

or

```{math}
:label: eq-p2-ch04-19
k = \left[\frac{2m_r}{\hbar^2}(\hbar\omega - E_g)\right]^{1/2}
```

so that

```{math}
:label: eq-p2-ch04-20
\rho_{cv}(\hbar\omega) = \frac{1}{2\pi^2}\left[\frac{2m_r}{\hbar^2}\right]^{3/2}\sqrt{\hbar\omega - E_g} \qquad \hbar\omega > E_g \\
= 0 \qquad \hbar\omega < E_g
```

as shown in Fig. {numref}`fig-p2-ch04-4` for an $M_0$ critical point. The expression for $\rho_{cv}(\hbar\omega)$ in Eq. {eq}`eq-p2-ch04-20` is not singular for a 3D system but represents a discontinuity in slope at $\hbar\omega = E_g$. This discontinuity in slope corresponds to a *threshold* for the absorption process, as discussed in Chapter 5.

On the other hand, the situation is quite different for the joint density of states corresponding to an $M_0$ critical point for a 3D system in a magnetic field, as we will see in Part III of the class notes. At a critical point, the joint density of states in a magnetic field *does* show singularities where the density of states in a magnetic field becomes infinite. These singularities in a magnetic field make it possible to carry out resonance experiments in solids, despite the quasi-continuum of the energy levels in the electronic dispersion relations $E(\mathbf{k})$.

:::{figure} images/fig-p2-ch04-5.png
:name: fig-p2-ch04-5
:width: 40%
:align: center
Fig. 4.5: Bands associated with a $M_0$ critical point for a 3D system.
:::

We note that we can have $M_0$-type critical points for bands that look like Fig. {numref}`fig-p2-ch04-6`a or like Fig. {numref}`fig-p2-ch04-6`b. It is clear that the energy difference $E_c - E_v$ in Fig. {numref}`fig-p2-ch04-6`b varies more slowly around the critical point than it does in Fig. {numref}`fig-p2-ch04-6`a. Thus, bands that tend to "track" each other have an exceptionally high joint density of states and contribute strongly to the optical properties. Above we gave examples of electronic energy bands with very high values for $\varepsilon_1$ and $\varepsilon_2$ due to bands that track each other as are found in common semiconductors like germanium along the $\Lambda$ (111) direction (see Figs. {numref}`fig-p2-ch04-2` and {numref}`fig-p2-ch04-3`).

:::{figure} images/fig-p2-ch04-6.png
:name: fig-p2-ch04-6
:width: 80%
:align: center
Fig. 4.6: Two cases of band extrema which are associated with $M_0$ critical points. (a) Conduction band minimum and a valence band maximum and (b) Both bands showing minima.
:::

In addition to the $M_0$ critical points, we have $M_1$, $M_2$, and $M_3$ critical points in 3D systems. The functional forms for the joint density of states for $\hbar\omega < E_g$ and $\hbar\omega > E_g$ are given in Table {numref}`tab-p2-ch04-1`. The table also gives the corresponding expressions for 2D and 1D systems. From the table we see that in 2D, the $M_0$ and $M_2$ critical points correspond to discontinuities in the joint density of states at $E_g$, while the $M_1$ singularity corresponds to a saddle point logarithmic divergence. In the case of the 1D system, both the $M_0$ and $M_1$ critical points are singular. For example, we make use of these critical points in 1D systems such as carbon nanotubes to measure the Raman spectrum of just one isolated carbon nanotube.

:::{table} Functional form for the joint density of states $\rho_{vc}(\hbar\omega)$ for various types of critical points $M_0$, $M_1$, $M_2$ and $M_3$ below and above the energy gap $E_g$ for 3D, 2D, and 1D systems.
:name: tab-p2-ch04-1
| Dimension | Type | $\hbar\omega < E_g$ | $\hbar\omega > E_g$ |
|:----------|:-----|:---------------------|:---------------------|
| 3D | $M_0$ | $0$ | $(\hbar\omega - E_g)^{1/2}$ |
| 3D | $M_1$ | $C - (E_g - \hbar\omega)^{1/2}$ | $C$ |
| 3D | $M_2$ | $C$ | $C - (\hbar\omega - E_g)^{1/2}$ |
| 3D | $M_3$ | $(E_g - \hbar\omega)^{1/2}$ | $0$ |
| 2D | $M_0$ | $0$ | $C$ |
| 2D | $M_1$ | $-\ln(E_g - \hbar\omega)$ | $-\ln(\hbar\omega - E_g)$ |
| 2D | $M_2$ | $C$ | $0$ |
| 1D | $M_0$ | $0$ | $(\hbar\omega - E_g)^{-1/2}$ |
| 1D | $M_1$ | $(E_g - \hbar\omega)^{-1/2}$ | $0$ |
:::
