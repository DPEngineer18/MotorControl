from motors import forward, backward, turn_left, turn_right, stop
from time import sleep

try:
    forward()
    sleep(2)
    stop()
    sleep(1)

    turn_left()
    sleep(0.5)
    stop()
    sleep(1)

    backward()
    sleep(2)
    stop()
    sleep(1)

    turn_right()
    sleep(0.5)
    stop()

finally:
    stop()