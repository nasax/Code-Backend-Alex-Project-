"""
This module is for processing the facial image
"""
import cv2
import numpy

# Utility constants
_CHANNELS_TO_PROCESS = ["blue", "green", "red", "gray"]

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
    Processes the image by using fft and hough transform in grayscale and its three color channels
    image - cv2 image
    """

    data = {} # Dictionary holding processed image data

    image_blue, image_green, image_red = cv2.split(image) # split image into color channels
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # image converted to grayscale

    # assign channel images to array in same order as _CHANNELS_TO_PROCESS
    image_channels = [image_blue, image_green, image_red, image_gray]

    # process each color channel
    for i, channel in enumerate(_CHANNELS_TO_PROCESS):
        data[channel] = _process_image(image_channels[i])

    return data

def _process_image(image):
    """
    Processes the image by using fft and hough transform
    image - cv2 image
    """
    data = {} # Dictionary holding processed image data

    # Take fft of image
    data["fft"] = cv2.dft(numpy.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)

    # Apply hough transform to image after Canny Edge Detection
    edges = cv2.Canny(image, _MIN_VAL, _MAX_VAL, apertureSize=_APERTURE_SIZE)
    lines = cv2.HoughLines(edges, _RHO, _THETA, _THRESHOLD)

    data["hough"] = lines

    return data
