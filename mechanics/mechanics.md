---
title: "mechanics"
author: bosonicli
output: pdf_document
mainfont: "Noto Serif CJK SC"
bibliography: [../../ref_repository/bib/EndNote_Bohai_2021.bib]
---

# mechanics

[toc]

## mission

## fragment

*	effective gravity induced by rotation of facility

	Only second-order effect is present at a perturbative level.

*	epicycle model

	Fitting Kepler orbit of binary star system to epicycle system?

*	space channel in gravitational fields

	More fictional rather than a realistic one. Few materials are found.

## Kepler

*   effective potential

*   orbit stability

	Bertland Theorem

*   Hydrogen and $SO(4)$ symmetry

	Laplace-Runge-Lenz vector does not necessarily commute with angular momentum $L$ in the $\mathcal{L}$ notion. It is conserved given that $\mathcal{H}$ is time-independent. In other words, it is invariant under a different (more strict) variational condition.

*   action / time evolution

	Time evolution operators classically (failed)

## asymptotic

### tidal force

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

## thermal/hydro

*	Fluid Roche limit

	To be continued.

*	Waterball without gravity

	ossilation?

## scenarios

### wander around space station

Space station $O$ is orbiting $\vec{r}:(r,\theta)$ around the earth and an astronaut is wandering around $O$ with displacement $\vec{\Delta r}$ in non-rotating system and $\vec{\delta r}$ in rorating system.

Dynamic in the rotating system is described in \eqref{eqn:a_delta}

$$
\begin{aligned}
{\vec{a}}_{\delta} &= \vec{a}_{Tide} + \vec{a}_{c} + \vec{a}_{\beta}	\\
\vec{a}_{Tide} &= - \frac{k}{r_0^3} (- 2 \delta r_{r} \hat{r} + \delta r_{\theta} \hat{\theta} )	\\
\vec{a}_{c} &= 2 \dot{\theta} (\dot{\delta r_{\theta}} \hat{r} - \dot{\delta r_{r}} \hat{\theta} )	\\
\vec{a}_{\beta} &= \ddot{\theta} (\delta r_{\theta} \hat{r} - \delta r_{r} \hat{\theta})
\end{aligned}
\tag{aDelta}
\label{eqn:a_delta}
$$

Assume $O$ is orbiting on a circle $(\dot{\theta}, \ddot{\theta}) = (\omega,0)$, we have $\omega = \frac{k}{r_0^3}$, 

then \eqref{eqn:a_delta} is simplified as \eqref{eqn:a_circle}

$$
\begin{aligned}
\frac{d^2}{dt^2} \vec{\delta r} &= \vec{a}_{Tide} + \vec{a}_{c}	\\
&= -\omega^2 (- 2 \delta r_{r} \hat{r} + \delta r_{\theta} \hat{\theta} ) + 2 \omega (\dot{\delta r_{\theta}} \hat{r} - \dot{\delta r_{r}} \hat{\theta})
\end{aligned}
\tag{aCircle}
\label{eqn:a_circle}
$$

Qualitative analysis of the dynamics: Assume the astronaut orbits around the space station with $\dot{\delta \theta} < 0$ and a period same as the space station orbit $T_0$

*	Averagely, orbit of $\vec{\delta r}$ operates with $\vec{-\omega}$;

*	At vertex along the $\hat{r}$ direction, $\vec{a}_{Tide}$ points outwards, so velocity should be large to generate massive $\vec{a}_{c}$;

*	At vertex along the $\hat{\theta}$ direction, $\vec{a}_{Tide}$ points inwards, enough to keep the orbit bound, so velocity should be small;

*	Quantitave description of the orbit dynamic remains mystery;

### Lagrangian points

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