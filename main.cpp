#include "include/graph.hpp"
#include "include/vertex.hpp"
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

    graph.print_graph();

    std::vector<int> vertex_cover = find_vertex_cover(&graph);

    graph.print_graph();
    for(auto item : vertex_cover){
        std::cout << item << ", ";
    }
    std::cout << std::endl;
    return 0;
}