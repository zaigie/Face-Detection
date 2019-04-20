# logic:
## 旧逻辑（opencv+baidu）
opencv_detect:
True（检测到一张人脸）:
    (baidu_detect):
        检测最大人脸，返回可选参数（年龄，眼镜评分等）:
            (upload_baidu)：
                存储user_id和group_id
False:
    (return:没有人脸)

## 旧逻辑优化(或将舍弃opencv)
opencv_takepic:
True（拍照成功）：
    (baidu_detect):
        检测最大人脸（face1），返回可选参数（年龄，眼镜评分等）:
            True:
                （upload_baidu）:
                    将最大人脸框内（百度画框）单独上传，存储user_id和group_id
            False:
                （return:没有人脸！）
False:
    （return:拍照失败！）

## 新逻辑（Arc）

