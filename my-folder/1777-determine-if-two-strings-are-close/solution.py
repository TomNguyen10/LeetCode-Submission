class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26
        for c in word1:
            freq1[ord(c) - ord('a')] += 1
        for c in word2:
            freq2[ord(c) - ord('a')] += 1
        hash_map = {}
        for i in range (0, 26):
            w1, w2 = freq1[i], freq2[i]
            if w1 == 0 and w1 != 0 or w1 != 0 and w2 == 0:
                return False
        for freq in freq1:
            if freq not in hash_map:
                hash_map[freq] = 0
            hash_map[freq] += 1
        for freq in freq2:
            if freq not in hash_map:
                hash_map[freq] = 0
            hash_map[freq] -= 1
        for value in hash_map.values():
            if value != 0:
                return False
        return True
