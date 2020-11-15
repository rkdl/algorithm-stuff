# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def get_leaf_seq(root):
            stack = []
            if root:
                stack.append(root)
            
            leaf_seq = []
            while stack:
                node = stack.pop()
                if not node.left and not node.right:
                    leaf_seq.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return leaf_seq

        return get_leaf_seq(root1) == get_leaf_seq(root2)
