#!/usr/bin/python3

import os

nginxStatus = os.system('service nginx status  > /dev/null 2>&1')

if nginxStatus == 0:
    nginxConfTest = os.system('nginx -t > /dev/null 2>&1')
    if nginxConfTest == 0:
        print("Status: OK")
    else:
        print("Status: Warning")

else:
    print("Status: Error")