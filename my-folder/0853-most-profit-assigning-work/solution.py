class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        projects = sorted(zip(profit, difficulty))
        worker = sorted(worker)
        res = 0

        for i in range(len(projects) - 1, -1, -1):
            pro, diff = projects[i]
            while worker and worker[-1] >= diff:
                res += pro
                worker.pop()
        
        return res
