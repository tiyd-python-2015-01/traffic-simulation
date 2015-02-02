import random


class Car:
    """
    Responsibilites:
    Can control it's speed, can tell if a car is too close, and can stop
    at a certain point.
    """

    def __init__(self, position):
        self.max_speed = 33.33
        self.speed = 0
        self.size = 5
        self.acceleration = 2
        self.space = 20
        self.back = position
        self.style = "Generic sedan"
        self.slow_chance = 0.1

    def __str__(self):
        return self.style

    def __repr__(self):
        return self.__str__()

    def speed_up(self):
        self.speed += self.acceleration

    def slow_down(self):
        self.speed -= self.acceleration

    def move(self, road_length):
        self.back = (self.back + self.speed) % road_length

    def set_speed(self, speed):
        self.speed = speed

    def check_buffer(self, previous_car):
        if (self.back + 20 + self.size - 1) >= previous_car.back:
            return True
        else:
            return False

    def set_position(self, position):
        self.back = position

    def set_slow_chance(self, chance):
        self.slow_chance = chance


class Aggressive(Car):

    def __init__(self, position):
        self.max_speed = 38.89
        self.acceleration = 5
        self.space = 15
        self.slow_chance = 0.05
        self.back = position
        self.style = "Sports car"
        self.speed = 0
        self.size = 5


class Commercial(Car):

    def __init__(self, position):
        self.max_speed = 27.78
        self.acceleration = 1.5
        self.space = 100
        self.slow_chance = 0.1
        self.size = 25
        self.back = position
        self.speed = 0
        self.style = "Mac Truck"
