import numpy as np
from trafficSimulator import *

sim = Simulation()

# Play with these
n = 15
a = 2
b = 20
c = 5
r = 10
l = 300

# Nodes
WEST_RIGHT_START = (-b-l, a-c)
WEST_LEFT_START =	(-b-l, -a-c)

SOUTH_RIGHT_START = (a-c, b+l)
SOUTH_LEFT_START = (-a-c, b+l)

EAST_RIGHT_START = (b+l, -a+c)
EAST_LEFT_START = (b+l, a+c)

NORTH_RIGHT_START = (-a+c, -b-l)
NORTH_LEFT_START = (a+c, -b-l)

WEST_RIGHT = (-b, a-c)
WEST_LEFT =	(-b, -a-c)

SOUTH_RIGHT = (a-c, b)
SOUTH_LEFT = (-a-c, b)

EAST_RIGHT = (b, -a+c)
EAST_LEFT = (b, a+c)

NORTH_RIGHT = (-a+c, -b)
NORTH_LEFT = (a+c, -b)

WEST = (-r, c)
SOUTH = (c, r)
EAST = (r, -c)
NORTH = (-c, -r)

# Roads
WEST_INBOUND = (WEST_RIGHT_START, WEST_RIGHT)
SOUTH_INBOUND = (SOUTH_RIGHT_START, SOUTH_RIGHT)
EAST_INBOUND = (EAST_RIGHT_START, EAST_RIGHT)
NORTH_INBOUND = (NORTH_RIGHT_START, NORTH_RIGHT)

WEST_OUTBOUND = (WEST_LEFT, WEST_LEFT_START)
SOUTH_OUTBOUND = (SOUTH_LEFT, SOUTH_LEFT_START)
EAST_OUTBOUND = (EAST_LEFT, EAST_LEFT_START)
NORTH_OUTBOUND = (NORTH_LEFT, NORTH_LEFT_START)

WEST_LEFT_TURN = (NORTH, WEST_LEFT)
SOUTH_LEFT_TURN = (WEST, SOUTH_LEFT)
EAST_LEFT_TURN = (SOUTH, EAST_LEFT)
NORTH_LEFT_TURN = (EAST, NORTH_LEFT)

WEST_RIGHT_TURN = curve_road(WEST_RIGHT, WEST, (WEST[0], WEST_RIGHT[1]), resolution=n)
SOUTH_RIGHT_TURN = curve_road(SOUTH_RIGHT, SOUTH, (SOUTH_RIGHT[0], SOUTH[1]), resolution=n)
EAST_RIGHT_TURN = curve_road(EAST_RIGHT, EAST, (EAST[0], EAST_RIGHT[1]), resolution=n)
NORTH_RIGHT_TURN = curve_road(NORTH_RIGHT, NORTH, (NORTH_RIGHT[0], NORTH[1]), resolution=n)

WEST_SOUTH = curve_road(WEST, SOUTH, (WEST[0], SOUTH[1]), resolution=n)
SOUTH_EAST = curve_road(SOUTH, EAST, (EAST[0], SOUTH[1]), resolution=n)
EAST_NORTH = curve_road(EAST, NORTH, (EAST[0], NORTH[1]), resolution=n)
NORTH_WEST = curve_road(NORTH, WEST, (WEST[0], NORTH[1]), resolution=n)

sim.create_roads([
    WEST_INBOUND,
    SOUTH_INBOUND,
    EAST_INBOUND,
    NORTH_INBOUND,

    WEST_OUTBOUND,
    SOUTH_OUTBOUND,
    EAST_OUTBOUND,
    NORTH_OUTBOUND,

    WEST_LEFT_TURN,
    SOUTH_LEFT_TURN,
    EAST_LEFT_TURN,
    NORTH_LEFT_TURN,

    *WEST_RIGHT_TURN,
    *SOUTH_RIGHT_TURN,
    *EAST_RIGHT_TURN,
    *NORTH_RIGHT_TURN,

    *WEST_SOUTH,
    *SOUTH_EAST,
    *EAST_NORTH,
    *NORTH_WEST
])

def road(a): return range(a, a+n)

sim.create_gen({
    'vehicle_rate': 30,
    'vehicles': [
        [2, {'path': [0, *road(12), *road(12+4*n), 10, 6]}],
        [1, {'path': [0, *road(12), 9, 5]}],
        [1, {'path': [0, *road(12), *road(12+4*n), *road(12+5*n), 11, 7]}],

        [2, {'path': [1, *road(12+n), *road(12+5*n), 11, 7]}],
        [1, {'path': [1, *road(12+n), 10, 6]}],
        [1, {'path': [1, *road(12+n), *road(12+5*n), *road(12+6*n), 8, 4]}],

        [2, {'path': [2, *road(12+2*n), *road(12+6*n), 8, 4]}],
        [1, {'path': [2, *road(12+2*n), 11, 7]}],
        [1, {'path': [2, *road(12+2*n), *road(12+6*n), *road(12+7*n), 9, 5]}],

        [2, {'path': [3, *road(12+3*n), *road(12+7*n), 9, 5]}],
        [1, {'path': [3, *road(12+3*n), 8, 4]}],
        [1, {'path': [3, *road(12+3*n), *road(12+7*n), *road(12+4*n), 10, 6]}],

    ]
})

# Start simulation
win = Window(sim)
win.zoom = 10
win.run(steps_per_update=5)