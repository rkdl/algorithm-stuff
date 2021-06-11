# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def sum_traverse(node: TreeNode, parents: Sequence[TreeNode]) -> int:
            if not node:
                return 0
            
            has_event_grandparent = len(parents) >= 2 and parents[-1].val % 2 == 0

            next_parents = (node, parents[0]) if parents else (node,)
            return (
                (node.val if has_event_grandparent else 0)
                + sum_traverse(node.left, next_parents)
                + sum_traverse(node.right, next_parents)
            )

        return sum_traverse(root, tuple())

"""
let n = number of nodes in tree

Time complexity: O(n), since we have to traverse all the tree once
Memory complexity: O(log n), to store the stack for traversal
"""    
    