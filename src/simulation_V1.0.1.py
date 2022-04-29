import numpy as np
from trafficSimulator import *


sim = Simulation()

G = Graph()

sim.create_roads(G.getEdgesTuples())
# sim.create_roads([
#     ((466, -143), (526, -143)),
# ])

# TODO missing leaf nodes on the right of all rows 1-4.. need another node 17
sim.create_gen({
    'vehicle_rate': 100,
    'vehicles': [
        [80, {'path': G.getPath("V_0_2_U", "V_3_2_D")}],
        [15, {'path': G.getPath("V_1_0_D", "V_1_17_D")}],
    ]
})

# Start simulation
win = Window(sim)
win.zoom = 1.5
win.run(steps_per_update=5)
