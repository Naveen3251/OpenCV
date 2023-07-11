import cv2
import cvzone
import numpy as np

#finding based on clor
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,380)


#money counter
totalMoney=0



def empty(a):
    pass

#keeping window name
cv2.namedWindow("Settings")
#param:same window name,size of the window
cv2.resizeWindow("Settings",640,240)
#creating tracking bar
#name,windowname,min,max,simple funct
cv2.createTrackbar("Threshold1","Settings",100,255,empty)
cv2.createTrackbar("Threshold2","Settings",150,255,empty)
def preProcessing(img):
    #blurring the image
    imgPre=cv2.GaussianBlur(img,(5,5),3)

    #to get trackbar position
    #trackbar window name,original window name
    thresh1=cv2.getTrackbarPos("Threshold1","Settings")
    thresh2 = cv2.getTrackbarPos("Threshold2", "Settings")

    #canny edge detection
    #images and threshold(min,max)
    imgPre=cv2.Canny(imgPre,thresh1,thresh2)

    #dialate(thicken the edges) and close method(close the gaps in contours)

    #create first kernel
    kernel=np.ones((3,3),np.uint8)
    #dialate
    imgPre=cv2.dilate(imgPre,kernel,iterations=1)
    #close method for the morphology
    imgPre=cv2.morphologyEx(imgPre,cv2.MORPH_CLOSE,kernel)

    return imgPre



while True:
    success,img=cap.read()

    #preprocessing the frame
    imgPre=preProcessing(img)

    #contorous detection
    imgContours,conFound=cvzone.findContours(img,imgPre,minArea=20)

    totalMoney=0

    if conFound:
        for contour in conFound:
            #perimeter
            peri = cv2.arcLength(contour['cnt'], True)
            #it resuces number of vertex in curve and aproxx to straight line
            approx = cv2.approxPolyDP(contour['cnt'], 0.02 * peri, True)

            if len(approx)>5:

                #area of contours
                area=contour['area']
                #experimenting to get area of coin
                print(area)
                #after some experiment by placing a coin the contours area lies in this range corresponding to coins
                if 6000<area<7000:
                    totalMoney += 1
                elif area>7150:
                    totalMoney += 2
                else:
                    totalMoney+=5

    #created empty image and puting amount on the image

    #stacking images
    #param:images,numOfColumns
    imgstacked=cvzone.stackImages([img,imgPre,imgContours],2,1)
    cvzone.putTextRect(imgstacked,f'Rs.{totalMoney}',(950,550))

    cv2.imshow('Image', imgstacked)

    if cv2.waitKey(1)==ord('b'):
        break