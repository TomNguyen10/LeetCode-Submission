class Solution:
    def minOperations(self, logs: List[str]) -> int:
        current = 0
        for log in logs:
            if log == "../":
                current = max(current-1, 0)
            elif log == "./":
                continue
            else:
                current += 1
        return current
