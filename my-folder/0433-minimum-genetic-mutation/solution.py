class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if not bank or endGene not in bank:
            return -1
        
        char = ['A', 'C', 'G', 'T']
        visited = set()
        res = 0
        q = deque([startGene])
        visited.add(startGene)

        while q:
            size = len(q)
            for _ in range(size):
                currGene = q.popleft()
                if currGene == endGene:
                    return res
                for i in range(len(currGene)):
                    original = currGene[i]
                    for c in char:
                        if c != original:
                            nextGene = currGene[:i] + c + currGene[i+1:]
                            if nextGene in bank and nextGene not in visited:
                                q.append(nextGene)
                                visited.add(nextGene)
            
            res += 1
        
        return -1


