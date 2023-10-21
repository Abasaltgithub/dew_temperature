# Minimum Dew Temperature

This repository contains code for simulating the minimum dew temperature. Dew temperature, or dew point, is a crucial meteorological parameter that represents the temperature at which air becomes saturated with moisture and condensation forms. This simulation can be useful in various fields, including meteorology, agriculture, and HVAC systems.






## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [References](#references)

## Overview

The minimum dew temperature simulation is a fundamental tool for understanding moisture levels in the atmosphere. This repository provides a Python-based implementation to calculate the minimum dew temperature. By specifying air temperature and relative humidity, you can determine the temperature at which condensation will occur.

<img src="MinT_RH.png" width="600">

$$
T_d = \frac{c \left( \ln\left(\frac{RH}{100}\right) + \frac{bT}{c+T} \right)}{b - \ln\left(\frac{RH}{100}\right) - \frac{bT}{c+T}}
$$



Where:
- `<code>T<sub>d</sub></code>` is the dew point temperature (in °C).
- `T` is the air temperature (in °C).
- `RH` is the relative humidity (in %).
- `a`, `b`, and `c` are constants:
  - `a = 6.112`
  - `b = 17.62`
  - `c = 243.12`

This formula calculates the minimum dew point temperature, a critical meteorological parameter representing the temperature at which air becomes saturated with moisture, leading to condensation.

## Getting Started

To get started with this simulation, follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/Abasaltgithub/dew_temperature.git
   ```

2. Navigate to the project directory:

   ```shell
   cd dew_temperature
   ```

3. Ensure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

4. Install the required Python packages if not already installed:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

You can use the minimum dew temperature simulation by running the Python script provided in this repository. Here's how to use it:
1. Open the `minimum_dew_temperature.py` script in your preferred code editor.
2. Modify the values of `air_temperature` and `relative_humidity` in the script to match your specific conditions.
3. Run the script:

   ```shell
   python dew_temperature.py
   ```

The script will calculate and display the minimum dew temperature based on the provided input.

## References

If you would like to learn more about the calculation methods or gain a deeper understanding of dew point, you can refer to the following resources:

- [Dew Point Calculation and Humidity Sensor](http://irtfweb.ifa.hawaii.edu/~tcs3/tcs3/Misc/Dewpoint_Calculation_Humidity_Sensor_E.pdf) - A detailed PDF document explaining the dew point calculation and its relation to humidity sensors.

- [Dew Point Calculator](https://www.calculator.net/dew-point-calculator.html?airtemperature=37&airtemperatureunit=celsius&humidity=60&dewpoint=&dewpointunit=celsius&x=63&y=22) - An online tool for calculating the dew point. You can use this calculator to verify the accuracy of the simulation results.

Feel free to contribute to this repository or use the code in your own projects. If you have any questions or encounter issues, please create an issue in the GitHub repository for assistance.
