import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import random
import os



cap=cv2.VideoCapture(0)
#setting
#width
cap.set(3,1280)
#height
cap.set(4,720)

#initialization
#only one player
detector=FaceMeshDetector(maxFaces=1)

#lip ids
#up,down,left,right
idList=[0,17,78,292]

#taking images

#eatable folder
folderEatable=r'C:\Users\91882\Downloads\OpenCV\OpenCvGame\Objects\Eatable'
listEatable=os.listdir(folderEatable)
eatables=[]
for object in listEatable:
    #-1 => preserving the original property
    eatables.append(cv2.imread(f'{folderEatable}/{object}',-1))


#non eatable folder
folderNonEatable=r'C:\Users\91882\Downloads\OpenCV\OpenCvGame\Objects\noneatable'
listNonEatable=os.listdir(folderNonEatable)
nonEatables=[]
for object in listNonEatable:
    #-1 => preserving the original property
    nonEatables.append(cv2.imread(f'{folderNonEatable}/{object}',-1))


global isEatable
isEatable=True
#droping obj
currObject=eatables[0]
#x,y
dynamicPos=[300,0]
speed=5
count=0

gameOver=False

#endpoint
def resetObj():
    global isEatable
   #x(changing),y=0
    dynamicPos[0]=random.randint(100,1180)#changes globally
    dynamicPos[1]=0
    randNo=random.randint(0,2)

    if randNo==0:
        currObject=nonEatables[random.randint(0,3)]
        isEatable=False
    else:
        currObject=eatables[random.randint(0,3)]
        isEatable=True

    return currObject



while True:
    success,img=cap.read()

    if gameOver is False:
        img, faces = detector.findFaceMesh(img, draw=False)

        # droping the bject
        img = cvzone.overlayPNG(img, currObject, dynamicPos)
        dynamicPos[1] += speed

        # heightFrame-HeightofImages-beforeboundary
        bound = 720 - 100 - 50

        # randomly chnaging the object
        if dynamicPos[1] > bound:
            currObject = resetObj()

        if faces:
            # here,have only one face
            face = faces[0]
            # to get points of lips(top down left right)
            '''for idNo,point in enumerate(face):
                cv2.putText(img,str(idNo),point,cv2.FONT_HERSHEY_SIMPLEX,0.4,(255,0,255),1)'''

            # highlighting the points
            for id in idList:
                cv2.circle(img, face[id], 5, (255, 0, 255), 5)

            # connecting line
            # up and down
            cv2.line(img, face[idList[0]], face[idList[1]], (0, 255, 0), 3)
            # left and right
            cv2.line(img, face[idList[2]], face[idList[3]], (0, 255, 0), 3)

            # to find distance between the points
            upDown, _ = detector.findDistance(face[idList[0]], face[idList[1]])
            leftRight, _ = detector.findDistance(face[idList[2]], face[idList[3]])

            # print(face[idList[0]])-->eg:[620, 494]
            # print(face[idList[1]])-->eg:[620, 519]
            # centre point mouth
            cx, cy = (face[idList[0]][0] + face[idList[1]][0]) // 2, (face[idList[0]][1] + face[idList[1]][1]) // 2

            # joining with line
            # width,height of image is 100,100 to get centre 50,50

            cv2.line(img, (cx, cy), (dynamicPos[0] + 50, dynamicPos[1] + 50), (0, 255, 0), 3)

            # distance between mouth and obj
            distanceMouthObj, _ = detector.findDistance((cx, cy), (dynamicPos[0] + 50, dynamicPos[1] + 50))

            # lip open or close(distance ratio)
            ratio = int((upDown / leftRight) * 100)
            # print(ratio)

            # fixing threshold after analysing
            if ratio > 75:
                mouthStatus = 'Open'
            else:
                mouthStatus = 'Closed'
            cv2.putText(img, mouthStatus, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 2)

            # reseting based on eating
            if distanceMouthObj < 100 and ratio > 60:
                if isEatable:
                    currObject = resetObj()
                    count += 1
                else:
                    gameOver = True
            cv2.putText(img, str(count), (1100, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 2)
    else:
        cv2.putText(img, "GAMEOVER", (300, 400), cv2.FONT_HERSHEY_PLAIN, 7, (255, 0, 255), 10)

    cv2.imshow('Naveen',img)
    if cv2.waitKey(1)==ord('r'):
        currObject=eatables[random.randint(0,3)]
        isEatable=True
        gameOver=False
        count=0
    if cv2.waitKey(1) == ord('b'):
        break

