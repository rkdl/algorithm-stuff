"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cache = {}

        def clone(node):
            if cached := cache.get(node.val):
                return cached
            new_node = Node(node.val, [])
            cache[new_node.val] = new_node
            for n in node.neighbors:
                new_node.neighbors.append(clone(n))
            return new_node

        if not node:
            return None
        return clone(node)
