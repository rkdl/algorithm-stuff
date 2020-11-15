# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        stack = []
        stack.append(root)
        
        while stack:
            node = stack.pop()
            if not node:
                continue
            
            if node.val == val:
                return node
            if node.val > val:
                stack.append(node.left)
            else:
                stack.append(node.right)
        return None
