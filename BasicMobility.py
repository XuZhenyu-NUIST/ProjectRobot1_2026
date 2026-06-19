from microbit import *
import tinybit
speed = 200
display.show(Image.HAPPY)
sleep(1000)
while True:
    tinybit.car_run(speed)
    sleep(3000)
    tinybit.carB_stop()
    sleep(2000)

