
import cv2
import numpy as np

def GetChar(x : int):
    cmap = [' ', '.', ',', '*', '%', '$', '#', '@']
    return cmap[x//(256//(len(cmap)-1))]

def ASCII_PIC(img):
    strPic = ""
    for i in img:
        for j in i:
            strPic += GetChar(j)
        strPic+='\n'
    print(strPic)

img = cv2.imread('Putin.jpg', cv2.IMREAD_GRAYSCALE)
ASCII_PIC(img)
cv2.waitKey(0)

