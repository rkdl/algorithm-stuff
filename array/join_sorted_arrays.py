from typing import *


def join(nums1: List[int], nums2: List[int]) -> List[int]:
    joined: List[int] = []
        
    i1 = 0
    i2 = 0
    l1_exceeded = False
    l2_exceeded = False
    while i1 < len(nums1) or i2 < len(nums2):
        if i1 < len(nums1) and (i2 >= len(nums2) or nums1[i1] <= nums2[i2]):
            joined.append(nums1[i1])
            i1 += 1
        if i2 < len(nums2) and (i1 >= len(nums1) or nums2[i2] <= nums1[i1]):
            joined.append(nums2[i2])
            i2 += 1
    return joined


print(join([1,3], [2]))

print(join([1,2], [2]))
print(join([1,2], []))

print(join([], [2]))

print(join([1,2, 8], [2,3]))

print(join([1], [2,3]))
