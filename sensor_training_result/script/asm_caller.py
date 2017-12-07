#!/usr/bin/env python
import roslib; roslib.load_manifest('laser_assembler')
import rospy; from laser_assembler.srv import *

rospy.init_node("asm_caller")
pub = rospy.Publisher('/my_cloud_map', Float64, queue_size=10)
rate = rospy.Rate(10)

while not rospy.is_shutdown():

    rospy.wait_for_service("assemble_scans")
    try:
        assemble_scans = rospy.ServiceProxy('assemble_scans', AssembleScans)
        resp = assemble_scans(rospy.Time(0,0), rospy.get_rostime())
         print "Got cloud with %u points" % len(resp.cloud.points)
     except rospy.ServiceException, e:
         print "Service call failed: %s"%e
