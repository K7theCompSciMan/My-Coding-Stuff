import pygame as p


class Button:
    def __init__(self, name, x, y, width, height, base_color, hover_color) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = p.Rect(x, y, width, height)
        self.color = base_color
        self.base_color = base_color
        self.hover_color = hover_color

    def is_clicked(self, event):
        if event.type == p.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True

    def hover(self, collide=False):
        if collide:
            self.color = self.hover_color
            p.mouse.set_cursor(*p.cursors.diamond)
        else:
            self.color = self.base_color
            p.mouse.set_cursor(*p.cursors.arrow)

    def draw(self, window, font_style, text_color):
        message = font_style.render(self.name, True, text_color)
        p.draw.rect(window, self.color, self.rect)
        window.blit(message, [self.rect.centerx - message.get_width() //
                    2, self.rect.centery - message.get_height()//2])
