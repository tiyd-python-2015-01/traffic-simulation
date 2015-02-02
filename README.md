Traffic Simulation by Joel Thompson and Zachary Huntington-Meath
At the Iron Yard January 2015.


Assumptions used in the simulation:
We created a program to simulate traffic. We made some assumptions that were
not in the original prompt. The traffic simulation starts by evenly
positioning thirty cars across a kilometer of road. Then it adjusts
speeds in several different ways. First, each car checks to see if the
car ahead is in its buffer zone. If it is not, then the car behind either speeds up by
its designated rate of acceleration, or it has a possibility of slowing down. If the car ahead is in the buffer zone, then the car behind checks to see if the car ahead is going faster. If it is, then the car behind will match the speed of the car in front of it. If the opposite is true, then the car behind will speed up or slow down as normal. Then the simulation moves the cars. When a car is going to move, it first checks to see if it is
going to hit the car in front of it. If it is, then the car will stop a preset distance (its car length + one meter) behind it. This will also set the car's speed to zero. We chose to do this because it would simulate an actual halt in traffic. If the
car does not hit the car in front of it, then it will move normally.


Requirements:
These may all be found in our requirements.txt.


How to use:
This simulation can be used many ways. We chose to run it in an Ipython
notebook. In the trial runner notebook, the run trials function may be used
to run the simulation as many times as desired. It has parameters to let you
choose number of simulations run, number of cars in a simulation, the length
of the road, how long the simulation runs for, and if you'd like to include
the commercial and agressive driver types used for nightmare mode. You may
also run one simulation by creating a Simulation object with the same attributes
other than number of trials. However Simulation defaults to normal mode
conditions, 30 cars, 1000 length road, and only the normal driver type.
