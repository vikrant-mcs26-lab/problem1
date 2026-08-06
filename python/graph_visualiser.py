import pathlib as path
import networkx as netx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, graph_file: str, vertex_file: str):
        self.edges: list[tuple[int,int]] = []
        self.vertices: set[int] = {}
        self.vertex_cover: set[int] = {}
        self.vertex_cover_edges: list[tuple[int,int]] = []

        self.graph_file_path = path.Path(graph_file)
        self.vertex_file_path = path.Path(vertex_file)

        with open(self.graph_file_path, 'r') as file:
            num_nodes = int(file.readline().strip())
            self.vertices = set(range(num_nodes))
            for line in file.readlines():
                split = line.strip().split(",")
                u = int(split[0])
                v = int(split[1])
                self.edges.append((u,v))

        with open(self.vertex_file_path, 'r') as file:
            vertices = file.readline().strip().split(" ")
            self.vertex_cover = {int(x) for x in vertices}
            for line in file.readlines():
                split = line.strip().split(",")
                u = int(split[0])
                v = int(split[1])
                self.vertex_cover_edges.append((u,v))

        print(self.vertices, self.vertex_cover, sep="\n")

    def show_graph(self, save_dir):
        fig, axes = plt.subplots(nrows=1, ncols=2)
        save_path = path.Path(save_dir)

        G = netx.Graph()
        G.add_nodes_from(self.vertices, color="green")
        G.add_edges_from(self.edges)
        netx.draw(G, with_labels=True, ax=axes[0])
        
        VC = netx.Graph()
        VC.add_nodes_from(self.vertex_cover, color="green")
        VC.add_edges_from(self.vertex_cover_edges, ax=axes[1])
        netx.draw(VC, with_labels=True)
        if save_path.is_dir():
            p = save_path.joinpath(self.vertex_file_path.stem + ".png")
            fig.savefig(p)

edges = 45

g = Graph(f"../cpp/resources/graphs/graph_{edges}.graph", f"../cpp/resources/vertex/graph_{edges}.vertex_cover")
g.show_graph("./resources")