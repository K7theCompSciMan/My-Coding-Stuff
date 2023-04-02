import pygame as p
import random, time

p.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

WIN_HEIGHT, WIN_WIDTH = 800,800

WIN = p.display.set_mode((WIN_HEIGHT, WIN_WIDTH))

p.display.set_caption("Pong Game")

FONT_STYLE = p.font.SysFont("bahnschrift", 50)

FPS = 60

PLAYER_WIDTH, PLAYER_HEIGHT = 10,60

PLAYER_VEL = 5


BALL_VEL = 15
BALL_WIDTH,BALL_HEIGHT = 10,10

def message(msg, color):
    WIN.fill(WHITE)
    mesg = FONT_STYLE.render(msg, True, color)
    mesg_width = mesg.get_width()
    WIN.blit(mesg, [(WIN_WIDTH//2) - (mesg_width//2), WIN_HEIGHT//2])
    p.display.update()

def display_score(player_1_score, player_2_score):
    p1score_message = FONT_STYLE.render(str(player_1_score), True, WHITE)
    p2score_message = FONT_STYLE.render(str(player_2_score), True, WHITE)
    WIN.blit(p1score_message, [WIN_WIDTH//4, WIN_HEIGHT//4])
    WIN.blit(p2score_message, [WIN_WIDTH//4*3, WIN_HEIGHT//4])

def reset_ball_location(ball):
    ball.x = WIN_WIDTH//2
    ball.y = WIN_HEIGHT//2

def ball_movement(ball, ball_move_left, ball_move_up, horz, vert):
    if ball_move_left == True:
        ball.x -= horz
    else:
        ball.x += horz
    if ball_move_up == True:
        ball.y -= vert
    else:
        ball.y += vert

def draw(player_1, player_2, ball, player_1_score, player_2_score):
    WIN.fill(BLACK)
    display_score(player_1_score, player_2_score)
    p.draw.rect(WIN, WHITE, ball)
    p.draw.rect(WIN, WHITE, player_1)
    p.draw.rect(WIN, WHITE, player_2)
    p.display.update()

def check_ball_location(ball, player_1_score, player_2_score):
    if ball.x <= 0 :
        reset_ball_location(ball)
        return player_1_score , player_2_score +1
    if ball.x >= WIN_WIDTH:
        reset_ball_location(ball)
        return player_1_score +1, player_2_score
    else:
        return player_1_score, player_2_score
    
def check_collisions(player_1, player_2, ball, ball_move_left, ball_move_up):
    if player_1.colliderect(ball) or player_2.colliderect(ball):
       temp = not ball_move_left
    else:
        temp = ball_move_left
    if ball.y <=0 or ball.y >= WIN_HEIGHT:
        vert_temp = not ball_move_up
    else:
        vert_temp = ball_move_up
    return temp, vert_temp

def main(): 
    game_over = False
    clock = p.time.Clock()
    player_1 = p.Rect(10,(WIN_HEIGHT//2)-(PLAYER_HEIGHT//2), PLAYER_WIDTH, PLAYER_HEIGHT)
    player_2 = p.Rect(780,(WIN_HEIGHT//2)-(PLAYER_HEIGHT//2), PLAYER_WIDTH, PLAYER_HEIGHT)
    ball = p.Rect(WIN_WIDTH//2, WIN_HEIGHT//2, BALL_WIDTH, BALL_HEIGHT)
    ball_move_up_or_down = random.randrange(1,3)
    ball_move_left_or_right = random.randrange(1,4)
    if ball_move_left_or_right ==1:
        ball_move_left = True 
    else:
        ball_move_left = False
    if  ball_move_up_or_down ==1:
        ball_move_up = False
    else:
        ball_move_up = True
    player_1_score, player_2_score = 0,0
    

    while not game_over:
        horz = random.randrange(3, 5)
        vert = random.randrange(2, 4)    
        clock.tick(FPS)

        ball_movement(ball, ball_move_left, ball_move_up, horz, vert)

        for event in p.event.get():
            if event.type == p.QUIT:
               return "no"
            elif event.type == p.K_q:
                return "no"
        keys_pressed = p.key.get_pressed()
        if keys_pressed[p.K_w]:
            if player_1.y - PLAYER_VEL > 0:
                player_1.y -= PLAYER_VEL
        if keys_pressed[p.K_s]:
            if player_1.y + PLAYER_VEL + PLAYER_HEIGHT < WIN_HEIGHT:
                player_1.y += PLAYER_VEL
        if keys_pressed[p.K_UP]:
            if player_2.y - PLAYER_VEL > 0:
                player_2.y -= PLAYER_VEL
        if keys_pressed[p.K_DOWN]:
            if player_2.y + PLAYER_VEL + PLAYER_HEIGHT< WIN_HEIGHT:
                player_2.y += PLAYER_VEL
        
            
        
        ball_move_left, ball_move_up = check_collisions(player_1, player_2, ball, ball_move_left, ball_move_up)   
        player_1_score, player_2_score = check_ball_location(ball, player_1_score, player_2_score)
        draw(player_1, player_2,ball,player_1_score,player_2_score)
        p.display.update()

        if player_1_score>=10 :
            time.sleep(1)
            return "player 1 won"
        elif player_2_score>=10:
            time.sleep(1)
            return "player 2 won"
       
            
who_won = main()
time.sleep(1)
if who_won == "player 1 won":
    message("Player 1 Won", BLUE)
    time.sleep(1)

elif who_won == "player 2 won":
    message("Player 2 Won", BLUE)
    time.sleep(1)
    
p.quit()