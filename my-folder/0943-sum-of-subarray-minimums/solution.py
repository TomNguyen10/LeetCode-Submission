class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''
        For each number in the array, we gonna consider all the subarray to the left and count how many it will be the mean
        If we find a previous less or equal value on its left A[j] <= A[i] then we know that result[i] = result[j] + A[i] * (i-j). Therefore we need an array to keep track of all previous result.
        We need a stack to track all the previous smaller number of A[i] to its left
        Loop through the array, while the top of the stack is larger than A[i], pop it out, till we meet number at j index
        Apply the formula res[i] = res[j] + (i-j) * A[i]
        Append i to the stack
        Return the sum of the res array
        '''
        stack = []
        res = [0] * len(arr)
        MOD = 10**9 + 7

        for i in range(len(arr)):
            num = arr[i]
            while stack and arr[stack[-1]] > num:
                stack.pop()
            j = stack[-1] if stack else -1 
            numJ = res[j] if j != -1 else 0
            res[i] = res[j] + (i - j) * num
            stack.append(i)

        return sum(res) % MOD
