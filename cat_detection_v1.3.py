# import the necessary packages
import cv2
import math
import time
import RPi.GPIO as GPIO
 
# Set up the GPIO pins for use
GPIO.setmode(GPIO.BCM)
pin1 = 17
GPIO.setup(pin1, GPIO.OUT)
#pin2 = 27
#pin3 = 22

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    # read image
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #detector = cv2.CascadeClassifier(args["cascade"])
    detector = cv2.CascadeClassifier("./haarcascade_frontalcatface_extended.xml")
 
    rects = detector.detectMultiScale(gray, scaleFactor=1.05,
    minNeighbors=10, minSize=(75, 75))
    cv2.imshow('Cat Faces', img)
    
    print(rects)
    
    # loop over the cat faces and draw a rectangle surrounding each
    for (fX, fY, fW, fH) in rects:
        # Apply rectangle highlight
        rect = cv2.rectangle(img, (fX, fY), (fX + fW, fY + fH), (0, 255, 0), 2)
        print("rect")
        # show appropriate images in windows
        cv2.imshow('Cat Faces', img)
    
        if (fX > 0):
            GPIO.output(pin1, GPIO.HIGH)
    
        k = cv2.waitKey(1)
        if k == 27:
            GPIO.cleanup()
            cap.release()
            cv2.destroyAllWindows()
            break
            
#
