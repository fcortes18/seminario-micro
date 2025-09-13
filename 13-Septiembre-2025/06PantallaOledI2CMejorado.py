from machine import Pin, I2C
import sh1106
import utime

intDelta = 0
strTemporal = "0"

#direccion de fabrica x3C
objI2C = I2C(1, scl=Pin(19), sda=Pin(18))
p_oled = sh1106.SH1106_I2C(128, 64, objI2C)

p_oled.fill(0)
p_oled.rotate(1)
p_oled.show()

utime.sleep_ms(2)
p_oled.text("Tiempo en ms = ", 0, 0)
p_oled.show()

intStart = utime.ticks_ms()
while True:
    intDelta = utime.ticks_diff(utime.ticks_ms(), intStart)
    
    utime.sleep(1)
    
    strTemporal = str(intDelta//1000)

    p_oled.text(strTemporal, 24, 10)
    p_oled.show()
    utime.sleep(0.1) # Tiempo de actualizacion de la pantalla
    p_oled.text(strTemporal, 24, 10, 0)


