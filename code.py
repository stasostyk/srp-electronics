import board
import external
import time
import measure
import statemachine
import buzzer
import config

delay_pyro_miliseconds = config.get_deployment_timer()
print(f'Read in a delay of {delay_pyro_miliseconds} ms from the config file')

states = statemachine.Statemachine(PYRO_FIRE_DELAY_MS = delay_pyro_miliseconds)

while True:
   buzzer.buzzer_tick()
   states.tick()
