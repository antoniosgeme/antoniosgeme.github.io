---
permalink: /
title: "About me"
#excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Greetings! I am a PhD Candidate in the Department of Aerospace Engineering at the University of Maryland, where I'm fortunate to conduct research under the guidance of [Dr. Anya Jones](https://aero.umd.edu/clark/faculty/40/Anya-R-Jones) in the [Separated and Transient Aerodynamics Laboratory (STAL)](http://stal.umd.edu/). My research revolves around the realms of unsteady aerodynamics, control theory, and optimization and is primarily aimed at addressing challenges in the aerospace engineering and renewable energy sectors. 

Nowadays, you can find me in the lab doing experiments in a water tank or wind tunnel facility. Previously, I earned a Bachelor's in mechanical engineering from New York University and a Master's in aeronautical engineering from the University of Cambridge. 




<div id="button-container" style="display: flex; justify-content: flex-end; margin-bottom: 10px;">
  <div id="observablehq-AirfoilButton-1cd9a08a" style="display: inline-block;"></div>
  <div id="observablehq-KuttaButton-1cd9a08a" style="display: inline-block; margin-left: 10px;"></div>
</div>

<div id="plot-options-container" style="display: flex; align-items: flex-start;">
  <div id="plot-container" style="flex: 1;">
    <div id="observablehq-viewof-gl-1cd9a08a"></div>
    <div id="observablehq-viewof-options-1cd9a08a"></div>
  </div>
  <div id="options-container" style="flex: 1; margin-left: 10px;"> 
    <div id="observablehq-viewof-flowSelection-1cd9a08a"></div>
    <div id="observablehq-viewof-alpha_deg-1cd9a08a"></div>
    <div id="observablehq-viewof-U-1cd9a08a"></div>
    <div id="observablehq-viewof-Gamma-1cd9a08a"></div>
    <div id="observablehq-viewof-Kappa-1cd9a08a"></div>
    <div id="observablehq-viewof-shift-1cd9a08a"></div>
    <div id="observablehq-viewof-shift_vertical-1cd9a08a"></div>
  </div>
</div>


<style>
    #wrapper {
      /* Add height to ensure there's enough scrollable content */
      height: 1000px; /* You can adjust this height as needed */
    }

    #plot-options-container {
      display: flex;
      align-items: flex-start;
      position: static;
      top: 0; /* Stick to the top of the viewport */
      background-color: white; /* Adjust the background color as needed */
      z-index: 1; /* Add z-index to ensure it appears above other content */
    }

    #plot-container {
      flex: 1;
    }

    #options-container {
      flex: 1;
      margin-left: 10px;
    }
    
  </style>



<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@observablehq/inspector@5/dist/inspector.css">
<script type="module">
import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@5/dist/runtime.js";
import define from "https://api.observablehq.com/d/6a13ba7040fa6e52.js?v=4";
new Runtime().module(define, name => {
  if (name === "viewof gl") return new Inspector(document.querySelector("#observablehq-viewof-gl-1cd9a08a"));
  if (name === "viewof flowSelection") return new Inspector(document.querySelector("#observablehq-viewof-flowSelection-1cd9a08a"));
  if (name === "viewof alpha_deg") return new Inspector(document.querySelector("#observablehq-viewof-alpha_deg-1cd9a08a"));
  if (name === "viewof U") return new Inspector(document.querySelector("#observablehq-viewof-U-1cd9a08a"));
  if (name === "viewof Gamma") return new Inspector(document.querySelector("#observablehq-viewof-Gamma-1cd9a08a"));
  if (name === "viewof Kappa") return new Inspector(document.querySelector("#observablehq-viewof-Kappa-1cd9a08a"));
  if (name === "viewof shift") return new Inspector(document.querySelector("#observablehq-viewof-shift-1cd9a08a"));
  if (name === "viewof shift_vertical") return new Inspector(document.querySelector("#observablehq-viewof-shift_vertical-1cd9a08a"));
  if (name === "viewof options") return new Inspector(document.querySelector("#observablehq-viewof-options-1cd9a08a"));
  if (name === "KuttaButton") return new Inspector(document.querySelector("#observablehq-KuttaButton-1cd9a08a"));
  if (name === "AirfoilButton") return new Inspector(document.querySelector("#observablehq-AirfoilButton-1cd9a08a"));
  return ["programInfo","render","executeMultipleFunctions","values","radius","x_te","Kutta_circulation","initialGrid","beta","values_uniform","values_vortex","values_doublet","grid","values_uniform_doublet","values_uniform_vortex","values_uniform_vortex_doublet","values_vortex_doublet","AirfoilButtonList","alpha","transform","body"].includes(name);
});
</script>



<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@observablehq/inspector@5/dist/inspector.css">
<script type="module">
import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@5/dist/runtime.js";
import define from "https://api.observablehq.com/d/6a13ba7040fa6e52@1629.js?v=4";
new Runtime().module(define, name => {
  if (name === "viewof gl") return new Inspector(document.querySelector("#observablehq-viewof-gl-7ed5cdb3"));
  if (name === "viewof flowSelection") return new Inspector(document.querySelector("#observablehq-viewof-flowSelection-7ed5cdb3"));
  if (name === "viewof alpha_deg") return new Inspector(document.querySelector("#observablehq-viewof-alpha_deg-7ed5cdb3"));
  if (name === "viewof U") return new Inspector(document.querySelector("#observablehq-viewof-U-7ed5cdb3"));
  if (name === "viewof Gamma") return new Inspector(document.querySelector("#observablehq-viewof-Gamma-7ed5cdb3"));
  if (name === "viewof Kappa") return new Inspector(document.querySelector("#observablehq-viewof-Kappa-7ed5cdb3"));
  if (name === "viewof shift") return new Inspector(document.querySelector("#observablehq-viewof-shift-7ed5cdb3"));
  if (name === "viewof shift_vertical") return new Inspector(document.querySelector("#observablehq-viewof-shift_vertical-7ed5cdb3"));
  if (name === "viewof transform") return new Inspector(document.querySelector("#observablehq-viewof-transform-7ed5cdb3"));
  if (name === "viewof body") return new Inspector(document.querySelector("#observablehq-viewof-body-7ed5cdb3"));
  return ["programInfo","render","values","radius","initialGrid","values_uniform","values_vortex","values_doublet","grid","values_uniform_doublet","values_uniform_vortex","values_uniform_vortex_doublet","values_vortex_doublet","alpha"].includes(name);
});
</script>









