import json

def get_apogee():
    parsed_jsondata = json.loads(open('config.json', 'r').read())
    return parsed_jsondata['apogee']

def get_window_before():
    parsed_jsondata = json.loads(open('config.json', 'r').read())
    return parsed_jsondata['window_before']

def get_window_after():
    parsed_jsondata = json.loads(open('config.json', 'r').read())
    return parsed_jsondata['window_after']
