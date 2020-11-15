# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        stack = [s]
        while stack:
            node = stack.pop()

            if not node:
                continue
            if node.val == t.val and self.check_subtree(node, t):
                return True
            stack.append(node.left)
            stack.append(node.right)

        return False

    def check_subtree(self, n1, n2):
        stack = [(n1, n2)]
        while stack:
            (n1, n2) = stack.pop()
            if not n1 and not n2:
                continue

            if (not n1) != (not n2):
                return False
            if n1.val != n2.val:
                return False

            stack.append((n1.left, n2.left))
            stack.append((n1.right, n2.right))

        return True
