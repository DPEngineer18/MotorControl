from machine import Pin, PWM
from time import sleep
import config as cfg

left_ini1 = Pin(cfg.LEFT_IN1, Pin.out)
left_ini2 = Pin(cfg.LEFT_IN2, Pin.out)
right_ini1 = Pin(cfg.RIGHT_IN1, Pin.out)
right_ini2 = Pin(cfg.RIGHT_IN2, Pin.out)

left_pmw = PMW(Pin(cfg.LEFT_PMW), freq=cfg.PMW_FREQ)
right_pmw = PMW(Pin(cfg.RIGHT_PMW), freq=cfg.PMW_FREQ)

left_stby = Pin(cfg.LEFT_STBY, Pin.out)
right_stby = Pin(cfg.RIGHT_STBY, Pin.out)


def forward(): return

def backward(): return

def left(): return

def right(): return

def stop(): return
