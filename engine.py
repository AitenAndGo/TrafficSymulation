import pygame.image
import math


class GameObject:
    def __init__(self, x=0, y=0):
        self.position = Vector(x, y)
        self.rotation = 0
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.image = None
        self.rect = None
        self.colR = 0
        self.colG = 0
        self.colB = 0
        self.front = Vector(0, 0)
        self.width = 0
        self.hight = 0

    def set_image(self, path):
        self.image = pygame.image.load(path)

    def scale(self, scale):
        new_width = int(self.image.get_width() * scale)
        new_height = int(self.image.get_height() * scale)
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect()

    def rectangular_shape(self):
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.hight)

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        self.rotation += angle

    def rotate_front(self):
        velocity = self.velocity  # przykładowy wektor prędkości
        direction = self.front  # przykładowy wektor kierunku
        cos_angle = direction.dot(velocity) / (direction.length() * velocity.length())
        if cos_angle > 1 or cos_angle < -1:
            return
        angle = math.acos(cos_angle)
        angle_degrees = math.degrees(angle)
        if angle_degrees <= 5:
            return
        print(angle_degrees)
        if velocity.x < 0:
            self.rotate(180 - angle_degrees)
        else:
            self.rotate(angle_degrees + 180)
        self.front = velocity

    def color(self, r, g, b):
        self.colR = r
        self.colG = g
        self.colB = b

    def update(self, delta_time):
        self.position = Vector(self.position.x + self.velocity.x * delta_time
                               + 0.5 * self.acceleration.x * pow(delta_time, 2),
                               self.position.y + self.velocity.y * delta_time
                               + 0.5 * self.acceleration.y * pow(delta_time, 2))
        self.velocity = Vector(self.velocity.x + self.acceleration.x * delta_time,
                               self.velocity.y + self.acceleration.y * delta_time)
        # self.rotate_front()
        if self.position.x >= 700:
            self.position.x = 0
        if self.position.y >= 700:
            self.position.y = 0
        if self.position.x < 0:
            self.position.x = 699
        if self.position.y < 0:
            self.position.y = 699

        # print(self.velocity.x)


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
