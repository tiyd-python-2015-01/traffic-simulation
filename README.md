# Traffic simulation

## Description

Analyze the behavior of drivers on a new road to determine the optimal speed
limits.

### Learning Objectives

* The use of NumPy
* Complex stochastic simulations
* Basic statistical methods

## About the Assignment

You are going to create a simulation of traffic on a road and find the optimal
speed limit for the road. In the normal mode below, this is for 1 kilometer of
road. We start by listing our assumptions. These will simplify the problem from
the real world.

### Assumptions

* Drivers want to go up to 120 km/hr.
* The average car is 5 meters long.
* Drivers want at least 4 car lengths between them and the next car.
* Drivers will accelerate 2 m/s up to their desired speed as long as they have
  room to do so.
* If another car is too close, drivers will match that car's speed until they
  have room again.
* If a driver would hit another car by continuing, they stop.
* Drivers will randomly (10% each second) slow by 2 m/s.
* This section of road will have a new car enter it every 2-6 seconds.
* This section of road is one lane going one way.

Given all this information, create a simulation of traffic on this road. Even
though the road is not circular in real life, you should treat it as such: cars
exiting the road start again at the beginning. This is to simulate a continuous
stream of traffic. When you start the simulation, add 30 cars to the road per
kilometer, evenly spaced. Then run the simulation for one minute to get a
continuous, randomized stream of traffic.

The optimal speed limit is one standard deviation above the mean speed.
For ease of drivers, this should be rounded down to an integer.

Your final report should have a graph of traffic over time, showing traffic
jams, as well as your recommendation for the speed limit. Add any plots that
back up your analysis.

[Here is an excellent example of a graph showing traffic jams.](https://en.wikipedia.org/wiki/Nagel%E2%80%93Schreckenberg_model#mediaviewer/File:Nagel-schreck_rho%3D0.35_p%3D0.3.png)

We have a 1 kilometer section of road being built and do not know what the
speed limit should be. Simulate 1 kilometer of road. As mentioned above, even
though this road is not circular, treat it as such in order to generate a
continuous flow of traffic.

![Road](road.png)

## Notes

This is incredibly similar to real work that a highway planner would do. Using
these tools should highlight how randomness can be used to solve many
real-world problems.

Your simulations may take quite some time to run. You should create smaller
simulations and make sure they are giving you reasonable answers before scaling
up.

Remember that one simulation is meaningless: you need many simulations for the
law of large numbers to matter.

This simulation currently has a few bugs which prevent it from being particularly
useful. It does demonstrate proper Monte Carlo methods, but my logic is flawed in 
getting all the car behaviors correct.

## Additional Resources

* Chapters 1 and 2 of [Monte Carlo Theory, Methods, and Examples](http://statweb.stanford.edu/~owen/mc/).
* [Traffic simulation on Wikipedia](https://en.wikipedia.org/wiki/Traffic_simulation).
