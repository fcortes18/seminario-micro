import machine, network, urequests, time
from machine import Pin, Timer, UART
from utime import sleep_ms
import dht

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
            pinLed2.toggle()
    except OSError as e:
        print('Error de conexion', e)
        reconectar()