class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dic = defaultdict(list)
        max_min = 0
        
        for log in logs:
            id, minute = log  
            max_min = max(max_min, minute) 
            if id not in dic:
                dic[id] = []
            if minute not in dic[id]:
                dic[id].append(minute)

        res = [0] * k  
        for key, value in dic.items():
            arr_len = len(value)
            res[arr_len - 1] += 1

        return res
