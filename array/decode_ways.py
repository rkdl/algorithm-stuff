ALPHABET_SIZE = 26

class Solution:
    def numDecodings(self, s: str) -> int:
        cache = [None] * len(s)
        
        def num_decodings_helper(i: int) -> int:
            if i >= len(s):
                return 1
            
            if cache[i] is not None:
                return cache[i]
            
            ways_to_decode = 0
            if s[i] != '0':
                ways_to_decode += num_decodings_helper(i + 1)
                if len(s) - i >= 2 and int(s[i:i+2]) <= ALPHABET_SIZE:
                    ways_to_decode += num_decodings_helper(i + 2)
            
            cache[i] = ways_to_decode
            
            return ways_to_decode
        
        return num_decodings_helper(0)
