"""
Resizes an image to the selected paramters
Scales Ratio
For parameters that keep the same ratio effectively 
performs compression 
"""
# Imports 
import numpy as np
import cv2
# Resizes image according to selected parameters
# if image contains the same x,y dimensions then 
# the same image is returned 
def resize(img,x_dim,y_dim):
	img_resized = cv2.resize(img,(x_dim, y_dim), interpolation = cv2.INTER_CUBIC)
	return img_resized 