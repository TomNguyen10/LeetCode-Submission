class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        table = defaultdict(int)

        for c in arr:
            table[c] += 1
        
        for key, val in table.items():
            if val == 1:
                if k == 1:
                    return key
                k -= 1
        
        return ""
