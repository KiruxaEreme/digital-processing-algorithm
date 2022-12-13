
import numpy as np
import cv2
import math

def picture():
    img = cv2.imread('example.jpg')
    img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(img2,(5,5))

    cv2.imshow('Display window', blur)
    cv2.waitKey(0)
    
    grad_lenght = [[0 for i in range(len(blur[j]))] for j in range(len(blur))]
    grad_angle = [[0 for i in range(len(blur[j]))] for j in range(len(blur))]

# оператор Собеля
    gx = [[-1,0,1],[-2,0,2],[-1,0,1]]
    gy = [[-1,-2,-1],[0,0,0],[1,2,1]]
    max_grad_lenght = 0
    for i in range(1, len(blur) - 1):
        for j in range(1, len(blur[i]) - 1):
            sum_gx = 0
            sum_gy = 0

            for h in range(0,2):
                for g in range(0,2):
                    # print(str(i)+" "+str(j)+" "+str(h)+" "+str(g))
                    sum_gx += gx[h][g]*blur[h-1+i][g-1+j]
                    sum_gy += gy[h][g]*blur[h-1+i][g-1+j]
            grad_lenght_temp = math.sqrt(sum_gx**2+sum_gy**2)
            if sum_gx == 0:
                sum_gx = 0.0000001
            tangens = math.tan(sum_gy/sum_gx)

# округлениe угла 
            if (sum_gx>0 and sum_gy<0 and tangens<-2.414) or (sum_gx<0 and sum_gy<0 and tangens>2.414):
                fi = 0
            elif (sum_gx>0 and sum_gy<0 and tangens<-0.414):
                fi = 1
            elif (sum_gx>0 and sum_gy<0 and tangens>-0.414) or (sum_gx>0 and sum_gy>0 and tangens<0.414):
                fi = 2
            elif (sum_gx>0 and sum_gy>0 and tangens<2.414):
                fi = 3
            elif (sum_gx>0 and sum_gy>0 and tangens>2.414) or (sum_gx<0 and sum_gy>0 and tangens<-2.414):
                fi = 4
            elif (sum_gx<0 and sum_gy>0 and tangens<-0.414):
                fi = 5
            elif (sum_gx<0 and sum_gy>0 and tangens>-0.414) or (sum_gx<0 and sum_gy<0 and tangens<0.414):
                fi = 6
            elif (sum_gx<0 and sum_gy<0 and tangens<2.414):
                fi = 7

            grad_lenght[i][j] = grad_lenght_temp
            grad_angle[i][j] = fi
            max_grad_lenght = max(max_grad_lenght, grad_lenght_temp)

# Подавление немаксимумов
    for i in range(3,len(grad_lenght)-3):
        for j in range(3,len(grad_lenght[i])-3):
            if grad_angle[i][j] == 6 or grad_angle[i][j] == 2:
                if grad_lenght[i][j] > grad_lenght[i-1][j] and grad_lenght[i][j] > grad_lenght[i+1][j]:
                    img2[i][j] = 255
                else: img2[i][j] = 0
            elif grad_angle[i][j] == 4 or grad_angle[i][j] == 0:
                if grad_lenght[i][j] > grad_lenght[i][j-1] and grad_lenght[i][j] > grad_lenght[i][j+1]:
                    img2[i][j] = 255
                else: img2[i][j] = 0
            elif grad_angle[i][j] == 5 or grad_angle[i][j] == 1:
                if grad_lenght[i][j] > grad_lenght[i-1][j-1] and grad_lenght[i][j] > grad_lenght[i+1][j+1]:
                    img2[i][j] = 255
                else: img2[i][j] = 0
            elif grad_angle[i][j] == 7 or grad_angle[i][j] == 2:
                if grad_lenght[i][j] > grad_lenght[i-1][j+1] and grad_lenght[i][j] > grad_lenght[i+1][j-1]:
                    img2[i][j] = 255
                else: img2[i][j] = 0

    cv2.imshow('Display window', img2) 
    cv2.waitKey(0)

# двойная пороговая фильтрация
    low_level = max_grad_lenght // 5
    high_level = max_grad_lenght // 2
    for i in range(3,len(grad_lenght)-3):
        for j in range(3,len(grad_lenght[i])-3):
            if img2[i][j] == 255:
                if grad_lenght[i][j] < low_level:
                    img2[i][j] = 0
                elif grad_lenght[i][j] < high_level:
                    img2[i][j] = 0
                    for h in range(0,8):
                        for g in range(0,8):
                            if h!=4 and g!=4 and img2[i-4+h][j-4+g] == 255:
                                img2[i][j] == 255

    cv2.imshow('Display window', img2) 
    cv2.waitKey(0)

if __name__ == '__main__':
    picture()
    

# cv2.destroyAllWindows()
# python cv_lab3.py