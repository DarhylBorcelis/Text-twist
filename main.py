import pygame
import random

# Initialize pygame
pygame.init()

# Create main window
SCREEN = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Text Twist")

state = "menu"  # start with menu

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == "menu":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                state = "game"  # press space to start game

    if state == "menu":
        SCREEN.fill((200, 200, 200))
        font = pygame.font.Font(None, 50)
        text = font.render("Press SPACE to Start", True, (0, 0, 0))
        SCREEN.blit(text, (300, 250))

    elif state == "game":
        SCREEN.fill((100, 150, 255))
        # draw your game stuff here
        font = pygame.font.Font(None, 50)
        text = font.render("Game Running...", True, (255, 255, 255))
        SCREEN.blit(text, (300, 250))

    pygame.display.update()
