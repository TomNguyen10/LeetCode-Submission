class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        count = 0
        cum_sum = 0
        dic[0] = 1

        for num in nums:
            cum_sum += num
            count += dic[cum_sum - k]
            dic[cum_sum] += 1
        
        return count
