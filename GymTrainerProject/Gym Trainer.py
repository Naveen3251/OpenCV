import cv2
import time
import numpy as np
import PoseDetectionModule as pdm

pTime=0
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
#initialization
detector=pdm.PoseDetector()

#counting lift
count=0
dir=0
hand='right'

while True:
    success, img = cap.read()

    #to find pose
    img=detector.finPose(img,False)

    #extracting the points
    lmList=detector.findPosition(img,False)

    if len(lmList)!=0:
        #to find the angle
        #rightarm
        if hand=='right':
           angle1=detector.findAngle(img,16,14,12)
           #convert to percentage
           angle1_per = np.interp(angle1, (210, 310), (0, 100))

           Angle=angle1_per
        #left arm
        elif hand=='left':
           angle2=detector.findAngle(img, 11, 13, 15)
           # convert to percentage
           angle2_per = np.interp(angle2, (210, 310), (0, 100))
           Angle = angle2_per

        # bar
        #interpolating Angle between (0, 100), (650, 100)

        bar = int(np.interp(Angle, (0, 100), (650, 100)))

        #checking dumbbell curl
        #color changing
        color=(255,0,255)
        #upward
        if Angle==100:
            color = (0, 255, 0)
            if dir==0:
                count+=0.5
                dir=1
        #downward
        if Angle==0:
            color = (0, 255, 0)
            if dir==1:
                count+=0.5
                dir=0

        #bar
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)

        #curl count
        cv2.rectangle(img,(0,450),(250,720),(0,255,0),cv2.FILLED)

        #print
        cv2.putText(img, f'{int(Angle)}%', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 5, color, 5)
        cv2.putText(img,str(int(count)),(45,670),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)


    #calculating fps
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    #witing fps
    cv2.putText(img,f'Fps:{int(fps)}',(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

    cv2.imshow('Naveen', img)
    if cv2.waitKey(1) == ord('b'):
        break