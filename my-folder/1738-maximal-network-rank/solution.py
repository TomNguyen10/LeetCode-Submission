class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                res = max(res, len(graph[i]) + len(graph[j]) - (i in graph[j]))
        
        return res
