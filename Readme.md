# Project Structure
```
├── build/
├── cpp/
├── python/
└── resources/
```

- `build` directory contains precompiled binaries for linux. 
- `cpp` directory contains C/C++ Source code for Graph Generation and Vertex Cover Algorithms.
- `python` directory contains Python source code for visualisation of Graphs.
- `resources` directory contains input/output files of various programs.
    - `graph_generation` generates `*.graph` files, which serves as input to `vertex` and produces `*.vertex_cover` files. Both `.graph` and `.vertex_cover` file serves as input to `graph_visualiser.py` which produces `png` files as output. All of these files are stored in `resources` directory. 

# Compiling
## Dependencies
- CMake (Version 3.16+)
- GNU C Compiler (C++ Std 17)
- Python (Version 3.9+)

First clone the project and open terminal in it before proceeding with the next steps.

Note: There instructions are for Unix like Operating system. Tested on Fedora 44. 

```bash
git clone https://github.com/vikrant-mcs26-lab/problem1.git
cd problem1
```
## C++ Project
Run these commands in root directory of project (i.e. problem1) to compile c++ project.
```bash
mkdir build
cd ./build
cmake ..
cmake --build .
```

## Python Project
In the root directory of project (i.e. problem1), run following commands to setup python 
```bash
python -m venv venv
source venv/bin/activate
pip install -r ./python/requirement.txt
```

# Instruction to Run

## Introduction to Executables

In `build` directory, you will find two binaries, `graph_generator` and `vertex`.
```
./graph_generator <seed> <directory>
    seed: Required 
            Seed for Pseudo Random Number Generator
    directory: Required
            Directory in which Graphs will be stored
```

```
./vertex <graph> [directory]
    graph: Required
            Path to graph File
    directory: Optional
            If passed, result would be stored in a vertex_cover file in the specified directory. 
```

Another executable is present in `python` directory.

```
graph_visualiser.py [-h] --graph-path GRAPH_PATH --vertex-cover-path VERTEX_COVER_PATH --save-dir SAVE_DIR

options:
  -h, --help            show this help message and exit
  --graph-path GRAPH_PATH
                        Directory where graph files are stored
  --vertex-cover-path VERTEX_COVER_PATH
                        Directory where vertex cover files are stored
  --save-dir SAVE_DIR   Directory to save resources
```

## Executing
First generate graphs with `graph_generator`. Run the following command from the root directory of the project. This would generate 8 graphs with 10 nodes and edges between 10 and 45. 
```bash
./build/graph_generator 101 ./resources/graphs
```

To find the vertex cover of these graphs, run `vertex` binary. 
```bash
./build/vertex ./resources/graphs/graph_10.graph ./resources/vertex
./build/vertex ./resources/graphs/graph_15.graph ./resources/vertex
./build/vertex ./resources/graphs/graph_20.graph ./resources/vertex
./build/vertex ./resources/graphs/graph_25.graph ./resources/vertex
./build/vertex ./resources/graphs/graph_30.graph ./resources/vertex
./build/vertex ./resources/graphs/graph_35.graph ./resources/vertex
./build/vertex ./resources/graphs/graph_40.graph ./resources/vertex
./build/vertex ./resources/graphs/graph_45.graph ./resources/vertex
```

To generate images of the graphs along with their vertex cover, run the following command (remember to activate venv first, see Compiling section)
```bash
python ./python/graph_visualiser.py --graph-path ./resources/graphs --vertex-cover-path ./resources/vertex --save-dir ./resources/images
```