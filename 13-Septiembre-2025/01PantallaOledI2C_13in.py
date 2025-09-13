from machine import Pin, I2C
import sh1106
import time

objI2C = I2C(1, scl=Pin(19), sda=Pin(18))
p_oled = sh1106.SH1106_I2C(128, 64, objI2C)

p_oled.poweroff()
time.sleep_ms(100)

p_oled.poweron()
time.sleep_ms(100)

p_oled.rotate(1)
p_oled.text("Hola mundito :P", 0, 0)
p_oled.show()
