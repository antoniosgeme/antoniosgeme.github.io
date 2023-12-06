document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.getElementById('webglCanvas');
    const gl = canvas.getContext('webgl');
    if (!gl) {
        alert('WebGL is not supported in your browser.');
        return;
    }

    let sliderValue = 50; // Initial slider value
    const slider = document.getElementById('mySlider');
    slider.addEventListener('input', function () {
        sliderValue = parseInt(this.value);
        updateVectorField();
    });

    let vectors = []; // Placeholder for vector field data

    // Initialize WebGL program
    const vertexShaderSource = `
        attribute vec2 a_position;
        void main() {
            gl_PointSize = 2.0; // Set the point size for vectors
            gl_Position = vec4(a_position, 0.0, 1.0);
        }
    `;

    const fragmentShaderSource = `
        precision mediump float;
        void main() {
            gl_FragColor = vec4(0.0, 0.0, 0.0, 1.0); // Black color for vectors
        }
    `;

    const vertexShader = createShader(gl, gl.VERTEX_SHADER, vertexShaderSource);
    const fragmentShader = createShader(gl, gl.FRAGMENT_SHADER, fragmentShaderSource);

    const program = gl.createProgram();
    gl.attachShader(program, vertexShader);
    gl.attachShader(program, fragmentShader);
    gl.linkProgram(program);
    gl.useProgram(program);

    const positionAttributeLocation = gl.getAttribLocation(program, 'a_position');
    const positionBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);

    const sliderUniformLocation = gl.getUniformLocation(program, 'u_slider');

    function createShader(gl, type, source) {
        const shader = gl.createShader(type);
        gl.shaderSource(shader, source);
        gl.compileShader(shader);
        if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
            console.error('Error compiling shader:', gl.getShaderInfoLog(shader));
            gl.deleteShader(shader);
            return null;
        }
        return shader;
    }

    function updateVectorField() {
        // Compute your vector field based on the slider value
        // Update the 'vectors' array with new data
        // For example:
        vectors = []; // Update 'vectors' array with your computed data

        // Constants for the flow (you can adjust these values)
        let U = 1; // Uniform flow velocity
        let K = 1; // Doublet strength
        let Gamma = 2; // Vortex strength
        let z = createComplexArray();
        W = computeComplexVelocity(z, U, K, Gamma) 
        vectors.push(W)
        //for (let i = 0; i < 100; i++) {
            //vectors.push(Math.random() * 2 - 1, Math.random() * 2 - 1); // Example random vectors
        //}

        // Update the WebGL buffer with the new vector field data
        gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vectors), gl.STATIC_DRAW);

        // Draw the updated vector field
        draw();
    }

    function draw() {
        gl.clearColor(1.0, 1.0, 1.0, 1.0);
        gl.clear(gl.COLOR_BUFFER_BIT);

        gl.useProgram(program);
        gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
        gl.vertexAttribPointer(positionAttributeLocation, 2, gl.FLOAT, false, 0, 0);
        gl.enableVertexAttribArray(positionAttributeLocation);

        gl.uniform1f(sliderUniformLocation, sliderValue);

        gl.drawArrays(gl.POINTS, 0, vectors.length / 2); // Draw vectors as points
    }

    // Initial vector field visualization
    updateVectorField();
});


// Include math.js library
// <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/9.5.0/math.js"></script>

// Function to create a complex number using math.js
function createComplexNumber(real, imaginary) {
    return math.complex(real, imaginary);
}

// Create an array of complex numbers with a range of real and imaginary parts
function createComplexArray() {
    let complexArray = [];
    const minReal = -5;
    const maxReal = 5;
    const minImaginary = -5;
    const maxImaginary = 5;

    for (let real = minReal; real <= maxReal; real++) {
        for (let imaginary = minImaginary; imaginary <= maxImaginary; imaginary++) {
            let complexNumber = createComplexNumber(real, imaginary);
            complexArray.push(complexNumber);
        }
    }

    return complexArray;
}



function computeComplexVelocity(z, U, K, Gamma) {
    let uniformFlowTerm = math.multiply(U, z); // Uniform flow term: U * z
    let doubletTerm = math.divide(K, math.multiply(z, z)); // Doublet term: K / (z * z)
    let vortexTerm = math.multiply(math.divide(Gamma, math.multiply(2 * Math.PI, math.i)), math.inv(z)); // Vortex term: (Gamma / (2 * π * i)) / z

    return math.add(math.add(uniformFlowTerm, doubletTerm), vortexTerm); // Summing up all terms
}
