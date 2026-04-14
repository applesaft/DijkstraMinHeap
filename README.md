# Dijkstra-Min-Heap

This project implements **Dijkstra's algorithm** using a **Binary Min Heap**, all from scratch in Python. 
The program accepts a graph via the CLI, given in the form of an Adjacency Matrix, a source node and a destination node and outputs the shortest path between the two nodes.
 
## Components
 
- `HeapNode` — a binary tree node with explicit `left`, `right`, and `parent` pointers
- `MinHeap` — a complete binary tree min-heap with `insert_node`, `extract_min`, `decrease_key`, and a `node_map` dictionary for O(1) node lookup
- `dijkstra` — Dijkstra's algorithm using the custom heap as a priority queue, with `decrease_key` instead of lazy insertion — each node exists in the heap exactly once
 
## Complexity
 
| Operation | Complexity |
|---|---|
| insert_node | O(log n) |
| extract_min | O(log n) |
| decrease_key | O(log n) |
| Dijkstra's overall | O((V + E) log V) |
 
## Project structure
 
```
Dijkstra-Min-Heap/
├── main.py            # entry point
├── dijkstra.py        # shortest path algorithm
├── min_heap.py        # pointer-based binary min-heap
├── min_heap_node.py   # HeapNode class
├── cli.py             # user input and result display
└── README.md
```
 
## How to run
 
**1. Clone the repository**
```bash
git clone https://github.com/applesaft/DijkstraMinHeap.git
cd DijkstraMinHeap
```
 
**2. Install dependencies**
- `rich` — terminal formatting and tables
  
## Example
 
For a graph with 5 nodes, entering this adjacency matrix:
 
```
     0   1   2   3   4
0  [ 0,  2,  6,  0,  0 ]
1  [ 0,  0,  0,  3,  0 ]
2  [ 0,  0,  0,  1,  0 ]
3  [ 0,  0,  0,  0,  5 ]
4  [ 0,  0,  0,  0,  0 ]
```
 
Source `0`, destination `4` produces:
 
```
+-----+--------+--------+--------+-----------------+
| Hop |  From  |   To   | Weight | Cumulative Cost |
+-----+--------+--------+--------+-----------------+
|  1  | Node 0 | Node 1 |   2    |        2        |
|  2  | Node 1 | Node 3 |   3    |        5        |
|  3  | Node 3 | Node 4 |   5    |       10        |
+-----+--------+--------+--------+-----------------+
Total cost: 10
```
 
## Adjacency matrix rules
- Size N×N where N is the number of nodes
- `matrix[u][v]` is the edge weight from node `u` to node `v`
- `0` means no connection
- Diagonal must be `0` (a node has no edge to itself)
- No negative weights
 