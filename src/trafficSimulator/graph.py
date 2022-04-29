import networkx as nx
import os
import json


class Graph:
    def __init__(self):
        #self.edges = edges
        self.G = nx.DiGraph()
        self.edgeToIndex = []
        self.initG()

    def initG(self):
        f = open(f"{os.getcwd()}/src/trafficSimulator/Graph_Data.json")
        self.graphData = json.load(f)
        for node in self.graphData["nodes"]:
            self.G.add_node(node["name"], coordinates=node["coordinates"])
        for edge in self.graphData["edges"]:
            self.G.add_edge(edge["nodes"][0], edge["nodes"]
                            [1], name=edge["name"], weight=edge["weight"], nodes=edge["nodes"])

    def printEdges(self):
        for e in self.G.edges:
            print(
                f"""{self.G.get_edge_data(e[0], e[1])["name"]} -> from {e[0]}:({self.G.nodes.get(e[0])["coordinates"]["x"]},{self.G.nodes.get(e[0])["coordinates"]["y"]}) to {e[1]}:({self.G.nodes.get(e[1])["coordinates"]["x"]},{self.G.nodes.get(e[1])["coordinates"]["y"]})""")

    def getEdgesTuples(self):
        edgesTuples = []
        for e in self.G.edges:
            self.edgeToIndex.append(self.G.get_edge_data(e[0], e[1])["name"])
            edgesTuples.append(((self.G.nodes.get(e[0])["coordinates"]["x"], self.G.nodes.get(e[0])[
                               "coordinates"]["y"]), (self.G.nodes.get(e[1])["coordinates"]["x"], self.G.nodes.get(e[1])["coordinates"]["y"])))
        return edgesTuples

    def getPath(self, source, target):
        try:
            path = nx.dijkstra_path(self.G, source, target)
            return self.nodePathToIndexPath(path)
        except Exception as err:
            print(err)

    def reverseEdge(self, edgeName):
        for edge in self.graphData["edges"]:
            if(edge["name"] == edgeName):
                u = edge["nodes"][0]
                v = edge["nodes"][1]
                attrs = self.G.get_edge_data(u, v)
                self.G.remove_edge(u, v)
                self.G.add_edge(v, u, **attrs)

    def getEdgeIndex(self, edgeName):
        return self.edgeToIndex.index(edgeName)

    def nodePathToIndexPath(self, nodePath):
        pathIndex = []
        for index, node in enumerate(nodePath):
            if(index + 1 < len(nodePath)):
                name = self.G.get_edge_data(
                    nodePath[index], nodePath[index+1])["name"]
                pathIndex.append(self.getEdgeIndex(name))
        return pathIndex
