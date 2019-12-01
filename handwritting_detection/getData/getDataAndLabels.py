from mlxtend.data import loadlocal_mnist
import cv2 as cv
import numpy as np


def ConvertAndSave(X,y):
	data = np.zeros((X.shape[0],8*8),dtype= np.uint8)
	labels = y[:]

	for index in range(0,X.shape[0]):
		im = np.reshape(X[index],(28,28))
		im = cv.resize(im,(8,8),interpolation = cv.INTER_AREA)
		im = np.reshape(im,(8*8))
		data[index] = im[:]
	return (data,labels)

X, y = loadlocal_mnist(
	images_path = 't10k-images.idx3-ubyte',
	labels_path = 't10k-labels.idx1-ubyte')

(data,labels) = ConvertAndSave(X,y)
np.save('../Code/t-data.npy',data)
np.save('../Code/t-labels.npy',labels) 

####
X, y = loadlocal_mnist(
	images_path = 'train-images.idx3-ubyte',
	labels_path = 'train-labels.idx1-ubyte')

(data,labels) = ConvertAndSave(X,y)
np.save('../Code/data.npy',data)
np.save('../Code/labels.npy',labels) 
####