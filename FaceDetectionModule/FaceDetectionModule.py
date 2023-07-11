import cv2
import mediapipe as mp
import time

class FaceDetector:
    def __init__(self,mindetectionCon=0.5,):

        self.mindetectionCon=mindetectionCon


        # mediapipe initilization for faces
        self.mpFaceDetection = mp.solutions.face_detection
        self.faceDetection = self.mpFaceDetection.FaceDetection(0.75)
        # drawing initialization
        self.mpDraw = mp.solutions.drawing_utils

    def findFaces(self,img,draw=True):

        #mediapipe always accept RGB format image for processing
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.faceDetection.process(imgRGB)

        # lists
        bboxs = []

        #if hand detected
        if self.results.detections:
            for id,detection in enumerate(self.results.detections):
                    #in relative bounding box we have xmin ymin width height
                    bboxC=detection.location_data.relative_bounding_box
                    #shape
                    ih,iw,ic=img.shape
                    #to draw bounding box calculating values
                    bbox=int(bboxC.xmin*iw),int(bboxC.ymin*ih),\
                         int(bboxC.width*iw),int(bboxC.height*ih)

                    #appending
                    bboxs.append([id,bbox,detection.score])
                    #fancy draw face
                    if draw:
                        img=self.fancyDraw(img,bbox)
                    #detection score
                    cv2.putText(img, f'{int(detection.score[0]*100)}%', (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        return img,bboxs
    def fancyDraw(self,img,bbox,l=30,t=10):
        x,y,w,h=bbox
        x1,y1=x+w,y+h

        #drawing rectangle
        cv2.rectangle(img,bbox,(255,0,255),2)

        #top left x,y
        cv2.line(img,(x,y),(x+l,y),(255,0,255),t)
        cv2.line(img, (x, y), (x, y+l), (255, 0, 255), t)

        #top right x1,y
        cv2.line(img, (x1, y), (x1-l, y), (255, 0, 255), t)
        cv2.line(img, (x1, y), (x1, y + l), (255, 0, 255), t)

        # bottom left x,y1
        cv2.line(img, (x, y1), (x, y1), (255, 0, 255), t)
        cv2.line(img, (x, y1), (x, y1 - l), (255, 0, 255), t)

        # bottom right x1,y1
        cv2.line(img, (x1, y1), (x1-l, y1), (255, 0, 255), t)
        cv2.line(img, (x1, y1), (x1, y1 - l), (255, 0, 255), t)

        return img


def main():
    pTime=0
    cap = cv2.VideoCapture(0)

    #initializing
    detector=FaceDetector()
    while True:
        success, img = cap.read()
        #to find thr hands
        img,bboxs=detector.findFaces(img)



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

