import cv2
import numpy as np

flag = False
ix =-1
iy = -1

def draw(event,x,y,flags,prams):
    global ix,iy,flag
    # print(x,y)
    if event==1:
        flag = True
        ix = x
        iy =y
    elif event==0:
        if flag == True:
            cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)
    elif event==4:
        flag= False
        # cv2.rectangle(img, (ix, iy), (x, y), (255, 23, 200), -1)

cv2.namedWindow('frame')
cv2.setMouseCallback("frame",draw)

img = cv2.imread('blur.jpg')


while(True):
    cv2.imshow('frame',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()