# 1
[[i*m + j for j in range(m)] for i in range(n)]

# 2
[[int(j>i) + 2*int(i>j) for j in range(m)] for i in range(n)]

# 3
[[max(i, j) for j in range(n)] for i in range(n)]

# 4
with open("input.txt") as f:
    words = f.readlines()
    print(*words[::-1], end="", sep="")

# 5
with open("input.txt") as f:
    words = f.read()
    words = '\n' + words #<---- без этой строки информатикс выдает частичное решение, тк в конце файла нужно \n
    print(*words[::-1], end="", sep="")

# 6
with open("input.txt") as f:
    # SecondName Name Class Score 
    words = f.readlines()
    words = [words[i].split() for i in range(len(words))]
    scores = [0]*3
    for word in words:
        clas = int(word[2])
        scores[clas - 9] = max(scores[clas-9], int(word[3]))
    print(*scores)
    
# 7
with open("input.txt") as f:
    # SecondName Name School Score 
    words = f.readlines()
    words = [words[i].split() for i in range(len(words))]
    schools = set()
    maxi = 0
    for word in words:
        maxi = max(maxi, int(word[3]))
    for word in words:
        if int(word[3]) == maxi:
            schools.add(int(word[2]))
    print(*sorted([i for i in schools]))


# 8
with open("input.txt") as f:
    # SecondName Name School Score 
    words = f.readlines()
    words = sorted([words[i].split() for i in range(len(words))], key = lambda x: x[0])
    for i in words:
        print(i[0], i[1], i[3])
    
# 9 
with open("input.txt") as f:
    # SecondName Name Class Score 
    words = f.readlines()
    words = [words[i].split() for i in range(len(words))]
    scores = [float(0)]*3
    col = [0]*3
    for word in words:
        clas = int(word[2])-9
        scores[clas] += float(word[3])
        col[clas] += 1
    print(*[ i/j for i, j in zip(scores, col)])
    
