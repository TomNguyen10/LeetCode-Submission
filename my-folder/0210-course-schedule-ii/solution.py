class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for des, src in prerequisites:
            graph[src].append(des)
        
        indegree = [0] * numCourses
        for nodes in graph.values():
            for node in nodes:
                indegree[node] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        res = []

        while q:
            node = q.popleft()
            res.append(node)
            for adj in graph[node]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)
            
        if len(res) != numCourses:
            return []
        
        return res
