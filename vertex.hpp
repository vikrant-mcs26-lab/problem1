#include "graph.hpp"
#include <vector>

Graph find_vertex_cover(Graph *g){
    auto edge_list = g->get_edge_list();
    
    for(int i = 0; i < edge_list.size(); ++i){
        std::cout << edge_list[i].node_u << ", " << edge_list[i].node_v << std::endl;
    }
}

void check_vertex_cover(Graph *g, Graph *vertex_cover){

}
