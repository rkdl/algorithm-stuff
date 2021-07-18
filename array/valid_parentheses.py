class Solution:
    def isValid(self, s: str) -> bool:        
        parens_mapping = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        
        stack = []
        
        for char in s:
            if char in parens_mapping:
                stack.append(char)
            elif not stack or parens_mapping[stack.pop()] != char:
                return False
        
        return not stack
