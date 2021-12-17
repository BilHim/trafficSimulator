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

sim.create_roads([
    ((55, 246),(49,-80)),
    ((49,-80),(45, -246)),
    ((35, -246),(45, 246)),
    #*curve_road((49,-80), (150,-190), (100,-200), resolution=n),
])

def road(a): return range(a, a+n)

#sim.create_gen({
    #'vehicle_rate': 150,
    #'vehicles': [
        #[50, {'path': [0,1]}],
        #[30, {'path': [0,*road(3)]}],
        #[50, {'path': [2]}],
    #]
#})
# Start simulation
win = Window(sim)
win.zoom = 1.5
win.run(steps_per_update=5)