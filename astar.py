from queue import PriorityQueue
from utils import *


def heuristic_cost_estimate(current_node: tuple, destination_node: tuple) -> int:
    """
    Heuristic cost estimate for A* algorithm.
    """
    return abs(((current_node[0] - destination_node[0]) ** 2 + (current_node[1] - destination_node[1]) ** 2))


def find_shortest_path_astar(occupancy_grid, movements: list, source_node: tuple, destination_node: tuple) -> tuple:
    """
    Find the shortest path using A* algorithm.
    """
    # Initialize the g_score dictionary with infinite values and Set the g_score for the source node to 0
    g_score = {(i, j): float('inf') for i in range(len(occupancy_grid)) for j in range(len(occupancy_grid[0]))}
    g_score[source_node] = 0

    # Initialize the f_score dictionary with infinite values and Set the f_score for the source node using heuristic estimate
    f_score = {(i, j): float('inf') for i in range(len(occupancy_grid)) for j in range(len(occupancy_grid[0]))}
    f_score[source_node] = heuristic_cost_estimate(source_node, destination_node)

    # Create a priority queue and put the source node in the priority queue with priority based on f_score and heuristic estimate.
    priority_queue = PriorityQueue()
    priority_queue.put((f_score[source_node], heuristic_cost_estimate(source_node, destination_node), source_node))

    # Initialize an empty list to keep track of searched nodes
    searched_nodes = []

    # Initialize an empty dictionary to store parent-child relationships
    came_from = {}

    while not priority_queue.empty():  # While the priority queue is not empty.
        _, _, current_node = priority_queue.get()  # Get the node with the highest priority.
        searched_nodes.append(current_node)  # Add the current node to the list of searched nodes.

        # If the current node is the destination node, return the reconstructed path and the list of searched nodes
        if current_node == destination_node:
            return reconstruct_path(source_node, destination_node, came_from), searched_nodes

            # For each possible movement, calculate the new node.
        for dy, dx in movements:
            new_node = (current_node[0] + dy, current_node[1] + dx)

            # If the new node is within the grid bounds and not an obstacle, calculate the temp g_score and temp f_score.
            if lies_in_grid(new_node, occupancy_grid) and not check_obstacle(new_node, occupancy_grid):
                temp_g_score = g_score[current_node] + COST
                temp_f_score = temp_g_score + heuristic_cost_estimate(new_node, destination_node)

                # If the temporary f_score is less than the existing f_score for the node.
                if temp_f_score < f_score[new_node]:
                    came_from[new_node] = current_node  # Update the parent-child relationship.
                    g_score[new_node] = temp_g_score  # Update the g_score.
                    f_score[new_node] = temp_f_score  # Update the f_score.
                    priority_queue.put((temp_f_score, heuristic_cost_estimate(new_node, destination_node),
                                        new_node))  # Put the node back in the priority queue with the updated priority.

    return None, searched_nodes  # Return None for path (if unsearched destination node) and the list of searched nodes
