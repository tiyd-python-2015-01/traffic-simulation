from car_movement import*
from car import Car

def test_accelerate_condition_car():
    car1 = Car(position=0)
    car2 = Car(position=40)
    car3 = Car(position=60)
    car4 = Car(position=80)
    car5 = Car(position=999)
    car_list = [car1, car2, car3, car4]

    assert accelerate_condition_car(car1, car_list) is False
    assert accelerate_condition_car(car2, car_list) == (60, 20)
    assert accelerate_condition_car(car3, car_list) == (80, 20)
    assert accelerate_condition_car(car4, car_list) is False
    assert accelerate_condition_car(car4, car_list) is False
