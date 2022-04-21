import numpy as np
from trafficSimulator import *


sim = Simulation()

G = Graph()

sim.create_roads(G.getEdgesTuples())

sim.create_gen({
    'vehicle_rate': 150,
    'vehicles': [
        [10, {'path': G.getPath("V_0_0_D", "V_0_2_U")}],
    ]
})

# Start simulation
win = Window(sim)
win.zoom = 1.5
win.run(steps_per_update=5)
