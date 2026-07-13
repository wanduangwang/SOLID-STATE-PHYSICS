---
title: "1 Review of Topics in Angular Momentum"
abstract: "Review of angular momentum fundamentals in quantum mechanics for application to magnetism topics: operator definitions and commutation relations, raising/lowering operators, eigenvalues and matrix representations, spherical harmonics in coordinate representation, orbital and spin angular momentum and magnetic moments, spin-orbit coupling, LS coupling scheme, vector model and Lande g-factor."
---

# 1 Review of Topics in Angular Momentum

## 1.1 Introduction

In this chapter we review some topics in quantum mechanics that we will apply to our discussion of magnetism. The major topic under discussion here is angular momentum.

### 1.1.1 Angular Momentum, Definitions and Commutation Relations

In classical mechanics, as in quantum mechanics, angular momentum is defined by

:::{math}
:label: eq-p3-ch01-1
\vec{L} = \vec{r} \times \vec{p} .
:::

Since the position operator $\vec{r}$ and momentum operator $\vec{p}$ do not commute, the components of the angular momentum do not commute. We note first that the position and momentum operators do not commute:

:::{math}
:label: eq-p3-ch01-2
(xp_x - p_x x)f(\vec{r}) = \frac{\hbar}{i} x \frac{\partial}{\partial x} f(\vec{r}) - \frac{\hbar}{i} \frac{\partial}{\partial x}[x f(\vec{r})] = i\hbar f(\vec{r}) .
:::

The result of Eq. {eq}`eq-p3-ch01-2` is conveniently written in terms of the commutator defined by $[r_j, p_k] \equiv r_j p_k - p_k r_j$ using the relation

:::{math}
:label: eq-p3-ch01-3
[r_j, p_k] = i\hbar \delta_{jk} ,
:::

where $\delta_{jk}$ is a delta function having the value unity if $j = k$, and zero otherwise. Equation {eq}`eq-p3-ch01-3` says that different components of $\vec{r}$ and $\vec{p}$ commute, and it is only the same components of $\vec{r}$ and $\vec{p}$ that fail to commute. If we now apply these commutation relations to the angular momentum we get:

:::{math}
:label: eq-p3-ch01-4
[L_x, L_y] = L_x L_y - L_y L_x = (yp_z - zp_y)(zpx - xp_z) - (zp_x - xp_z)(yp_z - zp_y)
= -i\hbar yp_x + i\hbar xp_y = i\hbar L_z .
:::

Similarly, the commutation relations for the other components are:

:::{math}
:label: eq-p3-ch01-5
[L_y, L_z] = i\hbar L_x \qquad [L_z, L_x] = i\hbar L_y .
:::

The commutation relations in Eqs. {eq}`eq-p3-ch01-4` and {eq}`eq-p3-ch01-5` are conveniently summarized in the symbolic statement

:::{math}
:label: eq-p3-ch01-6
\vec{L} \times \vec{L} = i\hbar \vec{L} .
:::

These commutation relations are basic to the properties of the angular momentum in quantum mechanics.

Since no two components of the angular momentum commute, it is not possible to find a representation that simultaneously diagonalizes more than one component of $\vec{L}$. That is, there is no wavefunction that is both an eigenfunction of $L_x$ and $L_y$, for if there were, we could then write

:::{math}
:label: eq-p3-ch01-7
L_x \Psi = \ell_x \Psi
:::

and

:::{math}
:label: eq-p3-ch01-8
L_y \Psi = \ell_y \Psi .
:::

Equations {eq}`eq-p3-ch01-7` and {eq}`eq-p3-ch01-8` would then imply that

:::{math}
:label: eq-p3-ch01-9
L_x L_y \Psi = L_x \ell_y \Psi = \ell_x \ell_y \Psi
:::

and also

:::{math}
:label: eq-p3-ch01-10
L_y L_x \Psi = \ell_y \ell_x \Psi
:::

so that if $L_x$ and $L_y$ could be diagonalized simultaneously, then $L_x$ and $L_y$ would have to commute. However, we know that they do not commute; therefore, they cannot be simultaneously diagonalized.

On the other hand, all three components of angular momentum, $L_x$, $L_y$, and $L_z$ commute with $L^2$ where

:::{math}
:label: eq-p3-ch01-11
L^2 = L_x^2 + L_y^2 + L_z^2 .
:::

For example

:::{math}
:label: eq-p3-ch01-12
[L_z, L^2] = L_z L_x^2 - L_x^2 L_z + L_z L_y^2 - L_y^2 L_z
= L_x L_z L_x + i\hbar L_y L_x - L_x L_z L_x + i\hbar L_x L_y
+ L_y L_z L_y - i\hbar L_x L_y - L_y L_z L_y - i\hbar L_y L_x = 0
:::

and similarly for $[L_x, L^2] = 0$ and $[L_y, L^2] = 0$. Since $L_x$, $L_y$ and $L_z$ do not commute with each other, it is convenient to select one component (e.g., $L_z$) as the component that is simultaneously diagonalized with $L^2$.

It is convenient to introduce raising and lowering operators

:::{math}
:label: eq-p3-ch01-13
L_{\pm} = L_x \pm i L_y
:::

so that we can write

:::{math}
:label: eq-p3-ch01-14
L^2 = L_z^2 + \frac{1}{2}(L_+ L_- + L_- L_+) .
:::

From Eq. {eq}`eq-p3-ch01-13` we know that $L_+$ and $L_-$ are non-hermitian operators, because $L_x$ and $L_y$ are both Hermitian operators and have real eigenvalues. Since $L_x$ and $L_y$ individually commute with $L^2$, we have the commutation relations:

:::{math}
:label: eq-p3-ch01-15
[L^2, L_+] = 0 \qquad \text{and} \qquad [L^2, L_-] = 0 .
:::

Furthermore, $L_+$ does not commute with $L_z$ but rather

:::{math}
:label: eq-p3-ch01-16
[L_z, L_+] = [L_z, (L_x + iL_y)] = i\hbar(L_y - iL_x) = \hbar L_+
:::

and likewise

:::{math}
:label: eq-p3-ch01-17
[L_z, L_-] = -\hbar L_- .
:::

By the same procedure we obtain

:::{math}
:label: eq-p3-ch01-18
[L_+, L_-] = [(L_x + iL_y), (L_x - iL_y)] = 2\hbar L_z
:::

and

:::{math}
:label: eq-p3-ch01-19
L_x = \frac{1}{2}(L_+ + L_-) \qquad L_y = -\frac{i}{2}(L_+ - L_-) .
:::

### 1.1.2 Angular momentum Eigenvalues

We will now use the commutation relations in §1.1.1 to find the eigenvalues of the angular momentum matrices. Let us choose as our representation, one that diagonalizes both $L_z$ and $L^2$ and we will use quantum numbers $m$ and $\ell$ to designate the representation. For example, if $\Psi$ is an eigenfunction of $L_z$ we can write

:::{math}
:label: eq-p3-ch01-20
L_z \Psi = m\hbar \Psi
:::

where the eigenvalue of $L_z$ is $m\hbar$. From Eq. {eq}`eq-p3-ch01-20` we can then write the matrix element of $L_z$ in the $|m\ell\rangle$ representation as

:::{math}
:label: eq-p3-ch01-21
\langle m\ell | L_z | m\ell \rangle = m\hbar
:::

where $m$ is a dimensionless real integer denoting the magnitude of $L_z$, while $\ell$ is the maximum value of $m$ and $\hbar$ has the dimension of angular momentum. Physically, we can think of $m$ as telling how many units of angular momentum there are along the $z$ direction. Since $L_z$ has only diagonal matrix elements, the above relation can be written more generally as

:::{math}
:label: eq-p3-ch01-22
\langle m'\ell' | L_z | m\ell \rangle = m\hbar \delta_{mm'} \delta_{\ell\ell'} .
:::

We will now compute the matrix elements of $L_+$, $L_-$, and $L^2$ in the $|m\ell\rangle$ representation.

From the commutation relation

:::{math}
:label: eq-p3-ch01-23
[L^2, L_+] = 0
:::

we obtain

:::{math}
:label: eq-p3-ch01-24
\langle m'\ell' | L^2 L_+ - L_+ L^2 | m''\ell'' \rangle = 0
:::

for all $|m\ell\rangle$ states. But $L^2$ is diagonal in the $|m\ell\rangle$ representation by hypothesis and therefore is specified by some function of $\ell$, the quantum number associated with $L^2$. We thus obtain

:::{math}
:label: eq-p3-ch01-25
L^2 |m''\ell''\rangle = (L^2)_{\ell''} |m''\ell''\rangle
:::

where we have written the eigenvalue of the operator $L^2$ using the notation $(L^2)_{\ell''}$. We will now show that

:::{math}
:label: eq-p3-ch01-26
(L^2)_{\ell''} = \hbar^2 \ell''(\ell'' + 1) .
:::

From Eqs. {eq}`eq-p3-ch01-24` and {eq}`eq-p3-ch01-25` we write

:::{math}
:label: eq-p3-ch01-27
[(L^2)_{\ell'} - (L^2)_{\ell''}] \langle m'\ell' | L_+ | m''\ell'' \rangle = 0 .
:::

For Eq. {eq}`eq-p3-ch01-27` to be satisfied, we see that the matrix elements of $L_+$ must vanish unless $\ell' = \ell''$ which implies that $L_+$ must be diagonal in $\ell$.

The commutation relation $[L_z, L_+] = \hbar L_+$ given by Eq. {eq}`eq-p3-ch01-16` then yields

:::{math}
:label: eq-p3-ch01-28
\langle m'\ell | L_z L_+ - L_+ L_z | m''\ell \rangle = \hbar \langle m'\ell | L_+ | m''\ell \rangle
:::

Now exploiting the eigenvalue relation in Eq. {eq}`eq-p3-ch01-22`, $L_z |m''\ell\rangle = m''\hbar |m''\ell\rangle$ we get:

:::{math}
:label: eq-p3-ch01-29
(m' - m'')\hbar \langle m'\ell | L_+ | m''\ell \rangle = \hbar \langle m'\ell | L_+ | m''\ell \rangle
:::

so that $(m' - m'' - 1)\hbar \langle m'\ell | L_+ | m''\ell \rangle = 0$ which is conveniently expressed as

:::{math}
:label: eq-p3-ch01-30
\hbar \langle m'\ell' | L_+ | m''\ell'' \rangle = \delta_{\ell'\ell''} \delta_{m',m''+1} \lambda_{m'} \hbar
:::

where $\lambda_{m'}$ is a dimensionless number. Thus, not only are the matrix elements of $L_+$ in the $|m\ell\rangle$ representation diagonal in $\ell$, but they are non-vanishing only on off-diagonal positions of $m$ (that is where the index of $m'$ exceeds the index $m''$ by unity). The matrix element for $L_+$ furthermore implies the matrix element of $L_-$ since these matrix elements are related by the Hermitian transpose

:::{math}
:label: eq-p3-ch01-31
\langle m'\ell' | L_- | m''\ell'' \rangle = \delta_{\ell'\ell''} \delta_{m',m''-1} \lambda_{m'}^* \hbar .
:::

We can evaluate $\lambda_{m'}$ explicitly by using the commutation relation $[L_+, L_-] = 2\hbar L_z$ from Eq. {eq}`eq-p3-ch01-18`, so that in taking matrix elements of $[L_+, L_-]$, we need only consider wholly diagonal matrix elements of

:::{math}
:label: eq-p3-ch01-32
\langle m\ell | [L_+, L_-] | m\ell \rangle = 2\hbar m\hbar = 2m\hbar^2
:::

because $L_z$ is diagonal in both $m$ and $\ell$. Since the matrix element of a product of two operators $O_1$ and $O_2$ in general can be written as

:::{math}
:label: eq-p3-ch01-33
\langle n | O_1 O_2 | n' \rangle = \sum_{n''} \langle n | O_1 | n'' \rangle \langle n'' | O_2 | n' \rangle
:::

Eq. {eq}`eq-p3-ch01-32` implies a sum over all possible $m''$ and $\ell''$ values. But since $L_+$ is diagonal in $\ell$ and has only one non-vanishing matrix element in $m$, then Eq. {eq}`eq-p3-ch01-32` only has the terms

:::{math}
:label: eq-p3-ch01-34
\langle m\ell | L_+ | m-1, \ell \rangle \langle m-1, \ell | L_- | m, \ell \rangle
- \langle m, \ell | L_- | m+1, \ell \rangle \langle m+1, \ell | L_+ | m, \ell \rangle
= |\lambda_{m-1}|^2 \hbar^2 - |\lambda_m|^2 \hbar^2 = 2m\hbar^2
:::

which has a solution

:::{math}
:label: eq-p3-ch01-35
|\lambda_m|^2 = -m(m+1)
:::

so that $-(m-1)m + m(m+1) = 2m$ is satisfied. Clearly we can add any constant $C$ to the solution of Eq. {eq}`eq-p3-ch01-34` and obtain another equally valid solution

:::{math}
:label: eq-p3-ch01-36
|\lambda_m|^2 = C - m(m+1) .
:::

Since $|\lambda_m|^2$ is positive, definite, we require that $C$ be chosen to guarantee that requirement. This means that $m$ must be restricted to the range from $-\ell$ to $+\ell$ and $C = \ell(\ell+1)$ or

:::{math}
:label: eq-p3-ch01-37
|\lambda_m|^2 = \ell(\ell+1) - m(m+1) .
:::

This then means that the raising operator acts on the state $|m, \ell\rangle$ to produce a state $|m+1, \ell\rangle$

:::{math}
:label: eq-p3-ch01-38
L_+ |m, \ell\rangle = \hbar \lambda_{m+1} |m+1, \ell\rangle .
:::

Starting with the lowest state $m = -\ell$, the raising operator $L_+$ produces a physical state until $m = \ell$ is reached at which time $L_+|\ell, \ell\rangle$ produces a non-existent or null state.

With these restrictions on possible values of $m$, we can evaluate the matrix element of $L^2$ in the $m, \ell$ representation:

:::{math}
:label: eq-p3-ch01-39
\langle m, \ell | L^2 | m, \ell \rangle = \langle m, \ell | \frac{1}{2}(L_+ L_- + L_- L_+) + L_z^2 | m, \ell \rangle
= \left[ \frac{1}{2}\bigl(\ell(\ell+1) - (m-1)m\bigr) + \frac{1}{2}\bigl(\ell(\ell+1) - m(m+1)\bigr) + m^2 \right] \hbar^2
= \ell(\ell+1)\hbar^2
:::

and from Eq. {eq}`eq-p3-ch01-38` we can write

:::{math}
:label: eq-p3-ch01-40
\langle m+1, \ell | L_+ | m, \ell \rangle = \hbar |\lambda_m| = \hbar \sqrt{\ell(\ell+1) - m(m+1)} \equiv \hbar \sqrt{(\ell - m)(\ell + m + 1)}
:::

which also implies

:::{math}
:label: eq-p3-ch01-41
\langle m-1, \ell | L_- | m, \ell \rangle = \hbar \sqrt{(\ell + m)(\ell - m + 1)} .
:::

The restrictions on the values of $m$ are thus:

1. The raising operator $L_+$ raises the $m$ index by 1, while the lowering operator $L_-$ lowers $m$ by 1.
2. The difference between the minimum and maximum values of $m$ must be an integer. This condition requires that $\ell$ be either integral or half-integral. Orbital angular momentum always involves integral values of $\ell$ and spin angular momentum may involve either half-integral or integral values of the unit of angular momentum $\hbar$.

In matrix form, the matrix elements of $L_z$ are:

:::{math}
:label: eq-p3-ch01-42
L_z = \begin{pmatrix}
\ell & 0 & 0 & \cdots & 0 \\
0 & \ell-1 & 0 & \cdots & 0 \\
0 & 0 & \ell-2 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & -\ell
\end{pmatrix}
:::

For $L_+$ we have only off-diagonal elements to the right of the diagonal. We will give here some matrix elements for specific values of $\ell$. For half integral spin $s = 1/2$ we have

:::{math}
:label: eq-p3-ch01-43
S_x = \frac{\hbar}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},
\qquad
S_y = \frac{\hbar}{2}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix},
\qquad
S_z = \frac{\hbar}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
:::

and

:::{math}
:label: eq-p3-ch01-44
S_+ = \hbar\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix},
\qquad
S_- = \hbar\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix},
\qquad
S^2 = \frac{3\hbar^2}{4}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
:::

(Note: We use $\ell$ to denote orbital angular momentum where $\ell = \text{integer}$ and we use $s$ when discussing half-integral values of angular momentum.) The four matrices

:::{math}
:label: eq-p3-ch01-45
\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},\qquad
\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},\qquad
\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix},\qquad
\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
:::

span the vector space and can be used to expand any arbitrary $(2\times 2)$ matrix. Similarly, we can write the matrices for $\ell = 1$ as

:::{math}
:label: eq-p3-ch01-46
L_x = \frac{\hbar}{\sqrt{2}}\begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}
:::

:::{math}
:label: eq-p3-ch01-47
L_y = \frac{\hbar}{\sqrt{2}}\begin{pmatrix} 0 & -i & 0 \\ i & 0 & -i \\ 0 & i & 0 \end{pmatrix}
:::

:::{math}
:label: eq-p3-ch01-48
L_z = \hbar\begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{pmatrix}
:::

:::{math}
:label: eq-p3-ch01-49
L_+ = \hbar\begin{pmatrix} 0 & \sqrt{2} & 0 \\ 0 & 0 & \sqrt{2} \\ 0 & 0 & 0 \end{pmatrix}
:::

:::{math}
:label: eq-p3-ch01-50
L_- = \hbar\begin{pmatrix} 0 & 0 & 0 \\ \sqrt{2} & 0 & 0 \\ 0 & \sqrt{2} & 0 \end{pmatrix}
:::

:::{math}
:label: eq-p3-ch01-51
L^2 = 2\hbar^2\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} .
:::

## 1.2 Angular Momentum in Wave Mechanics

:::{figure} images/fig-p3-ch01-1.png
:name: fig-p3-ch01-1
:width: 60%
:align: center
Fig. 1.1: Cartesian and polar coordinate system used in wave mechanics.
:::

The matrix element expressions

:::{math}
:label: eq-p3-ch01-52
\langle m\ell | L^2 | m'\ell' \rangle = \delta_{\ell\ell'} \delta_{mm'} \, \ell(\ell+1)\hbar^2 ,
:::

:::{math}
:label: eq-p3-ch01-53
\langle m\ell | L_z | m'\ell' \rangle = \delta_{\ell\ell'} \delta_{mm'} \, m\hbar ,
:::

:::{math}
:label: eq-p3-ch01-54
\langle m\ell | L_+ | m'\ell' \rangle = \delta_{\ell\ell'} \delta_{m,m'+1} \, \sqrt{(\ell - m')(\ell + m' + 1)} ,
:::

and

:::{math}
:label: eq-p3-ch01-55
\langle m\ell | L_- | m'\ell' \rangle = \delta_{\ell\ell'} \delta_{m,m'-1} \, \sqrt{(\ell + m')(\ell - m' + 1)}
:::

allow us to write explicit matrices for the angular momentum operators for all $\ell$ values.

By definition

:::{math}
:label: eq-p3-ch01-56
L_x = yp_z - zp_y = \frac{\hbar}{i}\left[ y\left(\frac{\partial}{\partial z}\right) - z\left(\frac{\partial}{\partial y}\right) \right]
:::

:::{math}
:label: eq-p3-ch01-57
L_y = zp_x - xp_z = \frac{\hbar}{i}\left[ z\left(\frac{\partial}{\partial x}\right) - x\left(\frac{\partial}{\partial z}\right) \right]
:::

:::{math}
:label: eq-p3-ch01-58
L_z = xp_y - yp_x = \frac{\hbar}{i}\left[ x\left(\frac{\partial}{\partial y}\right) - y\left(\frac{\partial}{\partial x}\right) \right]
:::

Using polar coordinates shown in Fig. {numref}`fig-p3-ch01-1`, we can write

:::{math}
:label: eq-p3-ch01-59
x = r\cos\phi\sin\theta \qquad y = r\sin\phi\sin\theta \qquad z = r\cos\theta .
:::

In spherical coordinates, the components of the angular momentum become

:::{math}
:label: eq-p3-ch01-60
L_x = i\hbar\left[ \sin\phi\left(\frac{\partial}{\partial\theta}\right) + \cot\theta\cos\phi\left(\frac{\partial}{\partial\phi}\right) \right]
:::

:::{math}
:label: eq-p3-ch01-61
L_y = i\hbar\left[ -\cos\phi\left(\frac{\partial}{\partial\theta}\right) + \cot\theta\sin\phi\left(\frac{\partial}{\partial\phi}\right) \right]
:::

:::{math}
:label: eq-p3-ch01-62
L_z = \frac{\hbar}{i}\left(\frac{\partial}{\partial\phi}\right)
:::

and

:::{math}
:label: eq-p3-ch01-63
L^2 = L_x^2 + L_y^2 + L_z^2 = -\hbar^2\left[ \frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\left(\frac{\partial^2}{\partial\phi^2}\right) \right] .
:::

In wave mechanics, the eigenfunctions of $L_z$ and $L^2$ are the spherical harmonics $Y_{\ell m}(\theta, \phi)$:

:::{math}
:label: eq-p3-ch01-64
L^2 Y_{\ell m}(\theta, \phi) = \ell(\ell+1)\hbar^2 Y_{\ell m}(\theta, \phi)
:::

and

:::{math}
:label: eq-p3-ch01-65
L_z Y_{\ell m}(\theta, \phi) = m\hbar Y_{\ell m}(\theta, \phi)
:::

where the spherical harmonics are explicitly given by

:::{math}
:label: eq-p3-ch01-66
Y_{\ell m}(\theta, \phi) = \left[ \frac{(2\ell+1)}{4\pi} \frac{(\ell-|m|)!}{(\ell+|m|)!} \right]^{1/2} P_\ell^m(\cos\theta) e^{im\phi}
:::

in which the associated Legendre functions $P_\ell^m(\cos\theta)$ are

:::{math}
:label: eq-p3-ch01-67
P_\ell^m(w) = (1 - w^2)^{|m|/2} \frac{d^{|m|} P_\ell(w)}{dw^{|m|}}
:::

where $w = \cos\theta$ and the Legendre functions are found from the generating functions

:::{math}
:label: eq-p3-ch01-68
\sum_{\ell=0}^{\infty} P_\ell(w) s^\ell = \frac{1}{\sqrt{1 - 2sw + s^2}} \qquad \text{for } s < 1 .
:::

From Eq. {eq}`eq-p3-ch01-68` it follows that

:::{math}
:label: eq-p3-ch01-69
P_0(w) = 1 \qquad P_1(w) = w = \cos\theta \qquad P_2(w) = \frac{1}{2}(3w^2 - 1) = \frac{1}{2}(3\cos^2\theta - 1) .
:::

Thus, the first few spherical harmonics are:

:::{math}
:label: eq-p3-ch01-70
Y_{0,0} = \sqrt{\frac{1}{4\pi}}
:::

:::{math}
:label: eq-p3-ch01-71
Y_{1,1} = \sqrt{\frac{3}{8\pi}} \sin\theta \, e^{i\phi}
:::

:::{math}
:label: eq-p3-ch01-72
Y_{1,0} = \sqrt{\frac{3}{4\pi}} \cos\theta
:::

:::{math}
:label: eq-p3-ch01-73
Y_{1,-1} = \sqrt{\frac{3}{8\pi}} \sin\theta \, e^{-i\phi} .
:::

The matrix elements of angular momentum can also be calculated from the point of view of wave mechanics. In that case we must perform the angular integrations which define the matrix element for an operator $\mathcal{O}$:

:::{math}
:label: eq-p3-ch01-74
\int_0^\pi d\phi \int_0^{2\pi} \sin\theta \, d\theta \, Y_{\ell m}^*(\theta, \phi) \, \mathcal{O} \, Y_{\ell' m'}(\theta, \phi) \equiv \langle \ell m | \mathcal{O} | \ell' m' \rangle .
:::

In general, the matrix mechanics approach to angular momentum is the easier technique for the evaluation of matrix elements. For example we have from Eq. {eq}`eq-p3-ch01-54` the result for the raising operator

:::{math}
:label: eq-p3-ch01-75
L_+ Y_{\ell m}(\theta, \phi) = \sqrt{(\ell - m)(\ell + m + 1)} \; \hbar Y_{\ell, m+1}(\theta, \phi) .
:::

## 1.3 Magnetic Moment and Orbital Angular Momentum

In this section we show that there is a magnetic moment $\vec{\mu}$ associated with the orbital angular momentum $\vec{L}$ given by

:::{math}
:label: eq-p3-ch01-76
\vec{\mu} = \left( \frac{e}{2mc} \right) \vec{L}
:::

where $e = -4.8\times 10^{-10}$ esu $= -1.6\times 10^{-19}$ Coulombs of charge. It is for this reason that a discussion of the magnetic properties of solids requires knowledge of the quantum mechanical properties of the angular momentum.

There are various derivations of the result given by Eq. {eq}`eq-p3-ch01-76` which follows from classical electromagnetic theory. By definition, the magnetic moment associated with a charge distribution $\rho_{\text{charge}}(\vec{r}, t)$ is: (see Jackson, pp 181)

:::{math}
:label: eq-p3-ch01-77
\vec{\mu} \equiv \frac{1}{2c} \int d^3r \, \rho_{\text{charge}}(\vec{r} \times \vec{v}) .
:::

The factor $(\vec{r} \times \vec{v})$ in the above definition suggests that $\vec{\mu}$ is related to the orbital angular momentum $\vec{L}$ which is defined for a mass distribution $\rho_{\text{mass}}(\vec{r}, t)$ as

:::{math}
:label: eq-p3-ch01-78
\vec{L} = \int d^3r \, \rho_{\text{mass}} (\vec{r} \times \vec{v}) .
:::

For simple systems, the mass and charge densities are proportional:

:::{math}
:label: eq-p3-ch01-79
\rho_{\text{mass}}/m = \rho_{\text{charge}}/q = \frac{1}{\text{Volume}}
:::

where $m$ is in units of mass and $q$ is in units of charge for the electron. Therefore we can write for a simple electron system

:::{math}
:label: eq-p3-ch01-80
\vec{\mu} = \left( \frac{q}{2mc} \right) \vec{L} = \left( \frac{e}{2mc} \right) \vec{L} .
:::

See Eisberg Ch. 11 for another derivation of this result.

It is usually convenient to introduce a special symbol for the magnetic moment of an electron, namely the Bohr magneton $\mu_B$ which is defined as

:::{math}
:label: eq-p3-ch01-81
\mu_B \equiv e\hbar/2mc = -0.927 \times 10^{-20} \; \text{erg/gauss}
:::

and $\mu_B$ is a negative number since $e$ is negative. Thus

:::{math}
:label: eq-p3-ch01-82
\vec{\mu} = \frac{\mu_B \vec{L}}{\hbar} = \frac{g_\ell \mu_B \vec{L}}{\hbar}
:::

where we note that the angular momentum is measured in units of $\hbar$. Equation {eq}`eq-p3-ch01-82` defines the $g$–factor as it relates $\vec{\mu}$ and the angular momentum and we note that the $g$–factor for orbital motion is $g_\ell = 1$. Remember that since $\mu_B$ is a negative number for electrons, the magnetic moment of the electron is directed antiparallel to the orbital angular momentum.

## 1.4 Spin Angular Momentum

The existence of spin angular momentum is based on several experimental observations:

1. The Stern–Gerlach atomic beam experiment shows that there could be an even number of possible $m$ values

:::{math}
:label: eq-p3-ch01-83
m = -\ell, -\ell+1, -\ell+2, \cdots, \ell
:::

which implies that $\ell$ can have a half-integral value.

2. The observation that associated with the spin angular momentum is a magnetic moment

:::{math}
:label: eq-p3-ch01-84
\vec{\mu} = g_s \mu_B \vec{S}/\hbar
:::

where $\vec{\mu}$ and $\vec{S}$ are oppositely directed. However in Eq. {eq}`eq-p3-ch01-84` the $g_s$ value for the spin is not unity but is very nearly $g_s = 2$. For spectroscopy, the Lamb shift correction is needed whereby $g_s = 2.0023$. Electron spin resonance experiments typically yield $g$-values to 5 or more significant figures.

3. There is evidence for spin in atomic spectra.

Like the orbital angular momentum, the spin angular momentum obeys the commutation relations

:::{math}
:label: eq-p3-ch01-85
\vec{S} \times \vec{S} = i\hbar \vec{S}
:::

and consequently we have the matrix elements of the spin operators in the $|s, m_s\rangle$ representation:

:::{math}
:label: eq-p3-ch01-86
\langle m_s' s' | S^2 | m_s s \rangle = \hbar^2 s(s+1) \, \delta_{s,s'} \, \delta_{m_s, m_s'}
:::

:::{math}
:label: eq-p3-ch01-87
\langle m_s' s' | S_z | m_s s \rangle = \hbar m_s \delta_{s,s'} \delta_{m_s, m_s'}
:::

:::{math}
:label: eq-p3-ch01-88
\langle m_s' s' | S_+ | m_s s \rangle = \hbar \sqrt{(s - m_s)(s + m_s + 1)} \; \delta_{s,s'} \delta_{m_s+1, m_s'}
:::

:::{math}
:label: eq-p3-ch01-89
\langle m_s' s' | S_- | m_s s \rangle = \hbar \sqrt{(s + m_s)(s - m_s + 1)} \; \delta_{s,s'} \delta_{m_s-1, m_s'} .
:::

A single electron has a spin angular momentum $S_z = \hbar/2$ so that there are two possible $m_s$ values, namely $m_s = \pm 1/2$ and also $s(s+1) = (1/2)(3/2) = 3/4$.

## 1.5 The Spin-Orbit Interaction

An electron in an atomic state having orbital angular momentum $\vec{L}$ and spin angular momentum $\vec{S}$ can have its spin angular momentum coupled to the orbital angular momentum through the so-called spin-orbit interaction. The physical basis for this interaction is as follows. Because of the orbital motion of the electrons, a magnetic field $\vec{H}$ is created. Now this magnetic field acts on the magnetic moment associated with the electron spin and attempts to line up the moment along the magnetic field giving an interaction energy

:::{math}
:label: eq-p3-ch01-90
\mathcal{H}_{s-o}' = -\vec{\mu} \cdot \vec{H} .
:::

We will give here a simple classical argument for the magnitude of the spin-orbit interaction and refer you to Eisberg Ch. 11 for a more complete derivation.

Since we wish to focus our attention on the electron and the magnetic field it sees, we choose a coordination system attached to the electron. In this coordinate system, the nucleus is moving, thereby generating at the position of the electron both an electric field $\vec{E} = e\vec{r}/r^3$ and a magnetic field $\vec{H} = -(\vec{v}/c) \times \vec{E}$. We thus find the interaction energy

:::{math}
:label: eq-p3-ch01-91
\mathcal{H}_{s-o}' = -\vec{\mu} \cdot \vec{H}
= -\left[ -\frac{|e|}{mc}\vec{S} \right] \cdot \left[ -\frac{\vec{v}}{c} \times \vec{E} \right] .
:::

In a solid, we replace $\vec{E} = \vec{\nabla}V(r)/|e|$ where $V(r)$ is the Coulomb potential energy in the solid; in an atomic system, $V(r)$ becomes $U(r)$ and $\vec{\nabla}U(r)$ becomes $f(r)\vec{r}$ where $f(r)$ is a scalar function. We thus obtain for atomic systems

:::{math}
:label: eq-p3-ch01-92
\mathcal{H}_{s-o}' = \frac{f(r)}{mc^2}[\vec{S} \cdot (\vec{r} \times \vec{v})] = \frac{f(r)}{m^2 c^2}(\vec{L} \cdot \vec{S}) .
:::

For the special case of a simple Coulomb potential $U(r) = -e^2/r$,

:::{math}
:label: eq-p3-ch01-93
\vec{\nabla}U = (e^2/r^3)\vec{r}
:::

or

:::{math}
:label: eq-p3-ch01-94
f(r) = e^2/r^3
:::

and

:::{math}
:label: eq-p3-ch01-95
\mathcal{H}_{s-o}' = \frac{e^2}{(m^2 c^2 r^3)} \vec{S} \cdot \vec{L} .
:::

The more correct derivation given in Eisberg shows that

:::{math}
:label: eq-p3-ch01-96
\mathcal{H}_{s-o}' = \frac{e^2}{(2m^2 c^2 r^3)} \vec{S} \cdot \vec{L}
:::

where the factor of 2 inserted in Eq. {eq}`eq-p3-ch01-96` is due to relativistic corrections. For more general atomic systems the spin-orbit interaction is written as

:::{math}
:label: eq-p3-ch01-97
\mathcal{H}_{s-o}' = \xi(r) \vec{S} \cdot \vec{L}
:::

and for solids where no central force approximation is made, we then have

:::{math}
:label: eq-p3-ch01-98
\mathcal{H}_{s-o}' = \frac{1}{2m^2 c^2}[\vec{\nabla}V \times \vec{p}] \cdot \vec{S}
:::

where $V(\vec{r})$ is the periodic potential in the solid.

### 1.5.1 Solution of Schrödinger's Equation for Free Atoms

We will now study the effect of the spin-orbit interaction on atomic spectra.

The one-electron atomic problem in a central force Coulomb field is written as the Schrödinger equation

:::{math}
:label: eq-p3-ch01-99
\left[ \frac{p^2}{2m} + U(r) \right] \Psi = E\Psi
:::

(without spin) or in wave mechanics (spherical coordinates) Eq. {eq}`eq-p3-ch01-99` becomes

:::{math}
:label: eq-p3-ch01-100
-\frac{\hbar^2}{2m}\left[ \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) + \frac{1}{r^2\sin^2\theta}\left(\frac{\partial^2}{\partial\phi^2}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) \right]\Psi + U(r)\Psi = E\Psi .
:::

It is clear that if the potential is spherically symmetric, the separation of variables leads to an eigenvalue problem in $L^2$, or writing

:::{math}
:label: eq-p3-ch01-101
\Psi(r, \theta, \phi) = R(r) \, Y_{\ell m}(\theta, \phi)
:::

we get for the radial equation

:::{math}
:label: eq-p3-ch01-102
\left\{ \frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{d}{dr}\right) + \left[ -\frac{\ell(\ell+1)}{r^2} + \frac{2m}{\hbar^2}\bigl(E - U(r)\bigr) \right] \right\} R(r) = 0
:::

where $m$ is the mass and the angular equation is written in terms of the spherical harmonics $Y_{\ell m}(\theta, \phi)$. Thus each atomic state is (without spin) characterized by a principal quantum number $n$ and a quantum number $\ell$ denoting the orbital angular momentum states. By inspection of the differential equation (Eq. {eq}`eq-p3-ch01-102`), the quantum number $m$ does not enter so that every solution to a one-electron atomic problem must be $(2\ell+1)$-fold degenerate or degenerate in the quantum number $m$. We can also understand this result physically. For a spherically symmetric system there is no preferred direction. Thus, there can be no difference in energy arising from the component of $\vec{L}$ taken along any particular direction.

:::{figure} images/fig-p3-ch01-2.png
:name: fig-p3-ch01-2
:width: 70%
:align: center
Fig. 1.2: Energy levels in the Bohr atom and the Schrödinger solution showing the orbital degeneracy.
:::

The solutions for $\ell = 0$ of the atomic problem where $U(r) = -e^2/r$ gives the Bohr energy levels for the hydrogen atom

:::{math}
:label: eq-p3-ch01-103
E_n = -\frac{me^4}{2\hbar^2 n^2} \qquad n = 1, 2, 3, 4, \ldots .
:::

Since the angular momentum term in the radial equation $-\ell(\ell+1)/r^2$ has the opposite sign from the potential term $-U(\vec{r})$, higher $\ell$ states will lie higher in energy. A physical way to see this is to think of the angular momentum as giving rise to an increase in kinetic energy and hence less binding. For a general attractive potential $U(\vec{r})$ the classification of the atomic levels is as shown in Fig. {numref}`fig-p3-ch01-2`.

We have reviewed this background in order to show that the spin-orbit interaction

:::{math}
:label: eq-p3-ch01-104
\mathcal{H}_{s-o}' = \xi(r) \vec{L} \cdot \vec{S}
:::

serves to lift certain degeneracies. To calculate the effect of the spin-orbit interaction we introduce the total angular momentum $\vec{J}$ which is defined by

:::{math}
:label: eq-p3-ch01-105
\vec{J} \equiv \vec{L} + \vec{S} .
:::

If no torques are acting on the atomic system, then the total angular momentum is conserved and the magnitude of $\vec{J}$ (or $J^2$) is a constant of the motion. We can thus find for atomic systems where $U = U(\vec{r})$ various constants of the motion:

1. the energy $E$ giving rise to the principal quantum number $n$
2. the magnitude of $L^2$ giving rise to quantum number $\ell$
3. the $z$ component (or any other single component) of $\vec{L}$ giving rise to quantum number $m_\ell$. The energy levels do not depend on $m_\ell$.
4. the magnitude of $S^2$ giving rise to quantum number $s$. In the absence of the spin-orbit interaction the energy levels do not depend on the spin.

Since no preferred direction in space is introduced by the spin-orbit interaction, each level is $(2\ell+1)(2s+1)$-fold degenerate.

At this point it is profitable to point out the difference between the various possible representations, which will be denoted here by their quantum numbers:

1. no spin: $n$, $\ell$, $m_\ell$
2. with spin but no spin-orbit interaction: $n$, $\ell$, $s$, $m_\ell$, $m_s$

Here each atomic level is $(2s+1)(2\ell+1)$-fold degenerate but since $s = 1/2$ we have each level $2(2\ell+1)$-fold degenerate. Having specified $m_\ell$ and $m_s$, then $m_j$ is determined by the relation:

:::{math}
:label: eq-p3-ch01-106
m_j = m_\ell + m_s
:::

which follows from the vector relation $\vec{J} = \vec{L} + \vec{S}$ taken along the $z$ direction of quantization. Having specified $\ell$ gives two possible values for $j$

:::{math}
:label: eq-p3-ch01-107
j = \ell + s = \ell + \frac{1}{2}
:::

or

:::{math}
:label: eq-p3-ch01-108
j = \ell - s = \ell - \frac{1}{2} .
:::

Now let us count up the degeneracy from the point of view of the $j$-values: $m_j$ can have $(2j+1)$ values for $j = \ell + 1/2$ or $(2\ell+1) + 1$ values and $m_j$ can have $(2j+1)$ values for $j = \ell - 1/2$ or $(2\ell-1) + 1$. Therefore the total number of states is $[2\ell+2] + [2\ell] = 4\ell+2 = 2(2\ell+1)$ so that the degeneracy of the states is the same whether we count states in the $|n, \ell, s, m_\ell, m_s\rangle$ representation or in the $|n, \ell, s, j, m_j\rangle$ representation.

Although (without spin-orbit interaction) the energy is the same for the two representations, the states are not the same. Suppose we take $m_\ell = 1$ and $m_s = -1/2$ to give $m_j = 1/2$. This does not tell us which $j, m_j$ state we have: that is we can have either $j = 3/2$ or $j = 1/2$, for in either case $m_j = 1/2$ is an acceptable quantum number. Thus to go from the $(m_\ell, m_s)$ representation to the $(j, m_j)$ representation we must make linear combinations of states. That is, the $(m_\ell, m_s)$ combination $(1, -1/2)$ contributes to both the $(j, m_j)$ states $(3/2, 1/2)$ and $(1/2, 1/2)$.

If we now introduce the spin-orbit interaction, then not only are the states that contribute to $(j, m_j)$ different but a splitting is introduced into the energy of the states, depending of the value of $j$. That is, the energy for the $j = 1/2$ levels (2-fold degenerate) will be different than that for the $j = 3/2$ levels (4-fold degenerate). The fact that this splitting occurs in this way is a consequence of symmetry (group theory) and has nothing to do with whether $\mathcal{H}_{s-o}'$ is small or large, or whether we use perturbation theory or not.

To show that this splitting does occur we will evaluate $\vec{L} \cdot \vec{S}$ in the $j, m_j$ representation (remembering that $\ell$ and $s$ are still “good” quantum numbers). We note that if we consider

:::{math}
:label: eq-p3-ch01-109
\vec{J} = \vec{L} + \vec{S}
:::

and square Eq. {eq}`eq-p3-ch01-109`, we obtain the following operator equation:

:::{math}
:label: eq-p3-ch01-110
J^2 = (\vec{L} + \vec{S}) \cdot (\vec{L} + \vec{S}) = L^2 + S^2 + 2\vec{L} \cdot \vec{S}
:::

since $\vec{L}$ and $\vec{S}$ commute. The spin and orbital angular momenta commute because they operate in different vector spaces. Thus we obtain

:::{math}
:label: eq-p3-ch01-111
\vec{L} \cdot \vec{S} = \frac{1}{2}(J^2 - L^2 - S^2) .
:::

If we now take the diagonal matrix element, we get:

:::{math}
:label: eq-p3-ch01-112
\langle jm_j | \vec{L} \cdot \vec{S} | jm_j \rangle = \frac{1}{2}\langle jm_j | J^2 - L^2 - S^2 | jm_j \rangle
= \frac{\hbar^2}{2}\bigl[j(j+1) - \ell(\ell+1) - s(s+1)\bigr] .
:::

If we consider, for example, the case of $\ell = 1$, $s = 1/2$, we get

:::{math}
:label: eq-p3-ch01-113
\langle jm_j | \vec{L} \cdot \vec{S} | jm_j \rangle = \hbar^2/2 \quad \text{for } j = 3/2
:::

and

:::{math}
:label: eq-p3-ch01-114
\langle jm_j | \vec{L} \cdot \vec{S} | jm_j \rangle = -\hbar^2 \quad \text{for } j = 1/2 .
:::

Thus, the spin-orbit interaction lifts the degeneracy of the atomic states (see Fig. {numref}`fig-p3-ch01-3`), though the center of gravity is maintained. The magnitude of the splitting depends on the matrix element of $\xi(r)$ between states with principal quantum number $n$.

:::{figure} images/fig-p3-ch01-3.png
:name: fig-p3-ch01-3
:width: 55%
:align: center
Fig. 1.3: Schematic of the spin-orbit splitting of the $p$-state, $\ell = 1$.
:::

Similarly, if we have $\ell = 2$ and $s = 1/2$ we will find a splitting into a $j = 5/2$ and a $j = 3/2$ state; the center of gravity of the levels will be maintained. If we should have $s = 1$ (as might occur in a multi-electron atom) and $\ell = 1$, then we can make states with $j = 2, 1, 0$. In this case, the spin-orbit interaction will produce a splitting into three levels of degeneracies 5, 3 and 1 to yield a total of nine states which is the number we started with $(2\ell+1)(2s+1) = 9$.

We would now like to consider the magnetic moment of an electron in an atom (see §1.3), taking into account the contribution from both the orbital and spin angular momenta. Of particular interest here is the fact that although the $g$-factor for the orbital contribution is $g_\ell = 1$, that for the spin contribution is $g_s = 2$. What this means is that the magnetic moment $\vec{\mu} = (e/2mc)(\vec{L} + 2\vec{S})$ due to both the orbital and spin contributions is not directed along the total angular momentum $\vec{J}$. As a consequence, we cannot simultaneously diagonalize the magnetic moment operator $\vec{\mu}$ and the total angular momentum $\vec{J}$. We will now discuss two ways to calculate matrix elements of $\vec{\mu}$. The first is called the vector model for angular momentum which gives the diagonal matrix elements, while the second is the Clebsch–Gordan coefficients, which gives both diagonal and off-diagonal matrix elements.

## 1.6 Vector Model for Angular Momentum

In this section we develop a method to find the expectation value of an operator which is itself a function of angular momentum operators, but cannot be directly diagonalized. The magnetic moment operator is an example of such an operator.

Because of the coupling between the orbital and spin angular momentum, the components $L_z$ and $S_z$ have no definite values. The spin-orbit interaction takes a state specified by the quantum numbers $\ell$ and $s$, and splits it into levels according to their $j$ values. So if we have $\ell = 1$ and $s = 1/2$ in the absence of the spin-orbit interaction, then we get a $j = 3/2$ level and a $j = 1/2$ level when the spin-orbit interaction is considered. For the $j = 3/2$ level we have the four states $m_j = 3/2, 1/2, -1/2, -3/2$ and for the $j = 1/2$ level we have the two states $m_j = 1/2$ and $-1/2$. Since the $m_j = 1/2$ state can arise from either an $m_\ell = 1$ and $m_s = -1/2$ state or an $m_\ell = 0$ and $m_s = 1/2$ state, the specifications of $m_\ell$ and $m_s$ do not uniquely specify the energy, or to say it another way, the state with quantum numbers $|\ell, s, m_\ell, m_s\rangle = |1, 1/2, 1, -1/2\rangle$ has no definite energy. On the other hand, the state $|\ell, s, j, m_j\rangle$ does have a definite energy and is thus an eigenstate of the energy while $|\ell, s, m_\ell, m_s\rangle$ is not an eigenstate in the presence of the spin-orbit interaction.

The various angular momenta are often represented in terms of a vector diagram as shown in Fig. {numref}`fig-p3-ch01-4`. Since there are no external torques acting on the system, the total angular momentum $\vec{J}$ is a constant of the motion. In the absence of any external perturbation on the free atom, we are free to choose the $z$ direction however we wish. If, however, a magnetic field is present, there is a preferred direction in space and the $z$ direction is conventionally taken along the direction of the external magnetic field. The projection of $\vec{J}$ on the $z$ axis, $J_z$, can be diagonalized along with the total Hamiltonian so that we can represent $\vec{J}$ on the diagram above by a definite vector with respect to the $z$ axis. The length of the vector $|\vec{J}|$ is $\hbar\sqrt{j(j+1)}$ and its projection $J_z$ on the diagram in Fig. {numref}`fig-p3-ch01-4` is $(3/2)\hbar$. (Actually for $j = 5/2$ we could have selected five other projections $m_j = 5/2, 1/2, -1/2, -3/2, -5/2$.) Thus the angle between $\vec{J}$ and $J_z$ in Fig. {numref}`fig-p3-ch01-4` is given by

:::{figure} images/fig-p3-ch01-4.png
:name: fig-p3-ch01-4
:width: 55%
:align: center
Fig. 1.4: This vector diagram for the angular momentum was constructed for: $\ell = 2$, $s = 1/2$, $j = 5/2$, $m_j = 3/2$ and shows that the total angular momentum $\vec{J}$ precesses around the $z$–axis. On the other hand, the angular momenta $\vec{S}$ and $\vec{L}$ precess around $\vec{J}$.
:::

:::{math}
:label: eq-p3-ch01-115
\cos\theta = \frac{J_z}{|J|} = \frac{3/2}{\sqrt{(5/2)(7/2)}} = \frac{3}{\sqrt{35}} .
:::

Now the magnitudes of the vectors $\vec{L}$ and $\vec{S}$ are fixed at

:::{math}
:label: eq-p3-ch01-116
|\vec{L}| = \hbar\sqrt{\ell(\ell+1)} = \hbar\sqrt{6}
:::

and

:::{math}
:label: eq-p3-ch01-117
|\vec{S}| = \hbar\sqrt{s(s+1)} = \frac{\hbar}{2}\sqrt{3} .
:::

However, the direction of these vectors in space is not fixed and this fact is illustrated in Fig. {numref}`fig-p3-ch01-4` as a freedom of precession of the vectors $\vec{L}$ and $\vec{S}$ about $\vec{J}$ such that only their lengths are fixed. We note that $\vec{L}$ and $\vec{S}$ have equal probabilities of being in any particular direction along the precessional path and consequently a projection of $\vec{L}$ or $\vec{S}$ on the $z$ axis would give different values depending on the position along this precessional path. For this reason $L_z$ and $S_z$ do not yield good quantum numbers.

From the diagram, we see that the projections of $\vec{L}$ and $\vec{S}$ on $\vec{J}$ have definite values. Thus, the vector diagram tells us that if we want to find the expectation value of the orbital angular momentum $\vec{L}$ along any direction in space, we project $\vec{L}$ on $\vec{J}$ and then project the resulting vector on the special direction of quantization $z$. Thus to calculate the expectation value of $L_z$ we find using the vector model:

:::{math}
:label: eq-p3-ch01-118
\langle \ell, s, j, m_j | L_z | \ell, s, j, m_j \rangle
= \langle \ell, s, j, m_j | \frac{\vec{L} \cdot \vec{J}}{|J|^2}(J_z) | \ell, s, j, m_j \rangle .
:::

In the $|\ell, s, j, m_j\rangle$ representation, we can readily calculate the diagonal matrix elements of $J_z$ and $J^2$

:::{math}
:label: eq-p3-ch01-119
\langle \ell, s, j, m_j | J_z | \ell, s, j, m_j \rangle = \hbar m_j
:::

:::{math}
:label: eq-p3-ch01-120
\langle \ell, s, j, m_j | J^2 | \ell, s, j, m_j \rangle = \hbar^2 j(j+1) .
:::

To find $\langle \ell, s, j, m_j | \vec{L} \cdot \vec{J} | \ell, s, j, m_j \rangle$ we observe that

:::{math}
:label: eq-p3-ch01-121
\vec{S} = \vec{J} - \vec{L} \qquad \text{and} \qquad S^2 = J^2 + L^2 - 2\vec{L} \cdot \vec{J}
:::

so that

:::{math}
:label: eq-p3-ch01-122
\langle \ell, s, j, m_j | \vec{L} \cdot \vec{J} | \ell, s, j, m_j \rangle
= \langle \ell, s, j, m_j | \frac{1}{2}(J^2 + L^2 - S^2) | \ell, s, j, m_j \rangle
= \frac{\hbar^2}{2}\bigl[j(j+1) + \ell(\ell+1) - s(s+1)\bigr]
:::

so for $\ell = 2$, $s = 1/2$, $j = 5/2$, $m_j = 3/2$ we get upon substitution into Eq. {eq}`eq-p3-ch01-122`

:::{math}
:label: eq-p3-ch01-123
\langle \ell, s, j, m_j | \frac{\vec{L} \cdot \vec{J}}{J^2}(J_z) | \ell, s, j, m_j \rangle = \hbar\frac{6}{5} .
:::

The vector model is of great importance in considering the expectation value of vectors which are functions of the angular momentum. Thus the magnetic moment operator $\vec{\mu}_{\text{total}}$ is

:::{math}
:label: eq-p3-ch01-124
\vec{\mu}_{\text{total}} = \frac{\mu_B}{\hbar}(g_\ell \vec{L} + g_s \vec{S}) = \frac{\mu_B}{\hbar}(\vec{L} + 2\vec{S})
:::

and the magnetic moment is directed along the vector $\vec{L} + 2\vec{S}$. This magnetic moment vector is not along $\vec{J}$ and therefore has no definite value when projected on an arbitrary direction in space such as the $z$–axis. On the other hand, the projection of $\vec{\mu}_{\text{total}}$ on $\vec{J}$ has a definite value. It is convenient to write Eq. {eq}`eq-p3-ch01-124` as

:::{math}
:label: eq-p3-ch01-125
\vec{\mu}_{\text{total}} = \frac{\mu_B}{\hbar}(g\vec{J})
:::

so that the energy of an electron in a magnetic field $\vec{B}$ is

:::{math}
:label: eq-p3-ch01-126
E = -\vec{\mu}_{\text{total}} \cdot \vec{B} = -\mu_B (B g m_j)
:::

where the Landé $g$–factor $g$ represents the projection of $\vec{\mu}_{\text{total}}$ on $\vec{J}$ so that

:::{math}
:label: eq-p3-ch01-127
g = \langle \ell, s, j, m_j | \frac{(\vec{L} + 2\vec{S}) \cdot \vec{J}}{J^2} | \ell, s, j, m_j \rangle .
:::

To evaluate $g$ we note that

:::{math}
:label: eq-p3-ch01-128
(\vec{L} + 2\vec{S}) \cdot \vec{J} = (\vec{L} + 2\vec{S}) \cdot (\vec{L} + \vec{S}) = L^2 + 3\vec{L} \cdot \vec{S} + 2S^2
:::

but

:::{math}
:label: eq-p3-ch01-129
\vec{J} = \vec{L} + \vec{S}
:::

and

:::{math}
:label: eq-p3-ch01-130
J^2 = (\vec{L} + \vec{S})^2 = L^2 + S^2 + 2\vec{L} \cdot \vec{S}
:::

:::{figure} images/fig-p3-ch01-5.png
:name: fig-p3-ch01-5
:width: 55%
:align: center
Fig. 1.5: The vector model for the magnetic moment operator $\vec{\mu}$. Here we see that $\vec{J}$ precesses around $z$ but $J_z$ is fixed. $\vec{S}$ precesses around $\vec{J}$ and the projection of $\vec{S}$ on $\vec{J}$ is fixed. The projection of $\vec{\mu}$ on $\vec{J}$ is fixed as is the projection of $(\vec{\mu} \cdot \vec{J})\vec{J}$ on the $z$ axis. Thus the vector model provides a prescription for finding the expectation value of the magnetic moment operator $\vec{\mu}$.
:::

so that

:::{math}
:label: eq-p3-ch01-131
\vec{L} \cdot \vec{S} = \frac{1}{2}(J^2 - L^2 - S^2) .
:::

Thus

:::{math}
:label: eq-p3-ch01-132
(\vec{L} + 2\vec{S}) \cdot \vec{J} = L^2 + \frac{3}{2}(J^2 - L^2 - S^2) + 2S^2
= \frac{3}{2}J^2 - \frac{1}{2}L^2 + \frac{1}{2}S^2 .
:::

We now take diagonal matrix elements of Eq. {eq}`eq-p3-ch01-132` in the $|\ell, s, j, m_j\rangle$ representation and find for the Landé $g$–factor

:::{math}
:label: eq-p3-ch01-133
g = \frac{ \frac{3}{2}j(j+1) + \frac{1}{2}s(s+1) - \frac{1}{2}\ell(\ell+1) }{j(j+1)} .
:::

Thus using the vector model, we have found the diagonal matrix elements of the magnetic moment operator. In §2.4 we will show how to also find the off–diagonal matrix elements of the angular momentum operator using the Clebsch–Gordan coefficients and using raising and lowering operators.

## 1.7 Summary

- Angular momentum operator definition $\vec{L} = \vec{r} \times \vec{p}$ and commutation relations $[L_i, L_j] = i\hbar \epsilon_{ijk} L_k$ ({eq}`eq-p3-ch01-1`–{eq}`eq-p3-ch01-6`) form the foundation of quantum mechanical angular momentum theory.
- $L^2$ and $L_z$ can be simultaneously measured; their eigenvalues are $\ell(\ell+1)\hbar^2$ and $m\hbar$ respectively; raising/lowering operators $L_\pm$ change $m$ by $\pm 1$ ({eq}`eq-p3-ch01-20`–{eq}`eq-p3-ch01-41`).
- Eigenfunctions of $L^2$, $L_z$ in spherical coordinates are spherical harmonics $Y_{\ell m}$ ({eq}`eq-p3-ch01-64`–{eq}`eq-p3-ch01-73`).
- Orbital magnetic moment $\vec{\mu} = (e/2mc)\vec{L}$; Bohr magneton $\mu_B = e\hbar/2mc$ ({eq}`eq-p3-ch01-76`, {eq}`eq-p3-ch01-81`); orbital $g$-factor $g_\ell = 1$.
- Spin obeys identical angular momentum algebra, but electron spin has $g_s \approx 2$ ({eq}`eq-p3-ch01-84`, {eq}`eq-p3-ch01-85`).
- Spin-orbit coupling $\mathcal{H}_{s-o}' = \xi(r)\,\vec{L}\cdot\vec{S}$ splits total angular momentum $\vec{J}=\vec{L}+\vec{S}$ into levels labeled by $j$ while preserving center of gravity ({eq}`eq-p3-ch01-104`–{eq}`eq-p3-ch01-114`).
- Vector model gives projections of $\vec{L}$, $\vec{S}$ onto $\vec{J}$, yielding the Lande $g$-factor ({eq}`eq-p3-ch01-124`–{eq}`eq-p3-ch01-133`).

## References

- Sakurai, *Modern Quantum Mechanics*, Chapter 3.
- Schiff, *Quantum Mechanics*, Chapter 7.
- Shankar, *Principles of Quantum Mechanics*, Chapter 12.
- Jackson, *Classical Electrodynamics*, 2nd Ed., Chapter 5.
