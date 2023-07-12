import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot


cap=cv2.VideoCapture(r'C:\Users\91882\Downloads\EyeBlink.mp4')

detector=FaceMeshDetector(maxFaces=1)

#for ploting based on blink ratio
#w,h,y_limits interval,
plotY=LivePlot(640,480,[20,60],invert=True)

#eye points ids
idList=[22,23,24,26,110,157,158,159,160,161,130,243]
ratioList=[]

frameCount=0
blinkCounter=0
while True:

    success, img = cap.read()

    #facemesh detecting
    img,faces=detector.findFaceMesh(img,draw=False)
    if faces:
        #we have only one face
        face=faces[0]
        for id in idList:
            cv2.circle(img,(face[id]),2,(255,0,255),cv2.FILLED)

        #distance between the points
        leftUP=face[159]
        leftDown=face[23]
        leftLeft=face[130]
        leftRight=face[243]
        left_vertical,_=detector.findDistance(leftUP,leftDown)
        left_horizontal,_=detector.findDistance(leftLeft,leftRight)
        cv2.line(img,leftUP,leftDown,(0,255,0),1)
        cv2.line(img, leftLeft, leftRight, (0, 255, 0), 1)

        #ratio
        ratio=int((left_vertical/left_horizontal)*100)
        ratioList.append(ratio)

        if len(ratioList)>3:
            ratioList.pop(0)

        #smothing the ratio values
        ratioAvg=sum(ratioList)/len(ratioList)

        #threshold for blinking
        if ratioAvg<35 and frameCount==0:
            blinkCounter+=1
            frameCount=1


        if frameCount!=0:
            frameCount+=1
            if frameCount>10:
                frameCount=0

        cvzone.putTextRect(img, f'Blink Count: {blinkCounter}', (50, 100))

        imgPlot=plotY.update(ratioAvg)


        #stacking the two window
        #images,col,scale
        img = cv2.resize(img, (640, 480))
        stackImages=cvzone.stackImages([img,imgPlot],2,1)
    else:
        img = cv2.resize(img, (640, 480))
        stackImages = cvzone.stackImages([img, img], 2, 1)


    cv2.imshow('Naveen',stackImages)
    if cv2.waitKey(25)==ord('b'):
        break