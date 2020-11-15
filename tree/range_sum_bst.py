# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        
        val = root.val
        left = root.left
        right = root.right
        rangeSumBST = self.rangeSumBST

        if val < L:
            return rangeSumBST(right, L, R)
        if val > R:
            return rangeSumBST(left, L, R)

        lsum = rangeSumBST(left, L, R)
        rsum = rangeSumBST(right, L, R)
        return val + lsum + rsum


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = [root]

        rsum = 0
        while stack:
            node = stack.pop()
            if not node:
                continue

            val = node.val
            if val > R:
                stack.append(node.left)
            elif val < L:
                stack.append(node.right)
            elif L <= val <= R:
                rsum += val
                stack.append(node.left)
                stack.append(node.right)

        return rsum
