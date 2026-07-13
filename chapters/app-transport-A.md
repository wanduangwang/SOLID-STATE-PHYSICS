---
title: "Appendix A — Time-Independent Perturbation Theory"
abstract: "A review of time-independent perturbation theory: non-degenerate Rayleigh-Schrodinger and Brillouin-Wigner theory (energies and wave functions to second order), followed by degenerate (nearly-degenerate) perturbation theory treated via the secular equation."
---

# Appendix A — Time-Independent Perturbation Theory

## A.0 Overview of this Appendix

This appendix provides the mathematical foundation for the weak-binding approximation of Chapter 1 and the effective-mass theory of Chapter 3. It reviews time-independent perturbation theory: starting from the first- and second-order corrections in the non-degenerate Rayleigh-Schrodinger form (Eq. {eq}`eq-apptransport-A-26`), proceeding to the self-consistent Brillouin-Wigner form (Eq. {eq}`eq-apptransport-A-31`, {eq}`eq-apptransport-A-32`), and finally giving degenerate (nearly-degenerate) perturbation theory (Eq. {eq}`eq-apptransport-A-33` to {eq}`eq-apptransport-A-40`).

## A.1 Introduction

Another review topic that we discuss here is time-independent perturbation theory because of its importance in experimental solid state physics in general and transport properties in particular.

There are many mathematical problems that occur in nature that cannot be solved exactly. It also happens frequently that a *related* problem can be solved *exactly*. Perturbation theory gives us a method for relating the problem that can be solved exactly to the one that cannot. This occurrence is more general than quantum mechanics — many problems in electromagnetic theory are handled by the techniques of perturbation theory. In this course however, we will think mostly about quantum mechanical systems, as occur typically in solid state physics.

Suppose that the Hamiltonian for our system can be written as

:::{math}
:label: eq-apptransport-A-1
\mathcal{H} = \mathcal{H}_0 + \mathcal{H}'
:::

where $\mathcal{H}_0$ is the part that we can solve exactly and $\mathcal{H}'$ is the part that we cannot solve. Provided that $\mathcal{H}' \ll \mathcal{H}_0$ we can use perturbation theory; that is, we consider the solution of the unperturbed Hamiltonian $\mathcal{H}_0$ and then calculate the effect of the perturbation Hamiltonian $\mathcal{H}'$. For example, we can solve the hydrogen atom energy levels exactly, but when we apply an electric or a magnetic field, we can no longer solve the problem exactly. For this reason, we treat the effect of the external fields as a perturbation, provided that the energy associated with these fields is small:

:::{math}
:label: eq-apptransport-A-2
\mathcal{H} = \frac{p^2}{2m} - \frac{e^2}{r} - e\vec{r}\cdot\vec{E} = \mathcal{H}_0 + \mathcal{H}'
:::

where

:::{math}
:label: eq-apptransport-A-3
\mathcal{H}_0 = \frac{p^2}{2m} - \frac{e^2}{r}
:::

and

:::{math}
:label: eq-apptransport-A-4
\mathcal{H}' = -e\vec{r}\cdot\vec{E}.
:::

As another illustration of an application of perturbation theory, consider a weak periodic potential in a solid. We can calculate the free electron energy levels (empty lattice) exactly. We would like to relate the weak potential situation to the empty lattice problem, and this can be done by considering the weak periodic potential as a perturbation.

### A.1.1 Non-degenerate Perturbation Theory

In non-degenerate perturbation theory we want to solve Schrödinger's equation

:::{math}
:label: eq-apptransport-A-5
\mathcal{H}\psi_n = E_n\psi_n
:::

where

:::{math}
:label: eq-apptransport-A-6
\mathcal{H} = \mathcal{H}_0 + \mathcal{H}'
:::

and

:::{math}
:label: eq-apptransport-A-7
\mathcal{H}' \ll \mathcal{H}_0.
:::

It is then assumed that the solutions to the unperturbed problem

:::{math}
:label: eq-apptransport-A-8
\mathcal{H}_0\psi_n^0 = E_n^0\psi_n^0
:::

are known, in which we have labeled the unperturbed energy by $E_n^0$ and the unperturbed wave function by $\psi_n^0$. By *non-degenerate* we mean that there is only one eigenfunction $\psi_n^0$ associated with each eigenvalue $E_n^0$.

The wave functions $\psi_n^0$ form a complete orthonormal set

:::{math}
:label: eq-apptransport-A-9
\int \psi_n^{0*}\psi_m^0\,d^3r = \langle \psi_n^0 | \psi_m^0 \rangle = \delta_{nm}.
:::

Since $\mathcal{H}'$ is small, the wave functions for the total problem $\psi_n$ do not differ greatly from the wave functions $\psi_n^0$ for the unperturbed problem. So we expand $\psi_{n'}$ in terms of the complete set of $\psi_n^0$ functions

:::{math}
:label: eq-apptransport-A-10
\psi_{n'} = \sum_n a_n \psi_n^0.
:::

Such an expansion can always be made; that is no approximation. We then substitute the expansion of Eq. {eq}`eq-apptransport-A-10` into Schrödinger's equation (Eq. {eq}`eq-apptransport-A-5`) to obtain

:::{math}
:label: eq-apptransport-A-11
\mathcal{H}\psi_{n'} = \sum_n a_n(\mathcal{H}_0 + \mathcal{H}')\psi_n^0
= \sum_n a_n(E_n^0 + \mathcal{H}')\psi_n^0 = E_{n'}\sum_n a_n\psi_n^0
:::

and therefore we can write

:::{math}
:label: eq-apptransport-A-12
\sum_n a_n(E_{n'} - E_n^0)\psi_n^0 = \sum_n a_n\mathcal{H}'\psi_n^0.
:::

If we are looking for the perturbation to the level $m$, then we multiply Eq. {eq}`eq-apptransport-A-12` from the left by $\psi_m^{0*}$ and integrate over all space. On the left hand side of Eq. {eq}`eq-apptransport-A-12` we get $\langle \psi_m^0 | \psi_m^0 \rangle = \delta_{mn}$ while on the right hand side we have the matrix element of the perturbation Hamiltonian taken between the unperturbed states:

:::{math}
:label: eq-apptransport-A-13
a_m(E_{n'} - E_m^0) = \sum_n a_n\langle \psi_m^0 | \mathcal{H}' | \psi_n^0 \rangle \equiv \sum_n a_n\mathcal{H}'_{mn}
:::

where we have written the indicated matrix element as $\mathcal{H}'_{mn}$. Equation {eq}`eq-apptransport-A-13` is an iterative equation on the $a_n$ coefficients, where each $a_m$ coefficient is related to a complete set of $a_n$ coefficients by the relation

:::{math}
:label: eq-apptransport-A-14
a_m = \frac{1}{E_{n'} - E_m^0}\sum_n a_n\langle \psi_m^0 | \mathcal{H}' | \psi_n^0 \rangle
= \frac{1}{E_{n'} - E_m^0}\sum_n a_n\mathcal{H}'_{mn}
:::

in which the summation includes the $n = n'$ and $m$ terms. We can rewrite Eq. {eq}`eq-apptransport-A-14` to involve terms in the sum $n \neq m$

:::{math}
:label: eq-apptransport-A-15
a_m(E_{n'} - E_m^0) = a_m\mathcal{H}'_{mm} + \sum_{n\neq m} a_n\mathcal{H}'_{mn}
:::

so that the coefficient $a_m$ is related to all the other $a_n$ coefficients by:

:::{math}
:label: eq-apptransport-A-16
a_m = \frac{1}{E_{n'} - E_m^0 - \mathcal{H}'_{mm}}\sum_{n\neq m} a_n\mathcal{H}'_{mn}
:::

where $n'$ is an index denoting the energy of the state we are seeking. The equation ({eq}`eq-apptransport-A-16`) written as

:::{math}
:label: eq-apptransport-A-17
a_m(E_{n'} - E_m^0 - \mathcal{H}'_{mm}) = \sum_{n\neq m} a_n\mathcal{H}'_{mn}
:::

is an identity in the $a_n$ coefficients. If the perturbation is small then $E_{n'}$ is very close to $E_m^0$ and the first order corrections are found by setting the coefficient on the right hand side equal to zero and $n' = m$. The next order of approximation is found by substituting for $a_n$ on the right hand side of Eq. {eq}`eq-apptransport-A-17` and substituting for $a_n$ the expression

:::{math}
:label: eq-apptransport-A-18
a_n = \frac{1}{E_{n'} - E_n^0 - \mathcal{H}'_{nn}}\sum_{n''\neq n} a_{n''}\mathcal{H}'_{nn''}
:::

which is obtained from Eq. {eq}`eq-apptransport-A-16` by the transcription $m \to n$ and $n \to n''$. In the above, the energy level $E_{n'} = E_m$ is the level for which we are calculating the perturbation. We now look for the $a_m$ term in the sum $\sum_{n''\neq n} a_{n''}\mathcal{H}'_{nn''}$ of Eq. {eq}`eq-apptransport-A-18` and bring it to the left hand side of Eq. {eq}`eq-apptransport-A-17`. If we are satisfied with our solutions, we end the perturbation calculation at this point. If we are not satisfied, we substitute for the $a_{n''}$ coefficients in Eq. {eq}`eq-apptransport-A-18` using the same basic equation as Eq. {eq}`eq-apptransport-A-18` to obtain a triple sum. We then select out the $a_m$ term, bring it to the left hand side of Eq. {eq}`eq-apptransport-A-17`, etc. This procedure gives us an easy recipe to find the energy in Eq. {eq}`eq-apptransport-A-11` to any order of perturbation theory. We now write these iterations down more explicitly for first and second order perturbation theory.

**1st Order Perturbation Theory**

In this case, no iterations of Eq. {eq}`eq-apptransport-A-17` are needed and the sum $\sum_{n\neq m} a_n\mathcal{H}'_{mn}$ on the right hand side of Eq. {eq}`eq-apptransport-A-17` is neglected, for the reason that if the perturbation is small, $\psi_{n'} \sim \psi_n^0$. Hence only $a_m$ in Eq. {eq}`eq-apptransport-A-10` contributes significantly. We merely write $E_{n'} = E_m$ to obtain:

:::{math}
:label: eq-apptransport-A-19
a_m(E_m - E_m^0 - \mathcal{H}'_{mm}) = 0.
:::

Since the $a_m$ coefficients are arbitrary coefficients, this relation must hold for all $a_m$ so that

:::{math}
:label: eq-apptransport-A-20
(E_m - E_m^0 - \mathcal{H}'_{mm}) = 0
:::

or

:::{math}
:label: eq-apptransport-A-21
E_m = E_m^0 + \mathcal{H}'_{mm}.
:::

We write Eq. {eq}`eq-apptransport-A-21` even more explicitly so that the energy for state $m$ for the perturbed problem $E_m$ is related to the unperturbed energy $E_m^0$ by

:::{math}
:label: eq-apptransport-A-22
E_m = E_m^0 + \langle \psi_m^0 | \mathcal{H}' | \psi_m^0 \rangle
:::

where the indicated diagonal matrix element of $\mathcal{H}'$ can be integrated as the average of the perturbation in the state $\psi_m^0$. The wave functions to lowest order are not changed

:::{math}
:label: eq-apptransport-A-23
\psi_m = \psi_m^0.
:::

**2nd order perturbation theory**

If we carry out the perturbation theory to the next order of approximation, one further iteration of Eq. {eq}`eq-apptransport-A-17` is required:

:::{math}
:label: eq-apptransport-A-24
a_m(E_m - E_m^0 - \mathcal{H}'_{mm}) = \sum_{n\neq m}\frac{1}{E_m - E_n^0 - \mathcal{H}'_{nn}}\sum_{n''\neq n} a_{n''}\mathcal{H}'_{nn''}\mathcal{H}'_{mn}
:::

in which we have substituted for the $a_n$ coefficient in Eq. {eq}`eq-apptransport-A-17` using the iteration relation given by Eq. {eq}`eq-apptransport-A-18`. We now pick out the term on the right hand side of Eq. {eq}`eq-apptransport-A-24` for which $n'' = m$ and bring that term to the left hand side of Eq. {eq}`eq-apptransport-A-24`. If no further iteration is to be done, we throw away what is left on the right hand side of Eq. {eq}`eq-apptransport-A-24` and get an expression for the arbitrary $a_m$ coefficients

:::{math}
:label: eq-apptransport-A-25
a_m\left[(E_m - E_m^0 - \mathcal{H}'_{mm}) - \sum_{n\neq m}\frac{\mathcal{H}'_{nm}\mathcal{H}'_{mn}}{E_m - E_n^0 - \mathcal{H}'_{nn}}\right] = 0.
:::

Since $a_m$ is arbitrary, the term in square brackets in Eq. {eq}`eq-apptransport-A-25` vanishes and the second order correction to the energy results:

:::{math}
:label: eq-apptransport-A-26
E_m = E_m^0 + \mathcal{H}'_{mm} + \sum_{n\neq m}\frac{|\mathcal{H}'_{mn}|^2}{E_m - E_n^0 - \mathcal{H}'_{nn}}
:::

in which the sum on states $n \neq m$ represents the 2nd order correction.

To this order in perturbation theory we must also consider corrections to the wave function

:::{math}
:label: eq-apptransport-A-27
\psi_m = \sum_n a_n\psi_n^0 = \psi_m^0 + \sum_{n\neq m} a_n\psi_n^0
:::

in which $\psi_m^0$ is the large term and the correction terms appear as a sum over all the other states $n \neq m$. In handling the correction term, we look for the $a_n$ coefficients, which from Eq. {eq}`eq-apptransport-A-18` are given by

:::{math}
:label: eq-apptransport-A-28
a_n = \frac{1}{E_n' - E_n^0 - \mathcal{H}'_{nn}}\sum_{n''\neq n} a_{n''}\mathcal{H}'_{nn''}.
:::

If we only wish to include the lowest order correction terms, we will take only the most important term, i.e., $n'' = m$, and we will also use the relation $a_m = 1$ in this order of approximation. Again using the identification $n' = m$, we obtain

:::{math}
:label: eq-apptransport-A-29
a_n = \frac{\mathcal{H}'_{nm}}{E_m - E_n^0 - \mathcal{H}'_{nn}}
:::

and

:::{math}
:label: eq-apptransport-A-30
\psi_m = \psi_m^0 + \sum_{n\neq m}\frac{\mathcal{H}'_{nm}\psi_n^0}{E_m - E_n^0 - \mathcal{H}'_{nn}}.
:::

For homework, you should do the next iteration to get 3rd order perturbation theory, in order to see if you really have mastered the technique (this will be an optional homework problem).

Now look at the results for the energy $E_m$ (Eq. {eq}`eq-apptransport-A-26`) and the wave function $\psi_m$ (Eq. {eq}`eq-apptransport-A-30`) for the 2nd order perturbation theory and observe that these solutions are implicit solutions. That is, the correction terms are themselves dependent on $E_m$. To obtain an explicit solution, we can do one of two things at this point.

1. We can ignore the fact that the energies differ from their unperturbed values in calculating the correction terms. This is known as **Rayleigh-Schrödinger perturbation theory**. This is the usual perturbation theory given in Quantum Mechanics texts and for homework you may review the proof as given in these texts.

2. We can take account of the fact that $E_m$ differs from $E_m^0$ by calculating the correction terms by an iteration procedure; the first time around, you substitute for $E_m$ the value that comes out of 1st order perturbation theory. We then calculate the second order correction to get $E_m$. We next take this $E_m$ value to compute the new second order correction term etc. until a convergent value for $E_m$ is reached. This iterative procedure is what is used in **Brillouin-Wigner** perturbation theory and is a better approximation than Rayleigh-Schrödinger perturbation theory to both the wave function and the energy eigenvalue for the same order in perturbation theory.

The Brillouin-Wigner method is often used for practical problems in solids. For example, if you have a 2-level system, the Brillouin-Wigner perturbation theory to second order gives an exact result, whereas Rayleigh-Schrödinger perturbation theory must be carried out to infinite order.

Let us summarize these ideas. If you have to compute only a small correction by perturbation theory, then it is advantageous to use Rayleigh-Schrödinger perturbation theory because it is much easier to use, since no iteration is needed. If one wants to do a more convergent perturbation theory (i.e., obtain a better answer to the same order in perturbation theory), then it is advantageous to use Brillouin-Wigner perturbation theory. There are other types of perturbation theory that are even more convergent and harder to use than Brillouin-Wigner perturbation theory (see Morse and Feshbach vol. 2). But these two types are the most important methods used in solid state physics today.

For your convenience we summarize here the results of the second-order non-degenerate Rayleigh-Schrödinger perturbation theory:

:::{math}
:label: eq-apptransport-A-31
E_m = E_m^0 + \mathcal{H}'_{mm} + \sum_n'\frac{|\mathcal{H}'_{nm}|^2}{E_m^0 - E_n^0} + \ldots
:::

:::{math}
:label: eq-apptransport-A-32
\psi_m = \psi_m^0 + \sum_n'\frac{\mathcal{H}'_{nm}\psi_n^0}{E_m^0 - E_n^0} + \ldots
:::

where the sums in Eqs. {eq}`eq-apptransport-A-31` and {eq}`eq-apptransport-A-32` denoted by primes exclude the $m = n$ term. Thus, Brillouin-Wigner perturbation theory (Eqs. {eq}`eq-apptransport-A-26` and {eq}`eq-apptransport-A-30`) contains contributions in second order which occur in higher order in the Rayleigh-Schrödinger form. In practice, Brillouin-Wigner perturbation theory is useful when the perturbation term is too large to be handled conveniently by Rayleigh-Schrödinger perturbation theory, but still small enough for perturbation theory to work insofar as the perturbation expansion forms a convergent series.

### A.1.2 Degenerate Perturbation Theory

It often happens that a number of quantum mechanical levels have the same or nearly the same energy. If they have exactly the same energy, we know that we can make any linear combination of these states that we like and get a new eigenstate also with the same energy. In the case of degenerate states, we have to do perturbation theory a little differently, as described in the following section.

Suppose that we have an $f$-fold degeneracy (or near-degeneracy) of energy levels

$$\underbrace{\psi_1^0, \psi_2^0, \ldots \psi_f^0}_{\text{states with the same or nearly the same energy}}\qquad\underbrace{\psi_{f+1}^0, \psi_{f+2}^0, \ldots}_{\text{states with quite different energies}}$$

We will call the set of states with the same (or approximately the same) energy a "nearly degenerate set" (NDS). In the case of degenerate sets, the iterative Eq. {eq}`eq-apptransport-A-17` still holds. The only difference is that for the degenerate case we solve for the perturbed energies by a different technique, as described below.

Starting with Eq. {eq}`eq-apptransport-A-17`, we now bring to the left-hand side of the iterative equation all terms involving the $f$ energy levels that are in the NDS. If we wish to calculate an energy within the NDS in the presence of a perturbation, we consider all the $a_n$'s within the NDS as large, and those outside the set as small. To first order in perturbation theory, we ignore the coupling to terms outside the NDS and we get $f$ linear homogeneous equations in the $a_n$'s where $n = 1, 2, \ldots f$. We thus obtain the following equations from Eq. {eq}`eq-apptransport-A-17`:

:::{math}
:label: eq-apptransport-A-33
\begin{aligned}
a_1(E_1^0 + \mathcal{H}'_{11} - E) &\quad + a_2\mathcal{H}'_{12} \quad + \ldots \quad + a_f\mathcal{H}'_{1f} &&= 0\\
a_1\mathcal{H}'_{21} &\quad + a_2(E_2^0 + \mathcal{H}'_{22} - E) \quad + \ldots \quad + a_f\mathcal{H}'_{2f} &&= 0\\
\vdots \qquad &\quad \vdots \qquad\qquad \ddots \qquad \vdots \\
a_1\mathcal{H}'_{f1} &\quad + a_2\mathcal{H}'_{f2} \quad + \ldots \quad + a_f(E_f^0 + \mathcal{H}'_{ff} - E) &&= 0.
\end{aligned}
:::

In order to have a solution of these $f$ linear equations, we demand that the coefficient determinant vanish:

:::{math}
:label: eq-apptransport-A-34
\begin{vmatrix}
(E_1^0 + \mathcal{H}'_{11} - E) & \mathcal{H}'_{12} & \mathcal{H}'_{13} & \cdots & \mathcal{H}'_{1f} \\
\mathcal{H}'_{21} & (E_2^0 + \mathcal{H}'_{22} - E) & \mathcal{H}'_{23} & \cdots & \mathcal{H}'_{2f} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
\mathcal{H}'_{f1} & \mathcal{H}'_{f2} & \cdots & \cdots & (E_f^0 + \mathcal{H}'_{ff} - E)
\end{vmatrix} = 0
:::

The $f$ eigenvalues that we are looking for are the eigenvalues of the matrix in Eq. {eq}`eq-apptransport-A-34` and the set of orthogonal states are the corresponding eigenvectors. Remember that the matrix elements $\mathcal{H}'_{ij}$ that occur in the above determinant are taken between the unperturbed states in the NDS.

The generalization to second order degenerate perturbation theory is immediate. In this case, Eqs. {eq}`eq-apptransport-A-33` and {eq}`eq-apptransport-A-34` have additional terms. For example, the first relation in Eq. {eq}`eq-apptransport-A-33` would then become

:::{math}
:label: eq-apptransport-A-35
a_1(E_1^0 + \mathcal{H}'_{11} - E) + a_2\mathcal{H}'_{12} + a_3\mathcal{H}'_{13} + \ldots + a_f\mathcal{H}'_{1f} = -\sum_{n\neq NDS} a_n\mathcal{H}'_{1n}
:::

and for the $a_n$ in the sum in Eq. {eq}`eq-apptransport-A-35`, which are now small (because they are outside the NDS), we would use our iterative form

:::{math}
:label: eq-apptransport-A-36
a_n = \frac{1}{E - E_n^0 - \mathcal{H}'_{nn}}\sum_{m\neq n} a_m\mathcal{H}'_{nm}.
:::

But we must only consider the terms in the above sum which are large; these terms are all in the NDS. This argument shows that every term on the left side of Eq. {eq}`eq-apptransport-A-35` will have a correction term. For example the correction term to a general coefficient $a_i$ will look as follows:

:::{math}
:label: eq-apptransport-A-37
a_i\mathcal{H}'_{1i} + a_i\sum_{n\neq NDS}\frac{\mathcal{H}'_{1n}\mathcal{H}'_{ni}}{E - E_n^0 - \mathcal{H}'_{nn}}
:::

where the first term is the original term from 1st order degenerate perturbation theory and the term from states outside the NDS gives the 2nd order correction terms. So, if we are doing higher order degenerate perturbation theory, we write for each entry in the secular equation the appropriate correction terms (Eq. {eq}`eq-apptransport-A-37`) that are obtained from these iterations. For example, in 2nd order degenerate perturbation theory, the $(1,1)$ entry to the matrix in Eq. {eq}`eq-apptransport-A-34` would be

:::{math}
:label: eq-apptransport-A-38
E_1^0 + \mathcal{H}'_{11} + \sum_{n\neq NDS}\frac{|\mathcal{H}'_{1n}|^2}{E - E_n^0 - \mathcal{H}'_{nn}} - E.
:::

As a further illustration let us write down the $(1,2)$ entry:

:::{math}
:label: eq-apptransport-A-39
\mathcal{H}'_{12} + \sum_{n\neq NDS}\frac{\mathcal{H}'_{1n}\mathcal{H}'_{n2}}{E - E_n^0 - \mathcal{H}'_{nn}}.
:::

Again we have an implicit dependence of the 2nd order term in Eqs. {eq}`eq-apptransport-A-38` and {eq}`eq-apptransport-A-39` on the energy eigenvalue that we are looking for. To do 2nd order degenerate perturbation we again have two options. If we take the energy $E$ in Eqs. {eq}`eq-apptransport-A-38` and {eq}`eq-apptransport-A-39` as the unperturbed energy in computing the correction terms, we have 2nd order degenerate Rayleigh-Schrödinger perturbation theory. On the other hand, if we iterate to get the best correction term, then we call it Brillouin-Wigner perturbation theory.

How do we know in an actual problem when to use degenerate 1st or degenerate 2nd order perturbation theory? If the matrix elements $\mathcal{H}'_{ij}$ coupling members of the NDS vanish, then we must go to 2nd order. Generally speaking, the first order terms will be much larger than the 2nd order terms, provided that there is no symmetry reason for the first order terms to vanish.

Let us explain this further. By the matrix element $\mathcal{H}'_{12}$ we mean $\langle \psi_1^0 | \mathcal{H}' | \psi_2^0 \rangle$. Suppose the perturbation Hamiltonian $\mathcal{H}'$ under consideration is due to an electric field $\vec{E}$

:::{math}
:label: eq-apptransport-A-40
\mathcal{H}' = -e\vec{r}\cdot\vec{E}
:::

where $e\vec{r}$ is the dipole moment of our system. If now we consider the effect of inversion on $\mathcal{H}'$, we see that $\vec{r}$ changes sign under inversion $(x,y,z) \to (-x,-y,-z)$, i.e., $\vec{r}$ is an odd function. Suppose that we are considering the energy levels of the hydrogen atom in the presence of an electric field. We have $s$ states (even), $p$ states (odd), $d$ states (even), etc. The electric dipole moment will only couple an even state to an odd state because of the oddness of the dipole moment under inversion. Hence there is no effect in 1st order non-degenerate perturbation theory for situations where the first order matrix element vanishes. For the $n = 1$ level, there is, however, an effect due to the electric field in second order so that the correction to the energy level goes as the square of the electric field, i.e., $|\vec{E}|^2$. For the $n = 2$ levels, we treat them in degenerate perturbation theory because the $2s$ and $2p$ states are degenerate in the simple treatment of the hydrogen atom. Here, first order terms only appear in entries coupling $s$ and $p$ states. To get corrections which split the $p$ levels among themselves, we must go to 2nd order degenerate perturbation theory.
