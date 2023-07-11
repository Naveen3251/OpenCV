import cv2
import time
import HandTrackingModule as htm
import numpy as np

########pycaw###############
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#initialization
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

#############################
volumeRange=volume.GetVolumeRange()
#min volume
minVol=volumeRange[0]
maxVol=volumeRange[1]
print(minVol)
print(maxVol)
####
wCam,hCam=640,480
####
#using pycaw for interacting with system volume


cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

pTime=0
vol=0
volBar=400
volPer=0
#initialization
detector=htm.HandDetector(detectionCon=0.7)
while True:
    success, img = cap.read()

    #finding hands
    img=detector.finHands(img,draw=False)
    #getting landmarks
    lmList=detector.findPosition(img,draw=False)

    #tip of index(8) and thumb finger(4)
    if len(lmList)!=0:
        #for thumb
        x1,y1=lmList[4][1],lmList[4][2]
        #for lindex
        x2,y2=lmList[8][1],lmList[8][2]

        ##to find midpoint
        cx,cy=(x1+x2)//2,(y1+y2)//2

        #drawing circle on that
        cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        #joining these two cicle
        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)

        #drawing midpoint circle
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        #to find length between two points
        length=np.hypot(x2-x1,y2-y1)
        #to get my hand range
        print(length)

        #HandRange 50-300
        #VolumeRange -65.25 - 0

        #interpolating the points to get in sme range
        #convert value,range,range to which we want to convert

        # interpolating length between [50,300]-->[-65.25,0]
        vol=np.interp(length,[50,300],[minVol,maxVol])

        #volume for bar
        # interpolating length between [50,300] to [400,150]
        volBar=np.interp(length,[50,300],[400,150])

        #vlume in percentage
        volPer = np.interp(length, [50, 300], [0, 100])

        #seting the volume of system
        volume.SetMasterVolumeLevel(vol, None)

        #fixing threshold
        if length<150:
            cv2.circle(img, (cx, cy), 15, (0,255,0), cv2.FILLED)

    #volume bar
    #outer area
    cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
    #dynamic change in fill
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    #writing volume
    cv2.putText(img, f'Fps:{int(volPer)}%', (40, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    #calculating fps
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    #witing fps
    cv2.putText(img,f'Fps:{int(fps)}',(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    cv2.imshow('Naveen', img)
    if cv2.waitKey(1) == ord('b'):
        break

