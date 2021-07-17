#! /usr/bin/env python
import rospy

rospy.init_node("loop_node_three")

rate = rospy.Rate(2)

while not rospy.is_shutdown():
	print "my loop node three is also active"
	rate.sleep()
