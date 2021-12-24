class Edge:
    def __init__(self,name, indices, weight,vertices):
        self.indices = indices
        self.weight = weight
        self.road_show = vertices[0]
        self.road_hide = vertices[1]

    def getEdge(self):
        return self.road_show