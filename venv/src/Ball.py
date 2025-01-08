import pygame
import random

class Ball():
    def __init__(self, x, y, radius, lever_x, lever_y,screen_width,screen_height,screen,player_one,player_two):
        self.x              = x
        self.y              = y
        self.radius         = radius 
        self.lever_x        = lever_x
        self.lever_y        = lever_y
        self.screen_width   = screen_width
        self.screen_height  = screen_height
        self.screen         = screen
        self.x_direction    = 0.0
        self.y_direction    = 0.0
        self.set_direction()
        self.player_one     = player_one
        self.player_two     = player_two
        self.__count_left   = 0
        self.__count_right  = 0

    def get_count(self):
        return str(self.__count_left) + " : " + str(self.__count_right)

    def set_direction(self):
        self.x_direction  = random.uniform(1.00, 1.00)#random.random()
        self.y_direction  = random.uniform(1.00, 1.00)
    
    def check_one(self):
        res = False
        if (self.x <= self.player_one.x + self.player_one.size_x) and (self.y >= self.player_one.y and self.y <= self.player_one.y + self.player_one.size_y):
            res = True
        return res

    def check_two(self):
        res = False
        if (self.x >= self.player_two.x and self.x <= self.player_two.x + self.player_two.size_x) and (self.y >= self.player_two.y and self.y <= 50 + self.player_two.y + self.player_two.size_y):
            res = True
        return res

    def draw(self):

        if self.x < 0.0:
            self.__count_right += 1

        if self.x > self.screen_width - self.radius:
            self.__count_left += 1

        if self.x < 0.0 or self.check_one():
            self.lever_x = True
        elif self.x + self.radius > self.screen_width or self.check_two():
            self.lever_x = False

        if self.y < 0.0:
            self.lever_y = True
        elif self.y + self.radius > self.screen_height:
            self.lever_y = False
            
################################
        if self.lever_x:
            self.x += self.x_direction
        else:
            self.x -= self.x_direction
        if self.lever_y:
            self.y += self.y_direction
        else:
            self.y -= self.y_direction

        pygame.draw.circle(self.screen, (0,200,200), (self.x, self.y), self.radius, width=0)
