import matplotlib.pyplot as plt
from colour import Color

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

print("[+] Rendering 3D results... ")
fig = plt.figure()
graph3D = fig.add_subplot(projection='3d')

csize = int((max(temperature)-min(temperature))*100)
colours = list(Color("blue").range_to(Color("purple"), csize+1))

for i in range(len(time)):
    col = int((temperature[i]-min(temperature))*100)
    print(col)
    graph3D.scatter(time[i], pressure[i], altitude[i], color=colours[col].rgb)

graph3D.set_title("Flight Data Visualization")
graph3D.set_xlabel("Time ($s$)")
graph3D.set_ylabel("Pressure ($kPa + 1010$)")
graph3D.set_zlabel("Altitude ($m$)")
plt.locator_params(axis='y', nbins=4)
plt.show()
