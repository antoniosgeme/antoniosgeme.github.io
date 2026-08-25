---
layout: single
title: "Spectral leakage: why your quiet tone disappeared"
permalink: /teaching/spectral-leakage/
author_profile: true
---

Anyone who has taken a Fourier transform of an unsteady pressure record has been bitten by this, usually
without noticing. A strong tone at one frequency can manufacture apparent energy at every other frequency,
and bury a real signal forty decibels below it. The cause is not noise, and it is not the sensor.

{% include demo.html src="/assets/demos/spectral-leakage.html" title="Windowing and spectral leakage" %}

## The transform believes your record repeats

A discrete Fourier transform does not analyse the finite record you handed it. It analyses the infinite
periodic signal built by laying that record end to end forever. If the tone completes a whole number of
cycles within the record, the joins are seamless and the transform is clean — all the energy lands in one
bin.

Move the frequency off a bin centre and the record's last sample no longer flows into its first. The
periodic extension has a discontinuity at every seam, and a discontinuity is broadband. That is what leaks.

Slide the **offset** control from 0 to 0.5 with a rectangular window and watch a single clean spike spread
into skirts spanning the entire band. Nothing about the signal changed; only its relationship to the bin
grid did.

## A window is a gentler ending

The fix is to taper the record so that it begins and ends near zero, removing the discontinuity before it
can radiate. Multiplying by a window $w[n]$ in time is convolution in frequency, so the price is that every
spectral line is smeared by the window's own transform. That transform has a **main lobe**, which sets how
finely you can resolve two nearby tones, and **sidelobes**, which set how far a strong tone can reach.

Every window is a position on that trade, and there is no way off it:

| Window | Peak sidelobe | Main lobe |
|---|---|---|
| Rectangular | &minus;13.3 dB | 2 bins |
| Hann | &minus;31.5 dB | 4 bins |
| Hamming | &minus;42.7 dB | 4 bins |
| Blackman | &minus;58.1 dB | 6 bins |
| Blackman-Harris | &minus;92.0 dB | 8 bins |
| Flat-top | &minus;93.0 dB | 10 bins |

The dashed line drawn across the spectrum is the measured peak sidelobe for the window in use, computed from
its own transform rather than looked up — it agrees with the published figures above to a tenth of a decibel.

## The failure this actually causes

Turn on the weak neighbour, set it to &minus;50 dB and the offset to 0.5, and choose the rectangular window.
The second tone is gone. Not attenuated — invisible, sitting well below the leakage skirt of its loud
neighbour. A red dashed marker shows where it really is.

Now switch to Blackman. It reappears as a clean peak exactly on the marker.

This is the everyday hazard in unsteady aerodynamic data. Tunnel background, a blade passing frequency, or a
resonance in the mounting can each be tens of decibels above the fluctuation you care about, and with no
window at all their leakage will simply swallow it. The instinct to reach for a raw FFT is the instinct to
be lied to.

## Choosing one

- **Hann** is the sensible default for general spectral work: cheap, well behaved, and enough sidelobe
  rejection for most purposes.
- **Blackman-Harris** when a weak feature sits near a strong one and dynamic range matters more than
  resolving them precisely.
- **Flat-top** when you need an accurate *amplitude* rather than an accurate frequency. Its main lobe is
  deliberately broad and flat so that a tone anywhere between bins still reads the correct height — the
  right choice for calibration, the wrong one for resolving anything.
- **Rectangular** only when the signal is genuinely periodic in the record, which in practice means a
  synchronously sampled or carefully tuned experiment.

## Things to try

- Set the offset to exactly 0 with a rectangular window. The spectrum is a single clean line, because the
  record happens to be periodic. Nudge the offset to 0.05 and watch that collapse.
- Compare the *coherent gain* readout across windows. Hann reads 0.5, so a windowed amplitude must be
  doubled to recover the true one — a correction it is very easy to forget.
- Put the weak tone only 4 bins away and raise it to &minus;20 dB. Now the wide-main-lobe windows fail
  instead, merging the two peaks. The trade runs in both directions.
- Shorten the record to 128 samples. Every bin gets wider, so both resolution and leakage worsen together.
