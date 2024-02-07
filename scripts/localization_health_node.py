#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import Twist

cov_trhesh = rospy.get_param('cov_thresh', '0.2')


def callback(msg):
    for covariance in msg.pose.covariance:
        # rospy.loginfo(rospy.get_caller_id() + "I heard %f", covariance)
        if abs(covariance) > float(cov_trhesh):
            rospy.loginfo("Covariance Threshold exceeded! STOP Robot.")
    
def localization_health():
    rospy.init_node('localization_health')
    cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

    rospy.Subscriber("amcl_pose", PoseWithCovarianceStamped, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        localization_health()
    except rospy.ROSInterruptException:
        pass