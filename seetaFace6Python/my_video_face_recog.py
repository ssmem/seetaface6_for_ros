#_*_coding:utf-8 _*_
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

from seetaface.api import *


init_mask = FACE_DETECT|FACERECOGNITION|LANDMARKER5
seetaFace = SeetaFace(init_mask)
seetaFace.SetProperty(DetectProperty.PROPERTY_MIN_FACE_SIZE,80)
seetaFace.SetProperty(DetectProperty.PROPERTY_THRESHOLD,0.9)


RecogThreshold = 0.6
image_local_path = "asserts/sushuai.jpg"






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
        image_local = cv2.imread(image_local_path)
        feature_local = seetaFace.ExtractCroppedFace(image_local)
        feature_cam = seetaFace.ExtractCroppedFace(video_face)
        similar = seetaFace.CalculateSimilarity(feature_local,feature_cam)
        if(similar > RecogThreshold):
            cv2.putText(frame, image_local_path[8:-4]+':  '+str(similar)[:-10], (face.x+5,face.y+5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        #cv2.imshow('video_face', video_face)
    cv2.imshow('frame', frame)
    success, frame = video.read()
cv2.destroyAllWindows()
video.release()


