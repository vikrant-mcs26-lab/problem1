import pathlib as path
import networkx as netx
import matplotlib.pyplot as plt
import argparse as ap
import glob

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

    def show_graph(self, save_dir):
        fig, axes = plt.subplots(nrows=1, ncols=2)
        save_path = path.Path(save_dir)

        axes[0].set_title("Original Graph")
        axes[1].set_title("Vertex Cover Graph")

        G = netx.Graph()
        G.add_nodes_from(self.vertices, color="green")
        G.add_edges_from(self.edges)
        netx.draw_shell(G, with_labels=True, ax=axes[0])
        
        VC = netx.Graph()
        VC.add_nodes_from(self.vertex_cover, color="green")
        VC.add_edges_from(self.vertex_cover_edges)
        netx.draw_shell(VC, with_labels=True, ax=axes[1])
        if save_path.is_dir():
            p = save_path.joinpath(self.vertex_file_path.stem + ".png")
            fig.savefig(p)


def parse_args() -> ap.Namespace[str, str, str] :
    parser = ap.ArgumentParser()

    parser.add_argument("--graph-path",type=str,required=True,help="Directory where graph files are stored")
    parser.add_argument("--vertex-cover-path",type=str,required=True,help="Directory where vertex cover files are stored")
    parser.add_argument("--save-dir",type=str,required=True,help="Directory to save resources")

    known_args, unknown = parser.parse_known_args()

    print(f"Found Unknown arguments: {unknown}")

    return known_args


def main():
    opts = parse_args()

    graph_path = path.Path(opts.graph_path)
    vertex_cover_path = path.Path(opts.vertex_cover_path)
    save_dir = path.Path(opts.save_dir)

    graph_files: list[path.Path] = None
    vertex_files: list[path.Path] = None

    if graph_path.exists() and graph_path.is_dir():
        graph_files = list(graph_path.glob("*.graph"))
    else:
        print("Please ensure --graph-path is a directory")
        return

    if vertex_cover_path.exists() and vertex_cover_path.is_dir():
        vertex_files = set(vertex_cover_path.glob("*.vertex_cover"))

    for i in range(len(graph_files)):
        graph = graph_files[i]
        vertex = vertex_cover_path.joinpath(graph.stem + ".vertex_cover")
        if not vertex in vertex_files:
            print(f"Vertex File Corresponding to {graph.stem} doesn't exist.\n"
                   f"Please run ./vertex {graph} {vertex.parent}"
                  )
            continue
        if not save_dir.is_dir():
            print("Save Directory doesn't exists. Creating One")
            save_dir.mkdir()
        g = Graph(graph, vertex)
        g.show_graph(save_dir)

if __name__ == "__main__":
    main()