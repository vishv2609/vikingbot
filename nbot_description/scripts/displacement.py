#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
initial_posx=0
initial_posy=0
initial_theta=0
current_posx=0
current_posy=0
current_theta=0
displacement=0
def msgCallback(data):
    current_posx=data.pose.pose.position.x
    current_posy=data.pose.pose.position.y
    current_theta=data.pose.pose.orientation.w
    displacement=((initial_posx - current_posx)**2 + (initial_posy - current_posy)**2)**0.5
    print(displacement)

def subscriber():
    rospy.init_node('displacement')
    rospy.Subscriber('odom', Odometry, msgCallback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()
    