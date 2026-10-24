
from gpiozero import DigitalOutputDevice, PWMOutputDevice
from config import (
    AIN1, AIN2, PWMA,
    BIN1, BIN2, PWMB,
    STBY, SPEED, PWM_FREQ
)

# Motor driver standby
standby = DigitalOutputDevice(STBY, initial_value=False)

# Left motor: channel A
ain1 = DigitalOutputDevice(AIN1, initial_value=False)
ain2 = DigitalOutputDevice(AIN2, initial_value=False)
pwma = PWMOutputDevice(
    PWMA, frequency=PWM_FREQ, initial_value=0
)

# Right motor: channel B
bin1 = DigitalOutputDevice(BIN1, initial_value=False)
bin2 = DigitalOutputDevice(BIN2, initial_value=False)
pwmb = PWMOutputDevice(
    PWMB, frequency=PWM_FREQ, initial_value=0
)


def drive(left_direction, right_direction, speed=SPEED):
    # Stop before changing direction
    pwma.value = 0
    pwmb.value = 0

    ain1.value = left_direction == 1
    ain2.value = left_direction == -1

    bin1.value = right_direction == 1
    bin2.value = right_direction == -1

    speed = max(0.0, min(1.0, speed))

    # Enable the motor driver
    standby.on()

    pwma.value = speed
    pwmb.value = speed


def forward():
    drive(1, 1)


def backward():
    drive(-1, -1)


def turn_left():
    drive(-1, 1)


def turn_right():
    drive(1, -1)


def stop():
    pwma.value = 0
    pwmb.value = 0
    standby.off()


def cleanup():
    stop()
    pwma.close()
    pwmb.close()
    ain1.close()
    ain2.close()
    bin1.close()
    bin2.close()
    standby.close()
