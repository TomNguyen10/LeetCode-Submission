class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        hash = set(nums)
        count = 0
        for num in hash:
            if num + diff in hash and num + diff*2 in hash:
                count += 1
        return count

        
