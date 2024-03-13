import pygame
import os

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Music Player")

# Define colors
WHITE = (255, 255, 255)

# Load music file
music_file = "./music/rickroll.mp3"
pygame.mixer.music.load(music_file)

current_position = 0
volume = 0.5
pygame.mixer.music.set_volume(volume)

def play():
    pygame.mixer.music.play(start=current_position)

def stop():
    pygame.mixer.music.stop()

def fast_forward():
    global current_position
    current_position += 1
    pygame.mixer.music.set_pos(current_position)

def rewind():
    global current_position
    current_position -= 1
    pygame.mixer.music.set_pos(current_position)

def increase_volume():
    global volume
    volume = min(1.0, volume + 0.1)
    pygame.mixer.music.set_volume(volume)

def decrease_volume():
    global volume
    volume = max(0.0, volume - 0.1)
    pygame.mixer.music.set_volume(volume)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop()
                else:
                    play()
            elif event.key == pygame.K_RIGHT:
                fast_forward()
            elif event.key == pygame.K_LEFT:
                rewind()
            elif event.key == pygame.K_UP:
                increase_volume()
            elif event.key == pygame.K_DOWN:
                decrease_volume()

    screen.fill(WHITE)
    pygame.display.flip()

pygame.quit()
