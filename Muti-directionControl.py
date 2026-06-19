fronanom microbit import *
import tinybit
speed = 200
display.show(Image.SMILE)
sleep(1000)
while True:
    tinybit.car_run(speed)
    sleep(2000)
    tinybit.car_back(speed)
    sleep(2000)
    tinybit.car_right(speed)
    sleep(1000)
    tinybit.car_left(speed)
    sleep(1000)
    tinybit.car_stop()
    sleep(2000)
