import time
import board
import adafruit_bmp280
#SD card imports
import busio
import sdcardio
import storage

# PHYSICS CONSTANTS
M_earth = 0.0289644
GRAV = 9.80665
R = 8.31432
LAPSE_RATE = 0.0065

# derived constants
p_constant = -R * LAPSE_RATE / GRAV * M_earth) - 1

# data readings
pressure_log = [] # log of last two seconds of data
time_log = [] # log of time for last two seconds of data
initial_height = 0 # log of initial heights

# initialize sensors
i2c = board.I2C()  # uses board.SCL and board.SDA
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# initialize SD Card
# Use the board's primary SPI bus
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = board.D11

sdcard = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")


# takes 10 initial height readings and logs them
def initialHeight():
    # take readings
    # save average of readings to initial heights
    # log average initial height to SD Card

    bmp280.sea_level_pressure = 1013.25
    pass

def pressureToAltitude(pressure):
    return (temp_0 / LAPSE_RATE)
            * ((pressure / pressure_0)  #
            ** p_constant # raised to the power of constant

def updateQueue(pressure, t):
    if len(pressure_log) >= 150:
        pressure_log.pop(0)
        time_log.pop(0)

    pressure_log.push(pressure)
    time_log.push(t)


def writeToBreakoutBoard(t, altitude, pressure, temperature):
    with open("/sd/data.txt", 'a') as f:
        f.write(t + ",")
        f.write(altitude + ",")
        f.write(pressure + ",")
        f.write(temperature + "\n")
        f.close()

def log(launched):
    alt, press, temp = bmp280.altitude, bmp280.pressure, bmp280.temperature
    t = time.monotonic() * 1000 - launched
    updateQueue(press, t)
    writeToBreakoutBoard(t, alt, press, temp)
