#! /usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('publisher')

pub=rospy.Publisher('/counter', String, queue_size=1)
rate=rospy.Rate(2)
count=String()
count.data="hello"
while not rospy.is_shutdown():
    pub.publish(count)
    rate.sleep()
