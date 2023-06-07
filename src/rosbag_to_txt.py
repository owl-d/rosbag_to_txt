#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry

def callback(data):
    scenario = "ex18"
    file_path = "/home/doyu/doyu_ws/Polaris/odometry/A-LOAM/A-LOAM_" + scenario + ".txt"
    is_first=True
    print("Odometry save as txt : "+scenario)

    file = open(file_path, 'a')
    odometry = str(data.header.stamp) + ' ' \
        + str(data.pose.pose.position.x) + ' ' + str(data.pose.pose.position.y) + ' ' + str(data.pose.pose.position.z) + ' ' \
        + str(data.pose.pose.orientation.x) + ' ' + str(data.pose.pose.orientation.y) + ' ' \
        + str(data.pose.pose.orientation.z) + ' ' + str(data.pose.pose.orientation.w)
    if is_first :
        file.write(odometry)
        is_first=False
    else : file.write("\n"+odometry)
    file.close()

if __name__ == "__main__":
    rospy.init_node("estimated_odometry")
    rospy.Subscriber("/aft_mapped_to_init", Odometry, callback)
    rospy.spin()