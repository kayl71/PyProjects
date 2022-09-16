# 1

import itertools as it

with open("input.txt", 'r') as f:
    lines = list(map(lambda x: x.rstrip().split(), f.readlines()))
    l = list(it.zip_longest(*lines, fillvalue=0))
    print([sum([int(i) for i in x]) for x in l])