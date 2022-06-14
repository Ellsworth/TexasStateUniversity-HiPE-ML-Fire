from requests import request
from example_interfaces.srv import AddTwoInts

import os
import rclpy
from rclpy.node import Node
from BME680_Data import *


class MinimalService(Node):

    def __init__(self):
        #super().__init__('minimal_service')
        #self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)
        #self.srv = self.create_service()
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(NUm, 'topic', 10)
        timer_period = .5
        self.timer = self.create_timer(timer_period, self.timer_callback)
    
    def timer_callback(self):
        msg = Num()
        msg.num = self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.num)
        self.i += 1

    def getTemperature():
        self.get_logger().info('Incoming Request: %d\n' % (request))
        
        return temp_sensor()
    
   
    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        return response


def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
