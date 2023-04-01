from scipy.spatial import distance
from scipy.interpolate import interp1d
from collections import deque
from numpy import arctan2, unwrap, linspace

class Segment:
    def __init__(self, points):
        self.points = points
        self.vehicles = deque()

        self.set_functions()
        

    def set_functions(self):
        # Point
        self.get_point = interp1d(linspace(0, 1, len(self.points)), self.points, axis=0)
        
        # Heading
        headings = unwrap([arctan2(
            self.points[i+1][1] - self.points[i][1],
            self.points[i+1][0] - self.points[i][0]
        ) for i in range(len(self.points)-1)])
        if len(headings) == 1:
            self.get_heading = lambda x: headings[0]
        else:
            self.get_heading = interp1d(linspace(0, 1, len(self.points)-1), headings, axis=0)

    def get_length(self):
        length = 0
        for i in range(len(self.points) -1):
            length += distance.euclidean(self.points[i], self.points[i+1])
        return length

    def add_vehicle(self, veh):
        self.vehicles.append(veh.id)

    def remove_vehicle(self, veh):
        self.vehicles.remove(veh.id)