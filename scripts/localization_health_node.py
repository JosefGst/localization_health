#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseWithCovarianceStamped
from std_msgs.msg import Bool

cov_trhesh = rospy.get_param('cov_thresh', '0.4')

health_pub = rospy.Publisher('localization_health_ok', Bool, queue_size=1)

def callback(msg):
    health_status = Bool()
    health_status.data = True
    for covariance in msg.pose.covariance:
        # rospy.loginfo(rospy.get_caller_id() + "I heard %f", covariance)
        if abs(covariance) > float(cov_trhesh):
            rospy.loginfo("Covariance Threshold exceeded! STOP Robot.")
            health_status.data = False
            break

    health_pub.publish(health_status.data)
    
def localization_health():
    rospy.init_node('localization_health')

    rospy.Subscriber("amcl_pose", PoseWithCovarianceStamped, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        localization_health()
    except rospy.ROSInterruptException:
        pass