
# recursive, DFS

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.right)        
        self.invertTree(root.left)
        
        return root

# recursive, DFS, immutable (create and return a new tree)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        return TreeNode(
            root.val,
            self.invertTree(root.right),
            self.invertTree(root.left),
        )


# imperative, DFS
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        stack = [root]
        while stack:
            n = stack.pop()

            l = n.left
            r = n.right
            n.left = r
            n.right = l
            if l:
                stack.append(l)
            if r:
                stack.append(r)

        return root