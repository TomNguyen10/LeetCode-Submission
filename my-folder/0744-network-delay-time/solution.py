class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for edge in times:
            u, v, w = edge
            graph[u].append((v, w))
        
        dist = [float('inf')] * (n+1)
        dist[k] = 0

        pq = []
        heapq.heappush(pq, (0, k))

        while pq:
            distance, node = heapq.heappop(pq)
            for vertex, w in graph[node]:
                if dist[vertex] > dist[node] + w:
                    dist[vertex] = dist[node] + w
                    heapq.heappush(pq, (dist[vertex], vertex))
        
        res = 0
        print(dist)
        for i in range(1, len(dist)):
            dis = dist[i]
            if dis == float('inf'):
                return -1
            res = max(res, dis)

        return res
