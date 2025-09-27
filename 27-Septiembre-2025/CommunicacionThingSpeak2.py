import machine, network, urequests, time
from machine import Pin, Timer, UART
from utime import sleep_ms
import dht
import sh1106

ssid = 'Wokwi-GUEST'
password = ''
url = 'https://api.thingspeak.com/update?api_key=Tu_API_Key_Aqui'

red = network.WLAN(network.STA_IF)
red.active(True)
red.connect(ssid, password)

while red.isconnected() == False:
    pass

print('Conexion exitosa')
print(red.ifconfig())

ultima_peticion = 0
intervalo_peticiones = 30

global Temper
global Humedad

Temper = 0
Humedad = 0

pinLed1 = Pin(4, Pin.OUT)
pinLed2 = Pin(3, Pin.OUT)
objSensorDht = dht.DHT11(Pin(8))
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

    objSensorDht.measure()
    Temper = objSensorDht.temperature()
    Humedad = objSensorDht.humidity()

    pinLed1.toggle()

objTimer.init(period=500, mode=Timer.PERIODIC, callback=TimerLeeSensor)

def reconectar():
    print('Fallo de conexion. Reconectando...')
    time.sleep(10)
    machine.reset()

while True:
    try:
        if (time.time() - ultima_peticion) > intervalo_peticiones:
            print(Temper)
            print(Humedad)
            respuesta = urequests.get(url + '&field1=' + str(Temper) + '&field2=' + str(Humedad))
            print("Respuesta: " + str(respuesta.status_code))
            respuesta.close()
            ultima_peticion = time.time()

            objPuertoSerial0.write("Temperatura = " + str(Temper) + " °C " + " - ")
            objPuertoSerial0.write("Humedad = " + str(Humedad) + " %\r\n")

            objPantOled.text("Temp. =   gC", 0, 20)
            objPantOled.text(str(Temper), 63, 20)

            objPantOled.text("Hum. =     %", 0, 40)
            objPantOled.text(str(Humedad), 63, 40)

            objPantOled.show()

            objPantOled.text(str(Temper), 63, 20, 0)
            objPantOled.text(str(Humedad), 63, 40, 0)

            pinLed2.toggle()
    except OSError as e:
        print('Error de conexion', e)
        reconectar()