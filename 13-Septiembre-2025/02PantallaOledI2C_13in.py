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

time.sleep(2)

p_oled.fill(0) #relleno 0 fondo negro, 1 fondo blanco

p_oled.fill_rect(0, 0, 32, 32, 1) #recta (X1, Y1, X2, Y2)
p_oled.fill_rect(2, 2, 28, 28, 0)

p_oled.vline(9, 8, 22, 1)
p_oled.vline(16, 2, 22, 1)
p_oled.vline(23, 8, 22, 1)

p_oled.fill_rect(26, 24, 2, 4, 1)

p_oled.text('Micropython', 40, 0, 1)
p_oled.text('SSD1306', 40, 12, 1)
p_oled.text('OLED 128x64', 40, 24, 1)
p_oled.show()









