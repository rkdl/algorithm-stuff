"""
Recursive with memo
O(N) time
O(N) additional space
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [None] * len(nums)
        def rob_helper(i):
            if i < 0:
                return 0
            if memo[i] is None:
                memo[i] = max(rob_helper(i - 2) + nums[i], rob_helper(i - 1))
            return memo[i]
        
        return rob_helper(len(nums) - 1)



"""
Dynamic programming or something?
O(N) time
O(1) additional space
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_best = 0
        prev_prev_best = 0
        for i, house_value in enumerate(nums):
            cur_best = max(prev_prev_best + house_value, prev_best)
            prev_prev_best = prev_best
            prev_best = cur_best
        return prev_best
