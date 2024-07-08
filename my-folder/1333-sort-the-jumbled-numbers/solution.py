class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(num, mapping):
            if num == 0:
                return mapping[0]
            q = deque()
            while num > 0:
                mod = num % 10
                q.appendleft(mapping[mod])
                num //= 10

            res = 0
            for digit in q:
                res = res * 10 + digit
            return res
        
        # Create a list of tuples where each tuple is (original number, mapped value)
        mapped_nums = [(num, convert(num, mapping)) for num in nums]
        
        # Sort based on the mapped values while maintaining relative order for equal mapped values
        mapped_nums.sort(key=lambda x: x[1])
        
        # Extract and return the original numbers in the sorted order
        return [num for num, _ in mapped_nums]
