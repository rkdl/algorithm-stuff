# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class TreeNodeHolder(NamedTuple):
    node: TreeNode
    index: int


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = []
        q.append(TreeNodeHolder(root, 1))
        max_width = 0
        while q:
            width = q[-1].index - q[0].index + 1
            max_width = max(max_width, width)

            new_level = []
            for node, index in q:
                if node.left:
                    new_level.append(TreeNodeHolder(node.left, index * 2))
                if node.right:
                    new_level.append(TreeNodeHolder(node.right, index * 2 + 1))
            q = new_level

        return max_width
