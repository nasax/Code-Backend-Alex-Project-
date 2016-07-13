"""
This module is for processing the facial image in grayscale.
"""
import cv2
import numpy

# Canny edge detection constants
_MIN_VAL = 50
_MAX_VAL = 150
_APERTURE_SIZE = 3

# Hough transform constants
_RHO = 1
_THETA = numpy.pi / 180
_THRESHOLD = 200

def process_image(image):
    """
    Processes the image by converting it into grayscale then using fft and hough transform
    image - cv2 image
    """
    data = {} # Dictionary holding processed image data
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # image converted to grayscale

    # Take fft of grayscale image
    data["fft"] = cv2.dft(numpy.float32(gray_image), flags=cv2.DFT_COMPLEX_OUTPUT)

    # Apply hough transform to graysacle image after Canny Edge Detection
    edges = cv2.Canny(gray_image, _MIN_VAL, _MAX_VAL, apertureSize=_APERTURE_SIZE)
    lines = cv2.HoughLines(edges, _RHO, _THETA, _THRESHOLD)

    data["hough"] = lines

    return data
