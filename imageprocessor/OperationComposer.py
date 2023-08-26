from EdgeDetector import EdgeDetector
from Button import Button

class OperationComposer:
    def __init__(self, screen) -> None:
        self._operations = []
        self._screen = screen
    
    def SpinOnce(self):
        self.draw()

    def draw(self):
        for idx, operation in enumerate(self._operations):
            Button(650, 200 + 100 * idx, 200, 50, [0, 0, 0], operation._name).draw(self._screen)

    def AddEdgeDetector(self):
        self._operations.append(EdgeDetector(255/3, 255))
    
    def Pop(self):
        if not self._operations:
            return
        del self._operations[-1]