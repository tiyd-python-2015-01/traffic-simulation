class Car:
    def __init__(self,
                 position=0,
                 length=5,
                 acceleration=2,
                 deceleration=2,
                 max_speed=33,
                 car_distance=20,
                 speed=0):
        self.position = position % 1000
        self.length = length
        self.acceleration = acceleration
        self.deceleration = deceleration
        self.max_speed = max_speed
        self.car_distance = car_distance
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
        """slows the car down by the set deceleration"""
        self.speed -= self.deceleration
        return self.speed

    def accelerate_condition_car(self, car_list):
        """If there's a car anywhere in the 25 spots ahead of the
        current car's position, return False.  Otherwise True"""
        new_list = [car.position for car in car_list]
        check = (
            [value for value in new_list if (
                self.position < value < ((self.position)+25))])
        if check:
            return False
        else:
            return True

    def accelerate_condition_speed(self):
        """If your speed is less than max speed, accelerate"""
        if self.speed < self.max_speed:
            return True
        else:
            return False

    def move(self):
        """moves the car based on original position and speed, sets
        new position for the car"""
        self.position += self.speed
        self.position %= 1000
        return self.position

    def move_check(self):
        """checks to see the position to which the car would move under
        current speed and acceleration"""
        current_position = self.position
        current_speed = self.speed
        future_position = current_position + current_speed
        return future_position
