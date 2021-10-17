#!/usr/bin/env python3
import sys
import math
import json

# ---------- Functions ---------- #

def vector_length(vector):
    length = 0
    for i in vector:
        length += i ** 2
    return math.sqrt(length)

def vector_dot_product(vector_1, vector_2):
    value = 0
    for i, j in zip(vector_1, vector_2):
        value += i * j
    return value
    
def similarity(vector_1, vector_2):
    return vector_dot_product(vector_1, vector_2) / (vector_length(vector_1) * vector_length(vector_2))
    
# ---------- Input Files  ---------- #

v_file = open(sys.argv[1])
initial_page_ranks = {}
for line in v_file:
    node, rank = line.split(',')
    initial_page_ranks[node] = float(rank)

pe_file = open(sys.argv[2])
page_embeddings = json.load(pe_file)

# ---------- Main Code  ---------- #

for line in sys.stdin:
    data = line.strip().split('$')
    node, children = data[0], data[1].strip('[]').split(', ')
    if children[0] == '':
        children = []
    n_children = len(children)
    
    for child in children:
        try:
            initial_page_rank = initial_page_ranks[child]
        except:
            initial_page_rank = 1
        print('%s,%s,%f' % (
                child.zfill(7),
                node.zfill(7),
                (1 / n_children) * initial_page_rank * similarity(page_embeddings[child], page_embeddings[node])
            ))
