# 'mediapipe_ros' Package
This repository is pose estimation program by mediapipe.
*   Maintainer: Shoichi Hasegawa ([hasegawa.shoichi@em.ci.ritsumei.ac.jp](mailto:hasegawa.shoichi@em.ci.ritsumei.ac.jp)).
*   Author: Shoichi Hasegawa ([hasegawa.shoichi@em.ci.ritsumei.ac.jp](mailto:hasegawa.shoichi@em.ci.ritsumei.ac.jp)).

**Content:**

*   [Setup](#Setup)
*   [Launch](#launch)
*   [Files](#files)
*   [References](#References)


## Setup
`pip install requirements.txt`  
(Since library `opencv-python` and `opencv-contrib-python` conflict, delete `opencv-python`.)

## Launch
* `python main.py`  
* `python main_ros.py`

## Files
 - `README.md`: Read me file (This file)

 - `__init__.py`: Code for initial setting (PATH and parameters)

 - `main.py`: Code for mediapipe. By reading image file, this program is executed.

 - `main_ros.py`: Code for mediapipe by ROS.

## References

