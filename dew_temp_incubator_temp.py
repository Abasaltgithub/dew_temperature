import plotly.graph_objs as go
import numpy as np
import math

# Constants for dew point calculation
a = 6.112
b = 17.62
c = 243.12

# Dew point calculation function


def dew_point(T, RH):
    if RH > 0:
        Td = c * (math.log(RH/100) + ((b * T) / (c + T))) / \
            (b - math.log(RH/100) - ((b * T) / (c + T)))
    else:
        Td = float('nan')
    return Td


# Relative humidity range
RH = np.linspace(0, 100, 100)

# Create a gradient of temperatures
T_values = np.linspace(27, 47, 100)

# Create a 2D grid of RH and T values
RH_grid, T_grid = np.meshgrid(RH, T_values)

# Calculate dew points for the grid
dew_points = np.array([[dew_point(T, RH) for T, RH in zip(
    T_row, RH_row)] for T_row, RH_row in zip(T_grid, RH_grid)])

# Create a 3D surface plot with a smaller color bar
# Define a custom colorscale that gradually transitions from blue to yellow, orange, and red
custom_colorscale = [
    [0.0, 'blue'],       # Blue at the lower end
    [0.25, 'lightblue'],  # Light blue in the blue region
    [0.5, 'lightblue'],  # Light blue in the blue region
    [0.75, 'yellow'],    # Yellow in the transition region
    [0.9, 'orange'],     # Orange in the transition region
    [1.0, 'red'],        # Red at the upper end
]

# Create a 3D surface plot with the custom colorscale
# Create a 3D surface plot with the custom colorscale and a smaller colorbar
surface = go.Surface(
    z=dew_points,
    x=RH,
    y=T_values,
    colorbar=dict(
        title=dict(text='Dew Temperature (°C)',
                   side='right', font=dict(size=12)),
        # Adjust the length of the colorbar (smaller value for smaller size)
        len=0.4
    ),
    colorscale=custom_colorscale  # Use the custom colorscale
)


# Calculate dew points for RH=60%
RH_60 = 60
dew_points_60 = [dew_point(T, RH_60) for T in T_values]

# Create a Scatter3d trace for RH=60% as a thick solid line
scatter_60 = go.Scatter3d(
    x=np.ones_like(T_values) * RH_60,
    y=T_values,
    z=dew_points_60,
    mode='lines',
    line=dict(color='black', dash='dash', width=5)  # Change 'dash' to 'solid'
)

# Create a layout for the plot without specific annotations
layout = go.Layout(
    scene=dict(
        xaxis=dict(title='Incubator Humidity (%)'),
        yaxis=dict(title='Incubator Temperature (°C)'),
        zaxis=dict(title='Dew Temperature (°C)'),
        aspectmode='manual',  # Set aspect mode to manual
        aspectratio=dict(x=2, y=2, z=1),  # Adjust aspect ratio for size
        # bgcolor='black',  # Set background color to white
        # camera=dict(
        #     up=dict(x=0, y=0, z=1),  # Set the camera up vector to make the z-axis vertical
        #     center=dict(x=0, y=0, z=0)  # Set the camera center
        # )
    ),
    width=1000,  # Set the width of the plot
    height=800,  # Set the height of the plot
    # Add left and right margin for the color bar and its label
    margin=dict(l=50, r=150),
)

# Create a figure with the surface plot, the solid line for RH=60%, and the color bar
fig = go.Figure(data=[surface, scatter_60], layout=layout)

fig.show()
