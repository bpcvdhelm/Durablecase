import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random
import time

class Temperature(Node):

    def __init__(self):
        super().__init__('Temperature')
        self.publisher_ = self.create_publisher(String, 'Temperature', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = '{ Robot: %d, Temperature: %.3f }' % (random.randint(1, 5), 14.5 + random.random())
        time.sleep(random.random() * 0.5)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = Temperature()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()