class Crop:
    def __init__(self) -> None:
        self._name = 'Crop'
    
    def __call__(self, image, x, y, w, h):
        return image[x:x+w, y:y+h]