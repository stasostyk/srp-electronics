import board
from digitalio import DigitalInOut, Direction
from pwmio import PWMOut
import neopixel

#Pin definitions
_pyro_detonate_pin = board.PYRO_DETONATE
_servo_pin = board.SERVO
_ext_led_pin = board.LED_EXT
_ext_gpio_pin = board.EXT_GPIO

# pyro detonation initialization
# Simple output, high to turn on
_pyro_detonate = DigitalInOut(_pyro_detonate_pin)
_pyro_detonate.direction = Direction.OUTPUT
_pyro_detonate.value = False

# Servo inizialization
# PWM output with 50 HZ frequency
_servo = PWMOut(_servo_pin, frequency=50, duty_cycle=0)

# external LED initialization
# Simple output, high to turn on
_ext_led = DigitalInOut(_ext_led_pin)
_ext_led.direction = Direction.OUTPUT
_ext_led.value = False

# external GPIO initialization
# Simple output, high to turn on
_ext_gpio = DigitalInOut(_ext_gpio_pin)
_ext_gpio.direction = Direction.OUTPUT
_ext_gpio.value = False

# Init the Neopixel
_pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=1, auto_write=True)
BRIGHTNESS = 0.1 # Value between 0.0 and 1.0 to define brightness of led


def set_external_led(state):
        _ext_led.value = state
        
def set_external_GPIO(state):
        _ext_gpio.value = state
        
        
def set_servo_duty(duty):
        '''
        Expects a number between 0.0 and 1.0 where 0 is the minimal setting and 1.0 is the maximal
        will set the servo accordingly
        '''

        if duty < 0.0 or duty > 1.0:
                raise ValueError(f"{duty} is an invalid input parameter, Stick with values between 0.0 and 1.0")
                
        # Calculate the actual dutycycle, 0 is 0% and 2**16 is 100%
        actual_duty = int((duty*0.05 + 0.05)*(2**16))
        _servo.duty_cycle = actual_duty

def PYRO_DETONATE():
        '''
        This function fires the Pyro!
        '''
        _pyro_detonate.value = True

def PYRO_RESET():
        '''
        This function resets the pyro
        '''
        _pyro_detonate.value = False
        
def neopixel_disable():
        global _pixel
        _pixel[0] = (0,0,0)
        
def neopixel_set_rgb(r, g, b):
        global _pixel
        _pixel[0] = (round(r*BRIGHTNESS),round(g*BRIGHTNESS),round(b*BRIGHTNESS))


