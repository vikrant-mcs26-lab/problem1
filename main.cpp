#include "graph.hpp"
#include <iostream>

void initialise_graph(Graph* g){
    int seed, number_of_nodes, number_of_edges;
    std::cout << "Seed: "; std::cin >> seed; 
    std::cout << "Number of Nodes: "; std::cin >> number_of_nodes;
    std::cout << "Number of Edges: "; std::cin >> number_of_edges;

    *g = Graph(number_of_nodes);
    g -> generate_graph(seed, number_of_edges);
}

int main(){
    Graph graph;
    initialise_graph(&graph);
    std::vector<Edge> e = graph.get_edge_list();


}