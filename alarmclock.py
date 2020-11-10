from pygame import * 
import spidev
import RPi.GPIO as GPIO
from time import sleep, time
from tkinter import *
root = Tk()
x = 0
#Define Variables
delay = 2
ldr_channel = 0
mixer.init()
#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz=1000000
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, (8 + adcnum) << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]  
    return data

l1 = Label(root)
l1.pack(fill=BOTH, expand=1)
gif = PhotoImage(file = 'download.gif')
owl = PhotoImage(file = 'owl.gif')

def clock():
    
    while True:
        ldr_value = readadc(ldr_channel)
        print("LDR Value: %d" % ldr_value)
        sleep(delay)
        break 
    

    if ldr_value >= 900:
        
        GPIO.output(17, GPIO.HIGH)
        sleep(.05)
        GPIO.output(17, GPIO.LOW)
        sleep(.05)
        l1.configure(image=owl)
        
        
        
    
    if ldr_value <= 899:
        GPIO.output(17, GPIO.LOW)
        l1.configure(image=gif)
        mixer.Sound('ocean.wav')
    root.after(1000, clock)
            

clock()        
print("clock")
root.mainloop()
