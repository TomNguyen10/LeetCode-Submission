class Solution:
    def longestPalindrome(self, s: str) -> int:
        st = set()
        res = 0
        for c in s:
            if c in st:
                res += 1
                st.remove(c)
            else:
                st.add(c)
        
        if st:
            return res * 2 + 1
        return res * 2
