"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#  DFS, Iterative
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


# DFS, Recursive
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        cloned_root = Node(node.val, [])
        cache = {node.val: cloned_root}

        stack = [node]
        while stack:
            node = stack.pop()
            for neigh in node.neighbors:
                cloned_neigh = cache.get(neigh.val)
                if cloned_neigh is None:
                    stack.append(neigh)
                    cloned_neigh = Node(neigh.val, [])
                    cache[neigh.val] = cloned_neigh
                cache[node.val].neighbors.append(cloned_neigh)

        return cloned_root
