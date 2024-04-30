class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        curr = 0
        count = 0
        for num in nums:
            curr += num
            count += dic[curr - k]
            dic[curr] += 1
        return count
