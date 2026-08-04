#include "graph.hpp"
#include <vector>

#ifndef VERTEX_HPP
#define VERTEX_HPP

std::vector<int> find_vertex_cover(Graph *g);
bool check_vertex_cover(std::vector<Edge> edge_list, std::vector<int> &vertex_cover);
bool contains(std::vector<int> &vertex_cover, int value);

#endif