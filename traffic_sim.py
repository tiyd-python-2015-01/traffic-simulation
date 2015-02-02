from traffic.car import Car
from traffic.road import Road
from traffic.sim import Sim
import numpy as np
import matplotlib.pyplot as ply


def multiple_simulations(num_simulations=1000):
    output_car_speeds = np.array([]).reshape(0, 30)
    output_tracks = np.array(np.zeros((1, 1000)))

    for _ in range(num_simulations):
        track_results, car_speeds = one_full_simulation()
        output_car_speeds = np.vstack([output_car_speeds, [car_speeds]])
        output_tracks = np.append(output_tracks, track_results, axis=0)

    output_tracks = np.delete(output_tracks, 0, 0)
    return output_tracks, output_car_speeds


def one_full_simulation(lenth_of_time=60):

    car_list = build_car_classes()
    sim = Sim()

    for _ in range(lenth_of_time):
        output = one_second_turn(car_list, sim)

    car_speeds = [car.speed for car in car_list]
    return output, car_speeds


def one_second_turn(cars, simulation):
    the_road = Road()
    simulation.car_impact(cars)
    simulation.move_rules(cars)
    simulation.move_cars_on_road(the_road, cars)
    simulation.increase_car_speed(cars)

    return the_road.track


def build_car_classes(num_cars=30):
    car_list = []
    counter = 33
    for car in range(num_cars):
        car = Car()
        car.location += counter
        car_list.append(car)
        counter += 33
    return car_list


def final_report():

    track_results, speed = multiple_simulations()
    speed_mean = Sim.m_to_km_conversion(np.mean(speed))
    speed_std = Sim.m_to_km_conversion(np.std(speed))
    rec_speed = speed_mean + speed_std
    track_plotting(track_results)
    print('Standard Deviation: ',speed_std)
    print('Mean: ',speed_mean)

    return rec_speed


def track_plotting(track_results):
    x = track_results
    y = np.arange(1, 101)
    choice = 50
    colors = np.random.rand(choice)

    ply.imshow(x, cmap="Greys", interpolation="nearest", aspect='auto')
    ply.show()


print(final_report())
