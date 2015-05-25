import cv2
import numpy as np
import cv2.cv as cv

img = cv2.imread("/Users/fideline/Documents/Circles/Circles2.tif")
#img = cv2.medianBlur(img,21)
#ret,gray = cv2.threshold(img,160,255,cv2.THRESH_BINARY)
#cv2.imwrite( "/Users/fideline/Documents/Circles/Thresh.tif", gray);
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray,cv.CV_HOUGH_GRADIENT,1,20, param1=100,param2=40,minRadius=1,maxRadius=60)
# circles = cv2.HoughCircles(gray,cv.CV_HOUGH_GRADIENT,1,20)

print(circles)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
	cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
	cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite( "/Users/fideline/Documents/Circles/DetectedCircles2.tif", img);

