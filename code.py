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

# detonate blackpowder
def detonate_blackpowder():
    rocket.autonomously_deploy = True

def main():
    if rocket.LAUNCHED:
        launched = time.monotonic() - (rocket.launched_time / 1000)
        telemetry.log(launched) # log flight data to SD card

        if launched > apogee - window_before:
            # in deployment window
            pressure_log = telemetry.pressure_log
            time_log = telemetry.time_log

            if parachute.detectApogee(pressure_log, time_log):
                detonate_blackpowder() # kaboom >:)
    else:
        initialHeight()

def rocketTesting(launched):
    telemetry.log(launched)

    pressure_log = telemetry.pressure_log
    time_log = telemetry.time_log

    if parachute.detectApogee(pressure_log, time_log):
        buzzer.append_buzzer_note(300, 200)
        buzzer.append_buzzer_wait(500)

### initial time
# initial_time = time.monotonic()

while True:
    buzzer.buzzer_tick()

    ### LAUNCH DAY MODE
    rocket.tick()
    main()

    ### XOR TESTING MODE
    # rocketTesting(initial_time)
