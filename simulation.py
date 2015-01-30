from car import Car
from road import Road
import random


class Simulation:
    """
    Responsibilities:
    - Creates new cars to be put on the road
    - Moves cars over time
    - Records traffic data

    Collaborators:
    - Has a road filled with cars
    """

    def __init__(self, car_list = []):
        self.road = Road()
        self.car_list = car_list

    def add_car(self, position=0):
        car = Car(position)
        self.road.place_car(car)
        self.car_list.append(car)
        return car

    def randomly_slow_down(self):
        return random.random() < .1

    def one_second(self):
        self.road.reset()
        for car in self.car_list:
            if self.randomly_slow_down():
                car.deccelerate()
            else:
                car.move()
            self.road.place_car(car)
