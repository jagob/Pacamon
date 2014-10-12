import pygame, sys, os, random
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

from src.menu import menu
from src.game import game
from src.Tile import Tile
from src.Apple import Apple
from src.Player import Player
 

if __name__ == '__main__':
    pygame.init()
    screen_width, screen_height = 800, 600
    screen=pygame.display.set_mode([screen_width,screen_height])

    while True:
        playerEnabled, wincondition, map, screen = menu(screen,screen_width,screen_height)
        game(screen, playerEnabled, wincondition, map, screen_width, screen_height)
