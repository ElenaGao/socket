#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: upd服务端.py
@date: 2020/7/9
"""

from socket import *

server = socket(AF_INET, SOCK_DGRAM)
server.bind(('127.0.0.1', 8080))

res = server.recvfrom(20)
res2 = server.recvfrom(30)
print(res)
print(res2)
server.close()
