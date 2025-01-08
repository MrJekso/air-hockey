import pygame
class Player():
    def __init__(self,x,y,size_x,size_y,screen_height,screen, is_bot):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.lever = True
        self.screen = screen
        self.screen_height = screen_height
        self.is_bot = is_bot
        self.__lever_key_up = False
        self.__lever_key_down = False


    def set_lever_key_up_on(self):
        self.__lever_key_up = True
    def set_lever_key_up_off(self):
        self.__lever_key_up = False    

    def set_lever_key_down_on(self):
        self.__lever_key_down = True
    def set_lever_key_down_off(self):
        self.__lever_key_down = False

    def draw(self):
        pygame.draw.rect(self.screen, (100,220,0), pygame.Rect(self.x, self.y, self.size_x, self.size_y), 0)
        if(self.is_bot):
            if self.lever:
                self.y += 0.1
            else:
                self.y -= 0.1
            if self.y < 0.0:
                self.lever = True
            elif self.y + self.size_y > self.screen_height:
                self.lever = False
        else:
            if self.__lever_key_down == True and self.y > 0.0:
                self.y -= 0.4
            if self.__lever_key_up == True and self.y + self.size_y < self.screen_height:
                self.y += 0.4