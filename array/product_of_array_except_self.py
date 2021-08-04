## with division


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        try:
            first_idx = nums.index(0)
        except ValueError:
            first_idx = 0    
        
        first_v = 1
        for i in range(len(nums)):
            if i != first_idx:
                first_v *= nums[i]
        
        result = [0] * len(nums)
        result[first_idx] = first_v
        
        for i in range(first_idx + 1, len(nums)):
            if nums[i] != 0:
                result[i] = (result[i - 1] // nums[i]) * nums[i - 1]
            else:
                result[i] = 0
        
        return result


# without division


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        
        p = 1
        for i in range(0,n):
            output[i] = p
            p *= nums[i]
        
        p = 1
        for i in range(n-1, -1, -1):
            output[i] *= p
            p *= nums[i]
        
        return output
