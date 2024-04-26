class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curr = 0
        for i in range(k):
            curr += arr[i]
        left = 0
        if curr / k >= threshold:
            res += 1
        for right in range(k, len(arr)):
            curr -= arr[left]
            left += 1
            curr += arr[right]
            print(curr / k)
            if curr / k >= threshold:
                res += 1
        return res

