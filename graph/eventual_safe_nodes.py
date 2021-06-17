class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = [False] * len(graph)
        visited = [False] * len(graph)

        def dfs(x):
            if visited[x]:
                return
            visited[x] = True

            for y in graph[x]:
                dfs(y)
            if all(safe[y] for y in graph[x]):
                safe[x] = True
        
        for i in range(len(graph)):
            dfs(i)
        
        return [i for i in range(len(safe)) if safe[i]]

"""
Time Complexity: O(N)
Mem Complexity: O(N)
"""
