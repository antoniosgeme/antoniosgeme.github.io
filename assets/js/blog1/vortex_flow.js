let arrowImage; // Variable to hold the arrow SVG image

function preload() {
  // Load the SVG file during preload
  arrowImage = loadImage('arrowup.svg');
}

function setup() {
  createCanvas(200, 200);
  background(255);

  const gamma = 10; // Strength of the vortex
  const centerX = width / 2; // X-coordinate of the center of the doublet
  const centerY = height / 2; // Y-coordinate of the center of the doublet

  for (let x = 0; x < width; x += 10) {
    for (let y = 0; y < height; y += 10) {
      const result = vortexFlowMagnitudeAndAngle(x, y, gamma, centerX, centerY);
      drawVector(x, y, result.magnitude, result.angle-PI/2);
    }
  }
}

function drawVector(x, y, magnitude, angle) {
  const arrowSize = 10; // Adjust arrow size as needed
  const vx = magnitude * cos(angle);
  const vy = magnitude * sin(angle);

  push();
  translate(x + vx, y + vy);
  rotate(angle);

  // Draw the arrow image at the end of the line
  image(arrowImage, -arrowSize / 2, -arrowSize / 2, arrowSize, arrowSize);

  pop();
}


  function vortexFlowMagnitudeAndAngle(x, y, gamma, centerX, centerY) {
    const dx = x-centerX
    const dy = y-centerY
    const r2 = dx*dx+dy*dy
  
    const U = gamma/(2*PI)*dy/r2
    const V = -gamma/(2*PI)*dx/r2

    magnitude = sqrt(U*U+V*V)
    angle = atan2(V,U)
  
    return { magnitude: V, angle: angle}; 
  }