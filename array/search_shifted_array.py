class Solution:
    def bin_search(self, haystack: List[int], needle: int, l: int, r: int) -> int:
        bin_search = self.bin_search
        if l > r:
            return -1
        mid = (l + r) // 2
        if haystack[mid] == needle:
            return mid
        if haystack[mid] > needle:
            return bin_search(haystack, needle, l, mid - 1)
        return bin_search(haystack, needle, mid + 1, r)

    def find_min(self, nums: List[int], l: int, r: int) -> int:
        find_min = self.find_min
        if l >= r:
            return l
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            return find_min(nums, mid + 1, r)
        return find_min(nums, l, mid)

    def search(self, nums: List[int], target: int) -> int:
        find_min = self.find_min
        bin_search = self.bin_search
        if not nums:
            return -1

        r = len(nums) - 1
        min_idx = find_min(nums, 0, r)

        if target >= nums[min_idx] and target <= nums[r]:
            return bin_search(nums, target, min_idx, r)
        return bin_search(nums, target, 0, min_idx)
