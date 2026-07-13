---
title: "2 Drude Theory—Free Carrier Contribution to the Optical Properties"
abstract: "This chapter treats the free-carrier (intraband) contribution to the optical properties of solids through the classical Drude model. It derives the complex conductivity and dielectric function, discusses the low- and high-frequency limits, introduces the plasma frequency, and explains the connection between optical and electrical properties in metals and semiconductors."
---

# 2 Drude Theory—Free Carrier Contribution to the Optical Properties

## 2.0 Overview

This chapter relates the optical constants to the electronic properties of the solid. The major contribution discussed here is through the free carriers, which is very important in semiconductors and metals. The Drude model gives the simplest theory of the optical constants and is based on the classical equations of motion of an electron in an optical electric field. The chapter also introduces the conductivity tensor, the core dielectric constant, and the plasma frequency.

## 2.1 The Free Carrier Contribution

In this chapter we relate the optical constants to the electronic properties of the solid. One major contribution to the dielectric function is through the "free carriers". Such free carrier contributions are very important in semiconductors and metals, and can be understood in terms of a simple classical conductivity model, called the Drude model. This model is based on the classical equations of motion of an electron in an optical electric field, and gives the simplest theory of the optical constants. The classical equation for the drift velocity of the carrier $\vec{v}$ is given by

:::{math}
:label: eq-p2-ch02-1
m\frac{d\vec{v}}{dt} + \frac{m\vec{v}}{\tau} = e\vec{E}_0 e^{-i\omega t}
:::

where the relaxation time $\tau$ is introduced to provide a damping term, $(m\vec{v}/\tau)$, and a sinusoidally time-dependent electric field provides the driving force. To respond to a sinusoidal applied field, the electrons undergo a sinusoidal motion which can be described as

:::{math}
:label: eq-p2-ch02-2
\vec{v} = \vec{v}_0 e^{-i\omega t}
:::

so that Eq. {eq}`eq-p2-ch02-1` becomes

:::{math}
:label: eq-p2-ch02-3
\left(-mi\omega + \frac{m}{\tau}\right)\vec{v}_0 = e\vec{E}_0
:::

and the amplitudes $\vec{v_0}$ and $\vec{E_0}$ are thereby related. The current density $\vec{j}$ is related to the drift velocity $\vec{v}_0$ and to the carrier density $n$ by

:::{math}
:label: eq-p2-ch02-4
\vec{j} = ne\vec{v}_0 = \sigma\vec{E}_0
:::

thereby introducing the electrical conductivity $\sigma$. Substitution for the drift velocity $v_0$ yields

:::{math}
:label: eq-p2-ch02-5
\vec{v}_0 = \frac{e\vec{E}_0}{(m/\tau) - im\omega}
:::

into Eq. {eq}`eq-p2-ch02-4` yields the complex conductivity

:::{math}
:label: eq-p2-ch02-6
\sigma = \frac{ne^2\tau}{m(1 - i\omega\tau)}
:::

In writing $\sigma$ in the Drude expression (Eq. {eq}`eq-p2-ch02-6`) for the free carrier conduction, we have suppressed the subscript in $\sigma_{\text{complex}}$, as is conventionally done in the literature. In what follows we will always write $\sigma$ and $\varepsilon$ to denote the complex conductivity and complex dielectric constant and suppress subscripts "complex" in order to simplify the notation. A more elegant derivation of the Drude expression can be made from the Boltzmann formulation, as is done in Part I of the notes. In a real solid, the same result as given above follows when the effective mass approximation can be used. Following the results for the dc conductivity obtained in Part I, an electric field applied in one direction can produce a force in another direction because of the anisotropy of the constant energy surfaces in solids. Because of the anisotropy of the effective mass in solids, $\vec{j}$ and $\vec{E}$ are related by the tensorial relation,

:::{math}
:label: eq-p2-ch02-7
j_\alpha = \sigma_{\alpha\beta}E_\beta
:::

thereby defining the conductivity tensor $\sigma_{\alpha\beta}$ as a second rank tensor. For perfectly free electrons in an isotropic (or cubic) medium, the conductivity tensor is written as:

:::{math}
:label: eq-p2-ch02-8
\overleftrightarrow{\sigma} = \begin{pmatrix} \sigma & 0 & 0 \\ 0 & \sigma & 0 \\ 0 & 0 & \sigma \end{pmatrix}
:::

and we have our usual scalar expression $\vec{j} = \sigma\vec{E}$. However, in a solid, $\sigma_{\alpha\beta}$ can have off-diagonal terms, because the effective mass tensors are related to the curvature of the energy bands $E(\vec{k})$ by

:::{math}
:label: eq-p2-ch02-9
\left(\frac{1}{m}\right)_{\alpha\beta} = \frac{1}{\hbar^2}\frac{\partial^2 E(\vec{k})}{\partial k_\alpha \partial k_\beta}
:::

The tensorial properties of the conductivity follow directly from the dependence of the conductivity on the reciprocal effective mass tensor.

As an example, semiconductors such as CdS and ZnO exhibit the wurtzite structure, which is a non-cubic structure. These semiconductors are *uniaxial* and contain an *optic axis* (which for the wurtzite structure is along the $c$-axis), along which the velocity of propagation of light is independent of the polarization direction. Along other directions, the velocity of light is different for the two polarization directions, giving rise to a phenomenon called *birefringence*. Crystals with tetragonal or hexagonal symmetry are uniaxial. Crystals with lower symmetry can have two axes along which light propagates at the same velocity for the two polarizations of light (but the actual velocities will be different from each other), and these crystals are therefore called *biaxial*.

Even though the constant energy surfaces for a large number of the common semiconductors are described by ellipsoids and the effective masses of the carriers are given by an effective mass tensor, it is a general result that for cubic materials (in the absence of externally applied stresses and magnetic fields), the conductivity for all electrons and all the holes is described by a single scalar quantity $\sigma$. To describe conduction processes in hexagonal materials we need to introduce two constants: $\sigma_\parallel$ for conduction along the high symmetry axis and $\sigma_\perp$ for conduction in the basal plane. These results can be directly demonstrated by summing the contributions to the conductivity from all carrier pockets.

In narrow gap semiconductors, $m_{\alpha\beta}$ is itself a function of energy. If this is the case, the Drude formula is valid when $m_{\alpha\beta}$ is evaluated at the Fermi level and $n$ is the total carrier density. Suppose now that the only conduction mechanism that we are treating in detail is the free carrier mechanism. Then we would consider all other contributions in terms of the core dielectric constant $\varepsilon_{\text{core}}$ to obtain for the total complex dielectric function

:::{math}
:label: eq-p2-ch02-10
\varepsilon(\omega) = \varepsilon_{\text{core}}(\omega) + 4\pi i\sigma/\omega
:::

so that

:::{math}
:label: eq-p2-ch02-11
\sigma(\omega) = \left(ne^2\tau/m^*\right)(1 - i\omega\tau)^{-1}
:::

in which $4\pi\sigma/\omega$ denotes the imaginary part of the free carrier contribution. If there were no free carrier absorption, $\sigma=0$ and $\varepsilon=\varepsilon_{\text{core}}$, and in empty space $\varepsilon=\varepsilon_{\text{core}}=1$. From the Drude theory,

:::{math}
:label: eq-p2-ch02-12
\varepsilon = \varepsilon_{\text{core}} + \frac{4\pi i}{\omega}\frac{ne^2\tau}{m(1-i\omega\tau)} = (\varepsilon_1 + i\varepsilon_2) = (n_1 + ik_2)^2
:::

It is of interest to consider the expression in Eq. {eq}`eq-p2-ch02-12` in two limiting cases: low and high frequencies.

## 2.2 Low Frequency Response: $\omega\tau \ll 1$

In the low frequency regime ($\omega\tau \ll 1$) we obtain from Eq. {eq}`eq-p2-ch02-12`

:::{math}
:label: eq-p2-ch02-13
\varepsilon \simeq \varepsilon_{\text{core}} + \frac{4\pi i ne^2\tau}{m\omega}
:::

Since the free carrier term in Eq. {eq}`eq-p2-ch02-13` shows a $1/\omega$ dependence as $\omega \to 0$, this term dominates in the low frequency limit. The core dielectric constant is typically 16 for germanium, 12 for silicon and perhaps 100 or more, for narrow gap semiconductors like PbTe. It is also of interest to note that the core contribution and free carrier contribution are out of phase.

To find the optical constants $\tilde{n}$ and $\tilde{k}$ we need to take the square root of $\varepsilon$. Since we will see below that $\tilde{n}$ and $\tilde{k}$ are large, we can for the moment ignore the core contribution to obtain:

:::{math}
:label: eq-p2-ch02-14
\sqrt{\varepsilon} \simeq \sqrt{\frac{4\pi ne^2\tau}{m\omega}}\sqrt{i} = \tilde{n} + i\tilde{k}
:::

and using the identity

:::{math}
:label: eq-p2-ch02-15
\sqrt{i} = e^{\frac{\pi i}{4}} = \frac{1+i}{\sqrt{2}}
:::

we see that in the low frequency limit $\tilde{n} \approx \tilde{k}$, and that $\tilde{n}$ and $\tilde{k}$ are both large. Therefore the normal incidence reflectivity can be written as

:::{math}
:label: eq-p2-ch02-16
\mathcal{R} = \frac{(\tilde{n}-1)^2 + \tilde{k}^2}{(\tilde{n}+1)^2 + \tilde{k}^2} \simeq \frac{\tilde{n}^2 + \tilde{k}^2 - 2\tilde{n}}{\tilde{n}^2 + \tilde{k}^2 + 2\tilde{n}} = 1 - \frac{4\tilde{n}}{\tilde{n}^2 + \tilde{k}^2} \simeq 1 - \frac{2}{\tilde{n}}
:::

Thus, the Drude theory shows that at low frequencies a material with a large concentration of free carriers (e.g., a metal) is a perfect reflector.

## 2.3 High Frequency Response; $\omega\tau \gg 1$

In this limit, Eq. {eq}`eq-p2-ch02-12` can be approximated by:

:::{math}
:label: eq-p2-ch02-17
\varepsilon \simeq \varepsilon_{\text{core}} - \frac{4\pi ne^2}{m\omega^2}
:::

As the frequency becomes large, the $1/\omega^2$ dependence of the free carrier contribution guarantees that free carrier effects will become less important, and other processes will dominate. In practice, these other processes are the interband processes which in Eq. {eq}`eq-p2-ch02-17` are dealt with in a very simplified form through the core dielectric constant $\varepsilon_{\text{core}}$. Using this approximation in the high frequency limit, we can neglect the free carrier contribution in Eq. {eq}`eq-p2-ch02-17` to obtain

:::{math}
:label: eq-p2-ch02-18
\sqrt{\varepsilon} \cong \sqrt{\varepsilon_{\text{core}}} = \text{real}
:::

Equation {eq}`eq-p2-ch02-18` implies that $\tilde{n} > 0$ and $\tilde{k}=0$ in the limit of $\omega\tau \gg 1$, with

:::{math}
:label: eq-p2-ch02-19
\mathcal{R} \to \frac{(\tilde{n}-1)^2}{(\tilde{n}+1)^2}
:::

where $\tilde{n} = \sqrt{\varepsilon_{\text{core}}}$. Thus, in the limit of very high frequencies, the Drude contribution is unimportant and the behavior of all materials is like that for a dielectric.

## 2.4 The Plasma Frequency

Thus, at very low frequencies the optical properties of semiconductors exhibit a metal-like behavior, while at very high frequencies their optical properties are like those of insulators. A characteristic frequency at which the material changes from a metallic to a dielectric response is called the plasma frequency $\hat{\omega}_p$, which is defined as that frequency at which the real part of the dielectric function vanishes $\varepsilon_1(\hat{\omega}_p) = 0$. According to the Drude theory (Eq. {eq}`eq-p2-ch02-12`), we have

:::{math}
:label: eq-p2-ch02-20
\varepsilon = \varepsilon_1 + i\varepsilon_2 = \varepsilon_{\text{core}} + \frac{4\pi i}{\omega}\frac{ne^2\tau}{m(1-i\omega\tau)} \cdot \left(\frac{1+i\omega\tau}{1+i\omega\tau}\right)
:::

where we have written $\varepsilon$ in a form which exhibits its real and imaginary parts explicitly. We can then write the real and imaginary parts $\varepsilon_1(\omega)$ and $\varepsilon_2(\omega)$ as:

:::{math}
:label: eq-p2-ch02-21
\varepsilon_1(\omega) = \varepsilon_{\text{core}} - \frac{4\pi ne^2\tau^2}{m(1+\omega^2\tau^2)} \qquad \varepsilon_2(\omega) = \frac{4\pi}{\omega}\frac{ne^2\tau}{m(1+\omega^2\tau^2)}
:::

The free carrier term makes a negative contribution to $\varepsilon_1$ which tends to cancel the core contribution shown schematically in {numref}`fig-p2-ch02-1`.

:::{figure} images/fig-p2-ch02-1.png
:name: fig-p2-ch02-1
:width: 60%
:align: center
Figure 2.1: The frequency dependence $\varepsilon_1(\omega)$, showing the definition of the plasma frequency $\hat{\omega}_p$ by the relation $\varepsilon_1(\hat{\omega}_p) = 0$.
:::

We see in {numref}`fig-p2-ch02-1` that $\varepsilon_1(\omega)$ vanishes at some frequency ($\hat{\omega}_p$) so that we can write

:::{math}
:label: eq-p2-ch02-22
\varepsilon_1(\hat{\omega}_p) = 0 = \varepsilon_{\text{core}} - \frac{4\pi ne^2\hat{\omega}_p^2\tau^2}{m(1+\hat{\omega}_p^2\tau^2)}
:::

which yields

:::{math}
:label: eq-p2-ch02-23
\hat{\omega}_p^2 = \frac{4\pi ne^2}{m\varepsilon_{\text{core}}} - \frac{1}{\tau^2} = \omega_p^2 - \frac{1}{\tau^2}
:::

Since the term $(-1/\tau^2)$ in Eq. {eq}`eq-p2-ch02-23` is usually small compared with $\omega_p^2$, it is customary to neglect this term and to identify the plasma frequency with $\omega_p$ defined by

:::{math}
:label: eq-p2-ch02-24
\omega_p^2 = \frac{4\pi ne^2}{m\varepsilon_{\text{core}}}
:::

in which screening of free carriers occurs through the core dielectric constant $\varepsilon_{\text{core}}$ of the medium. If $\varepsilon_{\text{core}}$ is too small, then $\varepsilon_1(\omega)$ never goes positive and there is no plasma frequency. The condition for the existence of a plasma frequency is

:::{math}
:label: eq-p2-ch02-25
\varepsilon_{\text{core}} > \frac{4\pi ne^2\tau^2}{m}
:::

The quantity $\omega_p$ in Eq. {eq}`eq-p2-ch02-24` is called the screened plasma frequency in the literature. Another quantity called the unscreened plasma frequency obtained from Eq. {eq}`eq-p2-ch02-24` by setting $\varepsilon_{\text{core}}=1$ is also used in the literature.

The general appearance of the reflectivity as a function of photon energy for a degenerate semiconductor or a metal is shown in {numref}`fig-p2-ch02-2`. At low frequencies, free carrier conduction dominates, and the reflectivity is $\simeq 100\%$. In the high frequency limit, we have

:::{math}
:label: eq-p2-ch02-26
\mathcal{R} \sim \frac{(\tilde{n}-1)^2}{(\tilde{n}+1)^2}
:::

:::{figure} images/fig-p2-ch02-2.png
:name: fig-p2-ch02-2
:width: 60%
:align: center
Figure 2.2: Reflectivity vs $\omega$ for a metal or a degenerate semiconductor in a frequency range where interband transitions are not important and the plasma frequency $\omega_p$ occurs near the minimum in reflectivity $\mathcal{R}$.
:::

which also is large, if $\tilde{n} \gg 1$. In the vicinity of the plasma frequency, $\varepsilon_1(\omega_1)$ is small by definition; furthermore, $\varepsilon_2(\omega_p)$ is also small, since from Eq. {eq}`eq-p2-ch02-21`

:::{math}
:label: eq-p2-ch02-27
\varepsilon_2(\omega_p) = \left(\frac{4\pi}{m\omega_p}\right)\frac{ne^2\tau}{1+(\omega_p\tau)^2}
:::

and if $\omega_p\tau \gg 1$

:::{math}
:label: eq-p2-ch02-28
\varepsilon_2(\omega_p) \cong \frac{\varepsilon_{\text{core}}}{\omega_p\tau}
:::

so that $\varepsilon_2(\omega_p)$ is often small. With $\varepsilon_1(\omega_p)=0$, we have from {numref}`eq-p2-ch01-25` $\tilde{n} \cong \tilde{k}$, and $\varepsilon_2(\omega_p) = 2\tilde{n}\tilde{k} \simeq 2\tilde{n}^2$. We thus see that $\tilde{n}$ tends to be small near $\omega_p$ and consequently $\mathcal{R}$ is also small (see {numref}`fig-p2-ch02-2`). The steepness of the dip at the plasma frequency is governed by the relaxation time $\tau$; the longer the relaxation time $\tau$, the sharper the plasma structure.

In metals, free carrier effects are almost always studied by reflectivity techniques because of the high optical absorption of metals at low frequency. For metals, the free carrier conductivity appears to be quite well described by the simple Drude theory. In studying free carrier effects in semiconductors, it is usually more accurate to use absorption techniques, which are discussed in Chapter 11. Because of the connection between the optical and the electrical properties of a solid through the conductivity tensor, transparent materials are expected to be poor electrical conductors while highly reflecting materials are expected to be reasonably good electrical conductors. It is, however, possible for a material to have its plasma frequency just below visible frequencies, so that the material will be a good electrical conductor, yet be transparent at visible frequencies. Because of the close connection between the optical and electrical properties, free carrier effects are sometimes exploited in the determination of the carrier density in instances where Hall effect measurements are difficult to make.

The contribution of holes to the optical conduction is of the same sign as for the electrons, since the conductivity depends on an even power of the charge ($\sigma \propto e^2$). In terms of the complex dielectric constant, we can write the contribution from electrons and holes as

:::{math}
:label: eq-p2-ch02-29
\varepsilon = \varepsilon_{\text{core}} + \frac{4\pi i}{\omega}\left[\frac{n_e e^2\tau_e}{m_e(1-i\omega\tau_e)} + \frac{n_h e^2\tau_h}{m_h(1-i\omega\tau_h)}\right]
:::

where the parameters $n_e$, $\tau_e$, and $m_e$ pertain to the electron carriers and $n_h$, $\tau_h$, and $m_h$ are for the holes. The plasma frequency is again found by setting $\varepsilon_1(\omega)=0$. If there are multiple electron or hole carrier pockets, as is common for semiconductors, the contributions from each carrier type is additive, using a formula similar to Eq. {eq}`eq-p2-ch02-29`.

We will now treat another conduction process in Chapter 3 which is due to interband transitions. In the above discussion, interband transitions were included in an extremely approximate way. That is, interband transitions were treated through a frequency independent core dielectric constant $\varepsilon_{\text{core}}$ (see Eq. {eq}`eq-p2-ch02-12`). In Chapter 3 we consider the frequency dependence of this important contribution.
