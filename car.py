class Car:
    """
    Responsibilities:
    - Travels on the Road
    - Can detect other cars
    - Tries to keeps 4 car lengths between them and other car
    - Accelerates 2 m/s up to desired speed as long as they have room
    - Randomly (10 percent chance) a second of slowing down by 2 m/s
    - max speed = 33.33 m/s
    - when cars collide, they stop

    """
    def __init__(self, position=0, current_speed=0):
        self.position = position
        self.current_speed = current_speed
        self.max_speed = 33  # all units of speed measurement in m/s
        self.acceleration = 2  # fixed acceleration amount
        self.length = 5

    def accelerate(self):
        """accelerates the car until it gets to max_speed"""
        if self.current_speed < self.max_speed - 2:
            self.current_speed += self.acceleration
        else:
            self.current_speed = self.max_speed

    def deccelerate(self):
        """deccelerates the car"""
        if self.current_speed > 2:
            self.current_speed -= self.acceleration
        else:
            self.current_speed = 0

    def collision(self):
        """Car stops on a collision"""
        self.current_speed = 0

    def move(self):
        self.position = (self.position + self.current_speed) % 1000
