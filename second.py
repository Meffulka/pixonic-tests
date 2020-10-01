#!/usr/bin/python3

import argparse
import re
import os
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True, type=str, help="Log path")
args = parser.parse_args()

if os.path.exists(args.file):
    logFormat = re.compile(r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - -.*""",re.IGNORECASE)
    logFile = open(args.file, "r")
    ipList = []
    for l in logFile.readlines():
        ipList.append(re.search(logFormat, l).groupdict()["ipaddress"])
    logFile.close()
    ipCounter = Counter(ipList)
    print(ipCounter.most_common(5))

else:
    print("Файл не найден")