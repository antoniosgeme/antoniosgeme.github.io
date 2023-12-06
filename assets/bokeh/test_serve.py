from bokeh.io import output_file, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.plotting import figure
import numpy as np

# Generate initial data for the sine wave
x = np.linspace(0, 4 * np.pi, 1000)
y = np.sin(x)

# Create a ColumnDataSource to hold the data
source = ColumnDataSource(data=dict(x=x, y=y))

# Create a figure
plot = figure(title='Interactive Sine Wave Plot', height=400, width=600)
line = plot.line('x', 'y', source=source, line_width=2)

# JavaScript callback function to update the plot based on slider values
callback = CustomJS(args=dict(source=source), code="""
    const data = source.data;
    const amp = amplitude.value;
    const freq = frequency.value;
    const x = data['x'];
    const y = data['y'];
    for (let i = 0; i < x.length; i++) {
        y[i] = amp * Math.sin(freq * x[i]);
    }
    source.change.emit();
""")

# Create sliders for amplitude and frequency
amplitude_slider = Slider(start=0, end=5, value=1, step=0.1, title="Amplitude")
frequency_slider = Slider(start=0.1, end=5, value=1, step=0.1, title="Frequency")

# Attach JavaScript callbacks to the sliders
amplitude_slider.js_on_change('value', callback)
frequency_slider.js_on_change('value', callback)

# Create layout with sliders and plot
layout = column(amplitude_slider, frequency_slider, plot)

# Save the plot as an HTML file
output_file("interactive_sine_wave.html")
show(layout)
