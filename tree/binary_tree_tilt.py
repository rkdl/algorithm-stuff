# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        acc = [0]
        def traverse(n, acc):
            if not n:
                return 0
            
            l = traverse(n.left, acc)
            r = traverse(n.right, acc)
            acc[0] += abs(l - r)
            return n.val + l + r
        
        traverse(root, acc)
        return acc[0]


# shit solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def traverse(n):
            if not n:
                return 0, 0
            
            l, l_acc = traverse(n.left)
            r, r_acc = traverse(n.right)
            acc = l_acc + r_acc + abs(l - r)
            subtree_tilt = l + r + n.val
            return subtree_tilt, acc
        
        _, acc = traverse(root)
        return acc
