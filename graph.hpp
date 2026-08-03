#include <vector>
#include <iostream>

typedef struct Edge{
    int u;
    int v;
} Edge;


class Graph {

public:
    int numNodes;
    int** matrix;

    Graph() {}
    Graph(int num);
    ~Graph();

    void load_graph();
    void save_graph();
    void generate_graph(int seed, int numberOfEdges);

    std::vector<Edge> get_edge_list;

    void print_graph();
};