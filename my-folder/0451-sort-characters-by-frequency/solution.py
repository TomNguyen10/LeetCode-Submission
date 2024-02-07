class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        arr = [[] for _ in range(len(s) + 1)]
        for k in dic.keys():
            freq = dic[k]
            arr[freq].append(k)
        res = ''
        for i in range(len(arr)-1, 0, -1):
            if not arr[i]:
                continue
            for c in arr[i]:
                add = i * c
                res += add
        return res
