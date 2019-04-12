import cv2
import os
from aip import AipFace
import base64

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

APP_ID = '15926606'
API_KEY = 'IDpHxZLsVhUtv6XErETilME5'
SECRET_KEY = 'kPf8gtTfmkzLDArHmkRs48R4bacAURbY'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = input('\n 输入用户ID，如1,2,3...然后回车 ==>  ')

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

        cv2.imwrite("facedata1/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >= 5:
         break
    if os.path.isfile("facedata1/" + str(face_id) + '.' + "1.jpg") == False:
        print("没有检测到人脸哦！")
        exit()
    for i in range(1,5):
        filePath = "facedata1/User." + str(face_id) + '.' + str(count) + ".jpg"
    with open(filePath,"rb") as f:
            base64_data = base64.b64encode(f.read())
    image = str(base64_data,"utf-8")
    imageType = "BASE64"
    groupId = "Dev"
    userId = "User" + str(face_id)
    client.addUser(image,imageType,groupId,userId);	
    pass

print("\n [提示]人脸ID：" + str(face_id) + "采集成功！")
print("\n [提示] 正在退出程序...")
cam.release()
cv2.destroyAllWindows()
