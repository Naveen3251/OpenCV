import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np
import math
#initializing video
cap=cv2.VideoCapture(r'C:\Users\91882\Downloads\OpenCV\BasketShot\Videos\vid (6).mp4')

#color finder obj
#true-->gives trackbar to get the color manually
#myColorFinder=ColorFinder(True)

#now we can make false
myColorFinder=ColorFinder(False)

#after debuggs we get color of ball
hsvVals={'hmin': 8, 'smin': 96, 'vmin': 115, 'hmax': 14, 'smax': 255, 'vmax': 255}


#var
ballTrackPosListX=[]
ballTrackPosListY=[]

#width
xList=[item for item in range(0,1300)]

prediction=False

while True:
    success,img=cap.read()


    #to get hsv vals of ball i used image to get that after using that vals for video
    #img=cv2.imread(r'C:\Users\91882\Downloads\OpenCV\BasketShot\Ball.png')

    #cropping the lower region
    #h,w-->y,x
    img=img[0:900,:]

    #find the color ball
    #mask tracks the targeted object on the video(in white color) here it is ball
    ballImg,mask=myColorFinder.update(img,hsvVals)


    #finding location of ball in original frame  w.r.t its  mask
    imgContoursBall,contours=cvzone.findContours(img,mask,minArea=500)

    # point by point
    if contours:
        # take biggest contour it is already sorted in package
        ballTrackPosListX.append(contours[0]['center'][0])
        ballTrackPosListY.append(contours[0]['center'][1])

    if ballTrackPosListX:
        # Polynomial regression of deg=2  (y=ax^2+bx+c)
        a,b,c=np.polyfit(ballTrackPosListX,ballTrackPosListY,2)



        # keeping dot at centre of contour and connecting the contours with line
        for i, (posx,posy) in enumerate(zip(ballTrackPosListX,ballTrackPosListY)):
            pos=(posx,posy)
            cv2.circle(imgContoursBall, pos, 10, (0, 255, 0), cv2.FILLED)
            if i != 0:
                cv2.line(imgContoursBall, pos, (ballTrackPosListX[i - 1],ballTrackPosListY[i - 1]), (0, 255, 0), 2)


        #tracing parabolic path for ball for each iteration
        for x in xList:
            y=int(a*x**2 + b*x + c)
            cv2.circle(imgContoursBall, (x,y), 5, (255, 0, 255), cv2.FILLED)

        #for 10 frame doing the prediction
        if len(ballTrackPosListX)<10:
            # find value of x when y=590(basket)
            c = c - 590
            x = int((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
            prediction=330 < x < 430




        if prediction:
            cvzone.putTextRect(imgContoursBall, "BASKET", (50, 100), scale=5, thickness=5, colorR=(0, 255, 0),
                                   offset=20)
        else:
            cvzone.putTextRect(imgContoursBall, "NO BASKET", (50, 100), scale=5, thickness=5, colorR=(0, 0, 255),
                                   offset=20)



    #dsize is (0, 0), it means the size will be calculated based on the other provided parameters.
    #If dsize is not specified, the output width will be calculated as (src_width * fx) and (src_height*fy)
    imgContours=cv2.resize(imgContoursBall,dsize=(0,0),dst=None,fx=0.7,fy=0.7)

    #cv2.imshow('Naveen',img)
    cv2.imshow('debug',imgContours)
    if cv2.waitKey(200)==ord('b'):
        break