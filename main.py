import cv2
import time
import numpy as np

#import cvzone
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon = 0.5, maxHands=4)

while True:

    ########### find hand and landmark
    success,img= cap.read()
    hands,img = detector.findHands(img)

    ###### getting tip of middle and index finger
    ### check which finger is up
    #### only index finger : moving mode
    ### convert coordinates
    ######### smoothing the value
    ### move the mouse
    ####   clicking mode (index ani middle  mathi cha vane)
    #### index ani middle finger of distance
    #### distance kam cha vane do click
    ## frame rate
### display
    cv2.imshow("image",img)
    k = cv2.waitKey(1)
    if k == ord('a'):

        break




