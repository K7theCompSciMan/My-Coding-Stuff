import pygame as p
import os, time
p.init()

WHITE = (255,255,255)
BLACK = (0,0,0)

WIN_WIDTH, WIN_HEIGHT = 800,800
WIN = p.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

CHARACTER_WIDTH, CHARACTER_HEIGHT = 200,250

BACKGROUND = p.transform.scale(p.image.load(os.path.join("Python Character Animation", "Background.png")), (WIN_WIDTH, WIN_HEIGHT))


FPS = 60

def draw(char1, char2):
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND, (0,0))
    WIN.blit(char1,(100,0)) 
    WIN.blit(char2,(500,0)) 
    p.display.update()

def char1_talk_animation():
    # change character image
    char1 = p.transform.scale(p.image.load(os.path.join('Python Character Animation','Kesavan Talking.png')), (CHARACTER_WIDTH, CHARACTER_HEIGHT))
    return char1

def char2_talk_animation():
    # change character image
    char2 = p.transform.scale(p.image.load(os.path.join('Python Character Animation','Aadarsh Talking.png')), (CHARACTER_WIDTH, CHARACTER_HEIGHT))
    return char2

def main():
    end_animation = False
    clock = p.time.Clock()

    while end_animation != True:
        clock.tick(FPS)
        char1 = p.transform.scale(p.image.load(os.path.join('Python Character Animation','Kesavan Blank.png')),(CHARACTER_WIDTH,CHARACTER_HEIGHT))
        char2 = p.transform.scale(p.image.load(os.path.join('Python Character Animation','Aadarsh Blank.png')), (CHARACTER_WIDTH, CHARACTER_HEIGHT))
        for event in p.event.get():
            if event.type == p.QUIT:
                end_animation = True
        keys_pressed = p.key.get_pressed()

        if keys_pressed[p.K_LCTRL]:
            char1 = char1_talk_animation()
    
        if keys_pressed[p.K_RCTRL]:
            char2 = char2_talk_animation()

        draw(char1, char2)
if __name__ == '__main__':
    main()