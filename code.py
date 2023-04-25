import board
import external
import time
import measure
import statemachine
import buzzer
import config
import numpy as np



delay_pyro_miliseconds = config.get_deployment_timer()
print(f'Read in a delay of {delay_pyro_miliseconds} ms from the config file')

states = statemachine.Statemachine(PYRO_FIRE_DELAY_MS = delay_pyro_miliseconds)

def pressureToAltitude(pressure):
    return (temp_0 / LAPSE_RATE) * ((pressure / pressure_0) ** (-R * LAPSE_RATE / GRAV * M_earth) - 1)

while True:
    buzzer.buzzer_tick()
    states.tick()
