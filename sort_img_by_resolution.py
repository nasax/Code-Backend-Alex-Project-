"""
This module sorts images into one of three categories 
low resolution < 600 x 400 medium resolution < 1200 x 800 and
high resolution > 1200 x 800
other images size can fall under ODD
can easily be expanded to include more categories
goal of subroutine is simple preprocessing for main program
"""

import cv2

def get_resolution_quality(img_name):
	# Read Image
	img = cv2.imread(img_name)
	# Get Image dimensions
	height, width, channels = img.shape
	if (height <= 600 and width <= 400):
		return 'LOW'
	if(height <= 1200 and width <= 800):
		return 'MED'
	if(height > 1200 and width > 800):
		return 'HIGH'
	else
		return 'ODD'