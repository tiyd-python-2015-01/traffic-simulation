import numpy as np
import random

class Car():
    """
    manages speed
    manages location
    its length - 5 meters long
    rising all the time if possible (2m/s) up to 33.3 m/sec
    if another car is w/i 20m, the car will match that car's speed until
    they have room again
    randomly slows down by 2m/s. 10 percent chance each second
    """

    def __init__(self):
        self.speed = 0
        self.size = 5
        self.location = 0

    def rising_speed(self):
        if random.random() < .1:
            self.speed -= 2
        else:
            if self.speed < 32:
                self.speed += 2
            else:
                self.speed


    def too_close_car(self, other_car):
        self.speed = other_car.speed

    def update_speed_to_loc(self):
        self.location += self.speed
        if self.location >= 999:
            self.location -= 999

    def is_car_too_close(self, other_car):
        if self.location >= 974:
            return True
        elif (other_car.location - self.location) <= 25:
            return True
        else:
            return False

    def did_hit_car(self, other_car):
        if self.location == (other_car.location - 4):
            self.speed = 0
            return True
