# Localization Health checker ros

    rosrun localization_health localization_health_node.py 

## Subscribed Topics
amcl_pose([geometry_msgs/PoseWithCovarianceStamped](https://docs.ros.org/en/api/geometry_msgs/html/msg/PoseWithCovarianceStamped.html))
&nbsp;&nbsp;&nbsp;&nbsp; subscribe to the covariance of the amcl_pose topic 
## Published Topics
localization_health_ok([std_msgs/Bool](https://docs.ros.org/en/melodic/api/std_msgs/html/msg/Bool.html))
&nbsp;&nbsp;&nbsp;&nbsp; If health is ok -> "True".
## Parameters
cov_thresh(float, default 0.5)
&nbsp;&nbsp;&nbsp;&nbsp; If any covariance value exceed the threshold, the "localization_health_ok" topic will publish "False". Meaning the localisation is lost.