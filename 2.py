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
count = 0
while(True):

    ret, img = cam.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        cv2.imwrite("cache/cache.jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >= 1:
         break
cam.release()
cv2.destroyAllWindows()

filePath ="cache/cache.jpg"
with open(filePath,"rb") as f:  
    base64_data = base64.b64encode(f.read())
image = str(base64_data,'utf-8')
imageType = "BASE64"

groupIdList = 'Dev'

a = client.search(image,imageType,groupIdList)
name = a['result']['user_list'][0]['user_id']
score = a['result']['user_list'][0]['score']

print('用户：' + str(name) + '  ' + '相似度：' + f'{score:.2f}' + "%")

os.remove("cache/cache.jpg")
#print(a)
