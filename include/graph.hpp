#include <vector>
#include <iostream>

#ifndef GRAPH_HPP
#define GRAPH_HPP

typedef struct Edge{
    int node_u;
    int node_v;
} Edge;

void parse_line(int *, int *, std::string, int);

class Graph {

public:
    int numNodes;
    int** matrix;

    Graph() {}
    Graph(Graph &g);
    Graph(int num);
    ~Graph();

    void load_graph();
    void save_graph();
    void generate_graph(int seed, int numberOfEdges);

    std::vector<Edge> get_edge_list();

    void print_graph();
};

#endif