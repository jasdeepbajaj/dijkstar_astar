import matplotlib.image as img
import numpy as np
from dijkstra import find_shortest_path_dijkstra
from utils import *
import matplotlib.pyplot as plt

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

movements = [(0, 1),  # right
             (0, -1),  # left
             (1, 0),  # down
             (-1, 0)]  # up


testImage3 = img.imread('pgmimg_10.000000.pgm')
env3 = PerceptionMapper(testImage3, 10)
map3 = env3.map

plt.imshow(map3)

source_node = (158, 224)
destination_node = (1468, 232)

start1 = int(source_node[0]/10.0)
start2 = int(source_node[1]/10.0)
start = (start1, start2)

goal1 = int(destination_node[0]/10.0)
goal2 = int(destination_node[1]/10.0)
goal = (goal1, goal2)

print(start)
print(goal)

grid_matrix = map3.tolist()

print(grid_matrix[start[0]][start[1]])
print(grid_matrix[goal[0]][goal[1]])

path_dijkstra, searched_nodes_dijkstra = find_shortest_path_dijkstra(grid_matrix, movements, start, goal)
print(path_dijkstra)
fig, ax = plt.subplots()

# displaying the occupancy grid
map_np = np.array(grid_matrix)
ax.imshow(map_np)
ax.plot(start[1], start[0], marker='s', color='green', markersize=2, label='source_node')
ax.plot(goal[1], goal[0], marker='s', color='red', markersize=2, label='destination_node')
ax.legend()  # Add a legend.
plt.show()

