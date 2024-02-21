class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        start = timeSeries[0]
        end = timeSeries[0] + duration
        for i in range(1, len(timeSeries)):
            if timeSeries[i] > end:
                res += end - start
                start = timeSeries[i]
            end = timeSeries[i] + duration
        res += end - start
        return res
