class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):
            count = 0
            for letter in counter:
                if counter[letter] > 0:
                    counter[letter] -= 1
                    count += 1 + backtrack(counter)
                    counter[letter] += 1
            return count
        
        counter = Counter(tiles)
        res = backtrack(counter)
        return res
