# Introduction
The MediaPipe Pose Landmarker task lets you detect landmarks of human bodies in an image or video. You can use this task to identify key body locations, analyze posture, and categorize movements.
This task uses machine learning (ML) models that work with single images or video.

# Pose Landmarks
The pose landmarker model tracks 33 body landmark locations, representing the approximate location of the following body parts:

<img width="723" alt="pose_landmarks_index" src="https://github.com/Naveen3251/OpenCv/assets/114800360/dbbc5e76-0e79-4a1e-8732-054c9c411480">

0 - nose
1 - left eye (inner)
2 - left eye
3 - left eye (outer)
4 - right eye (inner)
5 - right eye
6 - right eye (outer)
7 - left ear
8 - right ear
9 - mouth (left)
10 - mouth (right)
11 - left shoulder
12 - right shoulder
13 - left elbow
14 - right elbow
15 - left wrist
16 - right wrist
17 - left pinky
18 - right pinky
19 - left index
20 - right index
21 - left thumb
22 - right thumb
23 - left hip
24 - right hip
25 - left knee
26 - right knee
27 - left ankle
28 - right ankle
29 - left heel
30 - right heel
31 - left foot index
32 - right foot index

# Code Explanation
The code sets up a **PoseDetector class** using MediaPipe for detecting and tracking human poses in images or videos.

The PoseDetector class has various parameters, including **mode** (determines the mode of pose detection), **upBody** (specifies whether to detect the upper body only), **smooth** (controls the smoothing of pose landmarks), **detectionCon** (detection confidence threshold), and **trackCon** (tracking confidence threshold).

The PoseDetector class utilizes the MediaPipe library for pose detection, which provides pre-trained models and utilities for accurate pose estimation.

The PoseDetector class includes methods such as **finPose** (to detect and draw pose landmarks on an image) and **findPosition** (to extract the landmark positions of detected poses).

The PoseDetector class also includes the **findAngle method**, which calculates the angle between three specified points based on the landmark positions.

In the main function, the code captures video from a webcam using OpenCV (cv2.VideoCapture).

An instance of the PoseDetector class is created, and the finPose method is called to detect poses in each frame of the video.

The findPosition method is then called to extract the landmark positions of the detected poses.

The code also calculates the frames per second (FPS) and displays it on the video.

Finally, the modified video with pose landmarks is displayed in a window named "Naveen"
