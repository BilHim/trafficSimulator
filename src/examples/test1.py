from trafficSimulator import *

sim = Simulation()

lane_space = 3.5
intersection_size = 12
length = 100

# SOUTH, EAST, NORTH, WEST

# Intersection in
sim.add_segment(Segment([(lane_space/2, length+intersection_size/2), (lane_space/2, intersection_size/2)]))
sim.add_segment(Segment([(length+intersection_size/2, -lane_space/2), (intersection_size/2, -lane_space/2)]))
sim.add_segment(Segment([(-lane_space/2, -length-intersection_size/2), (-lane_space/2, -intersection_size/2)]))
sim.add_segment(Segment([(-length-intersection_size/2, lane_space/2), (-intersection_size/2, lane_space/2)]))
# Intersection out
sim.add_segment(Segment([(-lane_space/2, intersection_size/2), (-lane_space/2, length+intersection_size/2)]))
sim.add_segment(Segment([(intersection_size/2, lane_space/2), (length+intersection_size/2, lane_space/2)]))
sim.add_segment(Segment([(lane_space/2, -intersection_size/2), (lane_space/2, -length-intersection_size/2)]))
sim.add_segment(Segment([(-intersection_size/2, -lane_space/2), (-length-intersection_size/2, -lane_space/2)]))
# Straight
sim.add_segment(Segment([(lane_space/2, intersection_size/2), (lane_space/2, -intersection_size/2)]))
sim.add_segment(Segment([(intersection_size/2, -lane_space/2), (-intersection_size/2, -lane_space/2)]))
sim.add_segment(Segment([(-lane_space/2, -intersection_size/2), (-lane_space/2, intersection_size/2)]))
sim.add_segment(Segment([(-intersection_size/2, lane_space/2), (intersection_size/2, lane_space/2)]))
# Right turn
sim.add_segment(QuadraticCurve((lane_space/2, intersection_size/2), (lane_space/2, lane_space/2), (intersection_size/2, lane_space/2)))
sim.add_segment(QuadraticCurve((intersection_size/2, -lane_space/2), (lane_space/2, -lane_space/2), (lane_space/2, -intersection_size/2)))
sim.add_segment(QuadraticCurve((-lane_space/2, -intersection_size/2), (-lane_space/2, -lane_space/2), (-intersection_size/2, -lane_space/2)))
sim.add_segment(QuadraticCurve((-intersection_size/2, lane_space/2), (-lane_space/2, lane_space/2), (-lane_space/2, intersection_size/2)))
# Left turn
sim.add_segment(QuadraticCurve((lane_space/2, intersection_size/2), (lane_space/2, -lane_space/2), (-intersection_size/2, -lane_space/2)))
sim.add_segment(QuadraticCurve((intersection_size/2, -lane_space/2), (-lane_space/2, -lane_space/2), (-lane_space/2, intersection_size/2)))
sim.add_segment(QuadraticCurve((-lane_space/2, -intersection_size/2), (-lane_space/2, lane_space/2), (intersection_size/2, lane_space/2)))
sim.add_segment(QuadraticCurve((-intersection_size/2, lane_space/2), (lane_space/2, lane_space/2), (lane_space/2, -intersection_size/2)))

vg = VehicleGenerator({
    'vehicles': [
        (1, {'path': [0], 'v': 16.6})
        ]
    })
sim.add_generator(vg)



# v = Vehicle({'path': [0], 'x': 20, 'v':16.6})
# sim.add_vehicle(v)

# v = Vehicle({'path': [0]})
# sim.add_vehicle(v)

win = Window(sim)
win.run()
win.show()
