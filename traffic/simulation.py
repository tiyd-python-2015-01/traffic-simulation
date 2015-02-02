
class Simulation():
    """
    - Creates a simulation of 30 equidistant cars on a 1000m road
    - Checks to see if cars collide and if so, makes cars stop
    - Runs simulation for a 1 minute loop
    """

    def __init__(self):
        self.crash_count = 0

    def car_iterate(self, roadway, car):
        roadway.track[0, car.location] += 1
        return roadway

    def car_subtract(self, roadway, car):
        roadway.track[0, car.location] -= 0
        return roadway

    def drive_cars(self, roadway, cars):
        for car in cars:
            self.car_subtract(roadway, car)
            car.adjust_location()
            self.car_iterate(roadway, car)
        return roadway

    def driving_rules(self, cars):
        counter = 1
        for car in cars:
            if car.close_proximity_check(cars[counter]):
                car.proximity(cars[counter])
            if counter == (len(cars) - 1):
                counter = 0
            else:
                counter += 1
        return True

    def car_collision(self, cars):
        counter = 1
        for car in cars:
            if car.collision_check(cars[counter]):
                self.crash_count += 1
            if counter == (len(cars) - 1):
                counter = 0
            else:
                counter += 1

    def accelerate_cars(self, cars):
        for car in cars:
            car.accelerate()

    def metric_conversion(num):
        return num * (3600/1000)
