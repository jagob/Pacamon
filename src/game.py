import pygame, sys, os, random
from pygame.locals import *

from Player import *
from Apple import *
from Tile import *

green    = ( 43, 130, 53)
grey     = (100, 100, 100)
black    = (  0,   0,   0)
white    = (255, 255, 255)

def game(screen, playerEnabled, wincondition, map, screen_width, screen_height):
    
    all_sprites_list = pygame.sprite.Group()

    # ordered group
    player_list = pygame.sprite.OrderedUpdates()
    if playerEnabled >= 1:
        player1 = Player("player1")
        player_list.add(player1)
    
    if playerEnabled >= 2:
        player2 = Player("player2")
        player_list.add(player2)
    
    if playerEnabled >= 3:
        player3 = Player("player3")
        player_list.add(player3)
    
    if playerEnabled >= 4:
        player4 = Player("player4")
        player_list.add(player4)
    
    if playerEnabled >= 5:
        player5 = Player("player5")
        player_list.add(player5)
    
    if playerEnabled >= 6:
        player6 = Player("player6")
        player_list.add(player6)
    
    all_sprites_list.add(player_list)
    
    spawns = [( 6*32 + 32 - player1.rect.width,  5*32) , \
              (18*32 + 32 - player1.rect.width,  5*32) , \
              ( 6*32 + 32 - player1.rect.width, 13*32) , \
              (18*32 + 32 - player1.rect.width, 13*32) , \
              ( 7*32 + 32 - player1.rect.width,  5*32) , \
              (17*32 + 32 - player1.rect.width, 13*32) ]
    i = 0
    for player in player_list:
        playerSpawnpos = random.randint(1,playerEnabled-i)
        player.rect.x, player.rect.y = spawns[playerSpawnpos - 1]
        del spawns[playerSpawnpos - 1]
        i += 1
    
    # apple
    apple_list = pygame.sprite.Group()
    apple = Apple(screen_width,screen_height)
    all_sprites_list.add(apple)
    apple_list.add(apple)
    
    # Used to manage how fast the screen updates
    clock=pygame.time.Clock()
    leadingPlayerScore = 0
    
    # Map
    data = [line.strip() for line in open("maps/map%d.txt"%map)]
    # data = [line.strip() for line in open(os.path.join("levels", "map%d.txt"%level))]
    data.insert(0, [1234567890123456789012345])
    del data[19]
    y = 0
    background_list = pygame.sprite.Group()
    background_collide_list = pygame.sprite.Group()
    for row in data:
        x= 0
        for tiles in row:
            if tiles != ' ' and tiles != 'p' and tiles != 'a':
                if tiles == 'b':
                    image = pygame.image.load(os.path.join("img/busk.png"))
                    tile = Tile(x, y, image)
                    background_collide_list.add(tile)
                    background_list.add(tile)
                if tiles == 's':
                    image = pygame.image.load(os.path.join("img/stub.png"))
                    tile = Tile(x, y, image)
                    background_collide_list.add(tile)
                    background_list.add(tile)
            x += 32
        y += 32
        # print row # print map
    # all_sprites_list.add(background_list)
    showWinner = True
    
#    ------- Game Program Loop -------------------------------------------
    while leadingPlayerScore < wincondition:
        screen.fill(green)
        pygame.draw.rect(screen, grey, (0, 0, screen_width, 32)  )
        pygame.draw.line(screen, black, (0, 31) , (screen_width,31), 3)
        
        all_sprites_list.update(player_list, apple_list, background_collide_list, playerEnabled, screen_width, screen_height)
        
        background_list.draw(screen)
        all_sprites_list.draw(screen)
        
        # score
        font = pygame.font.Font('freesansbold.ttf', 24)
        posx , posy = (50, 5)
        for player in player_list:
            text=font.render(str(player.score), True, white)
            screen.blit(pygame.image.load("img/" + player.name + "score.png"), (posx, posy))
            # screen.blit(pygame.image.load(os.path.join("img/" + player.name + "score.png"), (posx, posy)))
            
            screen.blit(text, (posx + 30, posy - 4))     
            posx += 110

            if player.score > leadingPlayerScore:
                leadingPlayerScore = player.score

        text=font.render("FPS:  " + str(int(clock.get_fps())), True, black)
        screen.blit(text, (screen_width - 130, 0))     
        clock.tick(50)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit
            if event.type == KEYDOWN and event.key == K_RETURN:
                leadingPlayerScore = wincondition 
                showWinner = False
    
    # clear screen for next game
    for item in all_sprites_list:
        item.kill()
    
    while showWinner:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit
            if event.type == KEYDOWN and event.key == K_RETURN:
                showWinner = False
