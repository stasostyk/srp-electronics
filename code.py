# electronics imports
import board
import external
import time
import measure
import statemachine
import buzzer
import config

# custom files
import telemetry
import parachute



apogee = config.get_apogee()
window_before = config.get_window_before()
window_after = config.get_window_after()

rocket = statemachine.Statemachine(PYRO_FIRE_DELAY_MS = apogee + window_after)

def initialize():
    pass

# detonate blackpowder
def detonate_blackpowder():
    rocket.do_state_transition(States.DEPLOYED_MODE)

while True:
    buzzer.buzzer_tick()
    rocket.tick()

    if rocket.LAUNCHED:
        launched = time.monotonic()*1000 - rocket.launched_time
        telemetry.log(launched)

        if launched > apogee - window_before:
            # in deployment window
            pressure_log = telemetry.pressure_log
            time_log = telemetry.time_log

            if parachute.detectApogee(pressure_log, time_log):
                detonate_blackpowder() # kaboom >:)



    time.sleep(0.01) # get somewhere under 100 measurements a second
