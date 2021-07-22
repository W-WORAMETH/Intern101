#!CPG part
import math
import sys
import rospy
from std_msgs.msg import Float64MultiArray

MI = 0.2
WeightH1_H1 = 1.4
WeightH1_H2 = 0.18 + MI
WeightH2_H2 = 1.4
WeightH2_H1 = -(0.18 + MI) 
activityH1 = 0
activityH2 = 0
outputH1 = 0.01
outputH2 = 0.01

Massage = Float64MultiArray()
Massage.data = []

output = Float64MultiArray()
output.data = []

BiasH1 = 0.0
BiasH2 = 0.0

rospy.init_node('generateCPG', anonymous=True)
rate = rospy.Rate(1)

def cleanAndExit():
    print("Cleaning...")    
    print("Stop Working ...")
    sys.exit()

def sendData(Topic,Massage):
    pub = rospy.Publisher(Topic,Float64MultiArray,queue_size=10)
    rospy.loginfo(Massage)
    pub.publish(Massage)

def generateCPG() :
    global outputH1
    global outputH2
    activityH1 = WeightH1_H1 * outputH1 + WeightH1_H2 * outputH2 + BiasH1
    activityH2 = WeightH2_H2 * outputH2 + WeightH2_H1 * outputH1 + BiasH2

    outputH1 = math.tanh(activityH1)
    outputH2 = math.tanh(activityH2)

    output.data = [outputH1, -outputH1]
    sendData('CPG',output)
    rate.sleep()
 
  


if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            generateCPG()
    except rospy.ROSInterruptException:
            cleanAndExit()
        