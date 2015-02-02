"""Car class

    Responsibilities
        -car length
        -speed
        -distance between other cars
        -starting position



"""

# creating a car and its functions
class Car(object):
##car will continue to accelerate (up to 120k/h) as long as it has room to do so
  def __init__(self, size, speed):
    self.size = (5 meters)
    self.starting_speed = (0, 0)
    #self.max_speed = (120kilometers/hr)

  def move(self):
    self.move(self.speed[0], self.speed[1])
    #self.accelerate( 2m/s unless they are within 10 meters of lead car)


  def set_speed(self, x, y):
    self.speed = x, y
    #random slow down of 2m/s
    car1 = Car()
    car1.set_speed(3,30)




#  def update_car_and_check_spacing(self, x_move, y_move):
#       def constrain(min, max, actual):
#            if actual < min:
#                return min, True
#            elif actual > max:
#                return max, True
#            else:
#                return actual, False



# moving car withing the set parameters
    for x in range():
#self.sleep(sleep car if it gets within 10 meters of lead car)
    time.sleep(0.025)
    car1.move()
    car2.move()
