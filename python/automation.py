import argparse
import subprocess
import pathlib
import graph_visualiser
import os
from graph_visualiser import Graph
import time
import csv


def parse_args() -> argparse.Namespace :
    parser = argparse.ArgumentParser("automation")

    parser.add_argument("--resources-dir",type=str,required=True,help="Directory to store graph files")
    parser.add_argument("--seed", type=str, help="Seed for random number generator")

    parser.add_argument("--generator",type=str,required=True,help="Path to executable to generate graph")
    parser.add_argument("--vertex-cover",type=str,required=True,help="Path to executable to find vertex cover")

    known, unknown = parser.parse_known_args()
    print(f"Unknown Arguments: {unknown}")

    return known


def execute_graph_generator(executable: pathlib.Path ,seed: int, directory: pathlib.Path) -> bool: 
    arguments = [
        f"{executable}",
        f"{seed}",
        f"{directory}"
    ]

    print("Generating Graphs...")

    try:
        process = subprocess.run(arguments)
    except OSError as err:
        print("\n"*3)
        if err.errno == 8:
            print("Executable file given as --generator is incompatilbe with your OS")
        print(f"Unable to execute the graph_generator.\n{type(err)}:\n{err}")
        return False
    except Exception as err:
        print("\n"*3)
        print(f"Unable to execute the graph_generator.\n{type(err)}:\n{err}")
        return False
    return True


def execute_vertex_cover_generator(executable: pathlib.Path, graph_dir: pathlib.Path, vertex_dir: pathlib.Path) -> tuple[bool,dict]:

    print("-"*50, "Brute Forcing Vertex Cover...", sep="\n")

    glob = graph_dir.glob("*.graph")
    for g in glob:
        args = [
            str(executable),
            str(g),
            str(vertex_dir)
        ]

        try:
            process = subprocess.run(args,stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if process.returncode != 0:
                print(f"Unable to execute the vertex cover executable.\n{process.stderr}")
                return False

            print(f"{' '.join(args)}","Output:",process.stdout.decode(),sep="\n")
            print("-"*50)
        except OSError as err:
            print("\n"*3)
            if err.errno == 8:
                print("Executable file given as --vertex-cover is incompatilbe with your OS")
            print(f"Unable to execute the vertex cover executable.\n{err}")
            return False
        except Exception as err:
            print("\n"*3)
            print(f"Unable to execute the vertex cover executable.\n{err}")
            return False

    return True

def execute_graph_visualiser(graph_dir: pathlib.Path, vertex_dir: pathlib.Path, save_dir: pathlib.Path) -> bool:

    print("Generating Images...")

    args = [
        "--graph-path",
        str(graph_dir),
        "--vertex-cover-path",
        str(vertex_dir),
        "--save-dir",
        str(save_dir)
    ]

    graph_visualiser.main(args)


def run_full(opts):
    resources_dir = pathlib.Path(opts.resources_dir).absolute()
    generator = pathlib.Path(opts.generator).absolute()
    vertex_cover = pathlib.Path(opts.vertex_cover).absolute()
    seed = 101

    if not generator.exists():
        print(f"Please provide executable for generating graphs.\nValue Provided: {generator}")
        return

    if not vertex_cover.exists():
        print(f"Please provide executable for Vertex Cover.\nValue Provided: {vertex_cover}")
        return

    if opts.seed:
        seed = hash(opts.seed)

    if not resources_dir.is_dir():
        print("Directory, doesn't exists. Creating One")
    else:
        files = list(resources_dir.walk())
        if len(files) > 1:
            print("Directory is not empty. Please provide an empty directory",list(resources_dir.walk()),sep="\n")
            inp = input("Do you want to clean this directory [y|N]: ")
            inp = inp.strip().lower()

            if inp == 'y':
                for i in range(len(files) - 1, -1, -1):
                    root, dirs, file = files[i]
                    for f in file:
                        rm_file = root.absolute().joinpath(f)
                        print(rm_file)
                        os.remove(rm_file)
                    for dir in dirs:
                        rm_dir = root.absolute().joinpath(dir)
                        print(rm_dir)
                        os.removedirs(rm_dir)

            else:
                print("Unknown input, Exiting")
                return


    graph_path = resources_dir.joinpath("graphs")
    vertex_path = resources_dir.joinpath("vertex")
    image_path = resources_dir.joinpath("images")

    graph_path.mkdir(parents=True)
    vertex_path.mkdir(parents=True)
    image_path.mkdir(parents=True)

    if not execute_graph_generator(generator, seed, graph_path):
        return
    if not execute_vertex_cover_generator(vertex_cover, graph_path, vertex_path):
        return
    execute_graph_visualiser(graph_path, vertex_path, image_path)



def generate_table(opts):
    resources_dir = pathlib.Path(opts.resources_dir).absolute()
    vertex_path = resources_dir.joinpath("vertex")
    csv_path = resources_dir.joinpath("table.csv")

    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["(n,m)", "Size", "Time (s)"])

        glob = vertex_path.glob("*.vertex_cover")
        for g in glob:
            g = Graph(vertex_file=g)
            data = g.get_data()
            writer.writerow([f"({data[0]},{data[1]})", data[2], f"{data[3] * 10e-6}",])
    



def main():
    opts = parse_args()

    run_full(opts)
    generate_table(opts)




if __name__ == "__main__":
    main()

