import random

import engine
from engine import Vector


class Car:
    def __init__(self, x, y, mapa):
        self.tabele = mapa.map
        self.map = mapa
        self.a = 30
        self.gameObject = engine.GameObject(x, y)
        self.gameObject.width = 5
        self.gameObject.hight = 5
        self.dir = ''
        self.mapx = x // self.map.size
        self.mapy = y // self.map.size
        self.errors = 0
        self.roaddir = ''
        # self.gameObject.set_image("images/autko.png")
        self.gameObject.front = Vector(0, 1)
        # self.gameObject.scale(0.05)
        self.gameObject.color(random.randint(0, 150), random.randint(0, 150), random.randint(0, 150))
        # self.gameObject.velocity = engine.Vector(random.randint(-100, 100), random.randint(-100, 100))
        # self.gameObject.acceleration = engine.Vector(random.randint(-20, 20), random.randint(-20, 20))
        # self.gameObject.velocity = engine.Vector(50, 0)
        # self.gameObject.acceleration = engine.Vector(0, -10)
        # self.gameObject.rotate_front()

    def upgrade(self):
        x1 = int(self.gameObject.position.x // self.map.size)
        x2 = int((self.gameObject.position.x + self.gameObject.width) // self.map.size)
        y1 = int(self.gameObject.position.y // self.map.size)
        y2 = int((self.gameObject.position.y + self.gameObject.hight) // self.map.size)
        if not self.tabele[self.mapy][self.mapx].iscross:
            self.tabele[self.mapy][self.mapx].stop = False
        if x1 == x2 and y1 == y2:
            self.mapx = x1
            self.mapy = y1
            self.roaddir = self.tabele[self.mapy][self.mapx].dir
        x = self.mapx
        y = self.mapy
        self.tabele[y][x].stop = True

        if self.roaddir is not self.dir:
            self.turn(self.roaddir)

        count = self.count_stop(x, y, self.roaddir)
        # print(count)
        if count > 1 and self.gameObject.velocity.length() > 0:
            self.a = (self.gameObject.velocity.length() ** 2) / (2 * self.map.size * (count - 1))
            if self.gameObject.velocity.length() < self.tabele[y][x].val:
                self.a *= -1
        if count > 3:
            self.a = 30

        if self.gameObject.velocity.length() < self.tabele[y][x].val:
            self.dir = self.roaddir
            if self.dir == 'r':
                if self.gameObject.velocity.x < 0:
                    self.gameObject.velocity.x = 0
                    self.gameObject.acceleration.x = 0
                else:
                    self.gameObject.acceleration = engine.Vector(self.a, 0)
            elif self.dir == 'l':
                if self.gameObject.velocity.x > 0:
                    self.gameObject.velocity.x = 0
                    self.gameObject.acceleration.x = 0
                else:
                    self.gameObject.acceleration = engine.Vector(-self.a, 0)
            elif self.dir == 'd':
                if self.gameObject.velocity.y < 0:
                    self.gameObject.velocity.y = 0
                    self.gameObject.acceleration.y = 0
                self.gameObject.acceleration = engine.Vector(0, self.a)
            elif self.dir == 'u':
                if self.gameObject.velocity.y > 0:
                    self.gameObject.velocity.y = 0
                    self.gameObject.acceleration.y = 0
                else:
                    self.gameObject.acceleration = engine.Vector(0, -self.a)
        elif self.gameObject.velocity.length() > self.tabele[y][x].val:
            if self.dir == 'r':
                if self.gameObject.velocity.x < 0:
                    self.gameObject.velocity.x = 0
                    self.gameObject.acceleration.x = 0
                else:
                    self.gameObject.acceleration = engine.Vector(-self.a, 0)
            elif self.dir == 'l':
                if self.gameObject.velocity.x > 0:
                    self.gameObject.velocity.x = 0
                    self.gameObject.acceleration.x = 0
                else:
                    self.gameObject.acceleration = engine.Vector(self.a, 0)
            elif self.dir == 'd':
                if self.gameObject.velocity.y < 0:
                    self.gameObject.velocity.y = 0
                    self.gameObject.acceleration.y = 0
                else:
                    self.gameObject.acceleration = engine.Vector(0, -self.a)
            elif self.dir == 'u':
                if self.gameObject.velocity.y > 0:
                    self.gameObject.velocity.y = 0
                    self.gameObject.acceleration.y = 0
                else:
                    self.gameObject.acceleration = engine.Vector(0, self.a)
        else:
            self.gameObject.acceleration = engine.Vector(0, 0)

    def turn(self, roaddir):
        # print(roaddir)
        v = self.gameObject.velocity.length()
        if roaddir == 'd':
            self.gameObject.acceleration = engine.Vector(0, 0)
            self.gameObject.velocity = engine.Vector(0, v)
            self.dir = roaddir
        elif roaddir == 'u':
            self.gameObject.acceleration = engine.Vector(0, 0)
            self.gameObject.velocity = engine.Vector(0, -v)
            self.dir = roaddir
        elif roaddir == 'l':
            self.gameObject.acceleration = engine.Vector(0, 0)
            self.gameObject.velocity = engine.Vector(-v, 0)
            self.dir = roaddir
        elif roaddir == 'r':
            self.gameObject.acceleration = engine.Vector(0, 0)
            self.gameObject.velocity = engine.Vector(v, 0)
            self.dir = roaddir

    def count_stop(self, x, y, direction):
        count = 0
        if direction == 'r':
            # Calculate cells with value of True to the right of the current cell
            for i in range(x + 1, len(self.tabele[y]) + x):
                if i >= len(self.tabele[y]):
                    i -= len(self.tabele[y])
                if self.tabele[y][i].stop:
                    break
                else:
                    count += 1
        elif direction == 'l':
            # Calculate cells with value of True to the left of the current cell
            for i in range(x - 1, -1 - (len(self.tabele[y]) + x), -1):
                if i < 0:
                    i += len(self.tabele[y])
                if self.tabele[y][i].stop:
                    break
                else:
                    count += 1
        elif direction == 'd':
            # Calculate distance to the next cell with value of True below the current cell
            i = y + 1
            while i < len(self.tabele):
                if self.tabele[i][x].stop:
                    break
                else:
                    count += 1
                    i += 1
            # If we reached the end of the table, wrap around to the top of the column
            if i == len(self.tabele):
                for j in range(x, len(self.tabele[y])):
                    if self.tabele[0][j].stop:
                        break
                    else:
                        count += 1
        elif direction == 'u':
            # Calculate distance to the next cell with value of True above the current cell
            i = y - 1
            while i >= 0:
                if self.tabele[i][x].stop:
                    break
                else:
                    count += 1
                    i -= 1
            # If we reached the top of the column, wrap around to the bottom of the table
            if i == -1:
                for j in range(x, len(self.tabele[y])):
                    if self.tabele[-1][j].stop:
                        break
                    else:
                        count += 1
        return count
