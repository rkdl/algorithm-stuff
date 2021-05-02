
class Solution:
    def maxArea(self, height: List[int]) -> int:
        def calculate_water_area(l, r):
            box_w = r - l
            box_h = min(height[l], height[r])
            return box_w * box_h
        
        max_area = 0

        l = 0
        r = len(height) - 1
        while l < r:
            max_area = max(max_area, calculate_water_area(l, r))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
