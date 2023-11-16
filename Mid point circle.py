import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
width, height = 800, 600
center = (width // 2, height // 2)
radius = 100
color = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Midpoint Circle Algorithm")

# Function to draw a circle using the midpoint circle algorithm
def draw_circle(center, radius, color):
    x, y = radius, 0
    p = 1 - radius

    draw_symmetric_points(center, x, y, color)

    while x > y:
        y += 1

        if p <= 0:
            p = p + 2 * y + 1
        else:
            x -= 1
            p = p + 2 * y - 2 * x + 1

        draw_symmetric_points(center, x, y, color)

# Function to draw symmetric points based on the given points
def draw_symmetric_points(center, x, y, color):
    points = [
        (center[0] + x, center[1] - y),
        (center[0] - x, center[1] - y),
        (center[0] + x, center[1] + y),
        (center[0] - x, center[1] + y),
        (center[0] + y, center[1] - x),
        (center[0] - y, center[1] - x),
        (center[0] + y, center[1] + x),
        (center[0] - y, center[1] + x)
    ]

    for point in points:
        pygame.draw.circle(screen, color, point, 1)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a background color
    screen.fill((255, 255, 255))

    # Draw the circle using the midpoint circle algorithm
    draw_circle(center, radius, color)

    # Update the display
    pygame.display.flip()
