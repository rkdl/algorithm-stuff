class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {num: idx for idx, num in enumerate(nums)}
        
        first_idx = 0
        second_idx = 0
        for i, num in enumerate(nums):
            j = nums_map.get(target - num)
            if j is not None and i != j:
                first_idx = i
                second_idx = j
                break

        return [first_idx, second_idx]
