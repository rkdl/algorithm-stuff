# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root



class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        new_node = TreeNode(val)
        if not root:
            return new_node

        stack = []
        while stack:
            node = stack.pop()
            if node.val > val:
                if node.left:
                    stack.append(node.left)
                else:
                    node.left = new_node
            else:
                if node.right:
                    stack.append(node.right)
                else:
                    node.right = new_node

        return root
