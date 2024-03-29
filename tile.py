# tile.py
import pygame
import numpy as np

def rotation_matrix_y(angle):
    angle_rad = np.radians(angle)
    return np.array([
        [np.cos(angle_rad), 0, np.sin(angle_rad)],
        [0, 1, 0],
        [-np.sin(angle_rad), 0, np.cos(angle_rad)]
    ])

def rotation_matrix_x(angle):
    angle_rad = np.radians(angle)
    return np.array([
        [1, 0, 0],
        [0, np.cos(angle_rad), -np.sin(angle_rad)],
        [0, np.sin(angle_rad), np.cos(angle_rad)]
    ])

def rotate_vector(v, angle_x, angle_y):
    """Rotate vector v around X axis by angle_x and around Y axis by angle_y."""
    return rotation_matrix_y(angle_y) @ (rotation_matrix_x(angle_x) @ v)

class Tile:
    def __init__(self, color, position, size, screen_center):
        self.color = color
        self.position = np.array(position)  # A 3D position
        self.size = size
        self.screen_center = screen_center
        self.angle_x = 0  # Rotation around X-axis
        self.angle_y = 0  # Rotation around Y-axis

    def rotate(self, angle_x, angle_y):
        self.angle_x += angle_x
        self.angle_y += angle_y

    def get_corners(self):
        half_size = self.size / 2
        corners = [
            np.array([-half_size, -half_size, 0]),
            np.array([half_size, -half_size, 0]),
            np.array([half_size, half_size, 0]),
            np.array([-half_size, half_size, 0])
        ]
        rotated_corners = [rotate_vector(corner, self.angle_x, self.angle_y) + self.position for corner in corners]
        # Project 3D coordinates into 2D
        projected_corners = [(self.screen_center[0] + corner[0], self.screen_center[1] + corner[1]) for corner in rotated_corners]
        return projected_corners

    def draw(self, surface):
        pygame.draw.polygon(surface, self.color, self.get_corners())
