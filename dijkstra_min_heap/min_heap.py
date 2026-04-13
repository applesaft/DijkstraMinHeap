"""
Implementation of a pointer-based binary min-heap from scratch
This binary heap is used to find which one of the next vertex to visit next per Dijkstra's Algorithm
    Scanning every node linearly has complexity O(n),
    The heap has complexity O(log n)
"""
from min_heap_node import HeapNode

class MinHeap:

    def __init__(self):
        self.root = None
        self.size = 0
        self.node_map = {} 

    def insert_node(self, cost, node_id):
        """
        Inserting a new node into the heap:
            - Preserve shape: place the new node in the next available position, left to right
                            (We find this position using the binary representation of (size + 1))
            - Satisfying invariant, parent.cost <= children.cost
                            (the node with the smallest cost is always at the root)
        """

        new_node = HeapNode(cost, node_id)
        self.node_map[node_id] = new_node   # register node in the lookup table
    
        # Use binary representation of (size + 1) to find the exact path to the insertion position.
        binary = str(bin(self.size + 1))[3:]
        if binary == '':
            self.root = new_node
            self.size = self.size + 1
            return
        
        current = self.root
        i = 0  
        while i < len(binary):
            character = binary[i]

            if i == len(binary) - 1:
                if character == '0':
                    current.left = new_node
                else:
                    current.right = new_node
                new_node.parent = current

            else:
                if character == '0':
                    current = current.left
                else:
                    current = current.right

            i += 1

        self.size += 1
        self.sort_up(new_node)


    def sort_up(self, node):
        """
        Restore the heap order after insertion 
        We compare the node with its parent and swap values if the node's cost is smaller than its parent's.
        We keep swapping (values) until either: The node reaches the root (no more parent) or The invariant is satisfied
        """

        current = node
        while current.parent is not None:
            if current.cost < current.parent.cost:
                current.cost, current.parent.cost = current.parent.cost, current.cost
                current.node_id, current.parent.node_id = current.parent.node_id, current.node_id

                # two map updates after every swap
                self.node_map[current.node_id]        = current
                self.node_map[current.parent.node_id] = current.parent

                current = current.parent
            else:
                break

    def decrease_key(self, node_id, new_cost):
        node = self.node_map[node_id]  # O(1) lookup
        node.cost = new_cost
        self.sort_up(node)             # sort up to restore invariant

    def _find_last_node(self):
        """
        Uses the same binary path trick as insert_node, but reads
        bin(size) instead of bin(size + 1) because we want the current
        last node
        """
        binary = bin(self.size)[3:]
 
        current = self.root
        for bit in binary:
            if bit == '0':
                current = current.left
            else:
                current = current.right
 
        return current
    
    def sort_down(self, node):
        """
        Restore heap order after extraction.
        Compare the node with its smallest child and swap their data if the child's cost is smaller. Keep swapping downward until either:
            - The node has no children (reached a leaf)
            - The invariant is satisfied (node cost <= both children)
        """
        current = node
        while True:
            smallest = current
 
            if current.left is not None and current.left.cost < smallest.cost:
                smallest = current.left
 
            if current.right is not None and current.right.cost < smallest.cost:
                smallest = current.right
 
            if smallest == current:
                break
 
            current.cost,    smallest.cost    = smallest.cost,    current.cost
            current.node_id, smallest.node_id = smallest.node_id, current.node_id

            self.node_map[current.node_id]  = current
            self.node_map[smallest.node_id] = smallest 
            current = smallest

    # use by dijkstra.py
    def is_empty(self):
        return self.root is None or self.size == 0
    
    def extract_min(self):
        if self.root is None:
            return None

        min_cost = self.root.cost   # Save the root's data
        min_id   = self.root.node_id

        # remove the extracted node from the lookup table
        del self.node_map[min_id]

        # Copying the last node's data into the root
        # If only one node left
        if self.size == 1:
            self.root = None
            self.size = 0
            return (min_cost, min_id)
 
        # Find the last node and copy its data into the root
        last_node = self._find_last_node()
        self.root.cost    = last_node.cost
        self.root.node_id = last_node.node_id

        self.node_map[self.root.node_id] = self.root

        # delete the last node from its parent
        if last_node.parent.left == last_node:
            last_node.parent.left = None
        else:
            last_node.parent.right = None
 
        # Restore invariant
        self.size -= 1
        self.sort_down(self.root)
        return (min_cost, min_id)