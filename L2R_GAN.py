import rospy
import math
from sensor_msgs.msg import Imu
from gazebo_msgs.msg import LinkStates
from tf.transformations import euler_from_quaternion

class ImuPlugin:
    def __init__(self):
        # Initialize the ROS node and subscribers/publishers
        rospy.init_node('imu_plugin')
        self.imu_pub = rospy.Publisher('imu', Imu, queue_size=1)
        self.link_sub = rospy.Subscriber('/gazebo/link_states', LinkStates, self.on_link_states)
        
        # Initialize the IMU message
        self.imu_msg = Imu()
        self.imu_msg.header.frame_id = 'imu_link'
        
    def on_link_states(self, msg):
        # Get the index of the IMU link in the message
        try:
            index = msg.name.index('model_name::link_name')
        except ValueError:
            return
        
        # Get the linear and angular velocities and convert to body frame
        linear_vel = msg.twist[index].linear
        angular_vel = msg.twist[index].angular
        orientation = msg.pose[index].orientation
        euler = euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])
        
        # Set the IMU message fields
        self.imu_msg.header.stamp = rospy.Time.now()
        self.imu_msg.linear_acceleration.x = linear_vel.x
        self.imu_msg.linear_acceleration.y = linear_vel.y
        self.imu_msg.linear_acceleration.z = linear_vel.z
        self.imu_msg.angular_velocity.x = angular_vel.x
        self.imu_msg.angular_velocity.y = angular_vel.y
        self.imu_msg.angular_velocity.z = angular_vel.z
        self.imu_msg.orientation.x = orientation.x
        self.imu_msg.orientation.y = orientation.y
        self.imu_msg.orientation.z = orientation.z
        self.imu_msg.orientation.w = orientation.w
        
        # Publish the IMU message
        self.imu_pub.publish(self.imu_msg)
        
    def run(self):
        # Keep the node running
        rospy.spin()

if __name__ == '__main__':
    imu_plugin = ImuPlugin()
    imu_plugin.run()
