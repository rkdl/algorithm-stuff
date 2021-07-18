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
