import cv2 as cv

#img = cv.imread('Photos/Cat-2.jpg')
#cv.imshow('Cat-2',img)
#cv.imshow('ResizeImage', resize_image)
#resize_image = rescaleFrame(img)

def rescaleFrame(frame, scale=0.2):
    # Images, Video and Live videos
    width = int(frame.shape[1]* scale)
    height = int(frame.shape[0]* scale)
    dimention  = (width,height)

    return cv.resize(frame, dimention, interpolation=cv.INTER_AREA)

# Regulation Change 
def changeReg(width,height):
    # Live Videos
    capture.set(3,width)
    capture.set(4,height)

# Reading Video file
capture = cv.VideoCapture('Videos/Food.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized= rescaleFrame(frame)

    cv.imshow('vidoe', frame)
    cv.imshow('Video', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break



cv.waitKey(0)