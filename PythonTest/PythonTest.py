import numpy as np

WIDTH, HEIGHT = 126, 33
permission = 5
WIDTH*=permission
HEIGHT*=permission

screen = np.array([" "*WIDTH] * HEIGHT)
s = ""

screen[HEIGHT//4:-HEIGHT//4][:] = "@"


for i in screen:
    s+= i[:] + '\n'
#print(s, sep="")
k = "0123456789"
k[1:5] = '2'
print(k)

