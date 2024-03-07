class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = [-1] * 2
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr = numbers[left] + numbers[right]

            if curr == target:
                res[0] = left+1
                res[1] = right+1
                break
            
            elif curr < target:
                left += 1

            else:
                right -= 1
            
        return res
