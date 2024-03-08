class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = {}

        res = 0

        for num in answers:
            if num == 0:
                res += 1
                continue
            
            if num not in dic:
                dic[num] = 0
                res += num + 1
            
            else:
                val = dic[num]
                dic[num] = val + 1
                if dic[num] == num:
                    dic.pop(num)
        
        return res
