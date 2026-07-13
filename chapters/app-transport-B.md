---
title: "Appendix B — 1D Graphite: Carbon Nanotubes"
abstract: "Using the tight-binding approximation we derive the pi and pi-star bands of two-dimensional graphite, the geometry of carbon nanotubes (chiral and translation vectors), and the one-dimensional bands and density-of-states van Hove singularities obtained by zone-folding."
---

# Appendix B — 1D Graphite: Carbon Nanotubes

## B.0 Overview of this Appendix

This appendix shows how the tight-binding approximation (Sec. B.1.1) yields the electronic structure of carbon nanotubes (seamless cylinders rolled from a single graphite sheet), including the bands of two-dimensional graphite (Eq. {eq}`eq-apptransport-B-6`, {eq}`eq-apptransport-B-8`), nanotube geometry (Eq. {eq}`eq-apptransport-B-9` to {eq}`eq-apptransport-B-19`), the zone-folded one-dimensional bands (Eq. {eq}`eq-apptransport-B-20`), and the metallic/semiconducting criterion together with the density of states (Eq. {eq}`eq-apptransport-B-22` to {eq}`eq-apptransport-B-25`).

## B.1 Structure of 2D graphite

Graphite is a three-dimensional (3D) layered hexagonal lattice of carbon atoms. A single layer of graphite forms a two-dimensional (2D) material, called 2D graphite or a graphene layer. Even in 3D graphite, the interaction between two adjacent layers is very small compared with intra-layer interactions, and the electronic structure of 2D graphite is a first approximation of that for 3D graphite.

In Fig. {numref}`fig-apptransport-B-1` we show (a) the unit cell and (b) the Brillouin zone of two-dimensional graphite as a dotted rhombus and shaded hexagon, respectively, where $\vec{a}_1$ and $\vec{a}_2$ are unit vectors in real space, and $\vec{b}_1$ and $\vec{b}_2$ are reciprocal lattice vectors. In the $x,y$ coordinates shown in Fig. {numref}`fig-apptransport-B-1`, the real space unit vectors $\vec{a}_1$ and $\vec{a}_2$ of the hexagonal lattice are expressed as

:::{math}
:label: eq-apptransport-B-1
\vec{a}_1 = \left(\frac{\sqrt{3}}{2}a, \frac{a}{2}\right), \quad
\vec{a}_2 = \left(\frac{\sqrt{3}}{2}a, -\frac{a}{2}\right),
:::

where $a = |\vec{a}_1| = |\vec{a}_2| = 1.42 \times \sqrt{3} = 2.46\,\text{\AA}$ is the lattice constant of two-dimensional graphite. Correspondingly the unit vectors $\vec{b}_1$ and $\vec{b}_2$ of the reciprocal lattice are given by

:::{math}
:label: eq-apptransport-B-2
\vec{b}_1 = \left(\frac{2\pi}{\sqrt{3}a}, \frac{2\pi}{a}\right), \quad
\vec{b}_2 = \left(\frac{2\pi}{\sqrt{3}a}, -\frac{2\pi}{a}\right),
:::

corresponding to a lattice constant of $4\pi/\sqrt{3}a$ in reciprocal space.

:::{figure} images/fig-apptransport-B-1.png
:name: fig-apptransport-B-1
:width: 80%
:align: center
Fig. B.1: (a) The unit cell and (b) Brillouin zone of two-dimensional graphite are shown as the dotted rhombus and shaded hexagon, respectively. $\vec{a}_i$ and $\vec{b}_i$ ($i=1,2$) are unit vectors and reciprocal lattice vectors, respectively. Energy dispersion relations are obtained along the perimeter of the dotted triangle connecting the high symmetry points, $\Gamma$, $K$ and $M$.
:::

Three $\sigma$ bonds for 2D graphite hybridize in a $sp^2$ configuration, while the other $2p_z$ orbital, which is perpendicular to the graphene plane, makes $\pi$ covalent bonds. In Sect. {ref}`sec-apptransport-B-tight-binding` we consider only the $\pi$ energy bands for 2D graphite, because we know that the $\pi$ energy bands are covalent and are the most important for determining the solid state properties of 2D graphite.

(sec-apptransport-B-tight-binding)=
### B.1.1 Tight Binding approximation for the π Bands of Two-Dimensional Graphite

Two Bloch functions, constructed from atomic orbitals for the two inequivalent carbon atoms at A and B in Fig. {numref}`fig-apptransport-B-1`, provide the basis functions for 2D graphite. When we consider only nearest-neighbor interactions, then there is only an integration over a single atom in the diagonal matrix elements $\mathcal{H}_{AA}$ and $\mathcal{H}_{BB}$, as is shown in Eq. 1.81 and thus $\mathcal{H}_{AA} = \mathcal{H}_{BB} = \epsilon_{2p}$. For the off-diagonal matrix element $\mathcal{H}_{AB}$, we must consider the three nearest-neighbor B atoms relative to an A atom, which are denoted by the vectors $\vec{R}_1, \vec{R}_2$, and $\vec{R}_3$. We then consider the contribution to Eq. 1.82 from $\vec{R}_1, \vec{R}_2$, and $\vec{R}_3$ as follows:

:::{math}
:label: eq-apptransport-B-3
\begin{aligned}
\mathcal{H}_{AB} &= t\left(e^{i\vec{k}\cdot\vec{R}_1} + e^{i\vec{k}\cdot\vec{R}_2} + e^{i\vec{k}\cdot\vec{R}_3}\right) \\
&= tf(k)
\end{aligned}
:::

where $t$ is given by Eq. 1.83[^1] and $f(k)$ is a function of the sum of the phase factors of $e^{i\vec{k}\cdot\vec{R}_j}$ ($j = 1, \cdots, 3$). Using the $x,y$ coordinates of Fig. {numref}`fig-apptransport-B-1`(a), $f(k)$ is given by

:::{math}
:label: eq-apptransport-B-4
f(k) = e^{ik_x a/\sqrt{3}} + 2e^{-ik_x a/2\sqrt{3}}\cos\left(\frac{k_y a}{2}\right).
:::

[^1]: We often use the symbol $\gamma_0 = |t|$ for the nearest neighbor transfer integral.

Since $f(k)$ is a complex function, and the Hamiltonian forms a Hermitian matrix, we write $\mathcal{H}_{BA} = \mathcal{H}_{AB}^*$ in which $*$ denotes the complex conjugate. Using Eq. {eq}`eq-apptransport-B-4`, the overlap integral matrix is given by $\mathcal{S}_{AA} = \mathcal{S}_{BB} = 1$, and $\mathcal{S}_{AB} = sf(k) = \mathcal{S}_{BA}^*$. Here $s$ has the same definition as in Eq. 1.84, so that the explicit forms for $\mathcal{H}$ and $\mathcal{S}$ can be written as

:::{math}
:label: eq-apptransport-B-5
\mathcal{H} = \begin{pmatrix} \epsilon_{2p} & tf(k) \\ tf(k)^* & \epsilon_{2p} \end{pmatrix},
\quad
\mathcal{S} = \begin{pmatrix} 1 & sf(k) \\ sf(k)^* & 1 \end{pmatrix}.
:::

By solving the secular equation $\det(\mathcal{H} - E\mathcal{S}) = 0$ and using $\mathcal{H}$ and $\mathcal{S}$ as given in Eq. {eq}`eq-apptransport-B-5`, the eigenvalues $E(\vec{k})$ are obtained as a function $w(\vec{k})$, $k_x$ and $k_y$:

:::{math}
:label: eq-apptransport-B-6
E_{g2D}(\vec{k}) = \frac{\epsilon_{2p} \pm tw(\vec{k})}{1 \pm sw(\vec{k})},
:::

where the $+$ signs in the numerator and denominator go together giving the bonding $\pi$ energy band, and likewise for the $-$ signs, which give the anti-bonding $\pi^*$ band, while the function $w(\vec{k})$ is given by

:::{math}
:label: eq-apptransport-B-7
w(\vec{k}) = \sqrt{|f(\vec{k})|^2}
= \sqrt{1 + 4\cos\frac{\sqrt{3}k_x a}{2}\cos\frac{k_y a}{2} + 4\cos^2\frac{k_y a}{2}}.
:::

:::{figure} images/fig-apptransport-B-2.png
:name: fig-apptransport-B-2
:width: 75%
:align: center
Fig. B.2: The energy dispersion relations for 2D graphite are shown throughout the whole region of the Brillouin zone. Here we use the parameters $\epsilon_{2p}=0$, $t=-3.033$ eV and $s=0.129$. The inset shows the electronic energy dispersion along the high symmetry directions of the triangle $\Gamma MK$ shown in Fig. B.1(b) (see text).
:::

In Fig. {numref}`fig-apptransport-B-2`, the energy dispersion relations of two-dimensional graphite are shown throughout the 2D Brillouin zone and the inset shows the energy dispersion relations along the high symmetry axes along the perimeter of the triangle shown in Fig. {numref}`fig-apptransport-B-1`(b). The upper half of the energy dispersion curves describes the $\pi^*$-energy anti-bonding band, and the lower half is the $\pi$-energy bonding band. The upper $\pi^*$ band and the lower $\pi$ band are degenerate at the $K$ points through which the Fermi energy passes. Since there are two $\pi$ electrons per unit cell, these two $\pi$ electrons fully occupy the lower $\pi$ band. Since a detailed calculation of the density of states shows that the density of states at the Fermi level is zero, two-dimensional graphite is a zero-gap semiconductor.

When the overlap integral $s$ becomes zero, the $\pi$ and $\pi^*$ bands become symmetrical around $E = \epsilon_{2p}$ which can be understood from Eq. {eq}`eq-apptransport-B-6`. The energy dispersion relations in the case of $s = 0$ are commonly used as a simple approximation for the electronic structure of a graphene layer:

:::{math}
:label: eq-apptransport-B-8
E_{g2D}(k_x, k_y) = \pm t\left\{1 + 4\cos\left(\frac{\sqrt{3}k_x a}{2}\right)\cos\left(\frac{k_y a}{2}\right) + 4\cos^2\left(\frac{k_y a}{2}\right)\right\}^{1/2}.
:::

The simple approximation given by Eq. {eq}`eq-apptransport-B-8` is used next to obtain a simple approximation for the electronic dispersion relations for carbon nanotubes, and provides an excellent first approximation for the analysis of presently available experiments on carbon nanotubes.

## B.2 Single Wall Carbon Nanotubes

In §B.2 we briefly review the structure of single wall carbon nanotubes and relate this structure to the 2D graphene sheet discussed in §B.1, while §B.3.1 gives the electronic structure of the single wall carbon nanotube, as obtained from the tight binding approximation and from $E(k)$ for the graphene sheet, given by Eq. {eq}`eq-apptransport-B-8`.

### B.2.1 Structure

A single-wall carbon nanotube can be described as a graphene sheet rolled into a cylindrical shape so that the structure is one-dimensional with axial symmetry, and in general exhibits a spiral conformation, called *chirality*. The chirality, as defined in this appendix, is given by a single vector called the chiral vector. To specify the structure of carbon nanotubes, we define several important vectors, which are derived from the chiral vector.

**Chiral Vector: $\mathbf{C}_h$**

The structure of a single-wall carbon nanotube (see Fig. {numref}`fig-apptransport-B-3`) is specified by the vector ($\overrightarrow{OA}$ in Fig. {numref}`fig-apptransport-B-4`) which corresponds to a section of the nanotube perpendicular to the nanotube axis (hereafter we call this section the equator of the nanotube). In Fig. {numref}`fig-apptransport-B-4`, the unrolled honeycomb lattice of the nanotube is shown, in which $\overrightarrow{OB}$ is the direction of the nanotube axis, and the direction of $\overrightarrow{OA}$ corresponds to the equator. By considering the crystallographically equivalent sites $O, A, B$, and $B'$, and by rolling the honeycomb sheet so that points $O$ and $A$ coincide (and points $B$ and $B'$ coincide), a paper model of a carbon nanotube can be constructed. The vectors $\overrightarrow{OA}$ and $\overrightarrow{OB}$ define the chiral vector $\mathbf{C}_h$ and the translational vector $\mathbf{T}$ of a carbon nanotube, respectively, as further explained below.

:::{figure} images/fig-apptransport-B-3.png
:name: fig-apptransport-B-3
:width: 80%
:align: center
Fig. B.3: Classification of carbon nanotubes: (a) armchair, (b) zigzag, and (c) chiral nanotubes, showing cross-sections and caps for the 3 basic kinds of nanotubes.
:::

The chiral vector $\mathbf{C}_h$ can be expressed by the real space unit vectors $\mathbf{a}_1$ and $\mathbf{a}_2$ (see Fig. {numref}`fig-apptransport-B-4`) of the hexagonal lattice defined in Eq. {eq}`eq-apptransport-B-1`:

:::{math}
:label: eq-apptransport-B-9
\mathbf{C}_h = n\mathbf{a}_1 + m\mathbf{a}_2 \equiv (n, m), \quad (n,m \text{ are integers},\ 0 \le |m| \le n).
:::

The specific chiral vectors $\mathbf{C}_h$ shown in Fig. {numref}`fig-apptransport-B-3` are, respectively, (a) $(5,5)$, (b) $(9,0)$ and (c) $(10,5)$, and the chiral vector shown in Fig. {numref}`fig-apptransport-B-4` is $(4,2)$. An armchair nanotube corresponds to the case of $n = m$, that is $\mathbf{C}_h = (n,n)$ [see Fig. {numref}`fig-apptransport-B-3`(a)], and a zigzag nanotube corresponds to the case of $m = 0$, or $\mathbf{C}_h = (n,0)$ [see Fig. {numref}`fig-apptransport-B-3`(b)]. All other $(n,m)$ chiral vectors correspond to chiral nanotubes [see Fig. {numref}`fig-apptransport-B-3`(c)]. Because of the hexagonal symmetry of the honeycomb lattice, we need to consider only $0 < |m| < n$ in $\mathbf{C}_h = (n,m)$ for chiral nanotubes.

:::{figure} images/fig-apptransport-B-4.png
:name: fig-apptransport-B-4
:width: 80%
:align: center
Fig. B.4: The unrolled honeycomb lattice of a nanotube, showing the unit vectors $\vec{a}_1$ and $\vec{a}_2$ for the graphene sheet. When we connect sites $O$ and $A$, and $B$ and $B'$, a nanotube can be constructed. $\overrightarrow{OA}$ and $\overrightarrow{OB}$ define the chiral vector $\mathbf{C}_h$ and the translational vector $\mathbf{T}$ of the nanotube, respectively. The rectangle $OAB'B$ defines the unit cell for the nanotube. The figure corresponds to $\mathbf{C}_h=(4,2)$, $d=d_R=2$, $\mathbf{T}=(4,-5)$, $N=28$, $\mathbf{R}=(1,-1)$.
:::

The diameter of the carbon nanotube, $d_t$, is given by $L/\pi$, in which $L$ is the circumferential length of the carbon nanotube:

:::{math}
:label: eq-apptransport-B-10
d_t = L/\pi, \quad L = |\mathbf{C}_h| = \sqrt{\mathbf{C}_h\cdot\mathbf{C}_h} = a\sqrt{n^2 + m^2 + nm}.
:::

It is noted here that $\mathbf{a}_1$ and $\mathbf{a}_2$ are not orthogonal to each other and that the inner products between $\mathbf{a}_1$ and $\mathbf{a}_2$ yield:

:::{math}
:label: eq-apptransport-B-11
\mathbf{a}_1\cdot\mathbf{a}_1 = \mathbf{a}_2\cdot\mathbf{a}_2 = a^2, \quad \mathbf{a}_1\cdot\mathbf{a}_2 = \frac{a^2}{2},
:::

where the lattice constant $a = 1.42\,\text{\AA} \times \sqrt{3} = 2.46\,\text{\AA}$ of the honeycomb lattice is given in Eq. {eq}`eq-apptransport-B-1`.

The chiral angle $\theta$ (see Fig. {numref}`fig-apptransport-B-4`) is defined as the angle between the vectors $\mathbf{C}_h$ and $\mathbf{a}_1$, with values of $\theta$ in the range $0 \le |\theta| \le 30^{\circ}$, because of the hexagonal symmetry of the honeycomb lattice. The chiral angle $\theta$ denotes the tilt angle of the hexagons with respect to the direction of the nanotube axis, and the angle $\theta$ specifies the spiral symmetry. The chiral angle $\theta$ is defined by taking the inner product of $\mathbf{C}_h$ and $\mathbf{a}_1$, to yield an expression for $\cos\theta$:

:::{math}
:label: eq-apptransport-B-12
\cos\theta = \frac{\mathbf{C}_h\cdot\mathbf{a}_1}{|\mathbf{C}_h||\mathbf{a}_1|}
= \frac{2n + m}{2\sqrt{n^2 + m^2 + nm}},
:::

thus relating $\theta$ to the integers $(n,m)$ defined in Eq. {eq}`eq-apptransport-B-9`. In particular, zigzag and armchair nanotubes correspond to $\theta = 0^{\circ}$ and $\theta = 30^{\circ}$, respectively.

### B.2.2 Translational Vector: T

The translation vector $\mathbf{T}$ is defined to be the unit vector of a 1D carbon nanotube. The vector $\mathbf{T}$ is parallel to the nanotube axis and is normal to the chiral vector $\mathbf{C}_h$ in the unrolled honeycomb lattice in Fig. {numref}`fig-apptransport-B-4`. The lattice vector $\mathbf{T}$ shown as $\overrightarrow{OB}$ in Fig. {numref}`fig-apptransport-B-4` can be expressed in terms of the basis vectors $\mathbf{a}_1$ and $\mathbf{a}_2$ as

:::{math}
:label: eq-apptransport-B-13
\mathbf{T} = t_1\mathbf{a}_1 + t_2\mathbf{a}_2 \equiv (t_1, t_2), \quad (\text{where } t_1, t_2 \text{ are integers}).
:::

The translation vector $\mathbf{T}$ corresponds to the first lattice point of the 2D graphene sheet through which the vector $\overrightarrow{OB}$ (normal to the chiral vector $\mathbf{C}_h$) passes. From this fact, it is clear that $t_1$ and $t_2$ do not have a common divisor except for unity. Using $\mathbf{C}_h\cdot\mathbf{T} = 0$ and Eqs. {eq}`eq-apptransport-B-9`, {eq}`eq-apptransport-B-11`, and {eq}`eq-apptransport-B-13`, we obtain expressions for $t_1$ and $t_2$ given by

:::{math}
:label: eq-apptransport-B-14
t_1 = \frac{2m + n}{d_R}, \quad t_2 = -\frac{2n + m}{d_R},
:::

where $d_R$ is the greatest common divisor (gcd) of $(2m+n)$ and $(2n+m)$. Also, by introducing $d$ as the greatest common divisor of $n$ and $m$, then $d_R$ can be related to $d$ by[^2]

:::{math}
:label: eq-apptransport-B-15
d_R = \begin{cases} d & \text{if } n-m \text{ is not a multiple of } 3d \\ 3d & \text{if } n-m \text{ is a multiple of } 3d. \end{cases}
:::

[^2]: This relation is obtained by repeated use of the fact that when two integers, $\alpha$ and $\beta$ ($\alpha > \beta$), have a common divisor, $\gamma$, then $\gamma$ is also the common divisor of $(\alpha-\beta)$ and $\beta$ (Euclid's law). When we denote the greatest common divisor as $\gamma = \gcd(\alpha,\beta)$, we get $d_R = \gcd(2m+n, 2n+m) = \gcd(2m+n, n-m) = \gcd(3m, n-m) = \gcd(3d, n-m)$, which gives Eq. {eq}`eq-apptransport-B-15`.

The length of the translation vector, $T$, is given by

:::{math}
:label: eq-apptransport-B-16
T = |\mathbf{T}| = \sqrt{3}L/d_R,
:::

where the circumferential nanotube length $L$ is given by Eq. {eq}`eq-apptransport-B-10`. We note that the length $T$ is greatly reduced when $(n,m)$ have a common divisor or when $(n-m)$ is a multiple of $3d$. In fact, for the $\mathbf{C}_h = (5,5)$ armchair nanotube, we have $d_R = 3d = 15$, $\mathbf{T} = (1,-1)$ [Fig. {numref}`fig-apptransport-B-3`(a)], while for the $\mathbf{C}_h = (9,0)$ zigzag nanotube we have $d_R = d = 9$, and $\mathbf{T} = (1,-2)$ [Fig. {numref}`fig-apptransport-B-3`(b)].

The unit cell of the 1D carbon nanotube is the rectangle $OAB'B$ defined by the vectors $\mathbf{C}_h$ and $\mathbf{T}$ (see Fig. {numref}`fig-apptransport-B-4`), while the unit vectors $\mathbf{a}_1$ and $\mathbf{a}_2$ define the area of the unit cell of 2D graphite. When the area of the nanotube unit cell $|\mathbf{C}_h \times \mathbf{T}|$ (where the symbol $\times$ denotes the vector product operator) is divided by the area of a hexagon ($|\mathbf{a}_1 \times \mathbf{a}_2|$), the number of hexagons per unit cell $N$ is obtained as a function of $n$ and $m$ in Eq. {eq}`eq-apptransport-B-9` as

:::{math}
:label: eq-apptransport-B-17
N = \frac{|\mathbf{C}_h \times \mathbf{T}|}{|\mathbf{a}_1 \times \mathbf{a}_2|}
= \frac{2(m^2 + n^2 + nm)}{d_R}
= \frac{2L^2}{a^2 d_R},
:::

where $L$ and $d_R$ are given by Eqs. {eq}`eq-apptransport-B-10` and {eq}`eq-apptransport-B-15`, respectively, and we note that each hexagon contains two carbon atoms. Thus there are $2N$ carbon atoms (or $2p_z$ orbitals) in each unit cell of the carbon nanotube.

**Unit Cells and Brillouin Zones**

The unit cell for a carbon nanotube in real space is given by the rectangle generated by the chiral vector $\mathbf{C}_h$ and the translational vector $\mathbf{T}$, as is shown in $OAB'B$ in Fig. {numref}`fig-apptransport-B-4`. Since there are $2N$ carbon atoms in this unit cell, we will have $N$ pairs of bonding $\pi$ and anti-bonding $\pi^*$ electronic energy bands. Similarly the phonon dispersion relations will consist of $6N$ branches resulting from a vector displacement of each carbon atom in the unit cell.

Expressions for the reciprocal lattice vectors $\mathbf{K}_2$ along the nanotube axis and $\mathbf{K}_1$ in the circumferential direction[^3] are obtained from the relation $\mathbf{R}_i\cdot\mathbf{K}_j = 2\pi\delta_{ij}$, where $\mathbf{R}_i$ and $\mathbf{K}_j$ are, respectively, the lattice vectors in real and reciprocal space. Then, using Eqs. {eq}`eq-apptransport-B-14`, {eq}`eq-apptransport-B-17`, and the relations

:::{math}
:label: eq-apptransport-B-18
\mathbf{C}_h\cdot\mathbf{K}_1 = 2\pi, \qquad \mathbf{T}\cdot\mathbf{K}_1 = 0, \\
\mathbf{C}_h\cdot\mathbf{K}_2 = 0, \qquad \mathbf{T}\cdot\mathbf{K}_2 = 2\pi,
:::

we get expressions for $\mathbf{K}_1$ and $\mathbf{K}_2$:

:::{math}
:label: eq-apptransport-B-19
\mathbf{K}_1 = \frac{1}{N}(-t_2\mathbf{b}_1 + t_1\mathbf{b}_2), \quad
\mathbf{K}_2 = \frac{1}{N}(m\mathbf{b}_1 - n\mathbf{b}_2),
:::

where $\mathbf{b}_1$ and $\mathbf{b}_2$ are the reciprocal lattice vectors of two-dimensional graphite given by Eq. {eq}`eq-apptransport-B-2`.

[^3]: Since nanotubes are one-dimensional materials, only $\mathbf{K}_2$ is a reciprocal lattice vector. $\mathbf{K}_1$ gives discrete $k$ values in the direction of $\mathbf{C}_h$.

:::{figure} images/fig-apptransport-B-5.png
:name: fig-apptransport-B-5
:width: 80%
:align: center
Fig. B.5: The Brillouin zone of a carbon nanotube is represented by the line segment $WW'$ which is parallel to $\mathbf{K}_2$. The vectors $\mathbf{K}_1$ and $\mathbf{K}_2$ are reciprocal lattice vectors corresponding to $\mathbf{C}_h$ and $\mathbf{T}$, respectively. The figure corresponds to $\mathbf{C}_h=(4,2)$, $\mathbf{T}=(4,-5)$, $N=28$, $\mathbf{K}_1=(5\mathbf{b}_1+4\mathbf{b}_2)/28$, $\mathbf{K}_2=(4\mathbf{b}_1-2\mathbf{b}_2)/28$ (see text).
:::

In Fig. {numref}`fig-apptransport-B-5`, we show the reciprocal lattice vectors, $\mathbf{K}_1$ and $\mathbf{K}_2$, for a $\mathbf{C}_h = (4,2)$ chiral nanotube. The first Brillouin zone of this one-dimensional material is the line segment $WW'$. Since $N\mathbf{K}_1 = -t_2\mathbf{b}_1 + t_1\mathbf{b}_2$ corresponds to a reciprocal lattice vector of two-dimensional graphite, two wave vectors which differ by $N\mathbf{K}_1$ are equivalent. Since $t_1$ and $t_2$ do not have a common divisor except for unity (see Sect. B.2.2), none of the $N-1$ vectors $\mu\mathbf{K}_1$ (where $\mu = 1, \cdots, N-1$) are reciprocal lattice vectors of two-dimensional graphite. Thus the $N$ wave vectors $\mu\mathbf{K}_1$ ($\mu = 0, \cdots, N-1$) give rise to $N$ discrete $k$ vectors, as indicated by the $N = 28$ parallel line segments in Fig. {numref}`fig-apptransport-B-5`, which arise from the quantized wave vectors associated with the periodic boundary conditions on $\mathbf{C}_h$. The length of all the parallel lines in Fig. {numref}`fig-apptransport-B-5` is $2\pi/T$ which is the length of the one-dimensional first Brillouin zone. For the $N$ discrete values of the $k$ vectors, $N$ one-dimensional energy bands will appear. Because of the translational symmetry of $\mathbf{T}$, we have continuous wave vectors in the direction of $\mathbf{K}_2$ for a carbon nanotube of infinite length. However, for a nanotube of finite length $L_t$, the spacing between wave vectors is $2\pi/L_t$.

## B.3 Electronic Structure of Single-Wall Nanotubes

### B.3.1 Zone-Folding of Energy Dispersion Relations

The electronic structure of a single-wall nanotube can be obtained simply from that of two-dimensional graphite. By using periodic boundary conditions in the circumferential direction denoted by the chiral vector $\mathbf{C}_h$, the wave vector associated with the $\mathbf{C}_h$ direction becomes quantized, while the wave vector associated with the direction of the translational vector $\mathbf{T}$ (or along the nanotube axis) remains continuous for a nanotube of infinite length. Thus the energy bands consist of a set of one-dimensional energy dispersion relations which are cross sections of those for two-dimensional graphite (see Fig. {numref}`fig-apptransport-B-2`).

When the energy dispersion relations of two-dimensional graphite, $E_{g2D}(\mathbf{k})$ [see Eqs. {eq}`eq-apptransport-B-6` and/or {eq}`eq-apptransport-B-8`] at line segments shifted from $WW'$ by $\mu\mathbf{K}_1$ ($\mu = 0, \cdots, N-1$) are folded so that the wave vectors parallel to $\mathbf{K}_2$ coincide with $WW'$ as shown in Fig. {numref}`fig-apptransport-B-5`, $N$ pairs of 1D energy dispersion relations $E_\mu(k)$ are obtained, where $N$ is given by Eq. {eq}`eq-apptransport-B-17`. These 1D energy dispersion relations are given by

:::{math}
:label: eq-apptransport-B-20
E_\mu(k) = E_{g2D}\left(k\frac{\mathbf{K}_2}{|\mathbf{K}_2|} + \mu\mathbf{K}_1\right),
\quad (\mu = 0, \cdots, N-1, \text{ and } -\frac{\pi}{T} < k < \frac{\pi}{T}),
:::

corresponding to the energy dispersion relations of a single-wall carbon nanotube. The $N$ pairs of energy dispersion curves given by Eq. {eq}`eq-apptransport-B-20` correspond to the cross sections of the two-dimensional energy dispersion surface shown in Fig. {numref}`fig-apptransport-B-2`, where cuts are made on the lines of $k\mathbf{K}_2/|\mathbf{K}_2| + \mu\mathbf{K}_1$. If for a particular $(n,m)$ nanotube, the cutting line passes through a $K$ point of the 2D Brillouin zone (Fig. {numref}`fig-apptransport-B-1`), where the $\pi$ and $\pi^*$ energy bands of two-dimensional graphite are degenerate by symmetry, the one-dimensional energy bands have a zero energy gap. In this case, the density of states at the Fermi level has a finite value for these carbon nanotubes, and they therefore are metallic. If, however, the cutting line does not pass through a $K$ point, then the carbon nanotube is expected to show semiconducting behavior, with a finite energy gap between the valence and conduction bands.

:::{figure} images/fig-apptransport-B-6.png
:name: fig-apptransport-B-6
:width: 70%
:align: center
Fig. B.6: The condition for metallic energy bands: if the ratio of the length of the vector $\overrightarrow{YK}$ to that of $\mathbf{K}_1$ is an integer, metallic energy bands are obtained.
:::

The condition for obtaining a metallic energy band is that the ratio of the length of the vector $\overrightarrow{YK}$ to that of $\mathbf{K}_1$ in Fig. {numref}`fig-apptransport-B-6` is an integer.[^4] Since the vector $\overrightarrow{YK}$ is given by

:::{math}
:label: eq-apptransport-B-21
\overrightarrow{YK} = \frac{2n + m}{3}\mathbf{K}_1,
:::

the condition for metallic nanotubes is that $(2n+m)$ or equivalently $(n-m)$ is a multiple of 3.[^5] In particular, the armchair nanotubes denoted by $(n,n)$ are always metallic, and the zigzag nanotubes $(n,0)$ are only metallic when $n$ is a multiple of 3.

[^4]: There are two inequivalent $K$ and $K'$ points in the Brillouin zone of 2D graphite as is shown in Fig. {numref}`fig-apptransport-B-6` and thus the metallic condition can also be obtained in terms of $K'$. However, the results in that case are identical to the case specified by $\overrightarrow{YK}$.
[^5]: Since $3n$ is a multiple of 3, the remainders of $(2n+m)/3$ and $(n-m)/3$ are identical.

:::{figure} images/fig-apptransport-B-7.png
:name: fig-apptransport-B-7
:width: 80%
:align: center
Fig. B.7: The carbon nanotubes $(n,m)$ that are metallic and semiconducting, respectively, are denoted by open and solid circles on the map of chiral vectors $(n,m)$. For very small diameter nanotubes (e.g., $d_t < 0.7$ nm), the tight binding approximation is not sufficiently accurate, and more detailed approaches are needed. For example, small diameter nanotubes, such as the $(4,2)$ nanotube is predicted to be semiconducting by tight binding approximation, though more detailed calculations show $(4,2)$ to be metallic and experiments indicate that it may be superconducting.
:::

In Fig. {numref}`fig-apptransport-B-7`, we show which carbon nanotubes are metallic and which are semiconducting, denoted by open and solid circles, respectively. From Fig. {numref}`fig-apptransport-B-7`, it follows that approximately one third of the carbon nanotubes are metallic and the other two thirds are semiconducting.

### B.3.2 Energy Dispersion of Armchair and Zigzag Nanotubes

To obtain explicit expressions for the dispersion relations, the simplest cases to consider are the nanotubes having the highest symmetry, i.e. the achiral armchair and zigzag nanotubes. The appropriate periodic boundary conditions used to obtain the energy eigenvalues for the $(n,n)$ armchair nanotube define the small number of allowed wave vectors $k_{x,q}$ in the circumferential direction

:::{math}
:label: eq-apptransport-B-22
n\sqrt{3}k_{x,q}a = 2\pi q, \quad (q = 1, \ldots, 2n).
:::

:::{figure} images/fig-apptransport-B-8.png
:name: fig-apptransport-B-8
:width: 90%
:align: center
Fig. B.8: One-dimensional energy dispersion relations for (a) armchair $(5,5)$, (b) zigzag $(9,0)$, and (c) zigzag $(10,0)$ carbon nanotubes labeled by the irreducible representations of the point group $D_{nd}$ or $D_{nh}$ (which describe the symmetry of these nanotubes), depending on whether there are even or odd numbers of bands $n$ at the $\Gamma$ point ($k=0$). The $a$-bands are nondegenerate and the $e$-bands are doubly degenerate at a general $k$-point. The $X$ points for armchair and zigzag nanotubes correspond to $k=\pm\pi/a$ and $k=\pm\pi/\sqrt{3}a$, respectively. (See Eqs. B.23–B.25.)
:::

Substitution of the discrete allowed values for $k_{x,q}$ given by Eq. {eq}`eq-apptransport-B-22` into Eq. {eq}`eq-apptransport-B-8` yields the energy dispersion relations $E_q^a(k)$ for the armchair nanotube, $\mathbf{C}_h = (n,n)$,

:::{math}
:label: eq-apptransport-B-23
\begin{aligned}
E_q^a(k) &= \pm t\left\{1 \pm 4\cos\left(\frac{q\pi}{n}\right)\cos\left(\frac{ka}{2}\right) + 4\cos^2\left(\frac{ka}{2}\right)\right\}^{1/2}, \\
&\qquad (-\pi < ka < \pi), \quad (q = 1, \ldots, 2n)
\end{aligned}
:::

in which the superscript $a$ refers to armchair and $k$ is a one-dimensional vector in the direction of the vector $\mathbf{K}_2 = (\mathbf{b}_1 - \mathbf{b}_2)/2$. This direction corresponds to the vector from the $\Gamma$ point to the $K$ point in the two-dimensional Brillouin zone of graphite[^6] [see Fig. {numref}`fig-apptransport-B-1`(b)]. The resulting calculated 1D dispersion relations $E_q^a(k)$ for the $(5,5)$ armchair nanotube are shown in Fig. {numref}`fig-apptransport-B-8`(a), where we see six dispersion relations for the conduction bands[^7] and an equal number for the valence bands.

[^6]: Note that $\mathbf{K}_2$ vector is *not* a reciprocal lattice vector of the 2D graphite.
[^7]: The Fermi energy $E_F$ corresponds to $E/t = 0$. The upper half of Fig. B.8 corresponds to the unoccupied conduction bands.

Because of the degeneracy point between the valence and conduction bands at the band crossing which occurs at the Fermi energy, the $(5,5)$ armchair nanotube is thus a zero-gap semiconductor which will exhibit metallic conduction at finite temperatures, because only infinitesimal excitations are needed to excite carriers into the conduction band. All $(n,n)$ armchair nanotubes have a band degeneracy between the highest valence band and the lowest conduction band at $k = \pm 2\pi/(3a)$, where the bands cross the Fermi level. Thus, all armchair nanotubes are expected to exhibit metallic conduction, similar to the behavior of 2D graphene sheets.

:::{figure} images/fig-apptransport-B-9.png
:name: fig-apptransport-B-9
:width: 55%
:align: center
Fig. B.9: Plot of the energy bands $E(k)$ for the metallic 1D nanotube $(n,m)=(9,6)$ for values of the energy between $-t$ and $t$, in dimensionless units $E(k)/|t|$. The Fermi level is at $E=0$. The largest common divisor of $(9,6)$ is $d=3$, and the value of $d_R$ is $d_R=3$. The general behavior of the four energy bands intersecting at $k=0$ is typical of the case where $d_R=d$.
:::

The energy bands for the $\mathbf{C}_h = (n,0)$ zigzag nanotube $E_q^z(k)$ can be obtained likewise from Eq. {eq}`eq-apptransport-B-8` by writing the periodic boundary condition on $k_y$ as

:::{math}
:label: eq-apptransport-B-24
nk_{y,q}a = 2\pi q, \quad (q = 1, \ldots, 2n),
:::

to yield the 1D dispersion relations for the $4n$ states for the $(n,0)$ zigzag nanotube (denoted by the superscript $z$)

:::{math}
:label: eq-apptransport-B-25
\begin{aligned}
E_q^z(k) &= \pm t\left\{1 \pm 4\cos\left(\frac{\sqrt{3}ka}{2}\right)\cos\left(\frac{q\pi}{n}\right) + 4\cos^2\left(\frac{q\pi}{n}\right)\right\}^{1/2}, \\
&\qquad \left(-\frac{\pi}{\sqrt{3}} < ka < \frac{\pi}{\sqrt{3}}\right), \quad (q = 1, \ldots, 2n).
\end{aligned}
:::

The resulting calculated 1D dispersion relations $E_q^z(k)$ for the $(9,0)$ and $(10,0)$ zigzag nanotubes are shown in Figs. {numref}`fig-apptransport-B-8`(b) and (c), respectively. There is no energy gap for the metallic $(9,0)$ nanotube at $k=0$, whereas the $(10,0)$ nanotube indeed shows an energy gap. For a general $(n,0)$ zigzag nanotube, when $n$ is a multiple of 3, the energy gap at $k=0$ becomes zero; however, when $n$ is not a multiple of 3, an energy gap opens at $k=0$, as seen in Fig. {numref}`fig-apptransport-B-8`(c).

### B.3.3 Dispersion of Chiral Nanotubes

Chiral nanotubes have usually much larger unit cells and, therefore a large number of branches in their dispersion relation. In Fig. {numref}`fig-apptransport-B-9`, we show dispersion relations for the $(9,6)$ chiral nanotube. Since $n-m$ is a multiple of 3, this chiral nanotube is metallic.

## B.4 Density of States, Energy Gap

:::{figure} images/fig-apptransport-B-10.png
:name: fig-apptransport-B-10
:width: 70%
:align: center
Fig. B.10: Electronic 1D density of states per unit cell of a 2D graphene sheet for two $(n,0)$ zigzag nanotubes: (a) the $(9,0)$ nanotube which has metallic behavior, (b) the $(10,0)$ nanotube which has semiconducting behavior. Also shown as a dashed line in the figure is the density of states for the 2D graphene sheet.
:::

Of particular interest has been the energy dependence of the nanotube density of states, as shown in Fig. {numref}`fig-apptransport-B-10` which compares the density of states for metallic $(9,0)$ and semiconducting $(10,0)$ zigzag nanotubes. In this figure, we see that the density of states near the Fermi level $E_F$ (located at $E=0$) is different for metallic and semiconducting nanotubes. The density of states at $E_F$ has a value of zero for semiconducting nanotubes, but is non-zero (and small) for metallic nanotubes. Also of great interest are the singularities in the 1D density of states, corresponding to extrema in the $E(k)$ relations. The comparison between the 1D density of states for the nanotubes and the 2D density of states for a graphene layer is included in the figure. Another important result, pertaining to semiconducting nanotubes, shows that their energy gap depends upon the reciprocal nanotube diameter $d_t$, according to the relation

$$E_g = \frac{|t|a_{\mathrm{C}-\mathrm{C}}}{d_t},$$

independent of the chiral angle of the semiconducting nanotube, where $a_{\mathrm{C}-\mathrm{C}} = a/\sqrt{3}$.

:::{figure} images/fig-apptransport-B-11.png
:name: fig-apptransport-B-11
:width: 90%
:align: center
Fig. B.11: (a) Calculated energy separations $E_{ii}(d_t)$ between van Hove singularities $i$ in the 1D electronic density of states of the conduction and valence bands for all $(n,m)$ values vs nanotube diameter $0.4 < d_t < 3.0$ nm, using a value for the carbon-carbon energy overlap integral of $\gamma_0 = 2.9$ eV and a nearest neighbor carbon-carbon distance $a_{\mathrm{C}-\mathrm{C}} = 1.42\,\text{\AA}$. Semiconducting (S) and metallic (M) nanotubes are indicated by crosses and open circles, respectively. The index $i$ in the interband transitions $E_{ii}$ denotes the transition between the van Hove singularities, with $i=1$ being closest to the Fermi level. (b) Plot of the 2D equi-energy contours of graphite, showing trigonal warping effects in the contours, as we move from the $K$ point in the $K-\Gamma$ or $K-M$ directions. The equi-energy contours are circles near the $K$ point and near the center of the Brillouin zone. But near the zone boundary, the contours are straight lines which connect the nearest $M$ points.
:::

It is significant that every $(n,m)$ nanotube has a different and unique set of energies where the singularities in the 1D electronic density of states occur. Fig. {numref}`fig-apptransport-B-11`(a) shows a plot of the energy differences $E_{ii}$ between singularities $i$ in the conduction and valence bands for every possible nanotube as a function of nanotube diameter, showing the uniqueness of the energies of these singularities in the density of states. This uniqueness arises from the trigonal warping effect. Fig. {numref}`fig-apptransport-B-11`(b) shows that the constant energy surfaces around the origin ($\Gamma$ point where $k=0$) and around the $K$ and $K'$ points in the 2D Brillouin zone are circular only near the $\Gamma$, $K$, and $K'$ high symmetry points. Away from these symmetry points, trigonal warping effects become important, giving rise to a different set of singularities in the density of states, depending on the nanotube diameter and chirality. We can measure the $E_{ii}$ singularities in the density of states at the single nanotube level by the Raman effect, which shows a strong resonance with an individual $(n,m)$ carbon nanotube when the laser excitation energy is equal to one of these singularities. Therefore, the resonance Raman effect can be used to identify the $(n,m)$ values for individual carbon nanotubes. Because of the unique properties of these particular low dimensional systems, spectroscopy can be used to obtain structural information about individual carbon nanotubes.
