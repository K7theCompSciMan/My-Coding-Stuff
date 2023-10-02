import pygame as p
import math
from Button import Button
from Board import Board
p.init()

BOARD = Board(100, 100)

BOARD_STATES = [BOARD.piece_board]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BG = (37, 151, 191)
BASE_COLOR = (32, 104, 185)
HOVER_COLOR = (0, 255, 0)

HEIGHT, WIDTH = 800, 800

FONT_STYLE = p.font.SysFont("bahnschrift", 25)
WIN = p.display.set_mode((HEIGHT, WIDTH))
CLOCK = p.time.Clock()

FPS = 60


p.display.set_caption("K-Chess")

# ---------------- SETTINGS ---------------- #


def settings_screen(back_button):
    WIN.fill(BG)
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
            if back_button.is_clicked(event):
                main()
            if event.type == p.MOUSEMOTION:
                if back_button.rect.collidepoint(event.pos):
                    back_button.hover(True)
                    back_button.draw(WIN, FONT_STYLE, WHITE)
                else:
                    back_button.hover()

                    back_button.draw(WIN, FONT_STYLE, WHITE)

        back_button.draw(WIN, FONT_STYLE, WHITE)
        p.display.flip()

# ---------------- ABOUT ---------------- #


def about_screen(back_button):
    WIN.fill(BG)
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
            if back_button.is_clicked(event):
                main()
            if event.type == p.MOUSEMOTION:
                if back_button.rect.collidepoint(event.pos):
                    back_button.hover(True)
                    back_button.draw(WIN, FONT_STYLE, WHITE)
                else:
                    back_button.hover()

                    back_button.draw(WIN, FONT_STYLE, WHITE)

        back_button.draw(WIN, FONT_STYLE, WHITE)
        p.display.flip()


# ---------------- PLAYING ---------------- #
def local():
    WIN.fill(BG)

    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                return "quit"

            for rank in BOARD.piece_board:
                for piece in rank:
                    if (piece.image != None):
                        if (piece.is_clicked(event)):
                            piece.display_legal_moves(BOARD, WIN)
                            turn_over = False
                            piece.selected = True
                            p.display.flip()
                            while not turn_over:
                                for event in p.event.get():
                                    if event.type == p.QUIT:
                                        p.quit()
                                        return "quit"
                                    if event.type == p.MOUSEBUTTONUP:
                                        turn_over = True
                                        piece.selected = False
                            print(math.floor(
                                event.pos[1]/100), math.floor(event.pos[0]/100))
                            if (piece.is_legal_move(math.floor(event.pos[1]/100), math.floor(event.pos[0]/100), BOARD)):
                                piece.move_to(math.floor(
                                    event.pos[1]/100), math.floor(event.pos[0]/100), BOARD)
                                BOARD.white_to_move = not BOARD.white_to_move
                                BOARD_STATES.append(BOARD.piece_board)
                            else:
                                piece.move_to(
                                    piece.original_location[0], piece.original_location[1], BOARD)
                            BOARD.draw(WIN)

        BOARD.draw(WIN)
        p.display.flip()


def ai():
    WIN.fill(BG)
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                return "quit"
        BOARD.draw(WIN)
        p.display.flip()


def play_screen(back_button):

    WIN.fill(BG)
    local_button = Button("Local Multiplayer", WIDTH/2 -
                          100, HEIGHT/2-150, 200, 60, BASE_COLOR, HOVER_COLOR)
    ai_button = Button("AI", WIDTH/2-75, HEIGHT/2-50,
                       150, 60, BASE_COLOR, HOVER_COLOR)
    while True:

        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                return "quit"

            if back_button.is_clicked(event):
                main()

            if local_button.is_clicked(event):
                if (local() == "quit"):
                    return ("quit")

            elif ai_button.is_clicked(event):
                ai()

            if event.type == p.MOUSEMOTION:
                if back_button.rect.collidepoint(event.pos):
                    back_button.hover(True)
                    back_button.draw(WIN, FONT_STYLE, WHITE)
                elif local_button.rect.collidepoint(event.pos):
                    local_button.hover(True)
                    local_button.draw(WIN, FONT_STYLE, WHITE)
                elif ai_button.rect.collidepoint(event.pos):
                    ai_button.hover(True)
                    ai_button.draw(WIN, FONT_STYLE, WHITE)
                else:
                    back_button.hover()
                    local_button.hover()
                    ai_button.hover()

        local_button.draw(WIN, FONT_STYLE, WHITE)
        ai_button.draw(WIN, FONT_STYLE, WHITE)
        back_button.draw(WIN, FONT_STYLE, WHITE)
        p.display.flip()


# ---------------- MAIN MENU ---------------- #

def main():

    play_button = Button("Play", WIDTH/2-75, HEIGHT/2-150,
                         150, 60, BASE_COLOR, HOVER_COLOR)
    settings_button = Button("Settings", WIDTH/2-75,
                             HEIGHT/2-50, 150, 60, BASE_COLOR, HOVER_COLOR)
    about_button = Button("About", WIDTH/2-75, HEIGHT/2+50,
                          150, 60, BASE_COLOR, HOVER_COLOR)
    back_button = Button("Back", WIDTH/2-75, HEIGHT/2+100,
                         150, 60, BASE_COLOR, HOVER_COLOR)
    WIN.fill(BG)

    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                return

            if play_button.is_clicked(event):
                if play_screen(back_button) == "quit":
                    return

            if settings_button.is_clicked(event):
                settings_screen(back_button)

            if about_button.is_clicked(event):
                about_screen(back_button)

            if event.type == p.MOUSEMOTION:
                if play_button.rect.collidepoint(event.pos):
                    play_button.hover(True)
                    play_button.draw(WIN, FONT_STYLE, WHITE)
                elif settings_button.rect.collidepoint(event.pos):
                    settings_button.hover(True)
                    settings_button.draw(WIN, FONT_STYLE, WHITE)
                elif about_button.rect.collidepoint(event.pos):
                    about_button.hover(True)
                    about_button.draw(WIN, FONT_STYLE, WHITE)
                else:
                    play_button.hover()
                    settings_button.hover()
                    about_button.hover()

                    play_button.draw(WIN, FONT_STYLE, WHITE)
                    settings_button.draw(WIN, FONT_STYLE, WHITE)
                    about_button.draw(WIN, FONT_STYLE, WHITE)

        play_button.draw(WIN, FONT_STYLE, WHITE)
        settings_button.draw(WIN, FONT_STYLE, WHITE)
        about_button.draw(WIN, FONT_STYLE, WHITE)
        p.display.flip()
        CLOCK.tick(FPS)


main()
