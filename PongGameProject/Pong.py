import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap=cv2.VideoCapture(0)

#webcam
cap.set(3,1200)
cap.set(4,720)

#importing  file images
#reading in BGR
imgBackGround=cv2.imread(r'C:\Users\91882\Downloads\OpenCV\Pong Game\Files\Background.png')
imgGameOver=cv2.imread(r'C:\Users\91882\Downloads\OpenCV\Pong Game\Files\gameOver.png')

#reading as it is preserving orginal property
imgBall=cv2.imread(r'C:\Users\91882\Downloads\OpenCV\Pong Game\Files\Ball.png',-1)
imgPaddle_1=cv2.imread(r'C:\Users\91882\Downloads\OpenCV\Pong Game\Files\bat1.png',-1)
imgPaddle_2=cv2.imread(r'C:\Users\91882\Downloads\OpenCV\Pong Game\Files\bat2.png',-1)

#initilization for hand-detect module
detector = HandDetector(detectionCon=0.8, maxHands=2)

#variables
#ball position
ballPos=[100,100]
#speed of ball
speedX=10
speedY=10
#flag
gameOver=False
#for left and right score
score=[0,0]
while True:
    success,img=cap.read()

    #horizontal flip
    img=cv2.flip(img,1)

    #to display
    iAm=img.copy()

    #find the hands and landmarks
    hands,img=detector.findHands(img,flipType=False)#with drawing

    #overlaying the background
    #params:videoframe,alpha(determine opacity),image,1-alpha
    #here 1-alpha==>inverse transperency determines how much percent it visible,gamma(determines brightness)
    img=cv2.addWeighted(img,0.2,imgBackGround,0.8,0)

    if hands:
        for myhand in hands:
            #hand bbox information xoordinates and w,h
            x,y,w,h=myhand['bbox']

            h_1,w_1,_=imgPaddle_1.shape

            #move paddle based on the centre of image
            #original-centre

            # for left and right
            centre=y-h_1//2
            boundary=np.clip(centre,20,415)#boundary condition


            if myhand['type']=='Left':
                img = cvzone.overlayPNG(img, imgPaddle_1, (59, boundary))
                #ball is hitting or not
                if 59<=ballPos[0]<59+10 and boundary<ballPos[1]<boundary+h_1:
                    speedX = -speedX
                    #bouncing back
                    ballPos[0]+=30
                    score[0]+=1

            if myhand['type']=='Right':
                img = cvzone.overlayPNG(img, imgPaddle_2, (1195, boundary))
                # ball is hitting or not
                if 1195-50 < ballPos[0] < 1195-28 and boundary < ballPos[1] < boundary+h_1:
                    speedX = -speedX
                    # bouncing back
                    ballPos[0] -= 30
                    score[1] += 1

    #gameOver
    if ballPos[0]<30 or ballPos[0]>1200:
        gameOver=True
    #dont move the ball
    if gameOver:
        img=imgGameOver
        cv2.putText(img, str(score[0]+score[1]), (585, 360), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 20), 5)
    #move the ball
    else:
        # boundary conditions changing direction accordingly
        # up and down boundary
        if ballPos[1] >= 500 or ballPos[1] <= 10:
            speedY = -speedY

        # making the dynamic movement of the ball
        ballPos[0] += speedX
        ballPos[1] += speedY

        # draw the ball
        # params:source image,image to overlay,position
        img = cvzone.overlayPNG(img, imgBall, ballPos)

        cv2.putText(img,str(score[0]),(300,650),cv2.FONT_HERSHEY_COMPLEX,3,(255,255,255),5)
        cv2.putText(img, str(score[1]), (900, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)


    img[580:700,20:233]=cv2.resize(iAm,(213,120))
    cv2.imshow('Naveen-Pong',img)
    key=cv2.waitKey(1)
    if key==ord('r'):
        # variables
        # ball position
        ballPos = [100, 100]
        # speed of ball
        speedX = 10
        speedY = 10
        # flag
        gameOver = False
        # for left and right score
        score = [0, 0]
        imgGameOver = cv2.imread(r'C:\Users\91882\Downloads\OpenCV\Pong Game\Files\gameOver.png')
    if key==ord('q'):
        break

