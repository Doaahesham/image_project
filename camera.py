import cv2 as cv
import numpy as np
import modules as m
import time


def camera_concentration(frame):
    
    # Variables
    COUNTER = 0
    TOTAL_BLINKS = 0
    CLOSED_EYES_FRAME = 3
    POS_COUNTER = 0
    left, right, center = 0 , 0, 0
    videoPath = "Video/Your Eyes Independently_Trim5.mp4"
    # variables for frame rate.
    FRAME_COUNTER = 0
    START_TIME = time.time()
    FPS = 0

    # creating camera object
    # camera = cv.VideoCapture(0)
    

    # Define the codec and create VideoWriter object
    # fourcc = cv.VideoWriter_fourcc(*'XVID')
    # f = camera.get(cv.CAP_PROP_FPS)
    # width = camera.get(cv.CAP_PROP_FRAME_WIDTH)
    # height = camera.get(cv.CAP_PROP_FRAME_HEIGHT)
    # fileName = videoPath.split('/')[1]
    # name = fileName.split('.')[0]


    FRAME_COUNTER = 1
    # getting frame from camera


    # converting frame into Gry image.
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    height, width = grayFrame.shape
    # calling the face detector funciton
    image, face = m.faceDetector(frame, grayFrame)
    if face is not None:

        # calling landmarks detector funciton.
        image, PointList = m.landmarkDetector(frame, grayFrame, face)

        RightEyePoint = PointList[36:42]
        LeftEyePoint = PointList[42:48]
        leftRatio, topMid, bottomMid = m.blinkDetector(LeftEyePoint)
        rightRatio, rTop, rBottom = m.blinkDetector(RightEyePoint)


        blinkRatio = (leftRatio + rightRatio)/2


        if blinkRatio > 4:
            COUNTER += 1

        else:
            if COUNTER > CLOSED_EYES_FRAME:
                TOTAL_BLINKS += 1
                COUNTER = 0

        mask, pos, color = m.EyeTracking(frame, grayFrame, RightEyePoint)
        maskleft, leftPos, leftColor = m.EyeTracking(
            frame, grayFrame, LeftEyePoint)
        
        #count how many user looks left or right
        if(pos == "Center"):
            POS_COUNTER += 1
        

    SECONDS = time.time() - START_TIME
    # calculating the frame rate
    FPS = FRAME_COUNTER/SECONDS

    # defining the key to Quite the Loop


    #output concentration percentage
    conc_percentage = (POS_COUNTER/FRAME_COUNTER)*100
   
    return round(conc_percentage,2)