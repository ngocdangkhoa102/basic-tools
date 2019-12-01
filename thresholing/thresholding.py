import cv2 as cv
import numpy as np 

def nothing():
	pass

src = cv.imread("t3.jpg")
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

minVal = 0;
maxVal = 255;

cv.namedWindow('Trackbar')
cv.createTrackbar('value','Trackbar',minVal,maxVal,nothing)

while True:
	val = cv.getTrackbarPos('value','Trackbar')
	# im = src[:,0:src.shape[1] - val]
	ret,imbin = cv.threshold(gray,val,255,cv.THRESH_BINARY)
	# imbin = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 91, 12)
	cv.imshow('orginal',src)	
	cv.imshow('thresholded',imbin)
	k = cv.waitKey(1) & 0xFF
	if k == 27:
		break
cv.destroyAllWindows()