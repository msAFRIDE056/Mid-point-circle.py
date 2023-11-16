import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
width, height = 800, 600
house_color = (255, 200, 150)
roof_color = (150, 75, 0)
door_color = (100, 50, 0)
window_color = (200, 255, 255)

# Set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple House")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a background color
    screen.fill((255, 255, 255))

    # Draw the house
    pygame.draw.rect(screen, house_color, [width // 4, height // 2, width // 2, height // 2])

    # Draw the roof
    pygame.draw.polygon(screen, roof_color, [(width // 4, height // 2), (width // 2, height // 4),
                                             (3 * width // 4, height // 2)])

    # Draw the door
    door_width, door_height = 80, 160
    pygame.draw.rect(screen, door_color, [width // 2 - door_width // 2, 3 * height // 4 - door_height,
                                          door_width, door_height])

    # Draw windows
    window_size = 60
    window_margin = 20
    pygame.draw.rect(screen, window_color, [width // 4 + window_margin, height // 2 + window_margin,
                                            window_size, window_size])
    pygame.draw.rect(screen, window_color, [3 * width // 4 - window_margin - window_size, height // 2 + window_margin,
                                            window_size, window_size])

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)
