let arrowImage; // Variable to hold the arrow SVG image

function preload() {
  // Load the SVG file during preload
  arrowImage = loadImage('arrowup.svg');
}

function setup() {
  createCanvas(200, 200);
  background(255);

  const centerX = width / 2; // X-coordinate of the center of the doublet
  const centerY = height / 2; // Y-coordinate of the center of the doublet

  for (let x = 0; x < width; x += 10) {
    for (let y = 0; y < height; y += 10) {
      
      drawVector(x, y, 1, PI/2);
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