from microbit import *
import tinybit

BASE_SPEED = 160

def run_custom_path():
    tinybit.car_run(BASE_SPEED)
    sleep(3000)
    tinybit.car_right(BASE_SPEED)
    sleep(1000)
    tinybit.car_run(BASE_SPEED)
    sleep(2000)
    tinybit.car_left(BASE_SPEED)
    sleep(1000)
    tinybit.car_back(BASE_SPEED)
    sleep(2000)
    tinybit.car_stop()
display.show(Image.HAPPY)
sleep(1000)

while True:
    run_custom_path()
    tinybit.car_stop()
    sleep(3000)
