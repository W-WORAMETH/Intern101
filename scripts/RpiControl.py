#!/usr/bin/env python3
import time
import sys
import RPi.GPIO as GPIO
from std_msgs.msg import Int8MultiArray
from std_msgs.msg import Bool
import rospy

rospy.init_node('RpiControl', anonymous=True)
rate = rospy.Rate(1) # 1hz

Data = Int8MultiArray()
Data.data = []
cmd = Int8MultiArray()
cmd = []

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

def sendData(Topic,Massage):
    pub = rospy.Publisher(Topic,Int8MultiArray,queue_size=10)
    rospy.loginfo(Massage)
    pub.publish(Massage)

def CmdSolenoid(Solenoid,cmd):
    if(cmd == 1):
        GPIO.output(Solenoid,GPIO.HIGH)
    elif(cmd == 0):
        GPIO.output(Solenoid,GPIO.LOW)
    else:
        print("error : command must be 0 or 1")

SolenoidCommand = Int8MultiArray()




def listener():
    rospy.init_node('RecieveSensor', anonymous=True)
    rospy.Subscriber('sensor', Int8MultiArray, callbackSensor)    
    rospy.spin()

if __name__ == '__main__':
    listener()

def callbackSensor(Data):

    if (Data.data != cmd.data):
        cmd.data = Data.data
        CmdSolenoid(Solenoid1,cmd[0].data)
        CmdSolenoid(Solenoid2,cmd[1].data)
        CmdSolenoid(Solenoid3,cmd[2].data)
        CmdSolenoid(Solenoid4,cmd[3].data)
        CmdSolenoid(Solenoid5,cmd[4].data)
        CmdSolenoid(Solenoid6,cmd[5].data)

        rospy.loginfo(rospy.get_caller_id() + "   sensor1 = %s", str(cmd[0].data))
        rospy.loginfo(rospy.get_caller_id() + "   sensor2 = %s", str(cmd[1].data))
        rospy.loginfo(rospy.get_caller_id() + "   sensor3 = %s", str(cmd[2].data))
        rospy.loginfo(rospy.get_caller_id() + "   sensor4 = %s", str(cmd[3].data))
        rospy.loginfo(rospy.get_caller_id() + "   sensor5 = %s", str(cmd[3].data))
        rospy.loginfo(rospy.get_caller_id() + "   sensor6 = %s", str(cmd[3].data))
    
    

while(True) :
    

    

    # GPIO.output(Solenoid1,GPIO.LOW)
    # GPIO.output(Solenoid2,GPIO.LOW)
    # GPIO.output(Solenoid3,GPIO.HIGH)
    # GPIO.output(Solenoid4,GPIO.HIGH)
    # GPIO.output(Solenoid5,GPIO.LOW)
    # GPIO.output(Solenoid6,GPIO.HIGH)

