__author__ = 'andrewsmiley'

def get_thermo_status():
    return True
def get_keg_temperature():
    return 50
def get_flowmeter_status():
    return True
def get_pressure_sensor_status():
    return {"ps0":True, "ps1":True, "ps2":True}
def get_keg_percentage():
    return 100
def get_c02_percentage():
    return 100

def get_days_to_keg_empty():
    return 3

def get_days_in_tank():
    return 6

def get_days_in_lines():

    return 45

def get_optimal_maintenance_range():
    return ['6PM', "7AM"]