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

###あれnumpyってpipする必要あったっけ...まぁいいや

