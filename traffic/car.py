import random


class Car():
    """
    Creates a 5m long car and adjusts its speed and location based on
    other cars around it. This car will randomly slow down by 10% (2 m/s).
    """

    def __init__(self):
        self.speed = 0
        self.size = 5
        self.location = 0

    def accelerate(self):
        if random.random() < .1:
            if self.speed > 1:
                self.speed -= 2
        else:
            if self.speed < 32:
                self.speed += 2
            else:
                self.speed

    def proximity(self, other_car):
        self.speed = other_car.speed

    def adjust_location(self):
        self.location += self.speed
        if self.location >= 999:
            self.location -= 999

    def close_proximity_check(self, other_car):
        if self.location >= 974:
            return True
        elif (other_car.location - self.location) <= 25:
            return True
        else:
            return False

    def collision_check(self, other_car):
        if self.location == (other_car.location - 4):
            self.speed = 0
            return True
