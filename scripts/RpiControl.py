#!/usr/bin/env python3
import time
import sys
import RPi.GPIO as GPIO
from std_msgs.msg import Int8MultiArray
from std_msgs.msg import Bool

Solenoid1 = 4
Solenoid2 = 17
Solenoid3 = 27
Solenoid4 = 25
Solenoid5 = 24
Solenoid6 = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

def CmdSolenoid(Solenoid,cmd):
    if(cmd == 1):
        GPIO.output(Solenoid,GPIO.HIGH)
    elif(cmd == 0):
        GPIO.output(Solenoid,GPIO.LOW)
    else:
        print("error : command must be 0 or 1")

SolenoidCommand = Int8MultiArray()

while(True) :
    
    cmd1,cmd2,cmd3,cmd4,cmd5,cmd6 = [int(e) for e in input().split(",")]

    CmdSolenoid(Solenoid1,cmd1)
    CmdSolenoid(Solenoid2,cmd2)
    CmdSolenoid(Solenoid3,cmd3)
    CmdSolenoid(Solenoid4,cmd4)
    CmdSolenoid(Solenoid5,cmd5)
    CmdSolenoid(Solenoid6,cmd6)

    # GPIO.output(Solenoid1,GPIO.LOW)
    # GPIO.output(Solenoid2,GPIO.LOW)
    # GPIO.output(Solenoid3,GPIO.HIGH)
    # GPIO.output(Solenoid4,GPIO.HIGH)
    # GPIO.output(Solenoid5,GPIO.LOW)
    # GPIO.output(Solenoid6,GPIO.HIGH)

