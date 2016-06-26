"""
Resizes an image to the selected paramters
Scales Ratio
For parameters that keep the same ratio effectively
performs compression
"""

import cv2

_DEFAULT_WIDTH = 720
_DEFAULT_HEIGHT = 1280

def resize(image, width=_DEFAULT_WIDTH, height=_DEFAULT_HEIGHT):
    """
	Resizes image to given dimensions, width, height, which should be positive integers
    """
    image_resized = cv2.resize(image, (width, height), interpolation=cv2.INTER_CUBIC)
    return image_resized
