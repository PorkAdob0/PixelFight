import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Pixel Duel")
clock = pygame.time.Clock()
fullscreen = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if not fullscreen:
                    # Switch to full screen mode
                    screen = pygame.display.set_mode((1000, 600), pygame.FULLSCREEN)
                    fullscreen = True
                else:
                    # Switch back to windowed mode
                    screen = pygame.display.set_mode((1000, 600))
                    fullscreen = False
            # If the user presses the 'm' key, minimize the game window
            elif event.key == pygame.K_m:
                pygame.display.iconify()

    # Update the display
    pygame.display.update()

    # Limit the frame rate to 60 frames per second
    clock.tick(60)