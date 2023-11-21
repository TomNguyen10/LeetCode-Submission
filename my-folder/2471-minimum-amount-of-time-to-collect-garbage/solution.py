class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total, count = 0, 0
        last = {}
        last['G'], last['P'], last['M'] = 0, 0, 0
        for i in range(len(garbage)):
            s = garbage[i]
            count += len(s)
            for c in s:
                last[c] = total
            if i < len(travel):
                total += travel[i]
        res = count + last['G'] + last['P'] + last['M']
        return res
                
        



        
