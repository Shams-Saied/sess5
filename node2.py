#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import random

class myNode(Node):
    def __init__(self):
        super().__init__("secondNode")
        self.create_timer(1.0,self.timer_callback)

    def timer_callback(self):
        self.temp=random.uniform(-40,55)
        self.pressure=random.uniform(28.5,30.7)
        self.humidity=random.uniform(30,50)
        self.get_logger().info("Temperature: "+str(self.temp)+"°C "+"Pressure: "+str(self.pressure)+" millibars of mercury "+"Humidity: "+str(self.humidity)+"%")
        

def main(args=None):
    rclpy.init(args=args)
    node=myNode()
    rclpy.spin(node)


    rclpy.shutdown()

if __name__=='__main__':
    main()