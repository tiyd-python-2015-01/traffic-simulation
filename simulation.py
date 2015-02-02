from car import Car
from road import Road
from road import HardRoad
import random
import statistics as st

class Simulation:

    def __init__(self,road):

        self.total_cars = 0
        self.seconds = 0
        self.traffic = []
        self.road = road
        self.snapshots = []

    def make_cars(self,n,desired_speed,speed):
        """appends self.traffic with n number of class Car"""
        counter = 0
        for a_car in range(n):
            a_car = Car(desired_speed,speed,self.road,counter)
            counter += 30
            self.traffic.append(a_car)

    def is_first_car(self,car):
        if self.traffic.index(car) == len(self.traffic) -1:
            return True

    def next_car(self, car):
        """returns the car in front of current car"""
        if self.is_first_car(car):
             return self.traffic[0]
        else:
             return self.traffic[self.traffic.index(car)+1]

    def is_end_of_loop(self,car):
        if car.location > self.next_car(car).location:
            return True

    def nxt_loc(self,car):
        """gets the next location of a car"""
        return car.location + car.speed

    def check_for_cars(self):
        """"Checks if cars in front are too close"""
        for car in self.traffic:
            if self.is_end_of_loop(car):
               if self.nxt_loc(car) - self.road.length > self.nxt_loc(self.next_car(car)):
                   car.speed = self.next_car(car).speed
                   car.location = self.next_car(car).location -1
               else:
                   car.acc()
            else:
                if self.nxt_loc(car) > self.nxt_loc(self.next_car(car)):
                    car.speed = self.next_car(car).speed
                    car.location = self.next_car(car).location -1
                elif self.next_car(car).location - car.location  < 25:
                    if car.speed > 2:
                        car.speed -= 2
                else:
                    car.acc()


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
                car_locations.append((counter,cars.location))
                cars.go()
            self.snapshots.append(car_locations)




    def random_slow(self,percent_chance):
        """adds a 10 percent chance to randomly slow for all cars"""
        for car in self.traffic:
            if random.random() <= percent_chance:
                if car.speed > 1:
                    car.slow()



road2 = Road()
simulation2 = Simulation(road2)
simulation2.make_cars(30,33,0)
simulation2.start()


class HardMode(Simulation):

    def random_slow_logic(self):
        if  2000 > car.location > 999:
            return random_slow(.4)
        elif 4000 > car.location > 2999:
            return random_slow(.99)
        elif 6000 > car.location > 4999:
            return random_slow(.2)
        else:
            return random_slow()


    def start(self):
        """runs all distance checks, acc, slowing and movement of all cars"""
        counter = 0
        while counter <= 600:
            car_locations = []
            counter += 1
            self.check_for_cars()
            self.random_slow_logic()
            for cars in self.traffic:
                car_locations.append((counter,cars.location))
                cars.go()
            self.snapshots.append(car_locations)

road = Road
simulation = Simulation(road)
simulation.make_cars(30,30,0)
simulation.start()

print(simulation.snapshots)
