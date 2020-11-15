# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self._is_symmetric_helper(root.left, root.right)
        
    def _is_symmetric_helper(self, n1, n2):
        if not n1 and not n2:
            return True
        if not n1 or not n2:
            return False

        _is_symmetric_helper = self._is_symmetric_helper
        return (
            n1.val == n2.val
            and _is_symmetric_helper(n1.left, n2.right)
            and _is_symmetric_helper(n1.right, n2.left)
        )


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root.left, root.right)]
        while stack:
            (n1, n2) = stack.pop()
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            stack.append((n1.left, n2.right))
            stack.append((n1.right, n2.left))
        return True
