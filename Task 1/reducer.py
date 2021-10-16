#!/usr/bin/env python3
import sys

current_from_node = None
from_node = None
adj_list = []

file1 = open(sys.argv[1], 'w')

for line in sys.stdin:
    data = line.strip().split()
    from_node, to_node = int(data[0]), int(data[1])   

    if from_node != current_from_node:
        if current_from_node != None:
            print(current_from_node, adj_list, sep='$')
            file1.write(str(current_from_node) + ",1\n")
        adj_list = []
        current_from_node = from_node

    adj_list.append(to_node)

if adj_list:
    print(current_from_node, adj_list, sep='$')
    file1.write(str(current_from_node) + ",1")

