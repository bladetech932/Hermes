import serial

ser = serial.Serial()
ser.bauderate = 9600
ser.port = "/dev/ttyS0"
if (ser.isOpen() == False):
        ser.open()
while True:
       
	output = ser.readline() # Receives the same number of bytes as the input is long
        output1 = output.decode()
        print (output1)
ser.close() 


