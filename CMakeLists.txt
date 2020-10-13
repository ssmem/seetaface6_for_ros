cmake_minimum_required(VERSION 3.1)
project(detect_face)
add_compile_options(-std=c++11)

find_package(catkin REQUIRED 
COMPONENTS 
roscpp 

)
find_package(OpenCV REQUIRED)

include_directories(include
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)



catkin_package()
add_executable(detect_face src/detect_face.cpp)


target_link_libraries(detect_face
${OpenCV_LIBRARIES}

${catkin_LIBRARIES} /home/ssmem/pepper_ws/src/detect_face/lib64/libSeetaFaceDetector600.so -ldl -pthread
${catkin_LIBRARIES} /home/ssmem/pepper_ws/src/detect_face/lib64/libtennis.so -ldl -pthread
${catkin_LIBRARIES} /home/ssmem/pepper_ws/src/detect_face/lib64/libSeetaAgePredictor600.so -ldl -pthread
)
