class Car:
    """
    Responsibilities:
    * sets car's position, length, acceleration rate, deceleration
    rate, max_speed, and the distance it wants to keep between other
    cars
    * keeps track of the car's speed
    * can accelerate and change its speed
    * can decelerate and change its speed
    * can move itself, changing its position based on speed


    """
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

    def move1(self):
        """moves the car based on original position and speed, sets
        new position for the car"""
        self.position += ((self.speed)*2/3)
        self.position %= 1000
        return self.position

    def move2(self):
        """moves the car based on original position and speed, sets
        new position for the car"""
        self.position += ((self.speed)/3)
        self.position %= 1000
        return self.position
