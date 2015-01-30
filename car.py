from road import Road

class Car:
    def __init__(self,
             length=5,
             acceleration=2,
             deceleration=2,
             max_speed=33.33,
             car_distance=20,
             speed=20):
        self.length = length
        self.acceleration = acceleration
        self.deceleration = deceleration
        self.max_speed = max_speed
        self.car_distance= car_distance
        self.speed = speed

    def accelerate(self):
        if self.speed < (self.max_speed - self.acceleration):
            self.speed += self.acceleration
            return self.speed
        else:
            self.speed = self.max_speed
            return self.speed

    def decelerate(self):
        self.speed -= self.deceleration
        return self.speed

    def accelerate_condition_car(self, road):
        pass
        """If your speed is less than max speed and
        If the index of the car 20 in front of this one is empty,
        then accelerate"""

    def accelerate_condition_speed(self):
        if self.speed < self.max_speed:
            return True
        else:
            return False

        """If your speed is less than max speed and
        If the index of the car 20 in front of this one is empty,
        then accelerate"""

    def decelerate_condition(self, road):
        """If the index of any of the 20 indeces in front of the car
        is full, then decelerate"""
