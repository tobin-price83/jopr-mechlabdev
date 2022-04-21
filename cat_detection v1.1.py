# import the necessary packages
import argparse
import cv2
import numpy as np
import math
import time
import RPI.GPIO as GPIO
 
# Set up the GPIO pins for use
GPIO.setmode(GPIO.BOARD)
led1 = 17
led2 = 27
led3 = 22

# construct the argument parse and parse the arguments
#
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#   help="path to the input image")
# ap.add_argument("-c", "--cascade",
#   default="haarcascade_frontalcatface.xml",
#   help="path to cat detector haar cascade")
# args = vars(ap.parse_args())

cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    # read image
    ret, img = cap.read()

    # get cat image from the rectangle sub window on the screen
#    cv2.rectangle(img, (300,300), (100,100), (0,255,0),0)
#    crop_img = img[100:300, 100:300]

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #detector = cv2.CascadeClassifier(args["cascade"])
    detector = cv2.CascadeClassifier("./haarcascade_frontalcatface_extended.xml")
 
    rects = detector.detectMultiScale(gray, scaleFactor=1.3,
    minNeighbors=10, minSize=(75, 75))

    # loop over the cat faces and draw a rectangle surrounding each
    for (i, (x, y, w, h)) in enumerate(rects):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img, "Cat #{}".format(i + 1), (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
        if x > 0:
            print("Cat detected!")
        else:
            print("NO cats detected.")

    # show appropriate images in windows
    cv2.imshow("Cat Faces", img)
    
    #k = cv2.waitKey(10)
    cv2.waitKey(0)
    #if k == 27:
    GPIO.cleanup()
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()
    #break



#///////////////////////////////////////////////////
# load the input image and convert it to grayscale
#image = cv2.imread(args["image"])



# load the cat detector Haar cascade, then detect cat faces
# in the input image
#detector = cv2.CascadeClassifier(args["cascade"])





# show the detected cat faces
# cv2.imshow("Cat Faces", image)
# cv2.waitKey(0)
