import matplotlib.pyplot as plt

time = []
pressure = []
altitude = []
temperature = []

fname = input("[?] file name: ")

with open(fname) as data:
    next(data)
    next(data)
    for log in data:
        t, a, p, temp = log.split(',')

        time.append(float(t))
        pressure.append(float(p))
        altitude.append(float(a))
        temperature.append(float(temp))

fig, axs = plt.subplots(3)
fig.suptitle('Rocket Flight Data')

axs[0].set_title("Pressure")
axs[1].set_title("Altitude")
axs[2].set_title("Temperature")

axs[0].plot(time, pressure, label="pressure")
axs[1].plot(time, altitude, label="altitude")
axs[2].plot(time, temperature, label="temperature")

plt.show()
