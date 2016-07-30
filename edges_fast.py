"""
Alternate Implementation of get edges module
decidely faster than previous implementation
see opencv documentation for more details
"""

import cv2
import numpy as np

def get_edges(img):
	
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,50,150,apertureSize = 3)
	
	# Thresholds maybe set for changing accuracy 
	# and execution time
	minLineLength = 100
	maxLineGap = 10
	
	lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
	return lines 