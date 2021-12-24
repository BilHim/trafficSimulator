class Vertex:
    def __init__(self,coordinates,name):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.name = name

    def __hash__(self):
        return self.name

    def __eq__(self,othername):
        return othername == self.name

    def getPosition(self):
        return self.x,self.y