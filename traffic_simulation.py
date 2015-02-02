"""TO DO: Still needs a lot of work with matplotlib, stats, reporting, and ipython notebook"""

import numpy as np
import matplotlib.pyplot as plt
from traffic.simulation import Simulation
from traffic.road import Road
from traffic.car import Car


def multiple_simulations(num_simulations=100):

    output_car_speeds = np.array([]).reshape(0, 30)
    output_tracks = np.array(np.zeros((1, 1000)))

    for _ in range(num_simulations):
        track_results, car_speeds = one_simulation()
        output_car_speeds = np.vstack([output_car_speeds, [car_speeds]])
        output_tracks = np.append(output_tracks, track_results, axis=0)

    output_tracks = np.delete(output_tracks, 0, 0)
    return output_tracks, output_car_speeds


def one_simulation(time=60):

    car_list = car_factory()
    sim = Simulation()

    for _ in range(time):
        output = loop(car_list, sim)

    car_speeds = [car.speed for car in car_list]
    return output, car_speeds


def loop(cars, simulation):

    the_road = Road()
    simulation.driving_rules(cars)
    simulation.car_collision(cars)
    simulation.drive_cars(the_road, cars)
    simulation.accelerate_cars(cars)
    return the_road.track


def car_factory(car_fleet=30):

    car_list = []
    counter = 33
    for car in range(car_fleet):
        car = Car()
        car.location += counter
        car_list.append(car)
        counter += 33
    return car_list


def reporting():

    track_results, speed = multiple_simulations()
    speed_mean = Simulation.metric_conversion(np.mean(speed))
    speed_std = Simulation.metric_conversion(np.std(speed))
    rec_speed = speed_mean + speed_std
    plotting(track_results)
    return rec_speed


def plotting(track_results):

    x = track_results
    plt.imshow(x, cmap="binary_r", interpolation="gaussian")
    plt.show()


reporting()
