class HeapNode:
    """
    Represents a single node in binary tree min-heap
    Each node holds the node_id and the cost
        Pointers
        + left     : pointer to left child node, None if no left child
        + right    : pointer to right child node, None if no right child
        + parent   : pointer to parent node, None if this is the root
    """

    # cost, it takes to get to the node
    def __init__(self, cost, node_id):
        self.cost = cost
        self.node_id = node_id
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        # for any node, get information about its child nodes and parent node
        left_id   = self.left.node_id   if self.left   else None
        right_id  = self.right.node_id  if self.right  else None
        parent_id = self.parent.node_id if self.parent else None
        return (
            f"HeapNode(node_id={self.node_id}, cost={self.cost}, "
            f"parent={parent_id}, left={left_id}, right={right_id})"
        )

