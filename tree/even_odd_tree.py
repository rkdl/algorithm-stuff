# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        lvl_list = [root]
        level = 0
        while lvl_list:
            new_lvl_list = []
            prev = None
            for node in lvl_list:
                if not node:
                    continue
                if level % 2 == node.val % 2:
                    return False
                if prev and (
                    prev.val == node.val
                    or 
                    (level % 2 == 0) == (prev.val > node.val)
                ):
                    return False
                new_lvl_list.append(node.left)
                new_lvl_list.append(node.right)
                prev = node
            lvl_list = new_lvl_list
            level += 1

        return True
