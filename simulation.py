from car import Car
from road import Road
from road import HardRoad
import random
import statistics as st


class Simulation:

    def __init__(self, road):

        self.total_cars = 0
        self.seconds = 0
        self.traffic = []
        self.road = road
        self.snapshots = []
        self.length = self.road.length

    def make_cars(self, n, desired_speed, speed):
        """appends self.traffic with n number of class Car"""
        counter = 0
        for a_car in range(n):
            a_car = Car(desired_speed, speed, self.road, counter)
            counter += 30
            self.traffic.append(a_car)

    def is_first_car(self, car):
        """Checks if is the farthest ahead at beginning"""
        if self.traffic.index(car) == len(self.traffic) - 1:
            return True

    def next_car(self, car):
        """returns the car in front of current car"""
        if self.is_first_car(car):
            return self.traffic[0]
        else:
            return self.traffic[self.traffic.index(car)+1]

    def is_end_of_loop(self, car):
        """Checks if the trailing car is towards the end of the loop"""
        if car.location > self.next_car(car).location:
            return True

    def nxt_loc(self, car):
        """gets the next location of a car"""
        return car.location + car.speed

    def loop_adjust(self, car):
        return 1000 - car.location + car.speed

    def end_of_loop_logic(self, car):
        """Checks collision dist for cars that are nearing 'end' of track"""
        if self.nxt_loc(car) - self.length > self.nxt_loc(self.next_car(car)):
            car.speed = self.next_car(car).speed
            car.location = self.next_car(car).location - 1
        elif self.next_car(car).location - self.loop_adjust(car) < 25:
            car.slow()
        else:
            car.acc()

    def normal_logic(self, car):
        """checks collision distance for cars"""

        if self.nxt_loc(car) > self.nxt_loc(self.next_car(car)):
            car.speed = self.next_car(car).speed
            car.location = self.next_car(car).location - 1
        elif self.next_car(car).location - car.location < 25:
            if car.speed > 2:
                car.speed -= 2
        else:
            car.acc()

    def check_for_cars(self):
        """"Checks if cars in front are too close"""
        for car in self.traffic:
            if self.is_end_of_loop(car):
                self.end_of_loop_logic(car)
            else:
                self.normal_logic(car)

    def acc_cars(self):
        """Increases cars speed if they are not at desired speed"""
        for car in self.traffic:
            if car.speed < self.optimal_speed:
                car.acc()

    def start(self):
        """runs all distance checks, acc, slowing and movement of all cars"""
        counter = 0
        while counter <= 60:
            car_locations = []
            counter += 1
            self.check_for_cars()
            self.random_slow(.10)
            for cars in self.traffic:
                car_locations.append((counter, cars.location))
                cars.go()
            self.snapshots.append(car_locations)

    def random_slow(self, percent_chance):
        """adds a 10 percent chance to randomly slow for all cars"""
        for car in self.traffic:
            if random.random() <= percent_chance:
                if car.speed > 1:
                    car.slow()


class HardMode(Simulation):

    def rand(self, threshold):
        """Sets the oddsf or a slowed car"""
        if random.random() < threshold:
            return True

    def random_slow(self):
        """Slows cars based on location"""

        for car in self.traffic:
            if 2000 > car.location > 999:
                if self.rand(.4):
                    car.slow()
            elif 4000 > car.location > 2999:
                if self.rand(.99):
                    car.slow()
            elif 6000 > car.location > 4999:
                if self.rand(.2):
                    car.slow()
            else:
                if self.rand(.1):
                    car.slow()

    def start(self):
        """runs all distance checks, acc, slowing and movement of all cars"""
        counter = 0
        while counter <= 600:
            car_locations = []
            counter += 1
            self.check_for_cars()
            self.random_slow()
            for cars in self.traffic:
                car_locations.append((counter, cars.location))
                cars.go()
            self.snapshots.append(car_locations)
