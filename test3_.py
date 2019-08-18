import time
from neopixel import *
import argparse
import numpy as np

LED_COUNT      = 289      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

FPS = 60
elapsed_time=0
start=0
led_loop_count=0

if __name__ == '__main__':
   print('メイン関数を読み始める')
   strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
   strip.begin()
   print('ファイルオープン')
   file=open('output.txt')
   print('ライン読み込む')
   lines=file.readlines()
   col_ary=np.zeros((LED_COUNT,3))
   print('点灯プロセスに入ります')
   for line in lines:
       line_=line.strip().split(',')
       if int(line_[1])>=0:
           col_ary[led_loop_count][0]=int(line_[1])
           col_ary[led_loop_count][1]=int(line_[0])
           col_ary[led_loop_count][2]=int(line_[2])
           led_loop_count=led_loop_count+1
       else:
            led_loop_count=0
            print("点灯")
            elapsed_time=time.time()-start
            print(elapsed_time)
            start=time.time()
            for j in range(LED_COUNT):
                strip.setPixelColor(j,Color(int(col_ary[j][0]),int(col_ary[j][1]),int(col_ary[j][2])))
            strip.show()
            time.sleep(1/FPS)