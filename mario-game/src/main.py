# main.py

import pygame
from levels.level1 import setup_level
from characters.mario import Mario
from utils.helpers import load_image

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario Game")

# Initialize game variables
mario = Mario(position=(100, 500), lives=3)
level = setup_level()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle user input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mario.run(direction='left')
            elif event.key == pygame.K_RIGHT:
                mario.run(direction='right')
            elif event.key == pygame.K_SPACE:
                mario.jump()

    # Update game state
    level.update()
    mario.update()

    # Draw everything
    screen.fill((0, 0, 0))  # Clear the screen
    level.draw(screen)
    mario.draw(screen)

    # Refresh the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()