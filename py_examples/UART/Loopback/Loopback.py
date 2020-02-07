import serial

ser = serial.Serial()
ser.baudrate = 9600 # Sets the baud rate (bits trasmitted per sec)
ser.port = "/dev/ttyS0" # Sets the Port to pin 8 found by $ ls -l /dev
ser.open()
while True:
	Input = input("Enter Input: ")
	num_of_bytes  = len(Input) 
	ser.write (Input.encode()) # The .encode method encodes the Input into bytes
	output = ser.read(num_of_bytes) # Receives the same number of bytes as the input is long
	print (output)
ser.close()
