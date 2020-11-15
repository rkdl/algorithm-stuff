# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        if self.shall_prune(root):
            return None
        
        return TreeNode(
            root.val,
            self.pruneTree(root.left),
            self.pruneTree(root.right),
        )

    def shall_prune(self, root) -> bool:
        if not root:
            return True

        return (
            root.val == 0
            and self.shall_prune(root.left)
            and self.shall_prune(root.right)
        )
