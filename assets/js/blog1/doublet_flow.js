let arrowImage; // Variable to hold the arrow SVG image

function preload() {
  // Load the SVG file during preload
  arrowImage = loadImage('arrowup.svg');
}

function setup() {
  createCanvas(200, 200);
  background(255);

  const kappa = 10; // Strength of the doublet
  const centerX = width / 2; // X-coordinate of the center of the doublet
  const centerY = height / 2; // Y-coordinate of the center of the doublet

  for (let x = 0; x < width; x += 10) {
    for (let y = 0; y < height; y += 10) {
      const result = doubletFlowMagnitudeAndAngle(x, y, kappa, centerX, centerY);
      drawVector(x, y, result.magnitude, result.angle);
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

function doubletFlowMagnitudeAndAngle(x, y, kappa, centerX, centerY) {
  const dx = x-centerX
  const dy = y-centerY
  r4 = pow(dx*dx+dy*dy,2)

  const U = kappa/PI*dx*dy/r4
  const V = -kappa/(2*PI)*(dx*dx-dy*dy)/r4
  magnitude = sqrt(U*U+V*V)
  angle = atan2(V,U)

  return { magnitude: V, angle: angle };
}


class Complex {
  constructor(real, imaginary) {
    this.real = real; // Real part of the complex number
    this.imaginary = imaginary; // Imaginary part of the complex number
  }

  // Method to add two complex numbers
  add(otherComplex) {
    return new Complex(this.real + otherComplex.real, this.imaginary + otherComplex.imaginary);
  }

  // Method to subtract two complex numbers
  subtract(otherComplex) {
    return new Complex(this.real - otherComplex.real, this.imaginary - otherComplex.imaginary);
  }

  // Method to multiply two complex numbers
  multiply(otherComplex) {
    const realPart = this.real * otherComplex.real - this.imaginary * otherComplex.imaginary;
    const imaginaryPart = this.real * otherComplex.imaginary + this.imaginary * otherComplex.real;
    return new Complex(realPart, imaginaryPart);
  }

  // Method to divide two complex numbers
  divide(otherComplex) {
    const divisor = otherComplex.real ** 2 + otherComplex.imaginary ** 2;
    const realPart = (this.real * otherComplex.real + this.imaginary * otherComplex.imaginary) / divisor;
    const imaginaryPart = (this.imaginary * otherComplex.real - this.real * otherComplex.imaginary) / divisor;
    return new Complex(realPart, imaginaryPart);
  }

  // Method to square a complex number
  square() {
    return this.multiply(this);
  }

  // Method to calculate square root of a complex number
  squareRoot() {
    const modulus = Math.sqrt(this.real ** 2 + this.imaginary ** 2);
    const realPart = Math.sqrt((modulus + this.real) / 2);
    const imaginaryPart = Math.sign(this.imaginary) * Math.sqrt((modulus - this.real) / 2);
    return new Complex(realPart, imaginaryPart);
  }

  magnitude() {
    return Math.sqrt(this.real ** 2 + this.imaginary ** 2);
  }

  // Method to calculate the phase (argument) of a complex number in radians
  phase() {
    return Math.atan2(this.imaginary, this.real);
  }
}

// Usage example
//const complex1 = new Complex(3, 2); // Create a complex number 3 + 2i
//const complex2 = new Complex(1, 4); // Create a complex number 1 + 4i

//const sum = complex1.add(complex2); // Add two complex numbers
//console.log('Sum:', sum);

//const difference = complex1.subtract(complex2); // Subtract two complex numbers
//console.log('Difference:', difference);

//const product = complex1.multiply(complex2); // Multiply two complex numbers
//console.log('Product:', product);

//const quotient = complex1.divide(complex2); // Divide two complex numbers
//console.log('Quotient:', quotient);

//const squareResult = complex1.square(); // Square a complex number
//console.log('Square:', squareResult);

//const squareRootResult = complex1.squareRoot(); // Square root of a complex number
//console.log('Square Root:', squareRootResult);

