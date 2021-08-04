"""
IN: [1,2,3,4,5,6,7] k = 3

ER: [5,6,7,1,2,3,4]

What we need to do?

1. Move (shift) numbers at positions 0 .. n - k - 1 k times, to n - k .. n - 1
   e.g. for each num = nums[i] => num = nums[i+k]
   [1,2,3,4,...] -> [...,1,2,3,4]

2. Move numbers at positions n - k .. n - 1 to 0 .. k.
   e.g. for each num == nums[i] => num == nums[(i + k) % n]
                                               (i + k) % n === i + k - n

1 st reverse
[7,6,5,4,3,2,1]
2nd 
[5,6,7,4,3,2,1]
3rd
[5,6,7,1,2,3,4]

HMMM

[1,2,3,4,5,6,7] k = 2

1st
[7,6,5,4,3,2,1]
2nd
[6,7,5,4,3,2,1]
3rd
[6,7,1,2,3,4,5]

"""

def reverse(nums: list, from_: int, to: int) -> None:
    for i in range((to - from_ + 1) // 2):
        l = i + from_
        r = to - i
        nums[l], nums[r] = nums[r], nums[l]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
