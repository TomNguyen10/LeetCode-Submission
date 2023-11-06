class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        char = {}
        for c in s:
            if c in char:
                char[c] += 1
            else:
                char[c] = 1
        frequencies = set(char.values())
        return len(frequencies) == 1
            

