# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

MAX_VAL = 2 ** 31 - 1


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        result = MAX_VAL
        prev = MAX_VAL

        def inorder(node):
            nonlocal result
            nonlocal prev

            if not node:
                return
            inorder(node.left)
            
            diff = abs(node.val - prev)
            if diff < result:
                result = diff

            prev = node.val

            inorder(node.right)

        inorder(root)

        return result
