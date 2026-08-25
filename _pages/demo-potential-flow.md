---
layout: single
title: "Potential Flows and Conformal Maps"
permalink: /teaching/potential-flow/
author_profile: true
redirect_from:
  - /posts/2023/11/blog-post-1/
---

The goal here is to gain some familiarity and visual intuition of how conformal maps work and how they are
used in the theory of aerodynamics. The flows are rendered per pixel with WebGL, directly in the page below.

{% include demo.html src="/assets/demos/potential-flow.html" title="Potential flow and conformal map sandbox" %}

## Potential Flow

We will focus on fluid flows whose velocity fields can be written as gradients of scalar potentials,
$\mathbf{u} = \nabla \phi$. Conservation of mass for incompressible fluids, $\nabla \cdot \mathbf{u}= 0$
implies that the scalar potential satisfies Laplace's equation $\nabla^2 \phi = 0$. Thus, we can create
potential flows using solutions of Laplace's equation, called
[harmonic functions](https://en.wikipedia.org/wiki/Harmonic_function), and which are mathematically well
understood. Harmonic functions are also linearly superimposable, meaning that their linear combinations are
also valid solutions to Laplace's equations. We will exploit this fact to create flows which are relevant to
the theory of aerodynamics, using three fundamental building blocks: 1) the **uniform flow**, 2) the
**point vortex flow**, 3) and the **doublet flow**. A uniform flow is characterized by its freestream
velocity, $U_{\infty}$, and its flow angle, $\alpha$. A point vortex flow is characterized by its
circulation, $\Gamma$, and a doublet flow is characterized by its doublet strength, $\kappa$, and (for
simplicity) the same flow angle, $\alpha$. The complex velocity induced by each of these flows are,

$$
\begin{equation}
W_{U} = U_{\infty} e^{-i\alpha} \;\;\;\;\;\;\;\;
W_{V} = \frac{i \Gamma}{2\pi \zeta} \;\;\;\;\;\;\;\;
W_{D} = -\frac{\kappa}{\zeta^2}e^{i\alpha}
\end{equation}
$$

where $\zeta \in \mathbb{C}$ is the position in complex space. The interactive plot above plots the
streamlines as well as the pressure field induced by each of the above flows. The **Components** checkboxes
allow us to toggle each flow on and off, so any linear combination is available. For example, ticking
**Uniform stream** and **Vortex** plots $W_{U} + W_{V}$. The coefficients $U_\infty,\alpha,\Gamma,\kappa$ can
be adjusted using the sliders next to the plot. I encourage you to play around with the settings we
discussed so far and see how they change the flow pattern.

## Flow Over a Cylinder

An interesting flow arises when we add the **Uniform stream** and **Doublet**. You might have noticed that
one of the streamlines for this flow forms a closed circle which varies in size as the freestream velocity
and doublet strength change. By definition, the flow velocity is parallel to a streamline and never
perpendicular to it. This implies that a closed streamline divides the flow into two regions that cannot
communicate. That is, the fluid must flow around that circular streamline and not through it. This is the
identical effect that a solid body would have if immersed in a potential flow. We can consider that
streamline to be the boundary of a cylindrical solid body whose radius we can compute analytically as a
function of the flow variables. The radius ends up being $a = \sqrt{\frac{\kappa}{U_\infty}}$, which is what
the *radius a* readout tracks. We can then visualize the body by shading in the flow inside the streamline.
Checking the option **Fill body** under the plot does just that. Remember, this does not change the flow at
all. It just helps us see the boundary between the flow inside and outside the dividing streamline.

An important characteristic of this flow is that we can add a vortex of any strength, $\Gamma$, at the
center of the circle without violating this boundary condition. We can see this by ticking **Vortex** as
well and moving the $\Gamma$ slider. While the streamlines change quite a bit, they never cross the boundary
of the circle. Mathematically, this means that the solution to this problem is *non-unique*, or that there
are several (in this case infinite) valid solutions.

## Conformal Maps

Perhaps the most powerful idea in the theory of potential flows is that of a conformal map. Conformal maps
allow us to transform solutions of simple problems to solutions of difficult problems. For example, there
exists conformal maps that can take the solution for the flow over the cylinder shown above, to the flow
over a body of **any** shape. A conformal map of interest to the theory of aerodynamics is the *Joukowsky
transform*. This transform takes the flow over a cylinder and maps it to the flow over some very reasonable
looking airfoils! The transform is defined as,

$$
\begin{equation}
  z = \zeta + \frac{1}{\zeta}
\end{equation}
$$

The map takes every point in the complex $\zeta$-plane to a point in the a new complex z-plane. Checking the
option **Joukowski transform** applies the transform to the visualization. While the transform does some
interesting stuff to each of the flows, the body never quite looks like an airfoil. To get an airfoil shape
we need to move the center of the circle away from the origin and apply the same transform. The sliders
**Center $x_0$** and **Center $y_0$** do just that. You can play around with the settings until you have
something that looks like an airfoil, or you can just press the **Cambered airfoil** button. I encourage you
to fiddle around with how each of the parameters changes the shape of the airfoil or the characteristics of
the flow around it. For example, changing **Center $y_0$** adjusts the camber distribution of the airfoil,
while **Center $x_0$** adjusts the thickness distribution.

*One implementation note:* the visualization uses the slightly more general form $z = \zeta + b^2/\zeta$ and
picks $b$ so that the circle always passes exactly through it. That is why the trailing edge here is always
sharp, and why the *TE point b* readout moves as you drag the centre around.

## The Kutta Condition

Conformal maps guarantee that the flow will not cross through the body's surface, so long as the flow does
not cross the pre-transformed body's surface. Hence, the flow over the airfoil inherits the non-uniqueness
of the flow over the circular cylinder. This means that we can set the circulation, $\Gamma$ to any value
without affecting correctness of the solution. A natural question to ask is what is the "physical"
circulation value, or the one that would occur in practice? One reason this is important is because the
[Kutta-Joukowski theorem](https://en.wikipedia.org/wiki/Kutta%E2%80%93Joukowski_theorem) tells us that the
lift produced by the airfoil is proportional to its circulation, $L = \rho U_\infty \Gamma$. How can we
determine the physically occurring circulation? The answer is provided by the *Kutta condition*, which
states the circulation must be such so that the flow leaves the trailing edge of the airfoil *smoothly*. The
circulation necessitated by the Kutta condition is,

$$
\begin{equation}
  \Gamma = 4 \pi a U_\infty \mathrm{sin}(\alpha + \beta)
\end{equation}
$$

We have previously defined all of these parameters except $\beta$, which is the angle of the line connecting
the center of the circular cylinder with the cylinder's x-intercept, and is effectively a function of
airfoil's camber. Pressing the **Apply Kutta condition** button sets the circulation to the correct value.
We can visually confirm that flow indeed leaves the trailing edge smoothly. We can then change the flow
parameters and reapply the Kutta condition. We have now covered each of the options/buttons of the
calculator.

---

*An earlier version of this page built the visualization as an [ObservableHQ](https://observablehq.com/)
notebook, following the approaches of
[Ricky Reusser](https://observablehq.com/@rreusser/adaptive-domain-coloring) and
[Graham Pullan](https://observablehq.com/@grahampullan/joukowski-airfoils). The visualization above is a
standalone rewrite with no notebook runtime behind it, but the debt to both is unchanged.*
