import serial
import time

uart_port = "/dev/ttyS0" 
baud_rate = 9600
file = open("humidity.txt", "r")
contents = file.read()
file.close()
uart = serial.Serial(uart_port, baud_rate, timeout=1)
uart.write(contents)
time.sleep(1)
received_data = uart.readline().decode('utf-8')
print("Received data:", received_data)
uart.close()





