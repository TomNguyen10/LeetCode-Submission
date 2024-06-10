class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = []

        self.graph = defaultdict(list)
        
        def dfs(u, v, pre):
            if u == v:
                return True
            for child in self.graph[u]:
                if child == pre:
                    continue
                if dfs(child, v, u):
                    return True
            return False

        for edge in edges:
            u, v = edge
            if dfs(u, v, 0):
                res = edge
            else:
                self.graph[u].append(v)
                self.graph[v].append(u)
        
        return res
