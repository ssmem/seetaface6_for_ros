#_*_coding:utf-8 _*_
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

from seetaface.api import *

init_mask = FACE_DETECT|FACERECOGNITION|LANDMARKER5

seetaFace = SeetaFace(init_mask)

seetaFace.SetProperty(DetectProperty.PROPERTY_MIN_FACE_SIZE,80)

seetaFace.SetProperty(DetectProperty.PROPERTY_THRESHOLD,0.9)


video = cv2.VideoCapture(0)
success, frame = video.read()

while success and cv2.waitKey(1) & 0xFF != 27:

    detect_result = seetaFace.Detect(frame)
    for i in range(detect_result.size):
        face = detect_result.data[i].pos
        cv2.rectangle(frame, (face.x, face.y), (face.x + face.width, face.y + face.height), (255, 0, 0),2)
        video_face = frame[face.y:(face.y+face.height),face.x:(face.x+face.width)]
        if video_face is None:
            continue
        cv2.imwrite('takephoto.jpg',video_face)
        cv2.imshow('video_face', video_face)
    #cv2.imshow('frame', frame)
    success, frame = video.read()
cv2.destroyAllWindows()
video.release()


