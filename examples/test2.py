import trafficSimulator as ts

sim = ts.Simulation()

# sim.create_segment((0, 0), (50, 0))
sim.create_quadratic_bezier_curve((0, 0), (50, 0), (50, 50))
sim.create_vehicle(path=[0])

win = ts.Window(sim)
win.show()
