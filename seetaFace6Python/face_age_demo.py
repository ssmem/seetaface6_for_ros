#_*_coding:utf-8 _*_
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
"""
年龄识别demo
"""
from seetaface.api import *

""" 
使用到的函数:
    两个函数目的相同，但是结果会有一定差异
    PredictAge:  该函数检测一张只有人脸的图片,识别出年龄
    PredictAgeWithCrop：检测一张原图中一个人脸的年龄，需要人脸关键点位置,需要使用到5点关键点检测功能，而关键点检测功能又依赖检测功能 
要加载的功能 :
    年龄识别功能：FACE_AGE
依赖功能:
    FACE_DETECT：人脸检测
    LANDMARKER5：5点关键点检测

"""

""" 检测一张大图中的每个人脸的年龄 """
init_mask = FACE_DETECT|LANDMARKER5|FACE_AGE
seetaFace = SeetaFace(init_mask) #初始化引擎
print(seetaFace)


video = cv2.VideoCapture(0)
#将视频文件初始化为VideoCapture对象
success, frame = video.read()
#read()方法读取视频下一帧到frame，当读取不到内容时返回false!
while success and cv2.waitKey(1) & 0xFF != ord('q'):
#等待1毫秒读取键键盘输入，最后一个字节是键盘的ASCII码。ord()返回字母的ASCII码
    detect_result = seetaFace.Detect(frame)

    for i in range(detect_result.size):
        face = detect_result.data[i].pos
        c_image = frame[face.y:face.y+face.height,face.x:face.x+face.width]
    points_5 = seetaFace.mark5(frame, face)
    age = seetaFace.PredictAgeWithCrop(frame,points_5)
    print("PredictAgeWithCrop:{}".format(age)) 
    cv2.rectangle(frame, (face.x, face.y), (face.x + face.width, face.y + face.height), (255, 0, 0),2)
    cv2.putText(frame, str(age), (face.x+5,face.y+5), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
    cv2.imshow('frame', frame)
    success, frame = video.read()
cv2.destroyAllWindows()
video.release()



#""" 检测一张已经裁剪好的只有人脸的人脸年龄 """
#image = cv2.imread("asserts/crop1.jpg")
#age = seetaFace.PredictAge(image)
#print("PredictAge:{}".format(age))


