---
permalink: /
title: "About me"
#excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a Postdoctoral Associate at the University of Maryland's [High-Speed Aerodynamics and Propulsion Laboratory (HAPL)](http://www.hyper.umd.edu/index.html). I recently completed my PhD in Aerospace Engineering at the University of Maryland under the guidance of [Dr. Anya Jones](https://stal.seas.ucla.edu/). My research examines the fluid-mechanical phenomena that underpin the performance and design of next-generation flight and energy systems. Broadly, my work explores fundamental questions in unsteady aerodynamics and vorticity-dominated flows, high-speed turbulent boundary layer physics, and the interplay between aerodynamics, sensing, and control.

**Education:**
- **Ph.D. Aerospace Engineering**, University of Maryland (2025)
- **M.Res. Aeronautical Engineering**, University of Cambridge (2019)
- **B.S. Mechanical Engineering**, New York University (2018)

---

<section class="gallery-section" id="gallery">
  <h3>Gallery</h3>

  <!-- Hero video (optional) -->
  <div class="gallery-hero">
    <video autoplay muted loop playsinline>
      <source src="/images/gallery/GustEncounter.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
  <!-- Two-per-row image grid -->
  <div class="gallery-grid">
    <figure class="card">
      <img class="media" src="/images/gallery/Bubble.jpg" alt="Bubble flow dynamics" loading="lazy">
      <figcaption>Smoke visualization of bubble burst</figcaption>
    </figure>
    <figure class="card">
      <img class="media" src="/images/gallery/IMG_9883.jpg" alt="Experimental setup" loading="lazy">
      <figcaption>Particle Tracking Velocimetry</figcaption>
    </figure>
    <figure class="card">
      <img class="media" src="/images/gallery/breakdown.png" alt="Breakdown visualization" loading="lazy">
      <figcaption>Bubble breakdown pathlines</figcaption>
    </figure>
    <figure class="card">
      <video class="media" autoplay muted loop playsinline>
        <source src="/images/gallery/temperature_field_web.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>IR Thermography</figcaption>
    </figure>
    <figure class="card">
      <img class="media" src="/images/gallery/PEEKcone.jpg" alt="Hypersonic test model (PEEK cone)" loading="lazy">
      <figcaption>Cone-flare hypersonics model</figcaption>
    </figure>
    <figure class="card">
      <img class="media" src="/images/gallery/dark_wing_high_res.jpg" alt="High-resolution wing model" loading="lazy">
      <figcaption>Instrumented wing model</figcaption>
    </figure>
    <figure class="card">
      <img class="media" src="/images/gallery/IMG_4002.jpg" alt="Laboratory instrumentation" loading="lazy">
      <figcaption>PIV during a gust encounter</figcaption>
    </figure>
    <figure class="card">
      <img class="media" src="/images/gallery/IMG_7257.jpg" alt="Research facility" loading="lazy">
      <figcaption>PIV of bubble burst breakdown</figcaption>
    </figure>
    <!-- Optional extras
    <figure class="card">
      <img class="media" src="/images/gallery/Temps.png" alt="IR thermography capabilities" loading="lazy">
      <figcaption>IR thermography capabilities</figcaption>
    </figure>
    <figure class="card">
      <img class="media" src="/images/gallery/Schileren2.gif" alt="Schlieren flow visualization" loading="lazy">
      <figcaption>Schlieren flow visualization</figcaption>
    </figure>
    -->
  </div>
</section>


---

<style>
.gallery-section{
  background:#fff;border:1px solid #e1e5e9;border-left:4px solid #3498db;
  border-radius:12px;padding:24px;margin:32px 0
}
.gallery-section h3{margin:0 0 20px;text-align:center;color:#2c3e50;font-size:1.35rem}
.gallery-hero{display:grid;place-items:center;margin-bottom:22px}
.gallery-hero video{width:100%;max-width:780px;border-radius:10px;box-shadow:0 4px 12px rgba(0,0,0,.12)}
.gallery-grid{
  display:grid;grid-template-columns:repeat(2,1fr);gap:18px
}
/* Uniform tiles */
.card{background:#fff;border:1px solid #eef1f4;border-radius:10px;overflow:hidden;box-shadow:0 3px 10px rgba(0,0,0,.08)}
.card .media{width:100%;aspect-ratio:4/3;display:block}
.card img.media{object-fit:cover}
.card video.media{object-fit:cover;background:transparent}
.card figcaption{font-size:.9rem;color:#606b78;text-align:center;padding:10px 12px}
/* Keep 2 per row even on smaller screens; drop to 1 only when extremely narrow */
@media (max-width:520px){
  .gallery-grid{grid-template-columns:1fr}
}
</style>

