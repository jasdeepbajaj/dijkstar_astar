import numpy as np
import matplotlib.pyplot as plt
import math

OBSTACLE = 1
COST = 1


def lies_in_grid(node: tuple, occupancy_grid) -> bool:
    """
    Check if a node lies within the bounds of the occupancy grid.
    """
    num_rows = len(occupancy_grid)  # Get the number of rows in the occupancy grid.
    num_cols = len(occupancy_grid[0])  # Get the number of columns in the occupancy grid.

    return 0 <= node[0] < num_rows and 0 <= node[1] < num_cols


def check_obstacle(node: tuple, occupancy_grid) -> bool:
    """
    Check if a node is an obstacle in the occupancy grid.
    """
    return occupancy_grid[node[0]][node[1]] == OBSTACLE


def reconstruct_path(source_node: tuple, destination_node: tuple, came_from: dict) -> list:
    """
    Reconstruct the path from source to destination using the 'came_from' dictionary.
    """
    path = []  # Initialize an empty list called path.
    current = destination_node  # Set the current node to be the destination node.

    while current != source_node:  # While the current node is not the source node.
        path.append(current)  # Add the current node to the path.
        current = came_from[current]  # Set the current node to be its parent node.

    path.append(source_node)  # Add the source node to the path.
    path.reverse()  # Reverse the path to get it in the correct order.
    return path  # Return the reconstructed path.


def plot_map(occupancy_grid, path: list, source_node: tuple, destination_node: tuple):
    """
    Plot the grid map with the path, source node, and goal node.
    """
    fig, ax = plt.subplots()

    # displaying the occupancy grid
    map_np = np.array(occupancy_grid)
    ax.imshow(map_np)

    # displaying the path on occupancy grid
    path_np = np.array(path)
    ax.plot(path_np[:, 1], path_np[:, 0], marker='o', color='pink', markersize=0.5, linewidth=0.5)

    ax.plot(source_node[1], source_node[0], marker='s', color='green', markersize=2, label='source_node')
    ax.plot(destination_node[1], destination_node[0], marker='s', color='red', markersize=2, label='destination_node')
    ax.legend()  # Add a legend.
    plt.show()  # Display the plot.


def get_adjusted_pos(source_node: tuple, destination_node: tuple, resolution: float) -> tuple:
    """
    Adjust the source and destination positions based on the resolution.
    """
    start1 = int(source_node[0] / resolution)
    start2 = int(source_node[1] / resolution)
    start = (start1, start2)

    goal1 = int(destination_node[0] / resolution)
    goal2 = int(destination_node[1] / resolution)
    goal = (goal1, goal2)

    return start, goal