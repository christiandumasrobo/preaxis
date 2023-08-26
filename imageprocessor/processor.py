import pygame
from Button import Button
from OperationComposer import OperationComposer

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
)
class Processor:
    def __init__(self, screen) -> None:
        self._screen = screen
        self._operationComposer = OperationComposer(screen)
        self._buttons = [
            Button(100, 100, 200, 50, [0, 0, 0], 'edge detection', lambda : self._operationComposer.AddEdgeDetector()),
            Button(100, 200, 200, 50, [0, 0, 0], 'composition', lambda : print('comp')),
            Button(100, 300, 200, 50, [0, 0, 0], 'pop', lambda : self._operationComposer.Pop()),
        ]

        self._drawables = self._buttons
        self._clickables = self._buttons
        self._spinnables = [self._operationComposer]

        self._compositiontype = Button(400, 200, 200, 50, [0, 0, 0], 'or')
        self._drawables.append(self._compositiontype)
    
    def draw(self):
        self._screen.fill([255, 255, 255])
        for drawable in self._drawables:
            drawable.draw(self._screen)

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

screen = pygame.display.set_mode([1500, 800])

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