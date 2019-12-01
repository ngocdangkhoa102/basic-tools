import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img1 = cv.imread('obj.jpg',cv.IMREAD_GRAYSCALE)          # queryImage
img2 = cv.imread('src.jpg',cv.IMREAD_GRAYSCALE) # trainImage
# Initiate SIFT detector
surf = cv.xfeatures2d.SURF_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = surf.detectAndCompute(img1,None)
kp2, des2 = surf.detectAndCompute(img2,None)
# FLANN parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary
flann = cv.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1,des2,k=2)
# Need to draw only good matches, so create a mask
matchesMask = [[0,0] for i in range(len(matches))]
# ratio test as per Lowe's paper
for i,(m,n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        matchesMask[i]=[1,0]
draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = cv.DrawMatchesFlags_DEFAULT)
img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
print(kp1)
print(kp2)
# print(matches)

kps = np.float32([kp.pt for kp in kp1])
print(kps)
plt.plot(kps[:,0],kps[:,1],'go')
plt.imshow(img3,)
plt.show()
cv.waitKey(0)