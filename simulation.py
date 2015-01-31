from car import Car
from road import Road
from car_movement import*

class Simulation:
    def __init__(self):
        car1 = Car(position=0)
        car2 = Car(position=30)
        car3 = Car(position=60)
        car4 = Car(position=90)
        car5 = Car(position=120)
        car6 = Car(position=150)
        car7 = Car(position=180)
        car8 = Car(position=210)
        car9 = Car(position=240)
        car10 = Car(position=270)
        car11 = Car(position=300)
        car12 = Car(position=330)
        car13 = Car(position=360)
        car14 = Car(position=390)
        car15 = Car(position=420)
        car16 = Car(position=450)
        car17 = Car(position=480)
        car18 = Car(position=510)
        car19 = Car(position=540)
        car20 = Car(position=570)
        car21 = Car(position=600)
        car22 = Car(position=630)
        car23 = Car(position=660)
        car24 = Car(position=690)
        car25 = Car(position=720)
        car26 = Car(position=750)
        car27 = Car(position=780)
        car28 = Car(position=810)
        car29 = Car(position=840)
        car30 = Car(position=870)
        self.car_list = (
        [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10,
        car11, car12, car13, car14, car15, car16, car17, car18, car19,
        car20, car21, car22, car23, car24, car25, car26, car27, car28,
         car29, car30])

        def sim_round(self):
            new_car_list = all_car_movement(self.car_list)
            positions = [car.position for car in new_car_list]
            speeds = [car.speed for car in new_car_list]
            print(positions)
            print(speeds)
