---
title: "A Time Dependent Perturbation Theory"
abstract: >
  A self-contained review of time-dependent perturbation theory used throughout the
  optical properties of solids. It derives the general expansion in the unperturbed
  eigenstates, the first-order transition amplitudes for constant and sinusoidal
  perturbations, Fermi's Golden Rule for the transition rate, and the second-order
  theory required for indirect optical transitions.
---

# A Time Dependent Perturbation Theory

**References**

- Eisberg, *Fundamentals of Modern Physics*, Ch. 9
- Schiff, *Quantum Mechanics*, Ch. 8

## A.1 General Formulation

To proceed further with the formal development of the optical properties of solids, we need to
consider how to handle the effect of time-dependent electromagnetic fields quantum mechanically.
The most important case of interest is the one where the external field is a sinusoidal function
of time. For most practical applications, the external fields are sufficiently weak, so that
their effect can be handled within the framework of perturbation theory. If the perturbation has
an explicit time dependence, it must be handled by time-dependent perturbation theory. Practical
problems which are handled by time-dependent perturbation theory include such subjects as
magnetic resonance (nuclear and electronic spin), cyclotron resonance and optical properties of
solids. We give here a brief review of the subject.

In doing time-dependent perturbation theory we write the total Hamiltonian $H$ as

```{math}
:label: eq-p2-appA-1
H = H_0 + H'(t)
```

where $H_0$ is the unperturbed Hamiltonian and $H'(t)$ is the time-dependent perturbation. We
assume here that we know how to solve the unperturbed time independent problem for its
eigenvalues $E_n$ and corresponding eigenfunctions $u_n$.

```{math}
:label: eq-p2-appA-2
H_0 u_n = E_n u_n.
```

Since $H'(t)$ has an explicit time dependence, then "energy" is no longer a "constant of the
motion". Since we no longer have stationary, time-independent solutions, we must use the
time-dependent form of Schrödinger's equation, which is

```{math}
:label: eq-p2-appA-3
i\hbar \frac{\partial \psi}{\partial t} = H\psi = (H_0 + H')\psi.
```

Now, if we didn't have the perturbation term $H'(t)$ to contend with, we would set

```{math}
:label: eq-p2-appA-4
\psi(\vec{r}, t) = u_n(\vec{r}) e^{-i E_n t/\hbar}
```

where $u_n(\vec{r})$ is independent of time and satisfies {eq}`eq-p2-appA-2`. Thus all the time
dependence of $\psi(\vec{r}, t)$ is contained in the phase factor $e^{-i E_n t/\hbar}$. For
$H'(t) = 0$, it immediately follows that

```{math}
:label: eq-p2-appA-5
i\hbar \frac{\partial \psi}{\partial t} = E_n \psi
```

which yields the time-independent Schrödinger equation. With the perturbation present, we expand
the time dependent functions $\psi(\vec{r}, t)$ in terms of the complete set
$u_n(\vec{r}) e^{-i E_n t/\hbar}$

```{math}
:label: eq-p2-appA-6
\psi(\vec{r}, t) = \sum_n a_n(t) u_n(\vec{r}) e^{-i E_n t/\hbar}
```

where the $a_n(t)$ are the time-dependent expansion coefficients. Substituting {eq}`eq-p2-appA-6`
in the time-dependent Schrödinger equation ({eq}`eq-p2-appA-3`) we obtain

```{math}
:label: eq-p2-appA-7
i\hbar \sum_n \dot{a}_n(t) u_n(\vec{r}) e^{-i E_n t/\hbar}
+ \sum_n a_n(t) u_n(\vec{r}) E_n e^{-i E_n t/\hbar}
= \sum_n a_n(t) \big[ E_n + H'(t) \big] u_n(\vec{r}) e^{-i E_n t/\hbar}
```

where $\dot{a}_n(t)$ denotes the time derivative $d a_n(t)/dt$. We note that because of
{eq}`eq-p2-appA-2` the second term on the left hand side of {eq}`eq-p2-appA-7` is canceled by the
first term on the right hand side.

We now multiply on the left hand side of {eq}`eq-p2-appA-7` by $u_k^*(\vec{r})$ and integrate over
all space. If we make use of the orthogonality of the eigenfunctions

```{math}
:label: eq-p2-appA-8
\int u_k^*(\vec{r})\, u_n(\vec{r})\, d^3r = \delta_{n,k}
```

we obtain from {eq}`eq-p2-appA-7` the result

```{math}
:label: eq-p2-appA-9
i\hbar \sum_n \dot{a}_n(t) u_n e^{-i E_n t/\hbar}
= \sum_n a_n(t) H'(t) u_n e^{-i E_n t/\hbar}
```

which yields

```{math}
:label: eq-p2-appA-10
i\hbar \dot{a}_k e^{-i E_k t/\hbar}
= \sum_n a_n(t) \langle k|H'(t)|n\rangle e^{-i E_n t/\hbar}
```

where we have written the matrix element

```{math}
:label: eq-p2-appA-11
\langle k|H'(t)|n\rangle
= \int u_k^*(\vec{r})\, H'(t)\, u_n(\vec{r})\, d^3r.
```

Since $H'(t)$ is time-dependent, so is the matrix element time-dependent, even though the matrix
element is taken between stationary states. We thus obtain the result

```{math}
:label: eq-p2-appA-12
i\hbar \dot{a}_k(t)
= \sum_n a_n(t) \langle k|H'(t)|n\rangle e^{i(E_k - E_n)t/\hbar}.
```

If we set

```{math}
:label: eq-p2-appA-13
\hbar \omega_{kn} = E_k - E_n
```

where $\omega_{kn}$ is the Bohr frequency between states $k$ and $n$, we have

```{math}
:label: eq-p2-appA-14
\dot{a}_k(t) = \frac{1}{i\hbar} \sum_n a_n(t) e^{i\omega_{kn} t} \langle k|H'(t)|n\rangle
```

in which the indicated matrix element is taken between eigenstates of the unperturbed Hamiltonian
$H_0$.

So far, no perturbation theory has been used and the result given in {eq}`eq-p2-appA-14` is exact.
We notice that the unperturbed Hamiltonian is completely absent from {eq}`eq-p2-appA-14`.
Nevertheless, its energy eigenvalues appear in $\omega_{kn}$ and its eigenfunctions in the matrix
element $\langle k|H'(t)|n\rangle$.

In applying perturbation theory, we consider the matrix element $\langle k|H(t)|n\rangle$ to be
small, and we write each time-dependent amplitude as an expansion in perturbation theory

```{math}
:label: eq-p2-appA-15
a_n = a_n^{(0)} + a_n^{(1)} + a_n^{(2)} + \cdots = \sum_{i=0}^{\infty} a_n^{(i)}
```

where the superscript gives the order of the term. Thus $a_n^{(0)}$ is the zeroth order term and
$a_n^{(i)}$ is the $i$th order correction to $a_n$. From {eq}`eq-p2-appA-14`, we see that $a_k(t)$
changes its value with time only because of the time dependent perturbation. Thus, the unperturbed
situation (0th order perturbation theory) must give no time dependence in zeroth order

```{math}
:label: eq-p2-appA-16
\dot{a}_m^{(0)} = 0
```

and the first order correction yields

```{math}
:label: eq-p2-appA-17
\dot{a}_m^{(1)} = \frac{1}{i\hbar} \sum_n a_n^{(0)} \langle m|H'(t)|n\rangle e^{i\omega_{mn}t}.
```

In the application of perturbation theory we assume, for example, that if we start in an eigenstate
$n = \ell$, only the coefficient $a_\ell^{(0)}$ will be appreciably large. Then all other terms in
the sum can be neglected. This gives us in 1st order perturbation theory

```{math}
:label: eq-p2-appA-18
\dot{a}_m^{(1)} = \frac{1}{i\hbar} a_\ell^{(0)} \langle m|H'|\ell\rangle e^{i\omega_{m\ell}t}
```

where $a_\ell^{(0)}$ is approximately unity.

For many cases of interest, this integration over the time variable can be performed and
$a_m^{(1)}$ rather than its time derivative is obtained. The two simple cases that can be
integrated easily are:

1. The perturbation $H'$ is constant but is turned on at some time ($t = 0$) and we look at the
   amplitudes of the wave function in the various states after the perturbation has been acting
   for some time $t > 0$.
2. The perturbation $H'$ has a sinusoidal time dependence with frequency $\omega$. This is the
   situation for all resonant phenomena.

Let us first consider case (1). Then

```{math}
:label: eq-p2-appA-19
a_m^{(1)}(t) = \frac{1}{i\hbar} \int_0^t \langle m|H'|\ell\rangle e^{i\omega_{m\ell}t'}\,dt'
= \frac{\langle m|H'|\ell\rangle}{i\hbar} \frac{e^{i\omega_{m\ell}t} - 1}{i\omega_{m\ell}}.
```

Similarly, for case (2), we can write

```{math}
:label: eq-p2-appA-20
H'(t) = H'(0) e^{\pm i\omega t}
```

to show the explicit time dependence, so that upon integration we obtain for the amplitudes
$a_m^{(1)}(t)$

```{math}
:label: eq-p2-appA-21
a_m^{(1)}(t) = \frac{1}{i\hbar} \langle m|H'(0)|\ell\rangle \int_0^t e^{i(\omega_{m\ell}\pm\omega)t'}\,dt'
= \frac{1}{i\hbar} \langle m|H'(0)|\ell\rangle \frac{e^{i(\omega_{m\ell}\pm\omega)t} - 1}{i(\omega_{m\ell}\pm\omega)}.
```

We interpret the time dependent amplitudes $|a_m^{(1)}(t)|^2$ as the probability of finding the
system in a state $m$ after a time $t$ has elapsed since the perturbation was applied; the system
was initially in a state $\ell \neq m$.

We thus obtain for case (1) given by {eq}`eq-p2-appA-19`

```{math}
:label: eq-p2-appA-22
|a_m^{(1)}(t)|^2 = \left(\frac{|\langle m|H'|\ell\rangle|^2}{\hbar^2}\right)
\left(\frac{|e^{i\omega_{m\ell}t} - 1|^2}{\omega_{m\ell}^2}\right)
```

and, equivalently,

```{math}
:label: eq-p2-appA-23
|a_m^{(1)}(t)|^2 = \left(\frac{|\langle m|H'|\ell\rangle|^2}{\hbar^2}\right)
\left(\frac{4\sin^2(\omega_{m\ell}t/2)}{\omega_{m\ell}^2}\right).
```

Clearly for case (2), the same result follows except that $\omega_{m\ell}$ is replaced by
$(\omega_{m\ell}\pm \omega)$ where $\omega$ is the applied frequency and a resonant denominator
results for the transition probability amplitude. It is clear from the above arguments that for
both cases (1) and (2), the explicit time dependence is contained in an oscillatory term of the
form $[\sin^2(\omega' t/2)/\omega'^2]$ where $\omega' = \omega_{m\ell}$ for the case (1) and
$\omega' = \omega_{m\ell}\pm \omega$ for case (2). This function was previously encountered in
diffraction theory and looks like that shown in {numref}`fig-p2-appA-1`. Of special interest here
is the fact that the main contribution to this function comes for $\omega' \approx 0$, with the
height of the main peak proportional to $t^2/4$ and the width proportional to $1/t$. This means
that the area under the central peak goes as $t$. If we think of $|a_m(t)|^2$ as the probability
of finding the system in a state $m$, then for case (2), where we have a perturbation with
frequency $\omega$, the system attempts to make a transition from a state $\ell$ to a state $m$
with a transition probability proportional to the time the perturbation acts. If we then wait long
enough, a system in an energy state $\ell$ will make a transition to a state $m$, if photons of
the resonant frequency $\omega_{\ell m}$ are present.

:::{figure} images/fig-p2-appA-1.png
:name: fig-p2-appA-1
:width: 60%
:align: center

Figure A.1: Plot of $\sin^2(\omega' t/2)/\omega'^2$ vs. $\omega'$, a function which enters the calculation of time-dependent perturbation problems.
:::

## A.2 Fermi Golden Rule

Since the transition probability is proportional to the time the perturbation acts, it is
therefore useful to deal with a quantity called the transition probability per unit time and the
relation giving this quantity is called the Golden Rule (named by Fermi and often called Fermi's
Golden Rule).

In deriving the Golden Rule from {eq}`eq-p2-appA-19`, we must consider the system exposed to the
perturbation for a time sufficiently long so that we can make a meaningful measurement within the
framework of the Heisenberg uncertainty principle

```{math}
:label: eq-p2-appA-24
\Delta E\, \Delta t \sim \hbar
```

so that the uncertainty in energy (or frequency) during the time that the perturbation acts is

```{math}
:label: eq-p2-appA-25
\Delta E \sim \hbar/t
```

or

```{math}
:label: eq-p2-appA-26
\Delta \omega_{\ell m} \sim 2\pi/t.
```

But this is precisely the period of the oscillatory function shown in {numref}`fig-p2-appA-1`. In
this context, we must think of the concept of transition probability/unit time as encompassing a
range of energies and times consistent with the uncertainty principle. In the case of solids, it
is quite natural to do this anyhow, because the wave vector $\vec{k}$ is a quasi-continuous
variable. That is, there are a large number of $k$ states which have energies close to a given
energy. The quantum states labeled by wave vector $\vec{k}$ are close together in a solid having
about $10^{22}$ atoms/cm$^3$. Since the photon source itself has a bandwidth, we would
automatically want to consider a range of energy differences $\delta \hbar \omega'$. From this
point of view, we introduce the transition probability/unit time $W_m$ for making a transition to
a state $m$

```{math}
:label: eq-p2-appA-27
W_m = \frac{1}{t} \sum_{m'\approx m} \big| a_{m'}^{(1)}(t) \big|^2
```

where the summation is carried out over a range of energy states consistent with the uncertainty
principle; $\Delta \omega_{mm'} \sim 2\pi/t$.

Substituting for $|a_{m'}^{(1)}(t)|^2$ from {eq}`eq-p2-appA-23`, we have

```{math}
:label: eq-p2-appA-28
|a_m^{(1)}(t)|^2 = \left(\frac{4|\langle m|H'|\ell\rangle|^2}{\hbar^2}\right)
\left(\frac{\sin^2(\omega' t/2)}{\omega'^2}\right)
```

and the summation is replaced by an integration over a narrow energy range weighted by the density
of states $\rho(E_m)$ which gives the number of states per unit energy range. We thus obtain

```{math}
:label: eq-p2-appA-29
W_m = \frac{1}{\hbar^2 t} \int 4|H'_{m'\ell}|^2
\left(\frac{\sin^2(\omega_{m'\ell} t/2)}{\omega_{m'\ell}^2}\right)
\rho(E_{m'})\, dE_{m'}
```

where we have written $H'_{m'\ell}$ for the matrix element $\langle m'|H'|\ell\rangle$.

But, by hypothesis, we are only considering energies within a small energy range $E_{m'}$ around
$E_m$ and over this range the matrix elements and density of final states will not be varying.
However, the function $[\sin^2(\omega' t/2)/\omega'^2]$ will be varying rapidly, as can be seen
from {numref}`fig-p2-appA-1`. Therefore, it is adequate to integrate {eq}`eq-p2-appA-29` only over
the rapidly varying function $[\sin^2(\omega t/2)]/\omega^2$. Writing $dE = \hbar\, d\omega'$, we
obtain

```{math}
:label: eq-p2-appA-30
W_m \simeq \left(\frac{4|H'_{m\ell}|^2 \rho(E_m)}{t\hbar^2}\right)
\int \left(\frac{\sin^2(\omega' t/2)}{\omega'^2}\right) d\omega'.
```

The most important contribution to the integral in {eq}`eq-p2-appA-30` comes from values of
$\omega$ close to $\omega'$. On the other hand, we know how to do this integral between
$-\infty$ and $+\infty$, since

```{math}
:label: eq-p2-appA-31
\int_{-\infty}^{\infty} \frac{\sin^2 x}{x^2}\, dx = \pi.
```

Therefore we can write an approximate relation from {eq}`eq-p2-appA-30` by setting
$x = \omega' t/2$

```{math}
:label: eq-p2-appA-32
W_m \simeq \frac{2\pi}{\hbar} |H'_{m\ell}|^2 \rho(E_m)
```

which is often called Fermi's Golden Rule. In the subsequent sections, we will apply the Fermi
Golden Rule to calculate the optical properties of solids.

If the initial state is a discrete level (such as donor impurity level) and the final state is a
continuum (such as conduction band), then the Fermi Golden Rule ({eq}`eq-p2-appA-32`) as written
yields the transition probability per unit time and $\rho(E_m)$ is interpreted as the density of
final states. Likewise if the final state is discrete and the initial state is a continuum, $W_m$
also gives the transition probability per unit time, only in this case $\rho(E_m)$ is interpreted
as the density of initial states.

For many important applications in solid state physics, the transitions of interest are between a
continuum of initial states and a continuum of final states. In this case the Fermi Golden Rule
must be interpreted in terms of a joint density of states, whereby the initial and final states
are separated by the photon energy $\hbar\omega$ inducing the transition. These issues are
discussed in Chapter 4.

## A.3 Time Dependent 2nd Order Perturbation Theory

This second order treatment is needed for indirect optical transitions, where

```{math}
:label: eq-p2-appA-33
H = H_0 + \lambda H'
```

and $\lambda \ll 1$. Here $H_0 \psi_0 = i\hbar\, \partial\psi_0/\partial t$. Expand $\psi$, the
solution to {eq}`eq-p2-appA-33`, in terms of the complete set of functions denoted by
$\psi_0 \equiv |n,\vec{k}\rangle$

```{math}
:label: eq-p2-appA-34
\psi = \sum_{n,\vec{k}} a_n(\vec{k}, t) e^{-i E_n(\vec{k}) t/\hbar} |n,\vec{k}\rangle
```

where $|n,\vec{k}\rangle$ is a Bloch function describing the eigenstates of the unperturbed problem

```{math}
:label: eq-p2-appA-35
H \psi = i\hbar \dot{\psi}.
```

Inserting {eq}`eq-p2-appA-34` into {eq}`eq-p2-appA-35` gives

```{math}
:label: eq-p2-appA-36
\sum_{n,\vec{k}} a_n(\vec{k},t) E_n(\vec{k}) e^{-i E_n(\vec{k})t/\hbar} |n,\vec{k}\rangle
+ \sum_{n,\vec{k}} a_n(\vec{k},t) e^{-i E_n(\vec{k})t/\hbar} \lambda H' |n,\vec{k}\rangle
= i\hbar \sum_{n,\vec{k}} \dot{a}_n(\vec{k},t) e^{-i E_n(\vec{k})t/\hbar} |n,\vec{k}\rangle
+ \sum_{n,\vec{k}} a_n(\vec{k},t) E_n(\vec{k}) e^{-i E_n(\vec{k})t/\hbar} |n,\vec{k}\rangle
```

which gives

```{math}
:label: eq-p2-appA-37
\dot{a}_m(\vec{k}',t) = \frac{1}{i\hbar} \sum_{n,\vec{k}} a_n(\vec{k},t)
\exp\!\left[ \frac{i}{\hbar}\big(E_m(\vec{k}') - E_n(\vec{k})\big)t \right]
\langle m,\vec{k}'|\lambda H'|n,\vec{k}\rangle.
```

We expand

```{math}
:label: eq-p2-appA-38
a_m(\vec{k}',t) = a_m^{(0)} + \lambda a_m^{(1)} + \lambda^2 a_m^{(2)} + \cdots
```

and let $a_j(\vec{k}, 0) = 1$, and all others $a_n(\vec{k}, 0) = 0$ where $n \neq j$.

To first order, as before,

```{math}
:label: eq-p2-appA-39
\lambda^2 \dot{a}_m^{(1)}(\vec{k}',t) = \frac{1}{i\hbar} \lambda a_n^{(0)}(\vec{k},t)
\exp\!\left[ \frac{i}{\hbar}\big(E_m(\vec{k}') - E_n(\vec{k})\big)t' \right]
\langle m,\vec{k}'|\lambda H'|n,\vec{k}\rangle
```

or

```{math}
:label: eq-p2-appA-40
a_m^{(1)}(\vec{k}',t) = \frac{1}{i\hbar} \int_0^t dt'\,
\exp\!\left[ \frac{i}{\hbar}\big(E_m(\vec{k}') - E_n(\vec{k})\big)t' \right]
\langle m,\vec{k}'|\lambda H'|n,\vec{k}\rangle.
```

To second order

```{math}
:label: eq-p2-appA-41
\lambda^2 \dot{a}_m^{(2)}(\vec{k}',t) = \frac{1}{i\hbar} \sum_{n,\vec{k}} \lambda a_n^{(1)}(\vec{k},t)
\exp\!\left[ \frac{i}{\hbar}\big(E_m(\vec{k}') - E_n(\vec{k})\big)t \right]
\langle m,\vec{k}'|\lambda H'|n,\vec{k}\rangle
```

or

```{math}
:label: eq-p2-appA-42
\dot{a}_m^{(2)}(\vec{k}',t) = -\frac{1}{\hbar^2} \sum_{n,\vec{k}} a_n^{(1)}(\vec{k},t)
\exp\!\left[ \frac{i}{\hbar}\big(E_m(\vec{k}') - E_n(\vec{k})\big)t \right]
\langle m,\vec{k}'|\lambda H'|n,\vec{k}\rangle
\int_0^t dt'\,
\exp\!\left[ \frac{i}{\hbar}\big(E_n(\vec{k}') - E_i(\vec{k})\big)t' \right]
\langle n,\vec{k}'|\lambda H'|i,\vec{k}\rangle.
```

We write the time dependence of the perturbation Hamiltonian explicitly as

```{math}
:label: eq-p2-appA-43
H' = \sum_\alpha H_\alpha e^{-i\omega_\alpha t}
```

and then {eq}`eq-p2-appA-42` can be written, after integrating twice

```{math}
:label: eq-p2-appA-44
|a_f^{(2)}(\vec{k}_f, t)|^2 = 2\pi \hbar t
\sum_{m,\vec{k},\alpha,\alpha'}
\frac{|\langle f|H'_{\alpha'}|m,\vec{k}\rangle|^2\, |\langle m,\vec{k}|H'_\alpha|i\rangle|^2}
{(E_m(\vec{k}) - E_i - \hbar\omega_\alpha)^2}
\, \delta(E_f - E_i - \hbar\omega_\alpha - \hbar\omega_{\alpha'}).
```

This second-order time-dependent perturbation theory expression is used to derive the probability
of an indirect interband transition.
