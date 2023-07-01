import copy

import engine


class Crossing:
    def __init__(self, x, y, mapa):
        self.position = engine.Vector(x, y)
        self.map = mapa
        self.roads_coppy = [self.map.map[self.position.y][self.position.x - 1],
                            self.map.map[self.position.y + 1][self.position.x + 1],
                            self.map.map[self.position.y - 1][self.position.x + 2],
                            self.map.map[self.position.y - 2][self.position.x]].copy()
        self.roads = copy.deepcopy(self.roads_coppy)
        self.roads_coppy[0].iscross = True
        self.roads_coppy[1].iscross = True
        self.roads_coppy[2].iscross = True
        self.roads_coppy[3].iscross = True
        self.roads_coppy[0].light = True
        self.roads_coppy[1].light = True
        self.roads_coppy[2].light = True
        self.roads_coppy[3].light = True
        self.roads_coppy[0].stop = True
        self.roads_coppy[1].stop = True
        self.roads_coppy[2].stop = True
        self.roads_coppy[3].stop = True
        self.lightdir = 0

    def update(self, tick):
        gotime = tick % (60 * 8)
        # print(gotime)
        orange = -1
        if gotime == 0:
            # print("green")
            self.changelights(self.lightdir)
            self.lightdir += 1
            if self.lightdir == 4:
                self.lightdir = 0
        elif gotime == 60 * 5:
            # print("orange")
            self.changelights(orange)

    def changelights(self, light):
        # na razie tylko w jedna strone
        #
        #   ###  ###
        #   ###  ###
        # <-----------
        # ----------->
        #   ###  ###
        #   ###  ###
        crossing_np = [self.map.map[self.position.y - 1][self.position.x],
                       self.map.map[self.position.y - 1][self.position.x + 1],
                       self.map.map[self.position.y][self.position.x],
                       self.map.map[self.position.y][self.position.x + 1]]
        # crossing_np = map_np[19:21, 19:21]
        road1 = self.map.map[int(self.position.y)][int(self.position.x) - 1]
        road2 = self.map.map[self.position.y + 1][int(self.position.x) + 1]
        road3 = self.map.map[self.position.y - 1][int(self.position.x) + 2]
        road4 = self.map.map[self.position.y - 2][int(self.position.x)]

        if light == -1:
            road1.stop = True
            road2.stop = True
            road3.stop = True
            road4.stop = True

            road1.iscross = True
            road2.iscross = True
            road3.iscross = True
            road4.iscross = True
        elif light == 0:
            road1.stop = False
            road3.stop = False
            road1.iscross = False
            road3.iscross = False

            crossing_np[0].dir = 'l'
            crossing_np[1].dir = 'l'
            crossing_np[2].dir = 'r'
            crossing_np[3].dir = 'r'

            crossing_np[0].val = int(self.roads[2].val)
            crossing_np[1].val = int(self.roads[2].val)
            crossing_np[2].val = int(self.roads[0].val)
            crossing_np[3].val = int(self.roads[0].val)

        elif light == 1:
            # print("light 1")

            road2.stop = False
            road4.stop = False
            road2.iscross = False
            road4.iscross = False

            crossing_np[0].dir = 'd'
            crossing_np[1].dir = 'u'
            crossing_np[2].dir = 'd'
            crossing_np[3].dir = 'u'

            crossing_np[0].val = int(self.roads[3].val)
            crossing_np[1].val = int(self.roads[1].val)
            crossing_np[2].val = int(self.roads[3].val)
            crossing_np[3].val = int(self.roads[1].val)

        elif light == 2:
            # print("light 1")

            road2.stop = False
            road4.stop = False
            road2.iscross = False
            road4.iscross = False
            road1.stop = False
            road3.stop = False
            road1.iscross = False
            road3.iscross = False

            crossing_np[0].dir = 'l'
            crossing_np[1].dir = 'u'
            crossing_np[2].dir = 'd'
            crossing_np[3].dir = 'r'

            crossing_np[0].val = int(self.roads[3].val)
            crossing_np[1].val = int(self.roads[1].val)
            crossing_np[2].val = int(self.roads[3].val)
            crossing_np[3].val = int(self.roads[1].val)

        elif light == 3:
            # print("light 1")

            road2.stop = False
            road1.stop = False
            road2.iscross = False
            road1.iscross = False

            crossing_np[0].dir = 'l'
            crossing_np[1].dir = 'l'
            crossing_np[2].dir = 'd'
            crossing_np[3].dir = 'u'

            crossing_np[0].val = int(self.roads[3].val)
            crossing_np[1].val = int(self.roads[1].val)
            crossing_np[2].val = int(self.roads[3].val)
            crossing_np[3].val = int(self.roads[1].val)
