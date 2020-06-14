#pip3 install adafruit-circuit-motorkit
import cv2

import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from time import sleep

i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus)
pca.frequency = 50

servo1 = servo.Servo(pca.channels[1])

min_angle = 0
max_angle = 180
step_size = 1
delay = 10 # ms

while True:
	for i in range(min_angle, max_angle, step_size):
		print(i)
		servo1.angle = i
		sleep(delay/1000)
	for i in range(max_angle, min_angle, -step_size):
		print(i)
		servo1.angle = i
		sleep(delay/1000)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		pca.deinit()
		break
