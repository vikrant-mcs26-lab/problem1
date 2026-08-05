#include <graph.hpp>
#include <iostream>
#include <filesystem>
#include <cstdlib>

int main(int argc, char **argv){
    if (argc < 3){
        std::cout << "Usage: ./graph_generator <seed> <directory>" << std::endl;
        return 1;
    }

    std::filesystem::path directory = argv[2];
    int seed = atoi(argv[1]);
    
    if (!std::filesystem::is_directory(directory)){
        std::cout << "Directory does not exist." << std::endl;
        return 1;
    }

    directory = directory / std::filesystem::path("graph_");

    for(int i = 10; i <= 45; i += 5){
        Graph *g = new Graph(10);
        std::string path = directory.string() + std::to_string(i) + ".graph";
        g -> generate_graph(seed, i);
        g -> save_graph(path);
        delete g;
    }
    return 0;
}