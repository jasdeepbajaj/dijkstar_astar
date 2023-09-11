
import matplotlib.image as img
from dijkstra import find_shortest_path_dijkstra
from astar import find_shortest_path_astar
from utils import *
import time
import pandas as pd
import numpy as np

class PerceptionMapper:
    def __init__(self, image, resolution):
        self.map = self.initialiseMap(image)
        # height, width
        self.size = self.map.shape
        self.defaultResolution = resolution

    def initialiseMap(self, testImage):
        env = np.ones(testImage.shape)
        for i in range(testImage.shape[0]):
            for j in range(testImage.shape[1]):
                if testImage[i][j] > 125:
                    env[i][j] = 0
        # print(env.map[0][0])
        return env



# Map is represented by a numpy array, with origin at top left corner
# Positive X-axis is towards right
# Positive Y-axis is towards bottom
#  ----------> X
#  |
#  |
#  |
#  |
#  |
#  |
#  V Y
# map[y][x] will give you the occupancy value of the cell

# Map of Rellis Campus with resolution of 1pixel = 4mt^2 (2x2)
testImage1 = img.imread('pgmimg_2.000000.pgm')
env1 = PerceptionMapper(testImage1, 2)
map1 = env1.map

# Map of Rellis Campus with resolution of 1pixel = 25mt^2 (5x5)
testImage2 = img.imread('pgmimg_5.000000.pgm')
env2 = PerceptionMapper(testImage2, 5)
map2 = env2.map

# Map of Rellis Campus with resolution of 1pixel = 100mt^2 (10x10)
testImage3 = img.imread('pgmimg_10.000000.pgm')
env3 = PerceptionMapper(testImage3, 10)
map3 = env3.map

# Map of Rellis Campus with resolution of 1pixel = 1mt^2 (1x1)
testImage4 = img.imread('pgmimg_1.000000.pgm')
env4 = PerceptionMapper(testImage4, 1)
map4 = env4.map

# Define source and destination nodes
source_nodes = [(158, 224), (892, 436)]
destination_nodes = [(1468, 232), (870, 964), (72, 304), (840, 274)]

movements = [(0, 1),  # right
             (0, -1),  # left
             (1, 0),  # down
             (-1, 0)]  # up

results_list = []

maps = [map1, map2, map3, map4]
res = [2.0, 5.0, 10.0, 1.0]

# Loop through each map and its corresponding resolution
for i, selected_map in enumerate(maps):

    # Loop through each combination of source and target nodes
    for source in source_nodes:
        for destination in destination_nodes:

            # Get adjusted positions based on resolution
            start, goal = get_adjusted_pos(source, destination, res[i])

            grid_matrix = selected_map.tolist()

            # Check if start or goal positions are obstacles
            if check_obstacle(start, grid_matrix) or check_obstacle(goal, grid_matrix):
                print("start/goal position is occupied. Hence, No solution")

                results_list.append({
                    'map_num': f"map{i + 1}",
                    'resolution': f"{res[i]} m * {res[i]} m",
                    'source': source,
                    'destination': destination,
                    'computation time (dijkstra)': None,
                    'total_searched(dijkstra)': None,
                    'computation time (astar)': None,
                    'total_searched(astar)': None
                })

            else:
                # find path using Dijkstra's algorithm
                x = time.time()
                path_dijkstra, searched_nodes_dijkstra = find_shortest_path_dijkstra(grid_matrix, movements, start, goal)
                total_time_dijkstra = time.time() - x
                total_searched_nodes_dijkstra = len(searched_nodes_dijkstra)

                if path_dijkstra is None:
                    computation_time_dijkstra = "N/A"
                    print(f"Unreachable Destination Node. Hence, no path could be found by dijkstra between {source} to {destination} in map{i + 1} ({res[i]} m * {res[i]} m)")

                else:
                    computation_time_dijkstra = total_time_dijkstra
                    print(f"Computation time to get path from {source} to {destination} in map{i + 1} ({res[i]} m * {res[i]} m) for Dijkstra is {computation_time_dijkstra}")
                    plot_map(grid_matrix, path_dijkstra, start, goal)

                # find path using A* algorithm
                x = time.time()
                path_astar, searched_nodes_astar = find_shortest_path_astar(grid_matrix, movements, start, goal)
                total_time_astar = time.time() - x
                total_searched_nodes_astar = len(searched_nodes_astar)

                if path_astar is None:
                    computation_time_astar = "N/A"
                    print(f"Unreachable Destination Node. Hence, no path could be found by A* between {source} to {destination} in map{i + 1} ({res[i]} m * {res[i]} m)")

                else:
                    computation_time_astar = total_time_astar
                    print(f"Computation time to get path from {source} to {destination} in map{i + 1} ({res[i]} m * {res[i]} m) for A* is {computation_time_astar}")
                    # plot_map(grid_matrix, path_astar, start, goal)

                results_list.append({
                    'map_num': f"map{i + 1}",
                    'resolution': f"{res[i]} m * {res[i]} m",
                    'source': source,
                    'destination': destination,
                    'computation time (dijkstra)': computation_time_dijkstra,
                    'total_searched(dijkstra)': total_searched_nodes_dijkstra,
                    'computation time (astar)': computation_time_astar,
                    'total_searched(astar)': total_searched_nodes_astar
                })

# Create a DataFrame from the results_list
results_df = pd.DataFrame(results_list)

file_path = 'results.csv'
results_df.to_csv(file_path, index=False)