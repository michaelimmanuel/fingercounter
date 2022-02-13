import cv2
import time
import os
import handtrackingmodule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(1)
detector = htm.handDetector(detection_confidence=0.7)

lmList = []

tipid = [4 , 8, 12, 16, 20]

while True:
    
    success, img = cap.read()
    
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:
        
        fingers = []
        
        #thumb
        
        if lmList[tipid[0]][1] < lmList[tipid[0]-1] [1]:
            fingers.append(1)
        else:
            fingers.append(0)
        
        
        
        for id in range(1,5):
            if lmList[tipid[id]][2] < lmList[tipid[id]-2] [2]:
                fingers.append(1)
            else:
                fingers.append(0)
                
        
        #print(fingers)
        
        total_fingers = fingers.count(1)
        print(total_fingers)

                  
        cv2.rectangle(img, (20,225), (170,425),(0,255,0) ,cv2.FILLED)
        cv2.putText(img, str(total_fingers),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(0,0,0),25)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime    
    
    cv2.putText(img, str(round(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3,(0,255,0),3) #display fps
    
    cv2.imshow("image", img)
    cv2.waitKey(1)