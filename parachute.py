import numpy as np

def detectApogee(pressure_log, time_log):
    slope, intercept = np.polyfit(time_log, pressure_log, 1)

    return slope >= 0
