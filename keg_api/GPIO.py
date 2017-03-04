__author__ = 'andrewsmiley'
BCM = 99
IN = 99
PUD_UP=99
FALLING = 99
LOW= 99
HIGH=100
OUT=9999

def setmode(mode):
    pass

def setup(val0, val1, pull_up_down=0):
    pass

def add_event_detect(val0, val1, callback=lambda x: x+1):
    pass
def output(val0, val1 ):
    pass

# GPIO.output(18, GPIO.LOW)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(18, GPIO.OUT)
# GPIO.add_event_detect(23, GPIO.FALLING, callback=click_incrementer)
# GPIO.setmode(GPIO.BCM)
