import pygame, sys, os, random
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self) 
        self.name = str(name)
        self.image = pygame.image.load(os.path.join("img" , self.name + ".png"))
        self.flip = False
        self.rect = self.image.get_rect()
        self.movementSpeed = 10
        self.pacman = False
        self.score = 0

    
    def update(self, player_list, apple_list, background_collide_list, playerEnabled, screen_width, screen_height):
        midlertidig = self.image.get_rect()
        self.rect.width = midlertidig[2]
        self.rect.height = midlertidig[3]
        
        last = self.rect.copy()
        key = pygame.key.get_pressed()

        player_list = pygame.sprite.OrderedUpdates([player_list])
        pygame.sprite.Sprite.remove(self, player_list)

        # Move x direction
        if playerEnabled >= 1:
            if self.name == "player1": 
                if key[pygame.K_a]:
                    self.rect.x -= self.movementSpeed
                    self.flip = True
                if key[pygame.K_d]:
                    self.rect.x += self.movementSpeed
                    self.flip = False
        
        if playerEnabled >= 2:
            if self.name == "player2": 
                if key[pygame.K_LEFT]:
                    self.rect.x -= self.movementSpeed
                    self.flip = True
                if key[pygame.K_RIGHT]:
                    self.rect.x += self.movementSpeed
                    self.flip = False
        
        if playerEnabled >= 3:
            if self.name == "player3":
                if key[pygame.K_j]:
                    self.rect.x -= self.movementSpeed
                    self.flip = True
                if key[pygame.K_l]:
                    self.rect.x += self.movementSpeed
                    self.flip = False
        
        if playerEnabled >= 4:
            if self.name == "player4": 
                if key[pygame.K_KP4]:
                    self.rect.x -= self.movementSpeed
                    self.flip = True
                if key[pygame.K_KP6]:
                    self.rect.x += self.movementSpeed
                    self.flip = False
        
        if playerEnabled >= 5:
            if self.name == "player5": 
                if key[pygame.K_f]:
                    self.rect.x -= self.movementSpeed
                    self.flip = True
                if key[pygame.K_h]:
                    self.rect.x += self.movementSpeed
                    self.flip = False
        
        if playerEnabled >= 6:
            if self.name == "player6": 
                if key[pygame.K_DELETE]:
                    self.rect.x -= self.movementSpeed
                    self.flip = True
                if key[pygame.K_PAGEDOWN]:
                    self.rect.x += self.movementSpeed
                    self.flip = False

        # colliding players
        collidingPlayer_list = pygame.sprite.spritecollide(self, player_list, False)
        for collidingPlayer in collidingPlayer_list:
            if not self.killPlayers(collidingPlayer, background_collide_list, screen_width, screen_height):
                # self.rect = last
                self.rect.x = last[0]
        if self.rect.x < - self.rect.width / 2:
           self.rect.x = screen_width - self.rect.width / 2
        if self.rect.x - self.rect.width / 2 > screen_width - self.rect.width / 2:
           self.rect.x = - self.rect.width / 2
        
        # colliding background
        for item in pygame.sprite.spritecollide(self, background_collide_list, False):
            self.rect.x = last[0]


        # Move y direction
        if playerEnabled >= 1:
            if self.name == "player1": 
                if key[pygame.K_w]:
                    self.rect.y -= self.movementSpeed
                if key[pygame.K_s]:
                    self.rect.y += self.movementSpeed
        
        if playerEnabled >= 2:
            if self.name == "player2": 
                if key[pygame.K_UP]:
                    self.rect.y -= self.movementSpeed
                if key[pygame.K_DOWN]:
                    self.rect.y += self.movementSpeed
        
        if playerEnabled >= 3:
            if self.name == "player3":
                if key[pygame.K_i]:
                    self.rect.y -= self.movementSpeed
                if key[pygame.K_k]:
                    self.rect.y += self.movementSpeed
        
        if playerEnabled >= 4:
            if self.name == "player4": 
                if key[pygame.K_KP8]:
                    self.rect.y -= self.movementSpeed
                if key[pygame.K_KP5]:
                    self.rect.y += self.movementSpeed
        
        if playerEnabled >= 5:
            if self.name == "player5": 
                if key[pygame.K_t]:
                    self.rect.y -= self.movementSpeed
                if key[pygame.K_g]:
                    self.rect.y += self.movementSpeed
        
        if playerEnabled >= 6:
            if self.name == "player6": 
                if key[pygame.K_HOME]:
                    self.rect.y -= self.movementSpeed
                if key[pygame.K_END]:
                    self.rect.y += self.movementSpeed
        
        # colliding players
        collidingPlayer_list = pygame.sprite.spritecollide(self, player_list, False)
        for collidingPlayer in collidingPlayer_list:
            if not self.killPlayers(collidingPlayer, background_collide_list, screen_width, screen_height):
                self.rect.y = last[1]
        if self.rect.y < 32 - self.rect.height / 2:
           self.rect.y = screen_height - self.rect.height / 2
        if self.rect.y - self.rect.height / 2 > screen_height - self.rect.height / 2:
           self.rect.y = 32 - self.rect.height / 2 
        
        # colliding background
        for item in pygame.sprite.spritecollide(self, background_collide_list, False):
            self.rect.y = last[1]
        
        # colliding apple
        if pygame.sprite.spritecollide(self, apple_list, False):
            self.pacman = True
            for player in player_list:
                player.pacman = False

        player_list.add(self)

        
        # animation
        if self.pacman:
            self.image = pygame.image.load(os.path.join("img/pacman.png"))
            self.movementSpeed = 10
        else:
            self.image = pygame.image.load(os.path.join("img" , self.name + ".png"))
            self.movementspeed = 10
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, False)
    
    def killPlayers(self, collidingPlayer, background_collide_list, screen_width, screen_height):
        if self.pacman:
            # spawn new collidingPlayer
            collidingPlayer.rect.x = random.randint(0 , screen_width  - self.rect[2]) 
            collidingPlayer.rect.y = random.randint(32, screen_height - self.rect[3]) 
            while pygame.sprite.spritecollide(collidingPlayer, background_collide_list, False):
                collidingPlayer.rect.x = random.randint(0 , screen_width  - self.rect[2]) 
                collidingPlayer.rect.y = random.randint(32, screen_height - self.rect[3]) 
            self.score += 1
            return True
        if collidingPlayer.pacman is True:
            self.rect.x = random.randint(0 , screen_width  - self.rect[2]) 
            self.rect.y = random.randint(32, screen_height - self.rect[3]) 
            while pygame.sprite.spritecollide(self, background_collide_list, False):
                self.rect.x = random.randint(0 , screen_width  - self.rect[2]) 
                self.rect.y = random.randint(32, screen_height - self.rect[3]) 
            collidingPlayer.score += 1
            return False
    
    def die(self):
        self.kill()
