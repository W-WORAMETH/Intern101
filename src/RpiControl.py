
import time
import sys
import RPi.GPIO as GPIO
from std_msgs.msg import Int8MultiArray
from std_msgs.msg import bool

Solinoid1 = 4
Solinoid2 = 17
Solinoid3 = 27
Solinoid4 = 25
Solinoid5 = 24
Solinoid6 = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(Solinoid1, GPIO.OUT)
GPIO.setup(Solinoid2, GPIO.OUT)
GPIO.setup(Solinoid3, GPIO.OUT)
GPIO.setup(Solinoid4, GPIO.OUT)
GPIO.setup(Solinoid5, GPIO.OUT)
GPIO.setup(Solinoid6, GPIO.OUT)


SolinoidCommand = Int8MultiArray()
SolinoidCommand = [0,1,0,0,0,0]

GPIO.out(Solinoid1,bool(SolinoidCommand.data[0]))
GPIO.out(Solinoid1,bool(SolinoidCommand.data[1]))
GPIO.out(Solinoid1,bool(SolinoidCommand.data[2]))
GPIO.out(Solinoid1,bool(SolinoidCommand.data[3]))
GPIO.out(Solinoid1,bool(SolinoidCommand.data[4]))
GPIO.out(Solinoid1,bool(SolinoidCommand.data[5]))
