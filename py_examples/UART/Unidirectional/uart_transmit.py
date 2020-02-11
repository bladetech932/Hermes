import serial

ser = serial.Serial()
ser.bauderate = 9600
ser.port = "/dev/ttyS0"
if (ser.isOpen() == False):
	ser.open()
while True:
	Input = input("Enter Input: ")
	Input1 = (Input + "\n") 
	ser.write (Input1.encode()) # The .encode method encodes the Input into bytes
	output = ser.readline() # Receives the same number of bytes as the input is long
    output1 = output.decode()
    print (output1)

ser.close()
