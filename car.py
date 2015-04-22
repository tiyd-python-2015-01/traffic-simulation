import random


class Car:
    def __init__(self,
                 position=0,
                 length=5,
                 acceleration=2,
                 deceleration=2,
                 deceleration_chance=0.1,
                 max_speed=33.33,
                 speed=20):
        self.position = position % 1000
        self.length = length
        self.acceleration = acceleration
        self.deceleration = deceleration
        self.deceleration_chance = deceleration_chance
        self.max_speed = max_speed
        self.car_following_distance = length * 4
        self.speed = speed

    def accelerate(self):
        """accelerates the speed by the car's acceleration, unless
        it's close enough to max_speed where it just switches to max speed"""
        if self.speed < (self.max_speed - self.acceleration):
            self.speed += self.acceleration
            return self.speed
        else:
            self.speed = self.max_speed
            return self.speed

    def decelerate(self):
        if self.speed - self.deceleration > 0:
            self.speed -= self.deceleration
        else:
            self.speed = 0
        # What if you decelerate below 0?

    def is_within_range_of_bumper(self, car_list):
        """If there's a car rear end anywhere in the following range of the
        current car's position, return False.  Otherwise True."""
        following_distance = self.position + self.car_following_distance
        for car in car_list:
            if self.position < car.back_of_car() < following_distance:
                return False
        return True

    def match_speed(self, car_list):
        """Get the speed of the car in front of you."""
        following_distance = self.position + self.car_following_distance
        for car in car_list:
            if self.position < car.back_of_car() < following_distance:
                return car.speed

    def back_of_car(self):
        return self.position - self.length

    def accelerate_condition(self):
        """If your speed is less than max speed, accelerate"""
        return self.speed < self.max_speed

    def random_deceleration(self):
        """checks to see if the car will randomly decelerate"""
        return random.random() < self.deceleration_chance

    def move(self):
        """moves the car based on original position and speed, sets
        new position for the car"""
        self.position = (self.position + self.speed) % 1000
        return self.position

    def will_hit_car(self, car_list):
        future_position = (self.position + self.speed) % 1000
        for car in car_list:
            if self.position < car.back_of_car() < future_position:
                return True
        return False

    def stop(self):
        """Makes car speed zero. Used to prevent running into a car."""
        self.speed = 0
