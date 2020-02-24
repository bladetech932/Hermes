import cv2
import numpy as np
from threading import Thread
from queue import Queue
from time import sleep

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
# blur
	kernel = np.ones((5,5),np.float32)/25 #array of ones divided by a constant for adjusting the brightness of blur
	dst = cv2.filter2D(frame,-1,kernel)

	blur = cv2.blur(frame,(5,5)) #array of ones scaled by sum

	gblur = cv2.GaussianBlur(frame, (11, 11), 0) #(img, (width, height), sigma_x, sixma_y) x=y if y not given 0==kernal size

	med_blur = cv2.medianBlur(frame, 5) # 5 = kernal size

	bl_blur = cv2.bilateralFilter(frame, 9, 75, 75)
#########

	cv2.imshow('frame', frame)
	#cv2.imshow('dst', dst)
	#cv2.imshow('blur', blur)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
