import cv2
import numpy as np

def empty(x):
    pass
cv2.namedWindow('parameters')
cv2.resizeWindow('parameters',640,480)
cv2.createTrackbar('threshold1','parameters',100,255,empty)
cv2.createTrackbar('threshold2','parameters',200,255,empty)
cv2.createTrackbar('Area','parameters',1000,20000,empty)
def getContours(imgDilate,imgContours):
    """

    :param imgDiale: we are getting the cordinates of edges to draw the countors
    :param imgCountors: After getting cordinates we draw the countors to orginaal image
    :return:
    """
    contour,hie = cv2.findContours(imgDilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contour:
        area_min = cv2.getTrackbarPos('Area','parameters')
        area = cv2.contourArea(cnt)
        print(area)
        if area > area_min:
            # print(area)
            cv2.drawContours(imgContours,cnt,-1,(0,255,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            # print(len(approx))
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(imgContours,(x,y),(x+w,y+h),(255,0,255),3)
            # cv2.putText(imgContours,"Points"+str(len(approx)),(x+w+20,y+h+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2,0)
            # cv2.putText(imgContours,'Area: '+str(int(area)),(x+w+45,y+h+45),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2,0)
img = cv2.imread('67461825-d04a4400-f62d-11e9-9435-67da073a3c74.jpg',1)
imgContour = img.copy()

imgblur = cv2.GaussianBlur(img,(7,7),1)
imgGray = cv2.cvtColor(imgblur,cv2.COLOR_BGR2GRAY)


imgCanny = cv2.Canny(imgGray,100,200)
kernal = np.ones((5,5),np.uint8)
imgDilate = cv2.dilate(imgCanny,kernal,iterations=1)
getContours(imgDilate, imgContours=imgContour)



cv2.imshow('h',imgGray)
cv2.imwrite('detect.jpg',imgContour)
if cv2.waitKey(0)== ord('q'):
    cv2.destroyAllWindows()