COLOR_UNDEFINED = -1
COLOR_RED = 0
COLOR_GREEN = 1


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for a, b in dislikes:
            graph[a - 1].append(b - 1)

        return self.isBipartite(graph)
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [COLOR_UNDEFINED for _ in range(len(graph))]
        
        queue = deque()
        
        for i in range(len(graph)):
            if colors[i] != COLOR_UNDEFINED:
                continue
            queue.append(i)
            colors[i] = COLOR_RED
            while queue:
                cur = queue.popleft()
                for neighbor in graph[cur]:
                    if colors[neighbor] == COLOR_UNDEFINED:
                        if colors[cur] == COLOR_RED:
                            colors[neighbor] = COLOR_GREEN
                        else:
                            colors[neighbor] = COLOR_RED
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[cur]:
                        return False
        return True
