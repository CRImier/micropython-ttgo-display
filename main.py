from machine import Pin, SPI
from time import sleep
import random
import network

import st7789py as st7789
from st7789py import color565 as c565

ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)
#ap_if.config(essid="\U0001F4A9", password="atpisies1337")
ap_if.config(essid="Epstein_Didn't_Kill_Himself", password="atpisies1337")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(False)
#sta_if.connect("NTA2019", "notroll2019")

gpios = [32, 33, 25]
pins = [Pin(i, Pin.OUT) for i in gpios]

Pin(4, Pin.OUT).value(1)

spi = SPI(2, sck=Pin(18), mosi=Pin(19), miso=Pin(23),
  baudrate=20*1000*1000, polarity=1, phase=0)

spi2 = SPI(1, sck=Pin(21), mosi=Pin(13), miso=Pin(12),
  baudrate=20*1000*1000, polarity=0, phase=0)

display = st7789.ST7789(
    spi, 135, 240,
    reset=Pin(23, Pin.OUT),
    dc=Pin(16, Pin.OUT),
    cs = Pin(5, Pin.OUT)
)
display.start_x = 52
display.start_y = 40

def blink_leds():
    while True:
        for i, pin in enumerate(pins):
            last_pin = pins[i-1] if pin != 0 else pins[-1]
            last_pin.value(True)
            pin.value(False)
            sleep(0.3)

#import _thread
#_thread.start_new_thread(blink_leds, ())

display.init()
#while True:
"""if True:
    display.fill(
        st7789.color565(
            random.getrandbits(8),
            random.getrandbits(8),
            random.getrandbits(8),
        ),
    )
    sleep(2)"""

with open("file.bgr565", 'r') as f:
    buf = f.read()
l = len(buf)
display.blit_buffer(buf, 0, 0, display.width, int(l/display.width))

"""

oe = Pin(2, Pin.OUT)
oe.off()
rst = Pin(17, Pin.OUT)
rst.on()
cs = Pin(15, Pin.OUT)
cs.on()

b = bytearray(3)
b[0] = b[1] = b[2] = 0b10101010

def shiftOut(b):
    cs.off()
    spi2.write(b)
    cs.on()

num_boards = 3
pwm_resolution = 256
divisor = 4

l = list(range(0, pwm_resolution, divisor))+list(reversed(range(0, pwm_resolution-1, divisor)))
m = list(range(0, pwm_resolution, divisor))
e = bytearray(num_boards)
for i in range(num_boards):
    e[i] = 0
b = bytearray(num_boards)

pwm_range = list(range(256))
port_count = 8*num_boards
port_range = list(range(port_count))
board_range = list(range(num_boards))

wave_len = port_count//2

step = pwm_resolution/(wave_len//2)
wave_arr = [(i+1)*step for i in range(wave_len//2)]
wave_arr = wave_arr+list(reversed(wave_arr))+[0 for i in range(port_count-wave_len)]

while True:
    for i in pwm_range:
        val = 0
        for p in port_range:
            if i < wave_arr[p]:
                val |= 1 << p
            for d in board_range:
                b[num_boards-(d+1)] = (val >> d*8) & 0xff
            shiftOut(b)
    #print(wave_arr)
    wave_arr.append(wave_arr.pop(0))

while True:
    for a in port_range:
        i = 1 << a
        print(b)
        for d in board_range:
            b[num_boards-(d+1)] = (i >> d*8) & 0xff
        for j in l:
            for k in m:
                if k < j:
                    cs.off()
                    spi2.write(b)
                    cs.on()
                else:
                    cs.off()
                    spi2.write(e)
                    cs.on()

"""
