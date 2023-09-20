from EdgeDetector import EdgeDetector
from Identity import Identity
from LaplacianOfGaussians import LaplacianOfGaussians
from Button import Button
import cv2
import numpy as np
from copy import deepcopy

class OperationComposer:
    def __init__(self, screen) -> None:
        self._operations = []
        self._compositions = ['first', 'or', 'and', 'or(xor)']
        self._compositionIndex = 0
        self._screen = screen
        self._cropRegion = [0, 0, 0, 0]
        self._lastOperations = []
        self._cachedResult = None
    
    def SpinOnce(self):
        self.draw()
    
    def ComposeFunc(self, method):
        compMap = {
            'or': cv2.bitwise_or,
            'and': cv2.bitwise_and,
            'or(xor)': lambda x, y : cv2.bitwise_or(x, cv2.bitwise_xor(x, y)),
        }
        return compMap.get(method, lambda x, y: y)

    def Compose(self, images):
        if self._cachedResult is not None:
            if len(self._operations) == len(self._lastOperations):
                return self._cachedResult

        self._lastOperations = deepcopy(self._operations)

        if self._compositions[self._compositionIndex] == 'first':
            images = [images[0]]
        result = np.zeros(cv2.cvtColor(images[0], cv2.COLOR_BGR2GRAY).shape, dtype=np.uint8)
        for operation in self._operations:
            for image in images:
                opResult = cv2.cvtColor(operation(image), cv2.COLOR_BGR2GRAY)
                result = self.ComposeFunc(self._compositions[self._compositionIndex])(result, opResult)
        
        self._cachedResult = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)
        return self._cachedResult

    def draw(self):
        Button(400, 200, 200, 50, [0, 0, 0], self._compositions[self._compositionIndex]).draw(self._screen)
        for idx, operation in enumerate(self._operations):
            Button(650, 200 + 100 * idx, 200, 50, [0, 0, 0], operation._name).draw(self._screen)

    def AddEdgeDetector(self):
        self._operations.append(EdgeDetector(114, 255))

    def SetCrop(self, topLeftX, topLeftY, bottomRightX, bottomRightY):
        self.cropRegion = [topLeftX, topLeftY, bottomRightX, bottomRightY]

    def AddLoG(self):
        self._operations.append(LaplacianOfGaussians())

    def AddIdentity(self):
        self._operations.append(Identity())

    def RotateComposition(self):
        self._compositionIndex = (self._compositionIndex + 1) % len(self._compositions)
    
    def Pop(self):
        if not self._operations:
            return
        del self._operations[-1]