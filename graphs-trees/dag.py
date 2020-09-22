import networkx as nx

from matplotlib import pyplot as plt


class DAG(object):
    """We use networkx which is a python package used for the creation, manipulation,
    and study of the structure, dynamics & functions of complex networks.
    The complex networks we are talking about include but not limited to:
    --> Graphs
    --> Digraphs
    --> Multigraphs etc.
    """

    def __init__(self):
        self.graph = nx.DiGraph()
    
    def add_edges(self, edge):
        self.graph.add_edge(edge)
        if nx.is_directed_acyclic_graph():
            pass
        else:
            raise "Cannot insert a non-unique value. REMINDER: This is an acyclic graph."
            self.graph.remove_edge(edge)
    
    def add_set_of_edges(self, alist):
        self.graph.add_edges_from(alist)
        if nx.is_directed_acyclic_graph(self.graph):
            pass
        else:
            raise "This is an acyclic graph check your edges"
            self.graph.remove_edge(alist)
    
    def visualize_graph(self, location="."):
        """We use matplotlib for visualization.
        and the graph is stored as a png image.
        @CLI command: DAG.visualize_graph(home/img.png)
        """
        if self.graph == None:
            return "There is no graph. Add edged to create one for visualization."
        else:
            plt.tight_layout()
            nx.draw_networkx(self.graph, arrows=True, node_size=800)
            plt.savefig(location, format="png")
            plt.clf()
            return "Success!"


if __name__ == '__main__':
    graph = DAG()
    graph.add_set_of_edges([("root", "a"), ("a", "b"), ("b", "e"), ("e", "f"), ("g", "h")])
    graph.visualize_graph("graph1")
