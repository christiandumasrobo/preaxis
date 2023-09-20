import cv2
import scipy.ndimage as nd
import numpy as np
import time

class LaplacianOfGaussians:
    def __init__(self) -> None:
        self._name = 'Laplacian of Gaussians'
    
    def __call__(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        LoG = nd.gaussian_laplace(image, 3)
        threshold = np.absolute(LoG).mean()
        output = np.zeros(LoG.shape, dtype=np.uint8)
        _, max_value, _, _ = cv2.minMaxLoc(LoG)
        LoG_normalized = np.uint8((LoG / max_value + 1) * 127)  # Normalize LoG image

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
        dilated = cv2.dilate(LoG_normalized, kernel)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
        eroded = cv2.erode(LoG_normalized, kernel)

        zero_crossing = cv2.absdiff(dilated, eroded)
        output = (zero_crossing > threshold).astype(np.uint8) * 255

        output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)
        return output