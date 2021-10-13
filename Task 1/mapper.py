#!/usr/bin/env python3
import sys

for line in sys.stdin:
    data=line.strip().split()
    i,j=data[0],data[1]
    #making 'i' a 10 digit number
    if (len(i)==1):
        print("000000000"+i,j)
    if (len(i)==2):
        print("00000000"+i,j)
    if (len(i)==3):
        print("0000000"+i,j)
    if (len(i)==4):
        print("000000"+i,j)
    if (len(i)==5):
        print("00000"+i,j)
    if (len(i)==6):
        print("0000"+i,j)
    if (len(i)==7):
        print("000"+i,j)
    if (len(i)==8):
        print("00"+i,j)
    if (len(i)==9):
        print("0"+i,j)
    if (len(i)==10):
        print(i,j)
