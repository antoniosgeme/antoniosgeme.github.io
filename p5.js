// p5.js sketch code
let angle = 0;

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  translate(width / 2, height / 2);
  rotate(radians(angle));
  rect(0, 0, 100, 100);
  angle += 1;
}
