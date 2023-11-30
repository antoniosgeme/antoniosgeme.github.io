// Variables for wing simulation
let chord;
let wingLength;
let angleOfAttack = 0;
let liftForce = 0;
let dragForce = 0;

function setup() {
  createCanvas(400, 400);
  wingLength = height * 0.6; // Adjust the length of the wing here
  chord = wingLength * 0.1; // Adjust the chord length of the wing here
}

function draw() {
  background(220);
  translate(width / 2, height / 2);

  // Wing representation
  strokeWeight(2);
  line(-wingLength / 2, 0, wingLength / 2, 0);
  line(-wingLength / 2, chord / 2, -wingLength / 2, -chord / 2);
  line(-wingLength / 2, 0, -wingLength / 2 + 10, 0);
  line(wingLength / 2, 0, wingLength / 2 - 10, 0);

  // Airflow visualization
  let airflowSpeed = 50; // Change this value to adjust the speed of airflow
  for (let x = -width / 2; x < width / 2; x += 10) {
    let y1 = 10 * sin(angleOfAttack) * sin(PI * x / wingLength);
    let y2 = 10 * sin(angleOfAttack) * sin(PI * (x + 10) / wingLength);
    line(x, y1, x + 10, y2);
  }

  // Forces calculation (basic potential flow approximation)
  let velocity = airflowSpeed * cos(angleOfAttack);
  liftForce = 0.5 * 1.225 * velocity * velocity * chord * sin(angleOfAttack);
  dragForce = 0.5 * 1.225 * velocity * velocity * chord * cos(angleOfAttack);

  // Display forces
  fill(0);
  text(`Lift: ${liftForce.toFixed(2)} N`, -width / 2 + 10, 20);
  text(`Drag: ${dragForce.toFixed(2)} N`, -width / 2 + 10, 40);
}

function mouseDragged() {
  angleOfAttack = map(mouseX, 0, width, -PI / 6, PI / 6); // Adjust the range of the angle of attack
}
