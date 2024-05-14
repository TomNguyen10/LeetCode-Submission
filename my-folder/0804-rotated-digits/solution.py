class Solution:
    def rotatedDigits(self, n: int) -> int:
        def is_good_number(x):
            rotate_map = {'0': '0', '1': '1', '2': '5', '5': '2', '6': '9', '9': '6', '8': '8'}

            x_str = str(x)
            rotated_str = ''
    
            for digit in x_str:
                if digit not in rotate_map:
                    return False  
                rotated_str += rotate_map[digit]

            return rotated_str != x_str
    
        count = 0
        for i in range(1, n + 1):
            if is_good_number(i):
                count += 1
        return count
