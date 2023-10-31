class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first = second = maxsize
        for num in prices:
            if first > num:
                second = first
                first = num
            elif second > num:
                second = num
        min = first + second
        return money if min > money else money - min
