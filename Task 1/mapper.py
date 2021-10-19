#!/usr/bin/env python3
import sys

for line in sys.stdin:
    data = line.strip().split()
    i, j = data[0], data[1]
    print(i.zfill(7), j)
