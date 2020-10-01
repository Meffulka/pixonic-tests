#!/usr/bin/python3

import os
import socket

nginxStatus = os.system('service nginx status  > /dev/null 2>&1')

if nginxStatus == 0:
    nginxConfTest = os.system('nginx -t > /dev/null 2>&1')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketResult = sock.connect_ex(('127.0.0.1',80))
    if nginxConfTest == 0:
        print("Status: OK")
    elif socketResult == 0:
        print("Status: OK")
    else:
        print("Status: Warning")

else:
    print("Status: Error")