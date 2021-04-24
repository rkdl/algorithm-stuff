# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def traverse(root, path, all_paths):
            cur_path = [*path, root.val]
    
            if not root.left and not root.right:
                all_paths.append(cur_path)
            else:
                if root.left:
                    traverse(root.left, cur_path, all_paths)
                if root.right:
                    traverse(root.right, cur_path, all_paths)

        paths = []
        if root:
            traverse(root, [], paths)

        
        return [
            '->'.join(map(str, path))
            for path in paths
        ]


# ITERATIVE
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []

        stack = []
        if root:
            stack.append((root, []))

        while stack:
            node, path = stack.pop()
            cur_path = [*path, node.val]
            if not node.left and not node.right:
                paths.append(cur_path)
            else:
                if node.right:
                    stack.append((node.right, cur_path))
                if node.left:
                    stack.append((node.left, cur_path))

        return [
            '->'.join(map(str, path))
            for path in paths
        ]
