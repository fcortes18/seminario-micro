import machine
import sh1106
import utime
import dht

Temperatura = 0
Humedad = 0

objSensorDht = dht.DHT11(machine.Pin(8))

objI2c = machine.I2C(1, scl = machine.Pin(19), sda=machine.Pin(18))
p_oled = sh1106.SH1106_I2C(128, 64, objI2c)

p_oled.fill(0)
p_oled.rotate(1)
p_oled.show()
utime.sleep(1)
p_oled.text('Sensor dth11', 14, 0)
p_oled.show()

while True:
    objSensorDht.measure()
    Temperatura = objSensorDht.temperature()
    Humedad = objSensorDht.humidity()
    
    p_oled.text('Temp. = 	C', 0, 20)
    p_oled.text(str(Temperatura), 63, 20)
    
    p_oled.text('Hum. = 	%', 0, 40)
    p_oled.text(str(Humedad), 63, 40)
    
    p_oled.show()
    
    utime.sleep(0.5)
    
    p_oled.text(str(Temperatura), 63, 20, 0)
    p_oled.text(str(Humedad), 63, 40, 0)
    
    