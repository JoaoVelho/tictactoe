import cv2
import numpy as np

def createPattern(path):
  img = cv2.resize(cv2.imread(path), (500, 500))
  imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
  lower = np.array([0,23,0])
  upper = np.array([179,255,255])
  mask = cv2.inRange(imgHSV,lower,upper)
  imgResult = cv2.bitwise_and(img,img,mask=mask)
  imgGray = cv2.cvtColor(imgResult, cv2.COLOR_BGR2GRAY)
  imgCanny = cv2.Canny(imgGray, 200, 50)

  return imgCanny

def createPatternItem(path):
  img = cv2.resize(cv2.imread(path), (500, 500))
  imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  imgCanny = cv2.Canny(imgGray, 200, 50)

  return imgCanny

def getContours(img, patternX, patternO):
  contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cntX, _ = cv2.findContours(patternX, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cntO, _ = cv2.findContours(patternO, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  for cnt in contours:
    area = cv2.contourArea(cnt)
    print(area)
    if area < 20000:
      cv2.drawContours(imgContour, cnt, -1, (0, 0, 255), 3)
      peri = cv2.arcLength(cnt, False)
      approx = cv2.approxPolyDP(cnt, 0.01 * peri, False)
      
      resX = cv2.matchShapes(cntX[0], cnt, 3, 0.0)
      # print(resX)
      resO = cv2.matchShapes(cntO[0], cnt, 3, 0.0)
      # print(resO)

      x, y, w, h = cv2.boundingRect(approx)
      if resX >= 0 and resX <= 0.3:
        shape = 'X'
        cv2.rectangle(imgContour, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(
          imgContour, 
          shape, 
          (x + (w // 2) - 10, y - 10), 
          cv2.FONT_HERSHEY_COMPLEX, 
          1, 
          (0, 155, 0), 
          2
        )
      elif resO >= 0 and resO <= 0.3:
        shape = 'O'
        cv2.rectangle(imgContour, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(
          imgContour, 
          shape, 
          (x + (w // 2) - 10, y - 10), 
          cv2.FONT_HERSHEY_COMPLEX, 
          1, 
          (0, 155, 0), 
          2
        )
  
Xpath = 'ex1.png'
Opath = 'circle.png'
path = 'boardred2.jpg'
img = createPattern(path)
imgContour = cv2.resize(cv2.imread(path), (500, 500))
cv2.imshow('Original', imgContour)
cv2.imshow('Canny', img)

patternX = createPatternItem(Xpath)
patternO = createPatternItem(Opath)

getContours(img, patternX, patternO)

cv2.imshow('Contour', imgContour)

# def empty(a):
#   pass

# path = 'boardred2.jpg'
# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars",640,240)
# cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
# cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
# cv2.createTrackbar("Sat Min","TrackBars",8,255,empty)
# cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
# cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
# cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

# while True:
#   img = cv2.resize(cv2.imread(path), (500, 500))
#   imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#   h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
#   h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
#   s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
#   s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
#   v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
#   v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
#   print(h_min,h_max,s_min,s_max,v_min,v_max)
#   lower = np.array([h_min,s_min,v_min])
#   upper = np.array([h_max,s_max,v_max])
#   mask = cv2.inRange(imgHSV,lower,upper)
#   imgResult = cv2.bitwise_and(img,img,mask=mask)

#   cv2.imshow("Original",img)
#   cv2.imshow("HSV",imgHSV)
#   cv2.imshow("Mask", mask)
#   cv2.imshow("Result", imgResult)

#   cv2.waitKey(1)
cv2.waitKey(0)