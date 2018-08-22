#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def publisher():
    # This creates a node whose name is 'publisher_node'.
    rospy.init_node('publisher_node', anonymous=True)

    # This node will publish string data on 'publisher_topic'.
    pub = rospy.Publisher('publisher_topic', String, queue_size=10)

    # Run the loop at 10 hz.
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():

        # First generate the message that is to be published.
        hello_str = "hello world %s" % rospy.get_time()

        # Now publish the message through 'publisher_topic'.
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
