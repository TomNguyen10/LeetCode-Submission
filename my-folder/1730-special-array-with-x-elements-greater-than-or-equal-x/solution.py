class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        freq = [0] * (n+1)

        for num in nums:
            freq[min(n, num)] += 1

        curr = 0

        for i in range(n, 0, -1):
            curr += freq[i]
            if i == curr:
                return i

        return -1        
