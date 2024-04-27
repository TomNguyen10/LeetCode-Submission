class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = letters[0]
        left = 0
        right = len(letters) - 1
        while left < right:
            mid = (left + right) // 2
            if ord(letters[mid]) <= ord(target):
                left = mid + 1
            else:
                right = mid
        if ord(letters[right]) - ord(target) <= 0:
            return res
        return letters[right]
