import numpy as np

# physics constants
M_earth = 0.0289644
GRAV = 9.80665
R = 8.31432
LAPSE_RATE = 0.0065


def detectApogee(pressure_log, time_log):
    slope, intercept = np.polyfit(time_log, pressure_log, 1)

    return slope >= 0
