class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        ans = ""

        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return ans
            ans += strs[0][i]
        
        return ans
