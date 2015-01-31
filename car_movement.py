from car import Car

import random


def accelerate_condition_car(car, car_list):
    """If there's a car anywhere in the 25 spots ahead of the
    current car's position, return False.  Otherwise True"""
    check = (
        [x for x in car_list if (
            (car.position) < x.position < ((car.position)+25))])
    check1000 = (
        [x for x in car_list if (
            (car.position) < (x.position+1000) < ((car.position)+25))])

    if check:
        problem_car = check[0]
        return problem_car.position, problem_car.speed
    elif check1000:
        problem_car = check1000[0]
        return problem_car.position, problem_car.speed
    else:
        return False


def random_deceleration(chance=.1):
    """checks to see if the car will randomly decelerate"""
    if random.random() < chance:
        return True
    else:
        return False


def car_movement(car, car_list):
    car.move1()
    if accelerate_condition_car(car, car_list):
        problem_car = accelerate_condition_car(car, car_list)
        car.speed = problem_car[1]
    else:
        if random_deceleration():
            if car.speed > 2:
                car.decelerate()
        else:
            car.accelerate()
    car.move2()
    return car


def all_car_movement(car_list):
    for car in car_list:
        car = car_movement(car, car_list)
    return car_list


if __name__ == '__main__':
    car1 = Car(position=0)
    car2 = Car(position=40)
    car3 = Car(position=60)
    car4 = Car(position=80)
    car_list = [car1, car2, car3, car4]

    print(car_list[0].speed, car_list[0].position)
    print(car_list[1].speed, car_list[1].position)
    print(car_list[2].speed, car_list[2].position)
    print(car_list[3].speed, car_list[3].position)
    print("")
    all_car_movement(car_list)
    print(car_list[0].speed, car_list[0].position)
    print(car_list[1].speed, car_list[1].position)
    print(car_list[2].speed, car_list[2].position)
    print(car_list[3].speed, car_list[3].position)
    print("")
    car_movement(car1, car_list)
    print(car_list[0].speed, car_list[0].position)
    print(car_list[1].speed, car_list[1].position)
    print(car_list[2].speed, car_list[2].position)
    print(car_list[3].speed, car_list[3].position)
    print("")
    all_car_movement(car_list)
    print(car_list[0].speed, car_list[0].position)
    print(car_list[1].speed, car_list[1].position)
    print(car_list[2].speed, car_list[2].position)
    print(car_list[3].speed, car_list[3].position)
    car_movement(car1, car_list)
