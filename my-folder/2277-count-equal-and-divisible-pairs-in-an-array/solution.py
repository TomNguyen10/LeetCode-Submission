class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic = dict()
        count = 0
        for i in range(len(nums)):
            num = nums[i]
            if num not in dic:
                dic[num] = [i]
            else:
                arr = dic[num]
                for n in arr:
                    if (i * n) % k == 0:
                        count += 1
                arr.append(i)
        return count
