import pygame
import math

import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1440, 1080))
clock = pygame.time.Clock()
running = True
dt = 0
sun_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
earth_pos = pygame.Vector2(400, 300)
G = 1000
M = 1000
m = 100
r = earth_pos.distance_to(sun_pos)
earth_vel = pygame.Vector2(10000, 0)
u0 = 1000
F = G * m*M/r**2
trail = []


while running:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    trail.append(earth_pos.copy())
    a = F/m 

    # acceleration vector
    direction = sun_pos - earth_pos
    r_vec = earth_pos - sun_pos
    tangent = pygame.Vector2(-r_vec.y, r_vec.x).normalize()
    acceleration = direction * a

    # update velocity and position
    speed = math.sqrt(G * M / r_vec.length())
    earth_vel = tangent * speed
    earth_pos += earth_vel * dt

    direction = pygame.Vector2(-r_vec.y, r_vec.x).normalize()
    earth_vel = direction * speed
    # draw
    screen.fill("black")
    pygame.draw.circle(screen, "yellow", sun_pos, 50)
    pygame.draw.circle(screen, "blue", earth_pos, 20)

    if len(trail) > 1:
        pygame.draw.lines(screen, "white", False, trail, 2)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
