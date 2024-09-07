#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class myNode(Node):
    def __init__(self):
        super().__init__("firstNode")
        self.num=int(input())
        if self.num%2==0:
            self.parity="even"
        else:
            self.parity="odd"
        self.create_timer(1.0,self.timer_callback)

    def timer_callback(self):
        self.get_logger().info(self.parity)
        

def main(args=None):
    rclpy.init(args=args)
    node=myNode()
    rclpy.spin(node)


    rclpy.shutdown()

if __name__=='__main__':
    main()