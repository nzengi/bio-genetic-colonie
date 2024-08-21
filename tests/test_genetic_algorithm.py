import rospy
from geometry_msgs.msg import Twist

def move_robot():
    rospy.init_node('robot_controller', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz
    
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 0.5  # Move forward
        twist.angular.z = 0.1  # Rotate
        pub.publish(twist)
        rate.sleep()

if __name__ == "__main__":
    try:
        move_robot()
    except rospy.ROSInterruptException:
        pass
