---
title: "Agnosticism"
author: bosonicli
date: \today
mainfont: "Noto Serif CJK SC"
bibliography: [../../ref_repository/bib/EndNote_Bohai_2021.bib]
link-citations: true
colorlinks: true
links-as-notes: true
output: pdf_document
---

# agnosticism

[toc]

## mission

## fragment

*	earth heat engine hypo

	high T Sun, low T background radiation

## Gravity

### Gravitational Wave

*	coupling of gravitational wave?

	with mass / gravitational waves / black holes

*	curve of spacetime is nonlinear, 'gravitational wave' is just the linear asymptotic

*	vaccum with nonzero cosmological constant is itself a momentum medium, it has E-P density

*	it is not wierd that $ ( 1 + \lambda x^2 + \lambda y^2 )^{\frac{1}{2}} $ has a $xy$ term at first order of $\lambda$

### mass myth

*	'gravitational mass' in classical equations is defined through energy/force

	then blocked by the fact that energy is not well defined in curved spacetime

*	The only meaningful connection is through E-P tensor and Einstein equation $ S = \sqrt{-h} S_{flat} $

*	asymptotically mass could be treated as source of 'gravity' $ (h - h_{flat}) $

### energy of gravity system

*	how much energy is released in a collapsing celestial

	an extreme case is 'black hole bomb', which 'release energy' to an asymptotic flat spacetime

	then blocked by the fact that energy is not well defined in curved spacetime

## Black Hole

### Black Hole Geometry

*	Black hole has no volume

	It has only area, just like the line on the tennis has no area but only length

	decuction: all mass of black hole is stored on surface --- surface information hypo --- holographic universe hypo

*	Killing Vector

	how to comprehend the time/space Killing Vector?

### Black Hole as a Celestial

*	Dark region is larger than the horizon

### Black Hole ThermoDynamics

*	Hawking Radiation

	black hole evaporate V.S. Background Radiation

	mass-temp relation, critical mass/size

*	Does black hole has a characteristic scale? Does the Penrose CCC hypo require all black holes vaporized?

*	mass of a Schwarzmann black hole is proportional to area. But black hole thermodynamics is derived from energy extration in Penrose process of Kerr black hole. What's meaningful in black hole thermodynamics $ \delta M = \frac{\kappa}{8 \pi G} \delta A + \Omega_{H} \delta J $ is surface gravity $ \kappa = \frac{\partial M}{\partial A} \propto \frac{1}{M} $

*	What is mass

	Irreducible mass is area sqrt $ M_{irr}^2 = \frac{A}{16 \pi G^2} $

	mass is E-P tensor, E-P is invariant of spacetime invariance, but black hole is curved spacetime

	is it related to 'gravity is entropy force'

	is Penrose process also related to entropy / free energy

## Cosmology

*	Scale invariance

	expression of space of light

*	Penrose Conformal Cyclic Cosmology

## Astronomy

*	Magnetic Field

	Solar wind dynamics in geomagnetic field is plasma dynamics rather than single particle one

	Solar wind + solar magnetic field also blocks space rays

## HydroDynamics

*	Fluid Roche limit

*	Waterball without gravity

	ossilation?

## ElectroDynamics

*   action $ L = V(\phi) + J \phi $ means J is source related to energy, and from Lagrangian equation $ \partial \phi = J $ indicating J is also the field-generating source

*   EM field in higher dimension

	E & M field no longer dual?

## Dynamics

### fragment

*   orbit stability

	Bertland Theorem

*	sunshine duration

*	effective gravity induced by rotation of facility

	Only second-order effect is present at a perturbative level

*	epicycle model

	Fitting Kepler orbit of binary celestial system to epicycle system?

*	space channel in gravitational fields

	More fictional rather than a realistic one. Few materials are found

*   Hydrogen and $SO(4)$ symmetry

	Laplace-Runge-Lenz vector does not necessarily commute with angular momentum $L$ in the $\mathcal{L}$ notion. It is conserved given that $\mathcal{H}$ is time-independent. In other words, it is invariant under a different (more strict) variational condition.

*   action / time evolution

	Time evolution operators classically (failed)

### Tidal Force

$$
\begin{aligned}
(1+x)^{-\frac{1}{2}} &= 1 + (-\frac{1}{2} ) x + (\frac{3}{8}) x^2 + o(x^3)	\\
(1+x)^{-\frac{3}{2}} &= 1 + (-\frac{3}{2} ) x + (\frac{15}{8}) x^2 + o(x^3)
\end{aligned}
\tag{taylorM}
$$

$$
\begin{aligned}
\vec{a}_{g} &= - \frac{k}{{\vert\vec{r}\vert}^3} \vec{r}	\\
&= - k (\vec{r}^2)^{-\frac{3}{2}} \vec{r}	\\
&= - \frac{k}{r_0^3} (1 + \frac{(\vec{r_0}+\vec{\Delta r})^2-\vec{r_0}^2}{\vec{r_0}^2})^{-\frac{3}{2}} (\vec{r_0} + \vec{\Delta r})	\\
&= - \frac{k}{r_0^3} (1 + \frac{2 \vec{r_0} \cdot \vec{\Delta r} + (\vec{\Delta r})^2}{\vec{r_0}^2})^{-\frac{3}{2}} (\vec{r_0} + \vec{\Delta r})	\\
&= - \frac{k}{r_0^3} (1 - \frac{3 \vec{r_0} \cdot \vec{\Delta r}}{\vec{r_0}^2} + \frac{15 (\vec{r_0} \cdot \vec{\Delta r})^2}{2 \vec{r_0}^4} - \frac{3 (\vec{\Delta r})^2}{2 (\vec{r_0})^2}) (\vec{r_0} + \vec{\Delta r})
\end{aligned}
\tag{taylorG}
$$

$$
\begin{aligned}
\vec{a}_{c} &= - \frac{k}{r_0^3} \vec{r_0}	\\
\vec{a}_{Tide} &= \vec{a}_{g} - \vec{a}_{c}	\\
&= o((\vec{\Delta r})^3) - \frac{k}{r_0^3} (\vec{\Delta r} - \frac{3 \vec{r_0} \cdot \vec{\Delta r}}{\vec{r_0}^2} \vec{r_0})	\\
&- \frac{k}{r_0^3} ( \frac{15 (\vec{r_0} \cdot \vec{\Delta r})^2}{2 \vec{r_0}^4} - \frac{3 (\vec{\Delta r})^2}{2 (\vec{r_0})^2}) \vec{r_0} - \frac{k}{r_0^3} (- \frac{3 \vec{r_0} \cdot \vec{\Delta r}}{\vec{r_0}^2}) \vec{\Delta r}	\\
&= \vec{a}_{Tide}^{1} + \vec{a}_{Tide}^{2} + o((\vec{\Delta r})^3)	\\
\vec{a}_{Tide}^{1} &= - \frac{k}{r_0^3} (\vec{\Delta r}_{\perp} - 2 \vec{\Delta r}_{\parallel})
\end{aligned}
\tag{taylorTide}
$$

$$
\begin{aligned}
V_{g} &= - \frac{k}{\vert\vec{r}\vert}	\\
&= - k (\vec{r}^2)^{-\frac{1}{2}}	\\
&= - \frac{k}{r_0} (1 + \frac{(\vec{r_0}+\vec{\Delta r})^2-\vec{r_0}^2}{\vec{r_0}^2})^{-\frac{1}{2}}	\\
&= - \frac{k}{r_0} (1 + \frac{2 \vec{r_0} \cdot \vec{\Delta r} + (\vec{\Delta r})^2}{\vec{r_0}^2})^{-\frac{1}{2}}	\\
&= - \frac{k}{r_0} (1 - \frac{ \vec{r_0} \cdot \vec{\Delta r}}{\vec{r_0}^2} + \frac{3 (\vec{r_0} \cdot \vec{\Delta r})^2}{2 \vec{r_0}^4} - \frac{ (\vec{\Delta r})^2}{2 (\vec{r_0})^2}) + o((\vec{\Delta r})^3)	\\
&= V_{0} + V_{1} + V_{2} + o((\vec{\Delta r})^3)
\end{aligned}
\tag{taylorV}
$$

### Coriolis Force

In system with rotation $(\vec{\omega}, \vec{\beta})$ around point $O$, Non-inertial forces are

$$
\begin{aligned}
\vec{a}_{c} &= -2 (\vec{\omega} \times \vec{\delta v})	\\
\vec{a}_{\beta} &= - \beta \times \vec{\delta r}
\end{aligned}
\tag{aRot}
$$

### Space Colony

Space station $O$ is orbiting $\vec{r}:(r,\theta)$ around the earth and an astronaut is wandering around $O$ with displacement $\vec{\Delta r}$ in non-rotating system and $\vec{\delta r}$ in rorating system.

Dynamic in the rotating system is described as

$$
\begin{aligned}
{\vec{a}}_{\delta} &= \vec{a}_{Tide} + \vec{a}_{c} + \vec{a}_{\beta}	\\
\vec{a}_{Tide} &= - \frac{k}{r_0^3} (- 2 \delta r_{r} \hat{r} + \delta r_{\theta} \hat{\theta} )	\\
\vec{a}_{c} &= 2 \dot{\theta} (\dot{\delta r_{\theta}} \hat{r} - \dot{\delta r_{r}} \hat{\theta} )	\\
\vec{a}_{\beta} &= \ddot{\theta} (\delta r_{\theta} \hat{r} - \delta r_{r} \hat{\theta})
\end{aligned}
\tag{aDelta}
$$

Assume $O$ is orbiting on a circle $(\dot{\theta}, \ddot{\theta}) = (\omega,0)$, we have $\omega = \frac{k}{r_0^3}$, 

then the above equations are simplified as

$$
\begin{aligned}
\frac{d^2}{dt^2} \vec{\delta r} &= \vec{a}_{Tide} + \vec{a}_{c}	\\
&= -\omega^2 (- 2 \delta r_{r} \hat{r} + \delta r_{\theta} \hat{\theta} ) + 2 \omega (\dot{\delta r_{\theta}} \hat{r} - \dot{\delta r_{r}} \hat{\theta})
\end{aligned}
\tag{aCircle}
$$

Qualitative analysis of the dynamics: Assume the astronaut orbits around the space station with $\dot{\delta \theta} < 0$ and a period same as the space station orbit $T_0$

*	Averagely, orbit of $\vec{\delta r}$ operates with $\vec{-\omega}$;

*	At vertex along the $\hat{r}$ direction, $\vec{a}_{Tide}$ points outwards, so velocity should be large to generate massive $\vec{a}_{c}$;

*	At vertex along the $\hat{\theta}$ direction, $\vec{a}_{Tide}$ points inwards, enough to keep the orbit bound, so velocity should be small;

*	Quantitave description of the orbit dynamic remains mystery;

### Lagrangian Points

We consider the effective dynamics in a Non-inertial system of two-body gravity system.

Consider a two-body system consists of two celestial bodies $M_1$ and $M_2$ with distance of $D$. The two-body effective mass and orbiting angular velocity are

$$
\begin{aligned}
M &= \frac{M_1 M_2}{M_1+M_2}	\\
\frac{G M_1 M_2}{D^2} &= \frac{M_1 M_2} \omega^2 D	\\
\omega^2 &= \frac{G (M_1 + M_2)}{D^3}
\end{aligned}
\tag{motionBin}
$$

The two celestial bodies are orbiting around the centroid $O$. Now we consider the Lagrangian point $L_4$ locating at the vertex of an equilateral triangle connecting $M_1$ and $M_2$, thus we have $\vec{r} = \frac{M_1 \vec{r_1} + M_2 \vec{r_2}}{M_1 + M_2}$

In the rotating celestial system, the effective potential around $L_4$ is

$$
\begin{aligned}
V_{eff} &= V_0(\vec{r_1}) + V_1(\vec{r_1}) + V_2(\vec{r_1}) + V_0(\vec{r_2}) + V_1(\vec{r_2}) + V_2(\vec{r_2}) + o((\vec{\Delta r})^3) + V_{\omega}	\\
&= V_{eff}^{0} + V_{eff}^{1} + V_{eff}^{2} + o((\vec{\Delta r})^3)	\\
V_{\omega} &= -\frac{1}{2} \omega^2 (\vec{r} + \vec{\Delta r})^2	\\
V_{eff}^{1} &= -\frac{G M_1}{D} (-\frac{\vec{r_1} \cdot \vec{\Delta r}}{{\vert\vec{r_1}\vert}^2})  -\frac{G M_2}{D} (-\frac{\vec{r_2} \cdot \vec{\Delta r}}{{\vert\vec{r_2}\vert}^2}) - \omega^2 \vec{r} \cdot \vec{\Delta r}	\\
&= \frac{G}{D^3} (M_1 \vec{r_1} + M_2 \vec{r_2}) \cdot \vec{\Delta r} - \frac{G}{D^3} (M_1 \vec{r_1} + M_2 \vec{r_2}) \cdot \vec{\Delta r}	\\
&= 0	\\
V_{eff} &= V_{eff}^{0} + V_{eff}^{2} + o((\vec{\Delta r})^3)
\end{aligned}
\tag{taylorBin}
$$

In fact $V_{eff}^2$ is convex around $L_4$, thus $L_4$ is a smooth maximum in the rotating system. Celestial bodies around $L_4$ are bounded by Coriolis force under certain condition (the mass ratio boundary $\frac{M_1}{M_2}$ actually)