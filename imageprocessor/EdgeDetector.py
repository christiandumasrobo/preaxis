class EdgeDetector:
    def __init__(self, lower, upper) -> None:
        self._lower = lower
        self._upper = upper
        self._name = 'Edge Detector'
    
    def __call__(self):
        print('edge')