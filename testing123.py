# TODO
# - Investigate ROS2 more
#   - What happens when all robots are executing this code? This leads to doubles.
#   - Probably we need a service that gathers the already subscribed topics
#   - Or we just do anomaly detection on each robot. But do we have enough processor resources there?
# - Currently only String topics are accepterd. 
#   - I think we need to extend

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class AnomalyDetector(Node):    

    def __init__(self):
        super().__init__('AnomalyDetector')
        self.subscribed_topics = ["/AnomalyDetectorTopic"]                     # Prevent scanning own topic
        self.failed_subscribed_topics = []
        self.publisher = self.create_publisher(String, 'AnomalyDetectorTopic', 10)  # Create own topic
        self.timer = self.create_timer(1, self.check_topics)                   # Check every second on new topics
        self.get_logger().info("anomaly detector started")

    def check_topics(self):
        for topic in self.get_topic_names_and_types():
            if topic[0] not in self.subscribed_topics:                         # Check list with already subscribed topics
                try:
                    self.subscription = self.create_subscription(String, topic[0], self.listener_callback, 10)
                    self.subscribed_topics.append(topic[0])                    # Successfully subscribed
                    self.get_logger().info("subscribed to topic '%s'" % topic[0])
                except:
                    if topic[0] not in self.failed_subscribed_topics:          # Check already reported
                        self.get_logger().info("failed to subscribe to topic '%s'" % topic[0])
                        self.failed_subscribed_topics.append(topic[0])         # Do not report again

    def listener_callback(self, msg):
        #print(msg)
        self.publisher.publish(msg)                                            # Just copy the message to the anomaly detector topic
      

def main(args=None):
    rclpy.init(args=args)
    anomaly_detector = AnomalyDetector()
    rclpy.spin(anomaly_detector)
    anomaly_detector.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()