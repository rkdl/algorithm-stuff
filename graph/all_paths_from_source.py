from typing import *


Graph = List[List[int]]

def trace(
    graph: Graph,
    cur: int,
    res: List[List[int]],
    path: List[int],
) -> None:
    end = len(graph) - 1
    if cur == end:
        res.append(path)
    else:
        for direction in graph[cur]:
            trace(graph, direction, res, [*path, direction])


class Solution:
    def allPathsSourceTarget(self, graph: Graph) -> List[List[int]]:
        result = []
        trace(graph, 0, result, [0])
        return result
