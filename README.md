# Object-looked-at Estimation
Model that estimate the object you look at


## DepthAI version

Work In Progress...  
The model still only works with one person on the video and fo short distance.

**Model sources:**  
* Gaze estimation: [https://github.com/luxonis/depthai-experiments/tree/master/gaze-estimation](https://github.com/luxonis/depthai-experiments/tree/master/gaze-estimation)  
* Mobilenet-SSD: [https://github.com/luxonis/depthai-tutorials/tree/master/1-hello-world](https://github.com/luxonis/depthai-tutorials/tree/master/1-hello-world)  

**Run:**  

`python3 gaze_ssd.py -vid <video_path>`  
or
`python3 gaze_ssd.py -cam`


### First test on mono camera (OAK-1)

**Gaze estimation + Mobilenet-SSD:** 

![blue](utils/blue3.gif)

The model currently run at (on i7-8700 host):  
* 24 FPS with video input from host  
* 18 FPS with onboard camera

**Intersection detection between detection-bboxs and gaze:**   

![blue2](utils/OLAE_1.gif)  

#### TODO

* Integration of Midas V2 model (MonoDepth)

Midas V2 running on NCS2:  
![midas](utils/midasv2_ncs2.gif)
