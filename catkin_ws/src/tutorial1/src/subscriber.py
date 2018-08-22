#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    # This prints the data on the screen.
    # loginfo() is preferred function for printing data to the terminal.
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def subscriber():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('subscriber', anonymous=True)

    # This node will subscribe to the data that is published on 'publisher_topic'.
    # At anytime it receives new data, the callback function will be excuted.
    rospy.Subscriber("publisher_topic", String, callback)

    # spin() simply keeps python from exiting until this node is stopped.
    rospy.spin()

if __name__ == '__main__':
    subscriber()
