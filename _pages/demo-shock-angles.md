---
layout: single
title: "Mach cones and oblique shocks"
permalink: /teaching/shock-angles/
author_profile: true
---

A disturbance travels at the speed of sound. Move the source faster than that and it outruns its own
signal, so the fluid ahead gets no warning that anything is coming. Everything distinctive about supersonic
flow follows from that one sentence, including the two angles this page is about.

{% include demo.html src="/assets/demos/shock-angles.html" title="Mach cone and oblique shock" %}

## The cone is an envelope, not an object

In **Moving source**, each circle is a wavefront emitted at an earlier instant, expanding at speed $a$ while
the source moves at $Ma$. Below $M = 1$ the circles still enclose the source and sound reaches everywhere
eventually. Above it the source stays ahead of every wavefront it has ever emitted, and the circles acquire
a common tangent.

That tangent line is the Mach cone. It is not a physical surface — nothing is there but the coincidence that
infinitely many wavefronts touch it — and its half angle follows from a triangle: in time $t$ the wave has
grown to $at$ while the source has run $Mat$, so

$$ \sin\mu = \dfrac{1}{M} $$

At $M = 1$ the cone is a flat plane normal to the motion; as $M$ grows it sweeps back and thins.

## An oblique shock is a Mach wave that had to work

Switch to **Wedge**. Now the flow has to turn through an angle $\theta$ to run along the surface, and the
mechanism is a shock hinged at the apex. The geometry hides a simple idea: only the velocity component
*normal* to the shock is processed. That component behaves exactly like a normal shock at
$M_{n1} = M_1\sin\beta$, while the tangential component slides through unchanged. Every property ratio in the
readout comes from feeding $M_{n1}$ into the ordinary normal-shock relations.

Requiring that the flow leave parallel to the wedge closes the problem and gives the $\theta$–$\beta$–$M$
relation,

$$ \tan\theta = 2\cot\beta \, \dfrac{M_1^2\sin^2\beta - 1}{M_1^2(\gamma + \cos 2\beta) + 2} $$

plotted live underneath. Now drive $\theta$ towards zero and watch the shock angle collapse onto $\mu$. A
vanishingly weak oblique shock *is* a Mach wave — the two angles on this page are the same quantity at
opposite ends of a strength scale.

## Two answers, and then none

The curve is the surprising part. For every deflection below a maximum, it crosses twice: two shock angles
turn the flow through the same angle. The **weak** solution (lower $\beta$) usually leaves the flow
supersonic and is what nature picks unless downstream conditions force otherwise; the **strong** solution
leaves it subsonic. Tick *Strong branch* and watch $M_2$ drop below one.

Push $\theta$ past the nose of the curve and there is no crossing at all. No attached shock can turn the flow
that far at that Mach number, so the shock detaches and stands off ahead of the body as a curved bow shock —
locally normal on the axis, weakening into a Mach wave far out on the wings. This is why blunt reentry
bodies carry a detached shock, and why $\theta_{max}$ is the number that decides whether a supersonic inlet
ramp works.

## Things to try

- In **Moving source**, sweep $M$ down through 1 and watch the cone open until it is flat, then vanish.
- In **Wedge**, hold $\theta = 10°$ and raise $M$ from 1.5 to 5. The shock lies down against the surface as
  the Mach angle shrinks, and the pressure ratio across it climbs steeply.
- Hold $M = 2$ and raise $\theta$ slowly to $22.97°$. The two roots on the diagram slide towards each other,
  meet, and then the solution disappears — detachment is a pair of roots colliding.
- Compare $p_{02}/p_{01}$ between the weak and strong branches at the same deflection. The strong shock
  destroys far more stagnation pressure for the same turning, which is why inlets are designed to run on the
  weak branch.
