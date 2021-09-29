class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        
        initial_offsets = (
            (-1, 0),
            (-1, 1),
        )
        
        for i in range(len(s)):
            for step in range(2):
                l = i + initial_offsets[step][0]
                r = i + initial_offsets[step][1]
                
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                    count += 1
                    
        return count
