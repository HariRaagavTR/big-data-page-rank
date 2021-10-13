#!/usr/bin/env python3
import sys

for line in sys.stdin:
    data=line.strip().split()
    i,j=data[0],data[1]
    if (len(i)==1):
        print("0"+i,j)
    else:
        print(i,j)


