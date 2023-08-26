import pygame

from resource_path import resource_path

class Button:
    def __init__(self, x, y, w, h, color, text, callback=None, visible=True):
        self.w = w
        self.h = h
        self.surface = pygame.Surface((w, h))
        self.text = text

        self.old_x = x
        self.old_y = y

        self.x = x
        self.y = y
        self.surface.fill(color)
        self.font = pygame.font.Font(resource_path("pixel.ttf"), int(h/2))
        text_color = (255-color[0], 255-color[1], 255-color[2])

        self.t_surf = self.font.render(text, True, text_color)

        self.callback = callback
        # this is sadly necessary to make buttons unclickable even when not drawn
        self.visible = visible
    
    def draw(self, screen, x=None, y=None):
        if self.visible == False:
            return
        if x == None:
            self.x = self.old_x
            x = self.x
        else:
            self.x = x
        if y == None:
            self.y = self.old_y
            y = self.y
        else:
            self.y = y
        screen.blit(self.surface, self.surface.get_rect().move(x, y))
        text_rect = self.t_surf.get_rect().move(x + (self.w - self.t_surf.get_width())/2, y + (self.h - self.t_surf.get_height())/2)
        screen.blit(self.t_surf, text_rect)

    def click(self, x, y):
        if self.visible == False or self.callback == None:
            return
        if x > self.x and x < self.x + self.surface.get_width() and y > self.y and y < self.y + self.surface.get_height():
            self.callback()