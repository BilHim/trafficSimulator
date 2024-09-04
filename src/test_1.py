from trafficSimulator import *

# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([
    ((300, 98), (0, 98)),
    ((0, 102), (300, 102)),
    ((180, 60), (0, 60)),
    ((220, 55), (180, 60)),
    ((300, 30), (220, 55)),
    ((180, 60), (160, 98)),
    ((158, 130), (300, 130)),
    ((0, 178), (300, 178)),
    ((300, 182), (0, 182)),
    ((160, 102), (155, 180))
    
])

sim.create_gen({
    'vehicle_rate': 60,
    'vehicles': [
        [1, {"path": [4, 3, 2]}],
        [1, {"path": [0]}],
        [1, {"path": [1]}],
        [1, {"path": [6]}],
        [1, {"path": [7]}]
    ]
})

# Start simulation
win = Window(sim)
win.offset = (-150, -110)
win.run(steps_per_update=5)