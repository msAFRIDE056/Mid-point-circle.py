import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

# Set up ball
ball_radius = 20
ball_color = (255, 0, 0)
ball_speed = [5, 5]  # Initial speed in x and y directions
ball_position = [width // 2, height // 2]  # Initial position at the center

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update ball position
    ball_position[0] += ball_speed[0]
    ball_position[1] += ball_speed[1]

    # Bounce off the walls
    if ball_position[0] - ball_radius < 0 or ball_position[0] + ball_radius > width:
        ball_speed[0] = -ball_speed[0]
    if ball_position[1] - ball_radius < 0 or ball_position[1] + ball_radius > height:
        ball_speed[1] = -ball_speed[1]

    # Fill the screen with a background color
    screen.fill((255, 255, 255))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (int(ball_position[0]), int(ball_position[1])), ball_radius)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
