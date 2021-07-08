#!/usr/bin/env python
import rospy
from std_msgs.msg import String

sensor1 = 0
sensor2 = 0
sensor3 = 0
sensor4 = 0



def callbackSensor1(data):
    sensor1 = data.data
    rospy.loginfo(rospy.get_caller_id() + "sensor1 = %s", data.data)


def callbackSensor2(data):
    rospy.loginfo(rospy.get_caller_id() + "sensor2 = %s", data.data)

def callbackSensor3(data):
    rospy.loginfo(rospy.get_caller_id() + "sensor3 = %s", data.data)

def callbackSensor4(data):
    rospy.loginfo(rospy.get_caller_id() + "sensor4 = %s", data.data)

def listener():

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('sensor1', int, callbackSensor1)
    rospy.Subscriber('sensor2', int, callbackSensor2)
    rospy.Subscriber('sensor3', int, callbackSensor3)
    rospy.Subscriber('sensor4', int, callbackSensor4)
    rospy.spin()

if __name__ == '__main__':
    listener()