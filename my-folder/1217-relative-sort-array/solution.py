class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_val = max(arr1)
        count = [0] * (max_val + 1)

        for num in arr1:
            count[num] += 1
        
        i = 0

        for num in arr2:
            while count[num] > 0:
                arr1[i] = num
                i += 1
                count[num] -= 1
        
        for j in range(len(count)):
            while count[j] > 0:
                arr1[i] = j
                i += 1
                count[j] -= 1
        
        return arr1
