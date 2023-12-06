import numpy as np
import plotly.graph_objects as go

# Number of points for the grid
num_points = 20

# Generate grid points
x = np.linspace(-2, 2, num_points)
y = np.linspace(-2, 2, num_points)
X, Y = np.meshgrid(x, y)

# Define uniform flow velocity components
U_inf = 1  # Magnitude of the uniform flow
u_uniform = U_inf * np.ones_like(X)
v_uniform = np.zeros_like(Y)

# Define doublet flow parameters
strength_doublet = 2  # Strength of the doublet
x_doublet, y_doublet = 0, 0  # Location of the doublet
u_doublet = (-strength_doublet / (2 * np.pi)) * ((X - x_doublet)**2 - (Y - y_doublet)**2) / ((X - x_doublet)**2 + (Y - y_doublet)**2)**2
v_doublet = (-strength_doublet / (2 * np.pi)) * 2 * (X - x_doublet) * (Y - y_doublet) / ((X - x_doublet)**2 + (Y - y_doublet)**2)**2

# Define vortex flow parameters
strength_vortex = 1  # Strength of the vortex
x_vortex, y_vortex = 0, 0  # Location of the vortex
u_vortex = +strength_vortex / (2 * np.pi) * (Y - y_vortex) / ((X - x_vortex)**2 + (Y - y_vortex)**2)
v_vortex = -strength_vortex / (2 * np.pi) * (X - x_vortex) / ((X - x_vortex)**2 + (Y - y_vortex)**2)

# Create the quiver plots
fig = go.Figure()

fig.add_trace(go.Scatter(x=X.flatten(), y=Y.flatten(), mode='lines', line=dict(width=1, color='black')))
fig.add_trace(go.Scatter(x=[x_doublet], y=[y_doublet], mode='markers', marker=dict(size=10, color='red')))

fig.add_trace(go.Scatter(x=[x_vortex], y=[y_vortex], mode='markers', marker=dict(size=10, color='blue')))
fig.update_traces(name='Vortex Flow')

fig.update_layout(
    title='Quiver Plots: Uniform, Doublet, and Vortex Flows',
    xaxis=dict(title='X'),
    yaxis=dict(title='Y'),
    showlegend=True,
    width=900,
    height=400
)

fig.show()
