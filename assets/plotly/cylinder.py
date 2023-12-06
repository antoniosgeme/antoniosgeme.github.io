import plotly.graph_objects as go
import plotly.io as pio
import numpy as np
import plotly.figure_factory as ff

# Define the uniform flow field
U_inf = 1  # Magnitude of the uniform flow

# Number of points for the grid
num_points = 20

# Generate grid points
x = np.linspace(-2, 2, num_points)
y = np.linspace(-2, 2, num_points)
X, Y = np.meshgrid(x, y)

# Define uniform flow velocity components
u = U_inf * np.ones_like(X)
v = np.zeros_like(Y)

# Create the quiver plot
fig = ff.create_quiver(X, Y, u, v, scale=0.1, arrow_scale=0.3, name='Uniform Flow')

# Update layout
fig.update_layout(
    title='Quiver Plot: Uniform Flow',
    xaxis=dict(title='X'),
    yaxis=dict(title='Y'),
    showlegend=True
)

# Show the figure
fig.show()

pio.write_html(fig, file='cylinder.html', auto_open=False)
