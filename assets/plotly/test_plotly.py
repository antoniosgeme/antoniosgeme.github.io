import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
import plotly.io as pio


def create_sine_wave_plot(frequency):
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(frequency * x)

    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))

    fig.update_layout(
        title='Sine Wave',
        xaxis_title='X',
        yaxis_title='Y',
        sliders=[{
            'currentvalue': {'prefix': 'Frequency: '},
            'steps': [{'method': 'restyle',
                       'args': ['y', [np.sin(freq * x)]],
                       'label': str(freq)}
                      for freq in np.arange(1, 5, 0.1)],
            }]
    )
    #fig.show()
    pio.write_html(fig, file='sine_wave_plot.html', auto_open=False)

if __name__ == "__main__":
    default_frequency = 1  # Default frequency value
    create_sine_wave_plot(default_frequency)
