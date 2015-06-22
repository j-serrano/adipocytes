#!/usr/bin/python

import sys,cv2
import math
import numpy as np
import matplotlib.pyplot as plt
import cv2.cv as cv

# ----------------- LOAD IMAGE -------------------------
sIPath="./original"
sFPath="./filter"
sOPath="./result"
sImgID=sys.argv[1]
img = cv2.imread(sIPath+"/"+sImgID+".tif")


# ----------------- FILTER IMAGE -----------------------
imgF = img
# imgF = cv2.GaussianBlur(imgF,,)
# imgF = cv2.Sobel(imgF,-1,2,2,1)
# ret,imgF = cv2.threshold(imgF,50,255,cv2.THRESH_BINARY)
imgF = cv2.cvtColor(imgF,cv2.COLOR_BGR2GRAY)
cv2.imwrite(sFPath+"/"+sImgID+".tif", imgF);


# ----------------- DETECT CIRCLES ---------------------
circles = cv2.HoughCircles(imgF,cv.CV_HOUGH_GRADIENT,1,20, \
	param1=400,param2=35,minRadius=10,maxRadius=80)
circles = np.uint16(np.around(circles))

# hist, bin_edges = np.histogram(circles[0,:,2],bins=20)
# plt.bar(bin_edges[:-1], hist, width = 1)
# plt.xlim(min(bin_edges), max(bin_edges))
# plt.show()

# ---------- DETECT INNER AND OUTER LIMITS -------------
lCircles=[]
for i in circles[0,:]:
	lAvg=[]
	rInt=-1
	rExt=-1
	for r in range(1,i[2]+10):
		avg=0
		count=0
		for x in range(i[0]-r,i[0]+r):
			if (x>0 and x<imgF.shape[1]):
				if (r*r-(x-i[0])*(x-i[0])>0):
					y=i[1]+math.sqrt(r*r-(x-i[0])*(x-i[0]))
					if(y>0 and y<imgF.shape[0]):
						count=count+1.0
						avg=avg+imgF[y,x]
					y=i[1]-math.sqrt(r*r-(x-i[0])*(x-i[0]))
					if(y>0 and y<imgF.shape[0]):
						count=count+1.0
						avg=avg+imgF[y,x]
		avg=avg/(2.0*count)
		lAvg.append(avg)
		if(rInt<0 and avg<50):
			rInt=r
		if(rInt>0 and rExt<0 and avg>50):
			rExt=r
#	if (rInt>0 and rExt>0 and rExt-rInt>5 and rExt-rInt<20 and i[2]<1.1*float(rExt) and i[2]>0.9*float(rInt)):
	lCircles.append([i[0],i[1],rInt,rExt,i[2]])
 
# ----------------- DRAW DETECTED CIRCLES --------------
for i in lCircles:
	cv2.circle(img,(i[0],i[1]),i[4],(0,255,0),2)
	cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
	if(i[2]>0):
		cv2.circle(img,(i[0],i[1]),i[2],(0,255,255),1)
		cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
	if(i[3]>0):
		cv2.circle(img,(i[0],i[1]),i[3],(0,255,255),1)
		cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

# ----------------- SAVE IMAGE WITH CIRCLES ------------
cv2.imwrite(sOPath+"/"+sImgID+".tif", img);

