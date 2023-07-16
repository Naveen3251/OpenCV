# Introduction
The MediaPipe Face Detector task lets you detect faces in an image or video. You can use this task to locate faces and facial features within a frame. 
This task uses a machine learning (ML) model that works with single images or a continuous stream of images.

# Face Detection
![Screenshot 2023-07-16 181052](https://github.com/Naveen3251/OpenCv/assets/114800360/abf8e34d-ce89-4914-9c9e-59b6ccaeb628)

# Code Explanation
The code sets up a **FaceDetector** class using MediaPipe for detecting and tracking faces in images or videos.
The FaceDetector class has a parameter called **mindetectionCon**, which determines the minimum detection confidence threshold for face detection.
The FaceDetector class utilizes the MediaPipe library for face detection, which provides pre-trained models and utilities for accurate face detection.
The FaceDetector class includes the findFaces method, which takes an image (img) as input, detects faces in the image, and returns the modified image with bounding boxes around the detected faces.
The findFaces method **converts the image to RGB format, as MediaPipe requires RGB input**.
For each detected face, the method extracts the relative bounding box coordinates and calculates the absolute bounding box coordinates based on the image dimensions.
The method appends the face ID, bounding box coordinates, and detection score to a list called bboxs.
If draw is set to True, the method calls the **fancyDraw** method to draw a rectangle and additional lines on the image to highlight the face.
The method also displays the detection score as a percentage on the image using cv2.putText.
The findFaces method returns the modified image and the bboxs list.
The fancyDraw method is responsible for drawing the rectangle and lines around the face on the image.
In the main function, the code captures video from a webcam using OpenCV (cv2.VideoCapture).
An instance of the FaceDetector class is created, and the findFaces method is called to detect faces in each frame of the video.
The code also calculates the frames per second (FPS) and displays it on the video using cv2.putText.
Finally, the modified video with bounding boxes around the detected faces is displayed in a window named "Naveen".
