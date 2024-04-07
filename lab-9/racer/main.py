#Imports
import pygame
import sys
from pygame.locals import *
import random
import time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_WEIGHTS = {"normal": 80, "special": 20}  # Weighted probabilities for different types of coins
COIN_THRESHOLD = 5  # Number of coins required to increase enemy speed

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#Creating Sprites Groups
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Enemy.svg"), (75, 50)), -90)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

    def move(self):
        global SCORE, SPEED
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            coin = Coin.random_spawn()
            all_sprites.add(coin)
            coins.add(coin)
            
            # Check if it's time to increase enemy speed
            if SCORE % COIN_THRESHOLD == 0:
                SPEED += 1  # Increase enemy speed by 1

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Player.png"), (75, 50)), -90)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, coin_type):
        super().__init__()
        self.coin_type = coin_type
        if self.coin_type == "normal":
            self.image = pygame.transform.scale(pygame.image.load("Coin.png"), (50, 50))
        elif self.coin_type == "special":
            self.image = pygame.transform.scale(pygame.image.load("Special_Coin.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    @staticmethod
    def random_spawn():
        # Choose coin type based on weights
        coin_type = random.choices(list(COIN_WEIGHTS.keys()), weights=COIN_WEIGHTS.values())[0]
        x = random.randint(SCREEN_WIDTH * 0.1, SCREEN_WIDTH)
        y = random.randint(SCREEN_HEIGHT * 0.1, SCREEN_HEIGHT)
        return Coin((x, y), coin_type)
    
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            all_sprites.remove(self)
            coins.remove(self)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()

enemies.add(E1)
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill((255, 255, 255))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        if hasattr(entity, 'move'):
            entity.move()

    # Collision detection
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)             
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()
    if pygame.sprite.spritecollideany(P1, coins):
        for coin in coins:
            coin.kill()
        
    pygame.display.update()
    FramePerSec.tick(FPS)
