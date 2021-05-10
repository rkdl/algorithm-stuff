class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def str_diff(str1, str2):
            removed = [False] * len(str1)
            diff = 0
            for i, char1 in enumerate(str1):
                if removed[i]:
                    continue
                for j, char2 in enumerate(str2):
                    if char1 != char2:
                        removed[i] = True
                        diff += 1
            return diff

        return str_diff(word1, word2) + str_diff(word2, word1)
