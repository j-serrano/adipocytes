#!/usr/bin/python

import sys,cv2
import numpy as np
import cv2.cv as cv

# ----------------- LOAD IMAGE -------------------------
sIPath="./original"
sFPath="./filter"
sOPath="./result"
sImgID=sys.argv[1]
img = cv2.imread(sIPath+"/"+sImgID+".tif")


# ----------------- FILTER IMAGE -----------------------
imgF = img
# imgF = cv2.medianBlur(imgF,21)
# ret,imgF = cv2.threshold(imgF,160,255,cv2.THRESH_BINARY)
imgF = cv2.cvtColor(imgF,cv2.COLOR_BGR2GRAY)
cv2.imwrite(sFPath+"/"+sImgID+".tif", imgF);


# ----------------- DETECT CIRCLES ---------------------
circles = cv2.HoughCircles(imgF,cv.CV_HOUGH_GRADIENT,1,20, \
	param1=100,param2=40,minRadius=1,maxRadius=60)


# ----------------- DRAW DETECTED CIRCLES --------------
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
	cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
	cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

# cv2.imshow('detected circles',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ----------------- SAVE IMAGE WITH CIRCLES ------------
cv2.imwrite(sOPath+"/"+sImgID+".tif", img);

