import pygame
from pygame.locals import *
pygame.init()
width = 400
height = 300
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
size_increment = 10
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Increase the window size
    width += size_increment
    height += size_increment

    # Create a new display surface with the updated size
    window = pygame.display.set_mode((width, height))

    # Fill the window with a color (optional)
    window.fill((255, 255, 255))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
