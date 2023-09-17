#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = 1
    goal.target_pose.pose.position.y = 0
    goal.target_pose.pose.orientation.w = 1.0
    client.send_goal(goal)
    wait = client.wait_for_result()
    # goal.target_pose.pose.position.x = 1
    # goal.target_pose.pose.position.y = 1.5
    # goal.target_pose.pose.orientation.w = 0.75
    # client.send_goal(goal)
    # wait = client.wait_for_result()
    # goal.target_pose.pose.position.x = 0
    # goal.target_pose.pose.position.y = 1.5
    # goal.target_pose.pose.orientation.w =0
    # client.send_goal(goal)
    # wait = client.wait_for_result()
    # goal.target_pose.pose.position.x = 0
    # goal.target_pose.pose.position.y = 0
    # goal.target_pose.pose.orientation.w =0.25
    # client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")