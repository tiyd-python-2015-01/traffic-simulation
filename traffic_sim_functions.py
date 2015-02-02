import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean, stdev

# traffic_sim_functions.py
# Alan Grissett
# alan.grissett@gmail.com

"""This script is a traffic simulation of a 7km long road.  The first, third,
fifth and seventh km are all straight stretches of road.  The other sections
have varying degrees of curves which may cause drivers to slow down more
frequently.  There are three types of drivers in the simulation.  Normal
drivers and agressive drivers both have 5m long vehicles, while commercial
drivers have 25m long vehicles.  Each type of driver has predetermined
attributes, such as max speed and acceleration rate."""

car_list = []


def build_car():
    """This function randomly returns one of three types of drivers"""
    standard = {"front": 5,
                "rear": 0,
                "speed": 0,
                "acceleration": 2,
                "max speed": 33.333,
                "spacing": 20,
                "slow chance": .1,
                "mean speed": 0,
                "type": "Standard"
                }
    aggressive = {"front": 5,
                  "rear": 0,
                  "speed": 0,
                  "acceleration": 5,
                  "max speed": 38.888,
                  "spacing": 15,
                  "slow chance": .05,
                  "mean speed": 0,
                  "type": "Aggressive"
                  }
    commercial = {"front": 25,
                  "rear": 0,
                  "speed": 0,
                  "acceleration": 1.5,
                  "max speed": 27.777,
                  "spacing": 100,
                  "slow chance": .1,
                  "mean speed": 0,
                  "type": "Commercial"
                  }
    choice_roll = np.random.random()
    if choice_roll <= .1:
        return aggressive
    elif .1 < choice_roll <= .25:
        return commercial
    else:
        return standard


def check_for_stop(index, car):
    """Checks to see if a car should stop.  A car stops when moving forward
    at it's current speed would cause it to collide with another car."""
    if not index:
        return ((car["front"] + car["speed"]) - 7000
                >= car_list[len(car_list)-1]["rear"])
    else:
        return car["front"] + car["speed"] >= (car_list[index-1]["rear"])


def check_max_speed(car):
    """Checks to see if a car is going at it's maximum speed.  If it is
    within one "acceleration" of reaching max then speed is set to max speed"""
    if car["max speed"] - car["speed"] < car["acceleration"]:
        car["speed"] = car["max speed"]
        return True
    else:
        return car["speed"] + car["acceleration"] >= car["max speed"]


def check_random_slowdown(car):
    """Generates a random number to see if a car will slow down for no
    reason"""
    return (np.random.random() <= (car["slow chance"] *
                                   get_road_modifier(car["front"]))
            and car["speed"] > 2)


def check_spacing(index, car):
    """Checks to see if a car is within it's spacing range.  If it is, then
    the car matches the speed of the car in front."""
    if not index:
        return ((car["front"] + car["spacing"]) - 7000
                >= car_list[len(car_list)-1]["rear"])
    else:
        return car["front"] + car["spacing"] >= car_list[index-1]["rear"]


def get_road_modifier(location):
    """Returns the slow down modifier for each km of the road."""
    if 1000 < location <= 2000:
        return 1.4
    elif 3000 < location <= 4000:
        return 2
    elif 5000 < location <= 6000:
        return 1.2
    else:
        return 1


def initialize_plot(iterations):
    """Initializes the live-update plot."""
    global axes
    global figure
    figure = plt.figure()
    axes = plt.axes(xlim=(0, 7000), ylim=(0, iterations))
    plt.show(block=False)


def main(prep_iterations, data_iterations, number_of_cars=30,
         live_update=False):
    """Launching function for the simulation.  Takes arguments for the number
    of iterations to proceed through before recording data, the number of
    iterations to record data for, and has an optional argument for the
    number of cars in the simulation.  The default number of cars is 240."""
    if live_update:
        initialize_plot(data_iterations)
    populate_road(number_of_cars)
    run_simulation(prep_iterations, data_iterations, live_update)
    return car_list


def next_second(iterations=0, record_data=False, live_update=False):
    """Updates the position and location of all cars currently on the road.
    If record_data is True, a moving mean of the car's speed is kept."""
    update_speeds()
    update_locations()

    if record_data:
        update_mean(iterations)
    if live_update:
        update_plot(iterations)


def populate_road(number_of_cars):
    """A function to generate any number of cars for use in the simulation.
    The default number of cars is 30"""
    iterations, next_car = 0, 0
    while len(car_list) < number_of_cars:
        if iterations == next_car:
            car_list.append(build_car())
            next_car += np.random.randint(2, 7)
        iterations += 1
        next_second()


def run_simulation(prep_iterations, data_iterations, live_update):
    """Runs the simulation for the specified number of iterations.  Prep
    iterations allow the flow of traffic to normalize after populating the
    road, while data iterations are the iterations for which data will be
    recorded"""
    for _ in range(prep_iterations):
        next_second()
    for iteration in range(1, data_iterations + 1):
        next_second(iteration, record_data=True, live_update=live_update)


def update_locations():
    """Updates the location of each car on the road."""
    for car in car_list:
        car["front"] += car["speed"]
        car["rear"] += car["speed"]

    if car_list[0]["front"] > 7000:
        wrap_front(car_list[0])
    if car_list[len(car_list)-1]["rear"] > 7000:
        wrap_rear(car_list[len(car_list)-1])


def update_mean(iterations):
    """Updates the moving mean for a car's speed."""
    if iterations > 1:
        for car in car_list:
            car["mean speed"] = ((iterations - 1) * car["mean speed"] +
                                 car["speed"]) / iterations
    else:
        for car in car_list:
            car["mean speed"] = car["speed"]


def update_plot(iteration):
    """Update method to blit the new scatter plot to the canvas after each
    iteration of the simulation."""
    for car in car_list:
        if car["type"] == "Standard":
            new_point = plt.scatter(car["front"], iteration, marker=".")
            axes.draw_artist(new_point)
        elif car["type"] == "Aggressive":
            new_point = plt.scatter(car["front"], iteration, marker=".",
                                    color="red")
            axes.draw_artist(new_point)
        else:
            new_point = plt.scatter(car["front"], iteration, marker=".",
                                    color="green")
            axes.draw_artist(new_point)
    figure.canvas.blit()
    figure.canvas.flush_events()


def update_speeds():
    """Updates the car's speed based on the rules of the simulation."""
    for index, car in enumerate(car_list):
        if check_for_stop(index, car):
            car["speed"] = 0
        elif check_spacing(index, car):
            if car["speed"] > car_list[index-1]["speed"]:
                car["speed"] = car_list[index-1]["speed"]
        elif check_random_slowdown(car):
            car["speed"] -= 2
        elif not check_max_speed(car):
            car["speed"] += 2
        validate_speed(car)


def validate_speed(car):
    """Validates that each car is going at most their maximum speed."""
    if car["speed"] > car["max speed"]:
        car["speed"] = car["max speed"]


def wrap_front(car):
    """Wraps the front of the car to the beginning of the road when the car
    passes the 7km mark, the back of the car may remain at the other side
    if the rear has not also passed the 7km mark.  Also removes the car from
    the front of the list and places it in the back to maintain order."""
    car["front"] -= 7000
    car_list.append(car_list.pop(0))


def wrap_rear(car):
    """Wraps the rear of the car to the beginning of the road once it has
    crossed the 7km mark"""
    car["rear"] -= 7000

if __name__ == '__main__':
    main(1000, 1000, number_of_cars=50, live_update=True)
