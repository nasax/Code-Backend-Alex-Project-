"""
This module scans an image for faces 
and then saves said faces as new images. 
"""

import numpy as np
import cv2

def get_faces(img_name):
	pass
	# Facial recognition training file 
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

	"""
	Read image
	turn to graysclae 
	save pictures of 
	faces numbered 1 forward
	""" 
	img = cv2.imread(img_name)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.2, 5)
	number = 0
	# Iterate through all faces 
	for (x,y,w,h) in faces:
    	number +=1
    	crop_img = img[y:y+h, x:x+w]
    	name = img_name + '_face_' + str(number) + '.jpg'
    	cv2.imwrite(name,crop_img)
 # This really should return an array of images instead of writing them
 # Code Should be refactored for integration with larger program
