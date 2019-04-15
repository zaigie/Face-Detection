from aip import AipFace
import base64

APP_ID = '15926606'
API_KEY = 'IDpHxZLsVhUtv6XErETilME5'
SECRET_KEY = 'kPf8gtTfmkzLDArHmkRs48R4bacAURbY'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

filePath ="eee.jpg"
with open(filePath,"rb") as f:  
    base64_data = base64.b64encode(f.read())
image = str(base64_data,'utf-8')
imageType = "BASE64"

groupIdList = 'mingxing'

a = client.search(image,imageType,groupIdList)
name = a['result']['user_list'][0]['user_id']
score = a['result']['user_list'][0]['score']

print('姓名：' + str(name) + '  ' + '相似度：' + f'{score:.2%}')
#print(a)
