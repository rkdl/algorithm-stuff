class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        stack = [root]
        
        root_val = root.val
        while stack:
            node = stack.pop()
            if not node:
                continue
            
            if node.val != root_val:
                return False
            stack.append(node.left)
            stack.append(node.right)
        
        return True
