import pygame as p
from Button import Button
p.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BG = (37,151,191)

HEIGHT, WIDTH = 800,800

FONT_STYLE = p.font.SysFont("bahnschrift", 50)
WIN = p.display.set_mode((HEIGHT, WIDTH))
CLOCK = p.time.Clock()

FPS = 60

WIN.fill(BG)

p.display.set_caption("K-Chess")

def draw(button):
        button_message = FONT_STYLE.render(button.name, True, BLACK)
        p.draw.rect(WIN, WHITE, button.rect)
        WIN.blit(button_message, [button.x, button.y])
def play_screen():
        print("Playing")

def main():
        gameOver = False
        play_button = Button("Play", WIDTH/2-50, HEIGHT/2-150, 100, 50)
        play_rect = play_button.rect
        
        while not gameOver:
                for event in p.event.get():
                        if event.type == p.QUIT:
                                gameOver = True
                        if play_button.is_clicked(event):
                                play_screen()
                        if event.type == p.MOUSEMOTION:
                                play_button.hover(event)
                draw(play_button)
                p.display.flip()
                CLOCK.tick(FPS)
main()
p.quit()