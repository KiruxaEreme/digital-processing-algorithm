import cv2
import numpy as np

def picture():
    img = cv2.imread('zelenye-rasteniya.png')

    cv2.namedWindow('Display window',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Display window', img) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def video():
    cap = cv2.VideoCapture('VID_20200614_152436.mp4',cv2.CAP_ANY)
    while(True):
        ret, frame = cap.read()
        if not(ret):
            break
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

def video_from_cam():
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        if not(ret):
            break
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

def webcam():
    video = cv2.VideoCapture(0)
    ok, img = video.read()
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter('output.mov', fourcc,25,(w,h))
    while(True):
        ok, img = video.read()
        cv2.imshow('img',img)
        video_writer.write(img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    video.release()
    cv2.destroyAllWindows()

# video_from_cam()
webcam()

# python lab1.py