class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s = sentence.strip()
        arr = s.split(" ")
        for i in range(len(arr)):
            st = arr[i]
            if (st.startswith(searchWord)):
                return i + 1
        return -1
