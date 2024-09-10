class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefix(str1, str2):
            n = len(str1)
            return str2[:n] == str1 and str2[-n:] == str1
        
        res = 0
        for i in range(len(words) - 1):
            for j in range(i+1, len(words)):
                res += isPrefix(words[i], words[j])

        return res
