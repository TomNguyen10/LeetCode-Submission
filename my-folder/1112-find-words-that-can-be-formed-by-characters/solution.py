class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        alphabet = [0] * 26
        for c in chars:
            alphabet[ord(c) - ord('a')] += 1
        res = 0
        for word in words:
            rep = [0] * 26
            isGood = True
            for c in word:
                pos = ord(c) - ord('a')
                rep[pos] += 1
                if rep[pos] > alphabet[pos]:
                    isGood = False
                    break
            if isGood:
                res += len(word)
        return res


        
