class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        max_val = max(nums)
        bucket = [0] * (max_val + len(nums))
        for num in nums:
            bucket[num] += 1
        
        q = deque([])

        res = 0

        print(bucket)

        for i in range(len(bucket)):
            while bucket[i] > 1:
                q.append(i)
                bucket[i] -= 1
            if bucket[i] == 0 and q:
                prev = q.popleft()
                res += i - prev
        
        return res
