import cv2 as cv
import numpy as np 


def isAllZeros(mtrx):
	zeros_matrx = np.zeros((mtrx.shape[0],1))
	return (mtrx == zeros_matrx).all()

def cropBlackPart(grayim,offset):
	tmph = np.zeros((grayim.shape[0],1))
	for index in range(1,grayim.shape[1]):
		tmph[:,-1] = grayim[:,-index]
		if(isAllZeros(tmph)):
			pass
		else:
			x2 = grayim.shape[1]-index-offset
			break
	x1 = offset
	y1 = offset
	y2 = grayim.shape[0]-offset
	return (x1,x2,y1,y2)


src = cv.imread("src2.jpg")
grayim = cv.cvtColor(src, cv.COLOR_RGB2GRAY)

(x1,x2,y1,y2) = cropBlackPart(grayim,7)

print(x1,x2,y1,y2)

color_im = src[y1:y2,x1:x2,]

print(color_im)
# input("press any key to continue...")
cv.imshow("cropped image", color_im)
cv.waitKey(0)
print(output.shape[1])
