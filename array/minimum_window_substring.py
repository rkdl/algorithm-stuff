from collections import Counter


"""
First workable solution (better than brute force, which is smth like O(N^2*M))

Time: O(N * N)
Memory: O(N)
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        required_counts = Counter(t)
        actual_counts = Counter()
        
        left = 0
        right = 0
        min_indices = (0, len(s))
        
        got_it = False
        
        while True:
            if left < right and all(actual_counts[char] >= count for char, count in required_counts.items()):
                got_it = True

                min_indices = min(min_indices, (left, right), key=lambda ix: ix[1] - ix[0])
                
                lchar = s[left]
                if lchar in required_counts:
                    actual_counts[lchar] -= 1
                left += 1

            elif right < len(s):
                rchar = s[right]
                if rchar in required_counts:
                    actual_counts[rchar] += 1
                right += 1

            else:
                break

        if not got_it:
            return ""
        return s[min_indices[0]: min_indices[1]]


"""
An optimal solution

"""