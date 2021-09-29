from heapq import *
"""
heapq == min-heap
"""

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        if len(self.left_heap) == len(self.right_heap):
            heappush(self.right_heap, -heappushpop(self.left_heap, -num))
        else:
            heappush(self.left_heap, -heappushpop(self.right_heap, num))
    
    def findMedian(self) -> float:
        if not self.right_heap:
            return 0.0
        if len(self.right_heap) == len(self.left_heap):
            return float(-self.left_heap[0] + self.right_heap[0]) / 2.0
        else:
            return float(self.right_heap[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()