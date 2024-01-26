import cv2
import numpy as np
import stack_image


weidth = 640
hieght = 480

cap = cv2.VideoCapture(0)
cap.set(3,weidth)
cap.set(4,hieght)

while(True):
    ret , frame = cap.read()
    kernal = np.ones((5,5),dtype=np.uint8)

    if ret==True:
        # cv2.imshow('image',frame)

        imggray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imggray,(7,7),0)
        imgcanny = cv2.Canny(imgBlur,100,200)
        imgDialtion = cv2.dilate(imgcanny,kernal,iterations=2)
        imgeroded = cv2.erode(imgDialtion,kernal,iterations=2)
        stack = stack_image.stackImages(0.5,([frame,imggray,imgBlur],[imgcanny,imgDialtion,imgeroded]))
        cv2.imshow('image',stack)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;
    else:
        break;

cap.release()

cv2.destroyAllWindows()


