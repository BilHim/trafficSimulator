
from trafficSimulator.edge import Edge
from trafficSimulator.point import Point


class Vertex:
    def __init__(self, coordinates, name, edges):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.name = name
        self.edge_L = edges['L']
        self.edge_R = edges['R']
        self.edge_U = edges['U']
        self.edge_D = edges['D']

    def __hash__(self):
        return self.name

    def __eq__(self, othername):
        return othername == self.name

    def getPosition(self):
        return self.x, self.y
