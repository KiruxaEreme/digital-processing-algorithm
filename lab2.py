import numpy as np
import cv2
import math

def make_matr(len):
    return [[0 for i in range(len)] for j in range(len)]

def gauss(x,y,a,b,o):
    return (1/(2*np.pi*o*o))*np.exp(-((x-a)**2 + (y-b)**2)/(2*o*o))

def svert(matr,o):
    a = len(matr)//2
    b = a
    matr1 = matr
    s = 0
    for i in range(len(matr)):
        for j in range(len(matr)):
            matr1[i][j] = gauss(i,j,a,b,o)
    return matr1

def norm(matr):
    matr1 = matr
    s = 0
    for i in matr:
        for j in i:
            s += j*j
    s = math.sqrt(s)
    for i in range(len(matr1)):
        for j in range(len(matr1[i])):
            matr1[i][j] /= s
    return matr1


def picture():
    l = 21
    o = 1
    svert_matr = svert(make_matr(l),o)
    svert_matr = norm(svert_matr)

    img = cv2.imread('zelenye-rasteniya.png')
    img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    new_img = img2.copy()
    for i in range(0, len(new_img) - l):
        for j in range(0, len(new_img[0]) - l):
            summa = 0
            for h in range(i,i+l):
                for g in range(j,j+l):
                    summa += svert_matr[h-i][g-j]*img2[h][g]
            new_img[i][j] = summa
    cv2.imwrite("21picture"+str(o)+".png", new_img)
    cv2.namedWindow('Display window',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Display window', new_img) 
    cv2.waitKey(0)

def cv_gauss():
    img = cv2.imread('picture_gray.png')
    blur = cv2.blur(img,(5,5))
    cv2.imshow('Display window', blur)
    cv2.waitKey(0)

# svert(make_matr(5))
if __name__ == '__main__':
    # picture()
    cv_gauss()

# cv2.destroyAllWindows()
# python cv_lab2.py