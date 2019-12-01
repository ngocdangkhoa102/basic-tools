from sklearn import datasets
digits = datasets.load_digits()

import numpy as np
import cv2 as cv


for value in range(0,10):
	tmp = cv.imread('../dataT/'+str(value)+'.png',0)
	tmp = np.reshape(tmp,(100*100))

	imbin = np.zeros(tmp.shape,dtype = np.uint8)
	imbin[tmp != 0] = 250
	imbin = np.reshape(tmp,(100,100))
	cv.imshow("number",imbin)
	cv.waitKey(0)
