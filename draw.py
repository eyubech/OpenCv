import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#draw rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)


#draw circle
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

#draw line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('Line', blank)


cv.waitKey(0)