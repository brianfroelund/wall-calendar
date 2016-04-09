import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)

monitor = 15
sensor = 18

timeout = 300

GPIO.setup(sensor, GPIO.IN)
GPIO.setup(monitor, GPIO.OUT)

GPIO.output(monitor, 0) #ON
lastsensed = datetime.now()

while True:
	if GPIO.input(sensor) == 1: 
		lastsensed = datetime.now()
		GPIO.output(monitor, 0) #ON
		time.sleep(10)
	elif (datetime.now() - lastsensed).seconds > timeout:
		GPIO.output(monitor, 1) #OFF
		time.sleep(1)
	

GPIO.cleanup()
