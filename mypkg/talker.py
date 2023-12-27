#!/usr/bin/python3
# SPDX-FileCopyrightText: 2023 taisei0515
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msgs.srv import Query 

def cb(request, response):
    if request.name == "藤野泰生":
        response.age = 20
    else:
        response.age = 300

    return response
 
rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb) 
rclpy.spin(node)
