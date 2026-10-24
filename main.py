
from motorFunctions import (
    forward, backward,
    turn_left, turn_right,
    stop, cleanup
)
from time import sleep

try:
    print("Moving forward")
    forward()
    sleep(2)
    stop()
    sleep(1)

    print("Turning left")
    turn_left()
    sleep(0.5)
    stop()
    sleep(1)

    print("Moving backward")
    backward()
    sleep(2)
    stop()
    sleep(1)

    print("Turning right")
    turn_right()
    sleep(0.5)
    stop()

finally:
    cleanup()
    print("Program finished")
