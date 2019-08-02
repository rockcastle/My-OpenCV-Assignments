#! /usr/bin/python

__author__ = "Isa Bostan"

__email__ = "isabostan@gmail.com"
__status__ = "Assignment"


import cv2
import numpy as np

source = cv2.imread("sample.jpg")
cropping = False
cv2.namedWindow("Window")
x1, y1, x2, y2 = 0, 0, 0, 0
def mouse_cropping(event, x, y, flags, userdata):
    try:
        global x1, y1, x2, y2, cropping
        if event == cv2.EVENT_LBUTTONDOWN:
            x1, y1, x2, y2 = x, y, x, y
            cropping = True
            cv2.circle(source, (x1,y1), 1, (255, 0, 255), 2, cv2.LINE_AA)

        elif event == cv2.EVENT_MOUSEMOVE:
            if cropping == True:
                x2,y2 = x,y
        elif event == cv2.EVENT_LBUTTONUP:
            x2,y2 = x,y
            cropping = False
            points = [(x1,y1),(x2,y2)]
            cv2.rectangle(source,points[0],points[1],(255,0,255),thickness=3,lineType=cv2.LINE_AA)
            if len(points)==2:
                print("cropping...")
                crop = source[points[0][1]:points[1][1],points[0][0]:points[1][0]]
                cv2.imwrite("face.png",crop)
                cv2.imshow("Cropped", crop)

    except Exception as ex:
        print("Exception:",ex)


try:
    cv2.setMouseCallback("Window", mouse_cropping)
    k = 0
    # loop until escape character is pressed
    while k!=27:

        dummy = source.copy()
        cv2.putText(source,'''Choose center, and drag, 
                      Press ESC to exit and c to clear''' ,
              (10,30), cv2.FONT_HERSHEY_SIMPLEX,
              0.7,(255,255,255), 2 )


        if not cropping:
            cv2.imshow("Window", source)
        elif cropping:
            cv2.rectangle(dummy, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.imshow("Window", dummy)
        k = cv2.waitKey(20) & 0xFF

    cv2.destroyAllWindows()
except Exception as ex:
    print("Exception",ex)


