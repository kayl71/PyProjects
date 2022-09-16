# 2

with open("input.txt", 'r') as f:
    n = int(f.readline())
    for i, j in enumerate(f.readlines()):
        print(i%n, j, end = '')