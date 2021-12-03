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
    ((55, 246),(49,-80)),
    ((49,-80),(45, -246)),
    ((35, -246),(45, 246)),    
    *curve_road((49,-80), (150,-190), (100,-200), resolution=n), 
])

def road(a): return range(a, a+n)

sim.create_gen({
    'vehicle_rate': 150,
    'vehicles': [
        [50, {'path': [0,1]}],
        [30, {'path': [0,*road(3)]}],
        [50, {'path': [2]}],
    ]
})
# Start simulation
win = Window(sim)
win.zoom = 1.5
win.run(steps_per_update=5)