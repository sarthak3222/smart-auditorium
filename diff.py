import cv2,time
import numpy as np
#import div
#import RPi.GPIO as GPIO
#GPIO.setup(17,GPIO.OUT)
#GPIO.setup(27,GPIO.OUT)
#GPIO.setup(22,GPIO.OUT)
#GPIO.setup(23,GPIO.OUT)
w=1
x=2
y=3
z=4
i1=cv2.imread("room.jpg",0)
#i2=cv2.imread("23.jpg",0)
#i3=cv2.imread("14.jpg",0)
#i4=cv2.imread("24.jpg",0)
img=cv2.resize(i1,(320,240),interpolation = cv2.INTER_AREA)
while(True):
	img_1=cv2.imread("F:/MCA/sem-4/project/image/11.jpg");
	img_2=cv2.imread("F:/MCA/sem-4/project/image/12.jpg");
	img_3=cv2.imread("F:/MCA/sem-4/project/image/21.jpg");
	img_4=cv2.imread("F:/MCA/sem-4/project/image/22.jpg");
	#print(img_2.shape)
	gray=cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
	img1=gray
	diff1=cv2.subtract(img,img1);
	result=not np.any(diff1);
	if result is True:
		print("image one is same");
		#GPIO.output(17.GPIO.LOW)
		#time.sleep(1)
	else:
		file= 'F:/MCA/sem-4/project/image/' + str(int(w)) + ".jpg"
		cv2.imwrite(file,diff1);
		print("the images one is difference");
		#GPIO.output(17.GPIO.HIGH)
		#time.sleep(1)
	gray=cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
	img2=gray
	diff2=cv2.subtract(img,img2);
	result=not np.any(diff2);
	if result is True:
		print("image two is same");
		#GPIO.output(27.GPIO.LOW)
		#time.sleep(1)
	else:
		file= 'F:/MCA/sem-4/project/image/' + str(int(x)) + ".jpg"
		cv2.imwrite(file,diff2);
		print("the images is two difference");
		#GPIO.output(27.GPIO.HIGH)
		#time.sleep(1)
	gray=cv2.cvtColor(img_3, cv2.COLOR_BGR2GRAY)
	img3=gray
	diff3=cv2.subtract(img,img3);
	result=not np.any(diff3);
	if result is True:
		print("image three is same");
		#GPIO.output(22.GPIO.LOW)
		#time.sleep(1)
	else:
		file= 'F:/MCA/sem-4/project/image/' + str(int(y)) + ".jpg"
		cv2.imwrite(file,diff3);
		print("the images three is difference");
		#GPIO.output(22.GPIO.HIGH)
		#time.sleep(1)
	gray=cv2.cvtColor(img_4, cv2.COLOR_BGR2GRAY)
	img4=gray
	diff4=cv2.subtract(img,img4);
	result=not np.any(diff4);
	if result is True:
		print("image four is same");
		#GPIO.output(23.GPIO.LOW)
		#time.sleep(1)
	else:
		file= 'F:/MCA/sem-4/project/image/' + str(int(z)) + ".jpg"
		cv2.imwrite(file,diff4);
		print("the images four is difference");
		#GPIO.output(23.GPIO.HIGH)
		#time.sleep(1)
	time.sleep(6)		