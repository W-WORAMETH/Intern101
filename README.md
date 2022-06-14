# Intern101
## 1.Ros Installation
*http://wiki.ros.org/ROS/Installation*
## 2.Clone Package
#### for raspberry pi
````shell
    $ cd ~/catkin_ws/src
````

````shell
    $ git clone https://github.com/W-WORAMETH/Intern101
````

````shell
    $ catkin_make
````
#### for control device (where the joystick is connected)
````shell
    $ cd ~/catkin_ws/src
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
*add this to .bashrc (edit to your ip address)*

````
source /opt/ros/noetic/setup.bash
source ~/catkin_ws/devel/setup.bash

export ROS_MASTER_URI=http://192.168.1.39:11311/ 
export ROS_HOSTNAME=192.168.1.39
`````

*source*
````shell
    $ source ~/.bashrc
````
````shell
    $ source ~/.bashrc
````
#### roscore where ever you want
````shell
    $ roscore
    $ source ~/catkin_ws/devel/setup.bash
````

#### on Raspberry Pi
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
*run node generateCPG to generate CPG graph to control robot*
````shell
    $ rosrun Intern101 generateCPG.py
````
*this node not necessary but you can use it if you want to tast solenoid valve using your keyboard*
````shell
    $ rosrun Intern101 SendSolenoid.py
````

