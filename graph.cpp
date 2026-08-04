#include "include/graph.hpp"
#include <cstdlib>
#include <iostream>

Graph::Graph(int num){
    this->numNodes = num;
    this->matrix = new int*[num];
    
    for (int i = 0; i < num; ++i){
        this -> matrix[i] = new int[num]{0};
    }
}

void Graph::generate_graph(int seed, int numberOfEdges){
    srand(seed);
    int i = 0;
    while (i < numberOfEdges){
        int u,v;
        u = rand() % numNodes;
        v = rand() % numNodes;
    
        if(matrix[u][v] == 1)
            continue;
        
        matrix[u][v] = 1;
        matrix[v][u] = 1;
        ++i;
    }
}

void Graph::save_graph(){
    
}

void Graph::load_graph(){

}

void Graph::print_graph(){
    for(int u = 0; u < numNodes; ++u){
        for(int v = 0; v < numNodes; ++v){
            std::cout << matrix[u][v] << "\t";
        }
        std::cout << std::endl;
    }
}

Graph::~Graph(){
    for(int i = 0; i < numNodes; ++i){
        delete[] matrix[i];
    }
    delete[] matrix;
}

std::vector<Edge> Graph::get_edge_list(){
    std::vector<Edge> edges;
    for(int u = 0; u < numNodes; ++u){
        for(int v = 0; v < numNodes; ++v){
            if (matrix[u][v] > 0){
                Edge e; 
                e.node_u = u;
                e.node_v = v;
                edges.push_back(e);
            }
        }
    }
    return edges; 
}


