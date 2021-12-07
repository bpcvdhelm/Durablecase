import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random
import time

class Anomaly(Node):

    def __init__(self):
        super().__init__('Anomaly')
        self.coordinate_ = self.create_publisher(String, 'Coordinate', 10)
        self.cowsinsight_ = self.create_publisher(String, 'CowsInSight', 10)
        self.speed_ = self.create_publisher(String, 'Speed', 10)
        self.temperature_ = self.create_publisher(String, 'Temperature', 10)
        timer_period = 600 * random.random()  # Every 0-10 minutes randomly
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()

        for i in range(1, random.randint(1, 10)):
            msg.data = '{ Robot: %d, Coordinate: { %d, %d } }' % (random.randint(1, 10), random.random() * 1000000, random.random() * 1000000)
            self.coordinate_.publish(msg)
            self.get_logger().info('Publishing: "%s" to Coordinate' % msg.data)

        for i in range(1, random.randint(1, 10)):
            msg.data = '{ Robot: %d, CowsInSight: %d }' % (random.randint(1, 10), random.randint(30, 100))
            self.cowsinsight_.publish(msg)
            self.get_logger().info('Publishing: "%s" to CowsInSight' % msg.data)

        for i in range(1, random.randint(1, 10)):
            msg.data = '{ Robot: %d, Speed: %.3f }' % (random.randint(1, 10), random.random() * 100)
            self.speed_.publish(msg)
            self.get_logger().info('Publishing: "%s" to Speed' % msg.data)

        for i in range(1, random.randint(1, 10)):
            msg.data = '{ Robot: %d, Temperature: %.3f }' % (random.randint(1, 10), 14.5 + random.random() * 10)
            self.temperature_.publish(msg)
            self.get_logger().info('Publishing: "%s" to Temperature' % msg.data)

        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = Anomaly()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()