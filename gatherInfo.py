### `sample_to_show_topic_list.py` ###
import rclpy
from rclpy.node import Node

rclpy.init()
node_dummy = Node("dummy_node")
print("get_fully_qualified_name():", node_dummy.get_fully_qualified_name())
print("get_name():", node_dummy.get_name())
print("get_namespace():", node_dummy.get_namespace())
print("get_node_names():", node_dummy.get_node_names())
print("get_node_names_and_namespaces():", node_dummy.get_node_names_and_namespaces())
print("get_node_names_and_namespaces_with_enclaves():", node_dummy.get_node_names_and_namespaces_with_enclaves())
print("get_service_names_and_types():", node_dummy.get_service_names_and_types())
print("get_topic_names_and_types():", node_dummy.get_topic_names_and_types())
node_dummy.destroy_node()
rclpy.shutdown()
