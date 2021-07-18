class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        if not intervals:
            return result
        
        intervals.sort(key=lambda i: i[0])
        
        i = 0
        while i < len(intervals):
            interval_start = intervals[i][0]
            interval_end = intervals[i][1]
            while i < len(intervals) and interval_end >= intervals[i][0]:
                interval_end = max(interval_end, intervals[i][1])
                i += 1
            result.append((interval_start, interval_end))
        
        return result


########


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        if not intervals:
            return result
        
        intervals.sort(key=lambda i: i[0])
        
        current_interval = intervals[0]
        
        for i in range(1, len(intervals) + 1):
            next_interval = intervals[i] if i < len(intervals) else None
            
            if next_interval and current_interval[1] >= next_interval[0]:
                current_interval[1] = max(current_interval[1], next_interval[1])
            else:
                result.append(current_interval)
                current_interval = next_interval

        return result
