
import time
import sys
import RPi.GPIO as GPIO
from std_msgs.msg import Int8MultiArray
from std_msgs.msg import Bool

Solinoid1 = 4
Solinoid2 = 17
Solinoid3 = 27
Solinoid4 = 25
Solinoid5 = 24
Solinoid6 = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)


SolinoidCommand = Int8MultiArray()
SolinoidCommand = [0,1,0,0,0,0]

GPIO.output(Solinoid1,GPIO.LOW)
GPIO.output(Solinoid1,GPIO.LOW)
GPIO.output(Solinoid1,GPIO.HIGH)
GPIO.output(Solinoid1,GPIO.HIGH)
GPIO.output(Solinoid1,GPIO.LOW)
GPIO.output(Solinoid1,GPIO.HIGH)
