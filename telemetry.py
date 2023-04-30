import time
import board
import adafruit_bmp280
#SD card imports
import busio
import sdcardio
import storage

# telemetry variables
now = time.localtime()
filename = f'{now.tm_year}-{now.tm_mon}-{now.tm_mday}_{now.tm_hour}-{now.tm_min}-{now.tm_sec}-({time.monotonic_ns()}).txt'

# data readings
pressure_log = [] # log of last two seconds of data
time_log = [] # log of time for last two seconds of data

# initialize sensors
i2c = busio.I2C(board.SCL, board.SDA)   # uses board.SCL and board.SDA
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, 0x76) # BMP is on address 76

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

    readings = []
    for i in range(5):
        readings.append(bmp280.pressure)
        time.sleep(0.1)

    avg = sum(readings) / len(readings)
    bmp280.sea_level_pressure = avg

    with open("/sd/data/" + filename, 'a') as f:
        f.write(f'Flight Data for CHKN-1 in format time (s), altitude (m), pressure (Pa), temperature (C)\n')
        f.write(f'initial pressure: {avg}\n')
        f.close()



def updateLogQueue(pressure, t):
    if len(time_log) > 0 and t - time_log[0] >= 2:
        pressure_log.pop(0)
        time_log.pop(0)

    pressure_log.append(pressure)
    time_log.append(t)


def writeToBreakoutBoard(t, altitude, pressure, temperature):
    with open("/sd/data/" + filename, 'a') as f:
        f.write(f'{t}, {altitude}, {pressure}, {temperature}\n')
        f.close()

def log(launched):
    alt, press, temp = bmp280.altitude, bmp280.pressure, bmp280.temperature
    t = time.monotonic() - launched
    updateLogQueue(press, t)
    writeToBreakoutBoard(t, alt, press, temp)
