#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

rospy.init_node('my_node')
pub = rospy.Publisher('/laser_velocity_controller/command', Float64, queue_size=10)
rate = rospy.Rate(10)



while not rospy.is_shutdown():
    msg = Float64()
    msg.data = 2
    pub.publish(msg)
    rate.sleep()
