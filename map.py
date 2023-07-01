from crossing import Crossing

# zrobić tak aby na aucie był kierunek i żeby zminiło kierunkek tylko przy zmianie kratki położenia


class Element:
    def __init__(self, value, direction, bo, cross, light):
        self.val = value
        self.dir = direction
        self.stop = bo
        self.iscross = cross
        self.light = light

    def __index__(self):
        return self.val


class Map:
    def __init__(self, width, height, size):
        self.map = [[Element(None, "", False, False, False) for y in range(height)] for x in range(width)]
        self.width = width
        self.height = height
        self.size = size
        self.roadsize = 0
        self.crossings = []

    def addCrossing(self, x, y):
        crossing = Crossing(x, y, self)
        self.crossings.append(crossing)

    def updateCrossing(self):
        for cross in self.crossings:
            self.crossings[cross].update()

    def addRoad(self, xp, yp, xk, yk, speed, direction):
        punkt_poczatkowy = (xp, yp)
        punkt_koncowy = (xk, yk)

        # oblicz różnicę między punktem końcowym i początkowym w obu wymiarach
        dx = punkt_koncowy[0] - punkt_poczatkowy[0]
        dy = punkt_koncowy[1] - punkt_poczatkowy[1]

        # iteruj przez każdy punkt między punktami początkowym i końcowym
        for i in range(dy + 1):
            for j in range(dx + 1):
                # oblicz współrzędne punktu na podstawie różnicy między punktami i przypisz wartość
                x = punkt_poczatkowy[0] + j
                y = punkt_poczatkowy[1] + i
                # print(x, y)
                self.map[y][x].val = speed
                self.map[y][x].dir = direction
                self.map[y][x].stop = False
                self.roadsize += 1
