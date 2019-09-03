import time
from neopixel import *
import argparse
import numpy as np

LED_COUNT      = 288      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

FPS = 60
loop_count=0
loop_start_time=0

if __name__ == '__main__':
   print("start program")
   strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
   strip.begin()
   print("file read start")
   data = np.genfromtxt("output.txt",delimiter=",", skip_header=0,dtype='int')
   print("file read end")
   print("start loop")
   while True:
      loop_start_time=time.time()
      start_index=loop_count*(LED_COUNT+1)
      for j in range(LED_COUNT):
         strip.setPixelColor(j,Color(int(data[start_index+j,0]),int(data[start_index+j,1]),int(data[start_index+j,2])$
         #print(data[j,0])
      strip.show()
      #time.sleep(1/FPS)
      loop_count=loop_count+1
      print("loop time:"+str(time.time()-loop_start_time))

