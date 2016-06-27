"""
This module is for gathering information about the image so that we can make
informed decisions during the identification process.
"""


def preprocess(image):
    """
    Process information about the image and return it in a dictionary.
    image - A numpy array representing the image
    """
    image_info = {
        "is_light": _is_light(image)
    }
    return image_info

def _is_light(image):
    """
    Detects if the image is light or dark based on average pixel values.
    Returns a boolean
    image - A numpy array representing the image
    """
    return image.mean() > 127
