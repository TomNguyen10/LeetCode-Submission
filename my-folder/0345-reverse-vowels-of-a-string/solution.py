class Solution:
    def reverseVowels(self, s: str) -> str:
        hs = set()
        hs.add('a')
        hs.add('e')
        hs.add('i')
        hs.add('o')
        hs.add('u')
        hs.add('A')
        hs.add('E')
        hs.add('I')
        hs.add('O')
        hs.add('U')

        p1 = 0
        p2 = len(s) - 1

        s = list(s)

        while p1 < p2:
            while p1 < p2 and s[p1] not in hs:
                p1 += 1
            while p1 < p2 and s[p2] not in hs:
                p2 -= 1
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1
        
        return "".join(s)
