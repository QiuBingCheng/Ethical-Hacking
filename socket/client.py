# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 11:41:32 2022

@author: Jerry
"""

import socket               # 导入 socket 模块
 
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 5357                # 设置端口号
 
s.connect((host, port))
print (s.recv(1024))
s.close()
