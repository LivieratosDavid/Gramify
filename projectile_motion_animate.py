import pygame
import math


class Circle:
    def __init__(self, surface, surface_width, surface_height):
        self.surface = surface
        self.surface_width = surface_width
        self.surface_height = surface_height
        self.alpha = math.pi * 1.5
        self.radius = 250
        self.colour_name = 'white'
        self.colours = ['red', 'green', 'blue', 'white', 'orange', 'yellow', 'purple']
        self.radius_line_colour = pygame.color.Color(self.colour_name)
        self.radius_line_thickness = 2

    def display_line(self, ball, surface_width, surface_height):
        pygame.draw.line(self.surface, self.radius_line_colour, (surface_width // 2, surface_height // 2),
                         (ball.position.x, ball.position.y), self.radius_line_thickness)

    def change_radius(self, value):
        self.radius = int(value)

    def change_radius_line_colour(self, value):
        self.radius_line_colour = pygame.color.Color(self.colours[int(value) - 1])
        self.colour_name = self.colours[int(value) - 1]

    def change_radius_line_thickness(self, value):
        self.radius_line_thickness = int(value)