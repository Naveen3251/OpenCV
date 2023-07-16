# Introduction
This project focuses on calculating the total amount of coins in an image or video. It utilizes contour detection and geometric measurements to identify different coins based on their shapes and sizes. 
By analyzing the contours and applying specific criteria, the program determines the type and quantity of coins present, providing an accurate estimation of the total amount.
# Result
![Screenshot 2023-07-16 202151](https://github.com/Naveen3251/OpenCv/assets/114800360/0913ea60-592a-4e42-8e34-f8b3d90f59cd)


# Concepts
**1. Canny Edge Detection** 
Canny edge detection is an algorithm used to detect edges in an image. It works by first applying Gaussian smoothing to reduce noise, then calculating the intensity gradients to identify regions with significant changes in intensity.
A high and low threshold is used to determine which edges to keep based on gradient strength. 
Canny edge detection helps in identifying object boundaries and provides a binary image highlighting these edges.
![image](https://github.com/Naveen3251/OpenCv/assets/114800360/10d5b66a-0250-40cb-aa42-83f2d1ff5364)


**2. Contour Detection** 
Contour detection is the process of identifying and extracting continuous boundaries or curves from an image. 
It is used to find the outline of objects or regions of interest. Contours can be seen as a sequence of points that form the shape of an object in the image.
Contour detection algorithms analyze the image's intensity gradients to identify regions with similar intensity values, indicating a continuous boundary.
![image](https://github.com/Naveen3251/OpenCv/assets/114800360/55b60412-1e9b-4210-af1e-f1c6cc246c03)


**3. Dilation** 
Dilation is a morphological operation that expands or thickens the boundaries of objects in a binary image. 
It is achieved by convolving the image with a structuring element, which is a small predefined shape. Dilation helps in filling gaps, joining nearby edges, and enhancing the overall shape of objects in the image.

**4. Contour Analysis**
Contour analysis involves extracting meaningful information from detected contours. It includes calculating properties such as perimeter, area, centroid, orientation, and more. 
These properties can be used to characterize and classify objects based on their shape, size, and other geometric attributes. Contour analysis is commonly used in object recognition, shape detection, and image-based measurements.

**5. Area Thresholding** 
Area thresholding involves setting specific area criteria to filter and classify contours based on their size or area. By defining minimum and maximum area thresholds, contours can be segmented into different categories or used to identify specific objects in an image. Area thresholding is particularly useful when objects of interest have distinct sizes or when separating foreground and background regions based on their area.

These concepts are fundamental in image processing and computer vision and are commonly employed in various applications, including object detection, feature extraction, image segmentation, and shape analysis.
