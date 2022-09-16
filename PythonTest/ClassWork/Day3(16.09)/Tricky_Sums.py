m = int(input())
l = set(list(map(int, input().split())))
bol = []
for i in l:
    k = m-i
    if k in l-set([i]) and not (i,k) in bol:
        bol.append((i,k))
        bol.append((k,i))
        print((i, k))
