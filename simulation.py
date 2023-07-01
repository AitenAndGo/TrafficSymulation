import random

import map
from car import Car


class Simulation:
    def __init__(self):
        self.name = "Symulacja"
        self.resx = 100
        self.resy = 100
        self.mapsize = 7
        self.map = map.Map(self.resx, self.resy, self.mapsize)

        self.map.addRoad(0, 20, 99, 20, 50, 'r')
        self.map.addRoad(0, 40, 99, 40, 50, 'r')
        self.map.addRoad(0, 60, 99, 60, 50, 'r')
        self.map.addRoad(0, 80, 99, 80, 50, 'r')

        self.map.addRoad(0, 19, 99, 19, 50, 'l')
        self.map.addRoad(0, 39, 99, 39, 50, 'l')
        self.map.addRoad(0, 59, 99, 59, 50, 'l')
        self.map.addRoad(0, 79, 99, 79, 50, 'l')

        self.map.addRoad(21, 0, 21, 99, 50, 'u')
        self.map.addRoad(41, 0, 41, 99, 50, 'u')
        self.map.addRoad(61, 0, 61, 99, 50, 'u')
        self.map.addRoad(81, 0, 81, 99, 50, 'u')

        self.map.addRoad(20, 0, 20, 99, 50, 'd')
        self.map.addRoad(40, 0, 40, 99, 50, 'd')
        self.map.addRoad(60, 0, 60, 99, 50, 'd')
        self.map.addRoad(80, 0, 80, 99, 50, 'd')

        self.map.addCrossing(20, 20)
        self.map.addCrossing(20, 40)
        self.map.addCrossing(20, 60)
        self.map.addCrossing(20, 80)
        self.map.addCrossing(40, 20)
        self.map.addCrossing(40, 40)
        self.map.addCrossing(40, 60)
        self.map.addCrossing(40, 80)
        self.map.addCrossing(60, 20)
        self.map.addCrossing(60, 40)
        self.map.addCrossing(60, 60)
        self.map.addCrossing(60, 80)
        self.map.addCrossing(80, 20)
        self.map.addCrossing(80, 40)
        self.map.addCrossing(80, 60)
        self.map.addCrossing(80, 80)

        self.objects = []
        self.cars = []

    def generateCars(self, size):
        cars = 0
        used_positions = []  # lista wykorzystanych pozycji
        while True:
            x = random.randint(0, int(self.resx) - 1)
            y = random.randint(0, int(self.resy) - 1)
            # sprawdzamy, czy pozycja nie jest już wykorzystana i czy znajduje się na drodze
            if (x, y) not in used_positions and self.map.map[y][x].val is not None:
                is_valid_position = True
                # iterujemy po sąsiadach każdej już wykorzystanej pozycji
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        # jeśli pozycja jest już wykorzystana, oznaczamy, że nowa pozycja jest nieprawidłowa
                        if (x + dx, y + dy) in used_positions:
                            is_valid_position = False
                            break
                    if not is_valid_position:
                        break
                # jeśli nowa pozycja jest prawidłowa, dodajemy ją do listy i generujemy samochód
                if is_valid_position:
                    car = Car(x * self.mapsize, y * self.mapsize, self.map)
                    self.cars.append(car)
                    self.addObject(car.gameObject)
                    cars += 1
                    print((cars / size) * 100)
                    used_positions.append((x, y))
            # jeśli osiągnięto limit samochodów lub wykorzystano wszystkie pozycje, kończymy pętlę while
            if cars >= size or len(used_positions) >= self.resx * self.resy:
                break
        # wypisujemy informację o liczbie dodanych samochodów
        if cars < size:
            print("Nie udało się dodać wszystkich samochodów.")
        else:
            print(f"Dodano {cars} samochodów.")

    def addObject(self, obj):
        self.objects.append(obj)

    def updatesimulation(self, delta_time, tick):
        for cross in self.map.crossings:
            cross.update(tick)
        for car in self.cars:
            car.upgrade()
        for obj in self.objects:
            obj.update(delta_time)
