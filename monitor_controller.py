import RPi.GPIO as GPIO
import time
import os
import logging
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, 
                    filename='monitor_controller.log', # log to this file
                    format='%(asctime)s %(message)s') # include timestamp

logging.info("Starting Monitor Controller")

def turnMonitorOff():
	logging.info("Turning monitor off")
	os.system("/opt/vc/bin/tvservice -p && /opt/vc/bin/tvservice -o")
	time.sleep(5)

def turnMonitorOn():
	logging.info("Turning monitor on")
	os.system("/opt/vc/bin/tvservice -p && chvt 1 && chvt 7")
    time.sleep(5)

sensor = 18
timeout = 60

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

lastsensed = datetime.now()
turnMonitorOn()
isMonitorOn = True

while True:
    if GPIO.input(sensor) == 1:
            lastsensed = datetime.now()
            if isMonitorOn == False:
                    turnMonitorOn()
                    isMonitorOn = True
            time.sleep(1)
    elif (datetime.now() - lastsensed).seconds > timeout:
            if isMonitorOn == True:
                    turnMonitorOff()
                    isMonitorOn = False
            time.sleep(1)
logging.info("Stopping Monitor Controller")
GPIO.cleanup()





