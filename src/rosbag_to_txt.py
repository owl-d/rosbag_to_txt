#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry

def callback(data):

    ##### argument ######
    scenario = "exp04"
    algorithm = "A-LOAM"
    #####################

    file_path = "/home/doyu/doyu_ws/Polaris/trajectories/" + algorithm + "/" + algorithm + "_" + scenario + ".txt"
    print("Odometry save as txt : scenario " + scenario)

    file = open(file_path, 'a')
    odometry = str(data.header.stamp) + ' ' \
        + str(data.pose.pose.position.x) + ' ' + str(data.pose.pose.position.y) + ' ' + str(data.pose.pose.position.z) + ' ' \
        + str(data.pose.pose.orientation.x) + ' ' + str(data.pose.pose.orientation.y) + ' ' \
        + str(data.pose.pose.orientation.z) + ' ' + str(data.pose.pose.orientation.w)
    file.write("\n"+odometry)
    file.close()

if __name__ == "__main__":

    odom_topic = "/aft_mapped_to_init"

    rospy.init_node("estimated_odometry")
    rospy.Subscriber(odom_topic, Odometry, callback)
    rospy.spin()