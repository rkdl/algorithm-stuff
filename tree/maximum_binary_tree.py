# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        index_of_max = 0
        for idx, num in enumerate(nums):
            if num > nums[index_of_max]:
                index_of_max = idx

        lpart = nums[:index_of_max]
        rpart = nums[index_of_max + 1:]
        return TreeNode(
            nums[index_of_max],
            self.constructMaximumBinaryTree(lpart),
            self.constructMaximumBinaryTree(rpart),
        )
