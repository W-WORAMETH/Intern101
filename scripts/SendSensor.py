#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray
import sys
from intern101.hx711 import HX711


rospy.init_node('rpi', anonymous=True)

rate = rospy.Rate(1) # 1hz
Massage = Int32MultiArray()
Massage.data = []

Data = Int32MultiArray()
Data.data = []

print("1")
#EMULATE_HX711=False
#if not EMULATE_HX711:
#    from hx711 import HX711
#else:
#    from emulated_hx711 import HX711

def sendData(Topic,Massage):
    pub = rospy.Publisher(Topic,Int32MultiArray,queue_size=10)
    rospy.loginfo(Massage)
    pub.publish(Massage)


def cleanAndExit():
    print("Cleaning...")

#    if not EMULATE_HX711:
    GPIO.cleanup()
        
    print("Bye!")
    sys.exit()
rospy.loginfo("TEST1")
print("2")
hx1 = HX711(6,5)
print("2.2")
hx2 = HX711(19,13)
print("2.3")
hx3 = HX711(21,26)
print("2.4")
hx4 = HX711(16,20)

print("done initial")
rospy.loginfo("TEST")

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
    print("F")
    val1 = hx1.get_weight()
    val2 = hx2.get_weight()
    val3 = hx3.get_weight()
    val4 = hx4.get_weight()
    print("I")
    rospy.loginfo(rospy.get_caller_id() + "   sensor1 = %s", str(val1))
    rospy.loginfo(rospy.get_caller_id() + "   sensor2 = %s", str(val2))
    rospy.loginfo(rospy.get_caller_id() + "   sensor3 = %s", str(val3))
    rospy.loginfo(rospy.get_caller_id() + "   sensor4 = %s", str(val4))

   

    print("CH1 = %d" %(val1))
    print("CH3 = %d" %(val3))
    print("CH4 = %d" %(val4))
    print("===================")

    Data.data = [val1,val2,val3,val4]
    # if(not rospy.is_shutdown()): 
    #     sendData('sensor',Data)

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
        rospy.loginfo("TEST3")
        print("D")
        while not rospy.is_shutdown():
            rospy.loginfo("TEST4")
            print("E")
            ReadSensor()
            rospy.spin()
    except rospy.ROSInterruptException:
            print("Exxx")
            cleanAndExit()
        
