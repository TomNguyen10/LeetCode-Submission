class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            if end in graph[start]:
                return graph[start][end]
        
            visited.add(start)
            for neighbor in graph[start]:
                if neighbor not in visited:
                    val = dfs(neighbor, end, visited)
                    if val != -1.0:
                        return graph[start][neighbor] * val
            return -1.0

        results = []
        for query in queries:
            start, end = query
            results.append(dfs(start, end, set()))

        return results

