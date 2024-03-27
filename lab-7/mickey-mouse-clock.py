import sys
import pygame
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mickey Clock')

clock_image = pygame.image.load('./images/clock.png')
hour_hand_image = pygame.image.load('./images/hour_hand.png')
minute_hand_image = pygame.image.load('./images/minute_hand.png')

clock_image = pygame.transform.scale(clock_image, (WIDTH, HEIGHT))

WHITE = (255, 255, 255)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    clock_rect = screen.blit(clock_image, (0, 0))

    screen.blit(pygame.transform.rotate(hour_hand_image, 130), (295, 287))
    screen.blit(pygame.transform.rotate(minute_hand_image, -130), (270, 250))
    # rotated_hour_hand = pygame.transform.rotate(hour_hand_image, -90)
    # screen.blit(rotated_hour_hand, (WIDTH/2 - rotated_hour_hand.get_width()/2, HEIGHT/2 - rotated_hour_hand.get_height()/2))

    # rotated_minute_hand = pygame.transform.rotate(minute_hand_image, -45)
    # screen.blit(rotated_minute_hand, (WIDTH/2 - rotated_minute_hand.get_width()/2, HEIGHT/2 - rotated_minute_hand.get_height()/2))

    pygame.display.update()
    clock.tick(60)  # Adjust the frame rate as needed
