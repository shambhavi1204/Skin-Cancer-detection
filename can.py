import os
import cv2
import numpy as np



def hair_remove(image):
    # converts image to grayScale
    grayScale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # kernel for morphologyEx
    kernel = cv2.getStructuringElement(1,(5,5))
    # apply MORPH_BLACKHAT to grayScale image
    blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
    # apply thresholding to blackhat
    _,threshold = cv2.threshold(blackhat,20,255,cv2.THRESH_BINARY)
    # inpaint with original image and threshold image
    final_image = cv2.inpaint(image,threshold,5,cv2.INPAINT_TELEA)
    
    return final_image


image = cv2.imread(r"D:\dataset\bhot.jpg")

image_resize = cv2.resize(image,(224,224))
final_image = hair_remove(image_resize)
#cv2.imwrite(os.path.join(base,target),np.asarray(final_image))

cv2.imshow('fnal',final_image)
cv2.imshow('real',image)    
