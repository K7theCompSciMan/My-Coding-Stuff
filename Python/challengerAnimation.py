import pygame as p
from pygame import mixer
import os, time

p.init()

WHITE = (255,255,255)

EXPLOSION_SOUND = mixer.Sound(os.path.join('Python Animation Images', 'Explosion.wav'))

WIN_WIDTH, WIN_HEIGHT = 400,400
WIN = p.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
p.display.set_caption("Animation")


SHUTTLE = p.image.load(os.path.join('Python Animation Images', 'Cartoon Shuttle.png'))
EXPLOSION = p.image.load(os.path.join('Python Animation Images', 'Cartoon Explosion.png'))





FPS = 60


def draw(shuttle_rect):
    WIN.fill(WHITE)
    WIN.blit(SHUTTLE, (shuttle_rect.x, shuttle_rect.y))

    p.display.update()


def explosion_action(shuttle_rect):
    EXPLOSION_SOUND.play()
    time.sleep(0.5)
    WIN.blit(EXPLOSION, (shuttle_rect.x-EXPLOSION.get_width()//4, shuttle_rect.y))
    p.display.update()
    time.sleep(2)
    return 'end'


def shuttle_movement(shuttle_rect):
    shuttle_rect.y -=1
    if shuttle_rect.y <=40:
        return explosion_action(shuttle_rect)


def main():
    end = False
    clock = p.time.Clock()
    shuttle_rect = p.Rect(200-SHUTTLE.get_width()//2, 200, SHUTTLE.get_width(), SHUTTLE.get_height())

    while end != True:
        clock.tick(FPS)
        for event in p.event.get():
            if event.type == p.QUIT:
                end = True


        finish = shuttle_movement(shuttle_rect)
        
        if finish == 'end':
            end = True

        draw(shuttle_rect)


if __name__ == "__main__":
    main()