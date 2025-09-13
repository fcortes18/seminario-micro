from machine import Pin, I2C
import sh1106
import utime

intContador = 0

#direccion de fabrica x3C
objI2C = I2C(1, scl=Pin(19), sda=Pin(18))
p_oled = sh1106.SH1106_I2C(128, 64, objI2C)

p_oled.fill(0)
p_oled.rotate(1)
p_oled.show()

utime.sleep(1)

p_oled.text('Contando=', 0, 0)

while True:
    intContador += 1
    strContador = str(intContador)
    p_oled.text(strContador, 0, 10)
    p_oled.show()
    p_oled.text(strContador, 0, 10, 0)
    utime.sleep(0.01)
    
    


