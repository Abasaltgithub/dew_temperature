import matplotlib.pyplot as plt
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

# Create a gradient of blue colors that get darker as temperature increases
colors = plt.cm.Blues(np.linspace(0, 0.5, len(T_values)))

# Plot Dew Point Temperatures vs. Incubator Humidity with gradient colors
plt.figure(figsize=(7, 4))

for i, T_val in enumerate(T_values):
    color = colors[i]
    dew_points = [dew_point(T_val, rh) for rh in RH]
    plt.plot(RH, dew_points, color=color)

# Plot for incubator temperature = 37°C as dashed line
T_val_37 = 37
dew_points_37 = [dew_point(T_val_37, rh) for rh in RH]
plt.plot(RH, dew_points_37, color='black', linestyle='--',
         label='Incubator Temperature = 37°C')

plt.xlabel("Incubator Humidity (%)")
plt.ylabel("Minimum Dew Point Temperature (°C)")

# Add a color bar on the side
sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=plt.Normalize(
    vmin=min(T_values), vmax=max(T_values)))
sm.set_array([])  # You don't need to specify an array for the color bar
cbar = plt.colorbar(sm, label='Incubator Temperature (°C)',
                    ax=plt.gca())  # Specify the Axes

plt.legend(loc='best')

# Adjust the layout
plt.tight_layout()

# Save the figure
output_image_path = 'MinT_RH.pdf'
plt.savefig(output_image_path, bbox_inches='tight', dpi=500)

# Show the combined figure
plt.show()
