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

options = {}
options["face_field"] = "age,beauty"
options["max_face_num"] = 1
options["face_type"] = "LIVE"


result = client.detect(image, imageType, options)
age = result['result']['face_list'][0]['age']
beauty = result['result']['face_list'][0]['beauty']
sex = result['result']['face_list'][0]['gender']

if str(sex) == 'male'
    fsex == '男'
if str(sex) == 'female'
    fsex == '女'

print('估计年龄：' + f'{str(age):.2f}' + '岁' + '  ' + '估计性别：' + fsex + '  ' + '颜值评分：' + '%.2f' %str(beauty) + '分')
#print(result)
