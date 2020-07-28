import cv2
import numpy as np

def createPattern(path):
  img = cv2.resize(cv2.imread(path), (500, 500))
  imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
  imgCanny = cv2.Canny(imgBlur, 50, 50)

  return imgCanny

def getContours(img, patternX, patternO):
  contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  cntX, hierarchyX = cv2.findContours(patternX, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  cntO, hierarchyO = cv2.findContours(patternO, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  print(len(contours))
  for cnt in contours:
    area = cv2.contourArea(cnt)
    # print(area)
    cv2.drawContours(imgContour, cnt, -1, (0, 0, 255), 3)
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.01 * peri, True)
    
    resX = cv2.matchShapes(cntX[0], cnt, 3, 0.0)
    print(resX)
    resO = cv2.matchShapes(cntO[0], cnt, 3, 0.0)
    print(resO)

    x, y, w, h = cv2.boundingRect(approx)
    if resX >= 0 and resX <= 0.3:
      shape = 'Ex'
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
      shape = 'Circle'
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

  
X = 'ex.png'
O = 'circle.png'
path = 'board.png'
img = createPattern(path)
imgContour = cv2.resize(cv2.imread(path), (500, 500))

patternX = createPattern(X)
patternO = createPattern(O)

getContours(img, patternX, patternO)

cv2.imshow('Original', img)
# cv2.imshow('Gray', imgGray)
# cv2.imshow('Blur', imgBlur)
# cv2.imshow('Canny', imgCanny)
cv2.imshow('Contour', imgContour)
cv2.waitKey(0)