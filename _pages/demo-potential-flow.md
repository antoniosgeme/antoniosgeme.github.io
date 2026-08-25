---
layout: single
title: "Potential flow: building a wing out of nothing"
permalink: /teaching/potential-flow/
author_profile: true
---

Incompressible, irrotational flow obeys Laplace's equation, and Laplace's equation is linear. That single
fact is what most of classical aerodynamics is built on: complicated flows can be assembled by adding
simple ones together. Drag the sliders below and watch a cylinder, and then a lifting airfoil, appear out
of three elementary solutions.

{% include demo.html src="/assets/demos/potential-flow.html" title="Potential flow sandbox" %}

Color is the pressure coefficient $C_p$ — red where the flow runs fast and the pressure drops, blue-violet
where it stagnates. The white contours are streamlines.

## Why we are allowed to just add flows together

Irrotational flow has a velocity potential, $\mathbf{u} = \nabla\phi$, and incompressibility turns that into
$\nabla^2\phi = 0$. Because the operator is linear, the sum of two solutions is another solution. In two
dimensions we can go further and pack the potential $\phi$ and the streamfunction $\psi$ into one analytic
function of a complex variable, $F(z) = \phi + i\psi$. Any analytic $F$ is a legal flow, streamlines are the
contours of $\psi$, and the velocity falls out of a single derivative, $u - iv = \mathrm{d}F/\mathrm{d}z$.

The demo carries three terms:

- **Uniform stream**, $F = U e^{-i\alpha} z$ — flow at speed $U$ and angle $\alpha$.
- **Vortex**, $F = -\tfrac{i\Gamma}{2\pi}\ln(z - z_0)$ — circulation $\Gamma$ around the point $z_0$, yet
  irrotational everywhere except at the singularity itself.
- **Doublet**, $F = \tfrac{\kappa}{2\pi} e^{i\alpha}/(z - z_0)$ — the limit of a source and sink brought
  together while their strength grows.

## The body is a by-product, not an input

Switch on the uniform stream and the doublet together. A circle appears, and the flow parts around it as
though a solid cylinder were sitting there. Nothing imposed a boundary: the dividing streamline simply
closes on itself, and it does so at radius

$$ a = \sqrt{\dfrac{\kappa}{2\pi U}} $$

which is what the *radius a* readout tracks. Change the freestream and the body resizes, because the balance
between the two flows is what sets its size. This inversion is the heart of the method — you do not mesh a
shape and solve around it, you look for the superposition whose dividing streamline happens to be the shape
you want.

## Circulation is what makes lift, and nothing fixes it

Add the vortex. The circle survives, because a vortex centred inside it does not disturb the surface as a
streamline, but the fore-and-aft symmetry breaks: the two stagnation points slide around the body. The
Kutta–Joukowski theorem then gives the lift as $L' = -\rho U_\infty \Gamma$.

Notice what is missing. Nothing in the inviscid problem tells you *which* $\Gamma$ nature picks. A cylinder
in potential flow has no unique lift. That gap is the whole reason the Kutta condition has to be introduced
by hand.

## From a circle to an airfoil

The Joukowski map $\zeta = z + b^2/z$ is conformal, so it carries the flow across with it: $\psi$ is unchanged
at corresponding points, and velocities simply scale by $|\mathrm{d}\zeta/\mathrm{d}z|$. Offsetting the
circle's centre to the left produces thickness; lifting it produces camber.

The map has a catch. Its derivative vanishes at $z = \pm b$, which is exactly where the trailing edge lands.
Unless the flow leaves that point smoothly, the mapped velocity there is infinite. Demanding that it stay
finite — the **Kutta condition** — selects one and only one circulation,

$$ \Gamma = 4\pi U a \sin(\theta_{TE} - \alpha) $$

and with it the entire lift curve of a thin airfoil. It is worth sitting with the strangeness of that:
viscosity is what physically establishes the circulation, and viscosity appears nowhere in the formula.

## Things to try

- Start with the doublet alone, then add the uniform stream and watch the closed body form. Change $U$ and
  see the radius readout move as $\sqrt{\kappa/2\pi U}$.
- On the cylinder, wind up the circulation. The two stagnation points slide down and towards each other,
  merge at the bottom, then lift off the surface entirely. That departure happens at $\Gamma = 4\pi U a$.
- Press **Cambered airfoil**, then set $\Gamma$ back to zero by hand. The flow whips around the sharp
  trailing edge from below — the singularity the Kutta condition exists to remove. Press
  **Apply Kutta condition** and watch the rear stagnation point snap onto the trailing edge.
- With the airfoil at $\alpha = 8°$, compare the reported $C_L$ against the thin-airfoil estimate
  $2\pi(\alpha + \beta)$. They agree to a few percent, and the gap is the thickness the thin-airfoil
  approximation threw away.
