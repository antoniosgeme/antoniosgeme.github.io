---
layout: single
title: "Sound over ground: images in wave form"
permalink: /teaching/sound-over-ground/
author_profile: true
---

The [method of images](/teaching/method-of-images/) was introduced for a vortex near a wall. Nothing in the
argument was specific to vortices — it only needed a linear equation and a symmetry. Acoustics supplies both,
so the same construction works, with one interesting new wrinkle: there are two kinds of surface, and they
take opposite images.

{% include demo.html src="/assets/demos/sound-over-ground.html" title="Acoustic sources over a surface" %}

Drag to move the source. **Wavefronts** shows the instantaneous pressure; **Level** shows amplitude in
decibels, which is where the interference pattern reads most clearly.

## Two surfaces, two images

For time-harmonic sound the wave equation reduces to the Helmholtz equation, which is linear, so sources
superpose exactly as vortices did. A single source contributes $e^{ikr}/\sqrt{r}$ in two dimensions.

- A **rigid** surface requires zero normal velocity. The image has the *same* sign, and the two arrive in
  phase at the boundary, so the pressure there is **doubled**. This is the acoustic analogue of the wall in
  the vortex demo.
- A **pressure-release** surface — the underside of a water surface, for instance — requires zero pressure.
  The image flips sign, and the two cancel exactly on the boundary.

Toggle between them with the source held fixed. Every lobe becomes a null and every null becomes a lobe,
because the far field carries a factor of $2\cos(kh\sin\psi)$ in the rigid case and $2\sin(kh\sin\psi)$ in
the pressure-release case.

## Where the nulls come from

Those factors are just a two-source interference pattern viewed at elevation angle $\psi$. The path
difference between the direct and reflected rays is $2h\sin\psi$, so the rigid surface cancels whenever that
difference is an odd number of half wavelengths:

$$ \sin\psi = \dfrac{(2n+1)\lambda}{4h} $$

Turn on **Predicted null directions** and those angles are drawn as dashed rays straight from the formula.
They fall exactly on the dark bands the demo computes pixel by pixel — two independent routes to the same
answer, which is a satisfying thing to be able to show rather than assert.

The practical reading: raising the source, or shortening the wavelength, packs more lobes into the same
space. A microphone at fixed height can sit in a peak at one frequency and a null at another, which is why
ground reflection is a persistent nuisance in outdoor acoustic measurement and why measurement standards are
so specific about microphone heights.

## Two sources, and steering

Add a second source and the pattern acquires a factor from the array itself. Feeding the two elements with a
phase difference $\Delta\phi$ swings the main lobe to

$$ \cos\psi = -\dfrac{\Delta\phi}{kd} $$

without moving anything physically. That is the entire principle behind phased arrays, from radar to
beamforming microphone arrays used to localise noise sources on aircraft in flyover tests. The *main lobe*
readout tracks the formula as you drag the phase slider.

## Things to try

- Set a rigid surface and sweep the height. Count the lobes as $h/\lambda$ grows — a new one appears every
  half wavelength.
- Switch between rigid and pressure-release at fixed geometry and watch the pattern invert. Look at the
  surface itself: pressure doubles on one, vanishes on the other.
- Turn on the predicted nulls and change the wavelength. The dashed rays and the computed dark bands move
  together; if they ever disagreed, one of the two calculations would be wrong.
- With two sources, set the separation near a wavelength and sweep the phase. Watch the main lobe swing and
  grating lobes appear once $d > \lambda/2$ — the same aliasing constraint that governs sensor spacing in
  any array.
