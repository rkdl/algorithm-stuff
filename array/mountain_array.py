# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

def bin_search(get: Callable[[int], int], x: int, l: int, r: int) -> int:
    while l <= r: 
        mid = (l + r) // 2  
        mid_val = get(mid)
        if mid_val < x: 
            l = mid + 1
        elif mid_val > x: 
            r = mid - 1  
        else: 
            return mid   
    return -1


def descending_bin_search(get: Callable[[int], int], x: int, l: int, r: int) -> int:
    while l <= r: 
        mid = (l + r) // 2  
        mid_val = get(mid)
        if mid_val > x: 
            l = mid + 1
        elif mid_val < x: 
            r = mid - 1  
        else: 
            return mid   
    return -1


def find_peak_idx(get, length):
    l = 0
    r = length - 1
    while l <= r:
        mid = (l + r) // 2
        cur = get(mid)
        prev = get(mid - 1) if mid > 0 else cur - 1
        next_ = get(mid + 1) if mid < length else cur - 1
        if prev < cur > next_:
            return mid
        elif prev < cur:
            l = mid + 1
        elif prev > cur:
            r = mid - 1


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        # The algo is:
        # 1. find the mid point with modified binary search
        # 2. do the binary search on the left side
        # 2. do the binary search on the right side
        # expected mountain_arr.get calls:
        # 1. ((log2 10000) * 3 ops => 42)
        # 2. (log2 10000 ops => 14)
        # 3. (log2 10000 ops => 14)
        #  42 + 14 + 14 < 100
        length = mountain_arr.length()

        top_idx = find_peak_idx(mountain_arr.get, length)
        
        result = bin_search(mountain_arr.get, target, 0, top_idx)
        if result == -1:
            result = descending_bin_search(mountain_arr.get, target, top_idx + 1, length - 1)
        return result
