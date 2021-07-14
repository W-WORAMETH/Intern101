#!/usr/bin/env python
from array import array
import rospy
from std_msgs.msg import Int32MultiArray

import time
import sys
#import RPi.GPIO as GPIO
rospy.init_node('rpi', anonymous=True)
rate = rospy.Rate(1) # 1hz
Massage = Int32MultiArray()
Massage.data = []

Data = Int32MultiArray()
Data.data = []

def sendData(Topic,Massage):
    pub = rospy.Publisher(Topic,Int32MultiArray,queue_size=10)
    rospy.loginfo(Massage)
    pub.publish(Massage)


def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
       GPIO.cleanup()
        
    print("Bye!")
    sys.exit()

EMULATE_HX711=False
if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

hx1 = HX711(6,5)
hx2 = HX711(19,13)
hx3 = HX711(21,26)
hx4 = HX711(16,20)


hx1.set_reading_format("MSB", "MSB")
hx2.set_reading_format("MSB", "MSB")
hx3.set_reading_format("MSB", "MSB")
hx4.set_reading_format("MSB", "MSB")


hx1.set_reference_unit(1)
hx2.set_reference_unit(1)
hx3.set_reference_unit(1)
hx4.set_reference_unit(1)


hx1.reset()
hx2.reset()
hx3.reset()
hx4.reset()

# to use both channels, you'll need to tare them both
#hx.tare_A()
#hx.tare_B()

def ReadSensor():
    val1 = hx1.get_weight()
    val2 = hx2.get_weight()
    val3 = hx3.get_weight()
    val4 = hx4.get_weight()

    rospy.loginfo(rospy.get_caller_id() + "   sensor1 = %s", str(val1))
    rospy.loginfo(rospy.get_caller_id() + "   sensor2 = %s", str(val2))
    rospy.loginfo(rospy.get_caller_id() + "   sensor3 = %s", str(val3))
    rospy.loginfo(rospy.get_caller_id() + "   sensor4 = %s", str(val4))

   

  #  print("CH1 = %d" %(val1))
  #  print("CH2 = %d" %(val2))
  #  print("CH3 = %d" %(val3))
  #  print("CH4 = %d" %(val4))
  #  print("===================")

    Data.data = [val1,val2,val3,val4]
    if(not rospy.is_shutdown()): 
            sendData('sensor',Data)

    hx1.power_down()
    hx1.power_up()
    hx2.power_down()
    hx2.power_up()
    hx3.power_down()
    hx3.power_up()
    hx4.power_down()
    hx4.power_up()
    rate.sleep()

if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            ReadSensor()
    except rospy.ROSInterruptException:
        pass
