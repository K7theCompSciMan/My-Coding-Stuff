import pygame as p
class Button:
        def __init__(self, name, x, y, width, height) -> None:
                self.name = name
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.rect = p.Rect(x, y, width, height)
        def is_clicked(self, event):
                if event.type == p.MOUSEBUTTONDOWN:
                        if self.rect.collidepoint(event.pos):
                                return True
        def hover(self, event):
                if self.rect.collidepoint(event.pos):
                        self.rect = p.Rect(self.x-5, self.y-5, self.width+10, self.height+10)
                else:
                        self.rect = p.Rect(self.x, self.y, self.width, self.height)