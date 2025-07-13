import numpy as np
import cv2

def get_limits(color):
    c = np.uint8([[color]]) # here inserting the bgr values which you want to conver to hsv, to convert first we need to convert so uint8
    hsvC = cv2.cvtColor(c,cv2.COLOR_BGR2HSV)
    
    lowerLimit = hsvC[0][0][0] - 10,100,100
    upperLimit = hsvC[0][0][0] +  10,255,255
    
    lowerLimit = np.array(lowerLimit,dtype=np.uint8)
    upperLimit = np.array(upperLimit,dtype=np.uint8)
    
    return lowerLimit,upperLimit