import cv2
import mediapipe as mp 
import time


cap = cv2.VideoCapture(1)


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils #esto genera puntos de la mano
pTime = 0 #previous time
cTime = 0 #current time

while True:
    succes, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: #como puede detectar varias manos hago un bucle para cada una
            for id, lm in enumerate(handLms.landmark): #para cada id se tiene un landmark (poscion en la imagen)
                #print(id,lm) # esto muestra para cada id de la mano las pocisiones decimales en la imagen, en fracciones de imagen
                high, witdh , channel = img.shape
                cx, cy = int(lm.x * witdh), int(lm.y * high)
                print(id, cx, cy)
                if id == 0: # si el id es de la muneca dibujo mas grande
                    cv2.circle(img, (cx, cy), 25, (255,0,255), cv2.FILLED)
                if id == 4: # si es la punta del dedo pulgar dibujo mas grande
                    cv2.circle(img, (cx, cy), 15, (255,0,255), cv2.FILLED)



            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) # aca se general los puntos y linea entre puntos

    cTime = time.time()
    fps =  1/(cTime-pTime)
    pTime = cTime

    # agrego un texto en la img (img, txt, posicio, font, tamano, color, thickness )
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

    


    cv2.imshow("Image", img)
    cv2.waitKey(1)