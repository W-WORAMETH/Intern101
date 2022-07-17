#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16MultiArray
import sys
import time
#from intern101.hx711 import HX711

def cleanAndExit():
    print("Cleaning...")
    #GPIO.cleanup()    
    print("Stop Working ...")
    sys.exit()


# rospy.init_node('SendSolenoid', anonymous=True)
rospy.init_node('joyStick', anonymous=True)

rate = rospy.Rate(1) # 1hz
Massage = Int16MultiArray()
Massage.data = []

Data = Int16MultiArray()
Data.data = []


def sendData(Topic,Massage):
    pub = rospy.Publisher(Topic,Int16MultiArray,queue_size=10)
    rospy.loginfo(Massage)
    pub.publish(Massage)

def ReadKeyboard():
    rospy.loginfo("Please Enter command [Example cmd :0 1 0 1 0 1 ]")
    rospy.loginfo("cmd : ")
    cmd1,cmd2,cmd3,cmd4,cmd5,cmd6 = [int(e) for e in input().split()]
    
    Data.data = [int(cmd1),int(cmd2),int(cmd3),int(cmd4),int(cmd5),int(cmd6)]
    if(not rospy.is_shutdown()): 
        rospy.loginfo(rospy.get_caller_id() + "   cmd1 = %s", str(Data.data[0]))
        rospy.loginfo(rospy.get_caller_id() + "   cmd2 = %s", str(Data.data[1]))
        rospy.loginfo(rospy.get_caller_id() + "   cmd3 = %s", str(Data.data[2]))
        rospy.loginfo(rospy.get_caller_id() + "   cmd4 = %s", str(Data.data[3]))
        rospy.loginfo(rospy.get_caller_id() + "   cmd5 = %s", str(Data.data[4]))
        rospy.loginfo(rospy.get_caller_id() + "   cmd6 = %s", str(Data.data[5]))
        
        sendData('SendSolenoid',Data)
    
    rate.sleep()


def createCommand():

    Data.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    sendData('joyStick',Data)
    time.sleep(3)

    Data.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,16]
    sendData('joyStick',Data)
    time.sleep(0.1)
    Data.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16]
    sendData('joyStick',Data)
    time.sleep(0.1)
    Data.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,17]
    sendData('joyStick',Data)
    time.sleep(0.1)
    Data.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7]
    sendData('joyStick',Data)
    time.sleep(0.1)

    Data.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    sendData('joyStick',Data)
    time.sleep(0.1)

    Data.data = [0,0,0,0,0,-32767,0,0,0,0,0,0,0,0,0,0,0,0,0,5] #go front
    sendData('joyStick',Data)
    time.sleep(30)
    Data.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5]
    sendData('joyStick',Data)
    time.sleep(2)

    

    #inc MI
    Data.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,14]
    sendData('joyStick',Data)
    time.sleep(0.2)
    Data.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,14]
    sendData('joyStick',Data)
    time.sleep(0.2)
    

    Data.data = [0,0,0,0,0,-32767,0,0,0,0,0,0,0,0,0,0,0,0,0,5] #go front
    sendData('joyStick',Data)
    time.sleep(30)
    Data.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5]
    sendData('joyStick',Data)
    time.sleep(2)

    

    #inc MI
    Data.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,14]
    sendData('joyStick',Data)
    time.sleep(0.2)
    Data.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,14]
    sendData('joyStick',Data)
    time.sleep(0.2)


    Data.data = [0,0,0,0,0,-32767,0,0,0,0,0,0,0,0,0,0,0,0,0,5] #go front
    sendData('joyStick',Data)
    time.sleep(30)
    Data.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5]
    sendData('joyStick',Data)
    time.sleep(2)

    

    #inc MI
    Data.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,14]
    sendData('joyStick',Data)
    time.sleep(0.2)
    Data.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,14]
    sendData('joyStick',Data)
    time.sleep(0.2)



if __name__ == '__main__':
    try:

        createCommand()
        # while not rospy.is_shutdown():
        #     # ReadKeyboard()
        #     createCommand()

    except rospy.ROSInterruptException:
            cleanAndExit()
        
