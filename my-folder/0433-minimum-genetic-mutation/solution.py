class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        hash_set = set(bank)
        if not hash_set or endGene not in hash_set:
            return -1
        
        char = ['A', 'C', 'G', 'T']
        visited = set()
        res = 0
        q = deque([startGene])
        visited.add(startGene)

        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                if curr == endGene:
                    return res
                for i in range(len(curr)):
                    original = curr[i]
                    for c in char:
                        if c != original:  
                            next_gene = curr[:i] + c + curr[i+1:]
                            if next_gene in hash_set and next_gene not in visited:
                                q.append(next_gene)
                                visited.add(next_gene)
            res += 1
        
        return -1

