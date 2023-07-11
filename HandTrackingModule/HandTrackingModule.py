import cv2
import mediapipe as mp
import time





class HandDetector:
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        # mediapipe initilization for hands
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        # drawing initialization
        self.mpDraw = mp.solutions.drawing_utils

    def finHands(self,img,draw=True):

        #mediapipe always accept RGB format image for processing
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hands.process(imgRGB)

        #if hand detected
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                #extracting landmarks from the hand
                for id,lm in enumerate(handLms.landmark):
                    h,w,c=img.shape
                    #converting the ratio
                    cx,cy=int(lm.x*w),int(lm.y*h)

                    if draw:
                       cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)

                #drawing landmarks on the hand
                self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
        return img

    #to get landmarks
    def findPosition(self,img,handNo=0,draw=True):
        #landmark list
        lmList=[]
        if self.results.multi_hand_landmarks:
            #here we taking only specified hand number in the frame
            myHand=self.results.multi_hand_landmarks[handNo]
            #extracting landmarks from the hand
            for id,lm in enumerate(myHand.landmark):
                h,w,c=img.shape
                #converting the ratio
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        return lmList




def main():
    pTime=0
    cap = cv2.VideoCapture(0)

    #initializing
    detector=HandDetector()
    while True:
        success, img = cap.read()
        #to find thr hands
        img=detector.finHands(img)
        #geting landmarks
        lmList=detector.findPosition(img)
        if len(lmList)!=0:
            print(lmList[4])

        #calculating fps
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime

        #witing fps
        cv2.putText(img,f'Fps:{int(fps)}',(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

        cv2.imshow('Naveen', img)
        if cv2.waitKey(1) == ord('b'):
            break
if __name__=='__main__':
    main()


