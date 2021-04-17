# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.__stack = []
        self.__cur = root

    def next(self) -> int:
        if self.__stack or self.__cur:
            while self.__cur:
                self.__stack.append(self.__cur)
                self.__cur = self.__cur.left

            self.__cur = self.__stack.pop()
            next_val = self.__cur.val
    
            self.__cur = self.__cur.right
            
            return next_val
        return None

    def hasNext(self) -> bool:
        return bool(self.__stack or self.__cur)


# Iteration time complexity: O(n) where n is number of nodes
# Iteration memory complexity: O(h) where n is tree depth; h = log2n


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
