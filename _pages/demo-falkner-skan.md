---
layout: single
title: "Pressure gradient and the shape of a boundary layer"
permalink: /teaching/falkner-skan/
author_profile: true
---

A boundary layer that is about to separate looks different from a healthy one long before anything dramatic
happens. The Falkner-Skan family makes that visible, because a single parameter takes you continuously from
a strongly accelerated flow all the way to the point of separation.

{% include demo.html src="/assets/demos/falkner-skan.html" title="Falkner-Skan profiles" %}

The profile is solved live — a shooting method on the wall shear, marched with RK4 — so the curve you see is
a numerical solution of the ODE, not a stored table.

## Collapsing a partial differential equation into an ordinary one

Take an external velocity of the form $U_e \propto x^m$. The boundary layer equations then admit a
*similarity solution*: profiles at different stations are the same curve, stretched. Writing the
streamfunction in similarity variables reduces the problem to one ordinary differential equation,

$$ f''' + f f'' + \beta\left(1 - f'^2\right) = 0 $$

with $f(0) = f'(0) = 0$ at the wall and $f'(\infty) = 1$ in the free stream. Here $f' = u/U_e$ is the velocity
profile itself and

$$ \beta = \dfrac{2m}{m+1} $$

is the Hartree parameter, which is simply the pressure gradient in disguise. Positive $\beta$ is a
favorable (accelerating) gradient, negative is adverse.

Three members of the family are worth knowing by name. $\beta = 1$ is the stagnation-point flow;
$\beta = 0$ is the flat plate, the Blasius solution; $\beta = -0.198838$ is where the family stops.

## Reading the wall

The single most useful number is $f''(0)$, proportional to the wall shear stress and therefore to skin
friction. Sweep $\beta$ downward and watch it fall monotonically. A favorable gradient presses the profile
full and steep against the surface; an adverse gradient drains momentum out of the near-wall fluid and the
profile leans back.

Turn on the **shear** curve and something more specific appears. For any adverse gradient, $f''$ starts
positive at the wall, passes through zero somewhere out in the layer, and goes negative. That zero is an
**inflection point** in the velocity profile, and it is not merely cosmetic: by Rayleigh's criterion an
inflectional profile is the precondition for inviscid instability. An adverse gradient does not just weaken
a boundary layer, it makes it unstable, which is why transition and separation so often arrive together.

## Where the family ends

At $\beta = -0.198838$ the wall shear reaches exactly zero. The fluid arrives at the surface with no slope at
all, which is the definition of separation. Push the slider any further and there is no attached similarity
solution — not a numerical difficulty, but a statement that no self-similar boundary layer can survive a
gradient that strong.

The shape factor $H = \delta^*/\theta$ tracks the same story with a single number: 2.59 for the flat plate,
2.22 at the stagnation point, and 4.03 at separation. Because $H$ is dimensionless and easy to compute from
measured profiles, it is the quantity you actually monitor in an experiment when you want to know how close
a layer is to letting go.

## Things to try

- Step through the presets from stagnation to separation and watch the profile deflate. The Blasius
  reference stays fixed as a dashed line, so the change is easy to read against a familiar curve.
- Turn on the shear curve and find the $\beta$ at which the inflection point first leaves the wall. Below
  that, every profile is inflectional.
- Watch $H$ as you approach separation. It rises slowly at first and then quickly — by the time a measured
  $H$ reaches 3.5 there is very little margin left.
- Note the normalisation. $\eta$ here carries the $(m+1)/2$ factor conventional to Falkner-Skan, so the flat
  plate reads $f''(0) = 0.4696$ rather than the Blasius-scaled 0.3321. The two differ by exactly $\sqrt{2}$,
  and $H$, being a ratio, is identical either way.
