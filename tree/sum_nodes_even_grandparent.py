# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def sum_traverse(node, parent, grandparent) -> int:
            if not node:
                return 0
            return (
                (node.val if grandparent is not None and grandparent.val % 2 == 0 else 0)
                + sum_traverse(node.left, node, parent)
                + sum_traverse(node.right, node, parent)
            )

        return sum_traverse(root, None, None)

"""
let n = number of nodes in tree

Time complexity: O(n), since we have to traverse all the tree once
Memory complexity: O(log n), to store the stack for traversal
"""    
    