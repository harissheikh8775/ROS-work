#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def publisher():
    rospy.init_node('number_publisher', anonymous=True)
    pub = rospy.Publisher('/number_topic', Int32, queue_size=10)
    
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        try:
            user_input = int(input("Enter an integer: "))
            rospy.loginfo(f"Publishing: {user_input}")
            pub.publish(user_input)
        except ValueError:
            rospy.logwarn("Please enter a valid integer.")
        
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
 