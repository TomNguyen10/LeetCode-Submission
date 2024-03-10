class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res  = []

        start, end = nums[0], nums[0]

        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                if start == end:
                    res.append(str(end))
                else:
                    add = str(start) + "->" + str(end)
                    res.append(add)
                start = num
                end = num

        if start == end:
            res.append(str(end))
        else:
            res.append(str(start) + "->" + str(end))

        return res
