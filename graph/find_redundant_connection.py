class DisjointSet:
    def __init__(self):
        self.__parent = {}
    
    def union(self, x: int, y: int) -> None:
        parent = self.__parent

        parent.setdefault(x, x)
        parent.setdefault(y, y)
        
        p_x = parent[x]
        p_y = parent[y]
        
        for i in parent:
            if parent[i] == p_y:
                parent[i] = p_x
    
    def connected(self, x: int, y: int) -> bool:
        parent = self.__parent
        return parent.get(x, -1) == parent.get(y, -2)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dis_set = DisjointSet()
        
        for edge in edges:
            if dis_set.connected(*edge):
                return edge
            dis_set.union(*edge)
        return []
