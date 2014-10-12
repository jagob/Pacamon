import pygame, sys
from pygame.locals import *

class Tile(pygame.sprite.Sprite):
   def __init__(self, x, y, image):
      pygame.sprite.Sprite.__init__(self) 
      self.image = image
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y
      self.rect.width = self.rect.width - 10
      self.rect.height = self.rect.height - 15
