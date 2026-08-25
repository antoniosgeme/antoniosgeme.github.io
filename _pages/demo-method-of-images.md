---
layout: single
title: "The method of images: deleting a wall"
permalink: /teaching/method-of-images/
author_profile: true
---

A boundary condition is a constraint on a solution, but it can also be read as a statement about symmetry.
Read it the second way and a solid wall stops being an obstacle to solve around and becomes something you
can delete outright, provided you put the right thing on the other side.

{% include demo.html src="/assets/demos/image-vortex.html" title="Method of images" %}

Drag the vortex anywhere. Color is flow speed, white contours are streamlines, and the arrow on the vortex
is the velocity its own reflection induces on it. **Reveal image region** removes the wall and shows what
was standing in for it.

## A wall is a mirror

A solid wall requires that no fluid pass through it: the normal velocity must vanish along $y = 0$. Rather
than solve a boundary-value problem, place a second vortex at the mirror point $\bar{z}_1$ with the opposite
circulation. By symmetry the normal components of the two induced velocities cancel everywhere on the line,
so $y = 0$ becomes a streamline all by itself.

At that point the wall has no work left to do. The flow in the upper half plane is *identical* whether you
picture a vortex above a wall, or two counter-rotating vortices in unbounded fluid. Toggling
**Reveal image region** switches between those two pictures without changing a single streamline above
the line — which is the entire point of the technique.

## The image pushes back

The image is not merely bookkeeping; it induces a real velocity at the location of the real vortex. For a
vortex at height $h$, the image sits $2h$ below it and drives it *parallel* to the wall at

$$ u = \dfrac{\Gamma}{4\pi h} $$

That is the arrow in the demo, and it is why a vortex near the ground does not sit still. Bring the vortex
closer to the wall and the drift accelerates; a trailing vortex in ground effect convects sideways for
exactly this reason.

## A cylinder needs two images

Curved boundaries are harder, and the Milne-Thomson circle theorem supplies the answer: for a vortex
$\Gamma$ at $z_1$ outside a cylinder of radius $a$, put an image $-\Gamma$ at the inverse point $a^2/\bar{z}_1$
*and* an image $+\Gamma$ at the centre. The first makes $|z| = a$ a streamline; the second restores the net
circulation around the cylinder to zero, which the first one spoiled.

Switch to **Cylinder** and reveal the images: both appear inside the body, one near the surface and one
pinned at the centre. Their combined induction on the real vortex turns out to be purely azimuthal, so the
arrow always points along a circle about the centre — released, the vortex would orbit rather than drift
away or fall in.

## Where this shows up

The same construction, with different physics hung on it, appears throughout the subject. Ground effect on a
wing is a wing plus its mirror image. Wind tunnel wall corrections are images of the model in the tunnel
walls. Acoustic reflection off a hard surface is [an in-phase image source](/teaching/sound-over-ground/) —
the same trick in wave form, and worth comparing directly against this page.

## Things to try

- Put the vortex close to the wall and watch the drift arrow grow as $1/h$. Then flip the sign of $\Gamma$
  and watch the drift reverse.
- Turn on **Reveal image region** and confirm that the streamline pattern above the wall does not change at
  all. Nothing above the line can tell the difference.
- Add a freestream and tune $U$ against the self-induced drift until they cancel. The vortex is then
  stationary in the lab frame — a standing vortex in ground effect.
- Switch to the cylinder and move the vortex close to the surface. The inverse point races outward to meet
  it; in the limit the pair behaves exactly like the flat-wall case, because a small enough patch of any
  smooth surface is a plane.
