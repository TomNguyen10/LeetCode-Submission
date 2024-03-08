class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        arr = [0] * 26

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            arr[ord('a') - ord(c1)] += 1
            arr[ord('a') - ord(c2)] -= 1
        
        for num in arr:
            if num != 0:
                return False
        
        return True
