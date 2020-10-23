# seetaface6_for_ros
#Python
```
add
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/seetaFace6Python/seetaface/lib/ubuntu
to your .bashrc  (maybe you should use absolute path)

Attention:
add this 2 lines to keep conda-python away from ros-python:
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')


```









#C++
```
catkin_ws
    src
        detect_face
            include
                seeta
            lib64
            sf3.0_models
            src
                detect_face.cpp
            CMakeList.txt
            package.xml

```
