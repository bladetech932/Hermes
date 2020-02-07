import serial
ser = serial.Serial ("/dev/ttyS0")    #Open named port 
ser.baudrate = 9600                     #Set baud rate to 9600
while True:
	data1 = ser.read(10)
	data = "Hello"                     #Read ten characters from serial port to data
	ser.write(data)                         #Send back the received data
ser.close() 
