import sys
from min_heap import MinHeap
 
def dijkstra(matrix, size, source):
   
    costs    = [sys.maxsize] * size     # cost to reach each node
    previous = [-1] * size  # tracks the path, for each node, which node we came
    costs[source] = 0
 
    # Nodes go into the heap immediately. Source cost = 0, EE = INF
    # no insertions will happens mid-algorithm
    # decrease_key calls when cheaper paths are found.
    pq = MinHeap()
    for node_id in range(size):
        pq.insert_node(costs[node_id], node_id)
   
    while not pq.is_empty():
        current_cost, u = pq.extract_min()

        # no path from source
        if current_cost == sys.maxsize:
            break
        
        # look at every possible neighbour v of u by scanning its row in the adjacency matrix
        for v in range(size):
            weight = matrix[u][v]

            if weight == 0:
                continue
 
            # Skip if v has already been extracted (shortest path finalised)
            if v not in pq.node_map:
                continue
 
            new_cost = costs[u] + weight
 
            # Found a cheaper path to v
            if new_cost < costs[v]:
                costs[v]    = new_cost
                previous[v] = u # record that we reached v through u, so the path can be reconstructed later
                pq.decrease_key(v, new_cost)
 
    return costs, previous