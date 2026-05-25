import pygame
import math

# ---------------- SETUP ----------------
pygame.init()
screen = pygame.display.set_mode((1440, 1080))
pygame.display.set_caption("Earth-Sun Orbit")
clock = pygame.time.Clock()
running = True
dt = 0

# ---------------- CONSTANTS ----------------
G = 6.674e-11
M = 1.989e30
m = 5.972e24
AU = 1.496e11
SCALE = 4e8
TIME_SCALE = 3600 * 200
STEPS = 10

# ---------------- INITIAL CONDITIONS ----------------
sun_pos_real = pygame.Vector2(0, 0)
earth_pos_real = pygame.Vector2(AU, 0)
orbital_speed = math.sqrt(G * M / AU)
earth_vel = pygame.Vector2(0, -orbital_speed)

trail = []

def to_screen(pos):
    screen_center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    return screen_center + pos / SCALE

# ---------------- MAIN LOOP ----------------
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for _ in range(STEPS):
        r_vec = earth_pos_real - sun_pos_real
        r = r_vec.length()
        acceleration = -r_vec.normalize() * (G * M / r**2)
        earth_vel += acceleration * (dt / STEPS) * TIME_SCALE
        earth_pos_real += earth_vel * (dt / STEPS) * TIME_SCALE

    trail.append(to_screen(earth_pos_real).copy())
    if len(trail) > 1000:
        trail.pop(0)

    screen.fill("black")
    pygame.draw.circle(screen, "yellow", to_screen(sun_pos_real), 40)
    pygame.draw.circle(screen, "blue", to_screen(earth_pos_real), 10)

    if len(trail) > 1:
        pygame.draw.lines(screen, "white", False, trail, 2)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
