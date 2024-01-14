class Solution:
    def digitCount(self, num: str) -> bool:
        freq = [0] * 10
        for c in num:
            number = int(c)
            freq[number] += 1
        for i in range(len(num)):
            digit = i
            occurs = freq[digit]
            comp = int(num[i])
            if occurs != comp:
                return False
        return True

