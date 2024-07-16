class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = defaultdict(int)
        for i in range(len(s) - 9):
            print(i)
            sub = s[i:i+10]
            dic[sub] += 1
        res = [key for key, val in dic.items() if val > 1]

        return res 
