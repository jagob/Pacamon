import pygame, sys, os, random
from pygame.locals import *

class Apple(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(os.path.join("img/apple.png"))
        self.rect = self.image.get_rect()
        self.rect.x = screen_width  / 2
        self.rect.y = screen_height / 2
    
    def update(self, player_list, apple_list, background_collide_list, playerEnabled, screen_width, screen_height):
       if pygame.sprite.spritecollide(self, player_list, False):
          self.rect.x = random.randint(0  , screen_width-self.rect[2] ) 
          self.rect.y = random.randint(32 , screen_height-self.rect[3]) 
          while pygame.sprite.spritecollide(self, background_collide_list, False):
            self.rect.x = random.randint(0  , screen_width-self.rect[2] ) 
            self.rect.y = random.randint(32 , screen_height-self.rect[3]) 
