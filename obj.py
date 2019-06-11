import cv2
import numpy as np
#import RPi.GPIO as GPIO
#GPIO.setup(17,GPIO.OUT)
#GPIO.setup(27,GPIO.OUT)
#GPIO.setup(22,GPIO.OUT)
#GPIO.setup(23,GPIO.OUT)
flag=0
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
	flag=0;
	rect,img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img = np.array(img,dtype='uint8')
	faces = face_cascade.detectMultiScale(gray)
	f = bool(len(faces))
	print(f)
	if f == True:
		for(x,y,w,h) in faces:
			cv2.rectangle (img,(x,y),(x+w,y+h),(255,0,0),2)
			roi_gray = gray[y:y+h,x:x+w]
			roi_color = img[y:y+h,x:x+w]
			eyes = eye_cascade.detectMultiScale(roi_gray)
			for (ex,ey,ew,eh) in eyes:
				cv2.rectangle (roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
				print("face detect")
				#GPIO.output(17.GPIO.HIGH)
				#time.sleep(1)
				#GPIO.output(27.GPIO.HIGH)
				#time.sleep(1)
				#GPIO.output(22.GPIO.HIGH)
				#time.sleep(1)
				#GPIO.output(23.GPIO.HIGH)
				#time.sleep(1)
			cv2.imshow('img',img)
			key = cv2.waitKey(30) & 0xff
			if key == 27:
				break
	else :
		cv2.imshow('img',img)
		print("face not detect")
		#GPIO.output(17.GPIO.LOW)
		#time.sleep(1)
		#GPIO.output(27.GPIO.LOW)
		#time.sleep(1)
		#GPIO.output(22.GPIO.LOW)
		#time.sleep(1)
		#GPIO.output(23.GPIO.LOW)
		#time.sleep(1)
cap.release()
cv2.destroyAllWindows()
