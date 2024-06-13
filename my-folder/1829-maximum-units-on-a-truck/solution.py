class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        max_val = 0
        for i in range(len(boxTypes)):
            max_val = max(max_val, boxTypes[i][1])
        
        bucket = [0] * (max_val + 1)

        for box, unit in boxTypes:
            bucket[unit] += box
        
        boxes = 0
        units = 0

        for i in range(max_val, -1, -1):
            while bucket[i] > 0 and boxes < truckSize:
                units += i
                bucket[i] -= 1
                boxes += 1
        
        return units

