class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        hash_set = set()
        while right < len(s):
            if s[right] not in hash_set:
                hash_set.add(s[right])
                res = max(res, right - left + 1)
                right += 1
            else:
                hash_set.remove(s[left])
                left += 1
        return res
