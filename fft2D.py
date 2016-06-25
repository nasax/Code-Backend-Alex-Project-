"""
Module for FFT functions
"""

import numpy as np

def fourier_transform(image):
    """
    2D fourier transform
    """
    image_fft = np.fft.fft2(image)
    return image_fft

def fourier_shift(image):
    """
    Shifted 2D fourier transform
    """
    image_fft = np.fft.fft2(image)
    image_fft_shift = np.fft.fftshift(image_fft)
    return image_fft_shift
