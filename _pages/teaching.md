---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
---

<p class="teaching-lede">
Material I have built and used to teach aerodynamics, and the mathematics underneath it. Each one runs in a
browser with nothing to install, and each is a single self-contained HTML file &mdash; small enough to email
to a student, drop into a lecture, or hand over for them to take apart. I write these when a concept is
easier to manipulate than to describe: the Kutta condition is a sentence in a textbook and an afternoon of
confusion at the blackboard, but it is obvious the moment you can watch the trailing-edge singularity
disappear as you dial in the circulation.
</p>

<h2 class="sec">Incompressible aerodynamics</h2>

<div class="demo-grid">
  <a class="demo-card" href="/teaching/potential-flow/">
    <span class="demo-card__topic">Potential flow &middot; conformal mapping</span>
    <h3>Building a wing out of nothing</h3>
    <p>
      Add a uniform stream, a vortex and a doublet and a cylinder appears on its own &mdash; no boundary was
      ever imposed. Map the circle to an airfoil, then apply the Kutta condition and watch it pick the one
      circulation nature allows.
    </p>
  </a>

  <a class="demo-card" href="/teaching/method-of-images/">
    <span class="demo-card__topic">Boundary conditions &middot; ground effect</span>
    <h3>The method of images</h3>
    <p>
      A wall is a mirror. Place the reflected vortex and the boundary can be deleted outright &mdash; the
      demo lets you remove it and see that nothing above the line changes. A cylinder needs two images, and
      the circle theorem says where.
    </p>
  </a>

  <a class="demo-card" href="/posts/2023/11/blog-post-1/">
    <span class="demo-card__topic">Complex analysis &middot; WebGL</span>
    <h3>Potential flows and conformal maps</h3>
    <p>
      A longer written walkthrough of the same territory, building the visualisation from scratch: uniform
      flow, vortices, doublets, flow over a cylinder, the Joukowski transform and the Kutta condition.
    </p>
  </a>
</div>

<h2 class="sec">Compressible flow</h2>

<div class="demo-grid">
  <a class="demo-card" href="/teaching/shock-angles/">
    <span class="demo-card__topic">Supersonic flow &middot; shock relations</span>
    <h3>Mach cones and oblique shocks</h3>
    <p>
      Watch a source outrun its own sound until the wavefronts acquire a common tangent, then put a wedge in
      that flow and steepen the cone into a shock. Includes a live &theta;&ndash;&beta;&ndash;M diagram, both
      solution branches, and the detachment limit.
    </p>
  </a>

  <a class="demo-card" href="/teaching/falkner-skan/">
    <span class="demo-card__topic">Boundary layers &middot; separation</span>
    <h3>Pressure gradient and the shape of a boundary layer</h3>
    <p>
      One parameter carries you from stagnation-point flow to the exact point of separation. The profile is
      solved live by shooting, so you can watch the inflection point emerge and the wall shear fall to zero.
    </p>
  </a>
</div>

<h2 class="sec">Waves and measurement</h2>

<div class="demo-grid">
  <a class="demo-card" href="/teaching/sound-over-ground/">
    <span class="demo-card__topic">Acoustics &middot; interference</span>
    <h3>Sound over ground</h3>
    <p>
      The method of images again, in wave form. A rigid surface takes an in-phase image and doubles the
      pressure on it; a pressure-release surface takes the opposite. Predicted null directions are drawn
      from theory on top of the computed field.
    </p>
  </a>

  <a class="demo-card" href="/teaching/spectral-leakage/">
    <span class="demo-card__topic">Signal processing &middot; experimental data</span>
    <h3>Spectral leakage and windowing</h3>
    <p>
      Why a strong tone can bury a real one forty decibels below it, and what a window actually buys you.
      The everyday hazard in unsteady pressure data, and the reason a raw FFT is rarely the right first move.
    </p>
  </a>
</div>

<p class="teaching-foot">
  All of these are in the <a href="https://github.com/antoniosgeme/antoniosgeme.github.io/tree/master/assets/demos">site repository</a>
  and are free to reuse. If you adapt one for a course I would be glad to hear about it.
</p>

<style>
.teaching-lede{
  font-size:1.05rem;line-height:1.6;color:#34495e;
  background:#fff;border:1px solid #e1e5e9;border-left:4px solid #1f7a8c;
  border-radius:12px;padding:20px 24px;margin:24px 0 32px
}
h2.sec{
  margin:34px 0 4px;color:#2c3e50;font-size:1.15rem;letter-spacing:.02em;
  padding-bottom:8px;border-bottom:1px solid #e1e5e9
}
.demo-grid{
  display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:18px;margin:18px 0 6px
}
/* .archive a is underlined by the theme; outrank it rather than fight with !important */
.archive .demo-card,
.archive .demo-card:hover{text-decoration:none}
.demo-card{
  display:block;background:#fff;border:1px solid #e1e5e9;border-left:4px solid #2c3e50;
  border-radius:12px;padding:20px 22px;color:inherit;
  transition:border-color .14s ease, box-shadow .14s ease
}
.demo-card:hover{border-color:#1f7a8c;border-left-color:#1f7a8c;box-shadow:0 2px 10px rgba(31,122,140,.10)}
.demo-card:focus-visible{outline:2px solid #1f7a8c;outline-offset:2px}
.demo-card__topic{
  display:block;font-size:.72rem;letter-spacing:.09em;text-transform:uppercase;
  color:#1f7a8c;margin-bottom:8px;font-weight:600
}
.demo-card h3{margin:0 0 8px;font-size:1.02rem;color:#2c3e50;line-height:1.35}
.demo-card p{margin:0;font-size:.92rem;line-height:1.55;color:#3a4754}
.teaching-foot{margin-top:30px;font-size:.9rem;color:#5a6875}
</style>
