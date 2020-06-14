from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from time import sleep

i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus)
pca.frequency = 60

min_value = 2496
max_value = 10240
step_size = 16
delay = 10 # ms

for s in range(0, 3):
	for i in range(min_value, max_value, step_size):
		print(s,i)
		pca.channels[1].duty_cycle = i
		sleep(delay/1000)
	for i in range(max_value, min_value, -step_size):
		print(s,i)
		pca.channels[1].duty_cycle = i
		sleep(delay/1000)
