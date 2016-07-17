"""
This module is for processing the facial image in color.
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
    Processes the image by reading it in standard format then using fft and hough transform
    image - cv2 image
    """
    data = {} # Dictionary holding processed image data
    color_image = cv2.imread(image) # image read in existing format
    
    blue_image = color_image
    red_image = color_image
    green_image = color_image
    blue_image[:,:,0] = 255
    red_image[0,:,:] = 255
    green_image[:,0,:] = 255
    # Take fft of RGB components of image 
    data["fft_blue"] = cv2.dft(numpy.float32(blue_image), flags=cv2.DFT_COMPLEX_OUTPUT)
    data["fft_red"] = cv2.dft(numpy.float32(red_image), flags=cv2.DFT_COMPLEX_OUTPUT)
    data["fft_green"] = cv2.dft(numpy.float32(green_image), flags=cv2.DFT_COMPLEX_OUTPUT)
    # Apply hough transform to graysacle image after Canny Edge Detection
    # edges and line detections shouldn't change much between RGB

    edges_blue = cv2.Canny(blue_image, _MIN_VAL, _MAX_VAL, apertureSize=_APERTURE_SIZE)
    edges_red = cv2.Canny(red_image, _MIN_VAL, _MAX_VAL, apertureSize=_APERTURE_SIZE)
    edges_green = cv2.Canny(green_image, _MIN_VAL, _MAX_VAL, apertureSize=_APERTURE_SIZE)
    lines_blue = cv2.HoughLines(edges_blue, _RHO, _THETA, _THRESHOLD)
    lines_red = cv2.HoughLines(edges_red, _RHO, _THETA, _THRESHOLD)
    lines_green = cv2.HoughLines(edges_green, _RHO, _THETA, _THRESHOLD)

    data["hough_blue"] = lines_blue
    data["hough_red"] = lines_red
    data["hough_green"] = lines_green

    return data