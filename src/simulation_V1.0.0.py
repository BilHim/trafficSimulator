import numpy as np
from trafficSimulator import *

sim = Simulation()

n = 15
l = 200
a = 10
b = 50
c = 20
d = 5
e = 80
f = 40

SOUTH_RIGHT = (a, b)
SOUTH_LEFT = (-a, b)
NORTH_RIGHT = (-a, -b)
NORTH_LEFT = (a, -b)

SOUTH_RIGHT_START = (a, l+b)
SOUTH_LEFT_START = (-a, l+b)
NORTH_RIGHT_START = (-a, -l-b)
NORTH_LEFT_START = (a, -l-b)

SOUTH_MIDDLE = (0, b-c)
NORTH_MIDDLE = (0, -b+c)

SOUTH_RIGHT_IN = (d, b-c+d)
SOUTH_RIGHT_OUT = (-d, b-c-d)
SOUTH_RIGHT_MIDDLE = (-a, b-2*c)
NORTH_RIGHT_MIDDLE = (-a, -b+2*c)
NORTH_RIGHT_OUT = (-d, -b+c+d)
NORTH_RIGHT_IN = (d, -b+c-d)

SOUTH_LEFT_IN = (-d, b-c+d)
SOUTH_LEFT_OUT = (d, b-c-d)
SOUTH_LEFT_MIDDLE = (a, b-2*c)
NORTH_LEFT_MIDDLE = (a, -b+2*c)
NORTH_LEFT_OUT = (d, -b+c+d)
NORTH_LEFT_IN = (-d, -b+c-d)

SOUTH_RIGHT_TURN = (f, b-c-c/2)
SOUTH_RIGHT_MERGE = (e, 5)

SOUTH_LEFT_TURN = (-f, b-c-c/2)
SOUTH_LEFT_MERGE = (-e, 5)

NORTH_RIGHT_TURN = (f, -b+c+c/2)
NORTH_RIGHT_MERGE = (e, -5)

NORTH_LEFT_TURN = (-f, -b+c+c/2)
NORTH_LEFT_MERGE = (-e, -5)

sim.create_roads([
    ((-532, 0), (532, 0)), # width total screen.
    ((0, -246), (0, 246)), # hight total screen.
  #  ((-400, -400), (400, 400)),
   
    #*curve_road(SOUTH_RIGHT, SOUTH_RIGHT_IN, (a, b-c/2), resolution=n),

])

def road(a): return range(a, a+n)

sim.create_gen({
    'vehicle_rate': 120,
    'vehicles': [
        [15, {'path': [0]}],
       # [3, {'path': [1]}],
        # [5, {'path': [1, 23, *road(26+12*n), 9]}],
    ]
})
# Start simulation
win = Window(sim)
win.zoom = 1.5
win.run(steps_per_update=5)