def maybe_mark_province(isConnected, visited, i):
    stack = [
        i,
    ]
    while stack:
        i = stack.pop()
        visited[i] = 1
        for j in range(len(isConnected[i])):
            if isConnected[i][j] and not visited[j]:
                stack.append(j)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = [0] * len(isConnected)

        for i in range(len(isConnected)):
            if not visited[i]:
                maybe_mark_province(isConnected, visited, i)
                provinces += 1

        return provinces
