import pathlib as path
import networkx as netx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, graph_file: str, vertex_file: str):
        self.edges: list[tuple[int,int]] = []
        self.vertices: set[int] = {}
        self.vertex_cover: set[int] = {}

        graph_file_path = path.Path(graph_file)
        vertex_file_path = path.Path(vertex_file)

        with open(graph_file_path, 'r') as file:
            num_nodes = int(file.readline().strip())
            self.vertices = set(range(num_nodes))
            for line in file.readlines():
                split = line.strip().split(",")
                u = int(split[0])
                v = int(split[1])
                self.edges.append((u,v))

        with open(vertex_file_path, 'r') as file:
            vertices = file.readline().strip().split(" ")
            self.vertex_cover = {int(x) for x in vertices}

    def show_graph(self):
        G = netx.Graph()
        G.add_nodes_from(self.vertices, color="green")
        G.add_nodes_from(self.vertex_cover, color="red")
        G.add_edges_from(self.edges)
        netx.draw(G)
        plt.show()


g = Graph("../cpp/resources/graphs/graph_45.graph", "../cpp/resources/vertex/graph_45.vertex_cover")
g.show_graph()