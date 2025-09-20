from machine import Pin, UART
import utime

pinLed = Pin(8, Pin.OUT)
miPuertoSerial = UART(0, baudrate = 9600, tx = Pin(0), rx = Pin(1))

while True:
    miPuertoSerial.write('Hola mundo :) \r\n')
    pinLed.toggle()
    utime.sleep_ms(1000)