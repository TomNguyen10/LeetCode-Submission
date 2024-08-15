class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        arr = list(hamsters)
        res = 0
        for i in range(len(arr)):
            if arr[i] == 'H':
                if i > 0 and arr[i-1] == 'F':
                    continue
                if i < len(arr) - 1 and arr[i+1] == '.':
                    arr[i+1] = 'F'
                    res += 1
                elif i > 0 and arr[i-1] == '.':
                    arr[i-1] = 'F'
                    res += 1
                else:
                    return -1
        return res
