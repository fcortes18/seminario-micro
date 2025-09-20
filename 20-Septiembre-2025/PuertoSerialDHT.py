from machine import Pin, Timer, UART
from utime import sleep_ms
import dht
import sh1106

pinLed1 = Pin(4, Pin.OUT)
pinLed2 = Pin(3, Pin.OUT)

global Temper
global Humedad

Temper = 0
Humedad = 0

objSensorDHT = dht.DHT11(Pin(8))
objTimer = Timer()
objPuertoSerial0 = UART(0, baudrate = 9600, tx = Pin(0), rx = Pin(1))
objI2C = machine.I2C(1, scl=machine.Pin(19), sda=machine.Pin(18))
objPantOled = sh1106.SH1106_I2C(128, 64, objI2C)

objPantOled.fill(0)
objPantOled.rotate(1)
objPantOled.show()
sleep_ms(1000)
objPantOled.text("Sensor DHT11", 14, 0)
objPantOled.show()

def TimerLeeSensor(Dato):
    global pinLed1
    global Temper
    global Humedad

    objSensorDHT.measure()
    Temper = objSensorDHT.temperature()
    Humedad = objSensorDHT.humidity()
    
    pinLed1.toggle()

objTimer.init(period = 300, mode = Timer.PERIODIC, callback = TimerLeeSensor)

while True:

    objPuertoSerial0.write("Temperatura = " + str(Temper) + " °C " + " - ")
    objPuertoSerial0.write("Humedad = " + str(Humedad) + " %\r\n")

    objPantOled.text("Temp. = 	gC", 0, 20)
    objPantOled.text(str(Temper), 63, 20)

    objPantOled.text("Hum. = 	%", 0, 40)
    objPantOled.text(str(Humedad), 63, 40)

    objPantOled.show()

    objPantOled.text(str(Temper), 63, 20, 0)
    objPantOled.text(str(Humedad), 63, 40, 0)

    pinLed2.toggle()
    sleep_ms(1000)