# Introduction
The MediaPipe Hand Landmarker task lets you detect the **landmarks of the hands in an image**. You can use this Task to localize key points of the hands and render visual effects over the hands. This task operates on image data with a machine learning (ML) model as **static data or a continuous stream and outputs hand landmarks in image coordinates** These landmarks are represented as **(x, y) coordinates** within the image, hand landmarks in world coordinates and handedness(left/right hand) of multiple detected hands.

# Hand Landmarks
The hand landmark model bundle detects the keypoint localization of 21 hand-knuckle coordinates within the detected hand regions. The model was trained on approximately 30K real-world images, as well as several rendered synthetic hand models imposed over various backgrounds.

<img width="1073" alt="hand-landmarks" src="https://github.com/Naveen3251/OpenCv/assets/114800360/adc963a3-2084-48c0-bf59-92749dff9708">

# Working
1.The hand landmarker model bundle contains a **palm detection model and a hand landmarks detection model**.<br>
2.The Palm detection model **locates hands within the input image**.<br>
3.Hand landmarks detection model **identifies specific hand landmarks on the cropped hand image defined by the palm detection model**.<br>

# Code Explanation
The code begins by importing necessary libraries: cv2 for computer vision operations and mediapipe for hand tracking.

The HandDetector class is defined, which encapsulates the functionality for detecting and tracking hands. The constructor (__init__ method) initializes various parameters such as mode (whether to track hands in a static image or a video stream), maxHands (maximum number of hands to detect), detectionCon (detection confidence threshold), and trackCon (tracking confidence threshold).

Inside the HandDetector class, the MediaPipe hands module is initialized using self.mpHands = mp.solutions.hands. This module provides pre-trained models and utilities for hand tracking.

The finHands method of the HandDetector class takes an image (img) as input and detects hands in the image. It converts the image to RGB format, as MediaPipe requires RGB input. The self.hands.process function is used to process the RGB image and obtain hand tracking results (self.results).

If hands are detected in the image (self.results.multi_hand_landmarks is not None), the code iterates over each detected hand and extracts the landmarks (key points) of the hand. The landmarks are represented by their normalized coordinates (lm.x and lm.y) relative to the width and height of the image.

If the draw flag is set to True, the code draws circles at the landmark positions using cv2.circle, providing visual feedback of the detected landmarks on the image.

The self.mpDraw.draw_landmarks function is used to draw connections between the landmarks, creating a skeleton-like representation of the hand.

The finHands method returns the modified image with the drawn landmarks and connections.

The findPosition method of the HandDetector class is used to extract the landmark positions for a specific hand (handNo) from the self.results object. It returns a list of landmarks (lmList), where each landmark is represented by its ID, and its corresponding x and y coordinates in the image.

In the main function, the webcam video stream is captured using cv2.VideoCapture(0). The HandDetector object is created, and a while loop is executed to continuously process frames from the video stream.

For each frame, the finHands method is called to detect and draw the hand landmarks on the image. The findPosition method is then called to obtain the landmark positions.

If landmarks are detected (len(lmList) != 0), the code prints the position of the 5th landmark (lmList[4]).

The code calculates the frames per second (FPS) by measuring the time it takes to process each frame.

The FPS value is then displayed on the image using cv2.putText.

Finally, the modified image is displayed in a window named "Naveen". The loop continues until the user presses the 'b' key, upon which the program exits.
