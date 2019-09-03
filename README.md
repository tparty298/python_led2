# python_led2

- git clone [今回実行したいpythonファイルのあるプロジェクトのgit]
- cd [目的のディレクトリ]
- sudo python3 [目的のファイル].py


- これだけだとダメで、
```
pi@raspberrypi:~/python_led2 $ sudo python3 test.py
Traceback (most recent call last):
  File "test.py", line 2, in <module>
    from neopixel import *
ModuleNotFoundError: No module named 'neopixel'
pi@raspberrypi:~/python_led2 $ 
```


と、neopixelに関するライブラリがないと怒られる。


- そこで、 <https://blog.boochow.com/article/456229607.html>を参考に


###SPI通信を有効化
- sudo raspi-config
- 5 Interfacing Options -> SPI enabled

 
###rpi_ws281xというライブラリをインストールする。
- git clone https://github.com/jgarff/rpi_ws281x 
- cd rpi_ws281x
- sudo apt-get install scons
- scons
- cd python
- sudo apt-get install swig
- sudo python3 ./setup.py install
- cd
- cd [目的のディレクトリへ]
- sudo python3 [目的のファイル].pyで実行可能

##目的のコードでエラーが出る時
###uint32_tがなんちゃら
LED_COUNT=289で
```
led loop: j=286
led loop: j=287
led loop: j=288
Traceback (most recent call last):
  File "test_update_numpyCsv.py", line 33, in <module>
    strip.setPixelColor(j,Color(int(data[j,0]),int(data[0,1]),int(data[0,2])))
  File "/usr/local/lib/python3.7/dist-packages/rpi_ws281x-1.0.0-py3.7-linux-armv7l.egg/neopixel.py", line 118, in setPixelColor
    self._led_data[n] = color
  File "/usr/local/lib/python3.7/dist-packages/rpi_ws281x-1.0.0-py3.7-linux-armv7l.egg/neopixel.py", line 49, in __setitem__
    return ws.ws2811_led_set(self.channel, pos, value)
OverflowError: in method 'ws2811_led_set', argument 3 of type 'uint32_t'
```
が出た時、LEDの数(289)とデータのフォーマットの形(1~289行目まで+-1)の形が合っていない
LEDの数が多いか少ないはず
読み込むデータの1フレーム目を確認、この
    return ws.ws2811_led_set(self.channel, pos, value)g
    return ws.ws2811_led_set(self.channel, pos, value)
