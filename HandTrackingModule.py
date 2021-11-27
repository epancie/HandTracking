import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionConfidence=0.5, trackConfidence=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConfidence =  detectionConfidence
        self.trackConfidence = trackConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands(self.mode, self.maxHands, self.detectionConfidence, self.trackConfidence)



mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils #esto genera puntos de la mano



def main():

    pTime = 0 #previous time
    cTime = 0 #current time
    
    cap = cv2.VideoCapture(1) #captura img de camara id=1
    
    while True:
        succes, img = cap.read()
        
        cTime = time.time()
        fps =  1/(cTime-pTime)
        pTime = cTime
        
        # agrego un texto en la img (img, txt, posicio, font, tamano, color, thickness )
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        
        cv2.imshow("Image", img)
        cv2.waitKey(1)



if __name__ == "__main__":
    main()
