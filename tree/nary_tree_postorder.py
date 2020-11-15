"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def traverse(node, lst):
            for c in node.children:
                traverse(c, lst)
            lst.append(node.val)

        if not root:
            return []

        l = []
        traverse(root, l)
        return l
