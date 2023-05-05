from ulab import numpy as np

def detectApogee(pressure_log, time_log):
    print(len(pressure_log))
    print(len(time_log))
    if len(pressure_log) > 5:
        slope, intercept = np.polyfit(time_log, pressure_log, 1)
        print(slope)

        return slope >= 0.1
    return False
