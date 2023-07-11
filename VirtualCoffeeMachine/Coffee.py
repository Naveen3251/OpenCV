import cv2
import os
from cvzone import HandTrackingModule as htm


cap=cv2.VideoCapture(0)
#webcam
cap.set(3,640)
cap.set(4,480)


imgBackground=cv2.imread(r'C:\Users\91882\Downloads\OpenCV\VirtualCoffee\Background.png')

#importing backgroundtypes
folder_Modes=r'C:\Users\91882\Downloads\OpenCV\VirtualCoffee\Modes'
image_name=os.listdir(folder_Modes)
imglist=[]
for img in image_name:
    imglist.append(cv2.imread(os.path.join(folder_Modes,img)))


#importing icons
folder_Icons=r'C:\Users\91882\Downloads\OpenCV\VirtualCoffee\Icons'
icon_name=os.listdir(folder_Icons)
iconslist=[]
for icon in icon_name:
    iconslist.append(cv2.imread(os.path.join(folder_Icons,icon)))


#for changing background images
backgroundtype=0
selection=-1
selectionSpeed=7

counter=0
#pass the time in each phase of selection to make more userfriendly
counterPause=0

#for icons
selectionIconList=[-1,-1,-1]

detector=htm.HandDetector(maxHands=1)

#after checking the centre points of mode
mode_centre=[(1136,196),(1000,384),(1136,581)]

while True:
    success,img=cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img)


    #overlaying webcam to imgbackground image
    #h,w
    imgBackground[139:619,50:690]=img

    imgBackground[0:720, 847:1280] = imglist[backgroundtype]


    if hands and counterPause==0 and backgroundtype<3:
        # Hand 1
        hand1 = hands[0]
        fingers1 = detector.fingersUp(hand1)
        #checking
        print(fingers1)

        #checking howmany finger is up
        #i-finger
        if fingers1==[0,1,0,0,0]:
            if selection!=1:
                counter=1
            selection=1
        #2-fingers
        elif fingers1==[0,1,1,0,0]:
            if selection!=2:
                counter=1
            selection=2
        #3-fingers
        elif fingers1==[0,1,1,1,0]:
            if selection!=3:
                counter=1
            selection=3

        #no fingers are there ,no selection no counting
        else:
            selection=-1
            counter=0

        #if fingers there then counter wil become 1 and starts to count
        if counter>0:
            counter+=1
            #to make a arc
            #img,center,(x,y-radius),circle,strt angle of arc,end arc,color,thicknes
            cv2.ellipse(imgBackground,mode_centre[selection-1],(103,103),0,0,counter*selectionSpeed,(0,255,0),20)

            #if i selected the item then we have shift to next page
            if counter*selectionSpeed>360:
                selectionIconList[backgroundtype]=selection
                backgroundtype+=1
                counter=0
                selection=-1
                #activate the counter pause

        #program wait here for a while
        if counterPause>0:
            counterPause+=1
            if counterPause>30:
                counterPause=0

        #adding selected icons
        if selectionIconList[0]!=-1:
            imgBackground[636:701,133:198]=iconslist[selectionIconList[0]-1]
        #for each back groundtype we have 3 icons in icon list
        if selectionIconList[1]!=-1:
            imgBackground[636:701,340:405]=iconslist[2+selectionIconList[1]]
        if selectionIconList[2]!=-1:
            imgBackground[636:701,542:607]=iconslist[5+selectionIconList[2]]

    cv2.imshow("Naveen",imgBackground)
    if cv2.waitKey(1)==ord('b'):
        break
