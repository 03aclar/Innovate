import pygame, sys


pygame.init()


clock= pygame.time.clock()

screen_width= 1280
screen_height = 960

screen = pygame.display
screen = ((screen_width,screen_height))

pygame.display.set_caption("pong!!!")


#-----------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            sys.exit()