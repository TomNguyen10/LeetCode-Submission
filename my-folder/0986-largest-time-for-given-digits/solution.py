class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        def permutations(arr):
            if len(arr) == 1:
                return [arr]
            else:
                result = []
                for i in range(len(arr)):
                    current = arr[i]
                    remaining = arr[:i] + arr[i+1:]
                    for perm in permutations(remaining):
                        result.append([current] + perm)
                return result
        perms = permutations(arr)
    
        max_time = ""
        for perm in perms:
            hour = perm[0] * 10 + perm[1]
            minute = perm[2] * 10 + perm[3]
        
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                time_str = "{:02d}:{:02d}".format(hour, minute)
                if time_str > max_time:
                    max_time = time_str
    
        return max_time
