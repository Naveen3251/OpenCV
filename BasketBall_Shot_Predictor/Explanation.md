# Introduction
This project focuses on tracking the position and predicting the trajectory of a ball using color detection and polynomial regression. It demonstrates how computer vision techniques can be applied to analyze and understand the motion of objects in a video.

# Result
# Excatly predicted the ball will go into the basket
![Screenshot 2023-07-16 200044](https://github.com/Naveen3251/OpenCv/assets/114800360/02d2bbc0-0131-4e21-ac86-ad61fbe98e98)

# Excatly predicted the ball won't go into the basket
![Screenshot 2023-07-16 200205](https://github.com/Naveen3251/OpenCv/assets/114800360/8c38b9cb-ed41-435e-a536-fa6f74c2255b)

# Contours
Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity. 
The contours are a useful tool for shape analysis and object detection and recognition.
![image](https://github.com/Naveen3251/OpenCv/assets/114800360/1e454ad4-0eed-4177-8ac2-17d7d6d06cd8)


# Polynomial Regression

![image](https://github.com/Naveen3251/OpenCv/assets/114800360/f0387542-fc55-4614-8703-caa6fa75787e)

In this code, polynomial regression is used to predict the trajectory of a ball based on its previous tracked positions. The ball's x and y coordinates are tracked and stored in `ballTrackPosListX` and `ballTrackPosListY` respectively. A second-degree polynomial regression model (`y = ax^2 + bx + c`) is then fitted to these data points using NumPy's `polyfit` function.

The coefficients `a`, `b`, and `c` of the polynomial equation are obtained, representing the parabolic path of the ball. The parabolic path is traced by iterating through a range of x-values (`xList`) and calculating the corresponding y-values using the polynomial equation. These points are then visualized on the `imgContoursBall` image.

Furthermore, a prediction is made by finding the x-value where the ball's y-value is equal to the y-coordinate of the basket (590 pixels). This is done by adjusting the polynomial equation and solving for x. If the predicted x-value falls within a certain range (`330 < x < 430`), it indicates that the ball is predicted to go through the basket. The prediction result is displayed on the image as "BASKET" or "NO BASKET" using the `cvzone.putTextRect` function.
