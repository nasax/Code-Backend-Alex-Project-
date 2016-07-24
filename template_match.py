"""
Program isolates image_segments within a larger image
simple idea would be inputting a picture of a hat and 
isolating all the hats. 
"""
import cv2
import numpy as np

def isolate_image_content(image_name,image_segment,threshold)
	"""
	nominal threshold value is 0.8, image_name 
	and image_segment can be passed as file names 
	"""
	img_rgb = cv2.imread(image_name)
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	template = cv2.imread(image_segment,0)
	w, h = template.shape[::-1]

	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	loc = np.where( res >= threshold)
	for pt in zip(*loc[::-1]):
		cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
	return img_rgb
	# cv2.imwrite('res.png',img_rgb)