import RPi.GPIO as GPIO
import time

pin_number = 5
GPIO.setmode(GPIO.BOARD) # use BCM instead of BOARD for BCM pin numbers
GPIO.setup(pin_number, GPIO.OUT) # set as an output

GPIO.setwarnings(False)

while True:
	GPIO.output(pin_number, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(pin_number, GPIO.LOW)
	time.sleep(0.1)


