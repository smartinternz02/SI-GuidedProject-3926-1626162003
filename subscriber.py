#! /usr/bin/env python
import rospy
from std_msgs.msg import String
def callback(msg):
    print msg.data

rospy.init_node('subscriber')
sub=rospy.Subscriber('counter', String, callback)
rospy.spin()