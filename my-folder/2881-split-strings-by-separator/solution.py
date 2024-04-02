class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            arr = word.split(separator)
            for char in arr:
                if char != "":
                    res.append(char)
        return res
