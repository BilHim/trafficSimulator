import numpy as np
from trafficSimulator import *


sim = Simulation()

G = Graph()

sim.create_roads(G.getEdgesTuples())

sim.create_gen({
    'vehicle_rate': 150,
    'vehicles': [
        [50, {'path': G.getPath("VL_1", "VL_5")}],
    ]
})

# Start simulation
win = Window(sim)
win.zoom = 1
win.run(steps_per_update=5)
