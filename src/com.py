#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32MultiArray
rospy.init_node('com', anonymous=True)
sensor1 = 0
sensor2 = 0
sensor3 = 0
sensor4 = 0



def callbackSensor(data):
    sensor1 = data[0].data
    sensor2 = data[1].data
    sensor3 = data[2].data
    sensor4 = data[3].data

    rospy.loginfo(rospy.get_caller_id() + "sensor1 = %d", sensor1)
    rospy.loginfo(rospy.get_caller_id() + "sensor2 = %d", sensor2)
    rospy.loginfo(rospy.get_caller_id() + "sensor3 = %d", sensor3)
    rospy.loginfo(rospy.get_caller_id() + "sensor4 = %d", sensor4)


def listener():
     rospy.Subscriber('sensor', Int32MultiArray, callbackSensor)    
     rospy.spin()

if __name__ == '__main__':
    listener()