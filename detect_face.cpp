#include<opencv2/opencv.hpp>
#include<iostream>
#include<ros/ros.h>
#include <seeta/FaceDetector.h>

using namespace std;
using namespace cv;



int main(int argc, char *argv[])
{

	ros::init(argc, argv, "detect_face");
	seeta::ModelSetting FD_model;
	FD_model.append("/home/ssmem/pepper_ws/src/detect_face/sf3.0_models/face_detector.csta");
	FD_model.set_device(seeta::ModelSetting::CPU);
	seeta::FaceDetector FD(FD_model);
	FD_model.set_id(0);
	VideoCapture cam(0);
	Mat frame;
	Mat canvas;
	SeetaImageData simage;


	while(waitKey(10)!=0){
		cam>>frame;
		cv::flip(frame, canvas, 1);
		simage.width = frame.cols;
		simage.height = frame.rows;
		simage.channels = frame.channels();
		simage.data = frame.data;
		auto infos = FD.detect(simage);

		int line_width = 4;

		for (int i=0; i<infos.size; i++){
		float scale = infos.data[i].pos.width / 300.0;
		float line = 60;
		cv::rectangle(canvas, cv::Rect(canvas.cols - infos.data[i].pos.x - infos.data[i].pos.width, infos.data[i].pos.y, infos.data[i].pos.width, infos.data[i].pos.height), cv::Scalar(0, 255, 0), scale * line_width);
		imshow("demo",canvas);
		}		
	}

return 0;

}
