class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        res = [0] * n
        count = [1] * n

        def postOrder(node, parent):
            for child in graph[node]:
                if child != parent:
                    postOrder(child, node)
                    count[node] += count[child]
                    res[node] += res[child] + count[child]
        
        def preOrder(node, parent):
            for child in graph[node]:
                if child != parent:
                    res[child] = res[node] - count[child] + (n - count[child])
                    preOrder(child, node)
        
        postOrder(0, -1)
        preOrder(0, -1)

        return res
