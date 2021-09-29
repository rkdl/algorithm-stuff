"""
Brute force algorithm:
for each substring, check if it is a palindrome
generate all substrings: O(N^2)
check if it is a palindrome: O(N)

Overall time compl: O(N^3)

Improved:
instead of generating all the substrings, try to find a palindrome in a nested loop
kind of a sliding window
Overall time complexity: O(N^2)

"""


def extend_palindrome_substr(s: str, l: int, r: int) -> tuple[int, int]:
    while l - 1 >= 0 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
        l -= 1
        r += 1
    return (l, r)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        longest_substr_l = 0
        longest_substr_r = 0
        
        for i in range(1, len(s)):
            if 0 < i < len(s) - 1 and s[i - 1] == s[i + 1]:
                l, r = extend_palindrome_substr(s, i - 1, i + 1)
                if (r - l) > (longest_substr_r - longest_substr_l):
                    longest_substr_l = l
                    longest_substr_r = r
            if 0 < i and s[i - 1] == s[i]:
                l, r = extend_palindrome_substr(s, i - 1, i)
                if (r - l) > (longest_substr_r - longest_substr_l):
                    longest_substr_l = l
                    longest_substr_r = r
        
        return s[longest_substr_l:longest_substr_r+1]
