# Path Planning Project

## About
This project was created for MEEN 689 Motion Planning course at Texas A&M University. It finds optimal paths between source and destination nodes on maps of the RELLIS campus using Dijkstra's algorithm and A* search.

Four maps of different resolutions are used:

Map 1: 2mx2m \n
Map 2: 5mx5m
Map 3: 10mx10m
Map 4: 1mx1m

The map is represented as a 2D occupancy grid, with 1 indicating an obstacle and 0 indicating free space.

## Getting Started

##Project Scripts
###utils.py:
Contains a collection of handy functions utilized throughout the project.

###dijkstra.py
Implements the A* search algorithm for discovering optimal paths.

###astar.py
Houses the code for Dijkstra's search algorithm to determine optimal paths.

###main.py
Coordinates the execution of path planning, employing both Dijkstra and A* algorithms, across various map resolutions and source/destination pairs.

##Running
To run the path planner:
python main.py
This will output results to results.csv and also display plot visualizations.

##Usage
The main parameters that can be configured are:

source_nodes: List of source (start) nodes
destination_nodes: List of destination (goal) nodes
maps: List of occupancy grid maps to use
res: List of resolutions corresponding to each map
New maps can be added by placing pgm images in the data folder and loading them in main.py.

##Results
The main results are:

Computation time for Dijkstra's algorithm vs. A*
Number of nodes searched by each algorithm
Visualization showing the optimal path overlaid on the map
This allows analysis of how the optimal path and computation time varies based on map resolution.

Results are output to results.csv.
