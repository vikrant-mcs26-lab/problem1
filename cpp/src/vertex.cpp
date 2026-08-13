#include <graph.hpp>
#include <filesystem>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <chrono>

std::vector<int> find_vertex_cover(Graph *g);
bool check_vertex_cover(std::vector<Edge> edge_list, std::vector<int> &vertex_cover);
bool contains(std::vector<int> &vertex_cover, int value);
Graph* initialise_graph();
std::vector<Edge> graph_with_vertex_set(const std::vector<int> &vertex_cover, const Graph &g);
void save_graph(std::filesystem::path, std::vector<int>, std::vector<Edge>);

std::vector<int> find_vertex_cover(Graph *g){
    std::vector<Edge> edge_list = g -> get_edge_list();
    std::vector<int> vertex_covers;
    int minValue = g->numNodes + 1;

    for(int i = 0; i < (1 << g->numNodes); ++i){
        std::vector<int> subset;
        for(int j = 0; j <= g->numNodes; ++j){
            if ((i & (1 << j)) > 0){
                subset.emplace_back(j);
            }
        }
        if (subset.size() < minValue && check_vertex_cover(edge_list, subset)){
            vertex_covers = subset;
            minValue = subset.size();
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

Graph* initialise_graph(){
    int seed, number_of_nodes, number_of_edges;
    std::cout << "Seed: "; std::cin >> seed; 
    std::cout << "Number of Nodes: "; std::cin >> number_of_nodes;
    std::cout << "Number of Edges: "; std::cin >> number_of_edges;

    Graph *g = new Graph(number_of_nodes);
    g -> generate_graph(seed, number_of_edges);

    return g;
}

std::vector<Edge> graph_with_vertex_set(const std::vector<int> &vertex_cover, const Graph &g){
    std::vector<Edge> output;
    for(auto u : vertex_cover){
        for(auto v: vertex_cover){
            if (g.matrix[u][v] == 1){
                Edge e;
                e.node_u = u;
                e.node_v = v;
                output.emplace_back(e);
            }
        }
    }
    return output;
}

void save_graph(std::filesystem::path filename, std::vector<int> vector_set, std::vector<Edge> edges){
    std::fstream file(filename, std::ios::out);

    for (auto item : vector_set){
        file << item << " ";
    }
    file << "\n";

    for (auto item : edges){
        file << item.node_u << "," << item.node_v << "\n";
    }
    
    file.close();
}

int main(int argc, char **argv){
    if(argc < 2){
        std::cout << "This program needs atleast 1 arguments\n./vertex_cover <Graph File> [Output File]" << std::endl;
        return 1;
    }
    std::filesystem::path source(argv[1]);

    if(!std::filesystem::exists(source)){
        std::cout << "Please ensure path for Graph file is correct\n./vertex_cover <Graph File> [Output Directory]" << std::endl;
        return 1;
    }

    auto start_time = std::chrono::high_resolution_clock::now();

    Graph g;
    g.load_graph(source.string());

    std::vector<int> vertex_cover = find_vertex_cover(&g);
    std::vector<Edge> edges = graph_with_vertex_set(vertex_cover, g);

    std::cout << "Vertex Set = {";
    
    for(auto item : vertex_cover){
        std::cout << item << ", ";
    }
    
    std::cout << "}" << std::endl;
    
    auto end_time = std::chrono::high_resolution_clock::now();

    std::cout << std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count() << "\n";

    if(argc == 3){
        std::filesystem::path dest_folder(argv[2]);
        std::filesystem::path save_file_name = dest_folder / source.stem();
        save_file_name += ".vertex_cover";
        if(!std::filesystem::is_directory(dest_folder)){
            std::cout << "Please ensure path for Destination path is correct\n./vertex_cover <Graph File> [Output Directory]" << std::endl;
            return 1;
        }
        save_graph(save_file_name, vertex_cover, edges);
    }

    return 0;
}