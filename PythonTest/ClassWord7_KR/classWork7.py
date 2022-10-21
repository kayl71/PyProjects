import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

def task1():
    a = int(input())
    b = int(input())
    print(a**2-b**2)

def task2():
    s = input()
    count = 0
    for i in s:
        if i >= 'a' and i <= 'z':
            count+=1
    print(count)

def task3():
    s = input()
    l = list(s.split())
    count = 0
    for i in l:
        if i.find("sus") != -1:
            count+=1
    print(count)

def task4(generator):
    gen2 = filter(lambda x : x%3, generator)
    return gen2

def task5(list_of_smth):
    return list_of_smth[-2::-2] 

def task6(list1, list2, list3, list4):
    print(*set((list1 or list4) and (list2 or list3)))

def task7():
    np.random.seed(5)
    m = np.random.randint(25, size = (5, 5))
    det = np.linalg.det(m[1:,[0,1,2,4]])
    return m

def task8(f, min_x, max_x, N, min_y, max_y):
    x = np.linspace(min_x, max_x, N)
    y = f(x)

    y1 = [0]*(len(y)-1)
    for i in range(1, len(y)):
        y1[i-1] = (y[i] - y[i-1])/(x[i]-x[i-1])

    plt.ylim((min_y,max_y))
    plt.xscale('log')
    plt.grid(True)

    plt.plot(x,y, 'k.')

    plt.savefig("graph.jpg")

    plt.plot(x[:len(x)-1],y1)
    plt.show()

def task9(data, x_array, y_array):
    pass

def task10(list_of_smth):
    return [math.prod(list_of_smth[i:])**(1/len(list_of_smth))  for i in range(len(list_of_smth))]

def task11(filename="infile.csv"):
    df = pd.read_csv(filename)
    # 1
    lcolumns = df.columns
    for i in lcolumns:
        print(len(df[df[i].isnull()]))

    # 2
    l = df[df['x'].isnull()].index
    for i in range(len(l)):
        df['x'][l[i]] = (df['x'][l[i]-1] + df['x'][l[i]+1])/2

    # 3
    l = df[df['x_err'].isnull()].index
    for i in range(len(l)):
        df['x_err'][l[i]] = (df['x_err'][l[i]-1] + df['x_err'][l[i]+1])/2

    # 4
    df = df[df['y'].isnull() == False]
    df = df[df['y_err'].isnull() == False]

    # 5
    x = df['x']
    y = df['y']
    x_err = df['x_err']
    y_err = df['y_err']

    plt.errorbar(x,y, yerr=y_err, xerr=x_err, fmt='.')
    plt.grid(b=True, which='major', axis='both', alpha=1)
    plt.grid(b=True, which='minor', axis='both', alpha=0.5)
    plt.plot(x, y)
    plt.savefig("dataframe.pdf")
    
    
def task12(filename="video-games.csv"):
    df = pd.read_csv(filename)
    d12 = {}
    d12["n_games"] = df.title.count()
    d12["by_years"] = pd.DataFrame(df.groupby("year").count()["title"])
    d12["mean_price"] = df[df["publisher"] == "EA"]["price"].mean()
    d12["age_max_price"] = pd.DataFrame(df.groupby("age_raiting")["price"].max())
    d12["mean_raiting_1_2"] = df[(df["max_players"] == 1) | (df["max_players"] == 2)]["review_raiting"].mean()
    x = df.groupby("age_raiting")["price"]
    d12["min_max_price"] = pd.DataFrame({"min" : x.min(), "max" : x.max(), "sales_metric" : x.mean()}).sort_values(by="max", ascending = False)
    d12["n_games_by_age"] = pd.DataFrame(df.groupby("review_raiting")["title"].count())
    d12["same_price_raiting"] = 0
    l = df.publisher.unique()
    al = []
    for i in l:
        if type(i) == float:
            continue
        if i.find(',') == -1:
            al.append(i)
            continue

        x = i.split(',')
        for j in x:
            al.append(j)
    d12["creators"] = [*set(al)]

    p = pd.DataFrame(df.groupby("year")["review_raiting"].max())
    ltemp = []
    for i in p.index:
        ltemp.append(df[(df["year"] == i) & (p["review_raiting"][i] == df["review_raiting"])].iloc[0]["title"])
    p["title"] = ltemp
    d12["max_raiting_by_years"] = p
    d12["empty_creators"] = len(df.loc[df["publisher"].isnull(), "publisher"])
    return d12
