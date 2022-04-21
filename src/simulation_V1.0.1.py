import numpy as np
from trafficSimulator import *


sim = Simulation()

G = Graph()

sim.create_roads(G.getEdgesTuples())
sim.create_roads([
    ((466, -143), (526, -143)),
])

sim.create_gen({
    'vehicle_rate': 10,
    'vehicles': [
        [2, {'path': G.getPath("V_0_0_U", "V_1_3_D")}],
    ]
})

# Start simulation
win = Window(sim)
win.zoom = 1.5
win.run(steps_per_update=5)
