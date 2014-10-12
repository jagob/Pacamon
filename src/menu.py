import pygame, sys, os, random
from pygame.locals import *

black    = (  0,   0,   0)
grey     = (100, 100, 100)
white    = (255, 255, 255)

def menu(screen,screen_width,screen_height):
    font = pygame.font.Font('freesansbold.ttf', 24)
    menuItem = 2 # starting position
    map = 2
    playerEnabled = 4
    wincondition = 20 # default wincondition
    full = False
    runMenu = True
    btn_start        = MenuBtn(1, "Start", 50,  50)
    btn_players      = MenuBtn(2, "Players: " + str(playerEnabled), 50, 100)
    btn_wincondition = MenuBtn(3, "Wincondition: " + str(wincondition), 50, 150)
    btn_map          = MenuBtn(4, "Map: " + str(map), 50, 200)
    btn_fullscreen   = MenuBtn(5, "Fullscreen: ", 50, 250)
    btn_quit         = MenuBtn(6, "Quit", 50,  300)
    
    menuItems = [btn_start, btn_players, btn_wincondition, btn_map, btn_fullscreen, btn_quit]
    
    clock=pygame.time.Clock()
    while runMenu:
        screen.fill(grey)
        
        for item in menuItems:
            menuItem, playerEnabled, runMenu, wincondition, map, full= item.update(menuItem, playerEnabled, runMenu, wincondition, map, full)
            
            item.rend = font.render(item.text, True, item.color)
            screen.blit(item.rend, (item.x, item.y))     
        
        pygame.display.flip()
        clock.tick(50)
    
    if full:
        screen=pygame.display.set_mode([screen_width,screen_height], FULLSCREEN)
    else: 
        screen=pygame.display.set_mode([screen_width,screen_height])
    return playerEnabled, wincondition, map, screen



class MenuBtn():
    def __init__(self, itemInList, text, x, y):
        self.itemInList = itemInList
        self.x = x
        self.y = y
        self.color = black
        self.text = text
        font = pygame.font.Font('freesansbold.ttf', 24)
        self.rend = font.render("hej", True, black)
    
    def update(self, menuItem, playerEnabled, runMenu, wincondition, map, full):
        if self.itemInList == 2:
            self.text = "Players: " + str(playerEnabled)
        if self.itemInList == 3:
            self.text = "Wincondition: " + str(wincondition)
        if self.itemInList == 4:
            self.text = "Map:  " + str(map)
        if self.itemInList == 5:
            self.text = "Fullscreen: " + str(full)
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE or event.type == KEYDOWN and event.key == K_RETURN and menuItem == 6:
                pygame.quit()
                sys.exit
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    menuItem += 1
                if menuItem > 6:
                    menuItem = 1
                if event.key == K_UP:
                    menuItem -= 1
                    if menuItem < 1:
                        menuItem = 6
                if event.key == K_RIGHT and menuItem == 2:
                    playerEnabled += 1
                    if playerEnabled > 6:
                        playerEnabled = 6
                if event.key == K_LEFT and menuItem == 2:
                    playerEnabled -= 1
                    if playerEnabled < 1:
                        playerEnabled = 1
                if event.key == K_RIGHT and menuItem == 3:
                    wincondition += 10
                if event.key == K_LEFT and menuItem == 3:
                    wincondition -= 10
                    if wincondition < 1:
                        wincondition = 1
                if event.key == K_RIGHT and menuItem == 4:
                    map += 1
                    if map > 10:
                        map = 10
                if event.key == K_LEFT and menuItem == 4:
                    map -= 1
                    if map < 1:
                        map = 1
                if event.key == K_RIGHT and menuItem == 5 or event.key == K_LEFT and menuItem == 5:
                    full= not full
                if event.key == K_RETURN:
                    runMenu = False
                    return menuItem, playerEnabled, runMenu, wincondition, map, full
    
        if self.itemInList == menuItem:
            self.color = white
        else:
            self.color = black
        return menuItem, playerEnabled, runMenu, wincondition, map, full
