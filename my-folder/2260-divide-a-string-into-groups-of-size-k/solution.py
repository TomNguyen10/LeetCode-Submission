class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        groups = []
        n = len(s)

        for i in range(0, n, k):
            group = s[i:i + k]
            while len(group) < k:
                group += fill
            groups.append(group)

        return groups 
