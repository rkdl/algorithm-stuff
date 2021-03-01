# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        stack = []
        stack.append(root)

        seen = set()
        
        while stack:
            n = stack.pop()
            if not n:
                continue
            
            if (k - n.val) in seen:
                return True
            seen.add(n.val)
            
            stack.append(n.right)
            stack.append(n.left)
        
        return False
