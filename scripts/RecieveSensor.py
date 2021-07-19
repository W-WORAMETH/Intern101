#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import String

sensor1 = 0
sensor2 = 0
sensor3 = 0
sensor4 = 0

Data = Int32MultiArray()
Data.data = []

def callbackSensor(Data):
    sensor1 = Data.data[0]
    sensor2 = Data.data[1]
    sensor3 = Data.data[2]
    sensor4 = Data.data[3]

    rospy.loginfo(rospy.get_caller_id() + "   sensor1 = %s", str(sensor1))
    rospy.loginfo(rospy.get_caller_id() + "   sensor2 = %s", str(sensor2))
    rospy.loginfo(rospy.get_caller_id() + "   sensor3 = %s", str(sensor3))
    rospy.loginfo(rospy.get_caller_id() + "   sensor4 = %s", str(sensor4))

   # rospy.loginfo(rospy.get_caller_id() + "sensor1 = %d", Data[0])
   # rospy.loginfo(rospy.get_caller_id() + "sensor2 = %d", Data[1])
   # rospy.loginfo(rospy.get_caller_id() + "sensor3 = %d", Data[2])
   # rospy.loginfo(rospy.get_caller_id() + "sensor4 = %d", Data[3])



def listener():
    rospy.init_node('RecieveSensor', anonymous=True)
    rospy.Subscriber('sensor', Int32MultiArray, callbackSensor)    
    rospy.spin()

if __name__ == '__main__':
    listener()