"""A simple representation of graph using Adjacency matrix."""

class Graph:
    def __init__(self, num_vertex):
        self.adj_matrix = [[-1]*num_vertex for x in range(num_vertex)]
        self.numvertex = num_vertex
        self.vertices = {}
        self.verticeslist = [0]*num_vertex
    
    def set_vertex(self, vtx, id):
        if 0 <= vtx <= self.numvertex:
            self.vertices[id] = vtx
            self.verticeslist[vtx] = id
    
    def set_edge(self, frm, to, cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adj_matrix[frm][to] = cost
        # For directed graph, do not add this
        self.adj_matrix[to][frm] = cost
    
    def get_vertex(self):
        return self.verticeslist
    
    def get_edges(self):
        edges = []
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if (self.adj_matrix[i][j] != -1):
                    edges.append((self.verticeslist[i], self.verticeslist[j], self.adj_matrix[i][j]))
            return edges
    
    def get_matrix(self):
        return self.adj_matrix

G =Graph(6)
G.set_vertex(0,'a')
G.set_vertex(1,'b')
G.set_vertex(2,'c')
G.set_vertex(3,'d')
G.set_vertex(4,'e')
G.set_vertex(5,'f')
G.set_edge('a','e',10)
G.set_edge('a','c',20)
G.set_edge('c','b',30)
G.set_edge('b','e',40)
G.set_edge('e','d',50)
G.set_edge('f','e',60)
print("Vertices of Graph")
print(G.get_vertex())
print("Edges of Graph")
print(G.get_edges())
print("Adjacency Matrix of Graph")
print(G.get_matrix())