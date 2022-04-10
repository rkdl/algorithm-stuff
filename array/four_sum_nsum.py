class Solution:
    def two_sum(
        self,
        nums: list[int],
        left: int,
        right: int,
        target: int,
    ) -> Iterator[list[int]]:
        result = []
        
        while left < right:
            _sum = nums[left] + nums[right]
            if _sum < target:
                left += 1
            elif _sum > target:
                right -= 1
            else:
                result.append([nums[left], nums[right]])
                        
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                        
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                        
                left += 1
                right -= 1
        
        return result
    
    def n_sum(
        self,
        sum_n: int,
        nums: list[int],
        target: int,
        start: int = 0,
    ) -> Iterator[list[int]]:
        if sum_n == 2:
            yield from self.two_sum(
                nums,
                start,
                len(nums) - 1,
                target,
            )
        else:
            for i in range(start, len(nums) - (sum_n - 1)):
                if i > start and nums[i - 1] == nums[i]:
                    continue
                for tail in self.n_sum(
                    sum_n - 1,
                    nums,
                    target - nums[i],
                    i + 1,
                ):
                    yield [nums[i], *tail]
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:        
        return list(self.n_sum(4, sorted(nums), target))
