import cv2

class EdgeDetector:
    def __init__(self, lower, upper) -> None:
        self._lower = lower
        self._upper = upper
        self._name = 'Edge Detector'
    
    def __call__(self, image):
        image = cv2.GaussianBlur(image, (3, 3), 0)
        image = cv2.Canny(image, self._lower, self._upper)
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        return image