class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for des, src in prerequisites:
            graph[src].append(des)
        
        indegree = [0] * numCourses

        for nodes in graph.values():
            for node in nodes:
                indegree[node] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        count = 0

        while q:
            node = q.popleft()
            count += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return count == numCourses
