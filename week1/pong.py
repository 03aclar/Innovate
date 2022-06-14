import pygame, sys, random


###general setup###
pygame.init()
# initiates all pygame modules
clock = pygame.time.Clock()
#variable clock
screen_width = 1200
screen_height = 650
#screen size
screen = pygame.display.set_mode((screen_width, screen_height))
#screen creation
#------------------------------

pygame.display.set_caption("PONGY")


#####Functions####

def ball_animation():
    global ball_speed_x, ball_speed_y


    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <=0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
    

    
def player_animation():
        player.y += player_speed

        if player.top <= 0:
            player.top = 0
        if player.bottom >= screen_height:
            player.bottom = screen_height

def opponent_animation():
        if opponent.top < ball.y:
            opponent.top += opponent_speed
        if opponent.bottom > ball.y:
            opponent.bottom -= opponent_speed

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

#------------------------------


###Game rectangles###
# ball = pygame.Rect(30, 30) # <=== previous line, replaced on line 24 #
#takes x & y position & the height and width of the rect#
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
#screen widht and height divided by 2 and then minus half of ball size#
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)

opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

###Colours###
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)


######animation#######

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

#if ball.top <=0 or ball.bottom >= screen_height:
  #  ball_speed_y *= -1

#if ball.left <= 0 or ball.right >= screen_height:
 #   ball_speed_x *= -1

###While loop###
while True:
    #user input handling
    for event in pygame.event.get():
        #all user input is classed as an ebent in pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_animation()

        
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)

    pygame.draw.rect(screen, light_grey, opponent)

    pygame.draw.ellipse(screen, light_grey, ball)


    #draw line down centre of screen, aaline stands for anti-alias line#
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))
    #(display, color, start point, end point)#


    pygame.display.flip()
    
    clock.tick(60)
    #limits how fast the loop runs#

