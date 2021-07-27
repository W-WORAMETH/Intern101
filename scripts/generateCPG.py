#!CPG part
import math
import sys
import time
import rospy
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Int16MultiArray
from std_msgs.msg import Bool
#MI = 0.2  #best MI = 0.2
MI = 0.2
WeightH1_H1 = 1.4
WeightH1_H2 = -(0.18 + MI)
WeightH2_H2 = 1.4
WeightH2_H1 = (0.18 + MI) 
activityH1 = 0
activityH2 = 0
outputH1 = 0.0001
outputH2 = 0.0001
BiasH1 = 0.0
BiasH2 = 0.0


Massage = Float64MultiArray()
Massage.data = []

output = Float64MultiArray()
output.data = [0,0]
trigger = Bool()
trigger = False

Dataset = Int16MultiArray()
Dataset.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

Input_Dataset = Int16MultiArray()
Input_Dataset.data = []

OldDataset = Int16MultiArray()
OldDataset.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

rospy.init_node('generateCPG', anonymous=True)
rate = rospy.Rate(10) #5

#test 1

def restartCPG():
    global MI
    global WeightH1_H1
    global WeightH1_H2
    global WeightH2_H2
    global WeightH2_H1
    global activityH1 
    global activityH2
    global activityH2
    global outputH1
    global outputH2

    WeightH1_H1 = 1.4
    WeightH1_H2 = -0.18 + MI

    WeightH2_H1 = (0.18 + MI) 
    activityH1 = 0
    activityH2 = 0
    outputH1 = 0.1
    outputH2 = 0.1

def cleanAndExit():
    print("Cleaning...")    
    print("Stop Working ...")
    sys.exit()

def sendData(Topic,Massage):
    pub = rospy.Publisher(Topic,Float64MultiArray,queue_size=10)
    #rospy.loginfo(Massage)
    pub.publish(Massage)

def generateCPG() :
    global MI
    global WeightH1_H1
    global WeightH1_H2
    global WeightH2_H2
    global WeightH2_H1
    global activityH1 
    global activityH2
    global activityH2
    global outputH1
    global outputH2

    activityH1 = WeightH1_H1 * outputH1 + WeightH1_H2 * outputH2 + BiasH1
    activityH2 = WeightH2_H2 * outputH2 + WeightH2_H1 * outputH1 + BiasH2

    outputH1 = math.tanh(activityH1)
    outputH2 = math.tanh(activityH2)

    output.data = [outputH1, outputH2]
    rate.sleep()
    
    
  

def callbackJoy(Input_Dataset):
    global Dataset
    Dataset.data = Input_Dataset.data
   

#test1  

    
def listener():
    global trigger
    rospy.Subscriber('joyStick',Int16MultiArray, callbackJoy)   

    
    global Dataset
    global MI
    
    if (Dataset.data != OldDataset.data):
        
        if(Dataset.data[19] == 7):  #! must be edit
            button = Dataset.data[19]
            inputcmd = Dataset.data[button]
            if inputcmd == -32767: #! must be edit
                print("receive FW")   
                trigger = True
            elif inputcmd == 32767: #! must be edit
                print("receive BW")   
                trigger = True
            elif inputcmd == 0: #! must be edit
                print("no cmd receive")
                trigger = False
            
        elif(Dataset.data[19] == 6):  #! must be edit
            button = Dataset.data[19]
            inputcmd = Dataset.data[button]
            if inputcmd == -32767: #! must be edit
                print("receive Left")   
                trigger = True
            elif inputcmd == 32767: #! must be edit
                print("receive Right")   
                trigger = True
            elif inputcmd == 0: #! must be edit
                print("no cmd receive")
                trigger = False

        if(Dataset.data[19]== 18 ):  #digital input
            button = Dataset.data[19]
            state = Dataset.data[button] - OldDataset.data[button]  
            inputcmd = state   #use state because want rising adge
            if inputcmd == 1 :  #rising adge occure
                MI = MI+0.01
                print("[ Increase MI ] : MI = ", MI)
                restartCPG()
        
        if(Dataset.data[19]== 17 ):  #digital input

            button = Dataset.data[19]
            state = Dataset.data[button] - OldDataset.data[button]  
            inputcmd = state   #use state because want rising adge
            if inputcmd == 1 :  #rising adge occure
                MI = MI-0.01
                print("[ Decrease MI ] : MI = ", MI)
                restartCPG()
               
        Dataset.data = OldDataset.data    
    #rospy.spin()

    if(trigger == True):
        generateCPG()  #runnew cpg value
        sendData('CPG',output)
    if(trigger == False):
        sendData('CPG',output)
        rate.sleep()





if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            listener()
            
    except rospy.ROSInterruptException:
            cleanAndExit()
    
        


