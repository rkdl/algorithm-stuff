# First solution I came up with (cringe)
# takes ~8000 ms on Leetcode
# Perhaps it's time complexity should be O(N^2)? Not so sure now. It needs a detailed analysis


class Solution:
    def pack_triplet(self, a, b, c):
        triplet = [a, b, c]
        triplet.sort()
        return tuple(triplet)
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pack_triplet = self.pack_triplet
        
        nums_idx_map = {}
        for i, num in enumerate(nums):
            if num not in nums_idx_map:
                nums_idx_map[num] = set()
            nums_idx_map[num].add(i)
        
        suitable_triplets = set()
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                a = nums[i]
                b = nums[j]
                c = 0 - (a + b)
                
                c_indexes = nums_idx_map.get(c, tuple())
                
                num_of_matches_in_set = int(i in c_indexes) + int(j in c_indexes)
                if len(c_indexes) > num_of_matches_in_set:
                    suitable_triplets.add(pack_triplet(a, b, c))
        
        return [*map(list, suitable_triplets)]


#########################
# sort + sliding window
# takes ~700 ms on Leetcode
# Time complexity: O(N ^ 2)
# Memory complexity: O(sort method + result) -> O(N)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        
        nums.sort()
        
        result = []
        
        for i in range(len(nums) - 2):
            if nums[i] > target:
                break
            if i and nums[i - 1] == nums[i]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                a = nums[i]
                b = nums[left]
                c = nums[right]
                
                _sum = a + b + c
                if _sum < target:
                    left += 1
                elif _sum > target:
                    right -= 1
                else:
                    result.append((a, b, c))
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        
        return result
