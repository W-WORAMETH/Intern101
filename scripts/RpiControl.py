#!/usr/bin/env python3
#from scripts.RecieveSensor import Data
import time
import sys
#import RPi.GPIO as GPIO
from std_msgs.msg import Int16MultiArray
from std_msgs.msg import UInt16MultiArray
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import UInt8
from std_msgs.msg import Bool
import rospy
import math
import numpy as np


rospy.init_node('RpiControl', anonymous=True)
rate = rospy.Rate(1) # 1hz

Dataset = Int16MultiArray()
Dataset.data = []
OldDataset = Int16MultiArray()
OldDataset.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
state = UInt8()


Channal1 = 4
Channal2 = 17
Channal3 = 27
Channal4 = 25
Channal5 = 24
Channal6 = 23

M1 = 18
M2 = 22

#!-----------Define----------

Solenoid1 = Channal1
Solenoid2 = Channal2 
magneticFL = Channal3
magneticFR = Channal4
magneticBL = Channal5
magneticBR = Channal6


#!---------------------------


cmd = bool()
trigger = bool()
trigger = False
Solenoid = 0
#pin
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(Channal1, GPIO.OUT)
# GPIO.setup(Channal2, GPIO.OUT)
# GPIO.setup(Channal3, GPIO.OUT)
# GPIO.setup(Channal4, GPIO.OUT)
# GPIO.setup(Channal5, GPIO.OUT)
# GPIO.setup(Channal6, GPIO.OUT)
# GPIO.setup(M1, GPIO.OUT)
# GPIO.setup(M2, GPIO.OUT)

# GPIO.output(Channal1,GPIO.HIGH)
# GPIO.output(Channal2,GPIO.HIGH)
# GPIO.output(Channal3,GPIO.HIGH)
# GPIO.output(Channal4,GPIO.HIGH)
# GPIO.output(Channal5,GPIO.HIGH)
# GPIO.output(Channal6,GPIO.HIGH)
# GPIO.output(M1,GPIO.LOW)
# GPIO.output(M2,GPIO.LOW)

def cleanAndExit():
    print("Cleaning...")
    #GPIO.cleanup()    
    print("Stop Working ...")
    sys.exit()


def triggerCPG(Topic,Massage):
    pub = rospy.Publisher(Topic,Bool,queue_size=10)
    rospy.loginfo(Massage)
    pub.publish(Massage)

FrontCPG = float()
BackCPG = float()

def CmdChannal(Channal,cmd):
    pass
    print("def Cmd")
    if(cmd == 1):
        # GPIO.output(Channal,GPIO.HIGH)
        print("GPIO " + str(Channal) +" = "+ str(cmd) )
    elif(cmd == 0):
        # GPIO.output(Solenoid,GPIO.LOW)
        print("GPIO " + str(Channal) +" = "+ str(cmd) )
    else:
        print("error : command must be 0 or 1")

def toggleChannal(button):
    pass
    Sl = 0
    if(button ==8):     Sl = Channal1
    elif(button ==9):   Sl = Channal2
    elif(button ==10):  Sl = Channal3
    elif(button ==11):  Sl = Channal4
    elif(button ==12):  Sl = Channal5
    elif(button ==13):  Sl = Channal6

    elif(button ==14):  Sl = M1
    elif(button ==15):  Sl = M2
    # CmdChannal(Sl,not(GPIO.input(Sl)))


def callbackCPG(CPG):
    FrontCPG = CPG.data[0]
    BackCPG = CPG.data[1]
    pass

def sequenceRobotForward() :
    global Solenoid
    if(FrontCPG == 0)   : FrontMagnetic = 1
    elif(FrontCPG > 0)  : FrontMagnetic = 1
    elif(FrontCPG < 0)  : FrontMagnetic = 0
    
    if(BackCPG == 0)    : BackMagnetic = 1
    elif(BackCPG > 0)   : BackMagnetic = 1
    elif(BackCPG < 0)   : BackMagnetic = 0

    if(FrontCPG > 0.5)  : Solenoid = 1
    elif(FrontCPG < -0.5) : Solenoid = 0


    # can seperated to another function if create more than one direction of seq 
    if(FrontMagnetic == 1) : 
        CmdChannal(magneticFL,1)
        CmdChannal(magneticFR,1)
    elif(FrontMagnetic == 0) : 
        CmdChannal(magneticFL,0)
        CmdChannal(magneticFR,0)
    if(BackMagnetic == 1) : 
        CmdChannal(magneticBL,1)
        CmdChannal(magneticBR,1)
    elif(BackMagnetic == 0) : 
        CmdChannal(magneticBL,0)
        CmdChannal(magneticBR,0)
    if(Solenoid == 1):
        CmdChannal(Solenoid1,1)
        CmdChannal(Solenoid2,1)
    elif(Solenoid == 0):
        CmdChannal(Solenoid1,0)
        CmdChannal(Solenoid2,0)

    

def callbackSensor(Dataset):


    if (Dataset.data != OldDataset.data):
        #debouce and do one time when press
        
        if(Dataset.data[19]>=8 and Dataset.data[19]<=15):  #digital input
            #print(Dataset)
            button = Dataset.data[19]
            #print(button)
            #print(Dataset.data[19])
            state = Dataset.data[button] - OldDataset.data[button]  
            inputcmd = state   #use state because want rising adge
            if inputcmd == 1 :  #rising adge occure
                print("prp toggle")
                toggleChannal(button)
        
         
        if(Dataset.data[19] == 7):  #! must be edit
            print("receive1")
            button = Dataset.data[19]
            inputcmd = Dataset.data[button]
            if inputcmd == -32767: #! must be edit
                print("receive2")
                global trigger
                trigger = True
                sequenceRobotForward()

        OldDataset.data = Dataset.data    



            


        
        # CmdSolenoid(Solenoid1,cmd.data[19])
        # CmdSolenoid(Solenoid2,cmd.data[1])
        # CmdSolenoid(Solenoid3,cmd.data[2])
        # CmdSolenoid(Solenoid4,cmd.data[3])
        # CmdSolenoid(Solenoid5,cmd.data[4])
        # CmdSolenoid(Solenoid6,cmd.data[5])
        # CmdSolenoid(Solenoid6,cmd.data[6])


        # rospy.loginfo(rospy.get_caller_id() + "   sensor1 = %s", str(cmd.data[19]))
        #rospy.loginfo(Dataset)
        # rospy.loginfo(rospy.get_caller_id() + "   sensor2 = %s", str(cmd.data[1]))
        # rospy.loginfo(rospy.get_caller_id() + "   sensor3 = %s", str(cmd.data[2]))
        # rospy.loginfo(rospy.get_caller_id() + "   sensor4 = %s", str(cmd.data[3]))
        # rospy.loginfo(rospy.get_caller_id() + "   sensor5 = %s", str(cmd.data[4]))
        # rospy.loginfo(rospy.get_caller_id() + "   sensor6 = %s", str(cmd.data[5]))


    

def listener():
    triggerCPG('trigger',trigger)
    rospy.Subscriber('joyStick',Int16MultiArray, callbackSensor) 
    rospy.Subscriber('CPG',Float32MultiArray, callbackCPG)       
    #rospy.spin()

if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            listener()
            
    except rospy.ROSInterruptException:
            cleanAndExit()
        
  
    

    # GPIO.output(Solenoid1,GPIO.LOW)
    # GPIO.output(Solenoid2,GPIO.LOW)
    # GPIO.output(Solenoid3,GPIO.HIGH)
    # GPIO.output(Solenoid4,GPIO.HIGH)
    # GPIO.output(Solenoid5,GPIO.LOW)
    # GPIO.output(Solenoid6,GPIO.HIGH)

