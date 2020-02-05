import RPi.GPIO as GPIO
import time

pwm0_pin = 32 # also 12
pwm1_pin = 33

default_cycle = 95
delay =  0.1 #delay for sleep in seconds

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pwm0_pin, GPIO.OUT)
GPIO.setup(pwm1_pin, GPIO.OUT)

pwm0 = GPIO.PWM(pwm0_pin, 50)
pwm1 = GPIO.PWM(pwm1_pin, 50)

pwm0.start(default_cycle)
pwm1.start(default_cycle)

try:
	while True:

		i = 0
		while i < 100:
			pwm0.ChangeDutyCycle(i)
			pwm1.ChangeDutyCycle(i)
			time.sleep(delay)
			i += 1

		while i > 0:
			pwm0.ChangeDutyCycle(i)
			pwm1.ChangeDutyCycle(i)
			time.sleep(delay)
			i -= 1

except KeyboardInterrupt:
	pwm0.stop()
	GPIO.cleanup()
