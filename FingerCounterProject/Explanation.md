# Introduction
The project is used to count the fingers of the hands.It is the Application of **HandTracking Module in MediaPipe**

# Result
![Screenshot 2023-07-16 191936](https://github.com/Naveen3251/OpenCv/assets/114800360/677173d8-8c3d-4745-932c-a9bded7f496b)

# Code Explanation

**HandTracking:**

- The code initializes a video capture using OpenCV to capture frames from the webcam.
- The frame size is set to **640x480** using the `cap.set()` function.
- A variable `pTime` is initialized to keep track of the previous frame's time.

**Finger Images:**

- The code defines a folder path (`folderPath`) where the finger images are stored.
- The list of files in the folder is obtained using `os.listdir(folderPath)`.
- The code creates an empty list (`overlayList`) to store the resized finger images.
- For each image file in the folder, the code reads the image using `cv2.imread()`.
- The image is resized to a dimension of 200x200 using `cv2.resize()`.
- The resized image is appended to the `overlayList`.

**Overlay Image:**

- The code initializes the `HandDetector` class from the `HandTrackingModule` (custom module) with a** detection confidence of 0.75**.
- Inside the while loop, it reads frames from the video capture.
- The code calls the **`finHands` method of the `HandDetector` class** to detect hands in the frame.
- The code calls the **`findPosition` method of the `HandDetector` class** to get the landmark positions of the detected hands.
- The code checks if there are any detected landmarks (`lmList`) for further processing.

**Fingers other than Thumb:**

- For the  four fingers except thumb, the code compares the **y-coordinate of the tip with the y-coordinate of the corresponding knuckle** (`lmList[tipIds[id]]` and `lmList[tipIds[2] - 2]`).
- If the tip is below the knuckle, the finger is considered closed; otherwise, it is considered open.
- The status of each finger is appended to the `fingers_status` list.

**How can you tell if the thumb is closed (exceptional finger):**

- For the thumb, the code compares the x-coordinate of the tip (`lmList[tipIds[0]]`) with the **x-coordinate of the point before the tip (`lmList[tipIds[0] - 1]`)**.
- If the tip is to the right of the previous point (for the right hand), the thumb is considered closed; otherwise, it is considered open.

**Changing image accordingly:**

- The code **counts the number of opened fingers** by counting the occurrences of 1 in the `fingers_status` list using `fingers_status.count(1)`.
- Depending on the number of opened fingers, the code overlays the corresponding finger image from the `overlayList` on the top-left corner of the frame using array slicing (`img[0:200,0:200] = overlayList[totalFingers]`).

**Add rectangle:**

- The code adds a rectangle using `cv2.rectangle()` to create a background for displaying the finger count.
- The rectangle is drawn from coordinates (20, 255) to (170, 425) with a green color `(0,255,0)` and filled with the `cv2.FILLED` parameter.
- The finger count is displayed inside the rectangle using `cv2.putText()`.

**Calculating FPS and Displaying:**

- The code calculates the frames per second (FPS) by dividing 1 by the time difference between the current frame and the previous frame.
- The current time is obtained using `time.time()`.
- The code displays the FPS value using `cv2.putText()`.

**Displaying the Result:**

- The modified frame with finger overlays, finger count rectangle, and FPS display is shown in a window named "Naveen".
- The while loop continues until the user presses the 'b' key, upon which the program exits.
  
