import pygame
from Button import Button
from OperationComposer import OperationComposer
import cv2

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    FULLSCREEN,
)

class Processor:
    def __init__(self, screen) -> None:
        self._screen = screen
        self._operationComposer = OperationComposer(screen)
        self._images = [cv2.imread(f'images/{idx}_color.png') for idx in range(24)]
        self._buttons = [
            Button(100, 100, 200, 50, [0, 0, 0], 'pop', lambda : self._operationComposer.Pop()),
            Button(100, 200, 200, 50, [0, 0, 0], 'composition', lambda : self._operationComposer.RotateComposition()),
            Button(100, 300, 200, 50, [0, 0, 0], 'Canny', lambda : self._operationComposer.AddEdgeDetector()),
            Button(100, 400, 200, 50, [0, 0, 0], 'identity', lambda : self._operationComposer.AddIdentity()),
            Button(100, 500, 200, 50, [0, 0, 0], 'LoG', lambda : self._operationComposer.AddLoG()),
        ]

        self._drawables = self._buttons
        self._clickables = self._buttons
        self._spinnables = [self._operationComposer]

    def draw(self):
        self._screen.fill([255, 255, 255])
        for drawable in self._drawables:
            drawable.draw(self._screen)

        originalImage = pygame.image.frombuffer(self._images[0].tostring(), self._images[0].shape[1::-1], "BGR")
        rect = originalImage.get_rect()
        rect.centerx = 1300
        rect.centery = 300
        self._screen.blit(originalImage, rect)

        processed = self._operationComposer.Compose(self._images)
        #print(processed.shape)
        originalImage = pygame.image.frombuffer(processed.tostring(), processed.shape[1::-1], "BGR")
        rect = originalImage.get_rect()
        rect.centerx = 1300
        rect.centery = 800
        self._screen.blit(originalImage, rect)


    def SpinOnce(self, events):
        self.draw()
        for spinnable in self._spinnables:
            spinnable.SpinOnce()

        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                for clickable in self._clickables:
                    clickable.click(mousepos[0], mousepos[1])


pygame.init()

screen = pygame.display.set_mode([0, 0], FULLSCREEN)
processor = Processor(screen)

running = True
while running:
    last_events = []
    for event in pygame.event.get():
        last_events.append(event)
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    processor.SpinOnce(last_events)

    pygame.display.flip()

pygame.quit()