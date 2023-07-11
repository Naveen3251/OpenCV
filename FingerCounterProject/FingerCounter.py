import cv2
import time
import os
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

pTime=0


#tip ids
tipIds=[4,8,12,16,20]
#rrading images
folderPath='FingerImages'
myList=os.listdir(folderPath)
print(myList)
#overlaylist of images
overlayList=[]
for imgPath in myList:
    img=cv2.imread(f'{folderPath}/{imgPath}')
    img=cv2.resize(img,(200,200))
    overlayList.append(img)

#handdetetor module initializer
detector=htm.HandDetector(detectionCon=0.75)
while True:
    success, img = cap.read()

    #finding hands
    img=detector.finHands(img,draw=False)

    #getting landmarks
    lmList=detector.findPosition(img,draw=False)

    #8,12,16,20 are ti[ of fingers and there are 4 points in each
    #5-8,9-12,13-16,17-20
    #if fingers below half then it is closed

    #for thumb alone 3 points tip is 4
    #if it is left to the hand then it is closed(for RIght hand)
    if len(lmList)!=0:
        #status
        fingers_status=[]
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers_status.append(1)
        else:
            fingers_status.append(0)
        #for fore fingers
        for id in range(1,5):
            if lmList[tipIds[id]][2]<lmList[tipIds[2]-2][2]:
                fingers_status.append(1)
            else:
                fingers_status.append(0)

        #counting one
        totalFingers=fingers_status.count(1)

        #overlaying images in frame
        if totalFingers==0:
            img[0:200, 0:200] = overlayList[0]

        else:
            img[0:200,0:200]=overlayList[totalFingers]

        #diplaying finger count
        cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
        cv2.putText(img, f'{totalFingers}', (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)


    # calculating fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # witing fps
    cv2.putText(img, f'Fps:{int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow('Naveen', img)
    if cv2.waitKey(1) == ord('b'):
        break