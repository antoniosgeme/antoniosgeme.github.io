import plotly.graph_objects as go
import plotly.io as pio
import numpy as np
import plotly.figure_factory as ff

# Number of points for the grid
num_points = 50

# Generate grid points
x = np.linspace(-3, 3, num_points)
y = np.linspace(-3, 3, num_points)
X, Y = np.meshgrid(x, y)

# Define uniform flow velocity components
Gamma = 1
r2 = X**2 + Y**2
u = Gamma/(2*np.pi*r2)*Y/r2
v = -Gamma/(2*np.pi*r2)*X/r2
# Create the quiver plot
#fig = ff.create_quiver(X, Y, u, v, name='Uniform Flow')
fig = ff.create_streamline(x, y, u, v, arrow_scale=0.2)


# Update layout
fig.update_layout(
    width=600,  # Set the width of the figure (in pixels)
    height=600,  # Set the height of the figure (in pixels)
    title='Streamlines: Vortex Flow',
    xaxis=dict(title='X', scaleanchor="y",scaleratio=1),
    yaxis=dict(title='Y',scaleanchor="x", scaleratio=1),
)

# Show the figure
fig.show()

pio.write_html(fig, file='vortex.html', auto_open=False)
