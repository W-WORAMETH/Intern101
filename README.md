# Intern101
## 1.Ros Installation
*http://wiki.ros.org/ROS/Installation*
## 2.Clone Package
#### for raspberry pi
````shell
    $ cd ~/catkin_ws/
````

````shell
    $ git clone https://github.com/W-WORAMETH/Intern101
````

````shell
    $ catkin_make
````
#### for control device (where the joystick is connected)
````shell
    $ cd ~/catkin_ws/
````

````shell
    $ git clone https://github.com/W-WORAMETH/Intern101
````

````
    $ git clone https://github.com/W-WORAMETH/joystick_teleop
````

````shell
    $ catkin_make
````
## 3.Use package
#### edit IP for ros connection
*find ip address*
````shell
    $ ifconfig
````
*edit ip address*
````shell
    $ nano ~/.bashrc
````
*source*
````shell
    $ source ~/.bashrc
````

#### roscore where ever you want
````shell
    $ roscore
````
#### on Raspberry Pi
````shell
    $ rosrun Intern101 SendSensor.py
````
````shell
    $ rosrun Intern101 RpiControl.py
````
#### on computer
*run node SendSensor to read pressure from pressure sensor that connected to raspberry pi shield*
````shell
    $ rosrun Intern101 SendSensor.py
````
*run node RpiControl to control solenoid valve*
````shell
    $ rosrun Intern101 RpiControl.py
````
#### on Control Device or Computer
*run node ReceiveSensor to receive data from raspberry pi*
````shell
    $ rosrun Intern101 ReceiveSensor.py
````
