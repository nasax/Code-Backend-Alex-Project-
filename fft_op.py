import cv2 
import numpy as np
# Basic FFT module 
# offers 2D fourier transform
# and shifted version
def fourier_transform(img):
    IMG = np.fft.fft2(img)
    return IMG
def fourier_shift(img):
    IMG = np.fft.fft2(img)
    fshift = np.fft.fftshift(IMG)
    return fshift