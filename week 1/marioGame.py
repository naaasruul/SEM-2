import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario Game")

# Load Mario image
mario_img = pygame.image.load("mario.jpeg").convert_alpha()

# Set up Mario's initial position and speed
mario_x = 0
mario_y = screen_height - mario_img.get_height()
mario_speed = 5

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move Mario
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mario_x -= mario_speed
    if keys[pygame.K_RIGHT]:
        mario_x += mario_speed

    # Draw the game world
    screen.fill((0, 0, 255))
    screen.blit(mario_img, (mario_x, mario_y))
    pygame.display.flip()