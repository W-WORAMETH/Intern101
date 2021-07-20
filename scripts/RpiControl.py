#!/usr/bin/env python3
#from scripts.RecieveSensor import Data
import time
import sys
import RPi.GPIO as GPIO
from std_msgs.msg import Int16MultiArray
from std_msgs.msg import UInt16MultiArray
from std_msgs.msg import UInt8
from std_msgs.msg import Bool
import rospy

rospy.init_node('RpiControl', anonymous=True)
rate = rospy.Rate(1) # 1hz

Dataset = Int16MultiArray()
Dataset.data = []
OldDataset = Int16MultiArray()
OldDataset.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
state = UInt8()


Solenoid1 = 4
Solenoid2 = 17
Solenoid3 = 27
Solenoid4 = 25
Solenoid5 = 24
Solenoid6 = 23

M1 = 18
M2 = 22

cmd = bool()

#pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.output(Solenoid1,GPIO.HIGH)
GPIO.output(Solenoid2,GPIO.HIGH)
GPIO.output(Solenoid3,GPIO.HIGH)
GPIO.output(Solenoid4,GPIO.HIGH)
GPIO.output(Solenoid5,GPIO.HIGH)
GPIO.output(Solenoid6,GPIO.HIGH)

# def sendData(Topic,Massage):
#     pub = rospy.Publisher(Topic,Int8MultiArray,queue_size=10)
#     rospy.loginfo(Massage)
#     pub.publish(Massage)

def CmdSolenoid(Solenoid,cmd):
    pass
    print("def Cmd")
    if(cmd == 1):
        GPIO.output(Solenoid,GPIO.HIGH)
        print("GPIO " + str(Solenoid) +" = "+ str(cmd) )
    elif(cmd == 0):
        GPIO.output(Solenoid,GPIO.LOW)
        print("GPIO " + str(Solenoid) +" = "+ str(cmd) )
    else:
        print("error : command must be 0 or 1")
#hello



def callbackSensor(Dataset):

    if (Dataset.data != OldDataset.data):
        #debouce and do one time when press
        
        if(Dataset.data[19]>=8 and Dataset.data[19]<=15):  #digital input
            #print(Dataset)
            button = Dataset.data[19]
            # print(button)
            print(Dataset.data[19])
            state = Dataset.data[button] - OldDataset.data[button]  
            inputcmd = state   #use state because want rising adge
            if inputcmd == 1 :  #rising adge occure
                print("prp toggle")
                toggleSolenoid(button)
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

def toggleSolenoid(button):
    pass
    Sl = 0
    if(button ==8): Sl = Solenoid1
    elif(button ==9): Sl = Solenoid2
    elif(button ==10): Sl = Solenoid3
    elif(button ==11): Sl= Solenoid4
    elif(button ==12): Sl = Solenoid5
    elif(button ==13): Sl = Solenoid6
    elif(button ==14): Sl = M1
    elif(button ==15): Sl = M2
    CmdSolenoid(Sl,not(GPIO.input(Sl)))

    

def listener():
    rospy.Subscriber('joyStick',Int16MultiArray, callbackSensor)    
    rospy.spin()

if __name__ == '__main__':
    listener()  
    print("fvck")  

    

    # GPIO.output(Solenoid1,GPIO.LOW)
    # GPIO.output(Solenoid2,GPIO.LOW)
    # GPIO.output(Solenoid3,GPIO.HIGH)
    # GPIO.output(Solenoid4,GPIO.HIGH)
    # GPIO.output(Solenoid5,GPIO.LOW)
    # GPIO.output(Solenoid6,GPIO.HIGH)

