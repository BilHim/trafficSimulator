from trafficSimulator import *

# Create simulation
sim = Simulation()

# Curve resolution
n = 15

# Add multiple roads
sim.create_roads([
    ((-10, 106), (290, 106)),
    ((-10, 102), (290, 102)),

    ((290, 98), (-10, 98)),
    ((290, 94), (80, 94)),
    ((80, 94), (-10, 94)),

    ((101, 90), (80, 94)),
    ((160, 90), (100, 90)),

    *curve_road((250, 10), (160, 90), (210, 90), resolution=n)
])

sim.create_gen({
    'vehicle_rate': 60,
    'vehicles': [
        [3, {"path": [0]}],
        [6, {"path": [1]}],
        
        [3, {"path": [3, 4]}],
        [6, {"path": [2]}],
   
        [1, {"path": [*range(7, 7+n), 6, 5, 4]}]

    ]
})


# Start simulation
win = Window(sim)
win.offset = (-145, -95)
win.zoom = 8
win.run(steps_per_update=5)