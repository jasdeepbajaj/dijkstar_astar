from queue import PriorityQueue
from utils import *


def find_shortest_path_dijkstra(occupancy_grid, movements: list, source_node: tuple, destination_node: tuple) -> tuple:
    """
    Find the shortest path using Dijkstra's algorithm.
    """
    # Initialize the g_score dictionary with infinite values and Set the g_score for the source node to 0
    g_score = {(i, j): float('inf') for i in range(len(occupancy_grid)) for j in range(len(occupancy_grid[0]))}
    g_score[source_node] = 0

    # Create a priority queue and put the source node in the priority queue with a priority of 0
    priority_queue = PriorityQueue()
    priority_queue.put((0, source_node))

    # Initialize an empty list to keep track of searched nodes
    searched_nodes = []

    # Initialize an empty dictionary to store parent-child relationships
    came_from = {}

    while not priority_queue.empty():  # While the priority queue is not empty.
        current_g, current_node = priority_queue.get()  # Get the node with the highest priority.
        searched_nodes.append(current_node)  # Add the current node to the list of searched nodes.

        # If the current node is the destination node, return the reconstructed path and the list of searched nodes
        if current_node == destination_node:
            return reconstruct_path(source_node, destination_node, came_from), searched_nodes

        # For each possible movement, calculate the new node.
        for dy, dx in movements:
            new_node = (current_node[0] + dy, current_node[1] + dx)

            # If the new node is within the grid bounds and not an obstacle, calculate the new g_score.
            if lies_in_grid(new_node, occupancy_grid) and not check_obstacle(new_node, occupancy_grid):
                new_g = current_g + COST

                if new_g < g_score[new_node]:  # If the new g_score is less than the existing g_score for the node.
                    came_from[new_node] = current_node  # Update the parent-child relationship.
                    g_score[new_node] = new_g  # Update the g_score.
                    priority_queue.put(
                        (new_g, new_node))  # Put the node back in the priority queue with the updated priority.

    return None, searched_nodes  # Return None for path (if unsearched destination node) and the list of searched nodes
