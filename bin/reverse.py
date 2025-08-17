#!/usr/bin/python3

import sys

list = []

for e in sys.stdin.readlines():
    list.insert(0, e.strip())

for e in list:
    print(e)