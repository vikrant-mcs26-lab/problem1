#include <graph.hpp>
#include <iostream>
#include <filesystem>

int main(int argc, char **argv){
    if (argc < 2){
        std::cout << "Usage: ./graph_generator <directory>" << std::endl;
        return 1;
    }

    std::string directory = argv[1];

    if (directory.back() == '/'){
        directory.pop_back();
    }

    if (!std::filesystem::is_directory(directory)){
        std::cout << "Directory does not exist." << std::endl;
        return 1;
    }

    for(int i = 10; i <= 45; i += 5){
        Graph *g = new Graph(10);
        g -> generate_graph(1, i);
        g -> save_graph(std::string(argv[1]) + "/graph_" + std::to_string(i) + ".v");
        delete g;
    }
    return 0;
}