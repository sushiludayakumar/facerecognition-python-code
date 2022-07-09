#FACE RECOGNITION

import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('sus.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors =9)


for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
    #w and h are height and width

cv2.imshow('FACE RECOGNITION',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
