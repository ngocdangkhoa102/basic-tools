import cv2 as cv
import numpy as np 

src = cv.imread("src2.jpg")
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

while True:
	ret,imbin = cv.threshold(gray,60,255,cv.THRESH_BINARY)
	# imbin = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 91, 12)
	im, contours, hierarchy = cv.findContours(imbin, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

	for contour in contours:
		x,y,w,h = cv.boundingRect(contour)
		cv.rectangle(src, (x, y), (x + w, y + h), (0, 255,0), 2)
		cv.imshow("result",src)
		cv.waitKey(0)
	break

print(x,y,w,h)
cv.destroyAllWindows()