import plotly.graph_objects as go
import plotly.io as pio
import numpy as np
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

# Number of points for the grid
num_points = 50

# Generate grid points
x = np.linspace(-3, 3, num_points)
y = np.linspace(-3, 3, num_points)
X, Y = np.meshgrid(x, y)

# Define uniform flow velocity components
fig = make_subplots(
    rows=1, cols=3,
    subplot_titles=("Uniform Flow", "Vortex Flow", "Doublet Flow")
)

Uinf = 1
u = Uinf * np.ones_like(X)
v = np.zeros_like(X)
# Create the quiver plot
#fig = ff.create_quiver(X, Y, u, v, name='Uniform Flow')
fig.add_trace(
    ff.create_streamline(x, y, u, v, arrow_scale=0.2).data[0],
    row=1, col=1
              )

Gamma = 1
r2 = X**2 + Y**2
u = Gamma/(2*np.pi*r2)*Y/r2
v = -Gamma/(2*np.pi*r2)*X/r2
# Create the quiver plot
#fig = ff.create_quiver(X, Y, u, v, name='Uniform Flow')
fig.add_trace(
    ff.create_streamline(x, y, u, v, arrow_scale=0.2).data[0],
    row=1, col=2
              )

kappa = 1
u = kappa/np.pi*X*Y/r2**2
v = -kappa/(2*np.pi)*(X**2 - Y**2)/r2**2

fig.add_trace(
    ff.create_streamline(x, y, u, v, arrow_scale=0.2).data[0],
    row=1, col=3
              )
# Update layout
fig.update_layout(
    width=1000,  # Set the width of the figure (in pixels)
    height=600,  # Set the height of the figure (in pixels)
    title='Streamlines: Vortex Flow',
    xaxis=dict(title='X', scaleanchor="y",scaleratio=1),
    yaxis=dict(title='Y',scaleanchor="x", scaleratio=1)
)

# Set x and y-axis limits for Subplot 1
fig.update_xaxes(range=[-3, 3], row=1, col=1)  # X-axis limits for Subplot 1
fig.update_yaxes(range=[-3, 3], row=1, col=1)  # Y-axis limits for Subplot 1

# Set x and y-axis limits for Subplot 2
fig.update_xaxes(range=[-3, 3], row=1, col=2)  # X-axis limits for Subplot 1
fig.update_yaxes(range=[-3, 3], row=1, col=2)  # Y-axis limits for Subplot 1

# Set x and y-axis limits for Subplot 3
fig.update_xaxes(range=[-3, 3], row=1, col=3)  # X-axis limits for Subplot 1
fig.update_yaxes(range=[-3, 3], row=1, col=3)  # Y-axis limits for Subplot 1

# Show the figure
fig.show()

pio.write_html(fig, file='uniform.html', auto_open=False)
