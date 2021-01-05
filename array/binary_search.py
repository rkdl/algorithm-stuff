class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(haystack: List[int], needle: int, l: int, r: int) -> int:
            if l > r:
                return -1
            mid = (l + r) // 2
            if haystack[mid] == needle:
                return mid
            if haystack[mid] > needle:
                return bin_search(haystack, needle, l, mid - 1)
            return bin_search(haystack, needle, mid + 1, r)

        return bin_search(nums, target, 0, len(nums) - 1)
