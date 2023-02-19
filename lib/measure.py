import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull

#Pin definitions
_bw_pin = board.BW
_arm_sense_pin = board.ARM_MEAS
_vbat_sense_pin = board.VBAT_MEAS
_pyro_cont_sense_pin = board.CONT_MEAS

# Breakwire initialization
# Simple input with no pull up
_bw = DigitalInOut(_bw_pin)
_bw.direction = Direction.INPUT

# Arm sense initialization
# Simple input with a pull up
_arm_sense = DigitalInOut(_arm_sense_pin)
_arm_sense.direction = Direction.INPUT
_arm_sense.pull = Pull.UP

# Vbat measurement
# Analog input
_vbat_meas = AnalogIn(_vbat_sense_pin)

# Pyro continuity sense initialization
# Simple input with a pull up
_pyro_cont_sense = DigitalInOut(_pyro_cont_sense_pin)
_pyro_cont_sense.direction = Direction.INPUT
_pyro_cont_sense.pull = Pull.UP


def is_bw_inserted():
        '''
        if the BW is inserted, this pin will be pulled high so it will return True
        '''
        return _bw.value

def is_armed():
        '''
        if the system is armed, this pin will be pulled low so it will return False
        '''
        return not _arm_sense.value


def is_pyro_inserted():
        '''
        if the pyro is inserted, the pin will be pulled high so it will return True
        '''
        return _pyro_cont_sense.value

def get_vbat_voltage():
        '''
        This is an analog measurment between a 22k and 10k resistor. So the battery voltage will be 32/10 times as high
        Will return a float with the battery voltage
        '''
        return (_vbat_meas.value * 3.3 * 32/10) / 65536
