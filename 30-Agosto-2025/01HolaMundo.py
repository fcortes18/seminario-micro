import machine
import utime


pinLed = machine.Pin("LED", machine.Pin.OUT)

while True:
    pinLed.on()
    utime.sleep(0.5)
    pinLed.off()
    utime.sleep(0.5)