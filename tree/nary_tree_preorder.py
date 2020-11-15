"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def traverse(node, lst):
            if not node:
                return
            lst.append(node.val)
            for ch in node.children:
                traverse(ch, lst)
        
        l = []
        traverse(root, l)
        return l


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = []
        stack.append(root)
        
        result = []
        
        while stack:
            n = stack.pop()
            if not n:
                continue
            result.append(n.val)
            stack.extend(reversed(n.children))
        
        return result
