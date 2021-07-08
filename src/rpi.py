#!/usr/bin/env python
import rospy
from std_msgs.msg import String

import time
import sys
import RPi.GPIO as GPIO
rospy.init_node('rpi', anonymous=True)


def sendData(Topic,Massage):
    pub = rospy.Publisher(Topic,int,queue_size=10)
    rospy.loginfo(Massage)
    pub.publish(Massage)

EMULATE_HX711=False
if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
        
    print("Bye!")
    sys.exit()

#hx1 = HX711(27,17)
#hx2 = HX711(5,22)
#hx3 = HX711(13,6)
#hx4 = HX711(26,19)
hx1 = HX711(6,5)
hx2 = HX711(19,13)
hx3 = HX711(21,26)
hx4 = HX711(16,20)


hx1.set_reading_format("MSB", "MSB")
hx2.set_reading_format("MSB", "MSB")
hx3.set_reading_format("MSB", "MSB")
hx4.set_reading_format("MSB", "MSB")


# HOW TO CALCULATE THE REFFERENCE UNIT
# To set the reference unit to 1. Put 1kg on your sensor or anything you have and know exactly how much it weights.
# In this case, 92 is 1 gram because, with 1 as a reference unit I got numbers near 0 without any weight
# and I got numbers around 184000 when I added 2kg. So, according to the rule of thirds:
# If 2000 grams is 184000 then 1000 grams is 184000 / 2000 = 92.
#hx.set_reference_unit(113)
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

while True:
    try:
        # These three lines are usefull to debug wether to use MSB or LSB in the reading formats
        # for the first parameter of "hx.set_reading_format("LSB", "MSB")".
        # Comment the two lines "val = hx.get_weight(5)" and "print val" and uncomment these three lines to see what it prints.
        
        # np_arr8_string = hx.get_np_arr8_string()
        # binary_string = hx.get_binary_string()
        # print binary_string + " " + np_arr8_string
        
        # Prints the weight. Comment if you're debbuging the MSB and LSB issue.
      
        val1 = hx1.get_weight()
        val2 = hx2.get_weight()
        val3 = hx3.get_weight()
        val4 = hx4.get_weight()

        print("CH1 = %s" %(val1))
        print("CH2 = %s" %(val2))
        print("CH3 = %s" %(val3))
        print("CH4 = %s" %(val4))
        print("===================")

        if(not rospy.is_shutdown()): 
            sendData('sensor1',val1)
            sendData('sensor2',val2)
            sendData('sensor3',val3)
            sendData('sensor4',val4)




        # To get weight from both channels (if you have load cells hooked up 
        # to both channel A and B), do something like this
        #val_A = hx.get_weight_A(5)
        #val_B = hx.get_weight_B(5)
        #print "A: %s  B: %s" % ( val_A, val_B )

        hx1.power_down()
        hx1.power_up()
        hx2.power_down()
        hx2.power_up()
        hx3.power_down()
        hx3.power_up()
        hx4.power_down()
        hx4.power_up()
        time.sleep(0.1)

        
        

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()


