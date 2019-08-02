import cv2
__author__ = "Isa Bostan"
__status__ = "Assignment 3"

maxScaleUp = 100
scaleFactor = 1
scaleType = 0
maxType = 1
windowName = "Resized Image"
trackbarValue = "Scale"
trackbarType = "Type: \n0: Up\n1: Scale Down"

im = cv2.imread("truth.png")
dummy = im.copy()
cv2.namedWindow(windowName,cv2.WINDOW_AUTOSIZE)

#get image size
width,height = im.shape[:2]
print("width,height:",width,height)

#initial is scaling up so I wrote a text for initial
cv2.putText(im, '''Scaling Up is selected''',
            (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
            0.7, (255, 255, 255), 2)

def scaleImage(*args):
    global scaleFactor,scaleType,im
    if scaleFactor == 0:
        scaleFactor=1
    if scaleType == 0:
        scaleFactor = 1 + args[0] / 100.0
        # to check values uncomment print
        #print("scale Factor:",scaleFactor)
        scaledImage = cv2.resize(im,None,fx=scaleFactor,fy=scaleFactor,interpolation=cv2.INTER_LINEAR)
        cv2.imshow(windowName,scaledImage)
    elif scaleType == 1:
        scaleFactor = 1 - args[0] / 100.0
        #to check values uncomment print
        #print("scale Factor:",scaleFactor)
        scaledImage = cv2.resize(im,None,fx=scaleFactor,fy=scaleFactor,interpolation=cv2.INTER_LINEAR)
        cv2.imshow(windowName, scaledImage)

def scaleTypeImage(*args):
    global scaleType, scaleFactor,im
    im = dummy.copy()
    scaleType = args[0]
    scaleFactor = 1+scaleFactor/100.0
    if scaleFactor ==0:
        scaleFactor = 1
    if scaleType == 0:
        cv2.putText(im,'''You select scaling Up..''' ,
              (10,30), cv2.FONT_HERSHEY_SIMPLEX,
              0.7,(255,255,255), 2 )
    elif scaleType == 1:
        cv2.putText(im,'''You select scaling Down..''' ,
              (10,30), cv2.FONT_HERSHEY_SIMPLEX,
              0.7,(255,255,255), 2 )
    cv2.setTrackbarPos(trackbarValue,windowName,0)
    scaledImage = cv2.resize(im, None, fx=scaleFactor,fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)


cv2.createTrackbar(trackbarValue,windowName,scaleFactor,maxScaleUp,scaleImage)
cv2.createTrackbar(trackbarType,windowName,scaleType,maxType,scaleTypeImage)
cv2.imshow(windowName,im)
cv2.waitKey(0)
cv2.destroyAllWindows()