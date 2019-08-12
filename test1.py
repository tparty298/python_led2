import time
from neopixel import *
import argparse
import numpy as np

# LED strip configuration:
LED_COUNT      = 289      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/$
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor$
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

#Play variable
FPS = 30
LOOP_NUM=10000

if __name__ == '__main__':
   strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
   # Intialize the library (must be called once before other functions).
   strip.begin()
   in_f=file('output.txt','r')
   n=LOOP_NUM
   col_ary=np.zeros((n,LED_COUNT,3))
   print 'read'
   line_num=0
   n_index=0
   for line in in_f:
      line_=line.strip().split(',')
      if int(line_[1])>=0:
         col_ary[n_index][line_num][0]=int(line_[1])
         col_ary[n_index][line_num][1]=int(line_[0])
         col_ary[n_index][line_num][2]=int(line_[2])
         line_num=line_num+1
      else:
         line_num=0
         n_index=n_index+1
   print 'read finish'

   for i in range(n):
      for j in range(LED_COUNT):
         strip.setPixelColor(j,Color(int(col_ary[i][j][0]),int(col_ary[i][j][1]),int(col_ary[i][j][2])))#GRB
      strip.show()
      time.sleep(1/FPS)
