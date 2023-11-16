import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

gluPerspective(45, (width / height), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

car_vertices = [
    [1, -1, -1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, -1, -1],
    [0.5, 1, -0.5],
    [0.5, 1, 0.5],
    [-0.5, 1, 0.5],
    [-0.5, 1, -0.5]
]

car_edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)

    for edge in car_edges:
        for vertex in edge:
            glVertex3fv(car_vertices[vertex])

    glEnd()
    pygame.display.flip()
    pygame.time.wait(10)
