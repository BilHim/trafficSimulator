import numpy as np
from trafficSimulator import *


sim = Simulation()

# up = 7
# l = 200
# a = 10
# b = 50
# c = 20
# d = 5
# e = 80
# f = 40

# resolutions = [3, 4, 1, 3, 1, 3, 1]
# indexCount = 0

# UP = [(45, -180), (45, -250)]
# LEFT = [(45, -180), (-50, -180)]
# RIGHT = [(45, -180), (150, -180)]
# DOWN = [(45, -180), (45, -100)]

# C10_NORTH_SOUTH = [UP, DOWN]
# C10_NORTH_EAST = [DOWN, RIGHT]
# C10_NORTH_WEST = [DOWN, LEFT]

# C10_EAST_WEST = [RIGHT, LEFT]
# C10_EAST_SOUTH = [RIGHT, DOWN]

# C10_WEST_SOUTH = [LEFT, DOWN]


# nodes = {
#     "C10": [*C10_NORTH_SOUTH, *C10_EAST_WEST]
# }

G = Graph()


sim.create_roads(G.getEdgesTuples())


# def road(a):
#     global indexCount
#     res = range(indexCount, indexCount + resolutions[a])
#     indexCount += resolutions[a]
#     return res


sim.create_gen({
    'vehicle_rate': 150,
    'vehicles': [
        [50, {'path': G.getPath("VL_1", "VL_5")}],
    ]
    # 50, {'path': [*road(13), *road(12), *road(11), *road(10), *road(9), *road(8), *road(7)]}]  # car's on main road down right to left
})

# Start simulation
win = Window(sim)
win.zoom = 1
win.run(steps_per_update=5)
