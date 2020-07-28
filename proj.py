import cv2
import numpy as np

def createPattern(path):
  img = cv2.resize(cv2.imread(path), (500, 500))
  imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  imgCanny = cv2.Canny(imgGray, 50, 50)

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
path = 'board.png'
img = createPattern(path)
imgContour = cv2.resize(cv2.imread(path), (500, 500))
cv2.imshow('Original', imgContour)

patternX = createPattern(Xpath)
patternO = createPattern(Opath)

getContours(img, patternX, patternO)

cv2.imshow('Contour', imgContour)
cv2.waitKey(0)