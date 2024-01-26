import cv2

img = cv2.imread('img.png',1)

img = cv2.line(img,(0,0),(255,255),(0,255,0),5)
img = cv2.arrowedLine(img,(0,255),(523,135),(0,255,255),5)
img = cv2.rectangle(img,(238,345),(456,654),(255,255,244),5)
img = cv2.circle(img,(345,431),60,(124,34,67),-1)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,'OpenCv',(40,89,),font,4,(205,67,88),5,cv2.LINE_AA)



cv2.imshow('img',img)
k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()

