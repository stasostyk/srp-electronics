import board
import pwmio
import time

_buzzer_pin = board.BUZZER

_buzzer_current_item = None
_buzzer_queue = []

#duty cycle is the fraction of the given value divided by 2**16
_buzzer = pwmio.PWMOut(_buzzer_pin, duty_cycle=0, frequency=2000, variable_frequency=True)

def _get_time_from_start():
        return round(time.monotonic()*1000)

def _queue_next_note():
        global _buzzer_current_item
        if len(_buzzer_queue) > 0:
                next_item_to_be_queued = _buzzer_queue.pop()
        else:
                _buzzer.duty_cycle = 0
                _buzzer_current_item = None
                return
                
        next_item_to_be_queued['start_time'] = _get_time_from_start()
        _buzzer_current_item = next_item_to_be_queued
        
        if _buzzer_current_item['freq'] == 0: # This is a wait
                _buzzer.duty_cycle = 0
        else:
                _buzzer.frequency = _buzzer_current_item['freq']
                _buzzer.duty_cycle = 2**15
        

def append_buzzer_wait(duration):
        '''
        duration: time in ms
        '''
        item_to_add = {
                'freq': 0,
                'duration': duration
        }
        _buzzer_queue.append(item_to_add)

def append_buzzer_note(freq, duration):
        '''
        freq: frequency of the tone in Hz
        duration: time in ms
        '''

        if freq <= 0:
                append_buzzer_wait(duration)
        item_to_add = {
                'freq': freq,
                'duration': duration
        }
        _buzzer_queue.append(item_to_add)
        
def buzzer_tick():
        '''
        Call this function in a loop to run the buzzer code
        '''       
        if _buzzer_current_item == None: # There is notthing playing right now
                _queue_next_note() # Play another note if there is one                
        elif _buzzer_current_item['start_time'] + _buzzer_current_item['duration'] < _get_time_from_start():
                _queue_next_note() # Play next note
        


