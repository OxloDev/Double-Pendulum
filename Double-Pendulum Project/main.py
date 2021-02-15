import pygame
import os
import math
import random
from points import *
import formular
from pygame import font

os.environ['SDL_VIDEO_CENTERED']='1'

width, height = 1920, 1080
SIZE = (width, height)
pygame.init()
pygame.display.set_caption("Double Pendulum")
fps = 32
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

#colors
white = (255, 255 , 255)
black = (0, 0, 0)

length1 = 200
length2 = 200

mass1 = 40
mass2 = 40

angle1 = math.pi/2
angle2 = math.pi/2
angle_velocity1 = 0
angle_velocity2 = 0
angle_acceleration1 = 0
angle_acceleration2 = 0
Gravity = 4
scatter1 = []
scatter2 = []

starting_point = (int(width/2) , int(height/4))

x_offset = starting_point[0]
y_offset = starting_point[1]

run = True

while run:
    clock.tick(fps)

    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # acceleration formula
    angle_acceleration1 = formular.FirstAcceleration(angle1, angle2, mass1, mass2, length1, length2, Gravity, angle_velocity1, angle_velocity2)
    angle_acceleration2 = formular.SecondAcceleration(angle1, angle2, mass1, mass2, length1, length2, Gravity, angle_velocity1, angle_velocity2)

    x1 = float(length1 * math.sin(angle1)+x_offset)
    y1 = float(length1 * math.cos(angle1)+y_offset)

    x2 = float(x1 + length2 * math.sin(angle2))
    y2 = float(y1 + length2 * math.cos(angle2))

    # angle varies with respect to the velocity and the velocity with respect to the acceleration
    angle_velocity1 += angle_acceleration1
    angle_velocity2 += angle_acceleration2
    angle1 += angle_velocity1
    angle2 += angle_velocity2

    scatter1.append((x1, y1))
    scatter2.append((x2, y2))


    for point in scatter2:
        random_color = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
        plot = Points(point[0], point[1], screen, black, scatter2)
        plot.draw()

    pygame.draw.line(screen, black, starting_point, (x1, y1), 6)


    pygame.draw.line(screen, black, (x1, y1), (x2, y2), 6)
    pygame.draw.circle(screen, black, (int(x2), int(y2)), 10)
    pygame.draw.circle(screen, (60, 250, 127), (int(x1), int(y1)), 15)
    if len(scatter1) > 1:
        pygame.draw.lines(screen, (200, 50, 100), False, scatter1, 1)
    pygame.display.update()

pygame.quit()
