from aip import AipFace
import base64

APP_ID = '15926606'
API_KEY = 'IDpHxZLsVhUtv6XErETilME5'
SECRET_KEY = 'kPf8gtTfmkzLDArHmkRs48R4bacAURbY'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

for i in range(1,10):     #range表示每次循环i从1到10，这里代表上传10个用户
        filePath ="user"+ "%04d" % i +".jpg"
	    with open(filePath,"rb") as f:  
		    base64_data = base64.b64encode(f.read())
	    
        image = str(base64_data,'utf-8')
	    imageType = "BASE64"

	    groupId = "student"

	    userId = "user"+ "%04d" % i 

	print(userId)
	client.addUser(image, imageType, groupId, userId);
pass
