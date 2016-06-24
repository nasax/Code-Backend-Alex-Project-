import cv2
import numpy as np
# Gets image edges
def get_edges(img):
    edgs = cv2.Canny(img)
    return edgs