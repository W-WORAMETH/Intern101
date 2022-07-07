import rosbag
from std_msgs.msg import Float64MultiArray
import pandas as pd

# The bag file should be in the same directory as your terminal
bag = rosbag.Bag('2022-07-07-19-40-15.bag')
topic = '/LogData'
column_names = ['Solenoid1','Solenoid2' ,'FL' , 'FR' ,'BL' ,'BR' ,'M1' , 'M2' , 'CPG1' , 'CPG2' , 'MI' , 'DIRECTION']
df = pd.DataFrame(columns=column_names)

msg = Float64MultiArray()
msg.data = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]  

for topic, msg, t in bag.read_messages(topics=topic):
    Solenoid1 = msg.data[0]
    Solenoid2 = msg.data[1]
    FL = msg.data[2]
    FR = msg.data[3]
    BL = msg.data[4]
    BR = msg.data[5]
    M1 = msg.data[6]
    M2 = msg.data[7]
    CPG1 = msg.data[8]
    CPG2 = msg.data[9]
    MI = msg.data[10]
    DIRECTION = msg.data[11]


    df = df.append(
        {'Solenoid1': Solenoid1,
         'Solenoid2': Solenoid2,
         'FL': FL,
         'FR' : FR,
         'BL' : BL,
         'BR' : BR,
         'M1' : M1,
         'M2' : M2,
         'CPG1': CPG1,
         'CPG2' : CPG2,
         'MI':MI,
         'DIRECTION': DIRECTION
        },

        ignore_index=True
    )

df.to_csv('out.csv')