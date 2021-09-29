class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_counts: dict[int, int] = {}
        for num in nums:
            if num not in element_counts:
                element_counts[num] = 1
            else:
                element_counts[num] += 1
        
        max_frequency = max(element_counts.values())
        frequencies = [None] * (max_frequency + 1)
        
        for num, freq in element_counts.items():
            if not frequencies[freq]:
                frequencies[freq] = []
            frequencies[freq].append(num)
        
        top_k_frequent = []
        for nums in reversed(frequencies):
            if not nums:
                continue
            for num in nums:
                if len(top_k_frequent) == k:
                    break
                top_k_frequent.append(num)
        
        return top_k_frequent

    
"""
O(N) Time
O(N) Memory
"""