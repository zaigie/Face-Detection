import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

name = input('\n 输入姓名（英文），然后回车 ==>  ')

print("\n [提示] 正在进行人脸采集，请看向摄像头并等待...")
count = 0

while(True):

    ret, img = cam.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        cv2.imwrite("dataset/" + str(name) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >= 30:
         break

f = open('facedata.txt','a')
f.write(str(name) + '\n')
f.close()
print("\n [提示] 正在退出程序...")
cam.release()
cv2.destroyAllWindows()