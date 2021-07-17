#! /usr/bin/env python
import rospy

rospy.init_node("loop_node")

rate = rospy.Rate(2)

while not rospy.is_shutdown():
	print "my loop node is active"
	rate.sleep()
