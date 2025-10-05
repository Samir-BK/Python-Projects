
import pygame
import random

# Setup
pygame.init()
width = 800
height = 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Dice Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 48)

# Text
welcome_text = font.render('Welcome to Simple Dice Game!', True, WHITE)
instruction_text = font.render('Press any key to roll the dice...', True, WHITE)

# Display welcome screen
screen.fill(BLACK)
screen.blit(welcome_text, ((width - welcome_text.get_width()) // 2, 50))
screen.blit(instruction_text, ((width - instruction_text.get_width()) // 2, 120))
pygame.display.flip()

# Wait for key press
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            waiting = False  # key was pressed, move to game

# Dice game (show result)
screen.fill(BLACK)
dice_number = random.randint(1, 6)
dice_text = font.render(f'You rolled a {dice_number}!', True, WHITE)
screen.blit(dice_text, ((width - dice_text.get_width()) // 2, height // 2))
pygame.display.flip()

# Wait a few seconds before quitting
pygame.time.wait(3000)
pygame.quit()
