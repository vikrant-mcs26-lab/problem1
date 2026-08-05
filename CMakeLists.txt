cmake_minimum_required(VERSION 3.16)
project(problem1 CXX)

set(EXTRA 
    "cpp/src/graph.cpp"
)

include_directories(
    "cpp/include"
)

add_executable(graph_generator "cpp/src/graph_generator.cpp" ${EXTRA})
add_executable(vertex "cpp/src/vertex.cpp" ${EXTRA})
