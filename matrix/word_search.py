##### NAIVE

def trace_word(board, word, i, j, k, visited):
    if k == len(word):
        return True
    if not ((0 <= i < len(board)) and (0 <= j < len(board[i]))):
        return False
    if board[i][j] != word[k]:
        return False
    
    if (i, j) in visited:
        return False
    visited = {*visited, (i, j)}

    return (
        trace_word(board, word, i, j + 1, k + 1, visited) or
        trace_word(board, word, i - 1, j, k + 1, visited) or
        trace_word(board, word, i, j - 1, k + 1, visited) or
        trace_word(board, word, i + 1, j, k + 1, visited)
    )
    


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False        
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and trace_word(board, word, i, j, 0, set()):
                    return True
        
        return False
