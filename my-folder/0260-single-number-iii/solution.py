class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorResult = 0
        for num in nums:
            xorResult ^= num
        
        xorResult &= -xorResult

        res = [0, 0]

        for num in nums:
            if num & xorResult == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        
        return res
        
