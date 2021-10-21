#! /usr/bin/env python3
import sys

current_to_node = None 
total_contribution = 0
node_number = 1

for line in sys.stdin:
    content = line.split(",")
    to_node = int(content[0]) 
    contribution = float(content[1]) 
    if(to_node != current_to_node): 
        if(current_to_node != None): 
            new_page_rank = 0.15 + 0.85 * total_contribution 
            print(current_to_node,round(new_page_rank,2),sep=",")
        current_to_node = to_node 
        total_contribution = 0
    total_contribution += contribution 
if total_contribution != 0:
    new_page_rank = 0.15 + 0.85 * total_contribution 
    print(current_to_node,round(new_page_rank,2),sep=",")