class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
        
        nodes = sorted(range(n), key=lambda x: degree[x])
        
        importance = {}
        for i, node in enumerate(nodes):
            importance[node] = i + 1
        
        total_importance = 0
        for u, v in roads:
            total_importance += importance[u] + importance[v]
        
        return total_importance

