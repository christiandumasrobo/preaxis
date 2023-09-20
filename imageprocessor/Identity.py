class Identity:
    def __init__(self) -> None:
        self._name = 'Identity'
    
    def __call__(self, image):
        return image