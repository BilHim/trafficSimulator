import networkx as nx
from trafficSimulator import *

V1 = Vertex((0, 0), 'a')
V2 = Vertex((200, 200), 'b')
E = Edge("a_b",(0,1),0.3,V1,V2)

G = nx.Graph()
#e = [('a', 'b', 0.3), ('b', 'c', 0.9), ('c', 'd', 0.5)]  name, indices, weight, coordinates
e = [(V1.name, V2.name, 0.3), ('b', 'c', 0.9), ('c', 'd', 0.5)]
G.add_weighted_edges_from(e)
print(nx.dijkstra_path(G, 'a', 'd'))

#a = (0, 0)
#b = (100, 0)
#c = (100, 100)
#d = (200, 100)

#V = { a, b,c, d }
#E = {((a,b,W),(b,c,W),(c,d,W),(a,c,W))}

#G = { V,E }

#GenrateRoads(G){
#   for e in G.E{
#        Road(a,b,W) -> ROADS[Road_A->B,Road_B->A,]
#   }
#
#
#
#}

#Roads = {
#A_B = {
#Road_A->B(a,b,W = num)      #index 0
#Road_B->A(b,a,W - inf)      #index 1
#},
#B_C = {
#Road_B->C(b,c,W = num)      #index 2
#Road_C->B(c,b,W - inf)      #index 3
#},
#C_D = {
#Road_C->D(b,c,W = num)      #index 4
#Road_D->C(c,b,W - inf)      #index 5
#},
#A_C = {
#Road_A->C(a,c,W = num)      #index 6
#Road_C->A(c,a,W - inf)      #index 7
#}
#}
# dfs - should return path or roads indexes..

# path = [Road_A->B,Road_B->C,Road_C->D] = [0,2,4]