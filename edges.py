"""
Module for retreiving edges
"""

import cv2

def get_edges(image):
    """
    Retreives potential edges from image using the Canny edge detector.
    image - A numpy array representing the image
    """
    edges = cv2.Canny(image)
    return edges
