class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(num):
            if num == 0:
                return mapping[0]
            q = deque([])
            while num > 0:
                mod = num % 10
                q.appendleft(mapping[mod])
                num //= 10
            res = 0
            for digit in q:
                res = res * 10 + digit
            return res
        
        dic = [(num, convert(num)) for num in nums]
        
        sorted_dic = sorted(dic, key=lambda x: x[1])

        return [num for num, _ in sorted_dic]
