#!/usr/bin/env python3
import sys

for line in sys.stdin:
    data=line.strip().split()
    i, j = data[0], data[1]
    #making 'i' a 10 digit number
    print(i.zfill(10), j)