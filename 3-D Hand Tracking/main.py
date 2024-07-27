import cv2
from cvzone.HandTrackingModule import HandDetector

#WEBCAM
cap = cv2.VideoCapture(0)
cap.set(3, 1280) #width
cap.set(4, 720) #height

#hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1) #0.8 shows 80% sure of detection of a hand

#loop
while True:
    success, img = cap.read()
    hands = detector.findHands(img)

    cv2.imshow('Detectionwindow', img) #name of window with camera opened
    cv2.waitKey(1)