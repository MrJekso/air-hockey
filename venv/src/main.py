import pygame
import sys
import random

from Player import Player
from Ball   import Ball

pygame.init()
 
width = 1800
height = 800
screen = pygame.display.set_mode((width, height))
text = pygame.font.Font(None, 86)

player_one = Player(30,100,50,200,height,screen,False)
player_two = Player(width - 50 - 30,100,50,200,height,screen,False)
ball       = Ball(width / 2, height / 2, 30,random.randint(0,1),random.randint(0,1),width,height,screen,player_one,player_two)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_one.set_lever_key_up_on()
            if event.key == pygame.K_UP:
                player_two.set_lever_key_up_on()
            if event.key == pygame.K_s:
                player_one.set_lever_key_down_on()
            if event.key == pygame.K_DOWN:
                player_two.set_lever_key_down_on()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_one.set_lever_key_up_off()
            if event.key == pygame.K_UP:
                player_two.set_lever_key_up_off()
            if event.key == pygame.K_s:
                player_one.set_lever_key_down_off()
            if event.key == pygame.K_DOWN:
                player_two.set_lever_key_down_off()
    
    pygame.draw.rect(screen, (0,  0, 0)  ,pygame.Rect( 0, 0,  width,  height), 0)
   
    ball.draw()
    player_one.draw()
    player_two.draw()
    
    text1 = text.render(ball.get_count(), 1, (180, 200, 0))
    screen.blit(text1, (width / 2 - 60 , height - 100))

    pygame.display.flip()