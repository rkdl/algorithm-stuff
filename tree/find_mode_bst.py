# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

##########################################################################
# Two passes
# O(N) Time
# O(1) Additional Memory (Ignoring recursion stack and the result array)
##########################################################################

def for_each_inorder(root: TreeNode, callback: Callable[[TreeNode], None]):
    if not root:
        return
    for_each_inorder(root.left, callback)
    callback(root)
    for_each_inorder(root.right, callback)


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return 0
        
        max_occurences = 1
        cur_occurences = 1
        prev_val = None
        
        def find_max_occur(node):
            nonlocal max_occurences
            nonlocal cur_occurences
            nonlocal prev_val
            if node.val == prev_val:
                cur_occurences += 1
            else:
                max_occurences = max(max_occurences, cur_occurences)
                cur_occurences = 1
            
            prev_val = node.val
            
        for_each_inorder(root, find_max_occur)
    
        max_occurences = max(max_occurences, cur_occurences)
        
        cur_occurences = 1
        prev_val = None
        
        result = []
        
        def find_values_by_occurences(node):
            nonlocal cur_occurences
            nonlocal prev_val
            
            if node.val == prev_val:
                cur_occurences += 1
            else:
                if cur_occurences == max_occurences and prev_val is not None:
                    result.append(prev_val)
                cur_occurences = 1
            
            prev_val = node.val
        
        for_each_inorder(root, find_values_by_occurences)
        if cur_occurences == max_occurences and prev_val is not None:
            result.append(prev_val)
        
        return result
