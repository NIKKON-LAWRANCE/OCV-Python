import cv2 as cv
import numpy as np
from numpy.core.function_base import linspace

blank = np.zeros((500,500,3),dtype='uint8')
#cv.imshow('Blank',blank)

# 1. paint the image a cartain color 
# blank[200:300,300:400]=140,100,155
# cv.imshow('Red',blank)


# 2. Draw a Reactangle
cv.rectangle(blank,(0,0), (250,500), (0,247,255), thickness=cv.FILLED)
#cv.imshow('Rectangle', blank) 

# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),50,(255,247,0),thickness=-1)
#cv.imshow('Circle',blank)

# 4. Draw a line
cv.line(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2),(255,255,255),thickness=4)
#cv.imshow('Line',blank)

# 5. Write Text
cv.putText(blank,'Hello Nikkon',(255,100),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('Text',blank)

cv.waitKey(0)