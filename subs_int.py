#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def callback(data):
    number = data.data
    if is_prime(number):
        rospy.loginfo(f"Received Prime Number: {number}")
    else:
        rospy.loginfo(f"{number} is not a prime number.")

def subscriber():
    rospy.init_node('prime_subscriber', anonymous=True)
    rospy.Subscriber('/number_topic', Int32, callback)
    
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass
 