import numpy as np
from trafficSimulator import *

sim = Simulation()

up = 7
l = 200
a = 10
b = 50
c = 20
d = 5
e = 80
f = 40

resolutions = [3,4,1,3,1,3,1]
indexCount = 0

UP=[(45, -180), (45, -250)]
LEFT=[(45, -180),(-50, -180)]
RIGHT=[(45, -180), (150, -180)]
DOWN=[(45, -180), (45, -100)]

C10_NORTH_SOUTH=[UP,DOWN]
C10_NORTH_EAST=[DOWN,RIGHT]
C10_NORTH_WEST=[DOWN,LEFT]

C10_EAST_WEST=[RIGHT,LEFT]
C10_EAST_SOUTH=[RIGHT,DOWN]

C10_WEST_SOUTH=[LEFT,DOWN]



nodes = {
    "C10" : [*C10_NORTH_SOUTH,*C10_EAST_WEST]
}

sim.create_roads([
    # main road down left to right - roads 0-6
    #*curve_road((-926,-215), (-860,-285), (-890,-240), resolutions[0]),     #0
    #*curve_road((-860, -285), (-770, -358), (-840, -320), resolutions[1]),  #1
    #((-770, -358), (-450, -430)),                                           #2
    #*curve_road((-450, -430), (-300, -455), (-340, -460),resolutions[3]),   #3
    #((-300, -455), (625, -450)),                                            #4
    #*curve_road((625, -450), (760, -430), (675, -450), resolutions[5]),     #5
    #((760, -430), (926, -380)),                                             #6
    # main road down right to left - roads 7-13
    #*curve_road( (-860,-285-up),(-926,-215-up), (-890,-240-up), resolutions[7]),     #7
    #*curve_road( (-770, -358-up),(-860, -285-up), (-840, -320-up), resolutions[8]),  #8
    #( (-450, -430-up),(-770, -358-up)),                                              #9
    #*curve_road( (-300, -455-up),(-450, -430-up), (-340, -460-up),resolutions[10]),  #10
    #((625, -450-up),(-300, -455-up)),                                                #11
    #*curve_road( (760, -430-up),(625, -450-up), (675, -450-up), resolutions[12]),    #12
    #( (926, -380-up),(760, -430-up)),                                                #13
    #*C10_NORTH_SOUTH
    *nodes["C10"]
])

def road(a):
    global indexCount
    res = range(indexCount,indexCount + resolutions[a])
    indexCount += resolutions[a]
    return res

#sim.create_gen({
    #'vehicle_rate': 150,
    #'vehicles': [
        #[50, {'path': [*road(0), *road(1), *road(2), *road(3), *road(4), *road(5), *road(6)]}],       #car's on main road down left to right
        #[50, {'path': [*road(13), *road(12), *road(11), *road(10), *road(9), *road(8), *road(7)]}]      #car's on main road down right to left
    #]
#})
# Start simulation
win = Window(sim)
win.zoom = 1
win.run(steps_per_update=5)
