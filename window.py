import pygame
import time


class Window:
    def __init__(self, simulation, bg_color_r=255, bg_color_g=255, bg_color_b=255):
        pygame.init()
        self.simulation = simulation
        self.width = simulation.resx * simulation.mapsize
        self.height = simulation.resy * simulation.mapsize
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bg_color = (bg_color_r, bg_color_g, bg_color_b)
        self.name = "simulation"
        self.tick_rate = 120
        pygame.display.set_caption(self.name)
        self.start_time = time.perf_counter()
        self.tick = -5 * self.tick_rate - 1

    def loop(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            self.screen.fill(self.bg_color)
            delta_time = clock.tick(self.tick_rate) / 1000.0  # czas od ostatniego klatki w sekundach
            self.tick += 1
            # print(1 / delta_time)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # dodaj tutaj kod rysowania lub logiki gry
            self.update_objects(delta_time, self.tick)
            self.draw_map()
            self.draw(self.simulation.objects)
            # zaktualizuj ekran
            pygame.display.flip()
        pygame.quit()

    def run(self):
        self.loop()

    def draw_map(self):
        for i in range(self.simulation.map.height):
            for j in range(self.simulation.map.width):
                if self.simulation.map.map[i][j].val is not None:
                    y = i * self.simulation.map.size
                    x = j * self.simulation.map.size
                    if self.simulation.map.map[i][j].light is True:
                        if self.simulation.map.map[i][j].iscross is True:
                            color = (255, 0, 0)
                        else:
                            color = (0, 255, 0)
                    else:
                        color = (200, 200, 200)
                    # if self.simulation.map.map[i][j].stop is True:
                    #     color = (0, 0, 0)
                    road = pygame.Rect(x, y, self.simulation.mapsize, self.simulation.mapsize)
                    pygame.draw.rect(self.screen, color, road)

    def draw(self, objects):
        for obj in objects:
            if obj.image:
                self.screen.blit(obj.image, (obj.position.x, obj.position.y))
            else:
                obj.rectangular_shape()
                pygame.draw.rect(self.screen, (obj.colR, obj.colG, obj.colB), obj.rect)

    def update_objects(self, delta_time, tick):
        self.simulation.updatesimulation(delta_time, tick)
