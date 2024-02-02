class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        q = deque(range(1, 10))
        res = []
        while q:
            num = q.popleft()
            if low <= num <= high:
                res.append(num)
            add = num % 10
            if add < 9:
                q.append(num*10 + add + 1)
        return res
