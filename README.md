# Path Planning Project

## About
This project was created for MEEN 689 Motion Planning course at Texas A&M University. It finds optimal paths between source and destination nodes on maps of the RELLIS campus using Dijkstra's algorithm and A* search.

Four maps of different resolutions are used:

- Map 1: 2mx2m 
- Map 2: 5mx5m
- Map 3: 10mx10m
- Map 4: 1mx1m

The map is represented as a 2D occupancy grid, with 1 indicating an obstacle and 0 indicating free space.

## Getting Started

### Project Scripts

- `utils.py`: Contains a collection of handy functions utilized throughout the project.
- `dijkstra.py`: Houses the code for Dijkstra's search algorithm to determine optimal paths.
- `astar.py`: Houses the code for A* search algorithm along with heuristics function used to determine optimal paths.
- `main.py`: Coordinates the execution of path planning, employing both Dijkstra and A* algorithms, across various map resolutions and source/destination pairs.

### Running

To run the path planner:

```bash
python main.py

This will output results to results.csv and also display plot visualizations.
