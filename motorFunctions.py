from machine import Pin, PWM
from time import sleep
import config as cfg

ain1 = Pin(cfg.LEFT_IN1, Pin.out)
ain2 = Pin(cfg.LEFT_IN2, Pin.out)
bin1 = Pin(cfg.RIGHT_IN1, Pin.out)
bin2 = Pin(cfg.RIGHT_IN2, Pin.out)

pmwa = PMW(Pin(cfg.LEFT_PMW), freq=cfg.PMW_FREQ)
pmwb = PMW(Pin(cfg.RIGHT_PMW), freq=cfg.PMW_FREQ)

standby = Pin(cfg.STBY, Pin.OUT)

standby.value(0)
pmwa.duty_u16(0)
pmwb.duty_u16(0)

def set_motor(in1,in2,pmw,direction,speed):
    speed = max(0,min(speed,65535))

    pmw.duty_u16(0)

    if (direction == 1):
        in1.value(1)
        in2.value(0)
    elif (direction == -1):
        in1.value(0)
        in2.value(1)
    else:
        in1.value(0)
        in2.value(0)
        return

    pmw.duty_u16(speed)

def drive(left_direction,right_direction,speed=cfg.SPEED):
    set_motor(ain1,ain2,pmwa,left_direction,speed)
    set_motor(bin1,bin2,pmwb,right_direction,speed)
    standby.value(1)

def forward(): drive(1,1)

def backward(): drive(-1,-1)

def left(): drive(-1,1)

def right(): drive(1,-1)
