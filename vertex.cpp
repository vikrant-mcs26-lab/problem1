#include "include/vertex.hpp"

std::vector<int> find_vertex_cover(Graph *g){
    std::vector<Edge> edge_list = g -> get_edge_list();
    std::vector<int> vertex_covers;
    int minValue = g->numNodes + 1;

    for(int i = 0; i < (1 << g->numNodes); ++i){
        std::vector<int> subset;
        for(int j = 0; j < g->numNodes; ++j){
            if ((i & j) > 0){
                subset.emplace_back(j);
            }
        }
        if (subset.size() < minValue && check_vertex_cover(edge_list, subset)){
            vertex_covers = subset;
        }
    }

    return vertex_covers;
}

bool check_vertex_cover(std::vector<Edge> edge_list, std::vector<int> &vertex_cover){
    for(auto edge: edge_list){
        if(!contains(vertex_cover, edge.node_u) && !contains(vertex_cover, edge.node_v))
            return false;
    }
    return true;
}

bool contains(std::vector<int> &vertex_cover, int value){
    for(auto item: vertex_cover){
        if(item == value)
            return true;
    }
    return false;
}
