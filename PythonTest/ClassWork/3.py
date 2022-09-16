# 3
import collections as col

with open("input.txt", 'r') as f:
    n = 10
    print(*[x[0] for x in col.Counter(f.read().split()).most_common(n)])
    #print(col.Counter(f.read().split()).most_common(n))