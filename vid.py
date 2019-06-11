import cv2,time
import numpy as np
#img = cv2.imread('1.jpg')
#img2 = img
#height, width, channels = img.shape
# Number of pieces Horizontally 
CROP_W_SIZE  = 2 
# Number of pieces Vertically to each Horizontal  
CROP_H_SIZE = 2
img=1
while(True):
    video=cv2.VideoCapture(0)
   # framerate=video.get(5)
    ret,frame=video.read()
    #gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame2=frame
    #cv2.imshow('hhh', frame)
    height = len(frame)
    width = len(frame[0])
    #print(height, width)
    #height, width, channels = frame.shape
    for ih in range(CROP_H_SIZE ):
        for iw in range(CROP_W_SIZE ):
            x = int(width/CROP_W_SIZE * iw)
            y = int(height/CROP_H_SIZE * ih)
            h = int((height / CROP_H_SIZE))
            w = int((width / CROP_W_SIZE ))
            print(ih, iw, x,y,h,w)
            frame = frame[y:y+h, x:x+w]
            NAME = str(time.time())
            n = 0
            if ih == 0:
                n = 1
            else:
                n = 2
            cv2.imwrite("F:/MCA/sem-4/project/image/" + str(int((iw+1))) + "{}".format(n) +  ".jpg",frame)
            frame = frame2
    time.sleep(5)
	
