---
permalink: /
title: "About me"
#excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Greetings! I am a PhD Candidate in the Department of Aerospace Engineering at the University of Maryland, conducting research under the guidance of [Dr. Anya Jones](https://aero.umd.edu/clark/faculty/40/Anya-R-Jones) in the [Separated and Transient Aerodynamics Laboratory (STAL)](http://stal.umd.edu/). My research revolves around the realms of unsteady aerodynamics, control theory, and optimization and is primarily aimed at addressing challenges in the aerospace engineering and renewable energy sectors. If you would like to see some of my current and past projects, please visit my [Portfolio page](/gallery)

Nowadays, I spend most of my time in the lab doing experiments in a water tank or wind tunnel facility, or developing low-fidelity aerodynamics analysis and optimization tools. Previously, I earned a Master's in aeronautical engineering from the University of Cambridge and a Bachelor's in mechanical engineering from New York University. 

<div id="kutta-button-container" style="display: flex; justify-content: center;">
  <div id="observablehq-KuttaButton-a125070b" style="margin-bottom: 10px; margin-left: 20px;"></div>
</div>

<div id="plot-options-container">
  <div id="plot-container">
    <div id="observablehq-viewof-gl-a125070b"></div>
    <div id="observablehq-viewof-options-a125070b"></div>
  </div>
  <div id="options-container"> 
    <div id="observablehq-viewof-flowSelection-a125070b"></div>
    <div id="observablehq-viewof-alpha_deg-a125070b"></div>
    <div id="observablehq-viewof-U-a125070b"></div>
    <div id="observablehq-viewof-Gamma-a125070b"></div>
    <div id="observablehq-viewof-Kappa-a125070b"></div>
    <div id="observablehq-viewof-shift-a125070b"></div>
    <div id="observablehq-viewof-shift_vertical-a125070b"></div>
  </div>
</div>

<style>
  #wrapper {
    height: 1000px;
  }

  #plot-options-container {
    display: flex;
    align-items: flex-start;
    position: static;
    top: 0;
    background-color: white;
    z-index: 1;
  }

  #plot-container {
    flex: 1;
  }

  #options-container {
    flex: 1;
    margin-left: 10px;
  }

  /* Media query for mobile devices */
  @media (max-width: 768px) {
    #plot-options-container {
      flex-direction: column;
    }

    #options-container {
      margin-left: 0;
      margin-top: 10px;
    }

    #plot-container {
      position: sticky;
      top: 0;
      z-index: 2;
      background-color: white;
    }
  }

  #kutta-button-container {
    display: flex;
    justify-content: center;
    margin-bottom: 10px;
    width: 100%;
  }
</style>




<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@observablehq/inspector@5/dist/inspector.css">
<script type="module">
import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@5/dist/runtime.js";
import define from "https://api.observablehq.com/d/6a13ba7040fa6e52@2064.js?v=4";
new Runtime().module(define, name => {
  if (name === "viewof gl") return new Inspector(document.querySelector("#observablehq-viewof-gl-a125070b"));
  if (name === "viewof flowSelection") return new Inspector(document.querySelector("#observablehq-viewof-flowSelection-a125070b"));
  if (name === "viewof alpha_deg") return new Inspector(document.querySelector("#observablehq-viewof-alpha_deg-a125070b"));
  if (name === "viewof U") return new Inspector(document.querySelector("#observablehq-viewof-U-a125070b"));
  if (name === "viewof Gamma") return new Inspector(document.querySelector("#observablehq-viewof-Gamma-a125070b"));
  if (name === "viewof Kappa") return new Inspector(document.querySelector("#observablehq-viewof-Kappa-a125070b"));
  if (name === "viewof shift") return new Inspector(document.querySelector("#observablehq-viewof-shift-a125070b"));
  if (name === "viewof shift_vertical") return new Inspector(document.querySelector("#observablehq-viewof-shift_vertical-a125070b"));
  if (name === "viewof options") return new Inspector(document.querySelector("#observablehq-viewof-options-a125070b"));
  if (name === "KuttaButton") return new Inspector(document.querySelector("#observablehq-KuttaButton-a125070b"));
  return ["programInfo","render","executeMultipleFunctions","values","radius","AirfoilButton","x_te","Kutta_circulation","initialGrid","beta","values_uniform","values_vortex","values_doublet","grid","values_uniform_doublet","values_uniform_vortex","values_uniform_vortex_doublet","values_vortex_doublet","AirfoilButtonList","alpha","transform","body"].includes(name);
});
</script>