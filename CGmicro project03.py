import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
width, height = 800, 600
background_color = (255, 255, 255)
body_color = (0, 128, 255)
limb_color = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gym Boy")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a background color
    screen.fill(background_color)

    # Draw the body
    pygame.draw.rect(screen, body_color, [width // 2 - 25, height // 2 - 50, 50, 100])

    # Draw the limbs
    limb_length = 50
    pygame.draw.line(screen, limb_color, (width // 2, height // 2), (width // 2 + limb_length, height // 2 - limb_length), 5)
    pygame.draw.line(screen, limb_color, (width // 2, height // 2), (width // 2 - limb_length, height // 2 - limb_length), 5)
    pygame.draw.line(screen, limb_color, (width // 2, height // 2 + 50), (width // 2 + limb_length, height // 2 + 50 + limb_length), 5)
    pygame.draw.line(screen, limb_color, (width // 2, height // 2 + 50), (width // 2 - limb_length, height // 2 + 50 + limb_length), 5)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)
